# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=generated/nirfmxnr/nirfmxnr.proto sha256=1ae6f9f150e06699d55df858034d4251f5203fb887299168b38a6aa7e8bb19be bytes=181021 -->
## FILE: generated/nirfmxnr/nirfmxnr.proto

- repository: `ni/grpc-device`
- source_path: `generated/nirfmxnr/nirfmxnr.proto`
- sha256: `1ae6f9f150e06699d55df858034d4251f5203fb887299168b38a6aa7e8bb19be`
- bytes: 181021

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-RFMXNR API metadata version 26.5.0
//---------------------------------------------------------------------
// Proto file for the NI-RFMXNR Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.nirfmxnr";
option java_outer_classname = "NiRFmxNR";
option csharp_namespace = "NationalInstruments.Grpc.NiRFmxNR";

package nirfmxnr_grpc;

import "nidevice.proto";
import "session.proto";

service NiRFmxNR {
  rpc ACPCfgAveraging(ACPCfgAveragingRequest) returns (ACPCfgAveragingResponse);
  rpc ACPCfgMeasurementMethod(ACPCfgMeasurementMethodRequest) returns (ACPCfgMeasurementMethodResponse);
  rpc ACPCfgNoiseCompensationEnabled(ACPCfgNoiseCompensationEnabledRequest) returns (ACPCfgNoiseCompensationEnabledResponse);
  rpc ACPCfgNumberOfENDCOffsets(ACPCfgNumberOfENDCOffsetsRequest) returns (ACPCfgNumberOfENDCOffsetsResponse);
  rpc ACPCfgNumberOfEUTRAOffsets(ACPCfgNumberOfEUTRAOffsetsRequest) returns (ACPCfgNumberOfEUTRAOffsetsResponse);
  rpc ACPCfgNumberOfNROffsets(ACPCfgNumberOfNROffsetsRequest) returns (ACPCfgNumberOfNROffsetsResponse);
  rpc ACPCfgNumberOfUTRAOffsets(ACPCfgNumberOfUTRAOffsetsRequest) returns (ACPCfgNumberOfUTRAOffsetsResponse);
  rpc ACPCfgPowerUnits(ACPCfgPowerUnitsRequest) returns (ACPCfgPowerUnitsResponse);
  rpc ACPCfgRBWFilter(ACPCfgRBWFilterRequest) returns (ACPCfgRBWFilterResponse);
  rpc ACPCfgSweepTime(ACPCfgSweepTimeRequest) returns (ACPCfgSweepTimeResponse);
  rpc ACPFetchAbsolutePowersTrace(ACPFetchAbsolutePowersTraceRequest) returns (ACPFetchAbsolutePowersTraceResponse);
  rpc ACPFetchComponentCarrierMeasurement(ACPFetchComponentCarrierMeasurementRequest) returns (ACPFetchComponentCarrierMeasurementResponse);
  rpc ACPFetchComponentCarrierMeasurementArray(ACPFetchComponentCarrierMeasurementArrayRequest) returns (ACPFetchComponentCarrierMeasurementArrayResponse);
  rpc ACPFetchOffsetMeasurement(ACPFetchOffsetMeasurementRequest) returns (ACPFetchOffsetMeasurementResponse);
  rpc ACPFetchOffsetMeasurementArray(ACPFetchOffsetMeasurementArrayRequest) returns (ACPFetchOffsetMeasurementArrayResponse);
  rpc ACPFetchRelativePowersTrace(ACPFetchRelativePowersTraceRequest) returns (ACPFetchRelativePowersTraceResponse);
  rpc ACPFetchSpectrum(ACPFetchSpectrumRequest) returns (ACPFetchSpectrumResponse);
  rpc ACPFetchSubblockMeasurement(ACPFetchSubblockMeasurementRequest) returns (ACPFetchSubblockMeasurementResponse);
  rpc ACPFetchTotalAggregatedPower(ACPFetchTotalAggregatedPowerRequest) returns (ACPFetchTotalAggregatedPowerResponse);
  rpc ACPValidateNoiseCalibrationData(ACPValidateNoiseCalibrationDataRequest) returns (ACPValidateNoiseCalibrationDataResponse);
  rpc AbortMeasurements(AbortMeasurementsRequest) returns (AbortMeasurementsResponse);
  rpc AnalyzeIQ1Waveform(AnalyzeIQ1WaveformRequest) returns (AnalyzeIQ1WaveformResponse);
  rpc AnalyzeIQ1WaveformInterleavedIQ(AnalyzeIQ1WaveformInterleavedIQRequest) returns (AnalyzeIQ1WaveformInterleavedIQResponse);
  rpc AnalyzeIQ1WaveformSplit(AnalyzeIQ1WaveformSplitRequest) returns (AnalyzeIQ1WaveformSplitResponse);
  rpc AnalyzeNWaveformsIQ(AnalyzeNWaveformsIQRequest) returns (AnalyzeNWaveformsIQResponse);
  rpc AnalyzeNWaveformsIQInterleavedIQ(AnalyzeNWaveformsIQInterleavedIQRequest) returns (AnalyzeNWaveformsIQInterleavedIQResponse);
  rpc AnalyzeNWaveformsIQSplit(AnalyzeNWaveformsIQSplitRequest) returns (AnalyzeNWaveformsIQSplitResponse);
  rpc AnalyzeNWaveformsSpectrum(AnalyzeNWaveformsSpectrumRequest) returns (AnalyzeNWaveformsSpectrumResponse);
  rpc AnalyzeSpectrum1Waveform(AnalyzeSpectrum1WaveformRequest) returns (AnalyzeSpectrum1WaveformResponse);
  rpc AutoLevel(AutoLevelRequest) returns (AutoLevelResponse);
  rpc BuildBandwidthPartString(BuildBandwidthPartStringRequest) returns (BuildBandwidthPartStringResponse);
  rpc BuildCORESETClusterString(BuildCORESETClusterStringRequest) returns (BuildCORESETClusterStringResponse);
  rpc BuildCORESETString(BuildCORESETStringRequest) returns (BuildCORESETStringResponse);
  rpc BuildCarrierString(BuildCarrierStringRequest) returns (BuildCarrierStringResponse);
  rpc BuildListStepString(BuildListStepStringRequest) returns (BuildListStepStringResponse);
  rpc BuildListString(BuildListStringRequest) returns (BuildListStringResponse);
  rpc BuildOffsetString(BuildOffsetStringRequest) returns (BuildOffsetStringResponse);
  rpc BuildPDCCHString(BuildPDCCHStringRequest) returns (BuildPDCCHStringResponse);
  rpc BuildPDSCHClusterString(BuildPDSCHClusterStringRequest) returns (BuildPDSCHClusterStringResponse);
  rpc BuildPDSCHString(BuildPDSCHStringRequest) returns (BuildPDSCHStringResponse);
  rpc BuildPUSCHClusterString(BuildPUSCHClusterStringRequest) returns (BuildPUSCHClusterStringResponse);
  rpc BuildPUSCHString(BuildPUSCHStringRequest) returns (BuildPUSCHStringResponse);
  rpc BuildSignalString(BuildSignalStringRequest) returns (BuildSignalStringResponse);
  rpc BuildSubblockString(BuildSubblockStringRequest) returns (BuildSubblockStringResponse);
  rpc BuildUserString(BuildUserStringRequest) returns (BuildUserStringResponse);
  rpc CHPCfgAveraging(CHPCfgAveragingRequest) returns (CHPCfgAveragingResponse);
  rpc CHPCfgRBWFilter(CHPCfgRBWFilterRequest) returns (CHPCfgRBWFilterResponse);
  rpc CHPCfgSweepTime(CHPCfgSweepTimeRequest) returns (CHPCfgSweepTimeResponse);
  rpc CHPFetchComponentCarrierMeasurement(CHPFetchComponentCarrierMeasurementRequest) returns (CHPFetchComponentCarrierMeasurementResponse);
  rpc CHPFetchComponentCarrierMeasurementArray(CHPFetchComponentCarrierMeasurementArrayRequest) returns (CHPFetchComponentCarrierMeasurementArrayResponse);
  rpc CHPFetchSpectrum(CHPFetchSpectrumRequest) returns (CHPFetchSpectrumResponse);
  rpc CHPFetchSubblockPower(CHPFetchSubblockPowerRequest) returns (CHPFetchSubblockPowerResponse);
  rpc CHPFetchTotalAggregatedPower(CHPFetchTotalAggregatedPowerRequest) returns (CHPFetchTotalAggregatedPowerResponse);
  rpc CHPValidateNoiseCalibrationData(CHPValidateNoiseCalibrationDataRequest) returns (CHPValidateNoiseCalibrationDataResponse);
  rpc CfgDigitalEdgeTrigger(CfgDigitalEdgeTriggerRequest) returns (CfgDigitalEdgeTriggerResponse);
  rpc CfgExternalAttenuation(CfgExternalAttenuationRequest) returns (CfgExternalAttenuationResponse);
  rpc CfgFrequency(CfgFrequencyRequest) returns (CfgFrequencyResponse);
  rpc CfgFrequencyReference(CfgFrequencyReferenceRequest) returns (CfgFrequencyReferenceResponse);
  rpc CfgIQPowerEdgeTrigger(CfgIQPowerEdgeTriggerRequest) returns (CfgIQPowerEdgeTriggerResponse);
  rpc CfgMechanicalAttenuation(CfgMechanicalAttenuationRequest) returns (CfgMechanicalAttenuationResponse);
  rpc CfgRF(CfgRFRequest) returns (CfgRFResponse);
  rpc CfgRFAttenuation(CfgRFAttenuationRequest) returns (CfgRFAttenuationResponse);
  rpc CfgReferenceLevel(CfgReferenceLevelRequest) returns (CfgReferenceLevelResponse);
  rpc CfgSelectedPortsMultiple(CfgSelectedPortsMultipleRequest) returns (CfgSelectedPortsMultipleResponse);
  rpc CfgSoftwareEdgeTrigger(CfgSoftwareEdgeTriggerRequest) returns (CfgSoftwareEdgeTriggerResponse);
  rpc CfggNodeBCategory(CfggNodeBCategoryRequest) returns (CfggNodeBCategoryResponse);
  rpc CheckMeasurementStatus(CheckMeasurementStatusRequest) returns (CheckMeasurementStatusResponse);
  rpc ClearAllNamedResults(ClearAllNamedResultsRequest) returns (ClearAllNamedResultsResponse);
  rpc ClearNamedResult(ClearNamedResultRequest) returns (ClearNamedResultResponse);
  rpc ClearNoiseCalibrationDatabase(ClearNoiseCalibrationDatabaseRequest) returns (ClearNoiseCalibrationDatabaseResponse);
  rpc CloneSignalConfiguration(CloneSignalConfigurationRequest) returns (CloneSignalConfigurationResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc Commit(CommitRequest) returns (CommitResponse);
  rpc CreateList(CreateListRequest) returns (CreateListResponse);
  rpc CreateListStep(CreateListStepRequest) returns (CreateListStepResponse);
  rpc CreateSignalConfiguration(CreateSignalConfigurationRequest) returns (CreateSignalConfigurationResponse);
  rpc DeleteList(DeleteListRequest) returns (DeleteListResponse);
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
  rpc LoadFromGenerationConfigurationFile(LoadFromGenerationConfigurationFileRequest) returns (LoadFromGenerationConfigurationFileResponse);
  rpc ModAccAutoLevel(ModAccAutoLevelRequest) returns (ModAccAutoLevelResponse);
  rpc ModAccCfgMeasurementMode(ModAccCfgMeasurementModeRequest) returns (ModAccCfgMeasurementModeResponse);
  rpc ModAccCfgNoiseCompensationEnabled(ModAccCfgNoiseCompensationEnabledRequest) returns (ModAccCfgNoiseCompensationEnabledResponse);
  rpc ModAccCfgReferenceWaveform(ModAccCfgReferenceWaveformRequest) returns (ModAccCfgReferenceWaveformResponse);
  rpc ModAccCfgReferenceWaveformInterleavedIQ(ModAccCfgReferenceWaveformInterleavedIQRequest) returns (ModAccCfgReferenceWaveformInterleavedIQResponse);
  rpc ModAccCfgReferenceWaveformSplit(ModAccCfgReferenceWaveformSplitRequest) returns (ModAccCfgReferenceWaveformSplitResponse);
  rpc ModAccClearNoiseCalibrationDatabase(ModAccClearNoiseCalibrationDatabaseRequest) returns (ModAccClearNoiseCalibrationDatabaseResponse);
  rpc ModAccFetchCompositeEVM(ModAccFetchCompositeEVMRequest) returns (ModAccFetchCompositeEVMResponse);
  rpc ModAccFetchFrequencyErrorMean(ModAccFetchFrequencyErrorMeanRequest) returns (ModAccFetchFrequencyErrorMeanResponse);
  rpc ModAccFetchFrequencyErrorPerSlotMaximumTrace(ModAccFetchFrequencyErrorPerSlotMaximumTraceRequest) returns (ModAccFetchFrequencyErrorPerSlotMaximumTraceResponse);
  rpc ModAccFetchIQGainImbalancePerSubcarrierMeanTrace(ModAccFetchIQGainImbalancePerSubcarrierMeanTraceRequest) returns (ModAccFetchIQGainImbalancePerSubcarrierMeanTraceResponse);
  rpc ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace(ModAccFetchIQQuadratureErrorPerSubcarrierMeanTraceRequest) returns (ModAccFetchIQQuadratureErrorPerSubcarrierMeanTraceResponse);
  rpc ModAccFetchInBandEmissionTrace(ModAccFetchInBandEmissionTraceRequest) returns (ModAccFetchInBandEmissionTraceResponse);
  rpc ModAccFetchPBCHDMRSConstellationTrace(ModAccFetchPBCHDMRSConstellationTraceRequest) returns (ModAccFetchPBCHDMRSConstellationTraceResponse);
  rpc ModAccFetchPBCHDMRSConstellationTraceInterleavedIQ(ModAccFetchPBCHDMRSConstellationTraceInterleavedIQRequest) returns (ModAccFetchPBCHDMRSConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchPBCHDMRSConstellationTraceSplit(ModAccFetchPBCHDMRSConstellationTraceSplitRequest) returns (ModAccFetchPBCHDMRSConstellationTraceSplitResponse);
  rpc ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace(ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTraceRequest) returns (ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTraceResponse);
  rpc ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace(ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTraceRequest) returns (ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTraceResponse);
  rpc ModAccFetchPBCHDataConstellationTrace(ModAccFetchPBCHDataConstellationTraceRequest) returns (ModAccFetchPBCHDataConstellationTraceResponse);
  rpc ModAccFetchPBCHDataConstellationTraceInterleavedIQ(ModAccFetchPBCHDataConstellationTraceInterleavedIQRequest) returns (ModAccFetchPBCHDataConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchPBCHDataConstellationTraceSplit(ModAccFetchPBCHDataConstellationTraceSplitRequest) returns (ModAccFetchPBCHDataConstellationTraceSplitResponse);
  rpc ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTrace(ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTraceRequest) returns (ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTraceResponse);
  rpc ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace(ModAccFetchPBCHDataRMSEVMPerSymbolMeanTraceRequest) returns (ModAccFetchPBCHDataRMSEVMPerSymbolMeanTraceResponse);
  rpc ModAccFetchPDSCH1024QAMConstellationTrace(ModAccFetchPDSCH1024QAMConstellationTraceRequest) returns (ModAccFetchPDSCH1024QAMConstellationTraceResponse);
  rpc ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQ(ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQRequest) returns (ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchPDSCH1024QAMConstellationTraceSplit(ModAccFetchPDSCH1024QAMConstellationTraceSplitRequest) returns (ModAccFetchPDSCH1024QAMConstellationTraceSplitResponse);
  rpc ModAccFetchPDSCH16QAMConstellationTrace(ModAccFetchPDSCH16QAMConstellationTraceRequest) returns (ModAccFetchPDSCH16QAMConstellationTraceResponse);
  rpc ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQ(ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQRequest) returns (ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchPDSCH16QAMConstellationTraceSplit(ModAccFetchPDSCH16QAMConstellationTraceSplitRequest) returns (ModAccFetchPDSCH16QAMConstellationTraceSplitResponse);
  rpc ModAccFetchPDSCH256QAMConstellationTrace(ModAccFetchPDSCH256QAMConstellationTraceRequest) returns (ModAccFetchPDSCH256QAMConstellationTraceResponse);
  rpc ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQ(ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQRequest) returns (ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchPDSCH256QAMConstellationTraceSplit(ModAccFetchPDSCH256QAMConstellationTraceSplitRequest) returns (ModAccFetchPDSCH256QAMConstellationTraceSplitResponse);
  rpc ModAccFetchPDSCH4096QAMConstellationTrace(ModAccFetchPDSCH4096QAMConstellationTraceRequest) returns (ModAccFetchPDSCH4096QAMConstellationTraceResponse);
  rpc ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQ(ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQRequest) returns (ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchPDSCH4096QAMConstellationTraceSplit(ModAccFetchPDSCH4096QAMConstellationTraceSplitRequest) returns (ModAccFetchPDSCH4096QAMConstellationTraceSplitResponse);
  rpc ModAccFetchPDSCH64QAMConstellationTrace(ModAccFetchPDSCH64QAMConstellationTraceRequest) returns (ModAccFetchPDSCH64QAMConstellationTraceResponse);
  rpc ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQ(ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQRequest) returns (ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchPDSCH64QAMConstellationTraceSplit(ModAccFetchPDSCH64QAMConstellationTraceSplitRequest) returns (ModAccFetchPDSCH64QAMConstellationTraceSplitResponse);
  rpc ModAccFetchPDSCH8PSKConstellationTrace(ModAccFetchPDSCH8PSKConstellationTraceRequest) returns (ModAccFetchPDSCH8PSKConstellationTraceResponse);
  rpc ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQ(ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQRequest) returns (ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchPDSCH8PSKConstellationTraceSplit(ModAccFetchPDSCH8PSKConstellationTraceSplitRequest) returns (ModAccFetchPDSCH8PSKConstellationTraceSplitResponse);
  rpc ModAccFetchPDSCHDMRSConstellationTrace(ModAccFetchPDSCHDMRSConstellationTraceRequest) returns (ModAccFetchPDSCHDMRSConstellationTraceResponse);
  rpc ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQ(ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQRequest) returns (ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchPDSCHDMRSConstellationTraceSplit(ModAccFetchPDSCHDMRSConstellationTraceSplitRequest) returns (ModAccFetchPDSCHDMRSConstellationTraceSplitResponse);
  rpc ModAccFetchPDSCHDataConstellationTrace(ModAccFetchPDSCHDataConstellationTraceRequest) returns (ModAccFetchPDSCHDataConstellationTraceResponse);
  rpc ModAccFetchPDSCHDataConstellationTraceInterleavedIQ(ModAccFetchPDSCHDataConstellationTraceInterleavedIQRequest) returns (ModAccFetchPDSCHDataConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchPDSCHDataConstellationTraceSplit(ModAccFetchPDSCHDataConstellationTraceSplitRequest) returns (ModAccFetchPDSCHDataConstellationTraceSplitResponse);
  rpc ModAccFetchPDSCHDemodulatedBits(ModAccFetchPDSCHDemodulatedBitsRequest) returns (ModAccFetchPDSCHDemodulatedBitsResponse);
  rpc ModAccFetchPDSCHPTRSConstellationTrace(ModAccFetchPDSCHPTRSConstellationTraceRequest) returns (ModAccFetchPDSCHPTRSConstellationTraceResponse);
  rpc ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQ(ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQRequest) returns (ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchPDSCHPTRSConstellationTraceSplit(ModAccFetchPDSCHPTRSConstellationTraceSplitRequest) returns (ModAccFetchPDSCHPTRSConstellationTraceSplitResponse);
  rpc ModAccFetchPDSCHQPSKConstellationTrace(ModAccFetchPDSCHQPSKConstellationTraceRequest) returns (ModAccFetchPDSCHQPSKConstellationTraceResponse);
  rpc ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQ(ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQRequest) returns (ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchPDSCHQPSKConstellationTraceSplit(ModAccFetchPDSCHQPSKConstellationTraceSplitRequest) returns (ModAccFetchPDSCHQPSKConstellationTraceSplitResponse);
  rpc ModAccFetchPSSConstellationTrace(ModAccFetchPSSConstellationTraceRequest) returns (ModAccFetchPSSConstellationTraceResponse);
  rpc ModAccFetchPSSConstellationTraceInterleavedIQ(ModAccFetchPSSConstellationTraceInterleavedIQRequest) returns (ModAccFetchPSSConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchPSSConstellationTraceSplit(ModAccFetchPSSConstellationTraceSplitRequest) returns (ModAccFetchPSSConstellationTraceSplitResponse);
  rpc ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace(ModAccFetchPSSRMSEVMPerSubcarrierMeanTraceRequest) returns (ModAccFetchPSSRMSEVMPerSubcarrierMeanTraceResponse);
  rpc ModAccFetchPSSRMSEVMPerSymbolMeanTrace(ModAccFetchPSSRMSEVMPerSymbolMeanTraceRequest) returns (ModAccFetchPSSRMSEVMPerSymbolMeanTraceResponse);
  rpc ModAccFetchPUSCHDMRSConstellationTrace(ModAccFetchPUSCHDMRSConstellationTraceRequest) returns (ModAccFetchPUSCHDMRSConstellationTraceResponse);
  rpc ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQ(ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQRequest) returns (ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchPUSCHDMRSConstellationTraceSplit(ModAccFetchPUSCHDMRSConstellationTraceSplitRequest) returns (ModAccFetchPUSCHDMRSConstellationTraceSplitResponse);
  rpc ModAccFetchPUSCHDataConstellationTrace(ModAccFetchPUSCHDataConstellationTraceRequest) returns (ModAccFetchPUSCHDataConstellationTraceResponse);
  rpc ModAccFetchPUSCHDataConstellationTraceInterleavedIQ(ModAccFetchPUSCHDataConstellationTraceInterleavedIQRequest) returns (ModAccFetchPUSCHDataConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchPUSCHDataConstellationTraceSplit(ModAccFetchPUSCHDataConstellationTraceSplitRequest) returns (ModAccFetchPUSCHDataConstellationTraceSplitResponse);
  rpc ModAccFetchPUSCHDemodulatedBits(ModAccFetchPUSCHDemodulatedBitsRequest) returns (ModAccFetchPUSCHDemodulatedBitsResponse);
  rpc ModAccFetchPUSCHPTRSConstellationTrace(ModAccFetchPUSCHPTRSConstellationTraceRequest) returns (ModAccFetchPUSCHPTRSConstellationTraceResponse);
  rpc ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQ(ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQRequest) returns (ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchPUSCHPTRSConstellationTraceSplit(ModAccFetchPUSCHPTRSConstellationTraceSplitRequest) returns (ModAccFetchPUSCHPTRSConstellationTraceSplitResponse);
  rpc ModAccFetchPUSCHPhaseOffsetTrace(ModAccFetchPUSCHPhaseOffsetTraceRequest) returns (ModAccFetchPUSCHPhaseOffsetTraceResponse);
  rpc ModAccFetchPeakEVMHighPerSymbolMaximumTrace(ModAccFetchPeakEVMHighPerSymbolMaximumTraceRequest) returns (ModAccFetchPeakEVMHighPerSymbolMaximumTraceResponse);
  rpc ModAccFetchPeakEVMLowPerSymbolMaximumTrace(ModAccFetchPeakEVMLowPerSymbolMaximumTraceRequest) returns (ModAccFetchPeakEVMLowPerSymbolMaximumTraceResponse);
  rpc ModAccFetchPeakEVMPerSlotMaximumTrace(ModAccFetchPeakEVMPerSlotMaximumTraceRequest) returns (ModAccFetchPeakEVMPerSlotMaximumTraceResponse);
  rpc ModAccFetchPeakEVMPerSubcarrierMaximumTrace(ModAccFetchPeakEVMPerSubcarrierMaximumTraceRequest) returns (ModAccFetchPeakEVMPerSubcarrierMaximumTraceResponse);
  rpc ModAccFetchPeakEVMPerSymbolMaximumTrace(ModAccFetchPeakEVMPerSymbolMaximumTraceRequest) returns (ModAccFetchPeakEVMPerSymbolMaximumTraceResponse);
  rpc ModAccFetchRMSEVMHighPerSymbolMeanTrace(ModAccFetchRMSEVMHighPerSymbolMeanTraceRequest) returns (ModAccFetchRMSEVMHighPerSymbolMeanTraceResponse);
  rpc ModAccFetchRMSEVMLowPerSymbolMeanTrace(ModAccFetchRMSEVMLowPerSymbolMeanTraceRequest) returns (ModAccFetchRMSEVMLowPerSymbolMeanTraceResponse);
  rpc ModAccFetchRMSEVMPerSlotMeanTrace(ModAccFetchRMSEVMPerSlotMeanTraceRequest) returns (ModAccFetchRMSEVMPerSlotMeanTraceResponse);
  rpc ModAccFetchRMSEVMPerSubcarrierMeanTrace(ModAccFetchRMSEVMPerSubcarrierMeanTraceRequest) returns (ModAccFetchRMSEVMPerSubcarrierMeanTraceResponse);
  rpc ModAccFetchRMSEVMPerSymbolMeanTrace(ModAccFetchRMSEVMPerSymbolMeanTraceRequest) returns (ModAccFetchRMSEVMPerSymbolMeanTraceResponse);
  rpc ModAccFetchSSSConstellationTrace(ModAccFetchSSSConstellationTraceRequest) returns (ModAccFetchSSSConstellationTraceResponse);
  rpc ModAccFetchSSSConstellationTraceInterleavedIQ(ModAccFetchSSSConstellationTraceInterleavedIQRequest) returns (ModAccFetchSSSConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchSSSConstellationTraceSplit(ModAccFetchSSSConstellationTraceSplitRequest) returns (ModAccFetchSSSConstellationTraceSplitResponse);
  rpc ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace(ModAccFetchSSSRMSEVMPerSubcarrierMeanTraceRequest) returns (ModAccFetchSSSRMSEVMPerSubcarrierMeanTraceResponse);
  rpc ModAccFetchSSSRMSEVMPerSymbolMeanTrace(ModAccFetchSSSRMSEVMPerSymbolMeanTraceRequest) returns (ModAccFetchSSSRMSEVMPerSymbolMeanTraceResponse);
  rpc ModAccFetchSpectralFlatnessTrace(ModAccFetchSpectralFlatnessTraceRequest) returns (ModAccFetchSpectralFlatnessTraceResponse);
  rpc ModAccFetchSubblockInBandEmissionTrace(ModAccFetchSubblockInBandEmissionTraceRequest) returns (ModAccFetchSubblockInBandEmissionTraceResponse);
  rpc ModAccFetchTransientPeriodLocationsTrace(ModAccFetchTransientPeriodLocationsTraceRequest) returns (ModAccFetchTransientPeriodLocationsTraceResponse);
  rpc ModAccValidateCalibrationData(ModAccValidateCalibrationDataRequest) returns (ModAccValidateCalibrationDataResponse);
  rpc OBWCfgAveraging(OBWCfgAveragingRequest) returns (OBWCfgAveragingResponse);
  rpc OBWCfgRBWFilter(OBWCfgRBWFilterRequest) returns (OBWCfgRBWFilterResponse);
  rpc OBWCfgSweepTime(OBWCfgSweepTimeRequest) returns (OBWCfgSweepTimeResponse);
  rpc OBWFetchMeasurement(OBWFetchMeasurementRequest) returns (OBWFetchMeasurementResponse);
  rpc OBWFetchSpectrum(OBWFetchSpectrumRequest) returns (OBWFetchSpectrumResponse);
  rpc PVTCfgAveraging(PVTCfgAveragingRequest) returns (PVTCfgAveragingResponse);
  rpc PVTCfgMeasurementMethod(PVTCfgMeasurementMethodRequest) returns (PVTCfgMeasurementMethodResponse);
  rpc PVTCfgOFFPowerExclusionPeriods(PVTCfgOFFPowerExclusionPeriodsRequest) returns (PVTCfgOFFPowerExclusionPeriodsResponse);
  rpc PVTFetchMeasurement(PVTFetchMeasurementRequest) returns (PVTFetchMeasurementResponse);
  rpc PVTFetchMeasurementArray(PVTFetchMeasurementArrayRequest) returns (PVTFetchMeasurementArrayResponse);
  rpc PVTFetchSignalPowerTrace(PVTFetchSignalPowerTraceRequest) returns (PVTFetchSignalPowerTraceResponse);
  rpc PVTFetchWindowedSignalPowerTrace(PVTFetchWindowedSignalPowerTraceRequest) returns (PVTFetchWindowedSignalPowerTraceResponse);
  rpc ResetAttribute(ResetAttributeRequest) returns (ResetAttributeResponse);
  rpc ResetToDefault(ResetToDefaultRequest) returns (ResetToDefaultResponse);
  rpc SEMCfgAveraging(SEMCfgAveragingRequest) returns (SEMCfgAveragingResponse);
  rpc SEMCfgComponentCarrierRatedOutputPower(SEMCfgComponentCarrierRatedOutputPowerRequest) returns (SEMCfgComponentCarrierRatedOutputPowerResponse);
  rpc SEMCfgComponentCarrierRatedOutputPowerArray(SEMCfgComponentCarrierRatedOutputPowerArrayRequest) returns (SEMCfgComponentCarrierRatedOutputPowerArrayResponse);
  rpc SEMCfgNumberOfOffsets(SEMCfgNumberOfOffsetsRequest) returns (SEMCfgNumberOfOffsetsResponse);
  rpc SEMCfgOffsetAbsoluteLimit(SEMCfgOffsetAbsoluteLimitRequest) returns (SEMCfgOffsetAbsoluteLimitResponse);
  rpc SEMCfgOffsetAbsoluteLimitArray(SEMCfgOffsetAbsoluteLimitArrayRequest) returns (SEMCfgOffsetAbsoluteLimitArrayResponse);
  rpc SEMCfgOffsetBandwidthIntegral(SEMCfgOffsetBandwidthIntegralRequest) returns (SEMCfgOffsetBandwidthIntegralResponse);
  rpc SEMCfgOffsetBandwidthIntegralArray(SEMCfgOffsetBandwidthIntegralArrayRequest) returns (SEMCfgOffsetBandwidthIntegralArrayResponse);
  rpc SEMCfgOffsetFrequency(SEMCfgOffsetFrequencyRequest) returns (SEMCfgOffsetFrequencyResponse);
  rpc SEMCfgOffsetFrequencyArray(SEMCfgOffsetFrequencyArrayRequest) returns (SEMCfgOffsetFrequencyArrayResponse);
  rpc SEMCfgOffsetLimitFailMask(SEMCfgOffsetLimitFailMaskRequest) returns (SEMCfgOffsetLimitFailMaskResponse);
  rpc SEMCfgOffsetLimitFailMaskArray(SEMCfgOffsetLimitFailMaskArrayRequest) returns (SEMCfgOffsetLimitFailMaskArrayResponse);
  rpc SEMCfgOffsetRBWFilter(SEMCfgOffsetRBWFilterRequest) returns (SEMCfgOffsetRBWFilterResponse);
  rpc SEMCfgOffsetRBWFilterArray(SEMCfgOffsetRBWFilterArrayRequest) returns (SEMCfgOffsetRBWFilterArrayResponse);
  rpc SEMCfgOffsetRelativeLimit(SEMCfgOffsetRelativeLimitRequest) returns (SEMCfgOffsetRelativeLimitResponse);
  rpc SEMCfgOffsetRelativeLimitArray(SEMCfgOffsetRelativeLimitArrayRequest) returns (SEMCfgOffsetRelativeLimitArrayResponse);
  rpc SEMCfgSweepTime(SEMCfgSweepTimeRequest) returns (SEMCfgSweepTimeResponse);
  rpc SEMCfgUplinkMaskType(SEMCfgUplinkMaskTypeRequest) returns (SEMCfgUplinkMaskTypeResponse);
  rpc SEMFetchComponentCarrierMeasurement(SEMFetchComponentCarrierMeasurementRequest) returns (SEMFetchComponentCarrierMeasurementResponse);
  rpc SEMFetchComponentCarrierMeasurementArray(SEMFetchComponentCarrierMeasurementArrayRequest) returns (SEMFetchComponentCarrierMeasurementArrayResponse);
  rpc SEMFetchLowerOffsetMargin(SEMFetchLowerOffsetMarginRequest) returns (SEMFetchLowerOffsetMarginResponse);
  rpc SEMFetchLowerOffsetMarginArray(SEMFetchLowerOffsetMarginArrayRequest) returns (SEMFetchLowerOffsetMarginArrayResponse);
  rpc SEMFetchLowerOffsetPower(SEMFetchLowerOffsetPowerRequest) returns (SEMFetchLowerOffsetPowerResponse);
  rpc SEMFetchLowerOffsetPowerArray(SEMFetchLowerOffsetPowerArrayRequest) returns (SEMFetchLowerOffsetPowerArrayResponse);
  rpc SEMFetchMeasurementStatus(SEMFetchMeasurementStatusRequest) returns (SEMFetchMeasurementStatusResponse);
  rpc SEMFetchSpectrum(SEMFetchSpectrumRequest) returns (SEMFetchSpectrumResponse);
  rpc SEMFetchSubblockMeasurement(SEMFetchSubblockMeasurementRequest) returns (SEMFetchSubblockMeasurementResponse);
  rpc SEMFetchTotalAggregatedPower(SEMFetchTotalAggregatedPowerRequest) returns (SEMFetchTotalAggregatedPowerResponse);
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
  rpc TXPFetchMeasurement(TXPFetchMeasurementRequest) returns (TXPFetchMeasurementResponse);
  rpc TXPFetchPowerTrace(TXPFetchPowerTraceRequest) returns (TXPFetchPowerTraceResponse);
  rpc WaitForAcquisitionComplete(WaitForAcquisitionCompleteRequest) returns (WaitForAcquisitionCompleteResponse);
  rpc WaitForMeasurementComplete(WaitForMeasurementCompleteRequest) returns (WaitForMeasurementCompleteResponse);
}

enum NiRFmxNRAttribute {
  NIRFMXNR_ATTRIBUTE_UNSPECIFIED = 0;
  NIRFMXNR_ATTRIBUTE_CENTER_FREQUENCY = 9437185;
  NIRFMXNR_ATTRIBUTE_REFERENCE_LEVEL = 9437186;
  NIRFMXNR_ATTRIBUTE_EXTERNAL_ATTENUATION = 9437187;
  NIRFMXNR_ATTRIBUTE_TRIGGER_TYPE = 9437188;
  NIRFMXNR_ATTRIBUTE_DIGITAL_EDGE_TRIGGER_SOURCE = 9437189;
  NIRFMXNR_ATTRIBUTE_DIGITAL_EDGE_TRIGGER_EDGE = 9437190;
  NIRFMXNR_ATTRIBUTE_IQ_POWER_EDGE_TRIGGER_SOURCE = 9437191;
  NIRFMXNR_ATTRIBUTE_IQ_POWER_EDGE_TRIGGER_LEVEL = 9437192;
  NIRFMXNR_ATTRIBUTE_IQ_POWER_EDGE_TRIGGER_SLOPE = 9437193;
  NIRFMXNR_ATTRIBUTE_TRIGGER_DELAY = 9437194;
  NIRFMXNR_ATTRIBUTE_TRIGGER_MINIMUM_QUIET_TIME_MODE = 9437195;
  NIRFMXNR_ATTRIBUTE_TRIGGER_MINIMUM_QUIET_TIME_DURATION = 9437196;
  NIRFMXNR_ATTRIBUTE_LINK_DIRECTION = 9437198;
  NIRFMXNR_ATTRIBUTE_NUMBER_OF_SUBBLOCKS = 9437200;
  NIRFMXNR_ATTRIBUTE_BAND = 9437202;
  NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_SPACING_TYPE = 9437203;
  NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_AT_CENTER_FREQUENCY = 9437204;
  NIRFMXNR_ATTRIBUTE_NUMBER_OF_COMPONENT_CARRIERS = 9437205;
  NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_BANDWIDTH = 9437206;
  NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_FREQUENCY = 9437207;
  NIRFMXNR_ATTRIBUTE_CELL_ID = 9437209;
  NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_CYCLIC_PREFIX_MODE = 9437210;
  NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_SUBCARRIER_SPACING = 9437211;
  NIRFMXNR_ATTRIBUTE_PUSCH_TRANSFORM_PRECODING_ENABLED = 9437214;
  NIRFMXNR_ATTRIBUTE_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED = 9437215;
  NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_GROUP_HOPPING_ENABLED = 9437217;
  NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_SEQUENCE_HOPPING_ENABLED = 9437218;
  NIRFMXNR_ATTRIBUTE_PUSCH_MODULATION_TYPE = 9437222;
  NIRFMXNR_ATTRIBUTE_PUSCH_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS = 9437223;
  NIRFMXNR_ATTRIBUTE_PUSCH_RESOURCE_BLOCK_OFFSET = 9437224;
  NIRFMXNR_ATTRIBUTE_PUSCH_NUMBER_OF_RESOURCE_BLOCKS = 9437225;
  NIRFMXNR_ATTRIBUTE_MODACC_DC_SUBCARRIER_REMOVAL_ENABLED = 9437231;
  NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_POWER = 9437232;
  NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_CONFIGURATION_TYPE = 9437233;
  NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_ADDITIONAL_POSITIONS = 9437234;
  NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_DURATION = 9437235;
  NIRFMXNR_ATTRIBUTE_PUSCH_MAPPING_TYPE = 9437236;
  NIRFMXNR_ATTRIBUTE_FREQUENCY_RANGE = 9437237;
  NIRFMXNR_ATTRIBUTE_REFERENCE_GRID_ALIGNMENT_MODE = 9437239;
  NIRFMXNR_ATTRIBUTE_MODACC_COMPOSITE_RESULTS_INCLUDE_DMRS = 9437240;
  NIRFMXNR_ATTRIBUTE_MODACC_COMPOSITE_RESULTS_INCLUDE_PTRS = 9437241;
  NIRFMXNR_ATTRIBUTE_SUB_BAND_ALLOCATION = 9437244;
  NIRFMXNR_ATTRIBUTE_NUMBER_OF_BANDWIDTH_PARTS = 9437245;
  NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_RESOURCE_BLOCK_OFFSET = 9437246;
  NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_NUMBER_OF_RESOURCE_BLOCKS = 9437247;
  NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_ANTENNA_PORTS = 9437249;
  NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_NUMBER_OF_CDM_GROUPS = 9437250;
  NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_SCRAMBLING_ID_MODE = 9437252;
  NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_SCRAMBLING_ID = 9437253;
  NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_NSCID = 9437254;
  NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_PUSCH_ID_MODE = 9437255;
  NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_PUSCH_ID = 9437256;
  NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_TYPE_A_POSITION = 9437258;
  NIRFMXNR_ATTRIBUTE_NUMBER_OF_PUSCH_CONFIGURATIONS = 9437259;
  NIRFMXNR_ATTRIBUTE_PUSCH_SLOT_ALLOCATION = 9437260;
  NIRFMXNR_ATTRIBUTE_PUSCH_SYMBOL_ALLOCATION = 9437261;
  NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_POWER_MODE = 9437265;
  NIRFMXNR_ATTRIBUTE_PUSCH_PTRS_ENABLED = 9437269;
  NIRFMXNR_ATTRIBUTE_PUSCH_PTRS_ANTENNA_PORTS = 9437270;
  NIRFMXNR_ATTRIBUTE_PUSCH_PTRS_POWER_MODE = 9437271;
  NIRFMXNR_ATTRIBUTE_PUSCH_PTRS_POWER = 9437272;
  NIRFMXNR_ATTRIBUTE_NUMBER_OF_PTRS_GROUPS = 9437274;
  NIRFMXNR_ATTRIBUTE_SAMPLES_PER_PTRS_GROUP = 9437275;
  NIRFMXNR_ATTRIBUTE_PUSCH_PTRS_TIME_DENSITY = 9437276;
  NIRFMXNR_ATTRIBUTE_PUSCH_PTRS_FREQUENCY_DENSITY = 9437277;
  NIRFMXNR_ATTRIBUTE_PUSCH_PTRS_RE_OFFSET = 9437278;
  NIRFMXNR_ATTRIBUTE_GNODEB_CATEGORY = 9437279;
  NIRFMXNR_ATTRIBUTE_SUBBLOCK_TRANSMIT_LO_FREQUENCY = 9437280;
  NIRFMXNR_ATTRIBUTE_PHASE_COMPENSATION_FREQUENCY = 9437281;
  NIRFMXNR_ATTRIBUTE_REFERENCE_GRID_SUBCARRIER_SPACING = 9437282;
  NIRFMXNR_ATTRIBUTE_REFERENCE_GRID_START = 9437283;
  NIRFMXNR_ATTRIBUTE_NUMBER_OF_USERS = 9437284;
  NIRFMXNR_ATTRIBUTE_RNTI = 9437285;
  NIRFMXNR_ATTRIBUTE_PDSCH_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS = 9437287;
  NIRFMXNR_ATTRIBUTE_PDSCH_RESOURCE_BLOCK_OFFSET = 9437288;
  NIRFMXNR_ATTRIBUTE_PDSCH_NUMBER_OF_RESOURCE_BLOCKS = 9437289;
  NIRFMXNR_ATTRIBUTE_PDSCH_MODULATION_TYPE = 9437290;
  NIRFMXNR_ATTRIBUTE_PDSCH_DMRS_ANTENNA_PORTS = 9437291;
  NIRFMXNR_ATTRIBUTE_PDSCH_DMRS_POWER_MODE = 9437292;
  NIRFMXNR_ATTRIBUTE_PDSCH_DMRS_POWER = 9437293;
  NIRFMXNR_ATTRIBUTE_PDSCH_DMRS_NUMBER_OF_CDM_GROUPS = 9437294;
  NIRFMXNR_ATTRIBUTE_PDSCH_DMRS_SCRAMBLING_ID_MODE = 9437295;
  NIRFMXNR_ATTRIBUTE_PDSCH_DMRS_SCRAMBLING_ID = 9437296;
  NIRFMXNR_ATTRIBUTE_PDSCH_DMRS_NSCID = 9437297;
  NIRFMXNR_ATTRIBUTE_PDSCH_DMRS_CONFIGURATION_TYPE = 9437300;
  NIRFMXNR_ATTRIBUTE_PDSCH_MAPPING_TYPE = 9437301;
  NIRFMXNR_ATTRIBUTE_PDSCH_DMRS_TYPE_A_POSITION = 9437302;
  NIRFMXNR_ATTRIBUTE_PDSCH_DMRS_DURATION = 9437303;
  NIRFMXNR_ATTRIBUTE_PDSCH_DMRS_ADDITIONAL_POSITIONS = 9437304;
  NIRFMXNR_ATTRIBUTE_PDSCH_PTRS_ENABLED = 9437305;
  NIRFMXNR_ATTRIBUTE_PDSCH_PTRS_ANTENNA_PORTS = 9437306;
  NIRFMXNR_ATTRIBUTE_PDSCH_PTRS_POWER_MODE = 9437307;
  NIRFMXNR_ATTRIBUTE_PDSCH_PTRS_POWER = 9437308;
  NIRFMXNR_ATTRIBUTE_PDSCH_PTRS_TIME_DENSITY = 9437309;
  NIRFMXNR_ATTRIBUTE_PDSCH_PTRS_FREQUENCY_DENSITY = 9437310;
  NIRFMXNR_ATTRIBUTE_PDSCH_PTRS_RE_OFFSET = 9437311;
  NIRFMXNR_ATTRIBUTE_PDSCH_SLOT_ALLOCATION = 9437312;
  NIRFMXNR_ATTRIBUTE_PDSCH_SYMBOL_ALLOCATION = 9437313;
  NIRFMXNR_ATTRIBUTE_SSB_ENABLED = 9437314;
  NIRFMXNR_ATTRIBUTE_SSB_CRB_OFFSET = 9437315;
  NIRFMXNR_ATTRIBUTE_SSB_SUBCARRIER_OFFSET = 9437316;
  NIRFMXNR_ATTRIBUTE_SSB_PATTERN = 9437317;
  NIRFMXNR_ATTRIBUTE_PSS_POWER = 9437318;
  NIRFMXNR_ATTRIBUTE_SSS_POWER = 9437319;
  NIRFMXNR_ATTRIBUTE_PBCH_POWER = 9437320;
  NIRFMXNR_ATTRIBUTE_PBCH_DMRS_POWER = 9437321;
  NIRFMXNR_ATTRIBUTE_AUTO_CELL_ID_DETECTION_ENABLED = 9437324;
  NIRFMXNR_ATTRIBUTE_DOWNLINK_CHANNEL_CONFIGURATION_MODE = 9437326;
  NIRFMXNR_ATTRIBUTE_NUMBER_OF_PDSCH_CONFIGURATIONS = 9437328;
  NIRFMXNR_ATTRIBUTE_EPRE_RATIO_PORT = 9437330;
  NIRFMXNR_ATTRIBUTE_SSB_PERIODICITY = 9437332;
  NIRFMXNR_ATTRIBUTE_SSB_ACTIVE_BLOCKS = 9437333;
  NIRFMXNR_ATTRIBUTE_GRID_START = 9437334;
  NIRFMXNR_ATTRIBUTE_CHANNEL_RASTER = 9437336;
  NIRFMXNR_ATTRIBUTE_SUBCARRIER_SPACING_COMMON = 9437337;
  NIRFMXNR_ATTRIBUTE_GRID_SIZE = 9437338;
  NIRFMXNR_ATTRIBUTE_TRANSMIT_ANTENNA_TO_ANALYZE = 9437339;
  NIRFMXNR_ATTRIBUTE_POWER_CLASS = 9437340;
  NIRFMXNR_ATTRIBUTE_PIBY2BPSK_POWER_BOOST_ENABLED = 9437342;
  NIRFMXNR_ATTRIBUTE_AUTO_INCREMENT_CELL_ID_ENABLED = 9437343;
  NIRFMXNR_ATTRIBUTE_GNODEB_TYPE = 9437344;
  NIRFMXNR_ATTRIBUTE_RATED_TRP = 9437345;
  NIRFMXNR_ATTRIBUTE_RATED_EIRP = 9437346;
  NIRFMXNR_ATTRIBUTE_SATELLITE_ACCESS_NODE_CLASS = 9437347;
  NIRFMXNR_ATTRIBUTE_SATELLITE_ACCESS_NODE_TYPE = 9437348;
  NIRFMXNR_ATTRIBUTE_DOWNLINK_TEST_MODEL = 9437440;
  NIRFMXNR_ATTRIBUTE_DOWNLINK_TEST_MODEL_DUPLEX_SCHEME = 9437441;
  NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_RADIO_ACCESS_TYPE = 9437442;
  NIRFMXNR_ATTRIBUTE_SUBBLOCK_ENDC_NOMINAL_SPACING_ADJUSTMENT = 9437443;
  NIRFMXNR_ATTRIBUTE_NUMBER_OF_CORESETS = 9437446;
  NIRFMXNR_ATTRIBUTE_CORESET_SYMBOL_OFFSET = 9437447;
  NIRFMXNR_ATTRIBUTE_CORESET_NUMBER_OF_SYMBOLS = 9437448;
  NIRFMXNR_ATTRIBUTE_CORESET_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS = 9437449;
  NIRFMXNR_ATTRIBUTE_CORESET_RESOURCE_BLOCK_OFFSET = 9437450;
  NIRFMXNR_ATTRIBUTE_CORESET_NUMBER_OF_RESOURCE_BLOCKS = 9437451;
  NIRFMXNR_ATTRIBUTE_CORESET_PRECODING_GRANULARITY = 9437452;
  NIRFMXNR_ATTRIBUTE_CORESET_CCE_TO_REG_MAPPING_TYPE = 9437453;
  NIRFMXNR_ATTRIBUTE_CORESET_REG_BUNDLE_SIZE = 9437454;
  NIRFMXNR_ATTRIBUTE_CORESET_INTERLEAVER_SIZE = 9437455;
  NIRFMXNR_ATTRIBUTE_CORESET_SHIFT_INDEX = 9437456;
  NIRFMXNR_ATTRIBUTE_NUMBER_OF_PDCCH_CONFIGURATIONS = 9437458;
  NIRFMXNR_ATTRIBUTE_PDCCH_CCE_AGGREGATION_LEVEL = 9437459;
  NIRFMXNR_ATTRIBUTE_PDCCH_CCE_OFFSET = 9437460;
  NIRFMXNR_ATTRIBUTE_PDCCH_SLOT_ALLOCATION = 9437461;
  NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_RELEASE_VERSION = 9437462;
  NIRFMXNR_ATTRIBUTE_PDSCH_DMRS_RELEASE_VERSION = 9437463;
  NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_ALLOCATED = 9437464;
  NIRFMXNR_ATTRIBUTE_REFERENCE_GRID_SIZE = 9437465;
  NIRFMXNR_ATTRIBUTE_SSB_GRID_START = 9437466;
  NIRFMXNR_ATTRIBUTE_SSB_GRID_SIZE = 9437467;
  NIRFMXNR_ATTRIBUTE_GRID_SIZE_MODE = 9437468;
  NIRFMXNR_ATTRIBUTE_DOWNLINK_TEST_MODEL_MODULATION_TYPE = 9437469;
  NIRFMXNR_ATTRIBUTE_DOWNLINK_TEST_MODEL_CELL_ID_MODE = 9437470;
  NIRFMXNR_ATTRIBUTE_SUBBLOCK_FREQUENCY = 9437471;
  NIRFMXNR_ATTRIBUTE_SSB_HRF_INDEX = 9437472;
  NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_DC_LOCATION_KNOWN = 9437473;
  NIRFMXNR_ATTRIBUTE_TRANSMITTER_ARCHITECTURE = 9438267;
  NIRFMXNR_ATTRIBUTE_PHASE_COMPENSATION = 9438269;
  NIRFMXNR_ATTRIBUTE_LIST_STEP_TIMER_UNIT = 9441270;
  NIRFMXNR_ATTRIBUTE_LIST_STEP_TIMER_OFFSET = 9441271;
  NIRFMXNR_ATTRIBUTE_NUMBER_OF_STEPS = 9441272;
  NIRFMXNR_ATTRIBUTE_LIST_STEP_TIMER_DURATION = 9441273;
  NIRFMXNR_ATTRIBUTE_REFERENCE_LEVEL_HEADROOM = 9441276;
  NIRFMXNR_ATTRIBUTE_SELECTED_PORTS = 9441277;
  NIRFMXNR_ATTRIBUTE_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE = 9441279;
  NIRFMXNR_ATTRIBUTE_ACP_MEASUREMENT_ENABLED = 9441280;
  NIRFMXNR_ATTRIBUTE_ACP_SUBBLOCK_INTEGRATION_BANDWIDTH = 9441282;
  NIRFMXNR_ATTRIBUTE_ACP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH = 9441286;
  NIRFMXNR_ATTRIBUTE_ACP_NUMBER_OF_UTRA_OFFSETS = 9441289;
  NIRFMXNR_ATTRIBUTE_ACP_NUMBER_OF_EUTRA_OFFSETS = 9441290;
  NIRFMXNR_ATTRIBUTE_ACP_NUMBER_OF_NR_OFFSETS = 9441291;
  NIRFMXNR_ATTRIBUTE_ACP_NUMBER_OF_OFFSETS = 9441292;
  NIRFMXNR_ATTRIBUTE_ACP_OFFSET_FREQUENCY = 9441294;
  NIRFMXNR_ATTRIBUTE_ACP_OFFSET_SIDEBAND = 9441295;
  NIRFMXNR_ATTRIBUTE_ACP_OFFSET_INTEGRATION_BANDWIDTH = 9441298;
  NIRFMXNR_ATTRIBUTE_ACP_RBW_FILTER_AUTO_BANDWIDTH = 9441302;
  NIRFMXNR_ATTRIBUTE_ACP_RBW_FILTER_BANDWIDTH = 9441303;
  NIRFMXNR_ATTRIBUTE_ACP_RBW_FILTER_TYPE = 9441304;
  NIRFMXNR_ATTRIBUTE_ACP_SWEEP_TIME_AUTO = 9441305;
  NIRFMXNR_ATTRIBUTE_ACP_SWEEP_TIME_INTERVAL = 9441306;
  NIRFMXNR_ATTRIBUTE_ACP_POWER_UNITS = 9441307;
  NIRFMXNR_ATTRIBUTE_ACP_MEASUREMENT_METHOD = 9441308;
  NIRFMXNR_ATTRIBUTE_ACP_NOISE_COMPENSATION_ENABLED = 9441309;
  NIRFMXNR_ATTRIBUTE_ACP_AVERAGING_ENABLED = 9441310;
  NIRFMXNR_ATTRIBUTE_ACP_AVERAGING_COUNT = 9441311;
  NIRFMXNR_ATTRIBUTE_ACP_AVERAGING_TYPE = 9441313;
  NIRFMXNR_ATTRIBUTE_ACP_FFT_WINDOW = 9441314;
  NIRFMXNR_ATTRIBUTE_ACP_IF_OUTPUT_POWER_OFFSET_AUTO = 9441316;
  NIRFMXNR_ATTRIBUTE_ACP_NEAR_IF_OUTPUT_POWER_OFFSET = 9441317;
  NIRFMXNR_ATTRIBUTE_ACP_FAR_IF_OUTPUT_POWER_OFFSET = 9441318;
  NIRFMXNR_ATTRIBUTE_ACP_SEQUENTIAL_FFT_SIZE = 9441319;
  NIRFMXNR_ATTRIBUTE_ACP_AMPLITUDE_CORRECTION_TYPE = 9441320;
  NIRFMXNR_ATTRIBUTE_ACP_ALL_TRACES_ENABLED = 9441321;
  NIRFMXNR_ATTRIBUTE_ACP_NUMBER_OF_ANALYSIS_THREADS = 9441322;
  NIRFMXNR_ATTRIBUTE_ACP_RESULTS_TOTAL_AGGREGATED_POWER = 9441324;
  NIRFMXNR_ATTRIBUTE_ACP_RESULTS_SUBBLOCK_POWER = 9441328;
  NIRFMXNR_ATTRIBUTE_ACP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER = 9441331;
  NIRFMXNR_ATTRIBUTE_ACP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER = 9441332;
  NIRFMXNR_ATTRIBUTE_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER = 9441338;
  NIRFMXNR_ATTRIBUTE_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER = 9441339;
  NIRFMXNR_ATTRIBUTE_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER = 9441345;
  NIRFMXNR_ATTRIBUTE_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER = 9441346;
  NIRFMXNR_ATTRIBUTE_ACP_NUMBER_OF_ENDC_OFFSETS = 9441347;
  NIRFMXNR_ATTRIBUTE_ACP_OFFSET_CHANNEL_SPACING_ADJUSTMENT = 9441349;
  NIRFMXNR_ATTRIBUTE_ACP_FFT_OVERLAP_MODE = 9441350;
  NIRFMXNR_ATTRIBUTE_ACP_FFT_OVERLAP = 9441351;
  NIRFMXNR_ATTRIBUTE_ACP_MEASUREMENT_MODE = 9441352;
  NIRFMXNR_ATTRIBUTE_ACP_NOISE_COMPENSATION_TYPE = 9441353;
  NIRFMXNR_ATTRIBUTE_ACP_NOISE_CALIBRATION_AVERAGING_COUNT = 9441354;
  NIRFMXNR_ATTRIBUTE_ACP_NOISE_CALIBRATION_AVERAGING_AUTO = 9441355;
  NIRFMXNR_ATTRIBUTE_ACP_NOISE_CALIBRATION_MODE = 9441356;
  NIRFMXNR_ATTRIBUTE_ACP_CHANNEL_CONFIGURATION_TYPE = 9441357;
  NIRFMXNR_ATTRIBUTE_ACP_SUBBLOCK_OFFSET = 9441358;
  NIRFMXNR_ATTRIBUTE_CHP_MEASUREMENT_ENABLED = 9449472;
  NIRFMXNR_ATTRIBUTE_CHP_SWEEP_TIME_AUTO = 9449474;
  NIRFMXNR_ATTRIBUTE_CHP_SWEEP_TIME_INTERVAL = 9449475;
  NIRFMXNR_ATTRIBUTE_CHP_INTEGRATION_BANDWIDTH_TYPE = 9449476;
  NIRFMXNR_ATTRIBUTE_CHP_SUBBLOCK_INTEGRATION_BANDWIDTH = 9449477;
  NIRFMXNR_ATTRIBUTE_CHP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH = 9449478;
  NIRFMXNR_ATTRIBUTE_CHP_RBW_FILTER_AUTO_BANDWIDTH = 9449481;
  NIRFMXNR_ATTRIBUTE_CHP_RBW_FILTER_BANDWIDTH = 9449482;
  NIRFMXNR_ATTRIBUTE_CHP_RBW_FILTER_TYPE = 9449483;
  NIRFMXNR_ATTRIBUTE_CHP_AVERAGING_ENABLED = 9449485;
  NIRFMXNR_ATTRIBUTE_CHP_AVERAGING_COUNT = 9449486;
  NIRFMXNR_ATTRIBUTE_CHP_AVERAGING_TYPE = 9449488;
  NIRFMXNR_ATTRIBUTE_CHP_FFT_WINDOW = 9449489;
  NIRFMXNR_ATTRIBUTE_CHP_AMPLITUDE_CORRECTION_TYPE = 9449490;
  NIRFMXNR_ATTRIBUTE_CHP_ALL_TRACES_ENABLED = 9449491;
  NIRFMXNR_ATTRIBUTE_CHP_NUMBER_OF_ANALYSIS_THREADS = 9449492;
  NIRFMXNR_ATTRIBUTE_CHP_RESULTS_TOTAL_AGGREGATED_POWER = 9449494;
  NIRFMXNR_ATTRIBUTE_CHP_RESULTS_SUBBLOCK_POWER = 9449498;
  NIRFMXNR_ATTRIBUTE_CHP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER = 9449501;
  NIRFMXNR_ATTRIBUTE_CHP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER = 9449503;
  NIRFMXNR_ATTRIBUTE_CHP_MEASUREMENT_MODE = 9449505;
  NIRFMXNR_ATTRIBUTE_CHP_NOISE_COMPENSATION_ENABLED = 9449506;
  NIRFMXNR_ATTRIBUTE_CHP_NOISE_COMPENSATION_TYPE = 9449507;
  NIRFMXNR_ATTRIBUTE_CHP_NOISE_CALIBRATION_AVERAGING_COUNT = 9449508;
  NIRFMXNR_ATTRIBUTE_CHP_NOISE_CALIBRATION_AVERAGING_AUTO = 9449509;
  NIRFMXNR_ATTRIBUTE_CHP_NOISE_CALIBRATION_MODE = 9449510;
  NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_ENABLED = 9453568;
  NIRFMXNR_ATTRIBUTE_MODACC_MULTICARRIER_FILTER_ENABLED = 9453570;
  NIRFMXNR_ATTRIBUTE_MODACC_SYNCHRONIZATION_MODE = 9453572;
  NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_LENGTH_UNIT = 9453573;
  NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_OFFSET = 9453574;
  NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_LENGTH = 9453575;
  NIRFMXNR_ATTRIBUTE_MODACC_SPECTRUM_INVERTED = 9453576;
  NIRFMXNR_ATTRIBUTE_MODACC_CHANNEL_ESTIMATION_TYPE = 9453577;
  NIRFMXNR_ATTRIBUTE_MODACC_EVM_UNIT = 9453578;
  NIRFMXNR_ATTRIBUTE_MODACC_FFT_WINDOW_TYPE = 9453579;
  NIRFMXNR_ATTRIBUTE_MODACC_FFT_WINDOW_OFFSET = 9453580;
  NIRFMXNR_ATTRIBUTE_MODACC_FFT_WINDOW_LENGTH = 9453581;
  NIRFMXNR_ATTRIBUTE_MODACC_COMMON_CLOCK_SOURCE_ENABLED = 9453582;
  NIRFMXNR_ATTRIBUTE_MODACC_SPECTRAL_FLATNESS_CONDITION = 9453584;
  NIRFMXNR_ATTRIBUTE_MODACC_AVERAGING_ENABLED = 9453585;
  NIRFMXNR_ATTRIBUTE_MODACC_AVERAGING_COUNT = 9453586;
  NIRFMXNR_ATTRIBUTE_MODACC_ALL_TRACES_ENABLED = 9453587;
  NIRFMXNR_ATTRIBUTE_MODACC_NUMBER_OF_ANALYSIS_THREADS = 9453588;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_RMS_EVM_MEAN = 9453590;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_PEAK_EVM_MAXIMUM = 9453591;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_RMS_MAGNITUDE_ERROR_MEAN = 9453592;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_PEAK_MAGNITUDE_ERROR_MAXIMUM = 9453593;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_RMS_PHASE_ERROR_MEAN = 9453594;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_PEAK_PHASE_ERROR_MAXIMUM = 9453595;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SLOT_INDEX = 9453596;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SYMBOL_INDEX = 9453597;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SUBCARRIER_INDEX = 9453598;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PUSCH_DATA_RMS_EVM_MEAN = 9453599;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PUSCH_DATA_PEAK_EVM_MAXIMUM = 9453600;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PUSCH_DMRS_RMS_EVM_MEAN = 9453603;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PUSCH_DMRS_PEAK_EVM_MAXIMUM = 9453604;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_IN_BAND_EMISSION_MARGIN = 9453607;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_TO_RANGE1_MINIMUM = 9453608;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_TO_RANGE2_MINIMUM = 9453609;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_TO_RANGE2_MINIMUM = 9453610;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_TO_RANGE1_MINIMUM = 9453611;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SUBBLOCK_IN_BAND_EMISSION_MARGIN = 9453612;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_FREQUENCY_ERROR_MEAN = 9453613;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_IQ_ORIGIN_OFFSET_MEAN = 9453614;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_IQ_GAIN_IMBALANCE_MEAN = 9453615;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_QUADRATURE_ERROR_MEAN = 9453616;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_IQ_TIMING_SKEW_MEAN = 9453617;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_TIME_OFFSET_MEAN = 9453618;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_SYMBOL_CLOCK_ERROR_MEAN = 9453619;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SUBBLOCK_IQ_ORIGIN_OFFSET_MEAN = 9453622;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_DETECTED_CELL_ID = 9453626;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PUSCH_PTRS_RMS_EVM_MEAN = 9453640;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PUSCH_PTRS_PEAK_EVM_MAXIMUM = 9453641;
  NIRFMXNR_ATTRIBUTE_MODACC_PHASE_TRACKING_MODE = 9453649;
  NIRFMXNR_ATTRIBUTE_MODACC_TIMING_TRACKING_MODE = 9453650;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_PEAK_EVM_BWP_INDEX = 9453652;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PDSCH_QPSK_RMS_EVM_MEAN = 9453653;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PDSCH_16QAM_RMS_EVM_MEAN = 9453654;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PDSCH_64QAM_RMS_EVM_MEAN = 9453655;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PDSCH_256QAM_RMS_EVM_MEAN = 9453656;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PDSCH_DATA_RMS_EVM_MEAN = 9453657;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PDSCH_DATA_PEAK_EVM_MAXIMUM = 9453658;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PDSCH_DMRS_RMS_EVM_MEAN = 9453659;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PDSCH_DMRS_PEAK_EVM_MAXIMUM = 9453660;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PDSCH_PTRS_RMS_EVM_MEAN = 9453661;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PDSCH_PTRS_PEAK_EVM_MAXIMUM = 9453662;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SUBBLOCK_LO_COMPONENT_CARRIER_INDEX = 9453666;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SUBBLOCK_LO_SUBCARRIER_INDEX = 9453667;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SCH_SYMBOL_POWER_MEAN = 9453679;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SCH_DETECTED_MODULATION_TYPE = 9453680;
  NIRFMXNR_ATTRIBUTE_MODACC_FREQUENCY_ERROR_ESTIMATION = 9453681;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PDSCH_1024QAM_RMS_EVM_MEAN = 9453683;
  NIRFMXNR_ATTRIBUTE_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED = 9453685;
  NIRFMXNR_ATTRIBUTE_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED = 9453686;
  NIRFMXNR_ATTRIBUTE_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED = 9453687;
  NIRFMXNR_ATTRIBUTE_MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLED = 9453688;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PSS_RMS_EVM_MEAN = 9453689;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PSS_PEAK_EVM_MAXIMUM = 9453690;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SSS_RMS_EVM_MEAN = 9453691;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SSS_PEAK_EVM_MAXIMUM = 9453692;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PBCH_DATA_RMS_EVM_MEAN = 9453693;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PBCH_DATA_PEAK_EVM_MAXIMUM = 9453694;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PBCH_DMRS_RMS_EVM_MEAN = 9453695;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PBCH_DMRS_PEAK_EVM_MAXIMUM = 9453696;
  NIRFMXNR_ATTRIBUTE_MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE = 9453697;
  NIRFMXNR_ATTRIBUTE_MODACC_IQ_IMPAIRMENTS_MODEL = 9453698;
  NIRFMXNR_ATTRIBUTE_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED = 9453699;
  NIRFMXNR_ATTRIBUTE_MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED = 9453700;
  NIRFMXNR_ATTRIBUTE_MODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED = 9453701;
  NIRFMXNR_ATTRIBUTE_MODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED = 9453702;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SPECTRAL_FLATNESS_MARGIN_SLOT_INDEX = 9453704;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM = 9453705;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MINIMUM = 9453706;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM = 9453707;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MINIMUM = 9453708;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_SUBCARRIER_INDEX = 9453709;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MINIMUM_SUBCARRIER_INDEX = 9453710;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_SUBCARRIER_INDEX = 9453711;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MINIMUM_SUBCARRIER_INDEX = 9453712;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PDSCH_8PSK_RMS_EVM_MEAN = 9453713;
  NIRFMXNR_ATTRIBUTE_MODACC_NOISE_COMPENSATION_ENABLED = 9453714;
  NIRFMXNR_ATTRIBUTE_MODACC_NOISE_COMPENSATION_INPUT_POWER_CHECK_ENABLED = 9453715;
  NIRFMXNR_ATTRIBUTE_MODACC_NOISE_COMPENSATION_REFERENCE_LEVEL_COERCION_LIMIT = 9453716;
  NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_MODE = 9453717;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_NOISE_COMPENSATION_APPLIED = 9453718;
  NIRFMXNR_ATTRIBUTE_MODACC_AUTO_LEVEL_ALLOW_OVERFLOW = 9453719;
  NIRFMXNR_ATTRIBUTE_MODACC_SHORT_FRAME_ENABLED = 9453725;
  NIRFMXNR_ATTRIBUTE_MODACC_SHORT_FRAME_LENGTH = 9453726;
  NIRFMXNR_ATTRIBUTE_MODACC_SHORT_FRAME_LENGTH_UNIT = 9453727;
  NIRFMXNR_ATTRIBUTE_MODACC_PRE_FFT_ERROR_ESTIMATION_INTERVAL = 9453728;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_SLOT_FREQUENCY_ERROR_MAXIMUM = 9453729;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_SLOT_IQ_ORIGIN_OFFSET_MAXIMUM = 9453730;
  NIRFMXNR_ATTRIBUTE_MODACC_TRANSIENT_PERIOD_EVM_MODE = 9453731;
  NIRFMXNR_ATTRIBUTE_MODACC_TRANSIENT_PERIOD = 9453732;
  NIRFMXNR_ATTRIBUTE_MODACC_TRANSIENT_POWER_CHANGE_THRESHOLD = 9453733;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PUSCH_DATA_TRANSIENT_RMS_EVM_MEAN = 9453734;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PUSCH_PEAK_PHASE_OFFSET_MAXIMUM = 9453735;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PUSCH_PEAK_PHASE_OFFSET_SLOT_INDEX = 9453736;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PUSCH_DATA_RE_POWER_MEAN = 9453737;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PUSCH_DMRS_RE_POWER_MEAN = 9453738;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PUSCH_PTRS_RE_POWER_MEAN = 9453739;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PDSCH_DATA_RE_POWER_MEAN = 9453740;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PDSCH_DMRS_RE_POWER_MEAN = 9453741;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PDSCH_PTRS_RE_POWER_MEAN = 9453742;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_CROSS_POWER_MEAN = 9453743;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_TIME_ALIGNMENT_ERROR_MEAN = 9453744;
  NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PDSCH_4096QAM_RMS_EVM_MEAN = 9453746;
  NIRFMXNR_ATTRIBUTE_OBW_MEASUREMENT_ENABLED = 9461760;
  NIRFMXNR_ATTRIBUTE_OBW_SPAN = 9461763;
  NIRFMXNR_ATTRIBUTE_OBW_RBW_FILTER_AUTO_BANDWIDTH = 9461766;
  NIRFMXNR_ATTRIBUTE_OBW_RBW_FILTER_BANDWIDTH = 9461767;
  NIRFMXNR_ATTRIBUTE_OBW_RBW_FILTER_TYPE = 9461768;
  NIRFMXNR_ATTRIBUTE_OBW_SWEEP_TIME_AUTO = 9461769;
  NIRFMXNR_ATTRIBUTE_OBW_SWEEP_TIME_INTERVAL = 9461770;
  NIRFMXNR_ATTRIBUTE_OBW_AVERAGING_ENABLED = 9461771;
  NIRFMXNR_ATTRIBUTE_OBW_AVERAGING_COUNT = 9461772;
  NIRFMXNR_ATTRIBUTE_OBW_AVERAGING_TYPE = 9461774;
  NIRFMXNR_ATTRIBUTE_OBW_FFT_WINDOW = 9461775;
  NIRFMXNR_ATTRIBUTE_OBW_AMPLITUDE_CORRECTION_TYPE = 9461777;
  NIRFMXNR_ATTRIBUTE_OBW_ALL_TRACES_ENABLED = 9461778;
  NIRFMXNR_ATTRIBUTE_OBW_NUMBER_OF_ANALYSIS_THREADS = 9461779;
  NIRFMXNR_ATTRIBUTE_OBW_RESULTS_OCCUPIED_BANDWIDTH = 9461781;
  NIRFMXNR_ATTRIBUTE_OBW_RESULTS_ABSOLUTE_POWER = 9461782;
  NIRFMXNR_ATTRIBUTE_OBW_RESULTS_START_FREQUENCY = 9461783;
  NIRFMXNR_ATTRIBUTE_OBW_RESULTS_STOP_FREQUENCY = 9461784;
  NIRFMXNR_ATTRIBUTE_OBW_SPAN_AUTO = 9461786;
  NIRFMXNR_ATTRIBUTE_OBW_POWER_INTEGRATION_METHOD = 9461792;
  NIRFMXNR_ATTRIBUTE_TXP_MEASUREMENT_ENABLED = 9465856;
  NIRFMXNR_ATTRIBUTE_TXP_MEASUREMENT_OFFSET = 9465858;
  NIRFMXNR_ATTRIBUTE_TXP_MEASUREMENT_INTERVAL = 9465859;
  NIRFMXNR_ATTRIBUTE_TXP_AVERAGING_ENABLED = 9465860;
  NIRFMXNR_ATTRIBUTE_TXP_AVERAGING_COUNT = 9465861;
  NIRFMXNR_ATTRIBUTE_TXP_ALL_TRACES_ENABLED = 9465863;
  NIRFMXNR_ATTRIBUTE_TXP_NUMBER_OF_ANALYSIS_THREADS = 9465864;
  NIRFMXNR_ATTRIBUTE_TXP_RESULTS_AVERAGE_POWER_MEAN = 9465866;
  NIRFMXNR_ATTRIBUTE_TXP_RESULTS_PEAK_POWER_MAXIMUM = 9465867;
  NIRFMXNR_ATTRIBUTE_SEM_MEASUREMENT_ENABLED = 9469952;
  NIRFMXNR_ATTRIBUTE_SEM_UPLINK_MASK_TYPE = 9469954;
  NIRFMXNR_ATTRIBUTE_SEM_SUBBLOCK_INTEGRATION_BANDWIDTH = 9469955;
  NIRFMXNR_ATTRIBUTE_SEM_SUBBLOCK_AGGREGATED_CHANNEL_BANDWIDTH = 9469956;
  NIRFMXNR_ATTRIBUTE_SEM_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH = 9469957;
  NIRFMXNR_ATTRIBUTE_SEM_NUMBER_OF_OFFSETS = 9469958;
  NIRFMXNR_ATTRIBUTE_SEM_OFFSET_START_FREQUENCY = 9469959;
  NIRFMXNR_ATTRIBUTE_SEM_OFFSET_STOP_FREQUENCY = 9469960;
  NIRFMXNR_ATTRIBUTE_SEM_OFFSET_SIDEBAND = 9469961;
  NIRFMXNR_ATTRIBUTE_SEM_OFFSET_RBW_FILTER_BANDWIDTH = 9469962;
  NIRFMXNR_ATTRIBUTE_SEM_OFFSET_RBW_FILTER_TYPE = 9469963;
  NIRFMXNR_ATTRIBUTE_SEM_OFFSET_BANDWIDTH_INTEGRAL = 9469964;
  NIRFMXNR_ATTRIBUTE_SEM_OFFSET_LIMIT_FAIL_MASK = 9469965;
  NIRFMXNR_ATTRIBUTE_SEM_OFFSET_ABSOLUTE_LIMIT_START = 9469966;
  NIRFMXNR_ATTRIBUTE_SEM_OFFSET_ABSOLUTE_LIMIT_STOP = 9469967;
  NIRFMXNR_ATTRIBUTE_SEM_OFFSET_RELATIVE_LIMIT_START = 9469968;
  NIRFMXNR_ATTRIBUTE_SEM_OFFSET_RELATIVE_LIMIT_STOP = 9469969;
  NIRFMXNR_ATTRIBUTE_SEM_SWEEP_TIME_AUTO = 9469970;
  NIRFMXNR_ATTRIBUTE_SEM_SWEEP_TIME_INTERVAL = 9469971;
  NIRFMXNR_ATTRIBUTE_SEM_AVERAGING_ENABLED = 9469972;
  NIRFMXNR_ATTRIBUTE_SEM_AVERAGING_COUNT = 9469973;
  NIRFMXNR_ATTRIBUTE_SEM_AVERAGING_TYPE = 9469974;
  NIRFMXNR_ATTRIBUTE_SEM_AMPLITUDE_CORRECTION_TYPE = 9469975;
  NIRFMXNR_ATTRIBUTE_SEM_ALL_TRACES_ENABLED = 9469976;
  NIRFMXNR_ATTRIBUTE_SEM_NUMBER_OF_ANALYSIS_THREADS = 9469977;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_TOTAL_AGGREGATED_POWER = 9469979;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_MEASUREMENT_STATUS = 9469980;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_SUBBLOCK_POWER = 9469983;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_INTEGRATED_POWER = 9469984;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_COMPONENT_CARRIER_RELATIVE_INTEGRATED_POWER = 9469985;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_PEAK_POWER = 9469986;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_COMPONENT_CARRIER_PEAK_FREQUENCY = 9469987;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS = 9469988;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER = 9469989;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER = 9469990;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER = 9469991;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER = 9469992;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY = 9469993;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_MARGIN = 9469994;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER = 9469995;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER = 9469996;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY = 9469997;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS = 9469998;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER = 9469999;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER = 9470000;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER = 9470001;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER = 9470002;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY = 9470003;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_MARGIN = 9470004;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER = 9470005;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER = 9470006;
  NIRFMXNR_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY = 9470007;
  NIRFMXNR_ATTRIBUTE_SEM_DOWNLINK_MASK_TYPE = 9470008;
  NIRFMXNR_ATTRIBUTE_SEM_DELTA_F_MAXIMUM = 9470009;
  NIRFMXNR_ATTRIBUTE_SEM_COMPONENT_CARRIER_RATED_OUTPUT_POWER = 9470010;
  NIRFMXNR_ATTRIBUTE_SEM_FFT_WINDOW = 9470016;
  NIRFMXNR_ATTRIBUTE_SEM_OFFSET_FREQUENCY_DEFINITION = 9470018;
  NIRFMXNR_ATTRIBUTE_PVT_MEASUREMENT_ENABLED = 9474048;
  NIRFMXNR_ATTRIBUTE_PVT_MEASUREMENT_METHOD = 9474050;
  NIRFMXNR_ATTRIBUTE_PVT_AVERAGING_ENABLED = 9474051;
  NIRFMXNR_ATTRIBUTE_PVT_AVERAGING_COUNT = 9474052;
  NIRFMXNR_ATTRIBUTE_PVT_AVERAGING_TYPE = 9474053;
  NIRFMXNR_ATTRIBUTE_PVT_OFF_POWER_EXCLUSION_BEFORE = 9474055;
  NIRFMXNR_ATTRIBUTE_PVT_OFF_POWER_EXCLUSION_AFTER = 9474056;
  NIRFMXNR_ATTRIBUTE_PVT_ALL_TRACES_ENABLED = 9474057;
  NIRFMXNR_ATTRIBUTE_PVT_NUMBER_OF_ANALYSIS_THREADS = 9474059;
  NIRFMXNR_ATTRIBUTE_PVT_RESULTS_MEASUREMENT_STATUS = 9474060;
  NIRFMXNR_ATTRIBUTE_PVT_RESULTS_ABSOLUTE_OFF_POWER_BEFORE = 9474061;
  NIRFMXNR_ATTRIBUTE_PVT_RESULTS_ABSOLUTE_OFF_POWER_AFTER = 9474062;
  NIRFMXNR_ATTRIBUTE_PVT_RESULTS_ABSOLUTE_ON_POWER = 9474063;
  NIRFMXNR_ATTRIBUTE_PVT_RESULTS_BURST_WIDTH = 9474064;
  NIRFMXNR_ATTRIBUTE_PVT_MEASUREMENT_INTERVAL_AUTO = 9474068;
  NIRFMXNR_ATTRIBUTE_PVT_MEASUREMENT_INTERVAL = 9474069;
  NIRFMXNR_ATTRIBUTE_PVT_RESULTS_PEAK_WINDOWED_OFF_POWER = 9474070;
  NIRFMXNR_ATTRIBUTE_PVT_RESULTS_PEAK_WINDOWED_OFF_POWER_MARGIN = 9474071;
  NIRFMXNR_ATTRIBUTE_PVT_RESULTS_PEAK_WINDOWED_OFF_POWER_TIME = 9474072;
  NIRFMXNR_ATTRIBUTE_RESULT_FETCH_TIMEOUT = 9486336;
  NIRFMXNR_ATTRIBUTE_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED = 9490433;
  NIRFMXNR_ATTRIBUTE_LIMITED_CONFIGURATION_CHANGE = 9490434;
  NIRFMXNR_ATTRIBUTE_NUMBER_OF_RECEIVE_CHAINS = 9490435;
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

enum AcpNoiseCalibrationDataValid {
  ACP_NOISE_CALIBRATION_DATA_VALID_FALSE = 0;
  ACP_NOISE_CALIBRATION_DATA_VALID_TRUE = 1;
}

enum AcpNoiseCompensationEnabled {
  ACP_NOISE_COMPENSATION_ENABLED_FALSE = 0;
  ACP_NOISE_COMPENSATION_ENABLED_TRUE = 1;
}

enum AcpPowerUnits {
  ACP_POWER_UNITS_DBM = 0;
  ACP_POWER_UNITS_DBM_BY_HZ = 1;
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

enum ChpNoiseCalibrationDataValid {
  CHP_NOISE_CALIBRATION_DATA_VALID_FALSE = 0;
  CHP_NOISE_CALIBRATION_DATA_VALID_TRUE = 1;
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
  FREQUENCY_REFERENCE_SOURCE_REF_IN2 = 5;
  FREQUENCY_REFERENCE_SOURCE_PXI_CLK_MASTER = 6;
}

enum GNodeBCategory {
  GNODEB_CATEGORY_WIDE_AREA_BASE_STATION_CATEGORY_A = 0;
  GNODEB_CATEGORY_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION1 = 1;
  GNODEB_CATEGORY_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION2 = 2;
  GNODEB_CATEGORY_LOCAL_AREA_BASE_STATION = 3;
  GNODEB_CATEGORY_MEDIUM_RANGE_BASE_STATION = 5;
  GNODEB_CATEGORY_FR2_CATEGORY_A = 6;
  GNODEB_CATEGORY_FR2_CATEGORY_B = 7;
}

enum IQPowerEdgeTriggerLevelType {
  IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE = 0;
  IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE = 1;
}

enum IQPowerEdgeTriggerSlope {
  IQ_POWER_EDGE_TRIGGER_SLOPE_RISING = 0;
  IQ_POWER_EDGE_TRIGGER_SLOPE_FALLING = 1;
}

enum MeasurementTypes {
  MEASUREMENT_TYPES_UNSPECIFIED = 0;
  MEASUREMENT_TYPES_MODACC = 1;
  MEASUREMENT_TYPES_SEM = 2;
  MEASUREMENT_TYPES_ACP = 4;
  MEASUREMENT_TYPES_CHP = 8;
  MEASUREMENT_TYPES_OBW = 16;
  MEASUREMENT_TYPES_PVT = 32;
  MEASUREMENT_TYPES_TXP = 64;
}

enum MechanicalAttenuationAuto {
  MECHANICAL_ATTENUATION_AUTO_FALSE = 0;
  MECHANICAL_ATTENUATION_AUTO_TRUE = 1;
}

enum ModAccCalibrationDataValid {
  MODACC_CALIBRATION_DATA_VALID_FALSE = 0;
  MODACC_CALIBRATION_DATA_VALID_TRUE = 1;
}

enum ModAccMeasurementMode {
  MODACC_MEASUREMENT_MODE_MEASURE = 0;
  MODACC_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR = 1;
}

enum ModAccNoiseCompensationEnabled {
  MODACC_NOISE_COMPENSATION_ENABLED_FALSE = 0;
  MODACC_NOISE_COMPENSATION_ENABLED_TRUE = 1;
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

enum PvtAveragingEnabled {
  PVT_AVERAGING_ENABLED_FALSE = 0;
  PVT_AVERAGING_ENABLED_TRUE = 1;
}

enum PvtAveragingType {
  PVT_AVERAGING_TYPE_RMS = 0;
  PVT_AVERAGING_TYPE_LOG = 1;
}

enum PvtMeasurementMethod {
  PVT_MEASUREMENT_METHOD_NORMAL = 0;
  PVT_MEASUREMENT_METHOD_DYNAMIC_RANGE = 1;
}

enum PvtMeasurementStatus {
  PVT_MEASUREMENT_STATUS_FAIL = 0;
  PVT_MEASUREMENT_STATUS_PASS = 1;
}

enum RFAttenuationAuto {
  RF_ATTENUATION_AUTO_FALSE = 0;
  RF_ATTENUATION_AUTO_TRUE = 1;
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

enum SemOffsetLimitFailMask {
  SEM_OFFSET_LIMIT_FAIL_MASK_ABS_AND_REL = 0;
  SEM_OFFSET_LIMIT_FAIL_MASK_ABS_OR_REL = 1;
  SEM_OFFSET_LIMIT_FAIL_MASK_ABSOLUTE = 2;
  SEM_OFFSET_LIMIT_FAIL_MASK_RELATIVE = 3;
}

enum SemOffsetRbwFilterType {
  SEM_OFFSET_RBW_FILTER_TYPE_FFT_BASED = 0;
  SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN = 1;
  SEM_OFFSET_RBW_FILTER_TYPE_FLAT = 2;
}

enum SemOffsetSideband {
  SEM_OFFSET_SIDEBAND_NEGATIVE = 0;
  SEM_OFFSET_SIDEBAND_POSITIVE = 1;
  SEM_OFFSET_SIDEBAND_BOTH = 2;
}

enum SemSweepTimeAuto {
  SEM_SWEEP_TIME_AUTO_FALSE = 0;
  SEM_SWEEP_TIME_AUTO_TRUE = 1;
}

enum SemUplinkMaskType {
  SEM_UPLINK_MASK_TYPE_GENERAL = 0;
  SEM_UPLINK_MASK_TYPE_NS35 = 1;
  SEM_UPLINK_MASK_TYPE_CUSTOM = 2;
  SEM_UPLINK_MASK_TYPE_NS03 = 3;
  SEM_UPLINK_MASK_TYPE_NS04 = 4;
  SEM_UPLINK_MASK_TYPE_NS06 = 5;
  SEM_UPLINK_MASK_TYPE_NS21 = 6;
  SEM_UPLINK_MASK_TYPE_NS27 = 7;
  SEM_UPLINK_MASK_TYPE_NS07 = 8;
  SEM_UPLINK_MASK_TYPE_NS03U = 9;
  SEM_UPLINK_MASK_TYPE_NS21_REL_17_ONWARDS = 10;
  SEM_UPLINK_MASK_TYPE_NS04N = 11;
  SEM_UPLINK_MASK_TYPE_NS05N = 12;
  SEM_UPLINK_MASK_TYPE_NS09N = 13;
  SEM_UPLINK_MASK_TYPE_NS10N = 14;
  SEM_UPLINK_MASK_TYPE_NS11N = 15;
  SEM_UPLINK_MASK_TYPE_NS12N = 16;
  SEM_UPLINK_MASK_TYPE_NS203N = 17;
  SEM_UPLINK_MASK_TYPE_NS204N = 18;
  SEM_UPLINK_MASK_TYPE_NS207N = 19;
  SEM_UPLINK_MASK_TYPE_NS208N = 20;
  SEM_UPLINK_MASK_TYPE_NS02N = 21;
  SEM_UPLINK_MASK_TYPE_NS03N = 22;
  SEM_UPLINK_MASK_TYPE_NS06N = 23;
  SEM_UPLINK_MASK_TYPE_NS07N = 24;
  SEM_UPLINK_MASK_TYPE_NS08N = 25;
}

enum SemUpperOffsetMeasurementStatus {
  SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL = 0;
  SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS = 1;
}

enum TriggerMinimumQuietTimeMode {
  TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL = 0;
  TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO = 1;
}

enum NiRFmxNRInt32AttributeValues {
  option allow_alias = true;
  NIRFMXNR_INT32_UNSPECIFIED = 0;
  NIRFMXNR_INT32_ACP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY = 0;
  NIRFMXNR_INT32_ACP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN = 1;
  NIRFMXNR_INT32_ACP_AVERAGING_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_ACP_AVERAGING_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_ACP_AVERAGING_TYPE_RMS = 0;
  NIRFMXNR_INT32_ACP_AVERAGING_TYPE_LOG = 1;
  NIRFMXNR_INT32_ACP_AVERAGING_TYPE_SCALAR = 2;
  NIRFMXNR_INT32_ACP_AVERAGING_TYPE_MAXIMUM = 3;
  NIRFMXNR_INT32_ACP_AVERAGING_TYPE_MINIMUM = 4;
  NIRFMXNR_INT32_ACP_CHANNEL_CONFIGURATION_TYPE_STANDARD = 0;
  NIRFMXNR_INT32_ACP_CHANNEL_CONFIGURATION_TYPE_CUSTOM = 1;
  NIRFMXNR_INT32_ACP_CHANNEL_CONFIGURATION_TYPE_NS_29 = 2;
  NIRFMXNR_INT32_ACP_CHANNEL_CONFIGURATION_TYPE_STANDARD_REL_16 = 3;
  NIRFMXNR_INT32_ACP_CHANNEL_CONFIGURATION_TYPE_STANDARD_REL_18 = 4;
  NIRFMXNR_INT32_ACP_FFT_OVERLAP_MODE_DISABLED = 0;
  NIRFMXNR_INT32_ACP_FFT_OVERLAP_MODE_AUTOMATIC = 1;
  NIRFMXNR_INT32_ACP_FFT_OVERLAP_MODE_USER_DEFINED = 2;
  NIRFMXNR_INT32_ACP_FFT_WINDOW_NONE = 0;
  NIRFMXNR_INT32_ACP_FFT_WINDOW_FLAT_TOP = 1;
  NIRFMXNR_INT32_ACP_FFT_WINDOW_HANNING = 2;
  NIRFMXNR_INT32_ACP_FFT_WINDOW_HAMMING = 3;
  NIRFMXNR_INT32_ACP_FFT_WINDOW_GAUSSIAN = 4;
  NIRFMXNR_INT32_ACP_FFT_WINDOW_BLACKMAN = 5;
  NIRFMXNR_INT32_ACP_FFT_WINDOW_BLACKMAN_HARRIS = 6;
  NIRFMXNR_INT32_ACP_FFT_WINDOW_KAISER_BESSEL = 7;
  NIRFMXNR_INT32_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE = 0;
  NIRFMXNR_INT32_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE = 1;
  NIRFMXNR_INT32_ACP_MEASUREMENT_METHOD_NORMAL = 0;
  NIRFMXNR_INT32_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE = 1;
  NIRFMXNR_INT32_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT = 2;
  NIRFMXNR_INT32_ACP_MEASUREMENT_MODE_MEASURE = 0;
  NIRFMXNR_INT32_ACP_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR = 1;
  NIRFMXNR_INT32_ACP_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE = 0;
  NIRFMXNR_INT32_ACP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE = 1;
  NIRFMXNR_INT32_ACP_NOISE_CALIBRATION_MODE_MANUAL = 0;
  NIRFMXNR_INT32_ACP_NOISE_CALIBRATION_MODE_AUTO = 1;
  NIRFMXNR_INT32_ACP_NOISE_COMPENSATION_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_ACP_NOISE_COMPENSATION_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_ACP_NOISE_COMPENSATION_TYPE_ANALYZER_AND_TERMINATION = 0;
  NIRFMXNR_INT32_ACP_NOISE_COMPENSATION_TYPE_ANALYZER_ONLY = 1;
  NIRFMXNR_INT32_ACP_OFFSET_SIDEBAND_NEGATIVE = 0;
  NIRFMXNR_INT32_ACP_OFFSET_SIDEBAND_POSITIVE = 1;
  NIRFMXNR_INT32_ACP_OFFSET_SIDEBAND_BOTH = 2;
  NIRFMXNR_INT32_ACP_POWER_UNITS_DBM = 0;
  NIRFMXNR_INT32_ACP_POWER_UNITS_DBM_BY_HZ = 1;
  NIRFMXNR_INT32_ACP_RBW_AUTO_BANDWIDTH_FALSE = 0;
  NIRFMXNR_INT32_ACP_RBW_AUTO_BANDWIDTH_TRUE = 1;
  NIRFMXNR_INT32_ACP_RBW_FILTER_TYPE_FFT_BASED = 0;
  NIRFMXNR_INT32_ACP_RBW_FILTER_TYPE_GAUSSIAN = 1;
  NIRFMXNR_INT32_ACP_RBW_FILTER_TYPE_FLAT = 2;
  NIRFMXNR_INT32_ACP_SWEEP_TIME_AUTO_FALSE = 0;
  NIRFMXNR_INT32_ACP_SWEEP_TIME_AUTO_TRUE = 1;
  NIRFMXNR_INT32_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_AUTO_CELL_ID_DETECTION_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_AUTO_CELL_ID_DETECTION_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_AUTO_INCREMENT_CELL_ID_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_AUTO_INCREMENT_CELL_ID_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_BANDWIDTH_PART_CYCLIC_PREFIX_MODE_NORMAL = 0;
  NIRFMXNR_INT32_BANDWIDTH_PART_CYCLIC_PREFIX_MODE_EXTENDED = 1;
  NIRFMXNR_INT32_BANDWIDTH_PART_DC_LOCATION_KNOWN_FALSE = 0;
  NIRFMXNR_INT32_BANDWIDTH_PART_DC_LOCATION_KNOWN_TRUE = 1;
  NIRFMXNR_INT32_CHP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY = 0;
  NIRFMXNR_INT32_CHP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN = 1;
  NIRFMXNR_INT32_CHP_AVERAGING_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_CHP_AVERAGING_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_CHP_AVERAGING_TYPE_RMS = 0;
  NIRFMXNR_INT32_CHP_AVERAGING_TYPE_LOG = 1;
  NIRFMXNR_INT32_CHP_AVERAGING_TYPE_SCALAR = 2;
  NIRFMXNR_INT32_CHP_AVERAGING_TYPE_MAXIMUM = 3;
  NIRFMXNR_INT32_CHP_AVERAGING_TYPE_MINIMUM = 4;
  NIRFMXNR_INT32_CHP_FFT_WINDOW_NONE = 0;
  NIRFMXNR_INT32_CHP_FFT_WINDOW_FLAT_TOP = 1;
  NIRFMXNR_INT32_CHP_FFT_WINDOW_HANNING = 2;
  NIRFMXNR_INT32_CHP_FFT_WINDOW_HAMMING = 3;
  NIRFMXNR_INT32_CHP_FFT_WINDOW_GAUSSIAN = 4;
  NIRFMXNR_INT32_CHP_FFT_WINDOW_BLACKMAN = 5;
  NIRFMXNR_INT32_CHP_FFT_WINDOW_BLACKMAN_HARRIS = 6;
  NIRFMXNR_INT32_CHP_FFT_WINDOW_KAISER_BESSEL = 7;
  NIRFMXNR_INT32_CHP_INTEGRATION_BANDWIDTH_TYPE_SIGNAL_BANDWIDTH = 0;
  NIRFMXNR_INT32_CHP_INTEGRATION_BANDWIDTH_TYPE_CHANNEL_BANDWIDTH = 1;
  NIRFMXNR_INT32_CHP_MEASUREMENT_MODE_MEASURE = 0;
  NIRFMXNR_INT32_CHP_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR = 1;
  NIRFMXNR_INT32_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE = 0;
  NIRFMXNR_INT32_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE = 1;
  NIRFMXNR_INT32_CHP_NOISE_CALIBRATION_MODE_MANUAL = 0;
  NIRFMXNR_INT32_CHP_NOISE_CALIBRATION_MODE_AUTO = 1;
  NIRFMXNR_INT32_CHP_NOISE_COMPENSATION_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_CHP_NOISE_COMPENSATION_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_CHP_NOISE_COMPENSATION_TYPE_ANALYZER_AND_TERMINATION = 0;
  NIRFMXNR_INT32_CHP_NOISE_COMPENSATION_TYPE_ANALYZER_ONLY = 1;
  NIRFMXNR_INT32_CHP_RBW_AUTO_BANDWIDTH_FALSE = 0;
  NIRFMXNR_INT32_CHP_RBW_AUTO_BANDWIDTH_TRUE = 1;
  NIRFMXNR_INT32_CHP_RBW_FILTER_TYPE_FFT_BASED = 0;
  NIRFMXNR_INT32_CHP_RBW_FILTER_TYPE_GAUSSIAN = 1;
  NIRFMXNR_INT32_CHP_RBW_FILTER_TYPE_FLAT = 2;
  NIRFMXNR_INT32_CHP_SWEEP_TIME_AUTO_FALSE = 0;
  NIRFMXNR_INT32_CHP_SWEEP_TIME_AUTO_TRUE = 1;
  NIRFMXNR_INT32_COMPONENT_CARRIER_ALLOCATED_FALSE = 0;
  NIRFMXNR_INT32_COMPONENT_CARRIER_ALLOCATED_TRUE = 1;
  NIRFMXNR_INT32_COMPONENT_CARRIER_RADIO_ACCESS_TYPE_NR = 0;
  NIRFMXNR_INT32_COMPONENT_CARRIER_RADIO_ACCESS_TYPE_EUTRA = 1;
  NIRFMXNR_INT32_COMPONENT_CARRIER_SPACING_TYPE_NOMINAL = 0;
  NIRFMXNR_INT32_COMPONENT_CARRIER_SPACING_TYPE_USER = 2;
  NIRFMXNR_INT32_CORESET_CCE_TO_REG_MAPPING_TYPE_NON_INTERLEAVED = 0;
  NIRFMXNR_INT32_CORESET_CCE_TO_REG_MAPPING_TYPE_INTERLEAVED = 1;
  NIRFMXNR_INT32_CORESET_PRECODING_GRANULARITY_SAME_AS_REG_BUNDLE = 0;
  NIRFMXNR_INT32_CORESET_PRECODING_GRANULARITY_ALL_CONTIGUOUS_RESOURCE_BLOCKS = 1;
  NIRFMXNR_INT32_DIGITAL_EDGE_TRIGGER_EDGE_RISING = 0;
  NIRFMXNR_INT32_DIGITAL_EDGE_TRIGGER_EDGE_FALLING = 1;
  NIRFMXNR_INT32_DOWNLINK_CHANNEL_CONFIGURATION_MODE_USER_DEFINED = 1;
  NIRFMXNR_INT32_DOWNLINK_CHANNEL_CONFIGURATION_MODE_TEST_MODEL = 2;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_TM1_1 = 0;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_TM1_2 = 1;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_TM2 = 2;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_TM2A = 3;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_TM3_1 = 4;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_TM3_1A = 5;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_TM3_2 = 6;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_TM3_3 = 7;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_TM2B = 8;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_TM3_1B = 9;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_CELL_ID_MODE_AUTO = 0;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_CELL_ID_MODE_MANUAL = 1;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_DUPLEX_SCHEME_FDD = 0;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_DUPLEX_SCHEME_TDD = 1;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_MODULATION_TYPE_STANDARD = 0;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_MODULATION_TYPE_QPSK = 1;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_MODULATION_TYPE_QAM16 = 2;
  NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_MODULATION_TYPE_QAM64 = 3;
  NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE1 = 0;
  NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE2_1 = 1;
  NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE2_2 = 2;
  NIRFMXNR_INT32_GNODEB_CATEGORY_WIDE_AREA_BASE_STATION_CATEGORY_A = 0;
  NIRFMXNR_INT32_GNODEB_CATEGORY_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION1 = 1;
  NIRFMXNR_INT32_GNODEB_CATEGORY_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION2 = 2;
  NIRFMXNR_INT32_GNODEB_CATEGORY_LOCAL_AREA_BASE_STATION = 3;
  NIRFMXNR_INT32_GNODEB_CATEGORY_MEDIUM_RANGE_BASE_STATION = 5;
  NIRFMXNR_INT32_GNODEB_CATEGORY_FR2_CATEGORY_A = 6;
  NIRFMXNR_INT32_GNODEB_CATEGORY_FR2_CATEGORY_B = 7;
  NIRFMXNR_INT32_GNODEB_TYPE_1C = 0;
  NIRFMXNR_INT32_GNODEB_TYPE_1H = 1;
  NIRFMXNR_INT32_GNODEB_TYPE_1O = 2;
  NIRFMXNR_INT32_GNODEB_TYPE_2O = 3;
  NIRFMXNR_INT32_GRID_SIZE_MODE_MANUAL = 0;
  NIRFMXNR_INT32_GRID_SIZE_MODE_AUTO = 1;
  NIRFMXNR_INT32_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE = 0;
  NIRFMXNR_INT32_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE = 1;
  NIRFMXNR_INT32_IQ_POWER_EDGE_TRIGGER_SLOPE_RISING = 0;
  NIRFMXNR_INT32_IQ_POWER_EDGE_TRIGGER_SLOPE_FALLING = 1;
  NIRFMXNR_INT32_LIMITED_CONFIGURATION_CHANGE_DISABLED = 0;
  NIRFMXNR_INT32_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE = 1;
  NIRFMXNR_INT32_LIMITED_CONFIGURATION_CHANGE_FREQUENCY = 2;
  NIRFMXNR_INT32_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL = 3;
  NIRFMXNR_INT32_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL = 4;
  NIRFMXNR_INT32_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL = 5;
  NIRFMXNR_INT32_LINK_DIRECTION_DOWNLINK = 0;
  NIRFMXNR_INT32_LINK_DIRECTION_UPLINK = 1;
  NIRFMXNR_INT32_LIST_STEP_TIMER_UNIT_SLOT = 1;
  NIRFMXNR_INT32_LIST_STEP_TIMER_UNIT_TIME = 6;
  NIRFMXNR_INT32_MODACC_AUTO_LEVEL_ALLOW_OVERFLOW_FALSE = 0;
  NIRFMXNR_INT32_MODACC_AUTO_LEVEL_ALLOW_OVERFLOW_TRUE = 1;
  NIRFMXNR_INT32_MODACC_AVERAGING_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_MODACC_AVERAGING_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_MODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE = 0;
  NIRFMXNR_INT32_MODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE_AND_DATA = 1;
  NIRFMXNR_INT32_MODACC_COMMON_CLOCK_SOURCE_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_MODACC_COMMON_CLOCK_SOURCE_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_MODACC_COMPOSITE_RESULTS_INCLUDE_DMRS_FALSE = 0;
  NIRFMXNR_INT32_MODACC_COMPOSITE_RESULTS_INCLUDE_DMRS_TRUE = 1;
  NIRFMXNR_INT32_MODACC_COMPOSITE_RESULTS_INCLUDE_PTRS_FALSE = 0;
  NIRFMXNR_INT32_MODACC_COMPOSITE_RESULTS_INCLUDE_PTRS_TRUE = 1;
  NIRFMXNR_INT32_MODACC_DC_SUBCARRIER_REMOVAL_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_MODACC_DC_SUBCARRIER_REMOVAL_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE_ACQUIRED_WAVEFORM = 0;
  NIRFMXNR_INT32_MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE_REFERENCE_WAVEFORM = 1;
  NIRFMXNR_INT32_MODACC_EVM_UNIT_PERCENTAGE = 0;
  NIRFMXNR_INT32_MODACC_EVM_UNIT_DB = 1;
  NIRFMXNR_INT32_MODACC_FFT_WINDOW_TYPE_3GPP = 0;
  NIRFMXNR_INT32_MODACC_FFT_WINDOW_TYPE_CUSTOM = 1;
  NIRFMXNR_INT32_MODACC_FREQUENCY_ERROR_ESTIMATION_DISABLED = 0;
  NIRFMXNR_INT32_MODACC_FREQUENCY_ERROR_ESTIMATION_NORMAL = 1;
  NIRFMXNR_INT32_MODACC_FREQUENCY_ERROR_ESTIMATION_WIDE = 2;
  NIRFMXNR_INT32_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_MODACC_IQ_IMPAIRMENTS_MODEL_TX = 0;
  NIRFMXNR_INT32_MODACC_IQ_IMPAIRMENTS_MODEL_RX = 1;
  NIRFMXNR_INT32_MODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_MODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_MODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_MODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_MODACC_MEASUREMENT_LENGTH_UNIT_SLOT = 1;
  NIRFMXNR_INT32_MODACC_MEASUREMENT_LENGTH_UNIT_SUBFRAME = 3;
  NIRFMXNR_INT32_MODACC_MEASUREMENT_LENGTH_UNIT_TIME = 6;
  NIRFMXNR_INT32_MODACC_MEASUREMENT_MODE_MEASURE = 0;
  NIRFMXNR_INT32_MODACC_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR = 1;
  NIRFMXNR_INT32_MODACC_MULTICARRIER_FILTER_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_MODACC_MULTICARRIER_FILTER_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_MODACC_NOISE_COMPENSATION_APPLIED_FALSE = 0;
  NIRFMXNR_INT32_MODACC_NOISE_COMPENSATION_APPLIED_TRUE = 1;
  NIRFMXNR_INT32_MODACC_NOISE_COMPENSATION_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_MODACC_NOISE_COMPENSATION_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_MODACC_NOISE_COMPENSATION_INPUT_POWER_CHECK_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_MODACC_NOISE_COMPENSATION_INPUT_POWER_CHECK_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_MODACC_PHASE_TRACKING_MODE_DISABLED = 0;
  NIRFMXNR_INT32_MODACC_PHASE_TRACKING_MODE_REFERENCE_AND_DATA = 1;
  NIRFMXNR_INT32_MODACC_PHASE_TRACKING_MODE_PTRS = 2;
  NIRFMXNR_INT32_MODACC_PRE_FFT_ERROR_ESTIMATION_INTERVAL_SLOT = 0;
  NIRFMXNR_INT32_MODACC_PRE_FFT_ERROR_ESTIMATION_INTERVAL_MEASUREMENT_LENGTH = 1;
  NIRFMXNR_INT32_MODACC_SHORT_FRAME_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_MODACC_SHORT_FRAME_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_MODACC_SHORT_FRAME_LENGTH_UNIT_SLOT = 1;
  NIRFMXNR_INT32_MODACC_SHORT_FRAME_LENGTH_UNIT_SUBFRAME = 3;
  NIRFMXNR_INT32_MODACC_SHORT_FRAME_LENGTH_UNIT_TIME = 6;
  NIRFMXNR_INT32_MODACC_SPECTRAL_FLATNESS_CONDITION_NORMAL = 0;
  NIRFMXNR_INT32_MODACC_SPECTRAL_FLATNESS_CONDITION_EXTREME = 1;
  NIRFMXNR_INT32_MODACC_SPECTRUM_INVERTED_FALSE = 0;
  NIRFMXNR_INT32_MODACC_SPECTRUM_INVERTED_TRUE = 1;
  NIRFMXNR_INT32_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_MODACC_SYNCHRONIZATION_MODE_SLOT = 1;
  NIRFMXNR_INT32_MODACC_SYNCHRONIZATION_MODE_FRAME = 5;
  NIRFMXNR_INT32_MODACC_SYNCHRONIZATION_MODE_SSB_START_FRAME = 7;
  NIRFMXNR_INT32_MODACC_TIMING_TRACKING_MODE_DISABLED = 0;
  NIRFMXNR_INT32_MODACC_TIMING_TRACKING_MODE_REFERENCE_AND_DATA = 1;
  NIRFMXNR_INT32_MODACC_TRANSIENT_PERIOD_EVM_MODE_DISABLED = 0;
  NIRFMXNR_INT32_MODACC_TRANSIENT_PERIOD_EVM_MODE_EXCLUDE = 1;
  NIRFMXNR_INT32_MODACC_TRANSIENT_PERIOD_EVM_MODE_INCLUDE = 2;
  NIRFMXNR_INT32_OBW_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY = 0;
  NIRFMXNR_INT32_OBW_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN = 1;
  NIRFMXNR_INT32_OBW_AVERAGING_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_OBW_AVERAGING_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_OBW_AVERAGING_TYPE_RMS = 0;
  NIRFMXNR_INT32_OBW_AVERAGING_TYPE_LOG = 1;
  NIRFMXNR_INT32_OBW_AVERAGING_TYPE_SCALAR = 2;
  NIRFMXNR_INT32_OBW_AVERAGING_TYPE_MAXIMUM = 3;
  NIRFMXNR_INT32_OBW_AVERAGING_TYPE_MINIMUM = 4;
  NIRFMXNR_INT32_OBW_FFT_WINDOW_NONE = 0;
  NIRFMXNR_INT32_OBW_FFT_WINDOW_FLAT_TOP = 1;
  NIRFMXNR_INT32_OBW_FFT_WINDOW_HANNING = 2;
  NIRFMXNR_INT32_OBW_FFT_WINDOW_HAMMING = 3;
  NIRFMXNR_INT32_OBW_FFT_WINDOW_GAUSSIAN = 4;
  NIRFMXNR_INT32_OBW_FFT_WINDOW_BLACKMAN = 5;
  NIRFMXNR_INT32_OBW_FFT_WINDOW_BLACKMAN_HARRIS = 6;
  NIRFMXNR_INT32_OBW_FFT_WINDOW_KAISER_BESSEL = 7;
  NIRFMXNR_INT32_OBW_POWER_INTEGRATION_METHOD_NORMAL = 0;
  NIRFMXNR_INT32_OBW_POWER_INTEGRATION_METHOD_FROM_CENTER = 1;
  NIRFMXNR_INT32_OBW_RBW_AUTO_BANDWIDTH_FALSE = 0;
  NIRFMXNR_INT32_OBW_RBW_AUTO_BANDWIDTH_TRUE = 1;
  NIRFMXNR_INT32_OBW_RBW_FILTER_TYPE_FFT_BASED = 0;
  NIRFMXNR_INT32_OBW_RBW_FILTER_TYPE_GAUSSIAN = 1;
  NIRFMXNR_INT32_OBW_RBW_FILTER_TYPE_FLAT = 2;
  NIRFMXNR_INT32_OBW_SPAN_AUTO_FALSE = 0;
  NIRFMXNR_INT32_OBW_SPAN_AUTO_TRUE = 1;
  NIRFMXNR_INT32_OBW_SWEEP_TIME_AUTO_FALSE = 0;
  NIRFMXNR_INT32_OBW_SWEEP_TIME_AUTO_TRUE = 1;
  NIRFMXNR_INT32_PDSCH_DMRS_CONFIGURATION_TYPE_1 = 0;
  NIRFMXNR_INT32_PDSCH_DMRS_CONFIGURATION_TYPE_2 = 1;
  NIRFMXNR_INT32_PDSCH_DMRS_DURATION_SINGLE_SYMBOL = 1;
  NIRFMXNR_INT32_PDSCH_DMRS_DURATION_DOUBLE_SYMBOL = 2;
  NIRFMXNR_INT32_PDSCH_DMRS_POWER_MODE_CDM_GROUPS = 0;
  NIRFMXNR_INT32_PDSCH_DMRS_POWER_MODE_USER_DEFINED = 1;
  NIRFMXNR_INT32_PDSCH_DMRS_RELEASE_VERSION_RELEASE15 = 0;
  NIRFMXNR_INT32_PDSCH_DMRS_RELEASE_VERSION_RELEASE16 = 1;
  NIRFMXNR_INT32_PDSCH_DMRS_SCRAMBLING_ID_MODE_CELL_ID = 0;
  NIRFMXNR_INT32_PDSCH_DMRS_SCRAMBLING_ID_MODE_USER_DEFINED = 1;
  NIRFMXNR_INT32_PDSCH_MAPPING_TYPE_A = 0;
  NIRFMXNR_INT32_PDSCH_MAPPING_TYPE_B = 1;
  NIRFMXNR_INT32_PDSCH_MODULATION_TYPE_QPSK = 1;
  NIRFMXNR_INT32_PDSCH_MODULATION_TYPE_QAM16 = 2;
  NIRFMXNR_INT32_PDSCH_MODULATION_TYPE_QAM64 = 3;
  NIRFMXNR_INT32_PDSCH_MODULATION_TYPE_QAM256 = 4;
  NIRFMXNR_INT32_PDSCH_MODULATION_TYPE_QAM1024 = 5;
  NIRFMXNR_INT32_PDSCH_MODULATION_TYPE_PSK8 = 100;
  NIRFMXNR_INT32_PDSCH_MODULATION_TYPE_QAM4096 = 6;
  NIRFMXNR_INT32_PDSCH_PTRS_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_PDSCH_PTRS_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_PDSCH_PTRS_POWER_MODE_STANDARD = 0;
  NIRFMXNR_INT32_PDSCH_PTRS_POWER_MODE_USER_DEFINED = 1;
  NIRFMXNR_INT32_PHASE_COMPENSATION_DISABLED = 0;
  NIRFMXNR_INT32_PHASE_COMPENSATION_AUTO = 1;
  NIRFMXNR_INT32_PHASE_COMPENSATION_USER_DEFINED = 2;
  NIRFMXNR_INT32_PI_BY_2_BPSK_POWER_BOOST_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_PI_BY_2_BPSK_POWER_BOOST_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_PUSCH_DMRS_CONFIGURATION_TYPE_1 = 0;
  NIRFMXNR_INT32_PUSCH_DMRS_CONFIGURATION_TYPE_2 = 1;
  NIRFMXNR_INT32_PUSCH_DMRS_DURATION_SINGLE_SYMBOL = 1;
  NIRFMXNR_INT32_PUSCH_DMRS_DURATION_DOUBLE_SYMBOL = 2;
  NIRFMXNR_INT32_PUSCH_DMRS_GROUP_HOPPING_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_PUSCH_DMRS_GROUP_HOPPING_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_PUSCH_DMRS_POWER_MODE_CDM_GROUPS = 0;
  NIRFMXNR_INT32_PUSCH_DMRS_POWER_MODE_USER_DEFINED = 1;
  NIRFMXNR_INT32_PUSCH_DMRS_PUSCH_ID_MODE_CELL_ID = 0;
  NIRFMXNR_INT32_PUSCH_DMRS_PUSCH_ID_MODE_USER_DEFINED = 1;
  NIRFMXNR_INT32_PUSCH_DMRS_RELEASE_VERSION_RELEASE15 = 0;
  NIRFMXNR_INT32_PUSCH_DMRS_RELEASE_VERSION_RELEASE16 = 1;
  NIRFMXNR_INT32_PUSCH_DMRS_SCRAMBLING_ID_MODE_CELL_ID = 0;
  NIRFMXNR_INT32_PUSCH_DMRS_SCRAMBLING_ID_MODE_USER_DEFINED = 1;
  NIRFMXNR_INT32_PUSCH_DMRS_SEQUENCE_HOPPING_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_PUSCH_DMRS_SEQUENCE_HOPPING_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_PUSCH_MAPPING_TYPE_A = 0;
  NIRFMXNR_INT32_PUSCH_MAPPING_TYPE_B = 1;
  NIRFMXNR_INT32_PUSCH_MODULATION_TYPE_PI_BY_2_BPSK = 0;
  NIRFMXNR_INT32_PUSCH_MODULATION_TYPE_QPSK = 1;
  NIRFMXNR_INT32_PUSCH_MODULATION_TYPE_QAM16 = 2;
  NIRFMXNR_INT32_PUSCH_MODULATION_TYPE_QAM64 = 3;
  NIRFMXNR_INT32_PUSCH_MODULATION_TYPE_QAM256 = 4;
  NIRFMXNR_INT32_PUSCH_MODULATION_TYPE_QAM1024 = 5;
  NIRFMXNR_INT32_PUSCH_MODULATION_TYPE_PSK8 = 100;
  NIRFMXNR_INT32_PUSCH_MODULATION_TYPE_QAM4096 = 6;
  NIRFMXNR_INT32_PUSCH_PTRS_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_PUSCH_PTRS_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_PUSCH_PTRS_POWER_MODE_STANDARD = 0;
  NIRFMXNR_INT32_PUSCH_PTRS_POWER_MODE_USER_DEFINED = 1;
  NIRFMXNR_INT32_PUSCH_TRANSFORM_PRECODING_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_PUSCH_TRANSFORM_PRECODING_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_PVT_AVERAGING_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_PVT_AVERAGING_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_PVT_AVERAGING_TYPE_RMS = 0;
  NIRFMXNR_INT32_PVT_AVERAGING_TYPE_LOG = 1;
  NIRFMXNR_INT32_PVT_MEASUREMENT_INTERVAL_AUTO_FALSE = 0;
  NIRFMXNR_INT32_PVT_MEASUREMENT_INTERVAL_AUTO_TRUE = 1;
  NIRFMXNR_INT32_PVT_MEASUREMENT_METHOD_NORMAL = 0;
  NIRFMXNR_INT32_PVT_MEASUREMENT_METHOD_DYNAMIC_RANGE = 1;
  NIRFMXNR_INT32_PVT_MEASUREMENT_STATUS_FAIL = 0;
  NIRFMXNR_INT32_PVT_MEASUREMENT_STATUS_PASS = 1;
  NIRFMXNR_INT32_REFERENCE_GRID_ALIGNMENT_MODE_MANUAL = 0;
  NIRFMXNR_INT32_REFERENCE_GRID_ALIGNMENT_MODE_AUTO = 1;
  NIRFMXNR_INT32_SATELLITE_ACCESS_NODE_CLASS_GEO = 0;
  NIRFMXNR_INT32_SATELLITE_ACCESS_NODE_CLASS_LEO = 1;
  NIRFMXNR_INT32_SATELLITE_ACCESS_NODE_TYPE_1H = 0;
  NIRFMXNR_INT32_SATELLITE_ACCESS_NODE_TYPE_1O = 1;
  NIRFMXNR_INT32_SATELLITE_ACCESS_NODE_TYPE_2O = 2;
  NIRFMXNR_INT32_SCH_DETECTED_MODULATION_TYPE_PI_BY_2_BPSK = 0;
  NIRFMXNR_INT32_SCH_DETECTED_MODULATION_TYPE_QPSK = 1;
  NIRFMXNR_INT32_SCH_DETECTED_MODULATION_TYPE_QAM16 = 2;
  NIRFMXNR_INT32_SCH_DETECTED_MODULATION_TYPE_QAM64 = 3;
  NIRFMXNR_INT32_SCH_DETECTED_MODULATION_TYPE_QAM256 = 4;
  NIRFMXNR_INT32_SCH_DETECTED_MODULATION_TYPE_QAM1024 = 5;
  NIRFMXNR_INT32_SCH_DETECTED_MODULATION_TYPE_PSK8 = 100;
  NIRFMXNR_INT32_SCH_DETECTED_MODULATION_TYPE_QAM4096 = 6;
  NIRFMXNR_INT32_SEM_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY = 0;
  NIRFMXNR_INT32_SEM_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN = 1;
  NIRFMXNR_INT32_SEM_AVERAGING_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_SEM_AVERAGING_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_SEM_AVERAGING_TYPE_RMS = 0;
  NIRFMXNR_INT32_SEM_AVERAGING_TYPE_LOG = 1;
  NIRFMXNR_INT32_SEM_AVERAGING_TYPE_SCALAR = 2;
  NIRFMXNR_INT32_SEM_AVERAGING_TYPE_MAXIMUM = 3;
  NIRFMXNR_INT32_SEM_AVERAGING_TYPE_MINIMUM = 4;
  NIRFMXNR_INT32_SEM_DOWNLINK_MASK_TYPE_STANDARD = 0;
  NIRFMXNR_INT32_SEM_DOWNLINK_MASK_TYPE_CUSTOM = 2;
  NIRFMXNR_INT32_SEM_FFT_WINDOW_NONE = 0;
  NIRFMXNR_INT32_SEM_FFT_WINDOW_FLAT_TOP = 1;
  NIRFMXNR_INT32_SEM_FFT_WINDOW_HANNING = 2;
  NIRFMXNR_INT32_SEM_FFT_WINDOW_HAMMING = 3;
  NIRFMXNR_INT32_SEM_FFT_WINDOW_GAUSSIAN = 4;
  NIRFMXNR_INT32_SEM_FFT_WINDOW_BLACKMAN = 5;
  NIRFMXNR_INT32_SEM_FFT_WINDOW_BLACKMAN_HARRIS = 6;
  NIRFMXNR_INT32_SEM_FFT_WINDOW_KAISER_BESSEL = 7;
  NIRFMXNR_INT32_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL = 0;
  NIRFMXNR_INT32_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS = 1;
  NIRFMXNR_INT32_SEM_MEASUREMENT_STATUS_FAIL = 0;
  NIRFMXNR_INT32_SEM_MEASUREMENT_STATUS_PASS = 1;
  NIRFMXNR_INT32_SEM_OFFSET_FREQUENCY_DEFINITION_CARRIER_CENTER_TO_MEAS_BW_CENTER = 0;
  NIRFMXNR_INT32_SEM_OFFSET_FREQUENCY_DEFINITION_CARRIER_EDGE_TO_MEAS_BW_CENTER = 2;
  NIRFMXNR_INT32_SEM_OFFSET_FREQUENCY_DEFINITION_SUBBLOCK_EDGE_TO_MEAS_BW_CENTER = 6;
  NIRFMXNR_INT32_SEM_OFFSET_LIMIT_FAIL_MASK_ABS_AND_REL = 0;
  NIRFMXNR_INT32_SEM_OFFSET_LIMIT_FAIL_MASK_ABS_OR_REL = 1;
  NIRFMXNR_INT32_SEM_OFFSET_LIMIT_FAIL_MASK_ABSOLUTE = 2;
  NIRFMXNR_INT32_SEM_OFFSET_LIMIT_FAIL_MASK_RELATIVE = 3;
  NIRFMXNR_INT32_SEM_OFFSET_RBW_FILTER_TYPE_FFT_BASED = 0;
  NIRFMXNR_INT32_SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN = 1;
  NIRFMXNR_INT32_SEM_OFFSET_RBW_FILTER_TYPE_FLAT = 2;
  NIRFMXNR_INT32_SEM_OFFSET_SIDEBAND_NEGATIVE = 0;
  NIRFMXNR_INT32_SEM_OFFSET_SIDEBAND_POSITIVE = 1;
  NIRFMXNR_INT32_SEM_OFFSET_SIDEBAND_BOTH = 2;
  NIRFMXNR_INT32_SEM_SWEEP_TIME_AUTO_FALSE = 0;
  NIRFMXNR_INT32_SEM_SWEEP_TIME_AUTO_TRUE = 1;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_GENERAL = 0;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS35 = 1;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_CUSTOM = 2;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS03 = 3;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS04 = 4;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS06 = 5;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS21 = 6;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS27 = 7;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS07 = 8;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS03U = 9;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS21_REL_17_ONWARDS = 10;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS04N = 11;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS05N = 12;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS09N = 13;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS10N = 14;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS11N = 15;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS12N = 16;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS203N = 17;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS204N = 18;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS207N = 19;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS208N = 20;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS02N = 21;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS03N = 22;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS06N = 23;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS07N = 24;
  NIRFMXNR_INT32_SEM_UPLINK_MASK_TYPE_NS08N = 25;
  NIRFMXNR_INT32_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL = 0;
  NIRFMXNR_INT32_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS = 1;
  NIRFMXNR_INT32_SSB_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_SSB_ENABLED_TRUE = 1;
  NIRFMXNR_INT32_SSB_PATTERN_A_UP_TO_3GHZ = 0;
  NIRFMXNR_INT32_SSB_PATTERN_A_3GHZ_TO_6GHZ = 1;
  NIRFMXNR_INT32_SSB_PATTERN_B_UP_TO_3GHZ = 2;
  NIRFMXNR_INT32_SSB_PATTERN_B_3GHZ_TO_6GHZ = 3;
  NIRFMXNR_INT32_SSB_PATTERN_C_UP_TO_3GHZ = 4;
  NIRFMXNR_INT32_SSB_PATTERN_C_3GHZ_TO_6GHZ = 5;
  NIRFMXNR_INT32_SSB_PATTERN_D = 6;
  NIRFMXNR_INT32_SSB_PATTERN_E = 7;
  NIRFMXNR_INT32_SSB_PATTERN_F = 8;
  NIRFMXNR_INT32_SSB_PATTERN_G = 9;
  NIRFMXNR_INT32_TRANSMITTER_ARCHITECTURE_LO_PER_COMPONENT_CARRIER = 0;
  NIRFMXNR_INT32_TRANSMITTER_ARCHITECTURE_LO_PER_SUBBLOCK = 1;
  NIRFMXNR_INT32_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL = 0;
  NIRFMXNR_INT32_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO = 1;
  NIRFMXNR_INT32_TRIGGER_TYPE_NONE = 0;
  NIRFMXNR_INT32_TRIGGER_TYPE_DIGITAL_EDGE = 1;
  NIRFMXNR_INT32_TRIGGER_TYPE_IQ_POWER_EDGE = 2;
  NIRFMXNR_INT32_TRIGGER_TYPE_SOFTWARE = 3;
  NIRFMXNR_INT32_TXP_AVERAGING_ENABLED_FALSE = 0;
  NIRFMXNR_INT32_TXP_AVERAGING_ENABLED_TRUE = 1;
}

enum NiRFmxNRStringAttributeValuesMapped {
  NIRFMXNR_STRING_MAPPED_UNSPECIFIED = 0;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PFI0 = 1;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PFI1 = 2;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG0 = 3;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG1 = 4;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG2 = 5;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG3 = 6;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG4 = 7;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG5 = 8;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG6 = 9;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG7 = 10;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_STAR = 11;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXIE_DSTARB = 12;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_TIMER_EVENT = 13;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PULSE_IN = 14;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI0 = 15;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI1 = 16;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI2 = 17;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI3 = 18;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI4 = 19;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI5 = 20;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI6 = 21;
  NIRFMXNR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI7 = 22;
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

message ACPCfgNumberOfENDCOffsetsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  int32 number_of_endc_offsets = 3;
}

message ACPCfgNumberOfENDCOffsetsResponse {
  int32 status = 1;
}

message ACPCfgNumberOfEUTRAOffsetsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  int32 number_of_eutra_offsets = 3;
}

message ACPCfgNumberOfEUTRAOffsetsResponse {
  int32 status = 1;
}

message ACPCfgNumberOfNROffsetsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  int32 number_of_nr_offsets = 3;
}

message ACPCfgNumberOfNROffsetsResponse {
  int32 status = 1;
}

message ACPCfgNumberOfUTRAOffsetsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  int32 number_of_utra_offsets = 3;
}

message ACPCfgNumberOfUTRAOffsetsResponse {
  int32 status = 1;
}

message ACPCfgPowerUnitsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof power_units_enum {
    AcpPowerUnits power_units = 3;
    int32 power_units_raw = 4;
  }
}

message ACPCfgPowerUnitsResponse {
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

message ACPFetchComponentCarrierMeasurementRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ACPFetchComponentCarrierMeasurementResponse {
  int32 status = 1;
  double absolute_power = 2;
  double relative_power = 3;
}

message ACPFetchComponentCarrierMeasurementArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ACPFetchComponentCarrierMeasurementArrayResponse {
  int32 status = 1;
  repeated double absolute_power = 2;
  repeated double relative_power = 3;
  int32 actual_array_size = 4;
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

message ACPFetchSubblockMeasurementRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ACPFetchSubblockMeasurementResponse {
  int32 status = 1;
  double subblock_power = 2;
  double integration_bandwidth = 3;
  double frequency = 4;
}

message ACPFetchTotalAggregatedPowerRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ACPFetchTotalAggregatedPowerResponse {
  int32 status = 1;
  double total_aggregated_power = 2;
}

message ACPValidateNoiseCalibrationDataRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
}

message ACPValidateNoiseCalibrationDataResponse {
  int32 status = 1;
  AcpNoiseCalibrationDataValid noise_calibration_data_valid = 2;
  int32 noise_calibration_data_valid_raw = 3;
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

message AnalyzeNWaveformsIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  string result_name = 3;
  repeated double x0 = 4;
  repeated double dx = 5;
  repeated nidevice_grpc.NIComplexNumberF32 iq = 6;
  repeated int32 iq_sizes = 7;
  int32 reset = 8;
}

message AnalyzeNWaveformsIQResponse {
  int32 status = 1;
}

message AnalyzeNWaveformsIQInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  string result_name = 3;
  repeated double x0 = 4;
  repeated double dx = 5;
  repeated float iq = 6;
  repeated int32 iq_sizes = 7;
  int32 reset = 8;
}

message AnalyzeNWaveformsIQInterleavedIQResponse {
  int32 status = 1;
}

message AnalyzeNWaveformsIQSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  string result_name = 3;
  repeated double x0 = 4;
  repeated double dx = 5;
  repeated float iqi = 6;
  repeated float iqq = 7;
  repeated int32 iq_sizes = 8;
  int32 reset = 9;
}

message AnalyzeNWaveformsIQSplitResponse {
  int32 status = 1;
}

message AnalyzeNWaveformsSpectrumRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  string result_name = 3;
  repeated double x0 = 4;
  repeated double dx = 5;
  repeated float spectrum = 6;
  repeated int32 spectrum_sizes = 7;
  int32 reset = 8;
}

message AnalyzeNWaveformsSpectrumResponse {
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

message BuildBandwidthPartStringRequest {
  string selector_string = 1;
  int32 bandwidth_part_number = 2;
}

message BuildBandwidthPartStringResponse {
  int32 status = 1;
  string selector_string_out = 2;
}

message BuildCORESETClusterStringRequest {
  string selector_string = 1;
  int32 coreset_cluster_number = 2;
}

message BuildCORESETClusterStringResponse {
  int32 status = 1;
  string selector_string_out = 2;
}

message BuildCORESETStringRequest {
  string selector_string = 1;
  int32 coreset_number = 2;
}

message BuildCORESETStringResponse {
  int32 status = 1;
  string selector_string_out = 2;
}

message BuildCarrierStringRequest {
  string selector_string = 1;
  int32 carrier_number = 2;
}

message BuildCarrierStringResponse {
  int32 status = 1;
  string selector_string_out = 2;
}

message BuildListStepStringRequest {
  string list_name = 1;
  string result_name = 2;
  int32 step_number = 3;
}

message BuildListStepStringResponse {
  int32 status = 1;
  string selector_string = 2;
}

message BuildListStringRequest {
  string list_name = 1;
  string result_name = 2;
}

message BuildListStringResponse {
  int32 status = 1;
  string selector_string = 2;
}

message BuildOffsetStringRequest {
  string selector_string = 1;
  int32 offset_number = 2;
}

message BuildOffsetStringResponse {
  int32 status = 1;
  string selector_string_out = 2;
}

message BuildPDCCHStringRequest {
  string selector_string = 1;
  int32 pdcch_number = 2;
}

message BuildPDCCHStringResponse {
  int32 status = 1;
  string selector_string_out = 2;
}

message BuildPDSCHClusterStringRequest {
  string selector_string = 1;
  int32 pdsch_cluster_number = 2;
}

message BuildPDSCHClusterStringResponse {
  int32 status = 1;
  string selector_string_out = 2;
}

message BuildPDSCHStringRequest {
  string selector_string = 1;
  int32 pdsch_number = 2;
}

message BuildPDSCHStringResponse {
  int32 status = 1;
  string selector_string_out = 2;
}

message BuildPUSCHClusterStringRequest {
  string selector_string = 1;
  int32 pusch_cluster_number = 2;
}

message BuildPUSCHClusterStringResponse {
  int32 status = 1;
  string selector_string_out = 2;
}

message BuildPUSCHStringRequest {
  string selector_string = 1;
  int32 pusch_number = 2;
}

message BuildPUSCHStringResponse {
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

message BuildSubblockStringRequest {
  string selector_string = 1;
  int32 subblock_number = 2;
}

message BuildSubblockStringResponse {
  int32 status = 1;
  string selector_string_out = 2;
}

message BuildUserStringRequest {
  string selector_string = 1;
  int32 user_number = 2;
}

message BuildUserStringResponse {
  int32 status = 1;
  string selector_string_out = 2;
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

message CHPFetchComponentCarrierMeasurementRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CHPFetchComponentCarrierMeasurementResponse {
  int32 status = 1;
  double absolute_power = 2;
  double relative_power = 3;
}

message CHPFetchComponentCarrierMeasurementArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CHPFetchComponentCarrierMeasurementArrayResponse {
  int32 status = 1;
  repeated double absolute_power = 2;
  repeated double relative_power = 3;
  int32 actual_array_size = 4;
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

message CHPFetchSubblockPowerRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CHPFetchSubblockPowerResponse {
  int32 status = 1;
  double subblock_power = 2;
}

message CHPFetchTotalAggregatedPowerRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CHPFetchTotalAggregatedPowerResponse {
  int32 status = 1;
  double total_aggregated_power = 2;
}

message CHPValidateNoiseCalibrationDataRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
}

message CHPValidateNoiseCalibrationDataResponse {
  int32 status = 1;
  ChpNoiseCalibrationDataValid noise_calibration_data_valid = 2;
  int32 noise_calibration_data_valid_raw = 3;
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
  oneof trigger_min_quiet_time_mode_enum {
    TriggerMinimumQuietTimeMode trigger_min_quiet_time_mode = 8;
    int32 trigger_min_quiet_time_mode_raw = 9;
  }
  double trigger_min_quiet_time_duration = 10;
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

message CfgReferenceLevelRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double reference_level = 3;
}

message CfgReferenceLevelResponse {
  int32 status = 1;
}

message CfgSelectedPortsMultipleRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  string selected_ports = 3;
}

message CfgSelectedPortsMultipleResponse {
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

message CfggNodeBCategoryRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof gnodeb_category_enum {
    GNodeBCategory gnodeb_category = 3;
    int32 gnodeb_category_raw = 4;
  }
}

message CfggNodeBCategoryResponse {
  int32 status = 1;
}

message CheckMeasurementStatusRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
}

message CheckMeasurementStatusResponse {
  int32 status = 1;
  bool is_done = 2;
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

message ClearNoiseCalibrationDatabaseRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
}

message ClearNoiseCalibrationDatabaseResponse {
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

message CreateListRequest {
  nidevice_grpc.Session instrument = 1;
  string list_name = 2;
}

message CreateListResponse {
  int32 status = 1;
}

message CreateListStepRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
}

message CreateListStepResponse {
  int32 status = 1;
  int32 created_step_index = 2;
}

message CreateSignalConfigurationRequest {
  nidevice_grpc.Session instrument = 1;
  string signal_name = 2;
}

message CreateSignalConfigurationResponse {
  int32 status = 1;
}

message DeleteListRequest {
  nidevice_grpc.Session instrument = 1;
  string list_name = 2;
}

message DeleteListResponse {
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
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeF32Response {
  int32 status = 1;
  float attr_val = 2;
}

message GetAttributeF32ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeF32ArrayResponse {
  int32 status = 1;
  repeated float attr_val = 2;
  int32 actual_array_size = 3;
}

message GetAttributeF64Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeF64Response {
  int32 status = 1;
  double attr_val = 2;
}

message GetAttributeF64ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeF64ArrayResponse {
  int32 status = 1;
  repeated double attr_val = 2;
  int32 actual_array_size = 3;
}

message GetAttributeI16Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeI16Response {
  int32 status = 1;
  int32 attr_val = 2;
}

message GetAttributeI32Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeI32Response {
  int32 status = 1;
  NiRFmxNRInt32AttributeValues attr_val = 2;
  int32 attr_val_raw = 3;
}

message GetAttributeI32ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeI32ArrayResponse {
  int32 status = 1;
  repeated NiRFmxNRInt32AttributeValues attr_val = 2;
  repeated int32 attr_val_raw = 3;
  int32 actual_array_size = 4;
}

message GetAttributeI64Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeI64Response {
  int32 status = 1;
  int64 attr_val = 2;
}

message GetAttributeI64ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeI64ArrayResponse {
  int32 status = 1;
  repeated int64 attr_val = 2;
  int32 actual_array_size = 3;
}

message GetAttributeI8Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeI8Response {
  int32 status = 1;
  int32 attr_val = 2;
}

message GetAttributeI8ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeI8ArrayResponse {
  int32 status = 1;
  repeated int32 attr_val = 2;
  int32 actual_array_size = 3;
}

message GetAttributeNIComplexDoubleArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeNIComplexDoubleArrayResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumber attr_val = 2;
  int32 actual_array_size = 3;
}

message GetAttributeNIComplexSingleArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeNIComplexSingleArrayResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 attr_val = 2;
  int32 actual_array_size = 3;
}

message GetAttributeStringRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeStringResponse {
  int32 status = 1;
  string attr_val = 2;
}

message GetAttributeU16Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeU16Response {
  int32 status = 1;
  uint32 attr_val = 2;
}

message GetAttributeU32Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeU32Response {
  int32 status = 1;
  uint32 attr_val = 2;
}

message GetAttributeU32ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeU32ArrayResponse {
  int32 status = 1;
  repeated uint32 attr_val = 2;
  int32 actual_array_size = 3;
}

message GetAttributeU64ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeU64ArrayResponse {
  int32 status = 1;
  repeated uint64 attr_val = 2;
  int32 actual_array_size = 3;
}

message GetAttributeU8Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
}

message GetAttributeU8Response {
  int32 status = 1;
  uint32 attr_val = 2;
}

message GetAttributeU8ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
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

message LoadFromGenerationConfigurationFileRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  string file_path = 3;
  int32 configuration_index = 4;
}

message LoadFromGenerationConfigurationFileResponse {
  int32 status = 1;
}

message ModAccAutoLevelRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccAutoLevelResponse {
  int32 status = 1;
}

message ModAccCfgMeasurementModeRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof measurement_mode_enum {
    ModAccMeasurementMode measurement_mode = 3;
    int32 measurement_mode_raw = 4;
  }
}

message ModAccCfgMeasurementModeResponse {
  int32 status = 1;
}

message ModAccCfgNoiseCompensationEnabledRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof noise_compensation_enabled_enum {
    ModAccNoiseCompensationEnabled noise_compensation_enabled = 3;
    int32 noise_compensation_enabled_raw = 4;
  }
}

message ModAccCfgNoiseCompensationEnabledResponse {
  int32 status = 1;
}

message ModAccCfgReferenceWaveformRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double x0 = 3;
  double dx = 4;
  repeated nidevice_grpc.NIComplexNumberF32 reference_waveform = 5;
}

message ModAccCfgReferenceWaveformResponse {
  int32 status = 1;
}

message ModAccCfgReferenceWaveformInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double x0 = 3;
  double dx = 4;
  repeated float reference_waveform = 5;
}

message ModAccCfgReferenceWaveformInterleavedIQResponse {
  int32 status = 1;
}

message ModAccCfgReferenceWaveformSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double x0 = 3;
  double dx = 4;
  repeated float reference_waveform_i = 5;
  repeated float reference_waveform_q = 6;
}

message ModAccCfgReferenceWaveformSplitResponse {
  int32 status = 1;
}

message ModAccClearNoiseCalibrationDatabaseRequest {
  nidevice_grpc.Session instrument = 1;
}

message ModAccClearNoiseCalibrationDatabaseResponse {
  int32 status = 1;
}

message ModAccFetchCompositeEVMRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchCompositeEVMResponse {
  int32 status = 1;
  double composite_rms_evm_mean = 2;
  double composite_peak_evm_maximum = 3;
}

message ModAccFetchFrequencyErrorMeanRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchFrequencyErrorMeanResponse {
  int32 status = 1;
  double frequency_error_mean = 2;
}

message ModAccFetchFrequencyErrorPerSlotMaximumTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchFrequencyErrorPerSlotMaximumTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float frequency_error_per_slot_maximum = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchIQGainImbalancePerSubcarrierMeanTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchIQGainImbalancePerSubcarrierMeanTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float iq_gain_imbalance_per_subcarrier_mean = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchIQQuadratureErrorPerSubcarrierMeanTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchIQQuadratureErrorPerSubcarrierMeanTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float iq_quadrature_error_per_subcarrier_mean = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchInBandEmissionTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchInBandEmissionTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float in_band_emission = 4;
  repeated float in_band_emission_mask = 5;
  int32 actual_array_size = 6;
}

message ModAccFetchPBCHDMRSConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPBCHDMRSConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 pbch_dmrs_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPBCHDMRSConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPBCHDMRSConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float pbch_dmrs_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPBCHDMRSConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPBCHDMRSConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float pbch_dmrs_constellation_i = 2;
  repeated float pbch_dmrs_constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float pbch_dmrs_rms_evm_per_subcarrier_mean = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float pbch_dmrs_rms_evm_per_symbol_mean = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchPBCHDataConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPBCHDataConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 pbch_data_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPBCHDataConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPBCHDataConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float pbch_data_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPBCHDataConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPBCHDataConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float pbch_data_constellation_i = 2;
  repeated float pbch_data_constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float pbch_data_rms_evm_per_subcarrier_mean = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchPBCHDataRMSEVMPerSymbolMeanTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPBCHDataRMSEVMPerSymbolMeanTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float pbch_data_rms_evm_per_symbol_mean = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchPDSCH1024QAMConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH1024QAMConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 qam1024_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float qam1024_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCH1024QAMConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH1024QAMConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float qam1024_constellation_i = 2;
  repeated float qam1024_constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchPDSCH16QAMConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH16QAMConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 qam16_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float qam16_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCH16QAMConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH16QAMConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float qam16_constellation_i = 2;
  repeated float qam16_constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchPDSCH256QAMConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH256QAMConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 qam256_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float qam256_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCH256QAMConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH256QAMConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float qam256_constellation_i = 2;
  repeated float qam256_constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchPDSCH4096QAMConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH4096QAMConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 qam4096_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float qam4096_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCH4096QAMConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH4096QAMConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float qam4096_constellation_i = 2;
  repeated float qam4096_constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchPDSCH64QAMConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH64QAMConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 qam64_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float qam64_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCH64QAMConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH64QAMConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float qam64_constellation_i = 2;
  repeated float qam64_constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchPDSCH8PSKConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH8PSKConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 psk8_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float psk8_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCH8PSKConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCH8PSKConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float psk8_constellation_i = 2;
  repeated float psk8_constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchPDSCHDMRSConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCHDMRSConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 pdsch_dmrs_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float pdsch_dmrs_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCHDMRSConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCHDMRSConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float pdsch_dmrs_constellation_i = 2;
  repeated float pdsch_dmrs_constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchPDSCHDataConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCHDataConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 pdsch_data_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCHDataConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCHDataConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float pdsch_data_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCHDataConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCHDataConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float pdsch_data_constellation_i = 2;
  repeated float pdsch_data_constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchPDSCHDemodulatedBitsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCHDemodulatedBitsResponse {
  int32 status = 1;
  repeated int32 bits = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCHPTRSConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCHPTRSConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 pdsch_ptrs_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float pdsch_ptrs_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCHPTRSConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCHPTRSConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float pdsch_ptrs_constellation_i = 2;
  repeated float pdsch_ptrs_constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchPDSCHQPSKConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCHQPSKConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 qpsk_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float qpsk_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPDSCHQPSKConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPDSCHQPSKConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float qpsk_constellation_i = 2;
  repeated float qpsk_constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchPSSConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPSSConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 pss_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPSSConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPSSConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float pss_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPSSConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPSSConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float pss_constellation_i = 2;
  repeated float pss_constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchPSSRMSEVMPerSubcarrierMeanTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPSSRMSEVMPerSubcarrierMeanTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float pss_rms_evm_per_subcarrier_mean = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchPSSRMSEVMPerSymbolMeanTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPSSRMSEVMPerSymbolMeanTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float pss_rms_evm_per_symbol_mean = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchPUSCHDMRSConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPUSCHDMRSConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 pusch_dmrs_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float pusch_dmrs_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPUSCHDMRSConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPUSCHDMRSConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float pusch_dmrs_constellation_i = 2;
  repeated float pusch_dmrs_constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchPUSCHDataConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPUSCHDataConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 pusch_data_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPUSCHDataConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPUSCHDataConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float pusch_data_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPUSCHDataConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPUSCHDataConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float pusch_data_constellation_i = 2;
  repeated float pusch_data_constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchPUSCHDemodulatedBitsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPUSCHDemodulatedBitsResponse {
  int32 status = 1;
  repeated int32 bits = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPUSCHPTRSConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPUSCHPTRSConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 pusch_ptrs_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float pusch_ptrs_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchPUSCHPTRSConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPUSCHPTRSConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float pusch_ptrs_constellation_i = 2;
  repeated float pusch_ptrs_constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchPUSCHPhaseOffsetTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPUSCHPhaseOffsetTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float pusch_phase_offset = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchPeakEVMHighPerSymbolMaximumTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPeakEVMHighPerSymbolMaximumTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float peak_evm_high_per_symbol_maximum = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchPeakEVMLowPerSymbolMaximumTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPeakEVMLowPerSymbolMaximumTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float peak_evm_low_per_symbol_maximum = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchPeakEVMPerSlotMaximumTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPeakEVMPerSlotMaximumTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float peak_evm_per_slot_maximum = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchPeakEVMPerSubcarrierMaximumTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPeakEVMPerSubcarrierMaximumTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float peak_evm_per_subcarrier_maximum = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchPeakEVMPerSymbolMaximumTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPeakEVMPerSymbolMaximumTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float peak_evm_per_symbol_maximum = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchRMSEVMHighPerSymbolMeanTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchRMSEVMHighPerSymbolMeanTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float rms_evm_high_per_symbol_mean = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchRMSEVMLowPerSymbolMeanTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchRMSEVMLowPerSymbolMeanTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float rms_evm_low_per_symbol_mean = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchRMSEVMPerSlotMeanTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchRMSEVMPerSlotMeanTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float rms_evm_per_slot_mean = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchRMSEVMPerSubcarrierMeanTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchRMSEVMPerSubcarrierMeanTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float rms_evm_per_subcarrier_mean = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchRMSEVMPerSymbolMeanTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchRMSEVMPerSymbolMeanTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float rms_evm_per_symbol_mean = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchSSSConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchSSSConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 sss_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchSSSConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchSSSConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float sss_constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchSSSConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchSSSConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float sss_constellation_i = 2;
  repeated float sss_constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchSSSRMSEVMPerSubcarrierMeanTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchSSSRMSEVMPerSubcarrierMeanTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float sss_rms_evm_per_subcarrier_mean = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchSSSRMSEVMPerSymbolMeanTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchSSSRMSEVMPerSymbolMeanTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float sss_rms_evm_per_symbol_mean = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchSpectralFlatnessTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchSpectralFlatnessTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float spectral_flatness = 4;
  repeated float spectral_flatness_lower_mask = 5;
  repeated float spectral_flatness_upper_mask = 6;
  int32 actual_array_size = 7;
}

message ModAccFetchSubblockInBandEmissionTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchSubblockInBandEmissionTraceResponse {
  int32 status = 1;
  repeated double subblock_in_band_emission = 2;
  repeated double subblock_in_band_emission_mask = 3;
  repeated double subblock_in_band_emission_rb_indices = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchTransientPeriodLocationsTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchTransientPeriodLocationsTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float transient_period_locations = 4;
  int32 actual_array_size = 5;
}

message ModAccValidateCalibrationDataRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
}

message ModAccValidateCalibrationDataResponse {
  int32 status = 1;
  ModAccCalibrationDataValid calibration_data_valid = 2;
  int32 calibration_data_valid_raw = 3;
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

message PVTCfgAveragingRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof averaging_enabled_enum {
    PvtAveragingEnabled averaging_enabled = 3;
    int32 averaging_enabled_raw = 4;
  }
  int32 averaging_count = 5;
  oneof averaging_type_enum {
    PvtAveragingType averaging_type = 6;
    int32 averaging_type_raw = 7;
  }
}

message PVTCfgAveragingResponse {
  int32 status = 1;
}

message PVTCfgMeasurementMethodRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof measurement_method_enum {
    PvtMeasurementMethod measurement_method = 3;
    int32 measurement_method_raw = 4;
  }
}

message PVTCfgMeasurementMethodResponse {
  int32 status = 1;
}

message PVTCfgOFFPowerExclusionPeriodsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double off_power_exclusion_before = 3;
  double off_power_exclusion_after = 4;
}

message PVTCfgOFFPowerExclusionPeriodsResponse {
  int32 status = 1;
}

message PVTFetchMeasurementRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message PVTFetchMeasurementResponse {
  int32 status = 1;
  PvtMeasurementStatus measurement_status = 2;
  int32 measurement_status_raw = 3;
  double absolute_off_power_before = 4;
  double absolute_off_power_after = 5;
  double absolute_on_power = 6;
  double burst_width = 7;
}

message PVTFetchMeasurementArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message PVTFetchMeasurementArrayResponse {
  int32 status = 1;
  repeated PvtMeasurementStatus measurement_status = 2;
  repeated int32 measurement_status_raw = 3;
  repeated double absolute_off_power_before = 4;
  repeated double absolute_off_power_after = 5;
  repeated double absolute_on_power = 6;
  repeated double burst_width = 7;
  int32 actual_array_size = 8;
}

message PVTFetchSignalPowerTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message PVTFetchSignalPowerTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float signal_power = 4;
  repeated float absolute_limit = 5;
  int32 actual_array_size = 6;
}

message PVTFetchWindowedSignalPowerTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message PVTFetchWindowedSignalPowerTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float windowed_signal_power = 4;
  int32 actual_array_size = 5;
}

message ResetAttributeRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
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

message SEMCfgComponentCarrierRatedOutputPowerRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double component_carrier_rated_output_power = 3;
}

message SEMCfgComponentCarrierRatedOutputPowerResponse {
  int32 status = 1;
}

message SEMCfgComponentCarrierRatedOutputPowerArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  repeated double component_carrier_rated_output_power = 3;
}

message SEMCfgComponentCarrierRatedOutputPowerArrayResponse {
  int32 status = 1;
}

message SEMCfgNumberOfOffsetsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  int32 number_of_offsets = 3;
}

message SEMCfgNumberOfOffsetsResponse {
  int32 status = 1;
}

message SEMCfgOffsetAbsoluteLimitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double absolute_limit_start = 3;
  double absolute_limit_stop = 4;
}

message SEMCfgOffsetAbsoluteLimitResponse {
  int32 status = 1;
}

message SEMCfgOffsetAbsoluteLimitArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  repeated double absolute_limit_start = 3;
  repeated double absolute_limit_stop = 4;
}

message SEMCfgOffsetAbsoluteLimitArrayResponse {
  int32 status = 1;
}

message SEMCfgOffsetBandwidthIntegralRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  int32 bandwidth_integral = 3;
}

message SEMCfgOffsetBandwidthIntegralResponse {
  int32 status = 1;
}

message SEMCfgOffsetBandwidthIntegralArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  repeated int32 bandwidth_integral = 3;
}

message SEMCfgOffsetBandwidthIntegralArrayResponse {
  int32 status = 1;
}

message SEMCfgOffsetFrequencyRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double offset_start_frequency = 3;
  double offset_stop_frequency = 4;
  oneof offset_sideband_enum {
    SemOffsetSideband offset_sideband = 5;
    int32 offset_sideband_raw = 6;
  }
}

message SEMCfgOffsetFrequencyResponse {
  int32 status = 1;
}

message SEMCfgOffsetFrequencyArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  repeated double offset_start_frequency = 3;
  repeated double offset_stop_frequency = 4;
  repeated SemOffsetSideband offset_sideband = 5;
}

message SEMCfgOffsetFrequencyArrayResponse {
  int32 status = 1;
}

message SEMCfgOffsetLimitFailMaskRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof limit_fail_mask_enum {
    SemOffsetLimitFailMask limit_fail_mask = 3;
    int32 limit_fail_mask_raw = 4;
  }
}

message SEMCfgOffsetLimitFailMaskResponse {
  int32 status = 1;
}

message SEMCfgOffsetLimitFailMaskArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  repeated SemOffsetLimitFailMask limit_fail_mask = 3;
}

message SEMCfgOffsetLimitFailMaskArrayResponse {
  int32 status = 1;
}

message SEMCfgOffsetRBWFilterRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double offset_rbw = 3;
  oneof offset_rbw_filter_type_enum {
    SemOffsetRbwFilterType offset_rbw_filter_type = 4;
    int32 offset_rbw_filter_type_raw = 5;
  }
}

message SEMCfgOffsetRBWFilterResponse {
  int32 status = 1;
}

message SEMCfgOffsetRBWFilterArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  repeated double offset_rbw = 3;
  repeated SemOffsetRbwFilterType offset_rbw_filter_type = 4;
}

message SEMCfgOffsetRBWFilterArrayResponse {
  int32 status = 1;
}

message SEMCfgOffsetRelativeLimitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double relative_limit_start = 3;
  double relative_limit_stop = 4;
}

message SEMCfgOffsetRelativeLimitResponse {
  int32 status = 1;
}

message SEMCfgOffsetRelativeLimitArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  repeated double relative_limit_start = 3;
  repeated double relative_limit_stop = 4;
}

message SEMCfgOffsetRelativeLimitArrayResponse {
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

message SEMCfgUplinkMaskTypeRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof uplink_mask_type_enum {
    SemUplinkMaskType uplink_mask_type = 3;
    int32 uplink_mask_type_raw = 4;
  }
}

message SEMCfgUplinkMaskTypeResponse {
  int32 status = 1;
}

message SEMFetchComponentCarrierMeasurementRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SEMFetchComponentCarrierMeasurementResponse {
  int32 status = 1;
  double absolute_power = 2;
  double peak_absolute_power = 3;
  double peak_frequency = 4;
  double relative_power = 5;
}

message SEMFetchComponentCarrierMeasurementArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SEMFetchComponentCarrierMeasurementArrayResponse {
  int32 status = 1;
  repeated double absolute_power = 2;
  repeated double peak_absolute_power = 3;
  repeated double peak_frequency = 4;
  repeated double relative_power = 5;
  int32 actual_array_size = 6;
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
  double total_absolute_power = 2;
  double total_relative_power = 3;
  double peak_absolute_power = 4;
  double peak_frequency = 5;
  double peak_relative_power = 6;
}

message SEMFetchLowerOffsetPowerArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SEMFetchLowerOffsetPowerArrayResponse {
  int32 status = 1;
  repeated double total_absolute_power = 2;
  repeated double total_relative_power = 3;
  repeated double peak_absolute_power = 4;
  repeated double peak_frequency = 5;
  repeated double peak_relative_power = 6;
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
  repeated float composite_mask = 5;
  int32 actual_array_size = 6;
}

message SEMFetchSubblockMeasurementRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SEMFetchSubblockMeasurementResponse {
  int32 status = 1;
  double subblock_power = 2;
  double integration_bandwidth = 3;
  double frequency = 4;
}

message SEMFetchTotalAggregatedPowerRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SEMFetchTotalAggregatedPowerResponse {
  int32 status = 1;
  double total_aggregated_power = 2;
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
  double total_absolute_power = 2;
  double total_relative_power = 3;
  double peak_absolute_power = 4;
  double peak_frequency = 5;
  double peak_relative_power = 6;
}

message SEMFetchUpperOffsetPowerArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SEMFetchUpperOffsetPowerArrayResponse {
  int32 status = 1;
  repeated double total_absolute_power = 2;
  repeated double total_relative_power = 3;
  repeated double peak_absolute_power = 4;
  repeated double peak_frequency = 5;
  repeated double peak_relative_power = 6;
  int32 actual_array_size = 7;
}

message SelectMeasurementsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof measurements_enum {
    MeasurementTypes measurements = 3;
    uint32 measurements_raw = 4;
  }
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
  NiRFmxNRAttribute attribute_id = 3;
  float attr_val = 4;
}

message SetAttributeF32Response {
  int32 status = 1;
}

message SetAttributeF32ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  repeated float attr_val = 4;
}

message SetAttributeF32ArrayResponse {
  int32 status = 1;
}

message SetAttributeF64Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  double attr_val = 4;
}

message SetAttributeF64Response {
  int32 status = 1;
}

message SetAttributeF64ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  repeated double attr_val = 4;
}

message SetAttributeF64ArrayResponse {
  int32 status = 1;
}

message SetAttributeI16Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  int32 attr_val = 4;
}

message SetAttributeI16Response {
  int32 status = 1;
}

message SetAttributeI32Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  oneof attr_val_enum {
    NiRFmxNRInt32AttributeValues attr_val = 4;
    int32 attr_val_raw = 5;
  }
}

message SetAttributeI32Response {
  int32 status = 1;
}

message SetAttributeI32ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  repeated NiRFmxNRInt32AttributeValues attr_val = 4;
}

message SetAttributeI32ArrayResponse {
  int32 status = 1;
}

message SetAttributeI64Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  int64 attr_val = 4;
}

message SetAttributeI64Response {
  int32 status = 1;
}

message SetAttributeI64ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  repeated int64 attr_val = 4;
}

message SetAttributeI64ArrayResponse {
  int32 status = 1;
}

message SetAttributeI8Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  int32 attr_val = 4;
}

message SetAttributeI8Response {
  int32 status = 1;
}

message SetAttributeI8ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  repeated int32 attr_val = 4;
}

message SetAttributeI8ArrayResponse {
  int32 status = 1;
}

message SetAttributeNIComplexDoubleArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  repeated nidevice_grpc.NIComplexNumber attr_val = 4;
}

message SetAttributeNIComplexDoubleArrayResponse {
  int32 status = 1;
}

message SetAttributeNIComplexSingleArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  repeated nidevice_grpc.NIComplexNumberF32 attr_val = 4;
}

message SetAttributeNIComplexSingleArrayResponse {
  int32 status = 1;
}

message SetAttributeStringRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  oneof attr_val_enum {
    NiRFmxNRStringAttributeValuesMapped attr_val_mapped = 4;
    string attr_val_raw = 5;
  }
}

message SetAttributeStringResponse {
  int32 status = 1;
}

message SetAttributeU16Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  uint32 attr_val = 4;
}

message SetAttributeU16Response {
  int32 status = 1;
}

message SetAttributeU32Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  uint32 attr_val = 4;
}

message SetAttributeU32Response {
  int32 status = 1;
}

message SetAttributeU32ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  repeated uint32 attr_val = 4;
}

message SetAttributeU32ArrayResponse {
  int32 status = 1;
}

message SetAttributeU64ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  repeated uint64 attr_val = 4;
}

message SetAttributeU64ArrayResponse {
  int32 status = 1;
}

message SetAttributeU8Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  uint32 attr_val = 4;
}

message SetAttributeU8Response {
  int32 status = 1;
}

message SetAttributeU8ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxNRAttribute attribute_id = 3;
  bytes attr_val = 4;
}

message SetAttributeU8ArrayResponse {
  int32 status = 1;
}

message TXPFetchMeasurementRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message TXPFetchMeasurementResponse {
  int32 status = 1;
  double average_power_mean = 2;
  double peak_power_maximum = 3;
}

message TXPFetchPowerTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message TXPFetchPowerTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float power = 4;
  int32 actual_array_size = 5;
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

<!--NI_OSS_SOURCE repo=grpc-device path=generated/nirfmxnr/nirfmxnr_client.cpp sha256=83ee297ed86c2a279ceecd092322e3266b135a611cf445ab4bf8b3ace7b1fa04 bytes=192631 -->
## FILE: generated/nirfmxnr/nirfmxnr_client.cpp

- repository: `ni/grpc-device`
- source_path: `generated/nirfmxnr/nirfmxnr_client.cpp`
- sha256: `83ee297ed86c2a279ceecd092322e3266b135a611cf445ab4bf8b3ace7b1fa04`
- bytes: 192631

````cpp

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// EXPERIMENTAL Client convenience wrapper for NI-RFMXNR.
//---------------------------------------------------------------------
#include "nirfmxnr_client.h"

#include <grpcpp/grpcpp.h>

#include <nirfmxnr.grpc.pb.h>

#include <cstdint>
#include <memory>
#include <stdexcept>
#include <vector>

namespace nirfmxnr_grpc::experimental::client {

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

ACPCfgNumberOfENDCOffsetsResponse
acp_cfg_number_of_endc_offsets(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& number_of_endc_offsets)
{
  ::grpc::ClientContext context;

  auto request = ACPCfgNumberOfENDCOffsetsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_number_of_endc_offsets(number_of_endc_offsets);

  auto response = ACPCfgNumberOfENDCOffsetsResponse{};

  raise_if_error(
      stub->ACPCfgNumberOfENDCOffsets(&context, request, &response),
      context);

  return response;
}

ACPCfgNumberOfEUTRAOffsetsResponse
acp_cfg_number_of_eutra_offsets(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& number_of_eutra_offsets)
{
  ::grpc::ClientContext context;

  auto request = ACPCfgNumberOfEUTRAOffsetsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_number_of_eutra_offsets(number_of_eutra_offsets);

  auto response = ACPCfgNumberOfEUTRAOffsetsResponse{};

  raise_if_error(
      stub->ACPCfgNumberOfEUTRAOffsets(&context, request, &response),
      context);

  return response;
}

ACPCfgNumberOfNROffsetsResponse
acp_cfg_number_of_nr_offsets(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& number_of_nr_offsets)
{
  ::grpc::ClientContext context;

  auto request = ACPCfgNumberOfNROffsetsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_number_of_nr_offsets(number_of_nr_offsets);

  auto response = ACPCfgNumberOfNROffsetsResponse{};

  raise_if_error(
      stub->ACPCfgNumberOfNROffsets(&context, request, &response),
      context);

  return response;
}

ACPCfgNumberOfUTRAOffsetsResponse
acp_cfg_number_of_utra_offsets(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& number_of_utra_offsets)
{
  ::grpc::ClientContext context;

  auto request = ACPCfgNumberOfUTRAOffsetsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_number_of_utra_offsets(number_of_utra_offsets);

  auto response = ACPCfgNumberOfUTRAOffsetsResponse{};

  raise_if_error(
      stub->ACPCfgNumberOfUTRAOffsets(&context, request, &response),
      context);

  return response;
}

ACPCfgPowerUnitsResponse
acp_cfg_power_units(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<AcpPowerUnits, pb::int32>& power_units)
{
  ::grpc::ClientContext context;

  auto request = ACPCfgPowerUnitsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto power_units_ptr = power_units.get_if<AcpPowerUnits>();
  const auto power_units_raw_ptr = power_units.get_if<pb::int32>();
  if (power_units_ptr) {
    request.set_power_units(*power_units_ptr);
  }
  else if (power_units_raw_ptr) {
    request.set_power_units_raw(*power_units_raw_ptr);
  }

  auto response = ACPCfgPowerUnitsResponse{};

  raise_if_error(
      stub->ACPCfgPowerUnits(&context, request, &response),
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

ACPFetchComponentCarrierMeasurementResponse
acp_fetch_component_carrier_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ACPFetchComponentCarrierMeasurementRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ACPFetchComponentCarrierMeasurementResponse{};

  raise_if_error(
      stub->ACPFetchComponentCarrierMeasurement(&context, request, &response),
      context);

  return response;
}

ACPFetchComponentCarrierMeasurementArrayResponse
acp_fetch_component_carrier_measurement_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ACPFetchComponentCarrierMeasurementArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ACPFetchComponentCarrierMeasurementArrayResponse{};

  raise_if_error(
      stub->ACPFetchComponentCarrierMeasurementArray(&context, request, &response),
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

ACPFetchSubblockMeasurementResponse
acp_fetch_subblock_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ACPFetchSubblockMeasurementRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ACPFetchSubblockMeasurementResponse{};

  raise_if_error(
      stub->ACPFetchSubblockMeasurement(&context, request, &response),
      context);

  return response;
}

ACPFetchTotalAggregatedPowerResponse
acp_fetch_total_aggregated_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ACPFetchTotalAggregatedPowerRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ACPFetchTotalAggregatedPowerResponse{};

  raise_if_error(
      stub->ACPFetchTotalAggregatedPower(&context, request, &response),
      context);

  return response;
}

ACPValidateNoiseCalibrationDataResponse
acp_validate_noise_calibration_data(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string)
{
  ::grpc::ClientContext context;

  auto request = ACPValidateNoiseCalibrationDataRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);

  auto response = ACPValidateNoiseCalibrationDataResponse{};

  raise_if_error(
      stub->ACPValidateNoiseCalibrationData(&context, request, &response),
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

AnalyzeNWaveformsIQResponse
analyze_n_waveforms_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const std::vector<double>& x0, const std::vector<double>& dx, const std::vector<nidevice_grpc::NIComplexNumberF32>& iq, const std::vector<pb::int32>& iq_sizes, const pb::int32& reset)
{
  ::grpc::ClientContext context;

  auto request = AnalyzeNWaveformsIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_result_name(result_name);
  copy_array(x0, request.mutable_x0());
  copy_array(dx, request.mutable_dx());
  copy_array(iq, request.mutable_iq());
  copy_array(iq_sizes, request.mutable_iq_sizes());
  request.set_reset(reset);

  auto response = AnalyzeNWaveformsIQResponse{};

  raise_if_error(
      stub->AnalyzeNWaveformsIQ(&context, request, &response),
      context);

  return response;
}

AnalyzeNWaveformsIQInterleavedIQResponse
analyze_n_waveforms_iq_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const std::vector<double>& x0, const std::vector<double>& dx, const std::vector<float>& iq, const std::vector<pb::int32>& iq_sizes, const pb::int32& reset)
{
  ::grpc::ClientContext context;

  auto request = AnalyzeNWaveformsIQInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_result_name(result_name);
  copy_array(x0, request.mutable_x0());
  copy_array(dx, request.mutable_dx());
  copy_array(iq, request.mutable_iq());
  copy_array(iq_sizes, request.mutable_iq_sizes());
  request.set_reset(reset);

  auto response = AnalyzeNWaveformsIQInterleavedIQResponse{};

  raise_if_error(
      stub->AnalyzeNWaveformsIQInterleavedIQ(&context, request, &response),
      context);

  return response;
}

AnalyzeNWaveformsIQSplitResponse
analyze_n_waveforms_iq_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const std::vector<double>& x0, const std::vector<double>& dx, const std::vector<float>& iqi, const std::vector<float>& iqq, const std::vector<pb::int32>& iq_sizes, const pb::int32& reset)
{
  ::grpc::ClientContext context;

  auto request = AnalyzeNWaveformsIQSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_result_name(result_name);
  copy_array(x0, request.mutable_x0());
  copy_array(dx, request.mutable_dx());
  copy_array(iqi, request.mutable_iqi());
  copy_array(iqq, request.mutable_iqq());
  copy_array(iq_sizes, request.mutable_iq_sizes());
  request.set_reset(reset);

  auto response = AnalyzeNWaveformsIQSplitResponse{};

  raise_if_error(
      stub->AnalyzeNWaveformsIQSplit(&context, request, &response),
      context);

  return response;
}

AnalyzeNWaveformsSpectrumResponse
analyze_n_waveforms_spectrum(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const std::vector<double>& x0, const std::vector<double>& dx, const std::vector<float>& spectrum, const std::vector<pb::int32>& spectrum_sizes, const pb::int32& reset)
{
  ::grpc::ClientContext context;

  auto request = AnalyzeNWaveformsSpectrumRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_result_name(result_name);
  copy_array(x0, request.mutable_x0());
  copy_array(dx, request.mutable_dx());
  copy_array(spectrum, request.mutable_spectrum());
  copy_array(spectrum_sizes, request.mutable_spectrum_sizes());
  request.set_reset(reset);

  auto response = AnalyzeNWaveformsSpectrumResponse{};

  raise_if_error(
      stub->AnalyzeNWaveformsSpectrum(&context, request, &response),
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

BuildBandwidthPartStringResponse
build_bandwidth_part_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& bandwidth_part_number)
{
  ::grpc::ClientContext context;

  auto request = BuildBandwidthPartStringRequest{};
  request.set_selector_string(selector_string);
  request.set_bandwidth_part_number(bandwidth_part_number);

  auto response = BuildBandwidthPartStringResponse{};

  raise_if_error(
      stub->BuildBandwidthPartString(&context, request, &response),
      context);

  return response;
}

BuildCORESETClusterStringResponse
build_coreset_cluster_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& coreset_cluster_number)
{
  ::grpc::ClientContext context;

  auto request = BuildCORESETClusterStringRequest{};
  request.set_selector_string(selector_string);
  request.set_coreset_cluster_number(coreset_cluster_number);

  auto response = BuildCORESETClusterStringResponse{};

  raise_if_error(
      stub->BuildCORESETClusterString(&context, request, &response),
      context);

  return response;
}

BuildCORESETStringResponse
build_coreset_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& coreset_number)
{
  ::grpc::ClientContext context;

  auto request = BuildCORESETStringRequest{};
  request.set_selector_string(selector_string);
  request.set_coreset_number(coreset_number);

  auto response = BuildCORESETStringResponse{};

  raise_if_error(
      stub->BuildCORESETString(&context, request, &response),
      context);

  return response;
}

BuildCarrierStringResponse
build_carrier_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& carrier_number)
{
  ::grpc::ClientContext context;

  auto request = BuildCarrierStringRequest{};
  request.set_selector_string(selector_string);
  request.set_carrier_number(carrier_number);

  auto response = BuildCarrierStringResponse{};

  raise_if_error(
      stub->BuildCarrierString(&context, request, &response),
      context);

  return response;
}

BuildListStepStringResponse
build_list_step_string(const StubPtr& stub, const std::string& list_name, const std::string& result_name, const pb::int32& step_number)
{
  ::grpc::ClientContext context;

  auto request = BuildListStepStringRequest{};
  request.set_list_name(list_name);
  request.set_result_name(result_name);
  request.set_step_number(step_number);

  auto response = BuildListStepStringResponse{};

  raise_if_error(
      stub->BuildListStepString(&context, request, &response),
      context);

  return response;
}

BuildListStringResponse
build_list_string(const StubPtr& stub, const std::string& list_name, const std::string& result_name)
{
  ::grpc::ClientContext context;

  auto request = BuildListStringRequest{};
  request.set_list_name(list_name);
  request.set_result_name(result_name);

  auto response = BuildListStringResponse{};

  raise_if_error(
      stub->BuildListString(&context, request, &response),
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

BuildPDCCHStringResponse
build_pdcch_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& pdcch_number)
{
  ::grpc::ClientContext context;

  auto request = BuildPDCCHStringRequest{};
  request.set_selector_string(selector_string);
  request.set_pdcch_number(pdcch_number);

  auto response = BuildPDCCHStringResponse{};

  raise_if_error(
      stub->BuildPDCCHString(&context, request, &response),
      context);

  return response;
}

BuildPDSCHClusterStringResponse
build_pdsch_cluster_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& pdsch_cluster_number)
{
  ::grpc::ClientContext context;

  auto request = BuildPDSCHClusterStringRequest{};
  request.set_selector_string(selector_string);
  request.set_pdsch_cluster_number(pdsch_cluster_number);

  auto response = BuildPDSCHClusterStringResponse{};

  raise_if_error(
      stub->BuildPDSCHClusterString(&context, request, &response),
      context);

  return response;
}

BuildPDSCHStringResponse
build_pdsch_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& pdsch_number)
{
  ::grpc::ClientContext context;

  auto request = BuildPDSCHStringRequest{};
  request.set_selector_string(selector_string);
  request.set_pdsch_number(pdsch_number);

  auto response = BuildPDSCHStringResponse{};

  raise_if_error(
      stub->BuildPDSCHString(&context, request, &response),
      context);

  return response;
}

BuildPUSCHClusterStringResponse
build_pusch_cluster_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& pusch_cluster_number)
{
  ::grpc::ClientContext context;

  auto request = BuildPUSCHClusterStringRequest{};
  request.set_selector_string(selector_string);
  request.set_pusch_cluster_number(pusch_cluster_number);

  auto response = BuildPUSCHClusterStringResponse{};

  raise_if_error(
      stub->BuildPUSCHClusterString(&context, request, &response),
      context);

  return response;
}

BuildPUSCHStringResponse
build_pusch_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& pusch_number)
{
  ::grpc::ClientContext context;

  auto request = BuildPUSCHStringRequest{};
  request.set_selector_string(selector_string);
  request.set_pusch_number(pusch_number);

  auto response = BuildPUSCHStringResponse{};

  raise_if_error(
      stub->BuildPUSCHString(&context, request, &response),
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

BuildSubblockStringResponse
build_subblock_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& subblock_number)
{
  ::grpc::ClientContext context;

  auto request = BuildSubblockStringRequest{};
  request.set_selector_string(selector_string);
  request.set_subblock_number(subblock_number);

  auto response = BuildSubblockStringResponse{};

  raise_if_error(
      stub->BuildSubblockString(&context, request, &response),
      context);

  return response;
}

BuildUserStringResponse
build_user_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& user_number)
{
  ::grpc::ClientContext context;

  auto request = BuildUserStringRequest{};
  request.set_selector_string(selector_string);
  request.set_user_number(user_number);

  auto response = BuildUserStringResponse{};

  raise_if_error(
      stub->BuildUserString(&context, request, &response),
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

CHPFetchComponentCarrierMeasurementResponse
chp_fetch_component_carrier_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CHPFetchComponentCarrierMeasurementRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CHPFetchComponentCarrierMeasurementResponse{};

  raise_if_error(
      stub->CHPFetchComponentCarrierMeasurement(&context, request, &response),
      context);

  return response;
}

CHPFetchComponentCarrierMeasurementArrayResponse
chp_fetch_component_carrier_measurement_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CHPFetchComponentCarrierMeasurementArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CHPFetchComponentCarrierMeasurementArrayResponse{};

  raise_if_error(
      stub->CHPFetchComponentCarrierMeasurementArray(&context, request, &response),
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

CHPFetchSubblockPowerResponse
chp_fetch_subblock_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CHPFetchSubblockPowerRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CHPFetchSubblockPowerResponse{};

  raise_if_error(
      stub->CHPFetchSubblockPower(&context, request, &response),
      context);

  return response;
}

CHPFetchTotalAggregatedPowerResponse
chp_fetch_total_aggregated_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CHPFetchTotalAggregatedPowerRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CHPFetchTotalAggregatedPowerResponse{};

  raise_if_error(
      stub->CHPFetchTotalAggregatedPower(&context, request, &response),
      context);

  return response;
}

CHPValidateNoiseCalibrationDataResponse
chp_validate_noise_calibration_data(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string)
{
  ::grpc::ClientContext context;

  auto request = CHPValidateNoiseCalibrationDataRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);

  auto response = CHPValidateNoiseCalibrationDataResponse{};

  raise_if_error(
      stub->CHPValidateNoiseCalibrationData(&context, request, &response),
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
cfg_iq_power_edge_trigger(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& iq_power_edge_source, const simple_variant<IQPowerEdgeTriggerSlope, pb::int32>& iq_power_edge_slope, const double& iq_power_edge_level, const double& trigger_delay, const simple_variant<TriggerMinimumQuietTimeMode, pb::int32>& trigger_min_quiet_time_mode, const double& trigger_min_quiet_time_duration, const simple_variant<IQPowerEdgeTriggerLevelType, pb::int32>& iq_power_edge_level_type, const pb::int32& enable_trigger)
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
  const auto trigger_min_quiet_time_mode_ptr = trigger_min_quiet_time_mode.get_if<TriggerMinimumQuietTimeMode>();
  const auto trigger_min_quiet_time_mode_raw_ptr = trigger_min_quiet_time_mode.get_if<pb::int32>();
  if (trigger_min_quiet_time_mode_ptr) {
    request.set_trigger_min_quiet_time_mode(*trigger_min_quiet_time_mode_ptr);
  }
  else if (trigger_min_quiet_time_mode_raw_ptr) {
    request.set_trigger_min_quiet_time_mode_raw(*trigger_min_quiet_time_mode_raw_ptr);
  }
  request.set_trigger_min_quiet_time_duration(trigger_min_quiet_time_duration);
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

CfgSelectedPortsMultipleResponse
cfg_selected_ports_multiple(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& selected_ports)
{
  ::grpc::ClientContext context;

  auto request = CfgSelectedPortsMultipleRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_selected_ports(selected_ports);

  auto response = CfgSelectedPortsMultipleResponse{};

  raise_if_error(
      stub->CfgSelectedPortsMultiple(&context, request, &response),
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

CfggNodeBCategoryResponse
cfgg_node_b_category(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<GNodeBCategory, pb::int32>& gnodeb_category)
{
  ::grpc::ClientContext context;

  auto request = CfggNodeBCategoryRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto gnodeb_category_ptr = gnodeb_category.get_if<GNodeBCategory>();
  const auto gnodeb_category_raw_ptr = gnodeb_category.get_if<pb::int32>();
  if (gnodeb_category_ptr) {
    request.set_gnodeb_category(*gnodeb_category_ptr);
  }
  else if (gnodeb_category_raw_ptr) {
    request.set_gnodeb_category_raw(*gnodeb_category_raw_ptr);
  }

  auto response = CfggNodeBCategoryResponse{};

  raise_if_error(
      stub->CfggNodeBCategory(&context, request, &response),
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

ClearNoiseCalibrationDatabaseResponse
clear_noise_calibration_database(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string)
{
  ::grpc::ClientContext context;

  auto request = ClearNoiseCalibrationDatabaseRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);

  auto response = ClearNoiseCalibrationDatabaseResponse{};

  raise_if_error(
      stub->ClearNoiseCalibrationDatabase(&context, request, &response),
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

CreateListResponse
create_list(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& list_name)
{
  ::grpc::ClientContext context;

  auto request = CreateListRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_list_name(list_name);

  auto response = CreateListResponse{};

  raise_if_error(
      stub->CreateList(&context, request, &response),
      context);

  return response;
}

CreateListStepResponse
create_list_step(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string)
{
  ::grpc::ClientContext context;

  auto request = CreateListStepRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);

  auto response = CreateListStepResponse{};

  raise_if_error(
      stub->CreateListStep(&context, request, &response),
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

DeleteListResponse
delete_list(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& list_name)
{
  ::grpc::ClientContext context;

  auto request = DeleteListRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_list_name(list_name);

  auto response = DeleteListResponse{};

  raise_if_error(
      stub->DeleteList(&context, request, &response),
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
get_attribute_f32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_f32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_f64(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_f64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_i16(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_i32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_i32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_i64(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_i64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_i8(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_i8_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_ni_complex_double_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_ni_complex_single_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_string(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_u16(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_u32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_u32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_u64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_u8(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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
get_attribute_u8_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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

LoadFromGenerationConfigurationFileResponse
load_from_generation_configuration_file(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& file_path, const pb::int32& configuration_index)
{
  ::grpc::ClientContext context;

  auto request = LoadFromGenerationConfigurationFileRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_file_path(file_path);
  request.set_configuration_index(configuration_index);

  auto response = LoadFromGenerationConfigurationFileResponse{};

  raise_if_error(
      stub->LoadFromGenerationConfigurationFile(&context, request, &response),
      context);

  return response;
}

ModAccAutoLevelResponse
mod_acc_auto_level(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccAutoLevelRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccAutoLevelResponse{};

  raise_if_error(
      stub->ModAccAutoLevel(&context, request, &response),
      context);

  return response;
}

ModAccCfgMeasurementModeResponse
mod_acc_cfg_measurement_mode(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ModAccMeasurementMode, pb::int32>& measurement_mode)
{
  ::grpc::ClientContext context;

  auto request = ModAccCfgMeasurementModeRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto measurement_mode_ptr = measurement_mode.get_if<ModAccMeasurementMode>();
  const auto measurement_mode_raw_ptr = measurement_mode.get_if<pb::int32>();
  if (measurement_mode_ptr) {
    request.set_measurement_mode(*measurement_mode_ptr);
  }
  else if (measurement_mode_raw_ptr) {
    request.set_measurement_mode_raw(*measurement_mode_raw_ptr);
  }

  auto response = ModAccCfgMeasurementModeResponse{};

  raise_if_error(
      stub->ModAccCfgMeasurementMode(&context, request, &response),
      context);

  return response;
}

ModAccCfgNoiseCompensationEnabledResponse
mod_acc_cfg_noise_compensation_enabled(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ModAccNoiseCompensationEnabled, pb::int32>& noise_compensation_enabled)
{
  ::grpc::ClientContext context;

  auto request = ModAccCfgNoiseCompensationEnabledRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto noise_compensation_enabled_ptr = noise_compensation_enabled.get_if<ModAccNoiseCompensationEnabled>();
  const auto noise_compensation_enabled_raw_ptr = noise_compensation_enabled.get_if<pb::int32>();
  if (noise_compensation_enabled_ptr) {
    request.set_noise_compensation_enabled(*noise_compensation_enabled_ptr);
  }
  else if (noise_compensation_enabled_raw_ptr) {
    request.set_noise_compensation_enabled_raw(*noise_compensation_enabled_raw_ptr);
  }

  auto response = ModAccCfgNoiseCompensationEnabledResponse{};

  raise_if_error(
      stub->ModAccCfgNoiseCompensationEnabled(&context, request, &response),
      context);

  return response;
}

ModAccCfgReferenceWaveformResponse
mod_acc_cfg_reference_waveform(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& x0, const double& dx, const std::vector<nidevice_grpc::NIComplexNumberF32>& reference_waveform)
{
  ::grpc::ClientContext context;

  auto request = ModAccCfgReferenceWaveformRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_x0(x0);
  request.set_dx(dx);
  copy_array(reference_waveform, request.mutable_reference_waveform());

  auto response = ModAccCfgReferenceWaveformResponse{};

  raise_if_error(
      stub->ModAccCfgReferenceWaveform(&context, request, &response),
      context);

  return response;
}

ModAccCfgReferenceWaveformInterleavedIQResponse
mod_acc_cfg_reference_waveform_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& x0, const double& dx, const std::vector<float>& reference_waveform)
{
  ::grpc::ClientContext context;

  auto request = ModAccCfgReferenceWaveformInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_x0(x0);
  request.set_dx(dx);
  copy_array(reference_waveform, request.mutable_reference_waveform());

  auto response = ModAccCfgReferenceWaveformInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccCfgReferenceWaveformInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccCfgReferenceWaveformSplitResponse
mod_acc_cfg_reference_waveform_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& x0, const double& dx, const std::vector<float>& reference_waveform_i, const std::vector<float>& reference_waveform_q)
{
  ::grpc::ClientContext context;

  auto request = ModAccCfgReferenceWaveformSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_x0(x0);
  request.set_dx(dx);
  copy_array(reference_waveform_i, request.mutable_reference_waveform_i());
  copy_array(reference_waveform_q, request.mutable_reference_waveform_q());

  auto response = ModAccCfgReferenceWaveformSplitResponse{};

  raise_if_error(
      stub->ModAccCfgReferenceWaveformSplit(&context, request, &response),
      context);

  return response;
}

ModAccClearNoiseCalibrationDatabaseResponse
mod_acc_clear_noise_calibration_database(const StubPtr& stub, const nidevice_grpc::Session& instrument)
{
  ::grpc::ClientContext context;

  auto request = ModAccClearNoiseCalibrationDatabaseRequest{};
  request.mutable_instrument()->CopyFrom(instrument);

  auto response = ModAccClearNoiseCalibrationDatabaseResponse{};

  raise_if_error(
      stub->ModAccClearNoiseCalibrationDatabase(&context, request, &response),
      context);

  return response;
}

ModAccFetchCompositeEVMResponse
mod_acc_fetch_composite_evm(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchCompositeEVMRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchCompositeEVMResponse{};

  raise_if_error(
      stub->ModAccFetchCompositeEVM(&context, request, &response),
      context);

  return response;
}

ModAccFetchFrequencyErrorMeanResponse
mod_acc_fetch_frequency_error_mean(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchFrequencyErrorMeanRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchFrequencyErrorMeanResponse{};

  raise_if_error(
      stub->ModAccFetchFrequencyErrorMean(&context, request, &response),
      context);

  return response;
}

ModAccFetchFrequencyErrorPerSlotMaximumTraceResponse
mod_acc_fetch_frequency_error_per_slot_maximum_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchFrequencyErrorPerSlotMaximumTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchFrequencyErrorPerSlotMaximumTraceResponse{};

  raise_if_error(
      stub->ModAccFetchFrequencyErrorPerSlotMaximumTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchIQGainImbalancePerSubcarrierMeanTraceResponse
mod_acc_fetch_iq_gain_imbalance_per_subcarrier_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchIQGainImbalancePerSubcarrierMeanTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchIQGainImbalancePerSubcarrierMeanTraceResponse{};

  raise_if_error(
      stub->ModAccFetchIQGainImbalancePerSubcarrierMeanTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchIQQuadratureErrorPerSubcarrierMeanTraceResponse
mod_acc_fetch_iq_quadrature_error_per_subcarrier_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchIQQuadratureErrorPerSubcarrierMeanTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchIQQuadratureErrorPerSubcarrierMeanTraceResponse{};

  raise_if_error(
      stub->ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchInBandEmissionTraceResponse
mod_acc_fetch_in_band_emission_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchInBandEmissionTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchInBandEmissionTraceResponse{};

  raise_if_error(
      stub->ModAccFetchInBandEmissionTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPBCHDMRSConstellationTraceResponse
mod_acc_fetch_pbchdmrs_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPBCHDMRSConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPBCHDMRSConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPBCHDMRSConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPBCHDMRSConstellationTraceInterleavedIQResponse
mod_acc_fetch_pbchdmrs_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPBCHDMRSConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPBCHDMRSConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchPBCHDMRSConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchPBCHDMRSConstellationTraceSplitResponse
mod_acc_fetch_pbchdmrs_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPBCHDMRSConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPBCHDMRSConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchPBCHDMRSConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTraceResponse
mod_acc_fetch_pbchdmrsrmsevm_per_subcarrier_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTraceResponse
mod_acc_fetch_pbchdmrsrmsevm_per_symbol_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPBCHDataConstellationTraceResponse
mod_acc_fetch_pbch_data_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPBCHDataConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPBCHDataConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPBCHDataConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPBCHDataConstellationTraceInterleavedIQResponse
mod_acc_fetch_pbch_data_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPBCHDataConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPBCHDataConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchPBCHDataConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchPBCHDataConstellationTraceSplitResponse
mod_acc_fetch_pbch_data_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPBCHDataConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPBCHDataConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchPBCHDataConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTraceResponse
mod_acc_fetch_pbch_data_rmsevm_per_subcarrier_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPBCHDataRMSEVMPerSymbolMeanTraceResponse
mod_acc_fetch_pbch_data_rmsevm_per_symbol_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPBCHDataRMSEVMPerSymbolMeanTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPBCHDataRMSEVMPerSymbolMeanTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH1024QAMConstellationTraceResponse
mod_acc_fetch_pdsch1024q_am_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH1024QAMConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH1024QAMConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH1024QAMConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQResponse
mod_acc_fetch_pdsch1024q_am_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH1024QAMConstellationTraceSplitResponse
mod_acc_fetch_pdsch1024q_am_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH1024QAMConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH1024QAMConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH1024QAMConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH16QAMConstellationTraceResponse
mod_acc_fetch_pdsch16q_am_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH16QAMConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH16QAMConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH16QAMConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQResponse
mod_acc_fetch_pdsch16q_am_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH16QAMConstellationTraceSplitResponse
mod_acc_fetch_pdsch16q_am_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH16QAMConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH16QAMConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH16QAMConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH256QAMConstellationTraceResponse
mod_acc_fetch_pdsch256q_am_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH256QAMConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH256QAMConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH256QAMConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQResponse
mod_acc_fetch_pdsch256q_am_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH256QAMConstellationTraceSplitResponse
mod_acc_fetch_pdsch256q_am_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH256QAMConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH256QAMConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH256QAMConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH4096QAMConstellationTraceResponse
mod_acc_fetch_pdsch4096q_am_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH4096QAMConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH4096QAMConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH4096QAMConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQResponse
mod_acc_fetch_pdsch4096q_am_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH4096QAMConstellationTraceSplitResponse
mod_acc_fetch_pdsch4096q_am_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH4096QAMConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH4096QAMConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH4096QAMConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH64QAMConstellationTraceResponse
mod_acc_fetch_pdsch64q_am_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH64QAMConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH64QAMConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH64QAMConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQResponse
mod_acc_fetch_pdsch64q_am_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH64QAMConstellationTraceSplitResponse
mod_acc_fetch_pdsch64q_am_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH64QAMConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH64QAMConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH64QAMConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH8PSKConstellationTraceResponse
mod_acc_fetch_pdsch8p_sk_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH8PSKConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH8PSKConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH8PSKConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQResponse
mod_acc_fetch_pdsch8p_sk_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCH8PSKConstellationTraceSplitResponse
mod_acc_fetch_pdsch8p_sk_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCH8PSKConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCH8PSKConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCH8PSKConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCHDMRSConstellationTraceResponse
mod_acc_fetch_pdschdmrs_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCHDMRSConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCHDMRSConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCHDMRSConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQResponse
mod_acc_fetch_pdschdmrs_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCHDMRSConstellationTraceSplitResponse
mod_acc_fetch_pdschdmrs_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCHDMRSConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCHDMRSConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCHDMRSConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCHDataConstellationTraceResponse
mod_acc_fetch_pdsch_data_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCHDataConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCHDataConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCHDataConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCHDataConstellationTraceInterleavedIQResponse
mod_acc_fetch_pdsch_data_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCHDataConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCHDataConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCHDataConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCHDataConstellationTraceSplitResponse
mod_acc_fetch_pdsch_data_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCHDataConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCHDataConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCHDataConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCHDemodulatedBitsResponse
mod_acc_fetch_pdsch_demodulated_bits(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCHDemodulatedBitsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCHDemodulatedBitsResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCHDemodulatedBits(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCHPTRSConstellationTraceResponse
mod_acc_fetch_pdschptrs_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCHPTRSConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCHPTRSConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCHPTRSConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQResponse
mod_acc_fetch_pdschptrs_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCHPTRSConstellationTraceSplitResponse
mod_acc_fetch_pdschptrs_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCHPTRSConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCHPTRSConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCHPTRSConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCHQPSKConstellationTraceResponse
mod_acc_fetch_pdschqpsk_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCHQPSKConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCHQPSKConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCHQPSKConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQResponse
mod_acc_fetch_pdschqpsk_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchPDSCHQPSKConstellationTraceSplitResponse
mod_acc_fetch_pdschqpsk_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPDSCHQPSKConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPDSCHQPSKConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchPDSCHQPSKConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchPSSConstellationTraceResponse
mod_acc_fetch_pss_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPSSConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPSSConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPSSConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPSSConstellationTraceInterleavedIQResponse
mod_acc_fetch_pss_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPSSConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPSSConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchPSSConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchPSSConstellationTraceSplitResponse
mod_acc_fetch_pss_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPSSConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPSSConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchPSSConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchPSSRMSEVMPerSubcarrierMeanTraceResponse
mod_acc_fetch_pssrmsevm_per_subcarrier_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPSSRMSEVMPerSubcarrierMeanTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPSSRMSEVMPerSubcarrierMeanTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPSSRMSEVMPerSymbolMeanTraceResponse
mod_acc_fetch_pssrmsevm_per_symbol_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPSSRMSEVMPerSymbolMeanTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPSSRMSEVMPerSymbolMeanTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPSSRMSEVMPerSymbolMeanTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPUSCHDMRSConstellationTraceResponse
mod_acc_fetch_puschdmrs_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPUSCHDMRSConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPUSCHDMRSConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPUSCHDMRSConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQResponse
mod_acc_fetch_puschdmrs_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchPUSCHDMRSConstellationTraceSplitResponse
mod_acc_fetch_puschdmrs_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPUSCHDMRSConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPUSCHDMRSConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchPUSCHDMRSConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchPUSCHDataConstellationTraceResponse
mod_acc_fetch_pusch_data_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPUSCHDataConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPUSCHDataConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPUSCHDataConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPUSCHDataConstellationTraceInterleavedIQResponse
mod_acc_fetch_pusch_data_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPUSCHDataConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPUSCHDataConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchPUSCHDataConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchPUSCHDataConstellationTraceSplitResponse
mod_acc_fetch_pusch_data_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPUSCHDataConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPUSCHDataConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchPUSCHDataConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchPUSCHDemodulatedBitsResponse
mod_acc_fetch_pusch_demodulated_bits(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPUSCHDemodulatedBitsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPUSCHDemodulatedBitsResponse{};

  raise_if_error(
      stub->ModAccFetchPUSCHDemodulatedBits(&context, request, &response),
      context);

  return response;
}

ModAccFetchPUSCHPTRSConstellationTraceResponse
mod_acc_fetch_puschptrs_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPUSCHPTRSConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPUSCHPTRSConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPUSCHPTRSConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQResponse
mod_acc_fetch_puschptrs_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchPUSCHPTRSConstellationTraceSplitResponse
mod_acc_fetch_puschptrs_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPUSCHPTRSConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPUSCHPTRSConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchPUSCHPTRSConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchPUSCHPhaseOffsetTraceResponse
mod_acc_fetch_pusch_phase_offset_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPUSCHPhaseOffsetTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPUSCHPhaseOffsetTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPUSCHPhaseOffsetTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPeakEVMHighPerSymbolMaximumTraceResponse
mod_acc_fetch_peak_evm_high_per_symbol_maximum_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPeakEVMHighPerSymbolMaximumTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPeakEVMHighPerSymbolMaximumTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPeakEVMHighPerSymbolMaximumTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPeakEVMLowPerSymbolMaximumTraceResponse
mod_acc_fetch_peak_evm_low_per_symbol_maximum_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPeakEVMLowPerSymbolMaximumTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPeakEVMLowPerSymbolMaximumTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPeakEVMLowPerSymbolMaximumTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPeakEVMPerSlotMaximumTraceResponse
mod_acc_fetch_peak_evm_per_slot_maximum_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPeakEVMPerSlotMaximumTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPeakEVMPerSlotMaximumTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPeakEVMPerSlotMaximumTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPeakEVMPerSubcarrierMaximumTraceResponse
mod_acc_fetch_peak_evm_per_subcarrier_maximum_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPeakEVMPerSubcarrierMaximumTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPeakEVMPerSubcarrierMaximumTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPeakEVMPerSubcarrierMaximumTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchPeakEVMPerSymbolMaximumTraceResponse
mod_acc_fetch_peak_evm_per_symbol_maximum_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPeakEVMPerSymbolMaximumTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPeakEVMPerSymbolMaximumTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPeakEVMPerSymbolMaximumTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchRMSEVMHighPerSymbolMeanTraceResponse
mod_acc_fetch_rmsevm_high_per_symbol_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchRMSEVMHighPerSymbolMeanTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchRMSEVMHighPerSymbolMeanTraceResponse{};

  raise_if_error(
      stub->ModAccFetchRMSEVMHighPerSymbolMeanTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchRMSEVMLowPerSymbolMeanTraceResponse
mod_acc_fetch_rmsevm_low_per_symbol_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchRMSEVMLowPerSymbolMeanTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchRMSEVMLowPerSymbolMeanTraceResponse{};

  raise_if_error(
      stub->ModAccFetchRMSEVMLowPerSymbolMeanTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchRMSEVMPerSlotMeanTraceResponse
mod_acc_fetch_rmsevm_per_slot_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchRMSEVMPerSlotMeanTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchRMSEVMPerSlotMeanTraceResponse{};

  raise_if_error(
      stub->ModAccFetchRMSEVMPerSlotMeanTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchRMSEVMPerSubcarrierMeanTraceResponse
mod_acc_fetch_rmsevm_per_subcarrier_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchRMSEVMPerSubcarrierMeanTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchRMSEVMPerSubcarrierMeanTraceResponse{};

  raise_if_error(
      stub->ModAccFetchRMSEVMPerSubcarrierMeanTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchRMSEVMPerSymbolMeanTraceResponse
mod_acc_fetch_rmsevm_per_symbol_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchRMSEVMPerSymbolMeanTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchRMSEVMPerSymbolMeanTraceResponse{};

  raise_if_error(
      stub->ModAccFetchRMSEVMPerSymbolMeanTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchSSSConstellationTraceResponse
mod_acc_fetch_sss_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchSSSConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchSSSConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchSSSConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchSSSConstellationTraceInterleavedIQResponse
mod_acc_fetch_sss_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchSSSConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchSSSConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchSSSConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchSSSConstellationTraceSplitResponse
mod_acc_fetch_sss_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchSSSConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchSSSConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchSSSConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchSSSRMSEVMPerSubcarrierMeanTraceResponse
mod_acc_fetch_sssrmsevm_per_subcarrier_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchSSSRMSEVMPerSubcarrierMeanTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchSSSRMSEVMPerSubcarrierMeanTraceResponse{};

  raise_if_error(
      stub->ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchSSSRMSEVMPerSymbolMeanTraceResponse
mod_acc_fetch_sssrmsevm_per_symbol_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchSSSRMSEVMPerSymbolMeanTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchSSSRMSEVMPerSymbolMeanTraceResponse{};

  raise_if_error(
      stub->ModAccFetchSSSRMSEVMPerSymbolMeanTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchSpectralFlatnessTraceResponse
mod_acc_fetch_spectral_flatness_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchSpectralFlatnessTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchSpectralFlatnessTraceResponse{};

  raise_if_error(
      stub->ModAccFetchSpectralFlatnessTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchSubblockInBandEmissionTraceResponse
mod_acc_fetch_subblock_in_band_emission_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchSubblockInBandEmissionTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchSubblockInBandEmissionTraceResponse{};

  raise_if_error(
      stub->ModAccFetchSubblockInBandEmissionTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchTransientPeriodLocationsTraceResponse
mod_acc_fetch_transient_period_locations_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchTransientPeriodLocationsTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchTransientPeriodLocationsTraceResponse{};

  raise_if_error(
      stub->ModAccFetchTransientPeriodLocationsTrace(&context, request, &response),
      context);

  return response;
}

ModAccValidateCalibrationDataResponse
mod_acc_validate_calibration_data(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string)
{
  ::grpc::ClientContext context;

  auto request = ModAccValidateCalibrationDataRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);

  auto response = ModAccValidateCalibrationDataResponse{};

  raise_if_error(
      stub->ModAccValidateCalibrationData(&context, request, &response),
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

PVTCfgAveragingResponse
pvt_cfg_averaging(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<PvtAveragingEnabled, pb::int32>& averaging_enabled, const pb::int32& averaging_count, const simple_variant<PvtAveragingType, pb::int32>& averaging_type)
{
  ::grpc::ClientContext context;

  auto request = PVTCfgAveragingRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto averaging_enabled_ptr = averaging_enabled.get_if<PvtAveragingEnabled>();
  const auto averaging_enabled_raw_ptr = averaging_enabled.get_if<pb::int32>();
  if (averaging_enabled_ptr) {
    request.set_averaging_enabled(*averaging_enabled_ptr);
  }
  else if (averaging_enabled_raw_ptr) {
    request.set_averaging_enabled_raw(*averaging_enabled_raw_ptr);
  }
  request.set_averaging_count(averaging_count);
  const auto averaging_type_ptr = averaging_type.get_if<PvtAveragingType>();
  const auto averaging_type_raw_ptr = averaging_type.get_if<pb::int32>();
  if (averaging_type_ptr) {
    request.set_averaging_type(*averaging_type_ptr);
  }
  else if (averaging_type_raw_ptr) {
    request.set_averaging_type_raw(*averaging_type_raw_ptr);
  }

  auto response = PVTCfgAveragingResponse{};

  raise_if_error(
      stub->PVTCfgAveraging(&context, request, &response),
      context);

  return response;
}

PVTCfgMeasurementMethodResponse
pvt_cfg_measurement_method(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<PvtMeasurementMethod, pb::int32>& measurement_method)
{
  ::grpc::ClientContext context;

  auto request = PVTCfgMeasurementMethodRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto measurement_method_ptr = measurement_method.get_if<PvtMeasurementMethod>();
  const auto measurement_method_raw_ptr = measurement_method.get_if<pb::int32>();
  if (measurement_method_ptr) {
    request.set_measurement_method(*measurement_method_ptr);
  }
  else if (measurement_method_raw_ptr) {
    request.set_measurement_method_raw(*measurement_method_raw_ptr);
  }

  auto response = PVTCfgMeasurementMethodResponse{};

  raise_if_error(
      stub->PVTCfgMeasurementMethod(&context, request, &response),
      context);

  return response;
}

PVTCfgOFFPowerExclusionPeriodsResponse
pvt_cfg_off_power_exclusion_periods(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& off_power_exclusion_before, const double& off_power_exclusion_after)
{
  ::grpc::ClientContext context;

  auto request = PVTCfgOFFPowerExclusionPeriodsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_off_power_exclusion_before(off_power_exclusion_before);
  request.set_off_power_exclusion_after(off_power_exclusion_after);

  auto response = PVTCfgOFFPowerExclusionPeriodsResponse{};

  raise_if_error(
      stub->PVTCfgOFFPowerExclusionPeriods(&context, request, &response),
      context);

  return response;
}

PVTFetchMeasurementResponse
pvt_fetch_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = PVTFetchMeasurementRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = PVTFetchMeasurementResponse{};

  raise_if_error(
      stub->PVTFetchMeasurement(&context, request, &response),
      context);

  return response;
}

PVTFetchMeasurementArrayResponse
pvt_fetch_measurement_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = PVTFetchMeasurementArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = PVTFetchMeasurementArrayResponse{};

  raise_if_error(
      stub->PVTFetchMeasurementArray(&context, request, &response),
      context);

  return response;
}

PVTFetchSignalPowerTraceResponse
pvt_fetch_signal_power_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = PVTFetchSignalPowerTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = PVTFetchSignalPowerTraceResponse{};

  raise_if_error(
      stub->PVTFetchSignalPowerTrace(&context, request, &response),
      context);

  return response;
}

PVTFetchWindowedSignalPowerTraceResponse
pvt_fetch_windowed_signal_power_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = PVTFetchWindowedSignalPowerTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = PVTFetchWindowedSignalPowerTraceResponse{};

  raise_if_error(
      stub->PVTFetchWindowedSignalPowerTrace(&context, request, &response),
      context);

  return response;
}

ResetAttributeResponse
reset_attribute(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id)
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

SEMCfgComponentCarrierRatedOutputPowerResponse
sem_cfg_component_carrier_rated_output_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& component_carrier_rated_output_power)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgComponentCarrierRatedOutputPowerRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_component_carrier_rated_output_power(component_carrier_rated_output_power);

  auto response = SEMCfgComponentCarrierRatedOutputPowerResponse{};

  raise_if_error(
      stub->SEMCfgComponentCarrierRatedOutputPower(&context, request, &response),
      context);

  return response;
}

SEMCfgComponentCarrierRatedOutputPowerArrayResponse
sem_cfg_component_carrier_rated_output_power_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::vector<double>& component_carrier_rated_output_power)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgComponentCarrierRatedOutputPowerArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  copy_array(component_carrier_rated_output_power, request.mutable_component_carrier_rated_output_power());

  auto response = SEMCfgComponentCarrierRatedOutputPowerArrayResponse{};

  raise_if_error(
      stub->SEMCfgComponentCarrierRatedOutputPowerArray(&context, request, &response),
      context);

  return response;
}

SEMCfgNumberOfOffsetsResponse
sem_cfg_number_of_offsets(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& number_of_offsets)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgNumberOfOffsetsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_number_of_offsets(number_of_offsets);

  auto response = SEMCfgNumberOfOffsetsResponse{};

  raise_if_error(
      stub->SEMCfgNumberOfOffsets(&context, request, &response),
      context);

  return response;
}

SEMCfgOffsetAbsoluteLimitResponse
sem_cfg_offset_absolute_limit(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& absolute_limit_start, const double& absolute_limit_stop)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgOffsetAbsoluteLimitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_absolute_limit_start(absolute_limit_start);
  request.set_absolute_limit_stop(absolute_limit_stop);

  auto response = SEMCfgOffsetAbsoluteLimitResponse{};

  raise_if_error(
      stub->SEMCfgOffsetAbsoluteLimit(&context, request, &response),
      context);

  return response;
}

SEMCfgOffsetAbsoluteLimitArrayResponse
sem_cfg_offset_absolute_limit_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::vector<double>& absolute_limit_start, const std::vector<double>& absolute_limit_stop)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgOffsetAbsoluteLimitArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  copy_array(absolute_limit_start, request.mutable_absolute_limit_start());
  copy_array(absolute_limit_stop, request.mutable_absolute_limit_stop());

  auto response = SEMCfgOffsetAbsoluteLimitArrayResponse{};

  raise_if_error(
      stub->SEMCfgOffsetAbsoluteLimitArray(&context, request, &response),
      context);

  return response;
}

SEMCfgOffsetBandwidthIntegralResponse
sem_cfg_offset_bandwidth_integral(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& bandwidth_integral)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgOffsetBandwidthIntegralRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_bandwidth_integral(bandwidth_integral);

  auto response = SEMCfgOffsetBandwidthIntegralResponse{};

  raise_if_error(
      stub->SEMCfgOffsetBandwidthIntegral(&context, request, &response),
      context);

  return response;
}

SEMCfgOffsetBandwidthIntegralArrayResponse
sem_cfg_offset_bandwidth_integral_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::vector<pb::int32>& bandwidth_integral)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgOffsetBandwidthIntegralArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  copy_array(bandwidth_integral, request.mutable_bandwidth_integral());

  auto response = SEMCfgOffsetBandwidthIntegralArrayResponse{};

  raise_if_error(
      stub->SEMCfgOffsetBandwidthIntegralArray(&context, request, &response),
      context);

  return response;
}

SEMCfgOffsetFrequencyResponse
sem_cfg_offset_frequency(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& offset_start_frequency, const double& offset_stop_frequency, const simple_variant<SemOffsetSideband, pb::int32>& offset_sideband)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgOffsetFrequencyRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_offset_start_frequency(offset_start_frequency);
  request.set_offset_stop_frequency(offset_stop_frequency);
  const auto offset_sideband_ptr = offset_sideband.get_if<SemOffsetSideband>();
  const auto offset_sideband_raw_ptr = offset_sideband.get_if<pb::int32>();
  if (offset_sideband_ptr) {
    request.set_offset_sideband(*offset_sideband_ptr);
  }
  else if (offset_sideband_raw_ptr) {
    request.set_offset_sideband_raw(*offset_sideband_raw_ptr);
  }

  auto response = SEMCfgOffsetFrequencyResponse{};

  raise_if_error(
      stub->SEMCfgOffsetFrequency(&context, request, &response),
      context);

  return response;
}

SEMCfgOffsetFrequencyArrayResponse
sem_cfg_offset_frequency_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::vector<double>& offset_start_frequency, const std::vector<double>& offset_stop_frequency, const std::vector<pb::int32>& offset_sideband)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgOffsetFrequencyArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  copy_array(offset_start_frequency, request.mutable_offset_start_frequency());
  copy_array(offset_stop_frequency, request.mutable_offset_stop_frequency());
  copy_array(offset_sideband, request.mutable_offset_sideband());

  auto response = SEMCfgOffsetFrequencyArrayResponse{};

  raise_if_error(
      stub->SEMCfgOffsetFrequencyArray(&context, request, &response),
      context);

  return response;
}

SEMCfgOffsetLimitFailMaskResponse
sem_cfg_offset_limit_fail_mask(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<SemOffsetLimitFailMask, pb::int32>& limit_fail_mask)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgOffsetLimitFailMaskRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto limit_fail_mask_ptr = limit_fail_mask.get_if<SemOffsetLimitFailMask>();
  const auto limit_fail_mask_raw_ptr = limit_fail_mask.get_if<pb::int32>();
  if (limit_fail_mask_ptr) {
    request.set_limit_fail_mask(*limit_fail_mask_ptr);
  }
  else if (limit_fail_mask_raw_ptr) {
    request.set_limit_fail_mask_raw(*limit_fail_mask_raw_ptr);
  }

  auto response = SEMCfgOffsetLimitFailMaskResponse{};

  raise_if_error(
      stub->SEMCfgOffsetLimitFailMask(&context, request, &response),
      context);

  return response;
}

SEMCfgOffsetLimitFailMaskArrayResponse
sem_cfg_offset_limit_fail_mask_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::vector<pb::int32>& limit_fail_mask)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgOffsetLimitFailMaskArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  copy_array(limit_fail_mask, request.mutable_limit_fail_mask());

  auto response = SEMCfgOffsetLimitFailMaskArrayResponse{};

  raise_if_error(
      stub->SEMCfgOffsetLimitFailMaskArray(&context, request, &response),
      context);

  return response;
}

SEMCfgOffsetRBWFilterResponse
sem_cfg_offset_rbw_filter(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& offset_rbw, const simple_variant<SemOffsetRbwFilterType, pb::int32>& offset_rbw_filter_type)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgOffsetRBWFilterRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_offset_rbw(offset_rbw);
  const auto offset_rbw_filter_type_ptr = offset_rbw_filter_type.get_if<SemOffsetRbwFilterType>();
  const auto offset_rbw_filter_type_raw_ptr = offset_rbw_filter_type.get_if<pb::int32>();
  if (offset_rbw_filter_type_ptr) {
    request.set_offset_rbw_filter_type(*offset_rbw_filter_type_ptr);
  }
  else if (offset_rbw_filter_type_raw_ptr) {
    request.set_offset_rbw_filter_type_raw(*offset_rbw_filter_type_raw_ptr);
  }

  auto response = SEMCfgOffsetRBWFilterResponse{};

  raise_if_error(
      stub->SEMCfgOffsetRBWFilter(&context, request, &response),
      context);

  return response;
}

SEMCfgOffsetRBWFilterArrayResponse
sem_cfg_offset_rbw_filter_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::vector<double>& offset_rbw, const std::vector<pb::int32>& offset_rbw_filter_type)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgOffsetRBWFilterArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  copy_array(offset_rbw, request.mutable_offset_rbw());
  copy_array(offset_rbw_filter_type, request.mutable_offset_rbw_filter_type());

  auto response = SEMCfgOffsetRBWFilterArrayResponse{};

  raise_if_error(
      stub->SEMCfgOffsetRBWFilterArray(&context, request, &response),
      context);

  return response;
}

SEMCfgOffsetRelativeLimitResponse
sem_cfg_offset_relative_limit(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& relative_limit_start, const double& relative_limit_stop)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgOffsetRelativeLimitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_relative_limit_start(relative_limit_start);
  request.set_relative_limit_stop(relative_limit_stop);

  auto response = SEMCfgOffsetRelativeLimitResponse{};

  raise_if_error(
      stub->SEMCfgOffsetRelativeLimit(&context, request, &response),
      context);

  return response;
}

SEMCfgOffsetRelativeLimitArrayResponse
sem_cfg_offset_relative_limit_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::vector<double>& relative_limit_start, const std::vector<double>& relative_limit_stop)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgOffsetRelativeLimitArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  copy_array(relative_limit_start, request.mutable_relative_limit_start());
  copy_array(relative_limit_stop, request.mutable_relative_limit_stop());

  auto response = SEMCfgOffsetRelativeLimitArrayResponse{};

  raise_if_error(
      stub->SEMCfgOffsetRelativeLimitArray(&context, request, &response),
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

SEMCfgUplinkMaskTypeResponse
sem_cfg_uplink_mask_type(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<SemUplinkMaskType, pb::int32>& uplink_mask_type)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgUplinkMaskTypeRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto uplink_mask_type_ptr = uplink_mask_type.get_if<SemUplinkMaskType>();
  const auto uplink_mask_type_raw_ptr = uplink_mask_type.get_if<pb::int32>();
  if (uplink_mask_type_ptr) {
    request.set_uplink_mask_type(*uplink_mask_type_ptr);
  }
  else if (uplink_mask_type_raw_ptr) {
    request.set_uplink_mask_type_raw(*uplink_mask_type_raw_ptr);
  }

  auto response = SEMCfgUplinkMaskTypeResponse{};

  raise_if_error(
      stub->SEMCfgUplinkMaskType(&context, request, &response),
      context);

  return response;
}

SEMFetchComponentCarrierMeasurementResponse
sem_fetch_component_carrier_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SEMFetchComponentCarrierMeasurementRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SEMFetchComponentCarrierMeasurementResponse{};

  raise_if_error(
      stub->SEMFetchComponentCarrierMeasurement(&context, request, &response),
      context);

  return response;
}

SEMFetchComponentCarrierMeasurementArrayResponse
sem_fetch_component_carrier_measurement_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SEMFetchComponentCarrierMeasurementArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SEMFetchComponentCarrierMeasurementArrayResponse{};

  raise_if_error(
      stub->SEMFetchComponentCarrierMeasurementArray(&context, request, &response),
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

SEMFetchSubblockMeasurementResponse
sem_fetch_subblock_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SEMFetchSubblockMeasurementRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SEMFetchSubblockMeasurementResponse{};

  raise_if_error(
      stub->SEMFetchSubblockMeasurement(&context, request, &response),
      context);

  return response;
}

SEMFetchTotalAggregatedPowerResponse
sem_fetch_total_aggregated_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SEMFetchTotalAggregatedPowerRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SEMFetchTotalAggregatedPowerResponse{};

  raise_if_error(
      stub->SEMFetchTotalAggregatedPower(&context, request, &response),
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
select_measurements(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<MeasurementTypes, pb::uint32>& measurements, const bool& enable_all_traces)
{
  ::grpc::ClientContext context;

  auto request = SelectMeasurementsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto measurements_ptr = measurements.get_if<MeasurementTypes>();
  const auto measurements_raw_ptr = measurements.get_if<pb::uint32>();
  if (measurements_ptr) {
    request.set_measurements(*measurements_ptr);
  }
  else if (measurements_raw_ptr) {
    request.set_measurements_raw(*measurements_raw_ptr);
  }
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
set_attribute_f32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const float& attr_val)
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
set_attribute_f32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<float>& attr_val)
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
set_attribute_f64(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const double& attr_val)
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
set_attribute_f64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<double>& attr_val)
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
set_attribute_i16(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const pb::int32& attr_val)
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
set_attribute_i32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const simple_variant<NiRFmxNRInt32AttributeValues, pb::int32>& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeI32Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  const auto attr_val_ptr = attr_val.get_if<NiRFmxNRInt32AttributeValues>();
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
set_attribute_i32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<pb::int32>& attr_val)
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
set_attribute_i64(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const pb::int64& attr_val)
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
set_attribute_i64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<pb::int64>& attr_val)
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
set_attribute_i8(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const pb::int32& attr_val)
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
set_attribute_i8_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<pb::int32>& attr_val)
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
set_attribute_ni_complex_double_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<nidevice_grpc::NIComplexNumber>& attr_val)
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
set_attribute_ni_complex_single_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<nidevice_grpc::NIComplexNumberF32>& attr_val)
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
set_attribute_string(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const simple_variant<NiRFmxNRStringAttributeValuesMapped, std::string>& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeStringRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  const auto attr_val_ptr = attr_val.get_if<NiRFmxNRStringAttributeValuesMapped>();
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
set_attribute_u16(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const pb::uint32& attr_val)
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
set_attribute_u32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const pb::uint32& attr_val)
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
set_attribute_u32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<pb::uint32>& attr_val)
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
set_attribute_u64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<pb::uint64>& attr_val)
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
set_attribute_u8(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const pb::uint32& attr_val)
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
set_attribute_u8_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::string& attr_val)
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

TXPFetchMeasurementResponse
txp_fetch_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = TXPFetchMeasurementRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = TXPFetchMeasurementResponse{};

  raise_if_error(
      stub->TXPFetchMeasurement(&context, request, &response),
      context);

  return response;
}

TXPFetchPowerTraceResponse
txp_fetch_power_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = TXPFetchPowerTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = TXPFetchPowerTraceResponse{};

  raise_if_error(
      stub->TXPFetchPowerTrace(&context, request, &response),
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


} // namespace nirfmxnr_grpc::experimental::client
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/nirfmxnr/nirfmxnr_client.h sha256=b65156cd4277ec4a85da0fe1dc3e786b02e49a17094e5e674cc667b1a212b193 bytes=58665 -->
## FILE: generated/nirfmxnr/nirfmxnr_client.h

- repository: `ni/grpc-device`
- source_path: `generated/nirfmxnr/nirfmxnr_client.h`
- sha256: `b65156cd4277ec4a85da0fe1dc3e786b02e49a17094e5e674cc667b1a212b193`
- bytes: 58665

````c

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// EXPERIMENTAL Client convenience wrapper for NI-RFMXNR.
//---------------------------------------------------------------------
#ifndef NIRFMXNR_GRPC_CLIENT_H
#define NIRFMXNR_GRPC_CLIENT_H

#include <grpcpp/grpcpp.h>

#include <nirfmxnr.grpc.pb.h>
#include <tests/utilities/client_helpers.h>

#include <memory>
#include <vector>

namespace nirfmxnr_grpc::experimental::client {

namespace pb = ::google::protobuf;
using StubPtr = std::unique_ptr<NiRFmxNR::Stub>;
using namespace nidevice_grpc::experimental::client;


ACPCfgAveragingResponse acp_cfg_averaging(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<AcpAveragingEnabled, pb::int32>& averaging_enabled, const pb::int32& averaging_count, const simple_variant<AcpAveragingType, pb::int32>& averaging_type);
ACPCfgMeasurementMethodResponse acp_cfg_measurement_method(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<AcpMeasurementMethod, pb::int32>& measurement_method);
ACPCfgNoiseCompensationEnabledResponse acp_cfg_noise_compensation_enabled(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<AcpNoiseCompensationEnabled, pb::int32>& noise_compensation_enabled);
ACPCfgNumberOfENDCOffsetsResponse acp_cfg_number_of_endc_offsets(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& number_of_endc_offsets);
ACPCfgNumberOfEUTRAOffsetsResponse acp_cfg_number_of_eutra_offsets(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& number_of_eutra_offsets);
ACPCfgNumberOfNROffsetsResponse acp_cfg_number_of_nr_offsets(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& number_of_nr_offsets);
ACPCfgNumberOfUTRAOffsetsResponse acp_cfg_number_of_utra_offsets(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& number_of_utra_offsets);
ACPCfgPowerUnitsResponse acp_cfg_power_units(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<AcpPowerUnits, pb::int32>& power_units);
ACPCfgRBWFilterResponse acp_cfg_rbw_filter(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<AcpRbwAutoBandwidth, pb::int32>& rbw_auto, const double& rbw, const simple_variant<AcpRbwFilterType, pb::int32>& rbw_filter_type);
ACPCfgSweepTimeResponse acp_cfg_sweep_time(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<AcpSweepTimeAuto, pb::int32>& sweep_time_auto, const double& sweep_time_interval);
ACPFetchAbsolutePowersTraceResponse acp_fetch_absolute_powers_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout, const pb::int32& trace_index);
ACPFetchComponentCarrierMeasurementResponse acp_fetch_component_carrier_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ACPFetchComponentCarrierMeasurementArrayResponse acp_fetch_component_carrier_measurement_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ACPFetchOffsetMeasurementResponse acp_fetch_offset_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ACPFetchOffsetMeasurementArrayResponse acp_fetch_offset_measurement_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ACPFetchRelativePowersTraceResponse acp_fetch_relative_powers_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout, const pb::int32& trace_index);
ACPFetchSpectrumResponse acp_fetch_spectrum(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ACPFetchSubblockMeasurementResponse acp_fetch_subblock_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ACPFetchTotalAggregatedPowerResponse acp_fetch_total_aggregated_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ACPValidateNoiseCalibrationDataResponse acp_validate_noise_calibration_data(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
AbortMeasurementsResponse abort_measurements(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
AnalyzeIQ1WaveformResponse analyze_iq1_waveform(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const double& x0, const double& dx, const std::vector<nidevice_grpc::NIComplexNumberF32>& iq, const pb::int32& reset);
AnalyzeIQ1WaveformInterleavedIQResponse analyze_iq1_waveform_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const double& x0, const double& dx, const std::vector<float>& iq, const pb::int32& reset);
AnalyzeIQ1WaveformSplitResponse analyze_iq1_waveform_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const double& x0, const double& dx, const std::vector<float>& iqi, const std::vector<float>& iqq, const pb::int32& reset);
AnalyzeNWaveformsIQResponse analyze_n_waveforms_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const std::vector<double>& x0, const std::vector<double>& dx, const std::vector<nidevice_grpc::NIComplexNumberF32>& iq, const std::vector<pb::int32>& iq_sizes, const pb::int32& reset);
AnalyzeNWaveformsIQInterleavedIQResponse analyze_n_waveforms_iq_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const std::vector<double>& x0, const std::vector<double>& dx, const std::vector<float>& iq, const std::vector<pb::int32>& iq_sizes, const pb::int32& reset);
AnalyzeNWaveformsIQSplitResponse analyze_n_waveforms_iq_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const std::vector<double>& x0, const std::vector<double>& dx, const std::vector<float>& iqi, const std::vector<float>& iqq, const std::vector<pb::int32>& iq_sizes, const pb::int32& reset);
AnalyzeNWaveformsSpectrumResponse analyze_n_waveforms_spectrum(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const std::vector<double>& x0, const std::vector<double>& dx, const std::vector<float>& spectrum, const std::vector<pb::int32>& spectrum_sizes, const pb::int32& reset);
AnalyzeSpectrum1WaveformResponse analyze_spectrum1_waveform(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const double& x0, const double& dx, const std::vector<float>& spectrum, const pb::int32& reset);
AutoLevelResponse auto_level(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& measurement_interval);
BuildBandwidthPartStringResponse build_bandwidth_part_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& bandwidth_part_number);
BuildCORESETClusterStringResponse build_coreset_cluster_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& coreset_cluster_number);
BuildCORESETStringResponse build_coreset_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& coreset_number);
BuildCarrierStringResponse build_carrier_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& carrier_number);
BuildListStepStringResponse build_list_step_string(const StubPtr& stub, const std::string& list_name, const std::string& result_name, const pb::int32& step_number);
BuildListStringResponse build_list_string(const StubPtr& stub, const std::string& list_name, const std::string& result_name);
BuildOffsetStringResponse build_offset_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& offset_number);
BuildPDCCHStringResponse build_pdcch_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& pdcch_number);
BuildPDSCHClusterStringResponse build_pdsch_cluster_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& pdsch_cluster_number);
BuildPDSCHStringResponse build_pdsch_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& pdsch_number);
BuildPUSCHClusterStringResponse build_pusch_cluster_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& pusch_cluster_number);
BuildPUSCHStringResponse build_pusch_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& pusch_number);
BuildSignalStringResponse build_signal_string(const StubPtr& stub, const std::string& signal_name, const std::string& result_name);
BuildSubblockStringResponse build_subblock_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& subblock_number);
BuildUserStringResponse build_user_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& user_number);
CHPCfgAveragingResponse chp_cfg_averaging(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ChpAveragingEnabled, pb::int32>& averaging_enabled, const pb::int32& averaging_count, const simple_variant<ChpAveragingType, pb::int32>& averaging_type);
CHPCfgRBWFilterResponse chp_cfg_rbw_filter(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ChpRbwAutoBandwidth, pb::int32>& rbw_auto, const double& rbw, const simple_variant<ChpRbwFilterType, pb::int32>& rbw_filter_type);
CHPCfgSweepTimeResponse chp_cfg_sweep_time(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ChpSweepTimeAuto, pb::int32>& sweep_time_auto, const double& sweep_time_interval);
CHPFetchComponentCarrierMeasurementResponse chp_fetch_component_carrier_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CHPFetchComponentCarrierMeasurementArrayResponse chp_fetch_component_carrier_measurement_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CHPFetchSpectrumResponse chp_fetch_spectrum(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CHPFetchSubblockPowerResponse chp_fetch_subblock_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CHPFetchTotalAggregatedPowerResponse chp_fetch_total_aggregated_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CHPValidateNoiseCalibrationDataResponse chp_validate_noise_calibration_data(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
CfgDigitalEdgeTriggerResponse cfg_digital_edge_trigger(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<DigitalEdgeTriggerSource, std::string>& digital_edge_source, const simple_variant<DigitalEdgeTriggerEdge, pb::int32>& digital_edge, const double& trigger_delay, const pb::int32& enable_trigger);
CfgExternalAttenuationResponse cfg_external_attenuation(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& external_attenuation);
CfgFrequencyResponse cfg_frequency(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& center_frequency);
CfgFrequencyReferenceResponse cfg_frequency_reference(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& channel_name, const simple_variant<FrequencyReferenceSource, std::string>& frequency_reference_source, const double& frequency_reference_frequency);
CfgIQPowerEdgeTriggerResponse cfg_iq_power_edge_trigger(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& iq_power_edge_source, const simple_variant<IQPowerEdgeTriggerSlope, pb::int32>& iq_power_edge_slope, const double& iq_power_edge_level, const double& trigger_delay, const simple_variant<TriggerMinimumQuietTimeMode, pb::int32>& trigger_min_quiet_time_mode, const double& trigger_min_quiet_time_duration, const simple_variant<IQPowerEdgeTriggerLevelType, pb::int32>& iq_power_edge_level_type, const pb::int32& enable_trigger);
CfgMechanicalAttenuationResponse cfg_mechanical_attenuation(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& channel_name, const simple_variant<MechanicalAttenuationAuto, pb::int32>& mechanical_attenuation_auto, const double& mechanical_attenuation_value);
CfgRFResponse cfg_rf(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& center_frequency, const double& reference_level, const double& external_attenuation);
CfgRFAttenuationResponse cfg_rf_attenuation(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& channel_name, const simple_variant<RFAttenuationAuto, pb::int32>& rf_attenuation_auto, const double& rf_attenuation_value);
CfgReferenceLevelResponse cfg_reference_level(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& reference_level);
CfgSelectedPortsMultipleResponse cfg_selected_ports_multiple(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& selected_ports);
CfgSoftwareEdgeTriggerResponse cfg_software_edge_trigger(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& trigger_delay, const pb::int32& enable_trigger);
CfggNodeBCategoryResponse cfgg_node_b_category(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<GNodeBCategory, pb::int32>& gnodeb_category);
CheckMeasurementStatusResponse check_measurement_status(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
ClearAllNamedResultsResponse clear_all_named_results(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
ClearNamedResultResponse clear_named_result(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
ClearNoiseCalibrationDatabaseResponse clear_noise_calibration_database(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
CloneSignalConfigurationResponse clone_signal_configuration(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& old_signal_name, const std::string& new_signal_name);
CloseResponse close(const StubPtr& stub, const nidevice_grpc::Session& instrument, const bool& force_destroy);
CommitResponse commit(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
CreateListResponse create_list(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& list_name);
CreateListStepResponse create_list_step(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
CreateSignalConfigurationResponse create_signal_configuration(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& signal_name);
DeleteListResponse delete_list(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& list_name);
DeleteSignalConfigurationResponse delete_signal_configuration(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& signal_name);
DisableTriggerResponse disable_trigger(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
GetAllNamedResultNamesResponse get_all_named_result_names(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
GetAttributeF32Response get_attribute_f32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeF32ArrayResponse get_attribute_f32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeF64Response get_attribute_f64(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeF64ArrayResponse get_attribute_f64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeI16Response get_attribute_i16(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeI32Response get_attribute_i32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeI32ArrayResponse get_attribute_i32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeI64Response get_attribute_i64(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeI64ArrayResponse get_attribute_i64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeI8Response get_attribute_i8(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeI8ArrayResponse get_attribute_i8_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeNIComplexDoubleArrayResponse get_attribute_ni_complex_double_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeNIComplexSingleArrayResponse get_attribute_ni_complex_single_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeStringResponse get_attribute_string(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeU16Response get_attribute_u16(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeU32Response get_attribute_u32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeU32ArrayResponse get_attribute_u32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeU64ArrayResponse get_attribute_u64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeU8Response get_attribute_u8(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetAttributeU8ArrayResponse get_attribute_u8_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
GetErrorResponse get_error(const StubPtr& stub, const nidevice_grpc::Session& instrument);
GetErrorStringResponse get_error_string(const StubPtr& stub, const nidevice_grpc::Session& instrument, const pb::int32& error_code);
InitializeResponse initialize(const StubPtr& stub, const std::string& resource_name, const std::string& option_string, const nidevice_grpc::SessionInitializationBehavior& initialization_behavior = nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_UNSPECIFIED);
InitializeFromNIRFSASessionResponse initialize_from_nirfsa_session(const StubPtr& stub, const nidevice_grpc::Session& nirfsa_session, const nidevice_grpc::SessionInitializationBehavior& initialization_behavior = nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_UNSPECIFIED);
InitiateResponse initiate(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name);
LoadFromGenerationConfigurationFileResponse load_from_generation_configuration_file(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& file_path, const pb::int32& configuration_index);
ModAccAutoLevelResponse mod_acc_auto_level(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccCfgMeasurementModeResponse mod_acc_cfg_measurement_mode(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ModAccMeasurementMode, pb::int32>& measurement_mode);
ModAccCfgNoiseCompensationEnabledResponse mod_acc_cfg_noise_compensation_enabled(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ModAccNoiseCompensationEnabled, pb::int32>& noise_compensation_enabled);
ModAccCfgReferenceWaveformResponse mod_acc_cfg_reference_waveform(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& x0, const double& dx, const std::vector<nidevice_grpc::NIComplexNumberF32>& reference_waveform);
ModAccCfgReferenceWaveformInterleavedIQResponse mod_acc_cfg_reference_waveform_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& x0, const double& dx, const std::vector<float>& reference_waveform);
ModAccCfgReferenceWaveformSplitResponse mod_acc_cfg_reference_waveform_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& x0, const double& dx, const std::vector<float>& reference_waveform_i, const std::vector<float>& reference_waveform_q);
ModAccClearNoiseCalibrationDatabaseResponse mod_acc_clear_noise_calibration_database(const StubPtr& stub, const nidevice_grpc::Session& instrument);
ModAccFetchCompositeEVMResponse mod_acc_fetch_composite_evm(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchFrequencyErrorMeanResponse mod_acc_fetch_frequency_error_mean(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchFrequencyErrorPerSlotMaximumTraceResponse mod_acc_fetch_frequency_error_per_slot_maximum_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchIQGainImbalancePerSubcarrierMeanTraceResponse mod_acc_fetch_iq_gain_imbalance_per_subcarrier_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchIQQuadratureErrorPerSubcarrierMeanTraceResponse mod_acc_fetch_iq_quadrature_error_per_subcarrier_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchInBandEmissionTraceResponse mod_acc_fetch_in_band_emission_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPBCHDMRSConstellationTraceResponse mod_acc_fetch_pbchdmrs_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPBCHDMRSConstellationTraceInterleavedIQResponse mod_acc_fetch_pbchdmrs_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPBCHDMRSConstellationTraceSplitResponse mod_acc_fetch_pbchdmrs_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTraceResponse mod_acc_fetch_pbchdmrsrmsevm_per_subcarrier_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTraceResponse mod_acc_fetch_pbchdmrsrmsevm_per_symbol_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPBCHDataConstellationTraceResponse mod_acc_fetch_pbch_data_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPBCHDataConstellationTraceInterleavedIQResponse mod_acc_fetch_pbch_data_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPBCHDataConstellationTraceSplitResponse mod_acc_fetch_pbch_data_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTraceResponse mod_acc_fetch_pbch_data_rmsevm_per_subcarrier_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPBCHDataRMSEVMPerSymbolMeanTraceResponse mod_acc_fetch_pbch_data_rmsevm_per_symbol_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH1024QAMConstellationTraceResponse mod_acc_fetch_pdsch1024q_am_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQResponse mod_acc_fetch_pdsch1024q_am_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH1024QAMConstellationTraceSplitResponse mod_acc_fetch_pdsch1024q_am_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH16QAMConstellationTraceResponse mod_acc_fetch_pdsch16q_am_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQResponse mod_acc_fetch_pdsch16q_am_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH16QAMConstellationTraceSplitResponse mod_acc_fetch_pdsch16q_am_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH256QAMConstellationTraceResponse mod_acc_fetch_pdsch256q_am_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQResponse mod_acc_fetch_pdsch256q_am_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH256QAMConstellationTraceSplitResponse mod_acc_fetch_pdsch256q_am_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH4096QAMConstellationTraceResponse mod_acc_fetch_pdsch4096q_am_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQResponse mod_acc_fetch_pdsch4096q_am_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH4096QAMConstellationTraceSplitResponse mod_acc_fetch_pdsch4096q_am_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH64QAMConstellationTraceResponse mod_acc_fetch_pdsch64q_am_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQResponse mod_acc_fetch_pdsch64q_am_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH64QAMConstellationTraceSplitResponse mod_acc_fetch_pdsch64q_am_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH8PSKConstellationTraceResponse mod_acc_fetch_pdsch8p_sk_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQResponse mod_acc_fetch_pdsch8p_sk_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCH8PSKConstellationTraceSplitResponse mod_acc_fetch_pdsch8p_sk_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCHDMRSConstellationTraceResponse mod_acc_fetch_pdschdmrs_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQResponse mod_acc_fetch_pdschdmrs_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCHDMRSConstellationTraceSplitResponse mod_acc_fetch_pdschdmrs_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCHDataConstellationTraceResponse mod_acc_fetch_pdsch_data_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCHDataConstellationTraceInterleavedIQResponse mod_acc_fetch_pdsch_data_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCHDataConstellationTraceSplitResponse mod_acc_fetch_pdsch_data_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCHDemodulatedBitsResponse mod_acc_fetch_pdsch_demodulated_bits(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCHPTRSConstellationTraceResponse mod_acc_fetch_pdschptrs_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQResponse mod_acc_fetch_pdschptrs_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCHPTRSConstellationTraceSplitResponse mod_acc_fetch_pdschptrs_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCHQPSKConstellationTraceResponse mod_acc_fetch_pdschqpsk_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQResponse mod_acc_fetch_pdschqpsk_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPDSCHQPSKConstellationTraceSplitResponse mod_acc_fetch_pdschqpsk_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPSSConstellationTraceResponse mod_acc_fetch_pss_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPSSConstellationTraceInterleavedIQResponse mod_acc_fetch_pss_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPSSConstellationTraceSplitResponse mod_acc_fetch_pss_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPSSRMSEVMPerSubcarrierMeanTraceResponse mod_acc_fetch_pssrmsevm_per_subcarrier_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPSSRMSEVMPerSymbolMeanTraceResponse mod_acc_fetch_pssrmsevm_per_symbol_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPUSCHDMRSConstellationTraceResponse mod_acc_fetch_puschdmrs_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQResponse mod_acc_fetch_puschdmrs_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPUSCHDMRSConstellationTraceSplitResponse mod_acc_fetch_puschdmrs_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPUSCHDataConstellationTraceResponse mod_acc_fetch_pusch_data_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPUSCHDataConstellationTraceInterleavedIQResponse mod_acc_fetch_pusch_data_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPUSCHDataConstellationTraceSplitResponse mod_acc_fetch_pusch_data_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPUSCHDemodulatedBitsResponse mod_acc_fetch_pusch_demodulated_bits(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPUSCHPTRSConstellationTraceResponse mod_acc_fetch_puschptrs_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQResponse mod_acc_fetch_puschptrs_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPUSCHPTRSConstellationTraceSplitResponse mod_acc_fetch_puschptrs_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPUSCHPhaseOffsetTraceResponse mod_acc_fetch_pusch_phase_offset_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPeakEVMHighPerSymbolMaximumTraceResponse mod_acc_fetch_peak_evm_high_per_symbol_maximum_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPeakEVMLowPerSymbolMaximumTraceResponse mod_acc_fetch_peak_evm_low_per_symbol_maximum_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPeakEVMPerSlotMaximumTraceResponse mod_acc_fetch_peak_evm_per_slot_maximum_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPeakEVMPerSubcarrierMaximumTraceResponse mod_acc_fetch_peak_evm_per_subcarrier_maximum_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPeakEVMPerSymbolMaximumTraceResponse mod_acc_fetch_peak_evm_per_symbol_maximum_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchRMSEVMHighPerSymbolMeanTraceResponse mod_acc_fetch_rmsevm_high_per_symbol_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchRMSEVMLowPerSymbolMeanTraceResponse mod_acc_fetch_rmsevm_low_per_symbol_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchRMSEVMPerSlotMeanTraceResponse mod_acc_fetch_rmsevm_per_slot_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchRMSEVMPerSubcarrierMeanTraceResponse mod_acc_fetch_rmsevm_per_subcarrier_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchRMSEVMPerSymbolMeanTraceResponse mod_acc_fetch_rmsevm_per_symbol_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchSSSConstellationTraceResponse mod_acc_fetch_sss_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchSSSConstellationTraceInterleavedIQResponse mod_acc_fetch_sss_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchSSSConstellationTraceSplitResponse mod_acc_fetch_sss_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchSSSRMSEVMPerSubcarrierMeanTraceResponse mod_acc_fetch_sssrmsevm_per_subcarrier_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchSSSRMSEVMPerSymbolMeanTraceResponse mod_acc_fetch_sssrmsevm_per_symbol_mean_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchSpectralFlatnessTraceResponse mod_acc_fetch_spectral_flatness_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchSubblockInBandEmissionTraceResponse mod_acc_fetch_subblock_in_band_emission_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchTransientPeriodLocationsTraceResponse mod_acc_fetch_transient_period_locations_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccValidateCalibrationDataResponse mod_acc_validate_calibration_data(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
OBWCfgAveragingResponse obw_cfg_averaging(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ObwAveragingEnabled, pb::int32>& averaging_enabled, const pb::int32& averaging_count, const simple_variant<ObwAveragingType, pb::int32>& averaging_type);
OBWCfgRBWFilterResponse obw_cfg_rbw_filter(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ObwRbwAutoBandwidth, pb::int32>& rbw_auto, const double& rbw, const simple_variant<ObwRbwFilterType, pb::int32>& rbw_filter_type);
OBWCfgSweepTimeResponse obw_cfg_sweep_time(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ObwSweepTimeAuto, pb::int32>& sweep_time_auto, const double& sweep_time_interval);
OBWFetchMeasurementResponse obw_fetch_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
OBWFetchSpectrumResponse obw_fetch_spectrum(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
PVTCfgAveragingResponse pvt_cfg_averaging(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<PvtAveragingEnabled, pb::int32>& averaging_enabled, const pb::int32& averaging_count, const simple_variant<PvtAveragingType, pb::int32>& averaging_type);
PVTCfgMeasurementMethodResponse pvt_cfg_measurement_method(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<PvtMeasurementMethod, pb::int32>& measurement_method);
PVTCfgOFFPowerExclusionPeriodsResponse pvt_cfg_off_power_exclusion_periods(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& off_power_exclusion_before, const double& off_power_exclusion_after);
PVTFetchMeasurementResponse pvt_fetch_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
PVTFetchMeasurementArrayResponse pvt_fetch_measurement_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
PVTFetchSignalPowerTraceResponse pvt_fetch_signal_power_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
PVTFetchWindowedSignalPowerTraceResponse pvt_fetch_windowed_signal_power_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ResetAttributeResponse reset_attribute(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id);
ResetToDefaultResponse reset_to_default(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
SEMCfgAveragingResponse sem_cfg_averaging(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<SemAveragingEnabled, pb::int32>& averaging_enabled, const pb::int32& averaging_count, const simple_variant<SemAveragingType, pb::int32>& averaging_type);
SEMCfgComponentCarrierRatedOutputPowerResponse sem_cfg_component_carrier_rated_output_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& component_carrier_rated_output_power);
SEMCfgComponentCarrierRatedOutputPowerArrayResponse sem_cfg_component_carrier_rated_output_power_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::vector<double>& component_carrier_rated_output_power);
SEMCfgNumberOfOffsetsResponse sem_cfg_number_of_offsets(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& number_of_offsets);
SEMCfgOffsetAbsoluteLimitResponse sem_cfg_offset_absolute_limit(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& absolute_limit_start, const double& absolute_limit_stop);
SEMCfgOffsetAbsoluteLimitArrayResponse sem_cfg_offset_absolute_limit_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::vector<double>& absolute_limit_start, const std::vector<double>& absolute_limit_stop);
SEMCfgOffsetBandwidthIntegralResponse sem_cfg_offset_bandwidth_integral(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& bandwidth_integral);
SEMCfgOffsetBandwidthIntegralArrayResponse sem_cfg_offset_bandwidth_integral_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::vector<pb::int32>& bandwidth_integral);
SEMCfgOffsetFrequencyResponse sem_cfg_offset_frequency(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& offset_start_frequency, const double& offset_stop_frequency, const simple_variant<SemOffsetSideband, pb::int32>& offset_sideband);
SEMCfgOffsetFrequencyArrayResponse sem_cfg_offset_frequency_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::vector<double>& offset_start_frequency, const std::vector<double>& offset_stop_frequency, const std::vector<pb::int32>& offset_sideband);
SEMCfgOffsetLimitFailMaskResponse sem_cfg_offset_limit_fail_mask(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<SemOffsetLimitFailMask, pb::int32>& limit_fail_mask);
SEMCfgOffsetLimitFailMaskArrayResponse sem_cfg_offset_limit_fail_mask_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::vector<pb::int32>& limit_fail_mask);
SEMCfgOffsetRBWFilterResponse sem_cfg_offset_rbw_filter(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& offset_rbw, const simple_variant<SemOffsetRbwFilterType, pb::int32>& offset_rbw_filter_type);
SEMCfgOffsetRBWFilterArrayResponse sem_cfg_offset_rbw_filter_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::vector<double>& offset_rbw, const std::vector<pb::int32>& offset_rbw_filter_type);
SEMCfgOffsetRelativeLimitResponse sem_cfg_offset_relative_limit(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& relative_limit_start, const double& relative_limit_stop);
SEMCfgOffsetRelativeLimitArrayResponse sem_cfg_offset_relative_limit_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::vector<double>& relative_limit_start, const std::vector<double>& relative_limit_stop);
SEMCfgSweepTimeResponse sem_cfg_sweep_time(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<SemSweepTimeAuto, pb::int32>& sweep_time_auto, const double& sweep_time_interval);
SEMCfgUplinkMaskTypeResponse sem_cfg_uplink_mask_type(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<SemUplinkMaskType, pb::int32>& uplink_mask_type);
SEMFetchComponentCarrierMeasurementResponse sem_fetch_component_carrier_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchComponentCarrierMeasurementArrayResponse sem_fetch_component_carrier_measurement_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchLowerOffsetMarginResponse sem_fetch_lower_offset_margin(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchLowerOffsetMarginArrayResponse sem_fetch_lower_offset_margin_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchLowerOffsetPowerResponse sem_fetch_lower_offset_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchLowerOffsetPowerArrayResponse sem_fetch_lower_offset_power_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchMeasurementStatusResponse sem_fetch_measurement_status(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchSpectrumResponse sem_fetch_spectrum(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchSubblockMeasurementResponse sem_fetch_subblock_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchTotalAggregatedPowerResponse sem_fetch_total_aggregated_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchUpperOffsetMarginResponse sem_fetch_upper_offset_margin(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchUpperOffsetMarginArrayResponse sem_fetch_upper_offset_margin_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchUpperOffsetPowerResponse sem_fetch_upper_offset_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchUpperOffsetPowerArrayResponse sem_fetch_upper_offset_power_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SelectMeasurementsResponse select_measurements(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<MeasurementTypes, pb::uint32>& measurements, const bool& enable_all_traces);
SendSoftwareEdgeTriggerResponse send_software_edge_trigger(const StubPtr& stub, const nidevice_grpc::Session& instrument);
SetAttributeF32Response set_attribute_f32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const float& attr_val);
SetAttributeF32ArrayResponse set_attribute_f32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<float>& attr_val);
SetAttributeF64Response set_attribute_f64(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const double& attr_val);
SetAttributeF64ArrayResponse set_attribute_f64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<double>& attr_val);
SetAttributeI16Response set_attribute_i16(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const pb::int32& attr_val);
SetAttributeI32Response set_attribute_i32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const simple_variant<NiRFmxNRInt32AttributeValues, pb::int32>& attr_val);
SetAttributeI32ArrayResponse set_attribute_i32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<pb::int32>& attr_val);
SetAttributeI64Response set_attribute_i64(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const pb::int64& attr_val);
SetAttributeI64ArrayResponse set_attribute_i64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<pb::int64>& attr_val);
SetAttributeI8Response set_attribute_i8(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const pb::int32& attr_val);
SetAttributeI8ArrayResponse set_attribute_i8_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<pb::int32>& attr_val);
SetAttributeNIComplexDoubleArrayResponse set_attribute_ni_complex_double_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<nidevice_grpc::NIComplexNumber>& attr_val);
SetAttributeNIComplexSingleArrayResponse set_attribute_ni_complex_single_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<nidevice_grpc::NIComplexNumberF32>& attr_val);
SetAttributeStringResponse set_attribute_string(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const simple_variant<NiRFmxNRStringAttributeValuesMapped, std::string>& attr_val);
SetAttributeU16Response set_attribute_u16(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const pb::uint32& attr_val);
SetAttributeU32Response set_attribute_u32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const pb::uint32& attr_val);
SetAttributeU32ArrayResponse set_attribute_u32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<pb::uint32>& attr_val);
SetAttributeU64ArrayResponse set_attribute_u64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::vector<pb::uint64>& attr_val);
SetAttributeU8Response set_attribute_u8(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const pb::uint32& attr_val);
SetAttributeU8ArrayResponse set_attribute_u8_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxNRAttribute& attribute_id, const std::string& attr_val);
TXPFetchMeasurementResponse txp_fetch_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
TXPFetchPowerTraceResponse txp_fetch_power_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
WaitForAcquisitionCompleteResponse wait_for_acquisition_complete(const StubPtr& stub, const nidevice_grpc::Session& instrument, const double& timeout);
WaitForMeasurementCompleteResponse wait_for_measurement_complete(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);

} // namespace nirfmxnr_grpc::experimental::client

#endif /* NIRFMXNR_GRPC_CLIENT_H */
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/nirfmxnr/nirfmxnr_compilation_test.cpp sha256=c5959001a8ab7bd458a2a82ff43f32b49f0bcf7a07528031727235ee7ca2ff92 bytes=83008 -->
## FILE: generated/nirfmxnr/nirfmxnr_compilation_test.cpp

- repository: `ni/grpc-device`
- source_path: `generated/nirfmxnr/nirfmxnr_compilation_test.cpp`
- sha256: `c5959001a8ab7bd458a2a82ff43f32b49f0bcf7a07528031727235ee7ca2ff92`
- bytes: 83008

````cpp
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Compilation test for the NI-RFMXNR Metadata
//---------------------------------------------------------------------
#include "nirfmxnr_library.h"

namespace nirfmxnr_grpc {

int32 ACPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  return RFmxNR_ACPCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 ACPCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)
{
  return RFmxNR_ACPCfgMeasurementMethod(instrumentHandle, selectorString, measurementMethod);
}

int32 ACPCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled)
{
  return RFmxNR_ACPCfgNoiseCompensationEnabled(instrumentHandle, selectorString, noiseCompensationEnabled);
}

int32 ACPCfgNumberOfENDCOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfENDCOffsets)
{
  return RFmxNR_ACPCfgNumberOfENDCOffsets(instrumentHandle, selectorString, numberOfENDCOffsets);
}

int32 ACPCfgNumberOfEUTRAOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfEUTRAOffsets)
{
  return RFmxNR_ACPCfgNumberOfEUTRAOffsets(instrumentHandle, selectorString, numberOfEUTRAOffsets);
}

int32 ACPCfgNumberOfNROffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfNROffsets)
{
  return RFmxNR_ACPCfgNumberOfNROffsets(instrumentHandle, selectorString, numberOfNROffsets);
}

int32 ACPCfgNumberOfUTRAOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfUTRAOffsets)
{
  return RFmxNR_ACPCfgNumberOfUTRAOffsets(instrumentHandle, selectorString, numberOfUTRAOffsets);
}

int32 ACPCfgPowerUnits(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnits)
{
  return RFmxNR_ACPCfgPowerUnits(instrumentHandle, selectorString, powerUnits);
}

int32 ACPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)
{
  return RFmxNR_ACPCfgRBWFilter(instrumentHandle, selectorString, rbwAuto, rbw, rbwFilterType);
}

int32 ACPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)
{
  return RFmxNR_ACPCfgSweepTime(instrumentHandle, selectorString, sweepTimeAuto, sweepTimeInterval);
}

int32 ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 absolutePowersTrace[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ACPFetchAbsolutePowersTrace(instrumentHandle, selectorString, timeout, traceIndex, x0, dx, absolutePowersTrace, arraySize, actualArraySize);
}

int32 ACPFetchComponentCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absolutePower, float64* relativePower)
{
  return RFmxNR_ACPFetchComponentCarrierMeasurement(instrumentHandle, selectorString, timeout, absolutePower, relativePower);
}

int32 ACPFetchComponentCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 relativePower[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ACPFetchComponentCarrierMeasurementArray(instrumentHandle, selectorString, timeout, absolutePower, relativePower, arraySize, actualArraySize);
}

int32 ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* lowerRelativePower, float64* upperRelativePower, float64* lowerAbsolutePower, float64* upperAbsolutePower)
{
  return RFmxNR_ACPFetchOffsetMeasurement(instrumentHandle, selectorString, timeout, lowerRelativePower, upperRelativePower, lowerAbsolutePower, upperAbsolutePower);
}

int32 ACPFetchOffsetMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 lowerRelativePower[], float64 upperRelativePower[], float64 lowerAbsolutePower[], float64 upperAbsolutePower[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ACPFetchOffsetMeasurementArray(instrumentHandle, selectorString, timeout, lowerRelativePower, upperRelativePower, lowerAbsolutePower, upperAbsolutePower, arraySize, actualArraySize);
}

int32 ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 relativePowersTrace[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ACPFetchRelativePowersTrace(instrumentHandle, selectorString, timeout, traceIndex, x0, dx, relativePowersTrace, arraySize, actualArraySize);
}

int32 ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ACPFetchSpectrum(instrumentHandle, selectorString, timeout, x0, dx, spectrum, arraySize, actualArraySize);
}

int32 ACPFetchSubblockMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* subblockPower, float64* integrationBandwidth, float64* frequency)
{
  return RFmxNR_ACPFetchSubblockMeasurement(instrumentHandle, selectorString, timeout, subblockPower, integrationBandwidth, frequency);
}

int32 ACPFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAggregatedPower)
{
  return RFmxNR_ACPFetchTotalAggregatedPower(instrumentHandle, selectorString, timeout, totalAggregatedPower);
}

int32 ACPValidateNoiseCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* noiseCalibrationDataValid)
{
  return RFmxNR_ACPValidateNoiseCalibrationData(instrumentHandle, selectorString, noiseCalibrationDataValid);
}

int32 AbortMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  return RFmxNR_AbortMeasurements(instrumentHandle, selectorString);
}

int32 AnalyzeIQ1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved)
{
  return RFmxNR_AnalyzeIQ1Waveform(instrumentHandle, selectorString, resultName, x0, dx, iq, arraySize, reset, reserved);
}

int32 AnalyzeIQ1WaveformInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iq[], int32 arraySize, int32 reset, int64 reserved)
{
  return RFmxNR_AnalyzeIQ1Waveform(instrumentHandle, selectorString, resultName, x0, dx, reinterpret_cast<NIComplexSingle*>(iq), arraySize/2, reset, reserved);
}

int32 AnalyzeIQ1WaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iqi[], float32 iqq[], int32 arraySize, int32 reset, int64 reserved)
{
  return RFmxNR_AnalyzeIQ1WaveformSplit(instrumentHandle, selectorString, resultName, x0, dx, iqi, iqq, arraySize, reset, reserved);
}

int32 AnalyzeNWaveformsIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], NIComplexSingle iq[], int32 iqSize[], int32 arraySize, int32 reset)
{
  return RFmxNR_AnalyzeNWaveformsIQ(instrumentHandle, selectorString, resultName, x0, dx, iq, iqSize, arraySize, reset);
}

int32 AnalyzeNWaveformsIQInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], float32 iq[], int32 iqSize[], int32 arraySize, int32 reset)
{
  return RFmxNR_AnalyzeNWaveformsIQ(instrumentHandle, selectorString, resultName, x0, dx, reinterpret_cast<NIComplexSingle*>(iq), iqSize, arraySize/2, reset);
}

int32 AnalyzeNWaveformsIQSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], float32 iqi[], float32 iqq[], int32 iqSize[], int32 arraySize, int32 reset)
{
  return RFmxNR_AnalyzeNWaveformsIQSplit(instrumentHandle, selectorString, resultName, x0, dx, iqi, iqq, iqSize, arraySize, reset);
}

int32 AnalyzeNWaveformsSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], float32 spectrum[], int32 spectrumSize[], int32 arraySize, int32 reset)
{
  return RFmxNR_AnalyzeNWaveformsSpectrum(instrumentHandle, selectorString, resultName, x0, dx, spectrum, spectrumSize, arraySize, reset);
}

int32 AnalyzeSpectrum1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 spectrum[], int32 arraySize, int32 reset, int64 reserved)
{
  return RFmxNR_AnalyzeSpectrum1Waveform(instrumentHandle, selectorString, resultName, x0, dx, spectrum, arraySize, reset, reserved);
}

int32 AutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval, float64* referenceLevel)
{
  return RFmxNR_AutoLevel(instrumentHandle, selectorString, measurementInterval, referenceLevel);
}

int32 BuildBandwidthPartString(char selectorString[], int32 bandwidthPartNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  return RFmxNR_BuildBandwidthPartString(selectorString, bandwidthPartNumber, selectorStringOutLength, selectorStringOut);
}

int32 BuildCORESETClusterString(char selectorString[], int32 coresetClusterNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  return RFmxNR_BuildCORESETClusterString(selectorString, coresetClusterNumber, selectorStringOutLength, selectorStringOut);
}

int32 BuildCORESETString(char selectorString[], int32 coresetNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  return RFmxNR_BuildCORESETString(selectorString, coresetNumber, selectorStringOutLength, selectorStringOut);
}

int32 BuildCarrierString(char selectorString[], int32 carrierNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  return RFmxNR_BuildCarrierString(selectorString, carrierNumber, selectorStringOutLength, selectorStringOut);
}

int32 BuildListStepString(char listName[], char resultName[], int32 stepNumber, int32 selectorStringLength, char selectorString[])
{
  return RFmxNR_BuildListStepString(listName, resultName, stepNumber, selectorStringLength, selectorString);
}

int32 BuildListString(char listName[], char resultName[], int32 selectorStringLength, char selectorString[])
{
  return RFmxNR_BuildListString(listName, resultName, selectorStringLength, selectorString);
}

int32 BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  return RFmxNR_BuildOffsetString(selectorString, offsetNumber, selectorStringOutLength, selectorStringOut);
}

int32 BuildPDCCHString(char selectorString[], int32 pdcchNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  return RFmxNR_BuildPDCCHString(selectorString, pdcchNumber, selectorStringOutLength, selectorStringOut);
}

int32 BuildPDSCHClusterString(char selectorString[], int32 pdschClusterNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  return RFmxNR_BuildPDSCHClusterString(selectorString, pdschClusterNumber, selectorStringOutLength, selectorStringOut);
}

int32 BuildPDSCHString(char selectorString[], int32 pdschNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  return RFmxNR_BuildPDSCHString(selectorString, pdschNumber, selectorStringOutLength, selectorStringOut);
}

int32 BuildPUSCHClusterString(char selectorString[], int32 puschClusterNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  return RFmxNR_BuildPUSCHClusterString(selectorString, puschClusterNumber, selectorStringOutLength, selectorStringOut);
}

int32 BuildPUSCHString(char selectorString[], int32 puschNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  return RFmxNR_BuildPUSCHString(selectorString, puschNumber, selectorStringOutLength, selectorStringOut);
}

int32 BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])
{
  return RFmxNR_BuildSignalString(signalName, resultName, selectorStringLength, selectorString);
}

int32 BuildSubblockString(char selectorString[], int32 subblockNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  return RFmxNR_BuildSubblockString(selectorString, subblockNumber, selectorStringOutLength, selectorStringOut);
}

int32 BuildUserString(char selectorString[], int32 userNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  return RFmxNR_BuildUserString(selectorString, userNumber, selectorStringOutLength, selectorStringOut);
}

int32 CHPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  return RFmxNR_CHPCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 CHPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)
{
  return RFmxNR_CHPCfgRBWFilter(instrumentHandle, selectorString, rbwAuto, rbw, rbwFilterType);
}

int32 CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)
{
  return RFmxNR_CHPCfgSweepTime(instrumentHandle, selectorString, sweepTimeAuto, sweepTimeInterval);
}

int32 CHPFetchComponentCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absolutePower, float64* relativePower)
{
  return RFmxNR_CHPFetchComponentCarrierMeasurement(instrumentHandle, selectorString, timeout, absolutePower, relativePower);
}

int32 CHPFetchComponentCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 relativePower[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_CHPFetchComponentCarrierMeasurementArray(instrumentHandle, selectorString, timeout, absolutePower, relativePower, arraySize, actualArraySize);
}

int32 CHPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_CHPFetchSpectrum(instrumentHandle, selectorString, timeout, x0, dx, spectrum, arraySize, actualArraySize);
}

int32 CHPFetchSubblockPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* subblockPower)
{
  return RFmxNR_CHPFetchSubblockPower(instrumentHandle, selectorString, timeout, subblockPower);
}

int32 CHPFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAggregatedPower)
{
  return RFmxNR_CHPFetchTotalAggregatedPower(instrumentHandle, selectorString, timeout, totalAggregatedPower);
}

int32 CHPValidateNoiseCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* noiseCalibrationDataValid)
{
  return RFmxNR_CHPValidateNoiseCalibrationData(instrumentHandle, selectorString, noiseCalibrationDataValid);
}

int32 CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger)
{
  return RFmxNR_CfgDigitalEdgeTrigger(instrumentHandle, selectorString, digitalEdgeSource, digitalEdge, triggerDelay, enableTrigger);
}

int32 CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation)
{
  return RFmxNR_CfgExternalAttenuation(instrumentHandle, selectorString, externalAttenuation);
}

int32 CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)
{
  return RFmxNR_CfgFrequency(instrumentHandle, selectorString, centerFrequency);
}

int32 CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)
{
  return RFmxNR_CfgFrequencyReference(instrumentHandle, channelName, frequencyReferenceSource, frequencyReferenceFrequency);
}

int32 CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdgeSlope, float64 iqPowerEdgeLevel, float64 triggerDelay, int32 triggerMinQuietTimeMode, float64 triggerMinQuietTimeDuration, int32 iqPowerEdgeLevelType, int32 enableTrigger)
{
  return RFmxNR_CfgIQPowerEdgeTrigger(instrumentHandle, selectorString, iqPowerEdgeSource, iqPowerEdgeSlope, iqPowerEdgeLevel, triggerDelay, triggerMinQuietTimeMode, triggerMinQuietTimeDuration, iqPowerEdgeLevelType, enableTrigger);
}

int32 CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)
{
  return RFmxNR_CfgMechanicalAttenuation(instrumentHandle, channelName, mechanicalAttenuationAuto, mechanicalAttenuationValue);
}

int32 CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation)
{
  return RFmxNR_CfgRF(instrumentHandle, selectorString, centerFrequency, referenceLevel, externalAttenuation);
}

int32 CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue)
{
  return RFmxNR_CfgRFAttenuation(instrumentHandle, channelName, rfAttenuationAuto, rfAttenuationValue);
}

int32 CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel)
{
  return RFmxNR_CfgReferenceLevel(instrumentHandle, selectorString, referenceLevel);
}

int32 CfgSelectedPortsMultiple(niRFmxInstrHandle instrumentHandle, char selectorString[], char selectedPorts[])
{
  return RFmxNR_CfgSelectedPortsMultiple(instrumentHandle, selectorString, selectedPorts);
}

int32 CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)
{
  return RFmxNR_CfgSoftwareEdgeTrigger(instrumentHandle, selectorString, triggerDelay, enableTrigger);
}

int32 CfggNodeBCategory(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 gNodeBCategory)
{
  return RFmxNR_CfggNodeBCategory(instrumentHandle, selectorString, gNodeBCategory);
}

int32 CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* isDone)
{
  return RFmxNR_CheckMeasurementStatus(instrumentHandle, selectorString, isDone);
}

int32 ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  return RFmxNR_ClearAllNamedResults(instrumentHandle, selectorString);
}

int32 ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  return RFmxNR_ClearNamedResult(instrumentHandle, selectorString);
}

int32 ClearNoiseCalibrationDatabase(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  return RFmxNR_ClearNoiseCalibrationDatabase(instrumentHandle, selectorString);
}

int32 CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[])
{
  return RFmxNR_CloneSignalConfiguration(instrumentHandle, oldSignalName, newSignalName);
}

int32 Close(niRFmxInstrHandle instrumentHandle, int32 forceDestroy)
{
  return RFmxNR_Close(instrumentHandle, forceDestroy);
}

int32 Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  return RFmxNR_Commit(instrumentHandle, selectorString);
}

int32 CreateList(niRFmxInstrHandle instrumentHandle, char listName[])
{
  return RFmxNR_CreateList(instrumentHandle, listName);
}

int32 CreateListStep(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* createdStepIndex)
{
  return RFmxNR_CreateListStep(instrumentHandle, selectorString, createdStepIndex);
}

int32 CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])
{
  return RFmxNR_CreateSignalConfiguration(instrumentHandle, signalName);
}

int32 DeleteList(niRFmxInstrHandle instrumentHandle, char listName[])
{
  return RFmxNR_DeleteList(instrumentHandle, listName);
}

int32 DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])
{
  return RFmxNR_DeleteSignalConfiguration(instrumentHandle, signalName);
}

int32 DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  return RFmxNR_DisableTrigger(instrumentHandle, selectorString);
}

int32 GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32* actualResultNamesSize, int32* defaultResultExists)
{
  return RFmxNR_GetAllNamedResultNames(instrumentHandle, selectorString, resultNames, resultNamesBufferSize, actualResultNamesSize, defaultResultExists);
}

int32 GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32* attrVal)
{
  return RFmxNR_GetAttributeF32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_GetAttributeF32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64* attrVal)
{
  return RFmxNR_GetAttributeF64(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_GetAttributeF64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int16* attrVal)
{
  return RFmxNR_GetAttributeI16(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32* attrVal)
{
  return RFmxNR_GetAttributeI32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_GetAttributeI32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64* attrVal)
{
  return RFmxNR_GetAttributeI64(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_GetAttributeI64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8* attrVal)
{
  return RFmxNR_GetAttributeI8(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_GetAttributeI8Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexDouble attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_GetAttributeNIComplexDoubleArray(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexSingle attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_GetAttributeNIComplexSingleArray(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 arraySize, char attrVal[])
{
  return RFmxNR_GetAttributeString(instrumentHandle, selectorString, attributeID, arraySize, attrVal);
}

int32 GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt16* attrVal)
{
  return RFmxNR_GetAttributeU16(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32* attrVal)
{
  return RFmxNR_GetAttributeU32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_GetAttributeU32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt64 attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_GetAttributeU64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8* attrVal)
{
  return RFmxNR_GetAttributeU8(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_GetAttributeU8Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetError(niRFmxInstrHandle instrumentHandle, int32* errorCode, int32 errorDescriptionBufferSize, char errorDescription[])
{
  return RFmxNR_GetError(instrumentHandle, errorCode, errorDescriptionBufferSize, errorDescription);
}

int32 GetErrorString(niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[])
{
  return RFmxNR_GetErrorString(instrumentHandle, errorCode, errorDescriptionBufferSize, errorDescription);
}

int32 Initialize(char resourceName[], char optionString[], niRFmxInstrHandle* handleOut, int32* isNewSession)
{
  return RFmxNR_Initialize(resourceName, optionString, handleOut, isNewSession);
}

int32 InitializeFromNIRFSASession(uInt32 nirfsaSession, niRFmxInstrHandle* handleOut)
{
  return RFmxNR_InitializeFromNIRFSASession(nirfsaSession, handleOut);
}

int32 Initiate(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[])
{
  return RFmxNR_Initiate(instrumentHandle, selectorString, resultName);
}

int32 LoadFromGenerationConfigurationFile(niRFmxInstrHandle instrumentHandle, char selectorString[], char filePath[], int32 configurationIndex)
{
  return RFmxNR_LoadFromGenerationConfigurationFile(instrumentHandle, selectorString, filePath, configurationIndex);
}

int32 ModAccAutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)
{
  return RFmxNR_ModAccAutoLevel(instrumentHandle, selectorString, timeout);
}

int32 ModAccCfgMeasurementMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMode)
{
  return RFmxNR_ModAccCfgMeasurementMode(instrumentHandle, selectorString, measurementMode);
}

int32 ModAccCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled)
{
  return RFmxNR_ModAccCfgNoiseCompensationEnabled(instrumentHandle, selectorString, noiseCompensationEnabled);
}

int32 ModAccCfgReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, NIComplexSingle referenceWaveform[], int32 arraySize)
{
  return RFmxNR_ModAccCfgReferenceWaveform(instrumentHandle, selectorString, x0, dx, referenceWaveform, arraySize);
}

int32 ModAccCfgReferenceWaveformInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 referenceWaveform[], int32 arraySize)
{
  return RFmxNR_ModAccCfgReferenceWaveform(instrumentHandle, selectorString, x0, dx, reinterpret_cast<NIComplexSingle*>(referenceWaveform), arraySize/2);
}

int32 ModAccCfgReferenceWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 referenceWaveformI[], float32 referenceWaveformQ[], int32 arraySize)
{
  return RFmxNR_ModAccCfgReferenceWaveformSplit(instrumentHandle, selectorString, x0, dx, referenceWaveformI, referenceWaveformQ, arraySize);
}

int32 ModAccClearNoiseCalibrationDatabase(niRFmxInstrHandle instrumentHandle)
{
  return RFmxNR_ModAccClearNoiseCalibrationDatabase(instrumentHandle);
}

int32 ModAccFetchCompositeEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* compositeRMSEVMMean, float64* compositePeakEVMMaximum)
{
  return RFmxNR_ModAccFetchCompositeEVM(instrumentHandle, selectorString, timeout, compositeRMSEVMMean, compositePeakEVMMaximum);
}

int32 ModAccFetchFrequencyErrorMean(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* frequencyErrorMean)
{
  return RFmxNR_ModAccFetchFrequencyErrorMean(instrumentHandle, selectorString, timeout, frequencyErrorMean);
}

int32 ModAccFetchFrequencyErrorPerSlotMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 frequencyErrorPerSlotMaximum[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchFrequencyErrorPerSlotMaximumTrace(instrumentHandle, selectorString, timeout, x0, dx, frequencyErrorPerSlotMaximum, arraySize, actualArraySize);
}

int32 ModAccFetchIQGainImbalancePerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 iqGainImbalancePerSubcarrierMean[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchIQGainImbalancePerSubcarrierMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, iqGainImbalancePerSubcarrierMean, arraySize, actualArraySize);
}

int32 ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 iqQuadratureErrorPerSubcarrierMean[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, iqQuadratureErrorPerSubcarrierMean, arraySize, actualArraySize);
}

int32 ModAccFetchInBandEmissionTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 inBandEmission[], float32 inBandEmissionMask[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchInBandEmissionTrace(instrumentHandle, selectorString, timeout, x0, dx, inBandEmission, inBandEmissionMask, arraySize, actualArraySize);
}

int32 ModAccFetchPBCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pbchdmrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPBCHDMRSConstellationTrace(instrumentHandle, selectorString, timeout, pbchdmrsConstellation, arraySize, actualArraySize);
}

int32 ModAccFetchPBCHDMRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchdmrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPBCHDMRSConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(pbchdmrsConstellation), arraySize, actualArraySize);
}

int32 ModAccFetchPBCHDMRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchdmrsConstellationI[], float32 pbchdmrsConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPBCHDMRSConstellationTraceSplit(instrumentHandle, selectorString, timeout, pbchdmrsConstellationI, pbchdmrsConstellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchdmrsrmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, pbchdmrsrmsevmPerSubcarrierMean, arraySize, actualArraySize);
}

int32 ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchdmrsrmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, pbchdmrsrmsevmPerSymbolMean, arraySize, actualArraySize);
}

int32 ModAccFetchPBCHDataConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pbchDataConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPBCHDataConstellationTrace(instrumentHandle, selectorString, timeout, pbchDataConstellation, arraySize, actualArraySize);
}

int32 ModAccFetchPBCHDataConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchDataConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPBCHDataConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(pbchDataConstellation), arraySize, actualArraySize);
}

int32 ModAccFetchPBCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchDataConstellationI[], float32 pbchDataConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPBCHDataConstellationTraceSplit(instrumentHandle, selectorString, timeout, pbchDataConstellationI, pbchDataConstellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchDataRMSEVMPerSubcarrierMean[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, pbchDataRMSEVMPerSubcarrierMean, arraySize, actualArraySize);
}

int32 ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchDataRMSEVMPerSymbolMean[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, pbchDataRMSEVMPerSymbolMean, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH1024QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam1024Constellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH1024QAMConstellationTrace(instrumentHandle, selectorString, timeout, qam1024Constellation, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam1024Constellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH1024QAMConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(qam1024Constellation), arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH1024QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam1024ConstellationI[], float32 qam1024ConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH1024QAMConstellationTraceSplit(instrumentHandle, selectorString, timeout, qam1024ConstellationI, qam1024ConstellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH16QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam16Constellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH16QAMConstellationTrace(instrumentHandle, selectorString, timeout, qam16Constellation, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam16Constellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH16QAMConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(qam16Constellation), arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH16QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam16ConstellationI[], float32 qam16ConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH16QAMConstellationTraceSplit(instrumentHandle, selectorString, timeout, qam16ConstellationI, qam16ConstellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH256QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam256Constellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH256QAMConstellationTrace(instrumentHandle, selectorString, timeout, qam256Constellation, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam256Constellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH256QAMConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(qam256Constellation), arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH256QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam256ConstellationI[], float32 qam256ConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH256QAMConstellationTraceSplit(instrumentHandle, selectorString, timeout, qam256ConstellationI, qam256ConstellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH4096QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam4096Constellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH4096QAMConstellationTrace(instrumentHandle, selectorString, timeout, qam4096Constellation, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam4096Constellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH4096QAMConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(qam4096Constellation), arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH4096QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam4096ConstellationI[], float32 qam4096ConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH4096QAMConstellationTraceSplit(instrumentHandle, selectorString, timeout, qam4096ConstellationI, qam4096ConstellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH64QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam64Constellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH64QAMConstellationTrace(instrumentHandle, selectorString, timeout, qam64Constellation, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam64Constellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH64QAMConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(qam64Constellation), arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH64QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam64ConstellationI[], float32 qam64ConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH64QAMConstellationTraceSplit(instrumentHandle, selectorString, timeout, qam64ConstellationI, qam64ConstellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH8PSKConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle psk8Constellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH8PSKConstellationTrace(instrumentHandle, selectorString, timeout, psk8Constellation, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 psk8Constellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH8PSKConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(psk8Constellation), arraySize, actualArraySize);
}

int32 ModAccFetchPDSCH8PSKConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 psk8ConstellationI[], float32 psk8ConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCH8PSKConstellationTraceSplit(instrumentHandle, selectorString, timeout, psk8ConstellationI, psk8ConstellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschdmrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCHDMRSConstellationTrace(instrumentHandle, selectorString, timeout, pdschdmrsConstellation, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschdmrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCHDMRSConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(pdschdmrsConstellation), arraySize, actualArraySize);
}

int32 ModAccFetchPDSCHDMRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschdmrsConstellationI[], float32 pdschdmrsConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCHDMRSConstellationTraceSplit(instrumentHandle, selectorString, timeout, pdschdmrsConstellationI, pdschdmrsConstellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCHDataConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschDataConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCHDataConstellationTrace(instrumentHandle, selectorString, timeout, pdschDataConstellation, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCHDataConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschDataConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCHDataConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(pdschDataConstellation), arraySize, actualArraySize);
}

int32 ModAccFetchPDSCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschDataConstellationI[], float32 pdschDataConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCHDataConstellationTraceSplit(instrumentHandle, selectorString, timeout, pdschDataConstellationI, pdschDataConstellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCHDemodulatedBits(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int8 bits[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCHDemodulatedBits(instrumentHandle, selectorString, timeout, bits, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCHPTRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschptrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCHPTRSConstellationTrace(instrumentHandle, selectorString, timeout, pdschptrsConstellation, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschptrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCHPTRSConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(pdschptrsConstellation), arraySize, actualArraySize);
}

int32 ModAccFetchPDSCHPTRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschptrsConstellationI[], float32 pdschptrsConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCHPTRSConstellationTraceSplit(instrumentHandle, selectorString, timeout, pdschptrsConstellationI, pdschptrsConstellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCHQPSKConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qpskConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCHQPSKConstellationTrace(instrumentHandle, selectorString, timeout, qpskConstellation, arraySize, actualArraySize);
}

int32 ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qpskConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCHQPSKConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(qpskConstellation), arraySize, actualArraySize);
}

int32 ModAccFetchPDSCHQPSKConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qpskConstellationI[], float32 qpskConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPDSCHQPSKConstellationTraceSplit(instrumentHandle, selectorString, timeout, qpskConstellationI, qpskConstellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchPSSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pssConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPSSConstellationTrace(instrumentHandle, selectorString, timeout, pssConstellation, arraySize, actualArraySize);
}

int32 ModAccFetchPSSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pssConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPSSConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(pssConstellation), arraySize, actualArraySize);
}

int32 ModAccFetchPSSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pssConstellationI[], float32 pssConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPSSConstellationTraceSplit(instrumentHandle, selectorString, timeout, pssConstellationI, pssConstellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pssrmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, pssrmsevmPerSubcarrierMean, arraySize, actualArraySize);
}

int32 ModAccFetchPSSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pssrmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPSSRMSEVMPerSymbolMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, pssrmsevmPerSymbolMean, arraySize, actualArraySize);
}

int32 ModAccFetchPUSCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle puschdmrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPUSCHDMRSConstellationTrace(instrumentHandle, selectorString, timeout, puschdmrsConstellation, arraySize, actualArraySize);
}

int32 ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschdmrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPUSCHDMRSConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(puschdmrsConstellation), arraySize, actualArraySize);
}

int32 ModAccFetchPUSCHDMRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschdmrsConstellationI[], float32 puschdmrsConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPUSCHDMRSConstellationTraceSplit(instrumentHandle, selectorString, timeout, puschdmrsConstellationI, puschdmrsConstellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchPUSCHDataConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle puschDataConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPUSCHDataConstellationTrace(instrumentHandle, selectorString, timeout, puschDataConstellation, arraySize, actualArraySize);
}

int32 ModAccFetchPUSCHDataConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschDataConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPUSCHDataConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(puschDataConstellation), arraySize, actualArraySize);
}

int32 ModAccFetchPUSCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschDataConstellationI[], float32 puschDataConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPUSCHDataConstellationTraceSplit(instrumentHandle, selectorString, timeout, puschDataConstellationI, puschDataConstellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchPUSCHDemodulatedBits(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int8 bits[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPUSCHDemodulatedBits(instrumentHandle, selectorString, timeout, bits, arraySize, actualArraySize);
}

int32 ModAccFetchPUSCHPTRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle puschptrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPUSCHPTRSConstellationTrace(instrumentHandle, selectorString, timeout, puschptrsConstellation, arraySize, actualArraySize);
}

int32 ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschptrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPUSCHPTRSConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(puschptrsConstellation), arraySize, actualArraySize);
}

int32 ModAccFetchPUSCHPTRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschptrsConstellationI[], float32 puschptrsConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPUSCHPTRSConstellationTraceSplit(instrumentHandle, selectorString, timeout, puschptrsConstellationI, puschptrsConstellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchPUSCHPhaseOffsetTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 puschPhaseOffset[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPUSCHPhaseOffsetTrace(instrumentHandle, selectorString, timeout, x0, dx, puschPhaseOffset, arraySize, actualArraySize);
}

int32 ModAccFetchPeakEVMHighPerSymbolMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMHighPerSymbolMaximum[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPeakEVMHighPerSymbolMaximumTrace(instrumentHandle, selectorString, timeout, x0, dx, peakEVMHighPerSymbolMaximum, arraySize, actualArraySize);
}

int32 ModAccFetchPeakEVMLowPerSymbolMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMLowPerSymbolMaximum[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPeakEVMLowPerSymbolMaximumTrace(instrumentHandle, selectorString, timeout, x0, dx, peakEVMLowPerSymbolMaximum, arraySize, actualArraySize);
}

int32 ModAccFetchPeakEVMPerSlotMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMPerSlotMaximum[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPeakEVMPerSlotMaximumTrace(instrumentHandle, selectorString, timeout, x0, dx, peakEVMPerSlotMaximum, arraySize, actualArraySize);
}

int32 ModAccFetchPeakEVMPerSubcarrierMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMPerSubcarrierMaximum[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPeakEVMPerSubcarrierMaximumTrace(instrumentHandle, selectorString, timeout, x0, dx, peakEVMPerSubcarrierMaximum, arraySize, actualArraySize);
}

int32 ModAccFetchPeakEVMPerSymbolMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMPerSymbolMaximum[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchPeakEVMPerSymbolMaximumTrace(instrumentHandle, selectorString, timeout, x0, dx, peakEVMPerSymbolMaximum, arraySize, actualArraySize);
}

int32 ModAccFetchRMSEVMHighPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmHighPerSymbolMean[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchRMSEVMHighPerSymbolMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, rmsevmHighPerSymbolMean, arraySize, actualArraySize);
}

int32 ModAccFetchRMSEVMLowPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmLowPerSymbolMean[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchRMSEVMLowPerSymbolMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, rmsevmLowPerSymbolMean, arraySize, actualArraySize);
}

int32 ModAccFetchRMSEVMPerSlotMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmPerSlotMean[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchRMSEVMPerSlotMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, rmsevmPerSlotMean, arraySize, actualArraySize);
}

int32 ModAccFetchRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchRMSEVMPerSubcarrierMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, rmsevmPerSubcarrierMean, arraySize, actualArraySize);
}

int32 ModAccFetchRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchRMSEVMPerSymbolMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, rmsevmPerSymbolMean, arraySize, actualArraySize);
}

int32 ModAccFetchSSSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle sssConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchSSSConstellationTrace(instrumentHandle, selectorString, timeout, sssConstellation, arraySize, actualArraySize);
}

int32 ModAccFetchSSSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 sssConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchSSSConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(sssConstellation), arraySize, actualArraySize);
}

int32 ModAccFetchSSSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 sssConstellationI[], float32 sssConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchSSSConstellationTraceSplit(instrumentHandle, selectorString, timeout, sssConstellationI, sssConstellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 sssrmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, sssrmsevmPerSubcarrierMean, arraySize, actualArraySize);
}

int32 ModAccFetchSSSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 sssrmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchSSSRMSEVMPerSymbolMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, sssrmsevmPerSymbolMean, arraySize, actualArraySize);
}

int32 ModAccFetchSpectralFlatnessTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectralFlatness[], float32 spectralFlatnessLowerMask[], float32 spectralFlatnessUpperMask[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchSpectralFlatnessTrace(instrumentHandle, selectorString, timeout, x0, dx, spectralFlatness, spectralFlatnessLowerMask, spectralFlatnessUpperMask, arraySize, actualArraySize);
}

int32 ModAccFetchSubblockInBandEmissionTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 subblockInBandEmission[], float64 subblockInBandEmissionMask[], float64 subblockInBandEmissionRBIndices[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchSubblockInBandEmissionTrace(instrumentHandle, selectorString, timeout, subblockInBandEmission, subblockInBandEmissionMask, subblockInBandEmissionRBIndices, arraySize, actualArraySize);
}

int32 ModAccFetchTransientPeriodLocationsTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 transientPeriodLocations[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_ModAccFetchTransientPeriodLocationsTrace(instrumentHandle, selectorString, timeout, x0, dx, transientPeriodLocations, arraySize, actualArraySize);
}

int32 ModAccValidateCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* calibrationDataValid)
{
  return RFmxNR_ModAccValidateCalibrationData(instrumentHandle, selectorString, calibrationDataValid);
}

int32 OBWCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  return RFmxNR_OBWCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)
{
  return RFmxNR_OBWCfgRBWFilter(instrumentHandle, selectorString, rbwAuto, rbw, rbwFilterType);
}

int32 OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)
{
  return RFmxNR_OBWCfgSweepTime(instrumentHandle, selectorString, sweepTimeAuto, sweepTimeInterval);
}

int32 OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* occupiedBandwidth, float64* absolutePower, float64* startFrequency, float64* stopFrequency)
{
  return RFmxNR_OBWFetchMeasurement(instrumentHandle, selectorString, timeout, occupiedBandwidth, absolutePower, startFrequency, stopFrequency);
}

int32 OBWFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_OBWFetchSpectrum(instrumentHandle, selectorString, timeout, x0, dx, spectrum, arraySize, actualArraySize);
}

int32 PVTCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  return RFmxNR_PVTCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 PVTCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)
{
  return RFmxNR_PVTCfgMeasurementMethod(instrumentHandle, selectorString, measurementMethod);
}

int32 PVTCfgOFFPowerExclusionPeriods(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offPowerExclusionBefore, float64 offPowerExclusionAfter)
{
  return RFmxNR_PVTCfgOFFPowerExclusionPeriods(instrumentHandle, selectorString, offPowerExclusionBefore, offPowerExclusionAfter);
}

int32 PVTFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* absoluteOFFPowerBefore, float64* absoluteOFFPowerAfter, float64* absoluteONPower, float64* burstWidth)
{
  return RFmxNR_PVTFetchMeasurement(instrumentHandle, selectorString, timeout, measurementStatus, absoluteOFFPowerBefore, absoluteOFFPowerAfter, absoluteONPower, burstWidth);
}

int32 PVTFetchMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 absoluteOFFPowerBefore[], float64 absoluteOFFPowerAfter[], float64 absoluteONPower[], float64 burstWidth[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_PVTFetchMeasurementArray(instrumentHandle, selectorString, timeout, measurementStatus, absoluteOFFPowerBefore, absoluteOFFPowerAfter, absoluteONPower, burstWidth, arraySize, actualArraySize);
}

int32 PVTFetchSignalPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 signalPower[], float32 absoluteLimit[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_PVTFetchSignalPowerTrace(instrumentHandle, selectorString, timeout, x0, dx, signalPower, absoluteLimit, arraySize, actualArraySize);
}

int32 PVTFetchWindowedSignalPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 windowedSignalPower[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_PVTFetchWindowedSignalPowerTrace(instrumentHandle, selectorString, timeout, x0, dx, windowedSignalPower, arraySize, actualArraySize);
}

int32 ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID)
{
  return RFmxNR_ResetAttribute(instrumentHandle, selectorString, attributeID);
}

int32 ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  return RFmxNR_ResetToDefault(instrumentHandle, selectorString);
}

int32 SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  return RFmxNR_SEMCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 SEMCfgComponentCarrierRatedOutputPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 componentCarrierRatedOutputPower)
{
  return RFmxNR_SEMCfgComponentCarrierRatedOutputPower(instrumentHandle, selectorString, componentCarrierRatedOutputPower);
}

int32 SEMCfgComponentCarrierRatedOutputPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 componentCarrierRatedOutputPower[], int32 numberOfElements)
{
  return RFmxNR_SEMCfgComponentCarrierRatedOutputPowerArray(instrumentHandle, selectorString, componentCarrierRatedOutputPower, numberOfElements);
}

int32 SEMCfgNumberOfOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets)
{
  return RFmxNR_SEMCfgNumberOfOffsets(instrumentHandle, selectorString, numberOfOffsets);
}

int32 SEMCfgOffsetAbsoluteLimit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 absoluteLimitStart, float64 absoluteLimitStop)
{
  return RFmxNR_SEMCfgOffsetAbsoluteLimit(instrumentHandle, selectorString, absoluteLimitStart, absoluteLimitStop);
}

int32 SEMCfgOffsetAbsoluteLimitArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 absoluteLimitStart[], float64 absoluteLimitStop[], int32 numberOfElements)
{
  return RFmxNR_SEMCfgOffsetAbsoluteLimitArray(instrumentHandle, selectorString, absoluteLimitStart, absoluteLimitStop, numberOfElements);
}

int32 SEMCfgOffsetBandwidthIntegral(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandwidthIntegral)
{
  return RFmxNR_SEMCfgOffsetBandwidthIntegral(instrumentHandle, selectorString, bandwidthIntegral);
}

int32 SEMCfgOffsetBandwidthIntegralArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandwidthIntegral[], int32 numberOfElements)
{
  return RFmxNR_SEMCfgOffsetBandwidthIntegralArray(instrumentHandle, selectorString, bandwidthIntegral, numberOfElements);
}

int32 SEMCfgOffsetFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetStartFrequency, float64 offsetStopFrequency, int32 offsetSideband)
{
  return RFmxNR_SEMCfgOffsetFrequency(instrumentHandle, selectorString, offsetStartFrequency, offsetStopFrequency, offsetSideband);
}

int32 SEMCfgOffsetFrequencyArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetStartFrequency[], float64 offsetStopFrequency[], int32 offsetSideband[], int32 numberOfElements)
{
  return RFmxNR_SEMCfgOffsetFrequencyArray(instrumentHandle, selectorString, offsetStartFrequency, offsetStopFrequency, offsetSideband, numberOfElements);
}

int32 SEMCfgOffsetLimitFailMask(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 limitFailMask)
{
  return RFmxNR_SEMCfgOffsetLimitFailMask(instrumentHandle, selectorString, limitFailMask);
}

int32 SEMCfgOffsetLimitFailMaskArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 limitFailMask[], int32 numberOfElements)
{
  return RFmxNR_SEMCfgOffsetLimitFailMaskArray(instrumentHandle, selectorString, limitFailMask, numberOfElements);
}

int32 SEMCfgOffsetRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetRBW, int32 offsetRBWFilterType)
{
  return RFmxNR_SEMCfgOffsetRBWFilter(instrumentHandle, selectorString, offsetRBW, offsetRBWFilterType);
}

int32 SEMCfgOffsetRBWFilterArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetRBW[], int32 offsetRBWFilterType[], int32 numberOfElements)
{
  return RFmxNR_SEMCfgOffsetRBWFilterArray(instrumentHandle, selectorString, offsetRBW, offsetRBWFilterType, numberOfElements);
}

int32 SEMCfgOffsetRelativeLimit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 relativeLimitStart, float64 relativeLimitStop)
{
  return RFmxNR_SEMCfgOffsetRelativeLimit(instrumentHandle, selectorString, relativeLimitStart, relativeLimitStop);
}

int32 SEMCfgOffsetRelativeLimitArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 relativeLimitStart[], float64 relativeLimitStop[], int32 numberOfElements)
{
  return RFmxNR_SEMCfgOffsetRelativeLimitArray(instrumentHandle, selectorString, relativeLimitStart, relativeLimitStop, numberOfElements);
}

int32 SEMCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)
{
  return RFmxNR_SEMCfgSweepTime(instrumentHandle, selectorString, sweepTimeAuto, sweepTimeInterval);
}

int32 SEMCfgUplinkMaskType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 uplinkMaskType)
{
  return RFmxNR_SEMCfgUplinkMaskType(instrumentHandle, selectorString, uplinkMaskType);
}

int32 SEMFetchComponentCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absolutePower, float64* peakAbsolutePower, float64* peakFrequency, float64* relativePower)
{
  return RFmxNR_SEMFetchComponentCarrierMeasurement(instrumentHandle, selectorString, timeout, absolutePower, peakAbsolutePower, peakFrequency, relativePower);
}

int32 SEMFetchComponentCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 relativePower[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_SEMFetchComponentCarrierMeasurementArray(instrumentHandle, selectorString, timeout, absolutePower, peakAbsolutePower, peakFrequency, relativePower, arraySize, actualArraySize);
}

int32 SEMFetchLowerOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower)
{
  return RFmxNR_SEMFetchLowerOffsetMargin(instrumentHandle, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower);
}

int32 SEMFetchLowerOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_SEMFetchLowerOffsetMarginArray(instrumentHandle, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower, arraySize, actualArraySize);
}

int32 SEMFetchLowerOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAbsolutePower, float64* totalRelativePower, float64* peakAbsolutePower, float64* peakFrequency, float64* peakRelativePower)
{
  return RFmxNR_SEMFetchLowerOffsetPower(instrumentHandle, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower);
}

int32 SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 totalAbsolutePower[], float64 totalRelativePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 peakRelativePower[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_SEMFetchLowerOffsetPowerArray(instrumentHandle, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower, arraySize, actualArraySize);
}

int32 SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus)
{
  return RFmxNR_SEMFetchMeasurementStatus(instrumentHandle, selectorString, timeout, measurementStatus);
}

int32 SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], float32 compositeMask[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_SEMFetchSpectrum(instrumentHandle, selectorString, timeout, x0, dx, spectrum, compositeMask, arraySize, actualArraySize);
}

int32 SEMFetchSubblockMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* subblockPower, float64* integrationBandwidth, float64* frequency)
{
  return RFmxNR_SEMFetchSubblockMeasurement(instrumentHandle, selectorString, timeout, subblockPower, integrationBandwidth, frequency);
}

int32 SEMFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAggregatedPower)
{
  return RFmxNR_SEMFetchTotalAggregatedPower(instrumentHandle, selectorString, timeout, totalAggregatedPower);
}

int32 SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower)
{
  return RFmxNR_SEMFetchUpperOffsetMargin(instrumentHandle, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower);
}

int32 SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_SEMFetchUpperOffsetMarginArray(instrumentHandle, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower, arraySize, actualArraySize);
}

int32 SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAbsolutePower, float64* totalRelativePower, float64* peakAbsolutePower, float64* peakFrequency, float64* peakRelativePower)
{
  return RFmxNR_SEMFetchUpperOffsetPower(instrumentHandle, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower);
}

int32 SEMFetchUpperOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 totalAbsolutePower[], float64 totalRelativePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 peakRelativePower[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_SEMFetchUpperOffsetPowerArray(instrumentHandle, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower, arraySize, actualArraySize);
}

int32 SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)
{
  return RFmxNR_SelectMeasurements(instrumentHandle, selectorString, measurements, enableAllTraces);
}

int32 SendSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle)
{
  return RFmxNR_SendSoftwareEdgeTrigger(instrumentHandle);
}

int32 SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal)
{
  return RFmxNR_SetAttributeF32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal[], int32 arraySize)
{
  return RFmxNR_SetAttributeF32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal)
{
  return RFmxNR_SetAttributeF64(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal[], int32 arraySize)
{
  return RFmxNR_SetAttributeF64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int16 attrVal)
{
  return RFmxNR_SetAttributeI16(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal)
{
  return RFmxNR_SetAttributeI32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal[], int32 arraySize)
{
  return RFmxNR_SetAttributeI32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal)
{
  return RFmxNR_SetAttributeI64(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal[], int32 arraySize)
{
  return RFmxNR_SetAttributeI64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal)
{
  return RFmxNR_SetAttributeI8(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal[], int32 arraySize)
{
  return RFmxNR_SetAttributeI8Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexDouble attrVal[], int32 arraySize)
{
  return RFmxNR_SetAttributeNIComplexDoubleArray(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexSingle attrVal[], int32 arraySize)
{
  return RFmxNR_SetAttributeNIComplexSingleArray(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, char attrVal[])
{
  return RFmxNR_SetAttributeString(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt16 attrVal)
{
  return RFmxNR_SetAttributeU16(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal)
{
  return RFmxNR_SetAttributeU32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal[], int32 arraySize)
{
  return RFmxNR_SetAttributeU32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt64 attrVal[], int32 arraySize)
{
  return RFmxNR_SetAttributeU64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal)
{
  return RFmxNR_SetAttributeU8(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal[], int32 arraySize)
{
  return RFmxNR_SetAttributeU8Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 TXPFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* averagePowerMean, float64* peakPowerMaximum)
{
  return RFmxNR_TXPFetchMeasurement(instrumentHandle, selectorString, timeout, averagePowerMean, peakPowerMaximum);
}

int32 TXPFetchPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 power[], int32 arraySize, int32* actualArraySize)
{
  return RFmxNR_TXPFetchPowerTrace(instrumentHandle, selectorString, timeout, x0, dx, power, arraySize, actualArraySize);
}

int32 WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)
{
  return RFmxNR_WaitForAcquisitionComplete(instrumentHandle, timeout);
}

int32 WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)
{
  return RFmxNR_WaitForMeasurementComplete(instrumentHandle, selectorString, timeout);
}

}  // namespace nirfmxnr_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/nirfmxnr/nirfmxnr_library.cpp sha256=3b14565f413eda041ca6f117df11ac4c454a44a86e180b4b8514bb3229a41ee8 bytes=184379 -->
## FILE: generated/nirfmxnr/nirfmxnr_library.cpp

- repository: `ni/grpc-device`
- source_path: `generated/nirfmxnr/nirfmxnr_library.cpp`
- sha256: `3b14565f413eda041ca6f117df11ac4c454a44a86e180b4b8514bb3229a41ee8`
- bytes: 184379

````cpp
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Service implementation for the NI-RFMXNR Metadata
//---------------------------------------------------------------------
#include "nirfmxnr_library.h"
#include <server/shared_library.h>

#include <memory>

#if defined(_MSC_VER)
static const char* kLibraryName = "niRFmxNR.dll";
#else
static const char* kLibraryName = "libnirfmxnr.so.1";
#endif

namespace nirfmxnr_grpc {

NiRFmxNRLibrary::NiRFmxNRLibrary() : NiRFmxNRLibrary(std::make_shared<nidevice_grpc::SharedLibrary>()) {}

NiRFmxNRLibrary::NiRFmxNRLibrary(std::shared_ptr<nidevice_grpc::SharedLibraryInterface> shared_library) : shared_library_(shared_library)
{
  shared_library_->set_library_name(kLibraryName);
  shared_library_->load();
  bool loaded = shared_library_->is_loaded();
  memset(&function_pointers_, 0, sizeof(function_pointers_));
  if (!loaded) {
    return;
  }
  function_pointers_.ACPCfgAveraging = reinterpret_cast<ACPCfgAveragingPtr>(shared_library_->get_function_pointer("RFmxNR_ACPCfgAveraging"));
  function_pointers_.ACPCfgMeasurementMethod = reinterpret_cast<ACPCfgMeasurementMethodPtr>(shared_library_->get_function_pointer("RFmxNR_ACPCfgMeasurementMethod"));
  function_pointers_.ACPCfgNoiseCompensationEnabled = reinterpret_cast<ACPCfgNoiseCompensationEnabledPtr>(shared_library_->get_function_pointer("RFmxNR_ACPCfgNoiseCompensationEnabled"));
  function_pointers_.ACPCfgNumberOfENDCOffsets = reinterpret_cast<ACPCfgNumberOfENDCOffsetsPtr>(shared_library_->get_function_pointer("RFmxNR_ACPCfgNumberOfENDCOffsets"));
  function_pointers_.ACPCfgNumberOfEUTRAOffsets = reinterpret_cast<ACPCfgNumberOfEUTRAOffsetsPtr>(shared_library_->get_function_pointer("RFmxNR_ACPCfgNumberOfEUTRAOffsets"));
  function_pointers_.ACPCfgNumberOfNROffsets = reinterpret_cast<ACPCfgNumberOfNROffsetsPtr>(shared_library_->get_function_pointer("RFmxNR_ACPCfgNumberOfNROffsets"));
  function_pointers_.ACPCfgNumberOfUTRAOffsets = reinterpret_cast<ACPCfgNumberOfUTRAOffsetsPtr>(shared_library_->get_function_pointer("RFmxNR_ACPCfgNumberOfUTRAOffsets"));
  function_pointers_.ACPCfgPowerUnits = reinterpret_cast<ACPCfgPowerUnitsPtr>(shared_library_->get_function_pointer("RFmxNR_ACPCfgPowerUnits"));
  function_pointers_.ACPCfgRBWFilter = reinterpret_cast<ACPCfgRBWFilterPtr>(shared_library_->get_function_pointer("RFmxNR_ACPCfgRBWFilter"));
  function_pointers_.ACPCfgSweepTime = reinterpret_cast<ACPCfgSweepTimePtr>(shared_library_->get_function_pointer("RFmxNR_ACPCfgSweepTime"));
  function_pointers_.ACPFetchAbsolutePowersTrace = reinterpret_cast<ACPFetchAbsolutePowersTracePtr>(shared_library_->get_function_pointer("RFmxNR_ACPFetchAbsolutePowersTrace"));
  function_pointers_.ACPFetchComponentCarrierMeasurement = reinterpret_cast<ACPFetchComponentCarrierMeasurementPtr>(shared_library_->get_function_pointer("RFmxNR_ACPFetchComponentCarrierMeasurement"));
  function_pointers_.ACPFetchComponentCarrierMeasurementArray = reinterpret_cast<ACPFetchComponentCarrierMeasurementArrayPtr>(shared_library_->get_function_pointer("RFmxNR_ACPFetchComponentCarrierMeasurementArray"));
  function_pointers_.ACPFetchOffsetMeasurement = reinterpret_cast<ACPFetchOffsetMeasurementPtr>(shared_library_->get_function_pointer("RFmxNR_ACPFetchOffsetMeasurement"));
  function_pointers_.ACPFetchOffsetMeasurementArray = reinterpret_cast<ACPFetchOffsetMeasurementArrayPtr>(shared_library_->get_function_pointer("RFmxNR_ACPFetchOffsetMeasurementArray"));
  function_pointers_.ACPFetchRelativePowersTrace = reinterpret_cast<ACPFetchRelativePowersTracePtr>(shared_library_->get_function_pointer("RFmxNR_ACPFetchRelativePowersTrace"));
  function_pointers_.ACPFetchSpectrum = reinterpret_cast<ACPFetchSpectrumPtr>(shared_library_->get_function_pointer("RFmxNR_ACPFetchSpectrum"));
  function_pointers_.ACPFetchSubblockMeasurement = reinterpret_cast<ACPFetchSubblockMeasurementPtr>(shared_library_->get_function_pointer("RFmxNR_ACPFetchSubblockMeasurement"));
  function_pointers_.ACPFetchTotalAggregatedPower = reinterpret_cast<ACPFetchTotalAggregatedPowerPtr>(shared_library_->get_function_pointer("RFmxNR_ACPFetchTotalAggregatedPower"));
  function_pointers_.ACPValidateNoiseCalibrationData = reinterpret_cast<ACPValidateNoiseCalibrationDataPtr>(shared_library_->get_function_pointer("RFmxNR_ACPValidateNoiseCalibrationData"));
  function_pointers_.AbortMeasurements = reinterpret_cast<AbortMeasurementsPtr>(shared_library_->get_function_pointer("RFmxNR_AbortMeasurements"));
  function_pointers_.AnalyzeIQ1Waveform = reinterpret_cast<AnalyzeIQ1WaveformPtr>(shared_library_->get_function_pointer("RFmxNR_AnalyzeIQ1Waveform"));
  function_pointers_.AnalyzeIQ1WaveformInterleavedIQ = reinterpret_cast<AnalyzeIQ1WaveformInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_AnalyzeIQ1Waveform"));
  function_pointers_.AnalyzeIQ1WaveformSplit = reinterpret_cast<AnalyzeIQ1WaveformSplitPtr>(shared_library_->get_function_pointer("RFmxNR_AnalyzeIQ1WaveformSplit"));
  function_pointers_.AnalyzeNWaveformsIQ = reinterpret_cast<AnalyzeNWaveformsIQPtr>(shared_library_->get_function_pointer("RFmxNR_AnalyzeNWaveformsIQ"));
  function_pointers_.AnalyzeNWaveformsIQInterleavedIQ = reinterpret_cast<AnalyzeNWaveformsIQInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_AnalyzeNWaveformsIQ"));
  function_pointers_.AnalyzeNWaveformsIQSplit = reinterpret_cast<AnalyzeNWaveformsIQSplitPtr>(shared_library_->get_function_pointer("RFmxNR_AnalyzeNWaveformsIQSplit"));
  function_pointers_.AnalyzeNWaveformsSpectrum = reinterpret_cast<AnalyzeNWaveformsSpectrumPtr>(shared_library_->get_function_pointer("RFmxNR_AnalyzeNWaveformsSpectrum"));
  function_pointers_.AnalyzeSpectrum1Waveform = reinterpret_cast<AnalyzeSpectrum1WaveformPtr>(shared_library_->get_function_pointer("RFmxNR_AnalyzeSpectrum1Waveform"));
  function_pointers_.AutoLevel = reinterpret_cast<AutoLevelPtr>(shared_library_->get_function_pointer("RFmxNR_AutoLevel"));
  function_pointers_.BuildBandwidthPartString = reinterpret_cast<BuildBandwidthPartStringPtr>(shared_library_->get_function_pointer("RFmxNR_BuildBandwidthPartString"));
  function_pointers_.BuildCORESETClusterString = reinterpret_cast<BuildCORESETClusterStringPtr>(shared_library_->get_function_pointer("RFmxNR_BuildCORESETClusterString"));
  function_pointers_.BuildCORESETString = reinterpret_cast<BuildCORESETStringPtr>(shared_library_->get_function_pointer("RFmxNR_BuildCORESETString"));
  function_pointers_.BuildCarrierString = reinterpret_cast<BuildCarrierStringPtr>(shared_library_->get_function_pointer("RFmxNR_BuildCarrierString"));
  function_pointers_.BuildListStepString = reinterpret_cast<BuildListStepStringPtr>(shared_library_->get_function_pointer("RFmxNR_BuildListStepString"));
  function_pointers_.BuildListString = reinterpret_cast<BuildListStringPtr>(shared_library_->get_function_pointer("RFmxNR_BuildListString"));
  function_pointers_.BuildOffsetString = reinterpret_cast<BuildOffsetStringPtr>(shared_library_->get_function_pointer("RFmxNR_BuildOffsetString"));
  function_pointers_.BuildPDCCHString = reinterpret_cast<BuildPDCCHStringPtr>(shared_library_->get_function_pointer("RFmxNR_BuildPDCCHString"));
  function_pointers_.BuildPDSCHClusterString = reinterpret_cast<BuildPDSCHClusterStringPtr>(shared_library_->get_function_pointer("RFmxNR_BuildPDSCHClusterString"));
  function_pointers_.BuildPDSCHString = reinterpret_cast<BuildPDSCHStringPtr>(shared_library_->get_function_pointer("RFmxNR_BuildPDSCHString"));
  function_pointers_.BuildPUSCHClusterString = reinterpret_cast<BuildPUSCHClusterStringPtr>(shared_library_->get_function_pointer("RFmxNR_BuildPUSCHClusterString"));
  function_pointers_.BuildPUSCHString = reinterpret_cast<BuildPUSCHStringPtr>(shared_library_->get_function_pointer("RFmxNR_BuildPUSCHString"));
  function_pointers_.BuildSignalString = reinterpret_cast<BuildSignalStringPtr>(shared_library_->get_function_pointer("RFmxNR_BuildSignalString"));
  function_pointers_.BuildSubblockString = reinterpret_cast<BuildSubblockStringPtr>(shared_library_->get_function_pointer("RFmxNR_BuildSubblockString"));
  function_pointers_.BuildUserString = reinterpret_cast<BuildUserStringPtr>(shared_library_->get_function_pointer("RFmxNR_BuildUserString"));
  function_pointers_.CHPCfgAveraging = reinterpret_cast<CHPCfgAveragingPtr>(shared_library_->get_function_pointer("RFmxNR_CHPCfgAveraging"));
  function_pointers_.CHPCfgRBWFilter = reinterpret_cast<CHPCfgRBWFilterPtr>(shared_library_->get_function_pointer("RFmxNR_CHPCfgRBWFilter"));
  function_pointers_.CHPCfgSweepTime = reinterpret_cast<CHPCfgSweepTimePtr>(shared_library_->get_function_pointer("RFmxNR_CHPCfgSweepTime"));
  function_pointers_.CHPFetchComponentCarrierMeasurement = reinterpret_cast<CHPFetchComponentCarrierMeasurementPtr>(shared_library_->get_function_pointer("RFmxNR_CHPFetchComponentCarrierMeasurement"));
  function_pointers_.CHPFetchComponentCarrierMeasurementArray = reinterpret_cast<CHPFetchComponentCarrierMeasurementArrayPtr>(shared_library_->get_function_pointer("RFmxNR_CHPFetchComponentCarrierMeasurementArray"));
  function_pointers_.CHPFetchSpectrum = reinterpret_cast<CHPFetchSpectrumPtr>(shared_library_->get_function_pointer("RFmxNR_CHPFetchSpectrum"));
  function_pointers_.CHPFetchSubblockPower = reinterpret_cast<CHPFetchSubblockPowerPtr>(shared_library_->get_function_pointer("RFmxNR_CHPFetchSubblockPower"));
  function_pointers_.CHPFetchTotalAggregatedPower = reinterpret_cast<CHPFetchTotalAggregatedPowerPtr>(shared_library_->get_function_pointer("RFmxNR_CHPFetchTotalAggregatedPower"));
  function_pointers_.CHPValidateNoiseCalibrationData = reinterpret_cast<CHPValidateNoiseCalibrationDataPtr>(shared_library_->get_function_pointer("RFmxNR_CHPValidateNoiseCalibrationData"));
  function_pointers_.CfgDigitalEdgeTrigger = reinterpret_cast<CfgDigitalEdgeTriggerPtr>(shared_library_->get_function_pointer("RFmxNR_CfgDigitalEdgeTrigger"));
  function_pointers_.CfgExternalAttenuation = reinterpret_cast<CfgExternalAttenuationPtr>(shared_library_->get_function_pointer("RFmxNR_CfgExternalAttenuation"));
  function_pointers_.CfgFrequency = reinterpret_cast<CfgFrequencyPtr>(shared_library_->get_function_pointer("RFmxNR_CfgFrequency"));
  function_pointers_.CfgFrequencyReference = reinterpret_cast<CfgFrequencyReferencePtr>(shared_library_->get_function_pointer("RFmxNR_CfgFrequencyReference"));
  function_pointers_.CfgIQPowerEdgeTrigger = reinterpret_cast<CfgIQPowerEdgeTriggerPtr>(shared_library_->get_function_pointer("RFmxNR_CfgIQPowerEdgeTrigger"));
  function_pointers_.CfgMechanicalAttenuation = reinterpret_cast<CfgMechanicalAttenuationPtr>(shared_library_->get_function_pointer("RFmxNR_CfgMechanicalAttenuation"));
  function_pointers_.CfgRF = reinterpret_cast<CfgRFPtr>(shared_library_->get_function_pointer("RFmxNR_CfgRF"));
  function_pointers_.CfgRFAttenuation = reinterpret_cast<CfgRFAttenuationPtr>(shared_library_->get_function_pointer("RFmxNR_CfgRFAttenuation"));
  function_pointers_.CfgReferenceLevel = reinterpret_cast<CfgReferenceLevelPtr>(shared_library_->get_function_pointer("RFmxNR_CfgReferenceLevel"));
  function_pointers_.CfgSelectedPortsMultiple = reinterpret_cast<CfgSelectedPortsMultiplePtr>(shared_library_->get_function_pointer("RFmxNR_CfgSelectedPortsMultiple"));
  function_pointers_.CfgSoftwareEdgeTrigger = reinterpret_cast<CfgSoftwareEdgeTriggerPtr>(shared_library_->get_function_pointer("RFmxNR_CfgSoftwareEdgeTrigger"));
  function_pointers_.CfggNodeBCategory = reinterpret_cast<CfggNodeBCategoryPtr>(shared_library_->get_function_pointer("RFmxNR_CfggNodeBCategory"));
  function_pointers_.CheckMeasurementStatus = reinterpret_cast<CheckMeasurementStatusPtr>(shared_library_->get_function_pointer("RFmxNR_CheckMeasurementStatus"));
  function_pointers_.ClearAllNamedResults = reinterpret_cast<ClearAllNamedResultsPtr>(shared_library_->get_function_pointer("RFmxNR_ClearAllNamedResults"));
  function_pointers_.ClearNamedResult = reinterpret_cast<ClearNamedResultPtr>(shared_library_->get_function_pointer("RFmxNR_ClearNamedResult"));
  function_pointers_.ClearNoiseCalibrationDatabase = reinterpret_cast<ClearNoiseCalibrationDatabasePtr>(shared_library_->get_function_pointer("RFmxNR_ClearNoiseCalibrationDatabase"));
  function_pointers_.CloneSignalConfiguration = reinterpret_cast<CloneSignalConfigurationPtr>(shared_library_->get_function_pointer("RFmxNR_CloneSignalConfiguration"));
  function_pointers_.Close = reinterpret_cast<ClosePtr>(shared_library_->get_function_pointer("RFmxNR_Close"));
  function_pointers_.Commit = reinterpret_cast<CommitPtr>(shared_library_->get_function_pointer("RFmxNR_Commit"));
  function_pointers_.CreateList = reinterpret_cast<CreateListPtr>(shared_library_->get_function_pointer("RFmxNR_CreateList"));
  function_pointers_.CreateListStep = reinterpret_cast<CreateListStepPtr>(shared_library_->get_function_pointer("RFmxNR_CreateListStep"));
  function_pointers_.CreateSignalConfiguration = reinterpret_cast<CreateSignalConfigurationPtr>(shared_library_->get_function_pointer("RFmxNR_CreateSignalConfiguration"));
  function_pointers_.DeleteList = reinterpret_cast<DeleteListPtr>(shared_library_->get_function_pointer("RFmxNR_DeleteList"));
  function_pointers_.DeleteSignalConfiguration = reinterpret_cast<DeleteSignalConfigurationPtr>(shared_library_->get_function_pointer("RFmxNR_DeleteSignalConfiguration"));
  function_pointers_.DisableTrigger = reinterpret_cast<DisableTriggerPtr>(shared_library_->get_function_pointer("RFmxNR_DisableTrigger"));
  function_pointers_.GetAllNamedResultNames = reinterpret_cast<GetAllNamedResultNamesPtr>(shared_library_->get_function_pointer("RFmxNR_GetAllNamedResultNames"));
  function_pointers_.GetAttributeF32 = reinterpret_cast<GetAttributeF32Ptr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeF32"));
  function_pointers_.GetAttributeF32Array = reinterpret_cast<GetAttributeF32ArrayPtr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeF32Array"));
  function_pointers_.GetAttributeF64 = reinterpret_cast<GetAttributeF64Ptr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeF64"));
  function_pointers_.GetAttributeF64Array = reinterpret_cast<GetAttributeF64ArrayPtr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeF64Array"));
  function_pointers_.GetAttributeI16 = reinterpret_cast<GetAttributeI16Ptr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeI16"));
  function_pointers_.GetAttributeI32 = reinterpret_cast<GetAttributeI32Ptr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeI32"));
  function_pointers_.GetAttributeI32Array = reinterpret_cast<GetAttributeI32ArrayPtr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeI32Array"));
  function_pointers_.GetAttributeI64 = reinterpret_cast<GetAttributeI64Ptr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeI64"));
  function_pointers_.GetAttributeI64Array = reinterpret_cast<GetAttributeI64ArrayPtr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeI64Array"));
  function_pointers_.GetAttributeI8 = reinterpret_cast<GetAttributeI8Ptr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeI8"));
  function_pointers_.GetAttributeI8Array = reinterpret_cast<GetAttributeI8ArrayPtr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeI8Array"));
  function_pointers_.GetAttributeNIComplexDoubleArray = reinterpret_cast<GetAttributeNIComplexDoubleArrayPtr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeNIComplexDoubleArray"));
  function_pointers_.GetAttributeNIComplexSingleArray = reinterpret_cast<GetAttributeNIComplexSingleArrayPtr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeNIComplexSingleArray"));
  function_pointers_.GetAttributeString = reinterpret_cast<GetAttributeStringPtr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeString"));
  function_pointers_.GetAttributeU16 = reinterpret_cast<GetAttributeU16Ptr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeU16"));
  function_pointers_.GetAttributeU32 = reinterpret_cast<GetAttributeU32Ptr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeU32"));
  function_pointers_.GetAttributeU32Array = reinterpret_cast<GetAttributeU32ArrayPtr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeU32Array"));
  function_pointers_.GetAttributeU64Array = reinterpret_cast<GetAttributeU64ArrayPtr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeU64Array"));
  function_pointers_.GetAttributeU8 = reinterpret_cast<GetAttributeU8Ptr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeU8"));
  function_pointers_.GetAttributeU8Array = reinterpret_cast<GetAttributeU8ArrayPtr>(shared_library_->get_function_pointer("RFmxNR_GetAttributeU8Array"));
  function_pointers_.GetError = reinterpret_cast<GetErrorPtr>(shared_library_->get_function_pointer("RFmxNR_GetError"));
  function_pointers_.GetErrorString = reinterpret_cast<GetErrorStringPtr>(shared_library_->get_function_pointer("RFmxNR_GetErrorString"));
  function_pointers_.Initialize = reinterpret_cast<InitializePtr>(shared_library_->get_function_pointer("RFmxNR_Initialize"));
  function_pointers_.InitializeFromNIRFSASession = reinterpret_cast<InitializeFromNIRFSASessionPtr>(shared_library_->get_function_pointer("RFmxNR_InitializeFromNIRFSASession"));
  function_pointers_.Initiate = reinterpret_cast<InitiatePtr>(shared_library_->get_function_pointer("RFmxNR_Initiate"));
  function_pointers_.LoadFromGenerationConfigurationFile = reinterpret_cast<LoadFromGenerationConfigurationFilePtr>(shared_library_->get_function_pointer("RFmxNR_LoadFromGenerationConfigurationFile"));
  function_pointers_.ModAccAutoLevel = reinterpret_cast<ModAccAutoLevelPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccAutoLevel"));
  function_pointers_.ModAccCfgMeasurementMode = reinterpret_cast<ModAccCfgMeasurementModePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccCfgMeasurementMode"));
  function_pointers_.ModAccCfgNoiseCompensationEnabled = reinterpret_cast<ModAccCfgNoiseCompensationEnabledPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccCfgNoiseCompensationEnabled"));
  function_pointers_.ModAccCfgReferenceWaveform = reinterpret_cast<ModAccCfgReferenceWaveformPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccCfgReferenceWaveform"));
  function_pointers_.ModAccCfgReferenceWaveformInterleavedIQ = reinterpret_cast<ModAccCfgReferenceWaveformInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccCfgReferenceWaveform"));
  function_pointers_.ModAccCfgReferenceWaveformSplit = reinterpret_cast<ModAccCfgReferenceWaveformSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccCfgReferenceWaveformSplit"));
  function_pointers_.ModAccClearNoiseCalibrationDatabase = reinterpret_cast<ModAccClearNoiseCalibrationDatabasePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccClearNoiseCalibrationDatabase"));
  function_pointers_.ModAccFetchCompositeEVM = reinterpret_cast<ModAccFetchCompositeEVMPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchCompositeEVM"));
  function_pointers_.ModAccFetchFrequencyErrorMean = reinterpret_cast<ModAccFetchFrequencyErrorMeanPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchFrequencyErrorMean"));
  function_pointers_.ModAccFetchFrequencyErrorPerSlotMaximumTrace = reinterpret_cast<ModAccFetchFrequencyErrorPerSlotMaximumTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchFrequencyErrorPerSlotMaximumTrace"));
  function_pointers_.ModAccFetchIQGainImbalancePerSubcarrierMeanTrace = reinterpret_cast<ModAccFetchIQGainImbalancePerSubcarrierMeanTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchIQGainImbalancePerSubcarrierMeanTrace"));
  function_pointers_.ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace = reinterpret_cast<ModAccFetchIQQuadratureErrorPerSubcarrierMeanTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace"));
  function_pointers_.ModAccFetchInBandEmissionTrace = reinterpret_cast<ModAccFetchInBandEmissionTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchInBandEmissionTrace"));
  function_pointers_.ModAccFetchPBCHDMRSConstellationTrace = reinterpret_cast<ModAccFetchPBCHDMRSConstellationTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPBCHDMRSConstellationTrace"));
  function_pointers_.ModAccFetchPBCHDMRSConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchPBCHDMRSConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPBCHDMRSConstellationTrace"));
  function_pointers_.ModAccFetchPBCHDMRSConstellationTraceSplit = reinterpret_cast<ModAccFetchPBCHDMRSConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPBCHDMRSConstellationTraceSplit"));
  function_pointers_.ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace = reinterpret_cast<ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace"));
  function_pointers_.ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace = reinterpret_cast<ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace"));
  function_pointers_.ModAccFetchPBCHDataConstellationTrace = reinterpret_cast<ModAccFetchPBCHDataConstellationTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPBCHDataConstellationTrace"));
  function_pointers_.ModAccFetchPBCHDataConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchPBCHDataConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPBCHDataConstellationTrace"));
  function_pointers_.ModAccFetchPBCHDataConstellationTraceSplit = reinterpret_cast<ModAccFetchPBCHDataConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPBCHDataConstellationTraceSplit"));
  function_pointers_.ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTrace = reinterpret_cast<ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTrace"));
  function_pointers_.ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace = reinterpret_cast<ModAccFetchPBCHDataRMSEVMPerSymbolMeanTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace"));
  function_pointers_.ModAccFetchPDSCH1024QAMConstellationTrace = reinterpret_cast<ModAccFetchPDSCH1024QAMConstellationTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH1024QAMConstellationTrace"));
  function_pointers_.ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH1024QAMConstellationTrace"));
  function_pointers_.ModAccFetchPDSCH1024QAMConstellationTraceSplit = reinterpret_cast<ModAccFetchPDSCH1024QAMConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH1024QAMConstellationTraceSplit"));
  function_pointers_.ModAccFetchPDSCH16QAMConstellationTrace = reinterpret_cast<ModAccFetchPDSCH16QAMConstellationTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH16QAMConstellationTrace"));
  function_pointers_.ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH16QAMConstellationTrace"));
  function_pointers_.ModAccFetchPDSCH16QAMConstellationTraceSplit = reinterpret_cast<ModAccFetchPDSCH16QAMConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH16QAMConstellationTraceSplit"));
  function_pointers_.ModAccFetchPDSCH256QAMConstellationTrace = reinterpret_cast<ModAccFetchPDSCH256QAMConstellationTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH256QAMConstellationTrace"));
  function_pointers_.ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH256QAMConstellationTrace"));
  function_pointers_.ModAccFetchPDSCH256QAMConstellationTraceSplit = reinterpret_cast<ModAccFetchPDSCH256QAMConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH256QAMConstellationTraceSplit"));
  function_pointers_.ModAccFetchPDSCH4096QAMConstellationTrace = reinterpret_cast<ModAccFetchPDSCH4096QAMConstellationTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH4096QAMConstellationTrace"));
  function_pointers_.ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH4096QAMConstellationTrace"));
  function_pointers_.ModAccFetchPDSCH4096QAMConstellationTraceSplit = reinterpret_cast<ModAccFetchPDSCH4096QAMConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH4096QAMConstellationTraceSplit"));
  function_pointers_.ModAccFetchPDSCH64QAMConstellationTrace = reinterpret_cast<ModAccFetchPDSCH64QAMConstellationTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH64QAMConstellationTrace"));
  function_pointers_.ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH64QAMConstellationTrace"));
  function_pointers_.ModAccFetchPDSCH64QAMConstellationTraceSplit = reinterpret_cast<ModAccFetchPDSCH64QAMConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH64QAMConstellationTraceSplit"));
  function_pointers_.ModAccFetchPDSCH8PSKConstellationTrace = reinterpret_cast<ModAccFetchPDSCH8PSKConstellationTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH8PSKConstellationTrace"));
  function_pointers_.ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH8PSKConstellationTrace"));
  function_pointers_.ModAccFetchPDSCH8PSKConstellationTraceSplit = reinterpret_cast<ModAccFetchPDSCH8PSKConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCH8PSKConstellationTraceSplit"));
  function_pointers_.ModAccFetchPDSCHDMRSConstellationTrace = reinterpret_cast<ModAccFetchPDSCHDMRSConstellationTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCHDMRSConstellationTrace"));
  function_pointers_.ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCHDMRSConstellationTrace"));
  function_pointers_.ModAccFetchPDSCHDMRSConstellationTraceSplit = reinterpret_cast<ModAccFetchPDSCHDMRSConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCHDMRSConstellationTraceSplit"));
  function_pointers_.ModAccFetchPDSCHDataConstellationTrace = reinterpret_cast<ModAccFetchPDSCHDataConstellationTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCHDataConstellationTrace"));
  function_pointers_.ModAccFetchPDSCHDataConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchPDSCHDataConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCHDataConstellationTrace"));
  function_pointers_.ModAccFetchPDSCHDataConstellationTraceSplit = reinterpret_cast<ModAccFetchPDSCHDataConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCHDataConstellationTraceSplit"));
  function_pointers_.ModAccFetchPDSCHDemodulatedBits = reinterpret_cast<ModAccFetchPDSCHDemodulatedBitsPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCHDemodulatedBits"));
  function_pointers_.ModAccFetchPDSCHPTRSConstellationTrace = reinterpret_cast<ModAccFetchPDSCHPTRSConstellationTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCHPTRSConstellationTrace"));
  function_pointers_.ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCHPTRSConstellationTrace"));
  function_pointers_.ModAccFetchPDSCHPTRSConstellationTraceSplit = reinterpret_cast<ModAccFetchPDSCHPTRSConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCHPTRSConstellationTraceSplit"));
  function_pointers_.ModAccFetchPDSCHQPSKConstellationTrace = reinterpret_cast<ModAccFetchPDSCHQPSKConstellationTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCHQPSKConstellationTrace"));
  function_pointers_.ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCHQPSKConstellationTrace"));
  function_pointers_.ModAccFetchPDSCHQPSKConstellationTraceSplit = reinterpret_cast<ModAccFetchPDSCHQPSKConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPDSCHQPSKConstellationTraceSplit"));
  function_pointers_.ModAccFetchPSSConstellationTrace = reinterpret_cast<ModAccFetchPSSConstellationTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPSSConstellationTrace"));
  function_pointers_.ModAccFetchPSSConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchPSSConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPSSConstellationTrace"));
  function_pointers_.ModAccFetchPSSConstellationTraceSplit = reinterpret_cast<ModAccFetchPSSConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPSSConstellationTraceSplit"));
  function_pointers_.ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace = reinterpret_cast<ModAccFetchPSSRMSEVMPerSubcarrierMeanTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace"));
  function_pointers_.ModAccFetchPSSRMSEVMPerSymbolMeanTrace = reinterpret_cast<ModAccFetchPSSRMSEVMPerSymbolMeanTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPSSRMSEVMPerSymbolMeanTrace"));
  function_pointers_.ModAccFetchPUSCHDMRSConstellationTrace = reinterpret_cast<ModAccFetchPUSCHDMRSConstellationTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPUSCHDMRSConstellationTrace"));
  function_pointers_.ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPUSCHDMRSConstellationTrace"));
  function_pointers_.ModAccFetchPUSCHDMRSConstellationTraceSplit = reinterpret_cast<ModAccFetchPUSCHDMRSConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPUSCHDMRSConstellationTraceSplit"));
  function_pointers_.ModAccFetchPUSCHDataConstellationTrace = reinterpret_cast<ModAccFetchPUSCHDataConstellationTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPUSCHDataConstellationTrace"));
  function_pointers_.ModAccFetchPUSCHDataConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchPUSCHDataConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPUSCHDataConstellationTrace"));
  function_pointers_.ModAccFetchPUSCHDataConstellationTraceSplit = reinterpret_cast<ModAccFetchPUSCHDataConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPUSCHDataConstellationTraceSplit"));
  function_pointers_.ModAccFetchPUSCHDemodulatedBits = reinterpret_cast<ModAccFetchPUSCHDemodulatedBitsPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPUSCHDemodulatedBits"));
  function_pointers_.ModAccFetchPUSCHPTRSConstellationTrace = reinterpret_cast<ModAccFetchPUSCHPTRSConstellationTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPUSCHPTRSConstellationTrace"));
  function_pointers_.ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPUSCHPTRSConstellationTrace"));
  function_pointers_.ModAccFetchPUSCHPTRSConstellationTraceSplit = reinterpret_cast<ModAccFetchPUSCHPTRSConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPUSCHPTRSConstellationTraceSplit"));
  function_pointers_.ModAccFetchPUSCHPhaseOffsetTrace = reinterpret_cast<ModAccFetchPUSCHPhaseOffsetTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPUSCHPhaseOffsetTrace"));
  function_pointers_.ModAccFetchPeakEVMHighPerSymbolMaximumTrace = reinterpret_cast<ModAccFetchPeakEVMHighPerSymbolMaximumTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPeakEVMHighPerSymbolMaximumTrace"));
  function_pointers_.ModAccFetchPeakEVMLowPerSymbolMaximumTrace = reinterpret_cast<ModAccFetchPeakEVMLowPerSymbolMaximumTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPeakEVMLowPerSymbolMaximumTrace"));
  function_pointers_.ModAccFetchPeakEVMPerSlotMaximumTrace = reinterpret_cast<ModAccFetchPeakEVMPerSlotMaximumTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPeakEVMPerSlotMaximumTrace"));
  function_pointers_.ModAccFetchPeakEVMPerSubcarrierMaximumTrace = reinterpret_cast<ModAccFetchPeakEVMPerSubcarrierMaximumTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPeakEVMPerSubcarrierMaximumTrace"));
  function_pointers_.ModAccFetchPeakEVMPerSymbolMaximumTrace = reinterpret_cast<ModAccFetchPeakEVMPerSymbolMaximumTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchPeakEVMPerSymbolMaximumTrace"));
  function_pointers_.ModAccFetchRMSEVMHighPerSymbolMeanTrace = reinterpret_cast<ModAccFetchRMSEVMHighPerSymbolMeanTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchRMSEVMHighPerSymbolMeanTrace"));
  function_pointers_.ModAccFetchRMSEVMLowPerSymbolMeanTrace = reinterpret_cast<ModAccFetchRMSEVMLowPerSymbolMeanTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchRMSEVMLowPerSymbolMeanTrace"));
  function_pointers_.ModAccFetchRMSEVMPerSlotMeanTrace = reinterpret_cast<ModAccFetchRMSEVMPerSlotMeanTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchRMSEVMPerSlotMeanTrace"));
  function_pointers_.ModAccFetchRMSEVMPerSubcarrierMeanTrace = reinterpret_cast<ModAccFetchRMSEVMPerSubcarrierMeanTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchRMSEVMPerSubcarrierMeanTrace"));
  function_pointers_.ModAccFetchRMSEVMPerSymbolMeanTrace = reinterpret_cast<ModAccFetchRMSEVMPerSymbolMeanTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchRMSEVMPerSymbolMeanTrace"));
  function_pointers_.ModAccFetchSSSConstellationTrace = reinterpret_cast<ModAccFetchSSSConstellationTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchSSSConstellationTrace"));
  function_pointers_.ModAccFetchSSSConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchSSSConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchSSSConstellationTrace"));
  function_pointers_.ModAccFetchSSSConstellationTraceSplit = reinterpret_cast<ModAccFetchSSSConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchSSSConstellationTraceSplit"));
  function_pointers_.ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace = reinterpret_cast<ModAccFetchSSSRMSEVMPerSubcarrierMeanTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace"));
  function_pointers_.ModAccFetchSSSRMSEVMPerSymbolMeanTrace = reinterpret_cast<ModAccFetchSSSRMSEVMPerSymbolMeanTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchSSSRMSEVMPerSymbolMeanTrace"));
  function_pointers_.ModAccFetchSpectralFlatnessTrace = reinterpret_cast<ModAccFetchSpectralFlatnessTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchSpectralFlatnessTrace"));
  function_pointers_.ModAccFetchSubblockInBandEmissionTrace = reinterpret_cast<ModAccFetchSubblockInBandEmissionTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchSubblockInBandEmissionTrace"));
  function_pointers_.ModAccFetchTransientPeriodLocationsTrace = reinterpret_cast<ModAccFetchTransientPeriodLocationsTracePtr>(shared_library_->get_function_pointer("RFmxNR_ModAccFetchTransientPeriodLocationsTrace"));
  function_pointers_.ModAccValidateCalibrationData = reinterpret_cast<ModAccValidateCalibrationDataPtr>(shared_library_->get_function_pointer("RFmxNR_ModAccValidateCalibrationData"));
  function_pointers_.OBWCfgAveraging = reinterpret_cast<OBWCfgAveragingPtr>(shared_library_->get_function_pointer("RFmxNR_OBWCfgAveraging"));
  function_pointers_.OBWCfgRBWFilter = reinterpret_cast<OBWCfgRBWFilterPtr>(shared_library_->get_function_pointer("RFmxNR_OBWCfgRBWFilter"));
  function_pointers_.OBWCfgSweepTime = reinterpret_cast<OBWCfgSweepTimePtr>(shared_library_->get_function_pointer("RFmxNR_OBWCfgSweepTime"));
  function_pointers_.OBWFetchMeasurement = reinterpret_cast<OBWFetchMeasurementPtr>(shared_library_->get_function_pointer("RFmxNR_OBWFetchMeasurement"));
  function_pointers_.OBWFetchSpectrum = reinterpret_cast<OBWFetchSpectrumPtr>(shared_library_->get_function_pointer("RFmxNR_OBWFetchSpectrum"));
  function_pointers_.PVTCfgAveraging = reinterpret_cast<PVTCfgAveragingPtr>(shared_library_->get_function_pointer("RFmxNR_PVTCfgAveraging"));
  function_pointers_.PVTCfgMeasurementMethod = reinterpret_cast<PVTCfgMeasurementMethodPtr>(shared_library_->get_function_pointer("RFmxNR_PVTCfgMeasurementMethod"));
  function_pointers_.PVTCfgOFFPowerExclusionPeriods = reinterpret_cast<PVTCfgOFFPowerExclusionPeriodsPtr>(shared_library_->get_function_pointer("RFmxNR_PVTCfgOFFPowerExclusionPeriods"));
  function_pointers_.PVTFetchMeasurement = reinterpret_cast<PVTFetchMeasurementPtr>(shared_library_->get_function_pointer("RFmxNR_PVTFetchMeasurement"));
  function_pointers_.PVTFetchMeasurementArray = reinterpret_cast<PVTFetchMeasurementArrayPtr>(shared_library_->get_function_pointer("RFmxNR_PVTFetchMeasurementArray"));
  function_pointers_.PVTFetchSignalPowerTrace = reinterpret_cast<PVTFetchSignalPowerTracePtr>(shared_library_->get_function_pointer("RFmxNR_PVTFetchSignalPowerTrace"));
  function_pointers_.PVTFetchWindowedSignalPowerTrace = reinterpret_cast<PVTFetchWindowedSignalPowerTracePtr>(shared_library_->get_function_pointer("RFmxNR_PVTFetchWindowedSignalPowerTrace"));
  function_pointers_.ResetAttribute = reinterpret_cast<ResetAttributePtr>(shared_library_->get_function_pointer("RFmxNR_ResetAttribute"));
  function_pointers_.ResetToDefault = reinterpret_cast<ResetToDefaultPtr>(shared_library_->get_function_pointer("RFmxNR_ResetToDefault"));
  function_pointers_.SEMCfgAveraging = reinterpret_cast<SEMCfgAveragingPtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgAveraging"));
  function_pointers_.SEMCfgComponentCarrierRatedOutputPower = reinterpret_cast<SEMCfgComponentCarrierRatedOutputPowerPtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgComponentCarrierRatedOutputPower"));
  function_pointers_.SEMCfgComponentCarrierRatedOutputPowerArray = reinterpret_cast<SEMCfgComponentCarrierRatedOutputPowerArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgComponentCarrierRatedOutputPowerArray"));
  function_pointers_.SEMCfgNumberOfOffsets = reinterpret_cast<SEMCfgNumberOfOffsetsPtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgNumberOfOffsets"));
  function_pointers_.SEMCfgOffsetAbsoluteLimit = reinterpret_cast<SEMCfgOffsetAbsoluteLimitPtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgOffsetAbsoluteLimit"));
  function_pointers_.SEMCfgOffsetAbsoluteLimitArray = reinterpret_cast<SEMCfgOffsetAbsoluteLimitArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgOffsetAbsoluteLimitArray"));
  function_pointers_.SEMCfgOffsetBandwidthIntegral = reinterpret_cast<SEMCfgOffsetBandwidthIntegralPtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgOffsetBandwidthIntegral"));
  function_pointers_.SEMCfgOffsetBandwidthIntegralArray = reinterpret_cast<SEMCfgOffsetBandwidthIntegralArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgOffsetBandwidthIntegralArray"));
  function_pointers_.SEMCfgOffsetFrequency = reinterpret_cast<SEMCfgOffsetFrequencyPtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgOffsetFrequency"));
  function_pointers_.SEMCfgOffsetFrequencyArray = reinterpret_cast<SEMCfgOffsetFrequencyArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgOffsetFrequencyArray"));
  function_pointers_.SEMCfgOffsetLimitFailMask = reinterpret_cast<SEMCfgOffsetLimitFailMaskPtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgOffsetLimitFailMask"));
  function_pointers_.SEMCfgOffsetLimitFailMaskArray = reinterpret_cast<SEMCfgOffsetLimitFailMaskArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgOffsetLimitFailMaskArray"));
  function_pointers_.SEMCfgOffsetRBWFilter = reinterpret_cast<SEMCfgOffsetRBWFilterPtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgOffsetRBWFilter"));
  function_pointers_.SEMCfgOffsetRBWFilterArray = reinterpret_cast<SEMCfgOffsetRBWFilterArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgOffsetRBWFilterArray"));
  function_pointers_.SEMCfgOffsetRelativeLimit = reinterpret_cast<SEMCfgOffsetRelativeLimitPtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgOffsetRelativeLimit"));
  function_pointers_.SEMCfgOffsetRelativeLimitArray = reinterpret_cast<SEMCfgOffsetRelativeLimitArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgOffsetRelativeLimitArray"));
  function_pointers_.SEMCfgSweepTime = reinterpret_cast<SEMCfgSweepTimePtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgSweepTime"));
  function_pointers_.SEMCfgUplinkMaskType = reinterpret_cast<SEMCfgUplinkMaskTypePtr>(shared_library_->get_function_pointer("RFmxNR_SEMCfgUplinkMaskType"));
  function_pointers_.SEMFetchComponentCarrierMeasurement = reinterpret_cast<SEMFetchComponentCarrierMeasurementPtr>(shared_library_->get_function_pointer("RFmxNR_SEMFetchComponentCarrierMeasurement"));
  function_pointers_.SEMFetchComponentCarrierMeasurementArray = reinterpret_cast<SEMFetchComponentCarrierMeasurementArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SEMFetchComponentCarrierMeasurementArray"));
  function_pointers_.SEMFetchLowerOffsetMargin = reinterpret_cast<SEMFetchLowerOffsetMarginPtr>(shared_library_->get_function_pointer("RFmxNR_SEMFetchLowerOffsetMargin"));
  function_pointers_.SEMFetchLowerOffsetMarginArray = reinterpret_cast<SEMFetchLowerOffsetMarginArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SEMFetchLowerOffsetMarginArray"));
  function_pointers_.SEMFetchLowerOffsetPower = reinterpret_cast<SEMFetchLowerOffsetPowerPtr>(shared_library_->get_function_pointer("RFmxNR_SEMFetchLowerOffsetPower"));
  function_pointers_.SEMFetchLowerOffsetPowerArray = reinterpret_cast<SEMFetchLowerOffsetPowerArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SEMFetchLowerOffsetPowerArray"));
  function_pointers_.SEMFetchMeasurementStatus = reinterpret_cast<SEMFetchMeasurementStatusPtr>(shared_library_->get_function_pointer("RFmxNR_SEMFetchMeasurementStatus"));
  function_pointers_.SEMFetchSpectrum = reinterpret_cast<SEMFetchSpectrumPtr>(shared_library_->get_function_pointer("RFmxNR_SEMFetchSpectrum"));
  function_pointers_.SEMFetchSubblockMeasurement = reinterpret_cast<SEMFetchSubblockMeasurementPtr>(shared_library_->get_function_pointer("RFmxNR_SEMFetchSubblockMeasurement"));
  function_pointers_.SEMFetchTotalAggregatedPower = reinterpret_cast<SEMFetchTotalAggregatedPowerPtr>(shared_library_->get_function_pointer("RFmxNR_SEMFetchTotalAggregatedPower"));
  function_pointers_.SEMFetchUpperOffsetMargin = reinterpret_cast<SEMFetchUpperOffsetMarginPtr>(shared_library_->get_function_pointer("RFmxNR_SEMFetchUpperOffsetMargin"));
  function_pointers_.SEMFetchUpperOffsetMarginArray = reinterpret_cast<SEMFetchUpperOffsetMarginArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SEMFetchUpperOffsetMarginArray"));
  function_pointers_.SEMFetchUpperOffsetPower = reinterpret_cast<SEMFetchUpperOffsetPowerPtr>(shared_library_->get_function_pointer("RFmxNR_SEMFetchUpperOffsetPower"));
  function_pointers_.SEMFetchUpperOffsetPowerArray = reinterpret_cast<SEMFetchUpperOffsetPowerArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SEMFetchUpperOffsetPowerArray"));
  function_pointers_.SelectMeasurements = reinterpret_cast<SelectMeasurementsPtr>(shared_library_->get_function_pointer("RFmxNR_SelectMeasurements"));
  function_pointers_.SendSoftwareEdgeTrigger = reinterpret_cast<SendSoftwareEdgeTriggerPtr>(shared_library_->get_function_pointer("RFmxNR_SendSoftwareEdgeTrigger"));
  function_pointers_.SetAttributeF32 = reinterpret_cast<SetAttributeF32Ptr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeF32"));
  function_pointers_.SetAttributeF32Array = reinterpret_cast<SetAttributeF32ArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeF32Array"));
  function_pointers_.SetAttributeF64 = reinterpret_cast<SetAttributeF64Ptr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeF64"));
  function_pointers_.SetAttributeF64Array = reinterpret_cast<SetAttributeF64ArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeF64Array"));
  function_pointers_.SetAttributeI16 = reinterpret_cast<SetAttributeI16Ptr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeI16"));
  function_pointers_.SetAttributeI32 = reinterpret_cast<SetAttributeI32Ptr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeI32"));
  function_pointers_.SetAttributeI32Array = reinterpret_cast<SetAttributeI32ArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeI32Array"));
  function_pointers_.SetAttributeI64 = reinterpret_cast<SetAttributeI64Ptr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeI64"));
  function_pointers_.SetAttributeI64Array = reinterpret_cast<SetAttributeI64ArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeI64Array"));
  function_pointers_.SetAttributeI8 = reinterpret_cast<SetAttributeI8Ptr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeI8"));
  function_pointers_.SetAttributeI8Array = reinterpret_cast<SetAttributeI8ArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeI8Array"));
  function_pointers_.SetAttributeNIComplexDoubleArray = reinterpret_cast<SetAttributeNIComplexDoubleArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeNIComplexDoubleArray"));
  function_pointers_.SetAttributeNIComplexSingleArray = reinterpret_cast<SetAttributeNIComplexSingleArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeNIComplexSingleArray"));
  function_pointers_.SetAttributeString = reinterpret_cast<SetAttributeStringPtr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeString"));
  function_pointers_.SetAttributeU16 = reinterpret_cast<SetAttributeU16Ptr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeU16"));
  function_pointers_.SetAttributeU32 = reinterpret_cast<SetAttributeU32Ptr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeU32"));
  function_pointers_.SetAttributeU32Array = reinterpret_cast<SetAttributeU32ArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeU32Array"));
  function_pointers_.SetAttributeU64Array = reinterpret_cast<SetAttributeU64ArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeU64Array"));
  function_pointers_.SetAttributeU8 = reinterpret_cast<SetAttributeU8Ptr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeU8"));
  function_pointers_.SetAttributeU8Array = reinterpret_cast<SetAttributeU8ArrayPtr>(shared_library_->get_function_pointer("RFmxNR_SetAttributeU8Array"));
  function_pointers_.TXPFetchMeasurement = reinterpret_cast<TXPFetchMeasurementPtr>(shared_library_->get_function_pointer("RFmxNR_TXPFetchMeasurement"));
  function_pointers_.TXPFetchPowerTrace = reinterpret_cast<TXPFetchPowerTracePtr>(shared_library_->get_function_pointer("RFmxNR_TXPFetchPowerTrace"));
  function_pointers_.WaitForAcquisitionComplete = reinterpret_cast<WaitForAcquisitionCompletePtr>(shared_library_->get_function_pointer("RFmxNR_WaitForAcquisitionComplete"));
  function_pointers_.WaitForMeasurementComplete = reinterpret_cast<WaitForMeasurementCompletePtr>(shared_library_->get_function_pointer("RFmxNR_WaitForMeasurementComplete"));
}

NiRFmxNRLibrary::~NiRFmxNRLibrary()
{
}

::grpc::Status NiRFmxNRLibrary::check_function_exists(std::string functionName)
{
  return shared_library_->function_exists(functionName.c_str())
    ? ::grpc::Status::OK
    : ::grpc::Status(::grpc::NOT_FOUND, "Could not find the function " + functionName);
}

int32 NiRFmxNRLibrary::ACPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  if (!function_pointers_.ACPCfgAveraging) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPCfgAveraging.");
  }
  return function_pointers_.ACPCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 NiRFmxNRLibrary::ACPCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)
{
  if (!function_pointers_.ACPCfgMeasurementMethod) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPCfgMeasurementMethod.");
  }
  return function_pointers_.ACPCfgMeasurementMethod(instrumentHandle, selectorString, measurementMethod);
}

int32 NiRFmxNRLibrary::ACPCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled)
{
  if (!function_pointers_.ACPCfgNoiseCompensationEnabled) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPCfgNoiseCompensationEnabled.");
  }
  return function_pointers_.ACPCfgNoiseCompensationEnabled(instrumentHandle, selectorString, noiseCompensationEnabled);
}

int32 NiRFmxNRLibrary::ACPCfgNumberOfENDCOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfENDCOffsets)
{
  if (!function_pointers_.ACPCfgNumberOfENDCOffsets) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPCfgNumberOfENDCOffsets.");
  }
  return function_pointers_.ACPCfgNumberOfENDCOffsets(instrumentHandle, selectorString, numberOfENDCOffsets);
}

int32 NiRFmxNRLibrary::ACPCfgNumberOfEUTRAOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfEUTRAOffsets)
{
  if (!function_pointers_.ACPCfgNumberOfEUTRAOffsets) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPCfgNumberOfEUTRAOffsets.");
  }
  return function_pointers_.ACPCfgNumberOfEUTRAOffsets(instrumentHandle, selectorString, numberOfEUTRAOffsets);
}

int32 NiRFmxNRLibrary::ACPCfgNumberOfNROffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfNROffsets)
{
  if (!function_pointers_.ACPCfgNumberOfNROffsets) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPCfgNumberOfNROffsets.");
  }
  return function_pointers_.ACPCfgNumberOfNROffsets(instrumentHandle, selectorString, numberOfNROffsets);
}

int32 NiRFmxNRLibrary::ACPCfgNumberOfUTRAOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfUTRAOffsets)
{
  if (!function_pointers_.ACPCfgNumberOfUTRAOffsets) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPCfgNumberOfUTRAOffsets.");
  }
  return function_pointers_.ACPCfgNumberOfUTRAOffsets(instrumentHandle, selectorString, numberOfUTRAOffsets);
}

int32 NiRFmxNRLibrary::ACPCfgPowerUnits(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnits)
{
  if (!function_pointers_.ACPCfgPowerUnits) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPCfgPowerUnits.");
  }
  return function_pointers_.ACPCfgPowerUnits(instrumentHandle, selectorString, powerUnits);
}

int32 NiRFmxNRLibrary::ACPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)
{
  if (!function_pointers_.ACPCfgRBWFilter) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPCfgRBWFilter.");
  }
  return function_pointers_.ACPCfgRBWFilter(instrumentHandle, selectorString, rbwAuto, rbw, rbwFilterType);
}

int32 NiRFmxNRLibrary::ACPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)
{
  if (!function_pointers_.ACPCfgSweepTime) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPCfgSweepTime.");
  }
  return function_pointers_.ACPCfgSweepTime(instrumentHandle, selectorString, sweepTimeAuto, sweepTimeInterval);
}

int32 NiRFmxNRLibrary::ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 absolutePowersTrace[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ACPFetchAbsolutePowersTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPFetchAbsolutePowersTrace.");
  }
  return function_pointers_.ACPFetchAbsolutePowersTrace(instrumentHandle, selectorString, timeout, traceIndex, x0, dx, absolutePowersTrace, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ACPFetchComponentCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absolutePower, float64* relativePower)
{
  if (!function_pointers_.ACPFetchComponentCarrierMeasurement) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPFetchComponentCarrierMeasurement.");
  }
  return function_pointers_.ACPFetchComponentCarrierMeasurement(instrumentHandle, selectorString, timeout, absolutePower, relativePower);
}

int32 NiRFmxNRLibrary::ACPFetchComponentCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 relativePower[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ACPFetchComponentCarrierMeasurementArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPFetchComponentCarrierMeasurementArray.");
  }
  return function_pointers_.ACPFetchComponentCarrierMeasurementArray(instrumentHandle, selectorString, timeout, absolutePower, relativePower, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* lowerRelativePower, float64* upperRelativePower, float64* lowerAbsolutePower, float64* upperAbsolutePower)
{
  if (!function_pointers_.ACPFetchOffsetMeasurement) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPFetchOffsetMeasurement.");
  }
  return function_pointers_.ACPFetchOffsetMeasurement(instrumentHandle, selectorString, timeout, lowerRelativePower, upperRelativePower, lowerAbsolutePower, upperAbsolutePower);
}

int32 NiRFmxNRLibrary::ACPFetchOffsetMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 lowerRelativePower[], float64 upperRelativePower[], float64 lowerAbsolutePower[], float64 upperAbsolutePower[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ACPFetchOffsetMeasurementArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPFetchOffsetMeasurementArray.");
  }
  return function_pointers_.ACPFetchOffsetMeasurementArray(instrumentHandle, selectorString, timeout, lowerRelativePower, upperRelativePower, lowerAbsolutePower, upperAbsolutePower, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 relativePowersTrace[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ACPFetchRelativePowersTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPFetchRelativePowersTrace.");
  }
  return function_pointers_.ACPFetchRelativePowersTrace(instrumentHandle, selectorString, timeout, traceIndex, x0, dx, relativePowersTrace, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ACPFetchSpectrum) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPFetchSpectrum.");
  }
  return function_pointers_.ACPFetchSpectrum(instrumentHandle, selectorString, timeout, x0, dx, spectrum, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ACPFetchSubblockMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* subblockPower, float64* integrationBandwidth, float64* frequency)
{
  if (!function_pointers_.ACPFetchSubblockMeasurement) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPFetchSubblockMeasurement.");
  }
  return function_pointers_.ACPFetchSubblockMeasurement(instrumentHandle, selectorString, timeout, subblockPower, integrationBandwidth, frequency);
}

int32 NiRFmxNRLibrary::ACPFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAggregatedPower)
{
  if (!function_pointers_.ACPFetchTotalAggregatedPower) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPFetchTotalAggregatedPower.");
  }
  return function_pointers_.ACPFetchTotalAggregatedPower(instrumentHandle, selectorString, timeout, totalAggregatedPower);
}

int32 NiRFmxNRLibrary::ACPValidateNoiseCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* noiseCalibrationDataValid)
{
  if (!function_pointers_.ACPValidateNoiseCalibrationData) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ACPValidateNoiseCalibrationData.");
  }
  return function_pointers_.ACPValidateNoiseCalibrationData(instrumentHandle, selectorString, noiseCalibrationDataValid);
}

int32 NiRFmxNRLibrary::AbortMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  if (!function_pointers_.AbortMeasurements) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_AbortMeasurements.");
  }
  return function_pointers_.AbortMeasurements(instrumentHandle, selectorString);
}

int32 NiRFmxNRLibrary::AnalyzeIQ1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved)
{
  if (!function_pointers_.AnalyzeIQ1Waveform) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_AnalyzeIQ1Waveform.");
  }
  return function_pointers_.AnalyzeIQ1Waveform(instrumentHandle, selectorString, resultName, x0, dx, iq, arraySize, reset, reserved);
}

int32 NiRFmxNRLibrary::AnalyzeIQ1WaveformInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iq[], int32 arraySize, int32 reset, int64 reserved)
{
  if (!function_pointers_.AnalyzeIQ1WaveformInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_AnalyzeIQ1Waveform.");
  }
  return function_pointers_.AnalyzeIQ1WaveformInterleavedIQ(instrumentHandle, selectorString, resultName, x0, dx, reinterpret_cast<NIComplexSingle*>(iq), arraySize/2, reset, reserved);
}

int32 NiRFmxNRLibrary::AnalyzeIQ1WaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iqi[], float32 iqq[], int32 arraySize, int32 reset, int64 reserved)
{
  if (!function_pointers_.AnalyzeIQ1WaveformSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_AnalyzeIQ1WaveformSplit.");
  }
  return function_pointers_.AnalyzeIQ1WaveformSplit(instrumentHandle, selectorString, resultName, x0, dx, iqi, iqq, arraySize, reset, reserved);
}

int32 NiRFmxNRLibrary::AnalyzeNWaveformsIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], NIComplexSingle iq[], int32 iqSize[], int32 arraySize, int32 reset)
{
  if (!function_pointers_.AnalyzeNWaveformsIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_AnalyzeNWaveformsIQ.");
  }
  return function_pointers_.AnalyzeNWaveformsIQ(instrumentHandle, selectorString, resultName, x0, dx, iq, iqSize, arraySize, reset);
}

int32 NiRFmxNRLibrary::AnalyzeNWaveformsIQInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], float32 iq[], int32 iqSize[], int32 arraySize, int32 reset)
{
  if (!function_pointers_.AnalyzeNWaveformsIQInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_AnalyzeNWaveformsIQ.");
  }
  return function_pointers_.AnalyzeNWaveformsIQInterleavedIQ(instrumentHandle, selectorString, resultName, x0, dx, reinterpret_cast<NIComplexSingle*>(iq), iqSize, arraySize/2, reset);
}

int32 NiRFmxNRLibrary::AnalyzeNWaveformsIQSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], float32 iqi[], float32 iqq[], int32 iqSize[], int32 arraySize, int32 reset)
{
  if (!function_pointers_.AnalyzeNWaveformsIQSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_AnalyzeNWaveformsIQSplit.");
  }
  return function_pointers_.AnalyzeNWaveformsIQSplit(instrumentHandle, selectorString, resultName, x0, dx, iqi, iqq, iqSize, arraySize, reset);
}

int32 NiRFmxNRLibrary::AnalyzeNWaveformsSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], float32 spectrum[], int32 spectrumSize[], int32 arraySize, int32 reset)
{
  if (!function_pointers_.AnalyzeNWaveformsSpectrum) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_AnalyzeNWaveformsSpectrum.");
  }
  return function_pointers_.AnalyzeNWaveformsSpectrum(instrumentHandle, selectorString, resultName, x0, dx, spectrum, spectrumSize, arraySize, reset);
}

int32 NiRFmxNRLibrary::AnalyzeSpectrum1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 spectrum[], int32 arraySize, int32 reset, int64 reserved)
{
  if (!function_pointers_.AnalyzeSpectrum1Waveform) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_AnalyzeSpectrum1Waveform.");
  }
  return function_pointers_.AnalyzeSpectrum1Waveform(instrumentHandle, selectorString, resultName, x0, dx, spectrum, arraySize, reset, reserved);
}

int32 NiRFmxNRLibrary::AutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval, float64* referenceLevel)
{
  if (!function_pointers_.AutoLevel) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_AutoLevel.");
  }
  return function_pointers_.AutoLevel(instrumentHandle, selectorString, measurementInterval, referenceLevel);
}

int32 NiRFmxNRLibrary::BuildBandwidthPartString(char selectorString[], int32 bandwidthPartNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  if (!function_pointers_.BuildBandwidthPartString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_BuildBandwidthPartString.");
  }
  return function_pointers_.BuildBandwidthPartString(selectorString, bandwidthPartNumber, selectorStringOutLength, selectorStringOut);
}

int32 NiRFmxNRLibrary::BuildCORESETClusterString(char selectorString[], int32 coresetClusterNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  if (!function_pointers_.BuildCORESETClusterString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_BuildCORESETClusterString.");
  }
  return function_pointers_.BuildCORESETClusterString(selectorString, coresetClusterNumber, selectorStringOutLength, selectorStringOut);
}

int32 NiRFmxNRLibrary::BuildCORESETString(char selectorString[], int32 coresetNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  if (!function_pointers_.BuildCORESETString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_BuildCORESETString.");
  }
  return function_pointers_.BuildCORESETString(selectorString, coresetNumber, selectorStringOutLength, selectorStringOut);
}

int32 NiRFmxNRLibrary::BuildCarrierString(char selectorString[], int32 carrierNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  if (!function_pointers_.BuildCarrierString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_BuildCarrierString.");
  }
  return function_pointers_.BuildCarrierString(selectorString, carrierNumber, selectorStringOutLength, selectorStringOut);
}

int32 NiRFmxNRLibrary::BuildListStepString(char listName[], char resultName[], int32 stepNumber, int32 selectorStringLength, char selectorString[])
{
  if (!function_pointers_.BuildListStepString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_BuildListStepString.");
  }
  return function_pointers_.BuildListStepString(listName, resultName, stepNumber, selectorStringLength, selectorString);
}

int32 NiRFmxNRLibrary::BuildListString(char listName[], char resultName[], int32 selectorStringLength, char selectorString[])
{
  if (!function_pointers_.BuildListString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_BuildListString.");
  }
  return function_pointers_.BuildListString(listName, resultName, selectorStringLength, selectorString);
}

int32 NiRFmxNRLibrary::BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  if (!function_pointers_.BuildOffsetString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_BuildOffsetString.");
  }
  return function_pointers_.BuildOffsetString(selectorString, offsetNumber, selectorStringOutLength, selectorStringOut);
}

int32 NiRFmxNRLibrary::BuildPDCCHString(char selectorString[], int32 pdcchNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  if (!function_pointers_.BuildPDCCHString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_BuildPDCCHString.");
  }
  return function_pointers_.BuildPDCCHString(selectorString, pdcchNumber, selectorStringOutLength, selectorStringOut);
}

int32 NiRFmxNRLibrary::BuildPDSCHClusterString(char selectorString[], int32 pdschClusterNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  if (!function_pointers_.BuildPDSCHClusterString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_BuildPDSCHClusterString.");
  }
  return function_pointers_.BuildPDSCHClusterString(selectorString, pdschClusterNumber, selectorStringOutLength, selectorStringOut);
}

int32 NiRFmxNRLibrary::BuildPDSCHString(char selectorString[], int32 pdschNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  if (!function_pointers_.BuildPDSCHString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_BuildPDSCHString.");
  }
  return function_pointers_.BuildPDSCHString(selectorString, pdschNumber, selectorStringOutLength, selectorStringOut);
}

int32 NiRFmxNRLibrary::BuildPUSCHClusterString(char selectorString[], int32 puschClusterNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  if (!function_pointers_.BuildPUSCHClusterString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_BuildPUSCHClusterString.");
  }
  return function_pointers_.BuildPUSCHClusterString(selectorString, puschClusterNumber, selectorStringOutLength, selectorStringOut);
}

int32 NiRFmxNRLibrary::BuildPUSCHString(char selectorString[], int32 puschNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  if (!function_pointers_.BuildPUSCHString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_BuildPUSCHString.");
  }
  return function_pointers_.BuildPUSCHString(selectorString, puschNumber, selectorStringOutLength, selectorStringOut);
}

int32 NiRFmxNRLibrary::BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])
{
  if (!function_pointers_.BuildSignalString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_BuildSignalString.");
  }
  return function_pointers_.BuildSignalString(signalName, resultName, selectorStringLength, selectorString);
}

int32 NiRFmxNRLibrary::BuildSubblockString(char selectorString[], int32 subblockNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  if (!function_pointers_.BuildSubblockString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_BuildSubblockString.");
  }
  return function_pointers_.BuildSubblockString(selectorString, subblockNumber, selectorStringOutLength, selectorStringOut);
}

int32 NiRFmxNRLibrary::BuildUserString(char selectorString[], int32 userNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  if (!function_pointers_.BuildUserString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_BuildUserString.");
  }
  return function_pointers_.BuildUserString(selectorString, userNumber, selectorStringOutLength, selectorStringOut);
}

int32 NiRFmxNRLibrary::CHPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  if (!function_pointers_.CHPCfgAveraging) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CHPCfgAveraging.");
  }
  return function_pointers_.CHPCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 NiRFmxNRLibrary::CHPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)
{
  if (!function_pointers_.CHPCfgRBWFilter) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CHPCfgRBWFilter.");
  }
  return function_pointers_.CHPCfgRBWFilter(instrumentHandle, selectorString, rbwAuto, rbw, rbwFilterType);
}

int32 NiRFmxNRLibrary::CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)
{
  if (!function_pointers_.CHPCfgSweepTime) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CHPCfgSweepTime.");
  }
  return function_pointers_.CHPCfgSweepTime(instrumentHandle, selectorString, sweepTimeAuto, sweepTimeInterval);
}

int32 NiRFmxNRLibrary::CHPFetchComponentCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absolutePower, float64* relativePower)
{
  if (!function_pointers_.CHPFetchComponentCarrierMeasurement) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CHPFetchComponentCarrierMeasurement.");
  }
  return function_pointers_.CHPFetchComponentCarrierMeasurement(instrumentHandle, selectorString, timeout, absolutePower, relativePower);
}

int32 NiRFmxNRLibrary::CHPFetchComponentCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 relativePower[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.CHPFetchComponentCarrierMeasurementArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CHPFetchComponentCarrierMeasurementArray.");
  }
  return function_pointers_.CHPFetchComponentCarrierMeasurementArray(instrumentHandle, selectorString, timeout, absolutePower, relativePower, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::CHPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.CHPFetchSpectrum) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CHPFetchSpectrum.");
  }
  return function_pointers_.CHPFetchSpectrum(instrumentHandle, selectorString, timeout, x0, dx, spectrum, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::CHPFetchSubblockPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* subblockPower)
{
  if (!function_pointers_.CHPFetchSubblockPower) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CHPFetchSubblockPower.");
  }
  return function_pointers_.CHPFetchSubblockPower(instrumentHandle, selectorString, timeout, subblockPower);
}

int32 NiRFmxNRLibrary::CHPFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAggregatedPower)
{
  if (!function_pointers_.CHPFetchTotalAggregatedPower) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CHPFetchTotalAggregatedPower.");
  }
  return function_pointers_.CHPFetchTotalAggregatedPower(instrumentHandle, selectorString, timeout, totalAggregatedPower);
}

int32 NiRFmxNRLibrary::CHPValidateNoiseCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* noiseCalibrationDataValid)
{
  if (!function_pointers_.CHPValidateNoiseCalibrationData) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CHPValidateNoiseCalibrationData.");
  }
  return function_pointers_.CHPValidateNoiseCalibrationData(instrumentHandle, selectorString, noiseCalibrationDataValid);
}

int32 NiRFmxNRLibrary::CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger)
{
  if (!function_pointers_.CfgDigitalEdgeTrigger) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CfgDigitalEdgeTrigger.");
  }
  return function_pointers_.CfgDigitalEdgeTrigger(instrumentHandle, selectorString, digitalEdgeSource, digitalEdge, triggerDelay, enableTrigger);
}

int32 NiRFmxNRLibrary::CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation)
{
  if (!function_pointers_.CfgExternalAttenuation) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CfgExternalAttenuation.");
  }
  return function_pointers_.CfgExternalAttenuation(instrumentHandle, selectorString, externalAttenuation);
}

int32 NiRFmxNRLibrary::CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)
{
  if (!function_pointers_.CfgFrequency) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CfgFrequency.");
  }
  return function_pointers_.CfgFrequency(instrumentHandle, selectorString, centerFrequency);
}

int32 NiRFmxNRLibrary::CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)
{
  if (!function_pointers_.CfgFrequencyReference) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CfgFrequencyReference.");
  }
  return function_pointers_.CfgFrequencyReference(instrumentHandle, channelName, frequencyReferenceSource, frequencyReferenceFrequency);
}

int32 NiRFmxNRLibrary::CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdgeSlope, float64 iqPowerEdgeLevel, float64 triggerDelay, int32 triggerMinQuietTimeMode, float64 triggerMinQuietTimeDuration, int32 iqPowerEdgeLevelType, int32 enableTrigger)
{
  if (!function_pointers_.CfgIQPowerEdgeTrigger) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CfgIQPowerEdgeTrigger.");
  }
  return function_pointers_.CfgIQPowerEdgeTrigger(instrumentHandle, selectorString, iqPowerEdgeSource, iqPowerEdgeSlope, iqPowerEdgeLevel, triggerDelay, triggerMinQuietTimeMode, triggerMinQuietTimeDuration, iqPowerEdgeLevelType, enableTrigger);
}

int32 NiRFmxNRLibrary::CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)
{
  if (!function_pointers_.CfgMechanicalAttenuation) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CfgMechanicalAttenuation.");
  }
  return function_pointers_.CfgMechanicalAttenuation(instrumentHandle, channelName, mechanicalAttenuationAuto, mechanicalAttenuationValue);
}

int32 NiRFmxNRLibrary::CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation)
{
  if (!function_pointers_.CfgRF) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CfgRF.");
  }
  return function_pointers_.CfgRF(instrumentHandle, selectorString, centerFrequency, referenceLevel, externalAttenuation);
}

int32 NiRFmxNRLibrary::CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue)
{
  if (!function_pointers_.CfgRFAttenuation) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CfgRFAttenuation.");
  }
  return function_pointers_.CfgRFAttenuation(instrumentHandle, channelName, rfAttenuationAuto, rfAttenuationValue);
}

int32 NiRFmxNRLibrary::CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel)
{
  if (!function_pointers_.CfgReferenceLevel) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CfgReferenceLevel.");
  }
  return function_pointers_.CfgReferenceLevel(instrumentHandle, selectorString, referenceLevel);
}

int32 NiRFmxNRLibrary::CfgSelectedPortsMultiple(niRFmxInstrHandle instrumentHandle, char selectorString[], char selectedPorts[])
{
  if (!function_pointers_.CfgSelectedPortsMultiple) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CfgSelectedPortsMultiple.");
  }
  return function_pointers_.CfgSelectedPortsMultiple(instrumentHandle, selectorString, selectedPorts);
}

int32 NiRFmxNRLibrary::CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)
{
  if (!function_pointers_.CfgSoftwareEdgeTrigger) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CfgSoftwareEdgeTrigger.");
  }
  return function_pointers_.CfgSoftwareEdgeTrigger(instrumentHandle, selectorString, triggerDelay, enableTrigger);
}

int32 NiRFmxNRLibrary::CfggNodeBCategory(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 gNodeBCategory)
{
  if (!function_pointers_.CfggNodeBCategory) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CfggNodeBCategory.");
  }
  return function_pointers_.CfggNodeBCategory(instrumentHandle, selectorString, gNodeBCategory);
}

int32 NiRFmxNRLibrary::CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* isDone)
{
  if (!function_pointers_.CheckMeasurementStatus) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CheckMeasurementStatus.");
  }
  return function_pointers_.CheckMeasurementStatus(instrumentHandle, selectorString, isDone);
}

int32 NiRFmxNRLibrary::ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  if (!function_pointers_.ClearAllNamedResults) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ClearAllNamedResults.");
  }
  return function_pointers_.ClearAllNamedResults(instrumentHandle, selectorString);
}

int32 NiRFmxNRLibrary::ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  if (!function_pointers_.ClearNamedResult) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ClearNamedResult.");
  }
  return function_pointers_.ClearNamedResult(instrumentHandle, selectorString);
}

int32 NiRFmxNRLibrary::ClearNoiseCalibrationDatabase(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  if (!function_pointers_.ClearNoiseCalibrationDatabase) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ClearNoiseCalibrationDatabase.");
  }
  return function_pointers_.ClearNoiseCalibrationDatabase(instrumentHandle, selectorString);
}

int32 NiRFmxNRLibrary::CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[])
{
  if (!function_pointers_.CloneSignalConfiguration) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CloneSignalConfiguration.");
  }
  return function_pointers_.CloneSignalConfiguration(instrumentHandle, oldSignalName, newSignalName);
}

int32 NiRFmxNRLibrary::Close(niRFmxInstrHandle instrumentHandle, int32 forceDestroy)
{
  if (!function_pointers_.Close) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_Close.");
  }
  return function_pointers_.Close(instrumentHandle, forceDestroy);
}

int32 NiRFmxNRLibrary::Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  if (!function_pointers_.Commit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_Commit.");
  }
  return function_pointers_.Commit(instrumentHandle, selectorString);
}

int32 NiRFmxNRLibrary::CreateList(niRFmxInstrHandle instrumentHandle, char listName[])
{
  if (!function_pointers_.CreateList) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CreateList.");
  }
  return function_pointers_.CreateList(instrumentHandle, listName);
}

int32 NiRFmxNRLibrary::CreateListStep(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* createdStepIndex)
{
  if (!function_pointers_.CreateListStep) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CreateListStep.");
  }
  return function_pointers_.CreateListStep(instrumentHandle, selectorString, createdStepIndex);
}

int32 NiRFmxNRLibrary::CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])
{
  if (!function_pointers_.CreateSignalConfiguration) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_CreateSignalConfiguration.");
  }
  return function_pointers_.CreateSignalConfiguration(instrumentHandle, signalName);
}

int32 NiRFmxNRLibrary::DeleteList(niRFmxInstrHandle instrumentHandle, char listName[])
{
  if (!function_pointers_.DeleteList) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_DeleteList.");
  }
  return function_pointers_.DeleteList(instrumentHandle, listName);
}

int32 NiRFmxNRLibrary::DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])
{
  if (!function_pointers_.DeleteSignalConfiguration) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_DeleteSignalConfiguration.");
  }
  return function_pointers_.DeleteSignalConfiguration(instrumentHandle, signalName);
}

int32 NiRFmxNRLibrary::DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  if (!function_pointers_.DisableTrigger) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_DisableTrigger.");
  }
  return function_pointers_.DisableTrigger(instrumentHandle, selectorString);
}

int32 NiRFmxNRLibrary::GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32* actualResultNamesSize, int32* defaultResultExists)
{
  if (!function_pointers_.GetAllNamedResultNames) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAllNamedResultNames.");
  }
  return function_pointers_.GetAllNamedResultNames(instrumentHandle, selectorString, resultNames, resultNamesBufferSize, actualResultNamesSize, defaultResultExists);
}

int32 NiRFmxNRLibrary::GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32* attrVal)
{
  if (!function_pointers_.GetAttributeF32) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeF32.");
  }
  return function_pointers_.GetAttributeF32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::GetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeF32Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeF32Array.");
  }
  return function_pointers_.GetAttributeF32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64* attrVal)
{
  if (!function_pointers_.GetAttributeF64) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeF64.");
  }
  return function_pointers_.GetAttributeF64(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::GetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeF64Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeF64Array.");
  }
  return function_pointers_.GetAttributeF64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int16* attrVal)
{
  if (!function_pointers_.GetAttributeI16) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeI16.");
  }
  return function_pointers_.GetAttributeI16(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32* attrVal)
{
  if (!function_pointers_.GetAttributeI32) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeI32.");
  }
  return function_pointers_.GetAttributeI32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::GetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeI32Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeI32Array.");
  }
  return function_pointers_.GetAttributeI32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64* attrVal)
{
  if (!function_pointers_.GetAttributeI64) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeI64.");
  }
  return function_pointers_.GetAttributeI64(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::GetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeI64Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeI64Array.");
  }
  return function_pointers_.GetAttributeI64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8* attrVal)
{
  if (!function_pointers_.GetAttributeI8) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeI8.");
  }
  return function_pointers_.GetAttributeI8(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::GetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeI8Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeI8Array.");
  }
  return function_pointers_.GetAttributeI8Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::GetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexDouble attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeNIComplexDoubleArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeNIComplexDoubleArray.");
  }
  return function_pointers_.GetAttributeNIComplexDoubleArray(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::GetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexSingle attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeNIComplexSingleArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeNIComplexSingleArray.");
  }
  return function_pointers_.GetAttributeNIComplexSingleArray(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::GetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 arraySize, char attrVal[])
{
  if (!function_pointers_.GetAttributeString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeString.");
  }
  return function_pointers_.GetAttributeString(instrumentHandle, selectorString, attributeID, arraySize, attrVal);
}

int32 NiRFmxNRLibrary::GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt16* attrVal)
{
  if (!function_pointers_.GetAttributeU16) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeU16.");
  }
  return function_pointers_.GetAttributeU16(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32* attrVal)
{
  if (!function_pointers_.GetAttributeU32) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeU32.");
  }
  return function_pointers_.GetAttributeU32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::GetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeU32Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeU32Array.");
  }
  return function_pointers_.GetAttributeU32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::GetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt64 attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeU64Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeU64Array.");
  }
  return function_pointers_.GetAttributeU64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8* attrVal)
{
  if (!function_pointers_.GetAttributeU8) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeU8.");
  }
  return function_pointers_.GetAttributeU8(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::GetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeU8Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetAttributeU8Array.");
  }
  return function_pointers_.GetAttributeU8Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::GetError(niRFmxInstrHandle instrumentHandle, int32* errorCode, int32 errorDescriptionBufferSize, char errorDescription[])
{
  if (!function_pointers_.GetError) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetError.");
  }
  return function_pointers_.GetError(instrumentHandle, errorCode, errorDescriptionBufferSize, errorDescription);
}

int32 NiRFmxNRLibrary::GetErrorString(niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[])
{
  if (!function_pointers_.GetErrorString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_GetErrorString.");
  }
  return function_pointers_.GetErrorString(instrumentHandle, errorCode, errorDescriptionBufferSize, errorDescription);
}

int32 NiRFmxNRLibrary::Initialize(char resourceName[], char optionString[], niRFmxInstrHandle* handleOut, int32* isNewSession)
{
  if (!function_pointers_.Initialize) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_Initialize.");
  }
  return function_pointers_.Initialize(resourceName, optionString, handleOut, isNewSession);
}

int32 NiRFmxNRLibrary::InitializeFromNIRFSASession(uInt32 nirfsaSession, niRFmxInstrHandle* handleOut)
{
  if (!function_pointers_.InitializeFromNIRFSASession) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_InitializeFromNIRFSASession.");
  }
  return function_pointers_.InitializeFromNIRFSASession(nirfsaSession, handleOut);
}

int32 NiRFmxNRLibrary::Initiate(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[])
{
  if (!function_pointers_.Initiate) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_Initiate.");
  }
  return function_pointers_.Initiate(instrumentHandle, selectorString, resultName);
}

int32 NiRFmxNRLibrary::LoadFromGenerationConfigurationFile(niRFmxInstrHandle instrumentHandle, char selectorString[], char filePath[], int32 configurationIndex)
{
  if (!function_pointers_.LoadFromGenerationConfigurationFile) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_LoadFromGenerationConfigurationFile.");
  }
  return function_pointers_.LoadFromGenerationConfigurationFile(instrumentHandle, selectorString, filePath, configurationIndex);
}

int32 NiRFmxNRLibrary::ModAccAutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)
{
  if (!function_pointers_.ModAccAutoLevel) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccAutoLevel.");
  }
  return function_pointers_.ModAccAutoLevel(instrumentHandle, selectorString, timeout);
}

int32 NiRFmxNRLibrary::ModAccCfgMeasurementMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMode)
{
  if (!function_pointers_.ModAccCfgMeasurementMode) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccCfgMeasurementMode.");
  }
  return function_pointers_.ModAccCfgMeasurementMode(instrumentHandle, selectorString, measurementMode);
}

int32 NiRFmxNRLibrary::ModAccCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled)
{
  if (!function_pointers_.ModAccCfgNoiseCompensationEnabled) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccCfgNoiseCompensationEnabled.");
  }
  return function_pointers_.ModAccCfgNoiseCompensationEnabled(instrumentHandle, selectorString, noiseCompensationEnabled);
}

int32 NiRFmxNRLibrary::ModAccCfgReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, NIComplexSingle referenceWaveform[], int32 arraySize)
{
  if (!function_pointers_.ModAccCfgReferenceWaveform) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccCfgReferenceWaveform.");
  }
  return function_pointers_.ModAccCfgReferenceWaveform(instrumentHandle, selectorString, x0, dx, referenceWaveform, arraySize);
}

int32 NiRFmxNRLibrary::ModAccCfgReferenceWaveformInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 referenceWaveform[], int32 arraySize)
{
  if (!function_pointers_.ModAccCfgReferenceWaveformInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccCfgReferenceWaveform.");
  }
  return function_pointers_.ModAccCfgReferenceWaveformInterleavedIQ(instrumentHandle, selectorString, x0, dx, reinterpret_cast<NIComplexSingle*>(referenceWaveform), arraySize/2);
}

int32 NiRFmxNRLibrary::ModAccCfgReferenceWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 referenceWaveformI[], float32 referenceWaveformQ[], int32 arraySize)
{
  if (!function_pointers_.ModAccCfgReferenceWaveformSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccCfgReferenceWaveformSplit.");
  }
  return function_pointers_.ModAccCfgReferenceWaveformSplit(instrumentHandle, selectorString, x0, dx, referenceWaveformI, referenceWaveformQ, arraySize);
}

int32 NiRFmxNRLibrary::ModAccClearNoiseCalibrationDatabase(niRFmxInstrHandle instrumentHandle)
{
  if (!function_pointers_.ModAccClearNoiseCalibrationDatabase) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccClearNoiseCalibrationDatabase.");
  }
  return function_pointers_.ModAccClearNoiseCalibrationDatabase(instrumentHandle);
}

int32 NiRFmxNRLibrary::ModAccFetchCompositeEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* compositeRMSEVMMean, float64* compositePeakEVMMaximum)
{
  if (!function_pointers_.ModAccFetchCompositeEVM) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchCompositeEVM.");
  }
  return function_pointers_.ModAccFetchCompositeEVM(instrumentHandle, selectorString, timeout, compositeRMSEVMMean, compositePeakEVMMaximum);
}

int32 NiRFmxNRLibrary::ModAccFetchFrequencyErrorMean(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* frequencyErrorMean)
{
  if (!function_pointers_.ModAccFetchFrequencyErrorMean) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchFrequencyErrorMean.");
  }
  return function_pointers_.ModAccFetchFrequencyErrorMean(instrumentHandle, selectorString, timeout, frequencyErrorMean);
}

int32 NiRFmxNRLibrary::ModAccFetchFrequencyErrorPerSlotMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 frequencyErrorPerSlotMaximum[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchFrequencyErrorPerSlotMaximumTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchFrequencyErrorPerSlotMaximumTrace.");
  }
  return function_pointers_.ModAccFetchFrequencyErrorPerSlotMaximumTrace(instrumentHandle, selectorString, timeout, x0, dx, frequencyErrorPerSlotMaximum, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchIQGainImbalancePerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 iqGainImbalancePerSubcarrierMean[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchIQGainImbalancePerSubcarrierMeanTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchIQGainImbalancePerSubcarrierMeanTrace.");
  }
  return function_pointers_.ModAccFetchIQGainImbalancePerSubcarrierMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, iqGainImbalancePerSubcarrierMean, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 iqQuadratureErrorPerSubcarrierMean[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace.");
  }
  return function_pointers_.ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, iqQuadratureErrorPerSubcarrierMean, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchInBandEmissionTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 inBandEmission[], float32 inBandEmissionMask[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchInBandEmissionTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchInBandEmissionTrace.");
  }
  return function_pointers_.ModAccFetchInBandEmissionTrace(instrumentHandle, selectorString, timeout, x0, dx, inBandEmission, inBandEmissionMask, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPBCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pbchdmrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPBCHDMRSConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPBCHDMRSConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPBCHDMRSConstellationTrace(instrumentHandle, selectorString, timeout, pbchdmrsConstellation, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPBCHDMRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchdmrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPBCHDMRSConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPBCHDMRSConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPBCHDMRSConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(pbchdmrsConstellation), arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPBCHDMRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchdmrsConstellationI[], float32 pbchdmrsConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPBCHDMRSConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPBCHDMRSConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchPBCHDMRSConstellationTraceSplit(instrumentHandle, selectorString, timeout, pbchdmrsConstellationI, pbchdmrsConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchdmrsrmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace.");
  }
  return function_pointers_.ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, pbchdmrsrmsevmPerSubcarrierMean, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchdmrsrmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace.");
  }
  return function_pointers_.ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, pbchdmrsrmsevmPerSymbolMean, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPBCHDataConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pbchDataConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPBCHDataConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPBCHDataConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPBCHDataConstellationTrace(instrumentHandle, selectorString, timeout, pbchDataConstellation, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPBCHDataConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchDataConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPBCHDataConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPBCHDataConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPBCHDataConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(pbchDataConstellation), arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPBCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchDataConstellationI[], float32 pbchDataConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPBCHDataConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPBCHDataConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchPBCHDataConstellationTraceSplit(instrumentHandle, selectorString, timeout, pbchDataConstellationI, pbchDataConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchDataRMSEVMPerSubcarrierMean[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTrace.");
  }
  return function_pointers_.ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, pbchDataRMSEVMPerSubcarrierMean, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchDataRMSEVMPerSymbolMean[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace.");
  }
  return function_pointers_.ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, pbchDataRMSEVMPerSymbolMean, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH1024QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam1024Constellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH1024QAMConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH1024QAMConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCH1024QAMConstellationTrace(instrumentHandle, selectorString, timeout, qam1024Constellation, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam1024Constellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH1024QAMConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(qam1024Constellation), arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH1024QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam1024ConstellationI[], float32 qam1024ConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH1024QAMConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH1024QAMConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchPDSCH1024QAMConstellationTraceSplit(instrumentHandle, selectorString, timeout, qam1024ConstellationI, qam1024ConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH16QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam16Constellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH16QAMConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH16QAMConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCH16QAMConstellationTrace(instrumentHandle, selectorString, timeout, qam16Constellation, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam16Constellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH16QAMConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(qam16Constellation), arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH16QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam16ConstellationI[], float32 qam16ConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH16QAMConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH16QAMConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchPDSCH16QAMConstellationTraceSplit(instrumentHandle, selectorString, timeout, qam16ConstellationI, qam16ConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH256QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam256Constellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH256QAMConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH256QAMConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCH256QAMConstellationTrace(instrumentHandle, selectorString, timeout, qam256Constellation, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam256Constellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH256QAMConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(qam256Constellation), arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH256QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam256ConstellationI[], float32 qam256ConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH256QAMConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH256QAMConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchPDSCH256QAMConstellationTraceSplit(instrumentHandle, selectorString, timeout, qam256ConstellationI, qam256ConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH4096QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam4096Constellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH4096QAMConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH4096QAMConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCH4096QAMConstellationTrace(instrumentHandle, selectorString, timeout, qam4096Constellation, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam4096Constellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH4096QAMConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(qam4096Constellation), arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH4096QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam4096ConstellationI[], float32 qam4096ConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH4096QAMConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH4096QAMConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchPDSCH4096QAMConstellationTraceSplit(instrumentHandle, selectorString, timeout, qam4096ConstellationI, qam4096ConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH64QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam64Constellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH64QAMConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH64QAMConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCH64QAMConstellationTrace(instrumentHandle, selectorString, timeout, qam64Constellation, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam64Constellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH64QAMConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(qam64Constellation), arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH64QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam64ConstellationI[], float32 qam64ConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH64QAMConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH64QAMConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchPDSCH64QAMConstellationTraceSplit(instrumentHandle, selectorString, timeout, qam64ConstellationI, qam64ConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH8PSKConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle psk8Constellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH8PSKConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH8PSKConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCH8PSKConstellationTrace(instrumentHandle, selectorString, timeout, psk8Constellation, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 psk8Constellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH8PSKConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(psk8Constellation), arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCH8PSKConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 psk8ConstellationI[], float32 psk8ConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCH8PSKConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCH8PSKConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchPDSCH8PSKConstellationTraceSplit(instrumentHandle, selectorString, timeout, psk8ConstellationI, psk8ConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschdmrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCHDMRSConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCHDMRSConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCHDMRSConstellationTrace(instrumentHandle, selectorString, timeout, pdschdmrsConstellation, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschdmrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCHDMRSConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(pdschdmrsConstellation), arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCHDMRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschdmrsConstellationI[], float32 pdschdmrsConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCHDMRSConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCHDMRSConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchPDSCHDMRSConstellationTraceSplit(instrumentHandle, selectorString, timeout, pdschdmrsConstellationI, pdschdmrsConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCHDataConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschDataConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCHDataConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCHDataConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCHDataConstellationTrace(instrumentHandle, selectorString, timeout, pdschDataConstellation, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCHDataConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschDataConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCHDataConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCHDataConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCHDataConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(pdschDataConstellation), arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschDataConstellationI[], float32 pdschDataConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCHDataConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCHDataConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchPDSCHDataConstellationTraceSplit(instrumentHandle, selectorString, timeout, pdschDataConstellationI, pdschDataConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCHDemodulatedBits(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int8 bits[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCHDemodulatedBits) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCHDemodulatedBits.");
  }
  return function_pointers_.ModAccFetchPDSCHDemodulatedBits(instrumentHandle, selectorString, timeout, bits, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCHPTRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschptrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCHPTRSConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCHPTRSConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCHPTRSConstellationTrace(instrumentHandle, selectorString, timeout, pdschptrsConstellation, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschptrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCHPTRSConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(pdschptrsConstellation), arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCHPTRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschptrsConstellationI[], float32 pdschptrsConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCHPTRSConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCHPTRSConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchPDSCHPTRSConstellationTraceSplit(instrumentHandle, selectorString, timeout, pdschptrsConstellationI, pdschptrsConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCHQPSKConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qpskConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCHQPSKConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCHQPSKConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCHQPSKConstellationTrace(instrumentHandle, selectorString, timeout, qpskConstellation, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qpskConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCHQPSKConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(qpskConstellation), arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPDSCHQPSKConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qpskConstellationI[], float32 qpskConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPDSCHQPSKConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPDSCHQPSKConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchPDSCHQPSKConstellationTraceSplit(instrumentHandle, selectorString, timeout, qpskConstellationI, qpskConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPSSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pssConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPSSConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPSSConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPSSConstellationTrace(instrumentHandle, selectorString, timeout, pssConstellation, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPSSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pssConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPSSConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPSSConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPSSConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(pssConstellation), arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPSSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pssConstellationI[], float32 pssConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPSSConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPSSConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchPSSConstellationTraceSplit(instrumentHandle, selectorString, timeout, pssConstellationI, pssConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pssrmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace.");
  }
  return function_pointers_.ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, pssrmsevmPerSubcarrierMean, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPSSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pssrmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPSSRMSEVMPerSymbolMeanTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPSSRMSEVMPerSymbolMeanTrace.");
  }
  return function_pointers_.ModAccFetchPSSRMSEVMPerSymbolMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, pssrmsevmPerSymbolMean, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPUSCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle puschdmrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPUSCHDMRSConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPUSCHDMRSConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPUSCHDMRSConstellationTrace(instrumentHandle, selectorString, timeout, puschdmrsConstellation, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschdmrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPUSCHDMRSConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(puschdmrsConstellation), arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPUSCHDMRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschdmrsConstellationI[], float32 puschdmrsConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPUSCHDMRSConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPUSCHDMRSConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchPUSCHDMRSConstellationTraceSplit(instrumentHandle, selectorString, timeout, puschdmrsConstellationI, puschdmrsConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPUSCHDataConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle puschDataConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPUSCHDataConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPUSCHDataConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPUSCHDataConstellationTrace(instrumentHandle, selectorString, timeout, puschDataConstellation, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPUSCHDataConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschDataConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPUSCHDataConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPUSCHDataConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPUSCHDataConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(puschDataConstellation), arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPUSCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschDataConstellationI[], float32 puschDataConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPUSCHDataConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPUSCHDataConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchPUSCHDataConstellationTraceSplit(instrumentHandle, selectorString, timeout, puschDataConstellationI, puschDataConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPUSCHDemodulatedBits(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int8 bits[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPUSCHDemodulatedBits) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPUSCHDemodulatedBits.");
  }
  return function_pointers_.ModAccFetchPUSCHDemodulatedBits(instrumentHandle, selectorString, timeout, bits, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPUSCHPTRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle puschptrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPUSCHPTRSConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPUSCHPTRSConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPUSCHPTRSConstellationTrace(instrumentHandle, selectorString, timeout, puschptrsConstellation, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschptrsConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPUSCHPTRSConstellationTrace.");
  }
  return function_pointers_.ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(puschptrsConstellation), arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPUSCHPTRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschptrsConstellationI[], float32 puschptrsConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPUSCHPTRSConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPUSCHPTRSConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchPUSCHPTRSConstellationTraceSplit(instrumentHandle, selectorString, timeout, puschptrsConstellationI, puschptrsConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPUSCHPhaseOffsetTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 puschPhaseOffset[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPUSCHPhaseOffsetTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPUSCHPhaseOffsetTrace.");
  }
  return function_pointers_.ModAccFetchPUSCHPhaseOffsetTrace(instrumentHandle, selectorString, timeout, x0, dx, puschPhaseOffset, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPeakEVMHighPerSymbolMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMHighPerSymbolMaximum[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPeakEVMHighPerSymbolMaximumTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPeakEVMHighPerSymbolMaximumTrace.");
  }
  return function_pointers_.ModAccFetchPeakEVMHighPerSymbolMaximumTrace(instrumentHandle, selectorString, timeout, x0, dx, peakEVMHighPerSymbolMaximum, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPeakEVMLowPerSymbolMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMLowPerSymbolMaximum[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPeakEVMLowPerSymbolMaximumTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPeakEVMLowPerSymbolMaximumTrace.");
  }
  return function_pointers_.ModAccFetchPeakEVMLowPerSymbolMaximumTrace(instrumentHandle, selectorString, timeout, x0, dx, peakEVMLowPerSymbolMaximum, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPeakEVMPerSlotMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMPerSlotMaximum[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPeakEVMPerSlotMaximumTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPeakEVMPerSlotMaximumTrace.");
  }
  return function_pointers_.ModAccFetchPeakEVMPerSlotMaximumTrace(instrumentHandle, selectorString, timeout, x0, dx, peakEVMPerSlotMaximum, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPeakEVMPerSubcarrierMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMPerSubcarrierMaximum[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPeakEVMPerSubcarrierMaximumTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPeakEVMPerSubcarrierMaximumTrace.");
  }
  return function_pointers_.ModAccFetchPeakEVMPerSubcarrierMaximumTrace(instrumentHandle, selectorString, timeout, x0, dx, peakEVMPerSubcarrierMaximum, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchPeakEVMPerSymbolMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMPerSymbolMaximum[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPeakEVMPerSymbolMaximumTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchPeakEVMPerSymbolMaximumTrace.");
  }
  return function_pointers_.ModAccFetchPeakEVMPerSymbolMaximumTrace(instrumentHandle, selectorString, timeout, x0, dx, peakEVMPerSymbolMaximum, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchRMSEVMHighPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmHighPerSymbolMean[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchRMSEVMHighPerSymbolMeanTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchRMSEVMHighPerSymbolMeanTrace.");
  }
  return function_pointers_.ModAccFetchRMSEVMHighPerSymbolMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, rmsevmHighPerSymbolMean, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchRMSEVMLowPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmLowPerSymbolMean[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchRMSEVMLowPerSymbolMeanTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchRMSEVMLowPerSymbolMeanTrace.");
  }
  return function_pointers_.ModAccFetchRMSEVMLowPerSymbolMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, rmsevmLowPerSymbolMean, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchRMSEVMPerSlotMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmPerSlotMean[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchRMSEVMPerSlotMeanTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchRMSEVMPerSlotMeanTrace.");
  }
  return function_pointers_.ModAccFetchRMSEVMPerSlotMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, rmsevmPerSlotMean, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchRMSEVMPerSubcarrierMeanTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchRMSEVMPerSubcarrierMeanTrace.");
  }
  return function_pointers_.ModAccFetchRMSEVMPerSubcarrierMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, rmsevmPerSubcarrierMean, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchRMSEVMPerSymbolMeanTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchRMSEVMPerSymbolMeanTrace.");
  }
  return function_pointers_.ModAccFetchRMSEVMPerSymbolMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, rmsevmPerSymbolMean, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchSSSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle sssConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchSSSConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchSSSConstellationTrace.");
  }
  return function_pointers_.ModAccFetchSSSConstellationTrace(instrumentHandle, selectorString, timeout, sssConstellation, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchSSSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 sssConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchSSSConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchSSSConstellationTrace.");
  }
  return function_pointers_.ModAccFetchSSSConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(sssConstellation), arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchSSSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 sssConstellationI[], float32 sssConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchSSSConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchSSSConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchSSSConstellationTraceSplit(instrumentHandle, selectorString, timeout, sssConstellationI, sssConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 sssrmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace.");
  }
  return function_pointers_.ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, sssrmsevmPerSubcarrierMean, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchSSSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 sssrmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchSSSRMSEVMPerSymbolMeanTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchSSSRMSEVMPerSymbolMeanTrace.");
  }
  return function_pointers_.ModAccFetchSSSRMSEVMPerSymbolMeanTrace(instrumentHandle, selectorString, timeout, x0, dx, sssrmsevmPerSymbolMean, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchSpectralFlatnessTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectralFlatness[], float32 spectralFlatnessLowerMask[], float32 spectralFlatnessUpperMask[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchSpectralFlatnessTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchSpectralFlatnessTrace.");
  }
  return function_pointers_.ModAccFetchSpectralFlatnessTrace(instrumentHandle, selectorString, timeout, x0, dx, spectralFlatness, spectralFlatnessLowerMask, spectralFlatnessUpperMask, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchSubblockInBandEmissionTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 subblockInBandEmission[], float64 subblockInBandEmissionMask[], float64 subblockInBandEmissionRBIndices[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchSubblockInBandEmissionTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchSubblockInBandEmissionTrace.");
  }
  return function_pointers_.ModAccFetchSubblockInBandEmissionTrace(instrumentHandle, selectorString, timeout, subblockInBandEmission, subblockInBandEmissionMask, subblockInBandEmissionRBIndices, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccFetchTransientPeriodLocationsTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 transientPeriodLocations[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchTransientPeriodLocationsTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccFetchTransientPeriodLocationsTrace.");
  }
  return function_pointers_.ModAccFetchTransientPeriodLocationsTrace(instrumentHandle, selectorString, timeout, x0, dx, transientPeriodLocations, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ModAccValidateCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* calibrationDataValid)
{
  if (!function_pointers_.ModAccValidateCalibrationData) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ModAccValidateCalibrationData.");
  }
  return function_pointers_.ModAccValidateCalibrationData(instrumentHandle, selectorString, calibrationDataValid);
}

int32 NiRFmxNRLibrary::OBWCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  if (!function_pointers_.OBWCfgAveraging) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_OBWCfgAveraging.");
  }
  return function_pointers_.OBWCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 NiRFmxNRLibrary::OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)
{
  if (!function_pointers_.OBWCfgRBWFilter) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_OBWCfgRBWFilter.");
  }
  return function_pointers_.OBWCfgRBWFilter(instrumentHandle, selectorString, rbwAuto, rbw, rbwFilterType);
}

int32 NiRFmxNRLibrary::OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)
{
  if (!function_pointers_.OBWCfgSweepTime) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_OBWCfgSweepTime.");
  }
  return function_pointers_.OBWCfgSweepTime(instrumentHandle, selectorString, sweepTimeAuto, sweepTimeInterval);
}

int32 NiRFmxNRLibrary::OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* occupiedBandwidth, float64* absolutePower, float64* startFrequency, float64* stopFrequency)
{
  if (!function_pointers_.OBWFetchMeasurement) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_OBWFetchMeasurement.");
  }
  return function_pointers_.OBWFetchMeasurement(instrumentHandle, selectorString, timeout, occupiedBandwidth, absolutePower, startFrequency, stopFrequency);
}

int32 NiRFmxNRLibrary::OBWFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.OBWFetchSpectrum) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_OBWFetchSpectrum.");
  }
  return function_pointers_.OBWFetchSpectrum(instrumentHandle, selectorString, timeout, x0, dx, spectrum, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::PVTCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  if (!function_pointers_.PVTCfgAveraging) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_PVTCfgAveraging.");
  }
  return function_pointers_.PVTCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 NiRFmxNRLibrary::PVTCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)
{
  if (!function_pointers_.PVTCfgMeasurementMethod) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_PVTCfgMeasurementMethod.");
  }
  return function_pointers_.PVTCfgMeasurementMethod(instrumentHandle, selectorString, measurementMethod);
}

int32 NiRFmxNRLibrary::PVTCfgOFFPowerExclusionPeriods(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offPowerExclusionBefore, float64 offPowerExclusionAfter)
{
  if (!function_pointers_.PVTCfgOFFPowerExclusionPeriods) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_PVTCfgOFFPowerExclusionPeriods.");
  }
  return function_pointers_.PVTCfgOFFPowerExclusionPeriods(instrumentHandle, selectorString, offPowerExclusionBefore, offPowerExclusionAfter);
}

int32 NiRFmxNRLibrary::PVTFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* absoluteOFFPowerBefore, float64* absoluteOFFPowerAfter, float64* absoluteONPower, float64* burstWidth)
{
  if (!function_pointers_.PVTFetchMeasurement) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_PVTFetchMeasurement.");
  }
  return function_pointers_.PVTFetchMeasurement(instrumentHandle, selectorString, timeout, measurementStatus, absoluteOFFPowerBefore, absoluteOFFPowerAfter, absoluteONPower, burstWidth);
}

int32 NiRFmxNRLibrary::PVTFetchMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 absoluteOFFPowerBefore[], float64 absoluteOFFPowerAfter[], float64 absoluteONPower[], float64 burstWidth[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.PVTFetchMeasurementArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_PVTFetchMeasurementArray.");
  }
  return function_pointers_.PVTFetchMeasurementArray(instrumentHandle, selectorString, timeout, measurementStatus, absoluteOFFPowerBefore, absoluteOFFPowerAfter, absoluteONPower, burstWidth, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::PVTFetchSignalPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 signalPower[], float32 absoluteLimit[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.PVTFetchSignalPowerTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_PVTFetchSignalPowerTrace.");
  }
  return function_pointers_.PVTFetchSignalPowerTrace(instrumentHandle, selectorString, timeout, x0, dx, signalPower, absoluteLimit, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::PVTFetchWindowedSignalPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 windowedSignalPower[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.PVTFetchWindowedSignalPowerTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_PVTFetchWindowedSignalPowerTrace.");
  }
  return function_pointers_.PVTFetchWindowedSignalPowerTrace(instrumentHandle, selectorString, timeout, x0, dx, windowedSignalPower, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID)
{
  if (!function_pointers_.ResetAttribute) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ResetAttribute.");
  }
  return function_pointers_.ResetAttribute(instrumentHandle, selectorString, attributeID);
}

int32 NiRFmxNRLibrary::ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  if (!function_pointers_.ResetToDefault) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_ResetToDefault.");
  }
  return function_pointers_.ResetToDefault(instrumentHandle, selectorString);
}

int32 NiRFmxNRLibrary::SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  if (!function_pointers_.SEMCfgAveraging) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgAveraging.");
  }
  return function_pointers_.SEMCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 NiRFmxNRLibrary::SEMCfgComponentCarrierRatedOutputPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 componentCarrierRatedOutputPower)
{
  if (!function_pointers_.SEMCfgComponentCarrierRatedOutputPower) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgComponentCarrierRatedOutputPower.");
  }
  return function_pointers_.SEMCfgComponentCarrierRatedOutputPower(instrumentHandle, selectorString, componentCarrierRatedOutputPower);
}

int32 NiRFmxNRLibrary::SEMCfgComponentCarrierRatedOutputPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 componentCarrierRatedOutputPower[], int32 numberOfElements)
{
  if (!function_pointers_.SEMCfgComponentCarrierRatedOutputPowerArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgComponentCarrierRatedOutputPowerArray.");
  }
  return function_pointers_.SEMCfgComponentCarrierRatedOutputPowerArray(instrumentHandle, selectorString, componentCarrierRatedOutputPower, numberOfElements);
}

int32 NiRFmxNRLibrary::SEMCfgNumberOfOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets)
{
  if (!function_pointers_.SEMCfgNumberOfOffsets) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgNumberOfOffsets.");
  }
  return function_pointers_.SEMCfgNumberOfOffsets(instrumentHandle, selectorString, numberOfOffsets);
}

int32 NiRFmxNRLibrary::SEMCfgOffsetAbsoluteLimit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 absoluteLimitStart, float64 absoluteLimitStop)
{
  if (!function_pointers_.SEMCfgOffsetAbsoluteLimit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgOffsetAbsoluteLimit.");
  }
  return function_pointers_.SEMCfgOffsetAbsoluteLimit(instrumentHandle, selectorString, absoluteLimitStart, absoluteLimitStop);
}

int32 NiRFmxNRLibrary::SEMCfgOffsetAbsoluteLimitArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 absoluteLimitStart[], float64 absoluteLimitStop[], int32 numberOfElements)
{
  if (!function_pointers_.SEMCfgOffsetAbsoluteLimitArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgOffsetAbsoluteLimitArray.");
  }
  return function_pointers_.SEMCfgOffsetAbsoluteLimitArray(instrumentHandle, selectorString, absoluteLimitStart, absoluteLimitStop, numberOfElements);
}

int32 NiRFmxNRLibrary::SEMCfgOffsetBandwidthIntegral(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandwidthIntegral)
{
  if (!function_pointers_.SEMCfgOffsetBandwidthIntegral) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgOffsetBandwidthIntegral.");
  }
  return function_pointers_.SEMCfgOffsetBandwidthIntegral(instrumentHandle, selectorString, bandwidthIntegral);
}

int32 NiRFmxNRLibrary::SEMCfgOffsetBandwidthIntegralArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandwidthIntegral[], int32 numberOfElements)
{
  if (!function_pointers_.SEMCfgOffsetBandwidthIntegralArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgOffsetBandwidthIntegralArray.");
  }
  return function_pointers_.SEMCfgOffsetBandwidthIntegralArray(instrumentHandle, selectorString, bandwidthIntegral, numberOfElements);
}

int32 NiRFmxNRLibrary::SEMCfgOffsetFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetStartFrequency, float64 offsetStopFrequency, int32 offsetSideband)
{
  if (!function_pointers_.SEMCfgOffsetFrequency) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgOffsetFrequency.");
  }
  return function_pointers_.SEMCfgOffsetFrequency(instrumentHandle, selectorString, offsetStartFrequency, offsetStopFrequency, offsetSideband);
}

int32 NiRFmxNRLibrary::SEMCfgOffsetFrequencyArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetStartFrequency[], float64 offsetStopFrequency[], int32 offsetSideband[], int32 numberOfElements)
{
  if (!function_pointers_.SEMCfgOffsetFrequencyArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgOffsetFrequencyArray.");
  }
  return function_pointers_.SEMCfgOffsetFrequencyArray(instrumentHandle, selectorString, offsetStartFrequency, offsetStopFrequency, offsetSideband, numberOfElements);
}

int32 NiRFmxNRLibrary::SEMCfgOffsetLimitFailMask(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 limitFailMask)
{
  if (!function_pointers_.SEMCfgOffsetLimitFailMask) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgOffsetLimitFailMask.");
  }
  return function_pointers_.SEMCfgOffsetLimitFailMask(instrumentHandle, selectorString, limitFailMask);
}

int32 NiRFmxNRLibrary::SEMCfgOffsetLimitFailMaskArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 limitFailMask[], int32 numberOfElements)
{
  if (!function_pointers_.SEMCfgOffsetLimitFailMaskArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgOffsetLimitFailMaskArray.");
  }
  return function_pointers_.SEMCfgOffsetLimitFailMaskArray(instrumentHandle, selectorString, limitFailMask, numberOfElements);
}

int32 NiRFmxNRLibrary::SEMCfgOffsetRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetRBW, int32 offsetRBWFilterType)
{
  if (!function_pointers_.SEMCfgOffsetRBWFilter) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgOffsetRBWFilter.");
  }
  return function_pointers_.SEMCfgOffsetRBWFilter(instrumentHandle, selectorString, offsetRBW, offsetRBWFilterType);
}

int32 NiRFmxNRLibrary::SEMCfgOffsetRBWFilterArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetRBW[], int32 offsetRBWFilterType[], int32 numberOfElements)
{
  if (!function_pointers_.SEMCfgOffsetRBWFilterArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgOffsetRBWFilterArray.");
  }
  return function_pointers_.SEMCfgOffsetRBWFilterArray(instrumentHandle, selectorString, offsetRBW, offsetRBWFilterType, numberOfElements);
}

int32 NiRFmxNRLibrary::SEMCfgOffsetRelativeLimit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 relativeLimitStart, float64 relativeLimitStop)
{
  if (!function_pointers_.SEMCfgOffsetRelativeLimit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgOffsetRelativeLimit.");
  }
  return function_pointers_.SEMCfgOffsetRelativeLimit(instrumentHandle, selectorString, relativeLimitStart, relativeLimitStop);
}

int32 NiRFmxNRLibrary::SEMCfgOffsetRelativeLimitArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 relativeLimitStart[], float64 relativeLimitStop[], int32 numberOfElements)
{
  if (!function_pointers_.SEMCfgOffsetRelativeLimitArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgOffsetRelativeLimitArray.");
  }
  return function_pointers_.SEMCfgOffsetRelativeLimitArray(instrumentHandle, selectorString, relativeLimitStart, relativeLimitStop, numberOfElements);
}

int32 NiRFmxNRLibrary::SEMCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)
{
  if (!function_pointers_.SEMCfgSweepTime) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgSweepTime.");
  }
  return function_pointers_.SEMCfgSweepTime(instrumentHandle, selectorString, sweepTimeAuto, sweepTimeInterval);
}

int32 NiRFmxNRLibrary::SEMCfgUplinkMaskType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 uplinkMaskType)
{
  if (!function_pointers_.SEMCfgUplinkMaskType) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMCfgUplinkMaskType.");
  }
  return function_pointers_.SEMCfgUplinkMaskType(instrumentHandle, selectorString, uplinkMaskType);
}

int32 NiRFmxNRLibrary::SEMFetchComponentCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absolutePower, float64* peakAbsolutePower, float64* peakFrequency, float64* relativePower)
{
  if (!function_pointers_.SEMFetchComponentCarrierMeasurement) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMFetchComponentCarrierMeasurement.");
  }
  return function_pointers_.SEMFetchComponentCarrierMeasurement(instrumentHandle, selectorString, timeout, absolutePower, peakAbsolutePower, peakFrequency, relativePower);
}

int32 NiRFmxNRLibrary::SEMFetchComponentCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 relativePower[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.SEMFetchComponentCarrierMeasurementArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMFetchComponentCarrierMeasurementArray.");
  }
  return function_pointers_.SEMFetchComponentCarrierMeasurementArray(instrumentHandle, selectorString, timeout, absolutePower, peakAbsolutePower, peakFrequency, relativePower, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::SEMFetchLowerOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower)
{
  if (!function_pointers_.SEMFetchLowerOffsetMargin) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMFetchLowerOffsetMargin.");
  }
  return function_pointers_.SEMFetchLowerOffsetMargin(instrumentHandle, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower);
}

int32 NiRFmxNRLibrary::SEMFetchLowerOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.SEMFetchLowerOffsetMarginArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMFetchLowerOffsetMarginArray.");
  }
  return function_pointers_.SEMFetchLowerOffsetMarginArray(instrumentHandle, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::SEMFetchLowerOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAbsolutePower, float64* totalRelativePower, float64* peakAbsolutePower, float64* peakFrequency, float64* peakRelativePower)
{
  if (!function_pointers_.SEMFetchLowerOffsetPower) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMFetchLowerOffsetPower.");
  }
  return function_pointers_.SEMFetchLowerOffsetPower(instrumentHandle, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower);
}

int32 NiRFmxNRLibrary::SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 totalAbsolutePower[], float64 totalRelativePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 peakRelativePower[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.SEMFetchLowerOffsetPowerArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMFetchLowerOffsetPowerArray.");
  }
  return function_pointers_.SEMFetchLowerOffsetPowerArray(instrumentHandle, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus)
{
  if (!function_pointers_.SEMFetchMeasurementStatus) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMFetchMeasurementStatus.");
  }
  return function_pointers_.SEMFetchMeasurementStatus(instrumentHandle, selectorString, timeout, measurementStatus);
}

int32 NiRFmxNRLibrary::SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], float32 compositeMask[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.SEMFetchSpectrum) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMFetchSpectrum.");
  }
  return function_pointers_.SEMFetchSpectrum(instrumentHandle, selectorString, timeout, x0, dx, spectrum, compositeMask, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::SEMFetchSubblockMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* subblockPower, float64* integrationBandwidth, float64* frequency)
{
  if (!function_pointers_.SEMFetchSubblockMeasurement) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMFetchSubblockMeasurement.");
  }
  return function_pointers_.SEMFetchSubblockMeasurement(instrumentHandle, selectorString, timeout, subblockPower, integrationBandwidth, frequency);
}

int32 NiRFmxNRLibrary::SEMFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAggregatedPower)
{
  if (!function_pointers_.SEMFetchTotalAggregatedPower) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMFetchTotalAggregatedPower.");
  }
  return function_pointers_.SEMFetchTotalAggregatedPower(instrumentHandle, selectorString, timeout, totalAggregatedPower);
}

int32 NiRFmxNRLibrary::SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower)
{
  if (!function_pointers_.SEMFetchUpperOffsetMargin) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMFetchUpperOffsetMargin.");
  }
  return function_pointers_.SEMFetchUpperOffsetMargin(instrumentHandle, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower);
}

int32 NiRFmxNRLibrary::SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.SEMFetchUpperOffsetMarginArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMFetchUpperOffsetMarginArray.");
  }
  return function_pointers_.SEMFetchUpperOffsetMarginArray(instrumentHandle, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAbsolutePower, float64* totalRelativePower, float64* peakAbsolutePower, float64* peakFrequency, float64* peakRelativePower)
{
  if (!function_pointers_.SEMFetchUpperOffsetPower) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMFetchUpperOffsetPower.");
  }
  return function_pointers_.SEMFetchUpperOffsetPower(instrumentHandle, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower);
}

int32 NiRFmxNRLibrary::SEMFetchUpperOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 totalAbsolutePower[], float64 totalRelativePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 peakRelativePower[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.SEMFetchUpperOffsetPowerArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SEMFetchUpperOffsetPowerArray.");
  }
  return function_pointers_.SEMFetchUpperOffsetPowerArray(instrumentHandle, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)
{
  if (!function_pointers_.SelectMeasurements) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SelectMeasurements.");
  }
  return function_pointers_.SelectMeasurements(instrumentHandle, selectorString, measurements, enableAllTraces);
}

int32 NiRFmxNRLibrary::SendSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle)
{
  if (!function_pointers_.SendSoftwareEdgeTrigger) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SendSoftwareEdgeTrigger.");
  }
  return function_pointers_.SendSoftwareEdgeTrigger(instrumentHandle);
}

int32 NiRFmxNRLibrary::SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal)
{
  if (!function_pointers_.SetAttributeF32) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeF32.");
  }
  return function_pointers_.SetAttributeF32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeF32Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeF32Array.");
  }
  return function_pointers_.SetAttributeF32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxNRLibrary::SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal)
{
  if (!function_pointers_.SetAttributeF64) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeF64.");
  }
  return function_pointers_.SetAttributeF64(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeF64Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeF64Array.");
  }
  return function_pointers_.SetAttributeF64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxNRLibrary::SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int16 attrVal)
{
  if (!function_pointers_.SetAttributeI16) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeI16.");
  }
  return function_pointers_.SetAttributeI16(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal)
{
  if (!function_pointers_.SetAttributeI32) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeI32.");
  }
  return function_pointers_.SetAttributeI32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeI32Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeI32Array.");
  }
  return function_pointers_.SetAttributeI32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxNRLibrary::SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal)
{
  if (!function_pointers_.SetAttributeI64) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeI64.");
  }
  return function_pointers_.SetAttributeI64(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeI64Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeI64Array.");
  }
  return function_pointers_.SetAttributeI64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxNRLibrary::SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal)
{
  if (!function_pointers_.SetAttributeI8) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeI8.");
  }
  return function_pointers_.SetAttributeI8(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeI8Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeI8Array.");
  }
  return function_pointers_.SetAttributeI8Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxNRLibrary::SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexDouble attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeNIComplexDoubleArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeNIComplexDoubleArray.");
  }
  return function_pointers_.SetAttributeNIComplexDoubleArray(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxNRLibrary::SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexSingle attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeNIComplexSingleArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeNIComplexSingleArray.");
  }
  return function_pointers_.SetAttributeNIComplexSingleArray(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxNRLibrary::SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, char attrVal[])
{
  if (!function_pointers_.SetAttributeString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeString.");
  }
  return function_pointers_.SetAttributeString(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt16 attrVal)
{
  if (!function_pointers_.SetAttributeU16) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeU16.");
  }
  return function_pointers_.SetAttributeU16(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal)
{
  if (!function_pointers_.SetAttributeU32) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeU32.");
  }
  return function_pointers_.SetAttributeU32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeU32Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeU32Array.");
  }
  return function_pointers_.SetAttributeU32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxNRLibrary::SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt64 attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeU64Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeU64Array.");
  }
  return function_pointers_.SetAttributeU64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxNRLibrary::SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal)
{
  if (!function_pointers_.SetAttributeU8) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeU8.");
  }
  return function_pointers_.SetAttributeU8(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxNRLibrary::SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeU8Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_SetAttributeU8Array.");
  }
  return function_pointers_.SetAttributeU8Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxNRLibrary::TXPFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* averagePowerMean, float64* peakPowerMaximum)
{
  if (!function_pointers_.TXPFetchMeasurement) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_TXPFetchMeasurement.");
  }
  return function_pointers_.TXPFetchMeasurement(instrumentHandle, selectorString, timeout, averagePowerMean, peakPowerMaximum);
}

int32 NiRFmxNRLibrary::TXPFetchPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 power[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.TXPFetchPowerTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_TXPFetchPowerTrace.");
  }
  return function_pointers_.TXPFetchPowerTrace(instrumentHandle, selectorString, timeout, x0, dx, power, arraySize, actualArraySize);
}

int32 NiRFmxNRLibrary::WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)
{
  if (!function_pointers_.WaitForAcquisitionComplete) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_WaitForAcquisitionComplete.");
  }
  return function_pointers_.WaitForAcquisitionComplete(instrumentHandle, timeout);
}

int32 NiRFmxNRLibrary::WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)
{
  if (!function_pointers_.WaitForMeasurementComplete) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxNR_WaitForMeasurementComplete.");
  }
  return function_pointers_.WaitForMeasurementComplete(instrumentHandle, selectorString, timeout);
}

}  // namespace nirfmxnr_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/nirfmxnr/nirfmxnr_library.h sha256=8797923cda0dae42f69e281fe13bf63126ee944a1e4b6019dbc287053dc82390 bytes=91498 -->
## FILE: generated/nirfmxnr/nirfmxnr_library.h

- repository: `ni/grpc-device`
- source_path: `generated/nirfmxnr/nirfmxnr_library.h`
- sha256: `8797923cda0dae42f69e281fe13bf63126ee944a1e4b6019dbc287053dc82390`
- bytes: 91498

````c
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Real implementation of LibraryInterface for NI-RFMXNR
//---------------------------------------------------------------------
#ifndef NIRFMXNR_GRPC_LIBRARY_H
#define NIRFMXNR_GRPC_LIBRARY_H

#include "nirfmxnr_library_interface.h"

#include <server/shared_library_interface.h>

#include <memory>

namespace nirfmxnr_grpc {

class NiRFmxNRLibrary : public nirfmxnr_grpc::NiRFmxNRLibraryInterface {
 public:
  NiRFmxNRLibrary();
  explicit NiRFmxNRLibrary(std::shared_ptr<nidevice_grpc::SharedLibraryInterface> shared_library);
  virtual ~NiRFmxNRLibrary();

  ::grpc::Status check_function_exists(std::string functionName);
  int32 ACPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) override;
  int32 ACPCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod) override;
  int32 ACPCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled) override;
  int32 ACPCfgNumberOfENDCOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfENDCOffsets) override;
  int32 ACPCfgNumberOfEUTRAOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfEUTRAOffsets) override;
  int32 ACPCfgNumberOfNROffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfNROffsets) override;
  int32 ACPCfgNumberOfUTRAOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfUTRAOffsets) override;
  int32 ACPCfgPowerUnits(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnits) override;
  int32 ACPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType) override;
  int32 ACPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval) override;
  int32 ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 absolutePowersTrace[], int32 arraySize, int32* actualArraySize) override;
  int32 ACPFetchComponentCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absolutePower, float64* relativePower) override;
  int32 ACPFetchComponentCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 relativePower[], int32 arraySize, int32* actualArraySize) override;
  int32 ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* lowerRelativePower, float64* upperRelativePower, float64* lowerAbsolutePower, float64* upperAbsolutePower) override;
  int32 ACPFetchOffsetMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 lowerRelativePower[], float64 upperRelativePower[], float64 lowerAbsolutePower[], float64 upperAbsolutePower[], int32 arraySize, int32* actualArraySize) override;
  int32 ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 relativePowersTrace[], int32 arraySize, int32* actualArraySize) override;
  int32 ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize) override;
  int32 ACPFetchSubblockMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* subblockPower, float64* integrationBandwidth, float64* frequency) override;
  int32 ACPFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAggregatedPower) override;
  int32 ACPValidateNoiseCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* noiseCalibrationDataValid) override;
  int32 AbortMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[]) override;
  int32 AnalyzeIQ1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved) override;
  int32 AnalyzeIQ1WaveformInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iq[], int32 arraySize, int32 reset, int64 reserved) override;
  int32 AnalyzeIQ1WaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iqi[], float32 iqq[], int32 arraySize, int32 reset, int64 reserved) override;
  int32 AnalyzeNWaveformsIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], NIComplexSingle iq[], int32 iqSize[], int32 arraySize, int32 reset) override;
  int32 AnalyzeNWaveformsIQInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], float32 iq[], int32 iqSize[], int32 arraySize, int32 reset) override;
  int32 AnalyzeNWaveformsIQSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], float32 iqi[], float32 iqq[], int32 iqSize[], int32 arraySize, int32 reset) override;
  int32 AnalyzeNWaveformsSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], float32 spectrum[], int32 spectrumSize[], int32 arraySize, int32 reset) override;
  int32 AnalyzeSpectrum1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 spectrum[], int32 arraySize, int32 reset, int64 reserved) override;
  int32 AutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval, float64* referenceLevel) override;
  int32 BuildBandwidthPartString(char selectorString[], int32 bandwidthPartNumber, int32 selectorStringOutLength, char selectorStringOut[]) override;
  int32 BuildCORESETClusterString(char selectorString[], int32 coresetClusterNumber, int32 selectorStringOutLength, char selectorStringOut[]) override;
  int32 BuildCORESETString(char selectorString[], int32 coresetNumber, int32 selectorStringOutLength, char selectorStringOut[]) override;
  int32 BuildCarrierString(char selectorString[], int32 carrierNumber, int32 selectorStringOutLength, char selectorStringOut[]) override;
  int32 BuildListStepString(char listName[], char resultName[], int32 stepNumber, int32 selectorStringLength, char selectorString[]) override;
  int32 BuildListString(char listName[], char resultName[], int32 selectorStringLength, char selectorString[]) override;
  int32 BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[]) override;
  int32 BuildPDCCHString(char selectorString[], int32 pdcchNumber, int32 selectorStringOutLength, char selectorStringOut[]) override;
  int32 BuildPDSCHClusterString(char selectorString[], int32 pdschClusterNumber, int32 selectorStringOutLength, char selectorStringOut[]) override;
  int32 BuildPDSCHString(char selectorString[], int32 pdschNumber, int32 selectorStringOutLength, char selectorStringOut[]) override;
  int32 BuildPUSCHClusterString(char selectorString[], int32 puschClusterNumber, int32 selectorStringOutLength, char selectorStringOut[]) override;
  int32 BuildPUSCHString(char selectorString[], int32 puschNumber, int32 selectorStringOutLength, char selectorStringOut[]) override;
  int32 BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[]) override;
  int32 BuildSubblockString(char selectorString[], int32 subblockNumber, int32 selectorStringOutLength, char selectorStringOut[]) override;
  int32 BuildUserString(char selectorString[], int32 userNumber, int32 selectorStringOutLength, char selectorStringOut[]) override;
  int32 CHPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) override;
  int32 CHPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType) override;
  int32 CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval) override;
  int32 CHPFetchComponentCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absolutePower, float64* relativePower) override;
  int32 CHPFetchComponentCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 relativePower[], int32 arraySize, int32* actualArraySize) override;
  int32 CHPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize) override;
  int32 CHPFetchSubblockPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* subblockPower) override;
  int32 CHPFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAggregatedPower) override;
  int32 CHPValidateNoiseCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* noiseCalibrationDataValid) override;
  int32 CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger) override;
  int32 CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation) override;
  int32 CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency) override;
  int32 CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency) override;
  int32 CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdgeSlope, float64 iqPowerEdgeLevel, float64 triggerDelay, int32 triggerMinQuietTimeMode, float64 triggerMinQuietTimeDuration, int32 iqPowerEdgeLevelType, int32 enableTrigger) override;
  int32 CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue) override;
  int32 CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation) override;
  int32 CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue) override;
  int32 CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel) override;
  int32 CfgSelectedPortsMultiple(niRFmxInstrHandle instrumentHandle, char selectorString[], char selectedPorts[]) override;
  int32 CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger) override;
  int32 CfggNodeBCategory(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 gNodeBCategory) override;
  int32 CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* isDone) override;
  int32 ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[]) override;
  int32 ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[]) override;
  int32 ClearNoiseCalibrationDatabase(niRFmxInstrHandle instrumentHandle, char selectorString[]) override;
  int32 CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[]) override;
  int32 Close(niRFmxInstrHandle instrumentHandle, int32 forceDestroy) override;
  int32 Commit(niRFmxInstrHandle instrumentHandle, char selectorString[]) override;
  int32 CreateList(niRFmxInstrHandle instrumentHandle, char listName[]) override;
  int32 CreateListStep(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* createdStepIndex) override;
  int32 CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[]) override;
  int32 DeleteList(niRFmxInstrHandle instrumentHandle, char listName[]) override;
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
  int32 LoadFromGenerationConfigurationFile(niRFmxInstrHandle instrumentHandle, char selectorString[], char filePath[], int32 configurationIndex) override;
  int32 ModAccAutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout) override;
  int32 ModAccCfgMeasurementMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMode) override;
  int32 ModAccCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled) override;
  int32 ModAccCfgReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, NIComplexSingle referenceWaveform[], int32 arraySize) override;
  int32 ModAccCfgReferenceWaveformInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 referenceWaveform[], int32 arraySize) override;
  int32 ModAccCfgReferenceWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 referenceWaveformI[], float32 referenceWaveformQ[], int32 arraySize) override;
  int32 ModAccClearNoiseCalibrationDatabase(niRFmxInstrHandle instrumentHandle) override;
  int32 ModAccFetchCompositeEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* compositeRMSEVMMean, float64* compositePeakEVMMaximum) override;
  int32 ModAccFetchFrequencyErrorMean(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* frequencyErrorMean) override;
  int32 ModAccFetchFrequencyErrorPerSlotMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 frequencyErrorPerSlotMaximum[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchIQGainImbalancePerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 iqGainImbalancePerSubcarrierMean[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 iqQuadratureErrorPerSubcarrierMean[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchInBandEmissionTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 inBandEmission[], float32 inBandEmissionMask[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPBCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pbchdmrsConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPBCHDMRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchdmrsConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPBCHDMRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchdmrsConstellationI[], float32 pbchdmrsConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchdmrsrmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchdmrsrmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPBCHDataConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pbchDataConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPBCHDataConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchDataConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPBCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchDataConstellationI[], float32 pbchDataConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchDataRMSEVMPerSubcarrierMean[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchDataRMSEVMPerSymbolMean[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH1024QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam1024Constellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam1024Constellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH1024QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam1024ConstellationI[], float32 qam1024ConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH16QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam16Constellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam16Constellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH16QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam16ConstellationI[], float32 qam16ConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH256QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam256Constellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam256Constellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH256QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam256ConstellationI[], float32 qam256ConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH4096QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam4096Constellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam4096Constellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH4096QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam4096ConstellationI[], float32 qam4096ConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH64QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam64Constellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam64Constellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH64QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam64ConstellationI[], float32 qam64ConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH8PSKConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle psk8Constellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 psk8Constellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCH8PSKConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 psk8ConstellationI[], float32 psk8ConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschdmrsConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschdmrsConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCHDMRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschdmrsConstellationI[], float32 pdschdmrsConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCHDataConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschDataConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCHDataConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschDataConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschDataConstellationI[], float32 pdschDataConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCHDemodulatedBits(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int8 bits[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCHPTRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschptrsConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschptrsConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCHPTRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschptrsConstellationI[], float32 pdschptrsConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCHQPSKConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qpskConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qpskConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPDSCHQPSKConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qpskConstellationI[], float32 qpskConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPSSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pssConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPSSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pssConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPSSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pssConstellationI[], float32 pssConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pssrmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPSSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pssrmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPUSCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle puschdmrsConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschdmrsConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPUSCHDMRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschdmrsConstellationI[], float32 puschdmrsConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPUSCHDataConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle puschDataConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPUSCHDataConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschDataConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPUSCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschDataConstellationI[], float32 puschDataConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPUSCHDemodulatedBits(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int8 bits[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPUSCHPTRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle puschptrsConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschptrsConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPUSCHPTRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschptrsConstellationI[], float32 puschptrsConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPUSCHPhaseOffsetTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 puschPhaseOffset[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPeakEVMHighPerSymbolMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMHighPerSymbolMaximum[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPeakEVMLowPerSymbolMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMLowPerSymbolMaximum[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPeakEVMPerSlotMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMPerSlotMaximum[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPeakEVMPerSubcarrierMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMPerSubcarrierMaximum[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchPeakEVMPerSymbolMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMPerSymbolMaximum[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchRMSEVMHighPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmHighPerSymbolMean[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchRMSEVMLowPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmLowPerSymbolMean[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchRMSEVMPerSlotMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmPerSlotMean[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchSSSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle sssConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchSSSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 sssConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchSSSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 sssConstellationI[], float32 sssConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 sssrmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchSSSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 sssrmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchSpectralFlatnessTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectralFlatness[], float32 spectralFlatnessLowerMask[], float32 spectralFlatnessUpperMask[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchSubblockInBandEmissionTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 subblockInBandEmission[], float64 subblockInBandEmissionMask[], float64 subblockInBandEmissionRBIndices[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchTransientPeriodLocationsTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 transientPeriodLocations[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccValidateCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* calibrationDataValid) override;
  int32 OBWCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) override;
  int32 OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType) override;
  int32 OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval) override;
  int32 OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* occupiedBandwidth, float64* absolutePower, float64* startFrequency, float64* stopFrequency) override;
  int32 OBWFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize) override;
  int32 PVTCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) override;
  int32 PVTCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod) override;
  int32 PVTCfgOFFPowerExclusionPeriods(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offPowerExclusionBefore, float64 offPowerExclusionAfter) override;
  int32 PVTFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* absoluteOFFPowerBefore, float64* absoluteOFFPowerAfter, float64* absoluteONPower, float64* burstWidth) override;
  int32 PVTFetchMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 absoluteOFFPowerBefore[], float64 absoluteOFFPowerAfter[], float64 absoluteONPower[], float64 burstWidth[], int32 arraySize, int32* actualArraySize) override;
  int32 PVTFetchSignalPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 signalPower[], float32 absoluteLimit[], int32 arraySize, int32* actualArraySize) override;
  int32 PVTFetchWindowedSignalPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 windowedSignalPower[], int32 arraySize, int32* actualArraySize) override;
  int32 ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID) override;
  int32 ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[]) override;
  int32 SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) override;
  int32 SEMCfgComponentCarrierRatedOutputPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 componentCarrierRatedOutputPower) override;
  int32 SEMCfgComponentCarrierRatedOutputPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 componentCarrierRatedOutputPower[], int32 numberOfElements) override;
  int32 SEMCfgNumberOfOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets) override;
  int32 SEMCfgOffsetAbsoluteLimit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 absoluteLimitStart, float64 absoluteLimitStop) override;
  int32 SEMCfgOffsetAbsoluteLimitArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 absoluteLimitStart[], float64 absoluteLimitStop[], int32 numberOfElements) override;
  int32 SEMCfgOffsetBandwidthIntegral(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandwidthIntegral) override;
  int32 SEMCfgOffsetBandwidthIntegralArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandwidthIntegral[], int32 numberOfElements) override;
  int32 SEMCfgOffsetFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetStartFrequency, float64 offsetStopFrequency, int32 offsetSideband) override;
  int32 SEMCfgOffsetFrequencyArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetStartFrequency[], float64 offsetStopFrequency[], int32 offsetSideband[], int32 numberOfElements) override;
  int32 SEMCfgOffsetLimitFailMask(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 limitFailMask) override;
  int32 SEMCfgOffsetLimitFailMaskArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 limitFailMask[], int32 numberOfElements) override;
  int32 SEMCfgOffsetRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetRBW, int32 offsetRBWFilterType) override;
  int32 SEMCfgOffsetRBWFilterArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetRBW[], int32 offsetRBWFilterType[], int32 numberOfElements) override;
  int32 SEMCfgOffsetRelativeLimit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 relativeLimitStart, float64 relativeLimitStop) override;
  int32 SEMCfgOffsetRelativeLimitArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 relativeLimitStart[], float64 relativeLimitStop[], int32 numberOfElements) override;
  int32 SEMCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval) override;
  int32 SEMCfgUplinkMaskType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 uplinkMaskType) override;
  int32 SEMFetchComponentCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absolutePower, float64* peakAbsolutePower, float64* peakFrequency, float64* relativePower) override;
  int32 SEMFetchComponentCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 relativePower[], int32 arraySize, int32* actualArraySize) override;
  int32 SEMFetchLowerOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower) override;
  int32 SEMFetchLowerOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize) override;
  int32 SEMFetchLowerOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAbsolutePower, float64* totalRelativePower, float64* peakAbsolutePower, float64* peakFrequency, float64* peakRelativePower) override;
  int32 SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 totalAbsolutePower[], float64 totalRelativePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 peakRelativePower[], int32 arraySize, int32* actualArraySize) override;
  int32 SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus) override;
  int32 SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], float32 compositeMask[], int32 arraySize, int32* actualArraySize) override;
  int32 SEMFetchSubblockMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* subblockPower, float64* integrationBandwidth, float64* frequency) override;
  int32 SEMFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAggregatedPower) override;
  int32 SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower) override;
  int32 SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize) override;
  int32 SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAbsolutePower, float64* totalRelativePower, float64* peakAbsolutePower, float64* peakFrequency, float64* peakRelativePower) override;
  int32 SEMFetchUpperOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 totalAbsolutePower[], float64 totalRelativePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 peakRelativePower[], int32 arraySize, int32* actualArraySize) override;
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
  int32 TXPFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* averagePowerMean, float64* peakPowerMaximum) override;
  int32 TXPFetchPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 power[], int32 arraySize, int32* actualArraySize) override;
  int32 WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout) override;
  int32 WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout) override;

 private:
  using ACPCfgAveragingPtr = decltype(&RFmxNR_ACPCfgAveraging);
  using ACPCfgMeasurementMethodPtr = decltype(&RFmxNR_ACPCfgMeasurementMethod);
  using ACPCfgNoiseCompensationEnabledPtr = decltype(&RFmxNR_ACPCfgNoiseCompensationEnabled);
  using ACPCfgNumberOfENDCOffsetsPtr = decltype(&RFmxNR_ACPCfgNumberOfENDCOffsets);
  using ACPCfgNumberOfEUTRAOffsetsPtr = decltype(&RFmxNR_ACPCfgNumberOfEUTRAOffsets);
  using ACPCfgNumberOfNROffsetsPtr = decltype(&RFmxNR_ACPCfgNumberOfNROffsets);
  using ACPCfgNumberOfUTRAOffsetsPtr = decltype(&RFmxNR_ACPCfgNumberOfUTRAOffsets);
  using ACPCfgPowerUnitsPtr = decltype(&RFmxNR_ACPCfgPowerUnits);
  using ACPCfgRBWFilterPtr = decltype(&RFmxNR_ACPCfgRBWFilter);
  using ACPCfgSweepTimePtr = decltype(&RFmxNR_ACPCfgSweepTime);
  using ACPFetchAbsolutePowersTracePtr = decltype(&RFmxNR_ACPFetchAbsolutePowersTrace);
  using ACPFetchComponentCarrierMeasurementPtr = decltype(&RFmxNR_ACPFetchComponentCarrierMeasurement);
  using ACPFetchComponentCarrierMeasurementArrayPtr = decltype(&RFmxNR_ACPFetchComponentCarrierMeasurementArray);
  using ACPFetchOffsetMeasurementPtr = decltype(&RFmxNR_ACPFetchOffsetMeasurement);
  using ACPFetchOffsetMeasurementArrayPtr = decltype(&RFmxNR_ACPFetchOffsetMeasurementArray);
  using ACPFetchRelativePowersTracePtr = decltype(&RFmxNR_ACPFetchRelativePowersTrace);
  using ACPFetchSpectrumPtr = decltype(&RFmxNR_ACPFetchSpectrum);
  using ACPFetchSubblockMeasurementPtr = decltype(&RFmxNR_ACPFetchSubblockMeasurement);
  using ACPFetchTotalAggregatedPowerPtr = decltype(&RFmxNR_ACPFetchTotalAggregatedPower);
  using ACPValidateNoiseCalibrationDataPtr = decltype(&RFmxNR_ACPValidateNoiseCalibrationData);
  using AbortMeasurementsPtr = decltype(&RFmxNR_AbortMeasurements);
  using AnalyzeIQ1WaveformPtr = decltype(&RFmxNR_AnalyzeIQ1Waveform);
  using AnalyzeIQ1WaveformInterleavedIQPtr = decltype(&RFmxNR_AnalyzeIQ1Waveform);
  using AnalyzeIQ1WaveformSplitPtr = decltype(&RFmxNR_AnalyzeIQ1WaveformSplit);
  using AnalyzeNWaveformsIQPtr = decltype(&RFmxNR_AnalyzeNWaveformsIQ);
  using AnalyzeNWaveformsIQInterleavedIQPtr = decltype(&RFmxNR_AnalyzeNWaveformsIQ);
  using AnalyzeNWaveformsIQSplitPtr = decltype(&RFmxNR_AnalyzeNWaveformsIQSplit);
  using AnalyzeNWaveformsSpectrumPtr = decltype(&RFmxNR_AnalyzeNWaveformsSpectrum);
  using AnalyzeSpectrum1WaveformPtr = decltype(&RFmxNR_AnalyzeSpectrum1Waveform);
  using AutoLevelPtr = decltype(&RFmxNR_AutoLevel);
  using BuildBandwidthPartStringPtr = decltype(&RFmxNR_BuildBandwidthPartString);
  using BuildCORESETClusterStringPtr = decltype(&RFmxNR_BuildCORESETClusterString);
  using BuildCORESETStringPtr = decltype(&RFmxNR_BuildCORESETString);
  using BuildCarrierStringPtr = decltype(&RFmxNR_BuildCarrierString);
  using BuildListStepStringPtr = decltype(&RFmxNR_BuildListStepString);
  using BuildListStringPtr = decltype(&RFmxNR_BuildListString);
  using BuildOffsetStringPtr = decltype(&RFmxNR_BuildOffsetString);
  using BuildPDCCHStringPtr = decltype(&RFmxNR_BuildPDCCHString);
  using BuildPDSCHClusterStringPtr = decltype(&RFmxNR_BuildPDSCHClusterString);
  using BuildPDSCHStringPtr = decltype(&RFmxNR_BuildPDSCHString);
  using BuildPUSCHClusterStringPtr = decltype(&RFmxNR_BuildPUSCHClusterString);
  using BuildPUSCHStringPtr = decltype(&RFmxNR_BuildPUSCHString);
  using BuildSignalStringPtr = decltype(&RFmxNR_BuildSignalString);
  using BuildSubblockStringPtr = decltype(&RFmxNR_BuildSubblockString);
  using BuildUserStringPtr = decltype(&RFmxNR_BuildUserString);
  using CHPCfgAveragingPtr = decltype(&RFmxNR_CHPCfgAveraging);
  using CHPCfgRBWFilterPtr = decltype(&RFmxNR_CHPCfgRBWFilter);
  using CHPCfgSweepTimePtr = decltype(&RFmxNR_CHPCfgSweepTime);
  using CHPFetchComponentCarrierMeasurementPtr = decltype(&RFmxNR_CHPFetchComponentCarrierMeasurement);
  using CHPFetchComponentCarrierMeasurementArrayPtr = decltype(&RFmxNR_CHPFetchComponentCarrierMeasurementArray);
  using CHPFetchSpectrumPtr = decltype(&RFmxNR_CHPFetchSpectrum);
  using CHPFetchSubblockPowerPtr = decltype(&RFmxNR_CHPFetchSubblockPower);
  using CHPFetchTotalAggregatedPowerPtr = decltype(&RFmxNR_CHPFetchTotalAggregatedPower);
  using CHPValidateNoiseCalibrationDataPtr = decltype(&RFmxNR_CHPValidateNoiseCalibrationData);
  using CfgDigitalEdgeTriggerPtr = decltype(&RFmxNR_CfgDigitalEdgeTrigger);
  using CfgExternalAttenuationPtr = decltype(&RFmxNR_CfgExternalAttenuation);
  using CfgFrequencyPtr = decltype(&RFmxNR_CfgFrequency);
  using CfgFrequencyReferencePtr = decltype(&RFmxNR_CfgFrequencyReference);
  using CfgIQPowerEdgeTriggerPtr = decltype(&RFmxNR_CfgIQPowerEdgeTrigger);
  using CfgMechanicalAttenuationPtr = decltype(&RFmxNR_CfgMechanicalAttenuation);
  using CfgRFPtr = decltype(&RFmxNR_CfgRF);
  using CfgRFAttenuationPtr = decltype(&RFmxNR_CfgRFAttenuation);
  using CfgReferenceLevelPtr = decltype(&RFmxNR_CfgReferenceLevel);
  using CfgSelectedPortsMultiplePtr = decltype(&RFmxNR_CfgSelectedPortsMultiple);
  using CfgSoftwareEdgeTriggerPtr = decltype(&RFmxNR_CfgSoftwareEdgeTrigger);
  using CfggNodeBCategoryPtr = decltype(&RFmxNR_CfggNodeBCategory);
  using CheckMeasurementStatusPtr = decltype(&RFmxNR_CheckMeasurementStatus);
  using ClearAllNamedResultsPtr = decltype(&RFmxNR_ClearAllNamedResults);
  using ClearNamedResultPtr = decltype(&RFmxNR_ClearNamedResult);
  using ClearNoiseCalibrationDatabasePtr = decltype(&RFmxNR_ClearNoiseCalibrationDatabase);
  using CloneSignalConfigurationPtr = decltype(&RFmxNR_CloneSignalConfiguration);
  using ClosePtr = decltype(&RFmxNR_Close);
  using CommitPtr = decltype(&RFmxNR_Commit);
  using CreateListPtr = decltype(&RFmxNR_CreateList);
  using CreateListStepPtr = decltype(&RFmxNR_CreateListStep);
  using CreateSignalConfigurationPtr = decltype(&RFmxNR_CreateSignalConfiguration);
  using DeleteListPtr = decltype(&RFmxNR_DeleteList);
  using DeleteSignalConfigurationPtr = decltype(&RFmxNR_DeleteSignalConfiguration);
  using DisableTriggerPtr = decltype(&RFmxNR_DisableTrigger);
  using GetAllNamedResultNamesPtr = decltype(&RFmxNR_GetAllNamedResultNames);
  using GetAttributeF32Ptr = decltype(&RFmxNR_GetAttributeF32);
  using GetAttributeF32ArrayPtr = decltype(&RFmxNR_GetAttributeF32Array);
  using GetAttributeF64Ptr = decltype(&RFmxNR_GetAttributeF64);
  using GetAttributeF64ArrayPtr = decltype(&RFmxNR_GetAttributeF64Array);
  using GetAttributeI16Ptr = decltype(&RFmxNR_GetAttributeI16);
  using GetAttributeI32Ptr = decltype(&RFmxNR_GetAttributeI32);
  using GetAttributeI32ArrayPtr = decltype(&RFmxNR_GetAttributeI32Array);
  using GetAttributeI64Ptr = decltype(&RFmxNR_GetAttributeI64);
  using GetAttributeI64ArrayPtr = decltype(&RFmxNR_GetAttributeI64Array);
  using GetAttributeI8Ptr = decltype(&RFmxNR_GetAttributeI8);
  using GetAttributeI8ArrayPtr = decltype(&RFmxNR_GetAttributeI8Array);
  using GetAttributeNIComplexDoubleArrayPtr = decltype(&RFmxNR_GetAttributeNIComplexDoubleArray);
  using GetAttributeNIComplexSingleArrayPtr = decltype(&RFmxNR_GetAttributeNIComplexSingleArray);
  using GetAttributeStringPtr = decltype(&RFmxNR_GetAttributeString);
  using GetAttributeU16Ptr = decltype(&RFmxNR_GetAttributeU16);
  using GetAttributeU32Ptr = decltype(&RFmxNR_GetAttributeU32);
  using GetAttributeU32ArrayPtr = decltype(&RFmxNR_GetAttributeU32Array);
  using GetAttributeU64ArrayPtr = decltype(&RFmxNR_GetAttributeU64Array);
  using GetAttributeU8Ptr = decltype(&RFmxNR_GetAttributeU8);
  using GetAttributeU8ArrayPtr = decltype(&RFmxNR_GetAttributeU8Array);
  using GetErrorPtr = decltype(&RFmxNR_GetError);
  using GetErrorStringPtr = decltype(&RFmxNR_GetErrorString);
  using InitializePtr = decltype(&RFmxNR_Initialize);
  using InitializeFromNIRFSASessionPtr = decltype(&RFmxNR_InitializeFromNIRFSASession);
  using InitiatePtr = decltype(&RFmxNR_Initiate);
  using LoadFromGenerationConfigurationFilePtr = decltype(&RFmxNR_LoadFromGenerationConfigurationFile);
  using ModAccAutoLevelPtr = decltype(&RFmxNR_ModAccAutoLevel);
  using ModAccCfgMeasurementModePtr = decltype(&RFmxNR_ModAccCfgMeasurementMode);
  using ModAccCfgNoiseCompensationEnabledPtr = decltype(&RFmxNR_ModAccCfgNoiseCompensationEnabled);
  using ModAccCfgReferenceWaveformPtr = decltype(&RFmxNR_ModAccCfgReferenceWaveform);
  using ModAccCfgReferenceWaveformInterleavedIQPtr = decltype(&RFmxNR_ModAccCfgReferenceWaveform);
  using ModAccCfgReferenceWaveformSplitPtr = decltype(&RFmxNR_ModAccCfgReferenceWaveformSplit);
  using ModAccClearNoiseCalibrationDatabasePtr = decltype(&RFmxNR_ModAccClearNoiseCalibrationDatabase);
  using ModAccFetchCompositeEVMPtr = decltype(&RFmxNR_ModAccFetchCompositeEVM);
  using ModAccFetchFrequencyErrorMeanPtr = decltype(&RFmxNR_ModAccFetchFrequencyErrorMean);
  using ModAccFetchFrequencyErrorPerSlotMaximumTracePtr = decltype(&RFmxNR_ModAccFetchFrequencyErrorPerSlotMaximumTrace);
  using ModAccFetchIQGainImbalancePerSubcarrierMeanTracePtr = decltype(&RFmxNR_ModAccFetchIQGainImbalancePerSubcarrierMeanTrace);
  using ModAccFetchIQQuadratureErrorPerSubcarrierMeanTracePtr = decltype(&RFmxNR_ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace);
  using ModAccFetchInBandEmissionTracePtr = decltype(&RFmxNR_ModAccFetchInBandEmissionTrace);
  using ModAccFetchPBCHDMRSConstellationTracePtr = decltype(&RFmxNR_ModAccFetchPBCHDMRSConstellationTrace);
  using ModAccFetchPBCHDMRSConstellationTraceInterleavedIQPtr = decltype(&RFmxNR_ModAccFetchPBCHDMRSConstellationTrace);
  using ModAccFetchPBCHDMRSConstellationTraceSplitPtr = decltype(&RFmxNR_ModAccFetchPBCHDMRSConstellationTraceSplit);
  using ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTracePtr = decltype(&RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace);
  using ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTracePtr = decltype(&RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace);
  using ModAccFetchPBCHDataConstellationTracePtr = decltype(&RFmxNR_ModAccFetchPBCHDataConstellationTrace);
  using ModAccFetchPBCHDataConstellationTraceInterleavedIQPtr = decltype(&RFmxNR_ModAccFetchPBCHDataConstellationTrace);
  using ModAccFetchPBCHDataConstellationTraceSplitPtr = decltype(&RFmxNR_ModAccFetchPBCHDataConstellationTraceSplit);
  using ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTracePtr = decltype(&RFmxNR_ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTrace);
  using ModAccFetchPBCHDataRMSEVMPerSymbolMeanTracePtr = decltype(&RFmxNR_ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace);
  using ModAccFetchPDSCH1024QAMConstellationTracePtr = decltype(&RFmxNR_ModAccFetchPDSCH1024QAMConstellationTrace);
  using ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQPtr = decltype(&RFmxNR_ModAccFetchPDSCH1024QAMConstellationTrace);
  using ModAccFetchPDSCH1024QAMConstellationTraceSplitPtr = decltype(&RFmxNR_ModAccFetchPDSCH1024QAMConstellationTraceSplit);
  using ModAccFetchPDSCH16QAMConstellationTracePtr = decltype(&RFmxNR_ModAccFetchPDSCH16QAMConstellationTrace);
  using ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQPtr = decltype(&RFmxNR_ModAccFetchPDSCH16QAMConstellationTrace);
  using ModAccFetchPDSCH16QAMConstellationTraceSplitPtr = decltype(&RFmxNR_ModAccFetchPDSCH16QAMConstellationTraceSplit);
  using ModAccFetchPDSCH256QAMConstellationTracePtr = decltype(&RFmxNR_ModAccFetchPDSCH256QAMConstellationTrace);
  using ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQPtr = decltype(&RFmxNR_ModAccFetchPDSCH256QAMConstellationTrace);
  using ModAccFetchPDSCH256QAMConstellationTraceSplitPtr = decltype(&RFmxNR_ModAccFetchPDSCH256QAMConstellationTraceSplit);
  using ModAccFetchPDSCH4096QAMConstellationTracePtr = decltype(&RFmxNR_ModAccFetchPDSCH4096QAMConstellationTrace);
  using ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQPtr = decltype(&RFmxNR_ModAccFetchPDSCH4096QAMConstellationTrace);
  using ModAccFetchPDSCH4096QAMConstellationTraceSplitPtr = decltype(&RFmxNR_ModAccFetchPDSCH4096QAMConstellationTraceSplit);
  using ModAccFetchPDSCH64QAMConstellationTracePtr = decltype(&RFmxNR_ModAccFetchPDSCH64QAMConstellationTrace);
  using ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQPtr = decltype(&RFmxNR_ModAccFetchPDSCH64QAMConstellationTrace);
  using ModAccFetchPDSCH64QAMConstellationTraceSplitPtr = decltype(&RFmxNR_ModAccFetchPDSCH64QAMConstellationTraceSplit);
  using ModAccFetchPDSCH8PSKConstellationTracePtr = decltype(&RFmxNR_ModAccFetchPDSCH8PSKConstellationTrace);
  using ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQPtr = decltype(&RFmxNR_ModAccFetchPDSCH8PSKConstellationTrace);
  using ModAccFetchPDSCH8PSKConstellationTraceSplitPtr = decltype(&RFmxNR_ModAccFetchPDSCH8PSKConstellationTraceSplit);
  using ModAccFetchPDSCHDMRSConstellationTracePtr = decltype(&RFmxNR_ModAccFetchPDSCHDMRSConstellationTrace);
  using ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQPtr = decltype(&RFmxNR_ModAccFetchPDSCHDMRSConstellationTrace);
  using ModAccFetchPDSCHDMRSConstellationTraceSplitPtr = decltype(&RFmxNR_ModAccFetchPDSCHDMRSConstellationTraceSplit);
  using ModAccFetchPDSCHDataConstellationTracePtr = decltype(&RFmxNR_ModAccFetchPDSCHDataConstellationTrace);
  using ModAccFetchPDSCHDataConstellationTraceInterleavedIQPtr = decltype(&RFmxNR_ModAccFetchPDSCHDataConstellationTrace);
  using ModAccFetchPDSCHDataConstellationTraceSplitPtr = decltype(&RFmxNR_ModAccFetchPDSCHDataConstellationTraceSplit);
  using ModAccFetchPDSCHDemodulatedBitsPtr = decltype(&RFmxNR_ModAccFetchPDSCHDemodulatedBits);
  using ModAccFetchPDSCHPTRSConstellationTracePtr = decltype(&RFmxNR_ModAccFetchPDSCHPTRSConstellationTrace);
  using ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQPtr = decltype(&RFmxNR_ModAccFetchPDSCHPTRSConstellationTrace);
  using ModAccFetchPDSCHPTRSConstellationTraceSplitPtr = decltype(&RFmxNR_ModAccFetchPDSCHPTRSConstellationTraceSplit);
  using ModAccFetchPDSCHQPSKConstellationTracePtr = decltype(&RFmxNR_ModAccFetchPDSCHQPSKConstellationTrace);
  using ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQPtr = decltype(&RFmxNR_ModAccFetchPDSCHQPSKConstellationTrace);
  using ModAccFetchPDSCHQPSKConstellationTraceSplitPtr = decltype(&RFmxNR_ModAccFetchPDSCHQPSKConstellationTraceSplit);
  using ModAccFetchPSSConstellationTracePtr = decltype(&RFmxNR_ModAccFetchPSSConstellationTrace);
  using ModAccFetchPSSConstellationTraceInterleavedIQPtr = decltype(&RFmxNR_ModAccFetchPSSConstellationTrace);
  using ModAccFetchPSSConstellationTraceSplitPtr = decltype(&RFmxNR_ModAccFetchPSSConstellationTraceSplit);
  using ModAccFetchPSSRMSEVMPerSubcarrierMeanTracePtr = decltype(&RFmxNR_ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace);
  using ModAccFetchPSSRMSEVMPerSymbolMeanTracePtr = decltype(&RFmxNR_ModAccFetchPSSRMSEVMPerSymbolMeanTrace);
  using ModAccFetchPUSCHDMRSConstellationTracePtr = decltype(&RFmxNR_ModAccFetchPUSCHDMRSConstellationTrace);
  using ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQPtr = decltype(&RFmxNR_ModAccFetchPUSCHDMRSConstellationTrace);
  using ModAccFetchPUSCHDMRSConstellationTraceSplitPtr = decltype(&RFmxNR_ModAccFetchPUSCHDMRSConstellationTraceSplit);
  using ModAccFetchPUSCHDataConstellationTracePtr = decltype(&RFmxNR_ModAccFetchPUSCHDataConstellationTrace);
  using ModAccFetchPUSCHDataConstellationTraceInterleavedIQPtr = decltype(&RFmxNR_ModAccFetchPUSCHDataConstellationTrace);
  using ModAccFetchPUSCHDataConstellationTraceSplitPtr = decltype(&RFmxNR_ModAccFetchPUSCHDataConstellationTraceSplit);
  using ModAccFetchPUSCHDemodulatedBitsPtr = decltype(&RFmxNR_ModAccFetchPUSCHDemodulatedBits);
  using ModAccFetchPUSCHPTRSConstellationTracePtr = decltype(&RFmxNR_ModAccFetchPUSCHPTRSConstellationTrace);
  using ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQPtr = decltype(&RFmxNR_ModAccFetchPUSCHPTRSConstellationTrace);
  using ModAccFetchPUSCHPTRSConstellationTraceSplitPtr = decltype(&RFmxNR_ModAccFetchPUSCHPTRSConstellationTraceSplit);
  using ModAccFetchPUSCHPhaseOffsetTracePtr = decltype(&RFmxNR_ModAccFetchPUSCHPhaseOffsetTrace);
  using ModAccFetchPeakEVMHighPerSymbolMaximumTracePtr = decltype(&RFmxNR_ModAccFetchPeakEVMHighPerSymbolMaximumTrace);
  using ModAccFetchPeakEVMLowPerSymbolMaximumTracePtr = decltype(&RFmxNR_ModAccFetchPeakEVMLowPerSymbolMaximumTrace);
  using ModAccFetchPeakEVMPerSlotMaximumTracePtr = decltype(&RFmxNR_ModAccFetchPeakEVMPerSlotMaximumTrace);
  using ModAccFetchPeakEVMPerSubcarrierMaximumTracePtr = decltype(&RFmxNR_ModAccFetchPeakEVMPerSubcarrierMaximumTrace);
  using ModAccFetchPeakEVMPerSymbolMaximumTracePtr = decltype(&RFmxNR_ModAccFetchPeakEVMPerSymbolMaximumTrace);
  using ModAccFetchRMSEVMHighPerSymbolMeanTracePtr = decltype(&RFmxNR_ModAccFetchRMSEVMHighPerSymbolMeanTrace);
  using ModAccFetchRMSEVMLowPerSymbolMeanTracePtr = decltype(&RFmxNR_ModAccFetchRMSEVMLowPerSymbolMeanTrace);
  using ModAccFetchRMSEVMPerSlotMeanTracePtr = decltype(&RFmxNR_ModAccFetchRMSEVMPerSlotMeanTrace);
  using ModAccFetchRMSEVMPerSubcarrierMeanTracePtr = decltype(&RFmxNR_ModAccFetchRMSEVMPerSubcarrierMeanTrace);
  using ModAccFetchRMSEVMPerSymbolMeanTracePtr = decltype(&RFmxNR_ModAccFetchRMSEVMPerSymbolMeanTrace);
  using ModAccFetchSSSConstellationTracePtr = decltype(&RFmxNR_ModAccFetchSSSConstellationTrace);
  using ModAccFetchSSSConstellationTraceInterleavedIQPtr = decltype(&RFmxNR_ModAccFetchSSSConstellationTrace);
  using ModAccFetchSSSConstellationTraceSplitPtr = decltype(&RFmxNR_ModAccFetchSSSConstellationTraceSplit);
  using ModAccFetchSSSRMSEVMPerSubcarrierMeanTracePtr = decltype(&RFmxNR_ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace);
  using ModAccFetchSSSRMSEVMPerSymbolMeanTracePtr = decltype(&RFmxNR_ModAccFetchSSSRMSEVMPerSymbolMeanTrace);
  using ModAccFetchSpectralFlatnessTracePtr = decltype(&RFmxNR_ModAccFetchSpectralFlatnessTrace);
  using ModAccFetchSubblockInBandEmissionTracePtr = decltype(&RFmxNR_ModAccFetchSubblockInBandEmissionTrace);
  using ModAccFetchTransientPeriodLocationsTracePtr = decltype(&RFmxNR_ModAccFetchTransientPeriodLocationsTrace);
  using ModAccValidateCalibrationDataPtr = decltype(&RFmxNR_ModAccValidateCalibrationData);
  using OBWCfgAveragingPtr = decltype(&RFmxNR_OBWCfgAveraging);
  using OBWCfgRBWFilterPtr = decltype(&RFmxNR_OBWCfgRBWFilter);
  using OBWCfgSweepTimePtr = decltype(&RFmxNR_OBWCfgSweepTime);
  using OBWFetchMeasurementPtr = decltype(&RFmxNR_OBWFetchMeasurement);
  using OBWFetchSpectrumPtr = decltype(&RFmxNR_OBWFetchSpectrum);
  using PVTCfgAveragingPtr = decltype(&RFmxNR_PVTCfgAveraging);
  using PVTCfgMeasurementMethodPtr = decltype(&RFmxNR_PVTCfgMeasurementMethod);
  using PVTCfgOFFPowerExclusionPeriodsPtr = decltype(&RFmxNR_PVTCfgOFFPowerExclusionPeriods);
  using PVTFetchMeasurementPtr = decltype(&RFmxNR_PVTFetchMeasurement);
  using PVTFetchMeasurementArrayPtr = decltype(&RFmxNR_PVTFetchMeasurementArray);
  using PVTFetchSignalPowerTracePtr = decltype(&RFmxNR_PVTFetchSignalPowerTrace);
  using PVTFetchWindowedSignalPowerTracePtr = decltype(&RFmxNR_PVTFetchWindowedSignalPowerTrace);
  using ResetAttributePtr = decltype(&RFmxNR_ResetAttribute);
  using ResetToDefaultPtr = decltype(&RFmxNR_ResetToDefault);
  using SEMCfgAveragingPtr = decltype(&RFmxNR_SEMCfgAveraging);
  using SEMCfgComponentCarrierRatedOutputPowerPtr = decltype(&RFmxNR_SEMCfgComponentCarrierRatedOutputPower);
  using SEMCfgComponentCarrierRatedOutputPowerArrayPtr = decltype(&RFmxNR_SEMCfgComponentCarrierRatedOutputPowerArray);
  using SEMCfgNumberOfOffsetsPtr = decltype(&RFmxNR_SEMCfgNumberOfOffsets);
  using SEMCfgOffsetAbsoluteLimitPtr = decltype(&RFmxNR_SEMCfgOffsetAbsoluteLimit);
  using SEMCfgOffsetAbsoluteLimitArrayPtr = decltype(&RFmxNR_SEMCfgOffsetAbsoluteLimitArray);
  using SEMCfgOffsetBandwidthIntegralPtr = decltype(&RFmxNR_SEMCfgOffsetBandwidthIntegral);
  using SEMCfgOffsetBandwidthIntegralArrayPtr = decltype(&RFmxNR_SEMCfgOffsetBandwidthIntegralArray);
  using SEMCfgOffsetFrequencyPtr = decltype(&RFmxNR_SEMCfgOffsetFrequency);
  using SEMCfgOffsetFrequencyArrayPtr = decltype(&RFmxNR_SEMCfgOffsetFrequencyArray);
  using SEMCfgOffsetLimitFailMaskPtr = decltype(&RFmxNR_SEMCfgOffsetLimitFailMask);
  using SEMCfgOffsetLimitFailMaskArrayPtr = decltype(&RFmxNR_SEMCfgOffsetLimitFailMaskArray);
  using SEMCfgOffsetRBWFilterPtr = decltype(&RFmxNR_SEMCfgOffsetRBWFilter);
  using SEMCfgOffsetRBWFilterArrayPtr = decltype(&RFmxNR_SEMCfgOffsetRBWFilterArray);
  using SEMCfgOffsetRelativeLimitPtr = decltype(&RFmxNR_SEMCfgOffsetRelativeLimit);
  using SEMCfgOffsetRelativeLimitArrayPtr = decltype(&RFmxNR_SEMCfgOffsetRelativeLimitArray);
  using SEMCfgSweepTimePtr = decltype(&RFmxNR_SEMCfgSweepTime);
  using SEMCfgUplinkMaskTypePtr = decltype(&RFmxNR_SEMCfgUplinkMaskType);
  using SEMFetchComponentCarrierMeasurementPtr = decltype(&RFmxNR_SEMFetchComponentCarrierMeasurement);
  using SEMFetchComponentCarrierMeasurementArrayPtr = decltype(&RFmxNR_SEMFetchComponentCarrierMeasurementArray);
  using SEMFetchLowerOffsetMarginPtr = decltype(&RFmxNR_SEMFetchLowerOffsetMargin);
  using SEMFetchLowerOffsetMarginArrayPtr = decltype(&RFmxNR_SEMFetchLowerOffsetMarginArray);
  using SEMFetchLowerOffsetPowerPtr = decltype(&RFmxNR_SEMFetchLowerOffsetPower);
  using SEMFetchLowerOffsetPowerArrayPtr = decltype(&RFmxNR_SEMFetchLowerOffsetPowerArray);
  using SEMFetchMeasurementStatusPtr = decltype(&RFmxNR_SEMFetchMeasurementStatus);
  using SEMFetchSpectrumPtr = decltype(&RFmxNR_SEMFetchSpectrum);
  using SEMFetchSubblockMeasurementPtr = decltype(&RFmxNR_SEMFetchSubblockMeasurement);
  using SEMFetchTotalAggregatedPowerPtr = decltype(&RFmxNR_SEMFetchTotalAggregatedPower);
  using SEMFetchUpperOffsetMarginPtr = decltype(&RFmxNR_SEMFetchUpperOffsetMargin);
  using SEMFetchUpperOffsetMarginArrayPtr = decltype(&RFmxNR_SEMFetchUpperOffsetMarginArray);
  using SEMFetchUpperOffsetPowerPtr = decltype(&RFmxNR_SEMFetchUpperOffsetPower);
  using SEMFetchUpperOffsetPowerArrayPtr = decltype(&RFmxNR_SEMFetchUpperOffsetPowerArray);
  using SelectMeasurementsPtr = decltype(&RFmxNR_SelectMeasurements);
  using SendSoftwareEdgeTriggerPtr = decltype(&RFmxNR_SendSoftwareEdgeTrigger);
  using SetAttributeF32Ptr = decltype(&RFmxNR_SetAttributeF32);
  using SetAttributeF32ArrayPtr = decltype(&RFmxNR_SetAttributeF32Array);
  using SetAttributeF64Ptr = decltype(&RFmxNR_SetAttributeF64);
  using SetAttributeF64ArrayPtr = decltype(&RFmxNR_SetAttributeF64Array);
  using SetAttributeI16Ptr = decltype(&RFmxNR_SetAttributeI16);
  using SetAttributeI32Ptr = decltype(&RFmxNR_SetAttributeI32);
  using SetAttributeI32ArrayPtr = decltype(&RFmxNR_SetAttributeI32Array);
  using SetAttributeI64Ptr = decltype(&RFmxNR_SetAttributeI64);
  using SetAttributeI64ArrayPtr = decltype(&RFmxNR_SetAttributeI64Array);
  using SetAttributeI8Ptr = decltype(&RFmxNR_SetAttributeI8);
  using SetAttributeI8ArrayPtr = decltype(&RFmxNR_SetAttributeI8Array);
  using SetAttributeNIComplexDoubleArrayPtr = decltype(&RFmxNR_SetAttributeNIComplexDoubleArray);
  using SetAttributeNIComplexSingleArrayPtr = decltype(&RFmxNR_SetAttributeNIComplexSingleArray);
  using SetAttributeStringPtr = decltype(&RFmxNR_SetAttributeString);
  using SetAttributeU16Ptr = decltype(&RFmxNR_SetAttributeU16);
  using SetAttributeU32Ptr = decltype(&RFmxNR_SetAttributeU32);
  using SetAttributeU32ArrayPtr = decltype(&RFmxNR_SetAttributeU32Array);
  using SetAttributeU64ArrayPtr = decltype(&RFmxNR_SetAttributeU64Array);
  using SetAttributeU8Ptr = decltype(&RFmxNR_SetAttributeU8);
  using SetAttributeU8ArrayPtr = decltype(&RFmxNR_SetAttributeU8Array);
  using TXPFetchMeasurementPtr = decltype(&RFmxNR_TXPFetchMeasurement);
  using TXPFetchPowerTracePtr = decltype(&RFmxNR_TXPFetchPowerTrace);
  using WaitForAcquisitionCompletePtr = decltype(&RFmxNR_WaitForAcquisitionComplete);
  using WaitForMeasurementCompletePtr = decltype(&RFmxNR_WaitForMeasurementComplete);

  typedef struct FunctionPointers {
    ACPCfgAveragingPtr ACPCfgAveraging;
    ACPCfgMeasurementMethodPtr ACPCfgMeasurementMethod;
    ACPCfgNoiseCompensationEnabledPtr ACPCfgNoiseCompensationEnabled;
    ACPCfgNumberOfENDCOffsetsPtr ACPCfgNumberOfENDCOffsets;
    ACPCfgNumberOfEUTRAOffsetsPtr ACPCfgNumberOfEUTRAOffsets;
    ACPCfgNumberOfNROffsetsPtr ACPCfgNumberOfNROffsets;
    ACPCfgNumberOfUTRAOffsetsPtr ACPCfgNumberOfUTRAOffsets;
    ACPCfgPowerUnitsPtr ACPCfgPowerUnits;
    ACPCfgRBWFilterPtr ACPCfgRBWFilter;
    ACPCfgSweepTimePtr ACPCfgSweepTime;
    ACPFetchAbsolutePowersTracePtr ACPFetchAbsolutePowersTrace;
    ACPFetchComponentCarrierMeasurementPtr ACPFetchComponentCarrierMeasurement;
    ACPFetchComponentCarrierMeasurementArrayPtr ACPFetchComponentCarrierMeasurementArray;
    ACPFetchOffsetMeasurementPtr ACPFetchOffsetMeasurement;
    ACPFetchOffsetMeasurementArrayPtr ACPFetchOffsetMeasurementArray;
    ACPFetchRelativePowersTracePtr ACPFetchRelativePowersTrace;
    ACPFetchSpectrumPtr ACPFetchSpectrum;
    ACPFetchSubblockMeasurementPtr ACPFetchSubblockMeasurement;
    ACPFetchTotalAggregatedPowerPtr ACPFetchTotalAggregatedPower;
    ACPValidateNoiseCalibrationDataPtr ACPValidateNoiseCalibrationData;
    AbortMeasurementsPtr AbortMeasurements;
    AnalyzeIQ1WaveformPtr AnalyzeIQ1Waveform;
    AnalyzeIQ1WaveformInterleavedIQPtr AnalyzeIQ1WaveformInterleavedIQ;
    AnalyzeIQ1WaveformSplitPtr AnalyzeIQ1WaveformSplit;
    AnalyzeNWaveformsIQPtr AnalyzeNWaveformsIQ;
    AnalyzeNWaveformsIQInterleavedIQPtr AnalyzeNWaveformsIQInterleavedIQ;
    AnalyzeNWaveformsIQSplitPtr AnalyzeNWaveformsIQSplit;
    AnalyzeNWaveformsSpectrumPtr AnalyzeNWaveformsSpectrum;
    AnalyzeSpectrum1WaveformPtr AnalyzeSpectrum1Waveform;
    AutoLevelPtr AutoLevel;
    BuildBandwidthPartStringPtr BuildBandwidthPartString;
    BuildCORESETClusterStringPtr BuildCORESETClusterString;
    BuildCORESETStringPtr BuildCORESETString;
    BuildCarrierStringPtr BuildCarrierString;
    BuildListStepStringPtr BuildListStepString;
    BuildListStringPtr BuildListString;
    BuildOffsetStringPtr BuildOffsetString;
    BuildPDCCHStringPtr BuildPDCCHString;
    BuildPDSCHClusterStringPtr BuildPDSCHClusterString;
    BuildPDSCHStringPtr BuildPDSCHString;
    BuildPUSCHClusterStringPtr BuildPUSCHClusterString;
    BuildPUSCHStringPtr BuildPUSCHString;
    BuildSignalStringPtr BuildSignalString;
    BuildSubblockStringPtr BuildSubblockString;
    BuildUserStringPtr BuildUserString;
    CHPCfgAveragingPtr CHPCfgAveraging;
    CHPCfgRBWFilterPtr CHPCfgRBWFilter;
    CHPCfgSweepTimePtr CHPCfgSweepTime;
    CHPFetchComponentCarrierMeasurementPtr CHPFetchComponentCarrierMeasurement;
    CHPFetchComponentCarrierMeasurementArrayPtr CHPFetchComponentCarrierMeasurementArray;
    CHPFetchSpectrumPtr CHPFetchSpectrum;
    CHPFetchSubblockPowerPtr CHPFetchSubblockPower;
    CHPFetchTotalAggregatedPowerPtr CHPFetchTotalAggregatedPower;
    CHPValidateNoiseCalibrationDataPtr CHPValidateNoiseCalibrationData;
    CfgDigitalEdgeTriggerPtr CfgDigitalEdgeTrigger;
    CfgExternalAttenuationPtr CfgExternalAttenuation;
    CfgFrequencyPtr CfgFrequency;
    CfgFrequencyReferencePtr CfgFrequencyReference;
    CfgIQPowerEdgeTriggerPtr CfgIQPowerEdgeTrigger;
    CfgMechanicalAttenuationPtr CfgMechanicalAttenuation;
    CfgRFPtr CfgRF;
    CfgRFAttenuationPtr CfgRFAttenuation;
    CfgReferenceLevelPtr CfgReferenceLevel;
    CfgSelectedPortsMultiplePtr CfgSelectedPortsMultiple;
    CfgSoftwareEdgeTriggerPtr CfgSoftwareEdgeTrigger;
    CfggNodeBCategoryPtr CfggNodeBCategory;
    CheckMeasurementStatusPtr CheckMeasurementStatus;
    ClearAllNamedResultsPtr ClearAllNamedResults;
    ClearNamedResultPtr ClearNamedResult;
    ClearNoiseCalibrationDatabasePtr ClearNoiseCalibrationDatabase;
    CloneSignalConfigurationPtr CloneSignalConfiguration;
    ClosePtr Close;
    CommitPtr Commit;
    CreateListPtr CreateList;
    CreateListStepPtr CreateListStep;
    CreateSignalConfigurationPtr CreateSignalConfiguration;
    DeleteListPtr DeleteList;
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
    LoadFromGenerationConfigurationFilePtr LoadFromGenerationConfigurationFile;
    ModAccAutoLevelPtr ModAccAutoLevel;
    ModAccCfgMeasurementModePtr ModAccCfgMeasurementMode;
    ModAccCfgNoiseCompensationEnabledPtr ModAccCfgNoiseCompensationEnabled;
    ModAccCfgReferenceWaveformPtr ModAccCfgReferenceWaveform;
    ModAccCfgReferenceWaveformInterleavedIQPtr ModAccCfgReferenceWaveformInterleavedIQ;
    ModAccCfgReferenceWaveformSplitPtr ModAccCfgReferenceWaveformSplit;
    ModAccClearNoiseCalibrationDatabasePtr ModAccClearNoiseCalibrationDatabase;
    ModAccFetchCompositeEVMPtr ModAccFetchCompositeEVM;
    ModAccFetchFrequencyErrorMeanPtr ModAccFetchFrequencyErrorMean;
    ModAccFetchFrequencyErrorPerSlotMaximumTracePtr ModAccFetchFrequencyErrorPerSlotMaximumTrace;
    ModAccFetchIQGainImbalancePerSubcarrierMeanTracePtr ModAccFetchIQGainImbalancePerSubcarrierMeanTrace;
    ModAccFetchIQQuadratureErrorPerSubcarrierMeanTracePtr ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace;
    ModAccFetchInBandEmissionTracePtr ModAccFetchInBandEmissionTrace;
    ModAccFetchPBCHDMRSConstellationTracePtr ModAccFetchPBCHDMRSConstellationTrace;
    ModAccFetchPBCHDMRSConstellationTraceInterleavedIQPtr ModAccFetchPBCHDMRSConstellationTraceInterleavedIQ;
    ModAccFetchPBCHDMRSConstellationTraceSplitPtr ModAccFetchPBCHDMRSConstellationTraceSplit;
    ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTracePtr ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace;
    ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTracePtr ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace;
    ModAccFetchPBCHDataConstellationTracePtr ModAccFetchPBCHDataConstellationTrace;
    ModAccFetchPBCHDataConstellationTraceInterleavedIQPtr ModAccFetchPBCHDataConstellationTraceInterleavedIQ;
    ModAccFetchPBCHDataConstellationTraceSplitPtr ModAccFetchPBCHDataConstellationTraceSplit;
    ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTracePtr ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTrace;
    ModAccFetchPBCHDataRMSEVMPerSymbolMeanTracePtr ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace;
    ModAccFetchPDSCH1024QAMConstellationTracePtr ModAccFetchPDSCH1024QAMConstellationTrace;
    ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQPtr ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQ;
    ModAccFetchPDSCH1024QAMConstellationTraceSplitPtr ModAccFetchPDSCH1024QAMConstellationTraceSplit;
    ModAccFetchPDSCH16QAMConstellationTracePtr ModAccFetchPDSCH16QAMConstellationTrace;
    ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQPtr ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQ;
    ModAccFetchPDSCH16QAMConstellationTraceSplitPtr ModAccFetchPDSCH16QAMConstellationTraceSplit;
    ModAccFetchPDSCH256QAMConstellationTracePtr ModAccFetchPDSCH256QAMConstellationTrace;
    ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQPtr ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQ;
    ModAccFetchPDSCH256QAMConstellationTraceSplitPtr ModAccFetchPDSCH256QAMConstellationTraceSplit;
    ModAccFetchPDSCH4096QAMConstellationTracePtr ModAccFetchPDSCH4096QAMConstellationTrace;
    ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQPtr ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQ;
    ModAccFetchPDSCH4096QAMConstellationTraceSplitPtr ModAccFetchPDSCH4096QAMConstellationTraceSplit;
    ModAccFetchPDSCH64QAMConstellationTracePtr ModAccFetchPDSCH64QAMConstellationTrace;
    ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQPtr ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQ;
    ModAccFetchPDSCH64QAMConstellationTraceSplitPtr ModAccFetchPDSCH64QAMConstellationTraceSplit;
    ModAccFetchPDSCH8PSKConstellationTracePtr ModAccFetchPDSCH8PSKConstellationTrace;
    ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQPtr ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQ;
    ModAccFetchPDSCH8PSKConstellationTraceSplitPtr ModAccFetchPDSCH8PSKConstellationTraceSplit;
    ModAccFetchPDSCHDMRSConstellationTracePtr ModAccFetchPDSCHDMRSConstellationTrace;
    ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQPtr ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQ;
    ModAccFetchPDSCHDMRSConstellationTraceSplitPtr ModAccFetchPDSCHDMRSConstellationTraceSplit;
    ModAccFetchPDSCHDataConstellationTracePtr ModAccFetchPDSCHDataConstellationTrace;
    ModAccFetchPDSCHDataConstellationTraceInterleavedIQPtr ModAccFetchPDSCHDataConstellationTraceInterleavedIQ;
    ModAccFetchPDSCHDataConstellationTraceSplitPtr ModAccFetchPDSCHDataConstellationTraceSplit;
    ModAccFetchPDSCHDemodulatedBitsPtr ModAccFetchPDSCHDemodulatedBits;
    ModAccFetchPDSCHPTRSConstellationTracePtr ModAccFetchPDSCHPTRSConstellationTrace;
    ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQPtr ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQ;
    ModAccFetchPDSCHPTRSConstellationTraceSplitPtr ModAccFetchPDSCHPTRSConstellationTraceSplit;
    ModAccFetchPDSCHQPSKConstellationTracePtr ModAccFetchPDSCHQPSKConstellationTrace;
    ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQPtr ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQ;
    ModAccFetchPDSCHQPSKConstellationTraceSplitPtr ModAccFetchPDSCHQPSKConstellationTraceSplit;
    ModAccFetchPSSConstellationTracePtr ModAccFetchPSSConstellationTrace;
    ModAccFetchPSSConstellationTraceInterleavedIQPtr ModAccFetchPSSConstellationTraceInterleavedIQ;
    ModAccFetchPSSConstellationTraceSplitPtr ModAccFetchPSSConstellationTraceSplit;
    ModAccFetchPSSRMSEVMPerSubcarrierMeanTracePtr ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace;
    ModAccFetchPSSRMSEVMPerSymbolMeanTracePtr ModAccFetchPSSRMSEVMPerSymbolMeanTrace;
    ModAccFetchPUSCHDMRSConstellationTracePtr ModAccFetchPUSCHDMRSConstellationTrace;
    ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQPtr ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQ;
    ModAccFetchPUSCHDMRSConstellationTraceSplitPtr ModAccFetchPUSCHDMRSConstellationTraceSplit;
    ModAccFetchPUSCHDataConstellationTracePtr ModAccFetchPUSCHDataConstellationTrace;
    ModAccFetchPUSCHDataConstellationTraceInterleavedIQPtr ModAccFetchPUSCHDataConstellationTraceInterleavedIQ;
    ModAccFetchPUSCHDataConstellationTraceSplitPtr ModAccFetchPUSCHDataConstellationTraceSplit;
    ModAccFetchPUSCHDemodulatedBitsPtr ModAccFetchPUSCHDemodulatedBits;
    ModAccFetchPUSCHPTRSConstellationTracePtr ModAccFetchPUSCHPTRSConstellationTrace;
    ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQPtr ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQ;
    ModAccFetchPUSCHPTRSConstellationTraceSplitPtr ModAccFetchPUSCHPTRSConstellationTraceSplit;
    ModAccFetchPUSCHPhaseOffsetTracePtr ModAccFetchPUSCHPhaseOffsetTrace;
    ModAccFetchPeakEVMHighPerSymbolMaximumTracePtr ModAccFetchPeakEVMHighPerSymbolMaximumTrace;
    ModAccFetchPeakEVMLowPerSymbolMaximumTracePtr ModAccFetchPeakEVMLowPerSymbolMaximumTrace;
    ModAccFetchPeakEVMPerSlotMaximumTracePtr ModAccFetchPeakEVMPerSlotMaximumTrace;
    ModAccFetchPeakEVMPerSubcarrierMaximumTracePtr ModAccFetchPeakEVMPerSubcarrierMaximumTrace;
    ModAccFetchPeakEVMPerSymbolMaximumTracePtr ModAccFetchPeakEVMPerSymbolMaximumTrace;
    ModAccFetchRMSEVMHighPerSymbolMeanTracePtr ModAccFetchRMSEVMHighPerSymbolMeanTrace;
    ModAccFetchRMSEVMLowPerSymbolMeanTracePtr ModAccFetchRMSEVMLowPerSymbolMeanTrace;
    ModAccFetchRMSEVMPerSlotMeanTracePtr ModAccFetchRMSEVMPerSlotMeanTrace;
    ModAccFetchRMSEVMPerSubcarrierMeanTracePtr ModAccFetchRMSEVMPerSubcarrierMeanTrace;
    ModAccFetchRMSEVMPerSymbolMeanTracePtr ModAccFetchRMSEVMPerSymbolMeanTrace;
    ModAccFetchSSSConstellationTracePtr ModAccFetchSSSConstellationTrace;
    ModAccFetchSSSConstellationTraceInterleavedIQPtr ModAccFetchSSSConstellationTraceInterleavedIQ;
    ModAccFetchSSSConstellationTraceSplitPtr ModAccFetchSSSConstellationTraceSplit;
    ModAccFetchSSSRMSEVMPerSubcarrierMeanTracePtr ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace;
    ModAccFetchSSSRMSEVMPerSymbolMeanTracePtr ModAccFetchSSSRMSEVMPerSymbolMeanTrace;
    ModAccFetchSpectralFlatnessTracePtr ModAccFetchSpectralFlatnessTrace;
    ModAccFetchSubblockInBandEmissionTracePtr ModAccFetchSubblockInBandEmissionTrace;
    ModAccFetchTransientPeriodLocationsTracePtr ModAccFetchTransientPeriodLocationsTrace;
    ModAccValidateCalibrationDataPtr ModAccValidateCalibrationData;
    OBWCfgAveragingPtr OBWCfgAveraging;
    OBWCfgRBWFilterPtr OBWCfgRBWFilter;
    OBWCfgSweepTimePtr OBWCfgSweepTime;
    OBWFetchMeasurementPtr OBWFetchMeasurement;
    OBWFetchSpectrumPtr OBWFetchSpectrum;
    PVTCfgAveragingPtr PVTCfgAveraging;
    PVTCfgMeasurementMethodPtr PVTCfgMeasurementMethod;
    PVTCfgOFFPowerExclusionPeriodsPtr PVTCfgOFFPowerExclusionPeriods;
    PVTFetchMeasurementPtr PVTFetchMeasurement;
    PVTFetchMeasurementArrayPtr PVTFetchMeasurementArray;
    PVTFetchSignalPowerTracePtr PVTFetchSignalPowerTrace;
    PVTFetchWindowedSignalPowerTracePtr PVTFetchWindowedSignalPowerTrace;
    ResetAttributePtr ResetAttribute;
    ResetToDefaultPtr ResetToDefault;
    SEMCfgAveragingPtr SEMCfgAveraging;
    SEMCfgComponentCarrierRatedOutputPowerPtr SEMCfgComponentCarrierRatedOutputPower;
    SEMCfgComponentCarrierRatedOutputPowerArrayPtr SEMCfgComponentCarrierRatedOutputPowerArray;
    SEMCfgNumberOfOffsetsPtr SEMCfgNumberOfOffsets;
    SEMCfgOffsetAbsoluteLimitPtr SEMCfgOffsetAbsoluteLimit;
    SEMCfgOffsetAbsoluteLimitArrayPtr SEMCfgOffsetAbsoluteLimitArray;
    SEMCfgOffsetBandwidthIntegralPtr SEMCfgOffsetBandwidthIntegral;
    SEMCfgOffsetBandwidthIntegralArrayPtr SEMCfgOffsetBandwidthIntegralArray;
    SEMCfgOffsetFrequencyPtr SEMCfgOffsetFrequency;
    SEMCfgOffsetFrequencyArrayPtr SEMCfgOffsetFrequencyArray;
    SEMCfgOffsetLimitFailMaskPtr SEMCfgOffsetLimitFailMask;
    SEMCfgOffsetLimitFailMaskArrayPtr SEMCfgOffsetLimitFailMaskArray;
    SEMCfgOffsetRBWFilterPtr SEMCfgOffsetRBWFilter;
    SEMCfgOffsetRBWFilterArrayPtr SEMCfgOffsetRBWFilterArray;
    SEMCfgOffsetRelativeLimitPtr SEMCfgOffsetRelativeLimit;
    SEMCfgOffsetRelativeLimitArrayPtr SEMCfgOffsetRelativeLimitArray;
    SEMCfgSweepTimePtr SEMCfgSweepTime;
    SEMCfgUplinkMaskTypePtr SEMCfgUplinkMaskType;
    SEMFetchComponentCarrierMeasurementPtr SEMFetchComponentCarrierMeasurement;
    SEMFetchComponentCarrierMeasurementArrayPtr SEMFetchComponentCarrierMeasurementArray;
    SEMFetchLowerOffsetMarginPtr SEMFetchLowerOffsetMargin;
    SEMFetchLowerOffsetMarginArrayPtr SEMFetchLowerOffsetMarginArray;
    SEMFetchLowerOffsetPowerPtr SEMFetchLowerOffsetPower;
    SEMFetchLowerOffsetPowerArrayPtr SEMFetchLowerOffsetPowerArray;
    SEMFetchMeasurementStatusPtr SEMFetchMeasurementStatus;
    SEMFetchSpectrumPtr SEMFetchSpectrum;
    SEMFetchSubblockMeasurementPtr SEMFetchSubblockMeasurement;
    SEMFetchTotalAggregatedPowerPtr SEMFetchTotalAggregatedPower;
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
    TXPFetchMeasurementPtr TXPFetchMeasurement;
    TXPFetchPowerTracePtr TXPFetchPowerTrace;
    WaitForAcquisitionCompletePtr WaitForAcquisitionComplete;
    WaitForMeasurementCompletePtr WaitForMeasurementComplete;
  } FunctionLoadStatus;

  std::shared_ptr<nidevice_grpc::SharedLibraryInterface> shared_library_;
  FunctionPointers function_pointers_;
};

}  // namespace nirfmxnr_grpc

#endif  // NIRFMXNR_GRPC_LIBRARY_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/nirfmxnr/nirfmxnr_library_interface.h sha256=ca176d89c5ce7301af4f5364a74303e3ea958df5240aff5fc56a90f015e65c0c bytes=50171 -->
## FILE: generated/nirfmxnr/nirfmxnr_library_interface.h

- repository: `ni/grpc-device`
- source_path: `generated/nirfmxnr/nirfmxnr_library_interface.h`
- sha256: `ca176d89c5ce7301af4f5364a74303e3ea958df5240aff5fc56a90f015e65c0c`
- bytes: 50171

````c
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Library wrapper for implementing interactions with NI-RFMXNR
//---------------------------------------------------------------------
#ifndef NIRFMXNR_GRPC_LIBRARY_WRAPPER_H
#define NIRFMXNR_GRPC_LIBRARY_WRAPPER_H

#include <grpcpp/grpcpp.h>
#include <niRFmxNR.h>

namespace nirfmxnr_grpc {

class NiRFmxNRLibraryInterface {
 public:
  virtual ~NiRFmxNRLibraryInterface() {}

  virtual int32 ACPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) = 0;
  virtual int32 ACPCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod) = 0;
  virtual int32 ACPCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled) = 0;
  virtual int32 ACPCfgNumberOfENDCOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfENDCOffsets) = 0;
  virtual int32 ACPCfgNumberOfEUTRAOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfEUTRAOffsets) = 0;
  virtual int32 ACPCfgNumberOfNROffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfNROffsets) = 0;
  virtual int32 ACPCfgNumberOfUTRAOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfUTRAOffsets) = 0;
  virtual int32 ACPCfgPowerUnits(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnits) = 0;
  virtual int32 ACPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType) = 0;
  virtual int32 ACPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval) = 0;
  virtual int32 ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 absolutePowersTrace[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ACPFetchComponentCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absolutePower, float64* relativePower) = 0;
  virtual int32 ACPFetchComponentCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 relativePower[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* lowerRelativePower, float64* upperRelativePower, float64* lowerAbsolutePower, float64* upperAbsolutePower) = 0;
  virtual int32 ACPFetchOffsetMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 lowerRelativePower[], float64 upperRelativePower[], float64 lowerAbsolutePower[], float64 upperAbsolutePower[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 relativePowersTrace[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ACPFetchSubblockMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* subblockPower, float64* integrationBandwidth, float64* frequency) = 0;
  virtual int32 ACPFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAggregatedPower) = 0;
  virtual int32 ACPValidateNoiseCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* noiseCalibrationDataValid) = 0;
  virtual int32 AbortMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[]) = 0;
  virtual int32 AnalyzeIQ1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved) = 0;
  virtual int32 AnalyzeIQ1WaveformInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iq[], int32 arraySize, int32 reset, int64 reserved) = 0;
  virtual int32 AnalyzeIQ1WaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iqi[], float32 iqq[], int32 arraySize, int32 reset, int64 reserved) = 0;
  virtual int32 AnalyzeNWaveformsIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], NIComplexSingle iq[], int32 iqSize[], int32 arraySize, int32 reset) = 0;
  virtual int32 AnalyzeNWaveformsIQInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], float32 iq[], int32 iqSize[], int32 arraySize, int32 reset) = 0;
  virtual int32 AnalyzeNWaveformsIQSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], float32 iqi[], float32 iqq[], int32 iqSize[], int32 arraySize, int32 reset) = 0;
  virtual int32 AnalyzeNWaveformsSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], float32 spectrum[], int32 spectrumSize[], int32 arraySize, int32 reset) = 0;
  virtual int32 AnalyzeSpectrum1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 spectrum[], int32 arraySize, int32 reset, int64 reserved) = 0;
  virtual int32 AutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval, float64* referenceLevel) = 0;
  virtual int32 BuildBandwidthPartString(char selectorString[], int32 bandwidthPartNumber, int32 selectorStringOutLength, char selectorStringOut[]) = 0;
  virtual int32 BuildCORESETClusterString(char selectorString[], int32 coresetClusterNumber, int32 selectorStringOutLength, char selectorStringOut[]) = 0;
  virtual int32 BuildCORESETString(char selectorString[], int32 coresetNumber, int32 selectorStringOutLength, char selectorStringOut[]) = 0;
  virtual int32 BuildCarrierString(char selectorString[], int32 carrierNumber, int32 selectorStringOutLength, char selectorStringOut[]) = 0;
  virtual int32 BuildListStepString(char listName[], char resultName[], int32 stepNumber, int32 selectorStringLength, char selectorString[]) = 0;
  virtual int32 BuildListString(char listName[], char resultName[], int32 selectorStringLength, char selectorString[]) = 0;
  virtual int32 BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[]) = 0;
  virtual int32 BuildPDCCHString(char selectorString[], int32 pdcchNumber, int32 selectorStringOutLength, char selectorStringOut[]) = 0;
  virtual int32 BuildPDSCHClusterString(char selectorString[], int32 pdschClusterNumber, int32 selectorStringOutLength, char selectorStringOut[]) = 0;
  virtual int32 BuildPDSCHString(char selectorString[], int32 pdschNumber, int32 selectorStringOutLength, char selectorStringOut[]) = 0;
  virtual int32 BuildPUSCHClusterString(char selectorString[], int32 puschClusterNumber, int32 selectorStringOutLength, char selectorStringOut[]) = 0;
  virtual int32 BuildPUSCHString(char selectorString[], int32 puschNumber, int32 selectorStringOutLength, char selectorStringOut[]) = 0;
  virtual int32 BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[]) = 0;
  virtual int32 BuildSubblockString(char selectorString[], int32 subblockNumber, int32 selectorStringOutLength, char selectorStringOut[]) = 0;
  virtual int32 BuildUserString(char selectorString[], int32 userNumber, int32 selectorStringOutLength, char selectorStringOut[]) = 0;
  virtual int32 CHPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) = 0;
  virtual int32 CHPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType) = 0;
  virtual int32 CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval) = 0;
  virtual int32 CHPFetchComponentCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absolutePower, float64* relativePower) = 0;
  virtual int32 CHPFetchComponentCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 relativePower[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 CHPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 CHPFetchSubblockPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* subblockPower) = 0;
  virtual int32 CHPFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAggregatedPower) = 0;
  virtual int32 CHPValidateNoiseCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* noiseCalibrationDataValid) = 0;
  virtual int32 CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger) = 0;
  virtual int32 CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation) = 0;
  virtual int32 CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency) = 0;
  virtual int32 CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency) = 0;
  virtual int32 CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdgeSlope, float64 iqPowerEdgeLevel, float64 triggerDelay, int32 triggerMinQuietTimeMode, float64 triggerMinQuietTimeDuration, int32 iqPowerEdgeLevelType, int32 enableTrigger) = 0;
  virtual int32 CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue) = 0;
  virtual int32 CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation) = 0;
  virtual int32 CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue) = 0;
  virtual int32 CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel) = 0;
  virtual int32 CfgSelectedPortsMultiple(niRFmxInstrHandle instrumentHandle, char selectorString[], char selectedPorts[]) = 0;
  virtual int32 CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger) = 0;
  virtual int32 CfggNodeBCategory(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 gNodeBCategory) = 0;
  virtual int32 CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* isDone) = 0;
  virtual int32 ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[]) = 0;
  virtual int32 ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[]) = 0;
  virtual int32 ClearNoiseCalibrationDatabase(niRFmxInstrHandle instrumentHandle, char selectorString[]) = 0;
  virtual int32 CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[]) = 0;
  virtual int32 Close(niRFmxInstrHandle instrumentHandle, int32 forceDestroy) = 0;
  virtual int32 Commit(niRFmxInstrHandle instrumentHandle, char selectorString[]) = 0;
  virtual int32 CreateList(niRFmxInstrHandle instrumentHandle, char listName[]) = 0;
  virtual int32 CreateListStep(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* createdStepIndex) = 0;
  virtual int32 CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[]) = 0;
  virtual int32 DeleteList(niRFmxInstrHandle instrumentHandle, char listName[]) = 0;
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
  virtual int32 LoadFromGenerationConfigurationFile(niRFmxInstrHandle instrumentHandle, char selectorString[], char filePath[], int32 configurationIndex) = 0;
  virtual int32 ModAccAutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout) = 0;
  virtual int32 ModAccCfgMeasurementMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMode) = 0;
  virtual int32 ModAccCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled) = 0;
  virtual int32 ModAccCfgReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, NIComplexSingle referenceWaveform[], int32 arraySize) = 0;
  virtual int32 ModAccCfgReferenceWaveformInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 referenceWaveform[], int32 arraySize) = 0;
  virtual int32 ModAccCfgReferenceWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 referenceWaveformI[], float32 referenceWaveformQ[], int32 arraySize) = 0;
  virtual int32 ModAccClearNoiseCalibrationDatabase(niRFmxInstrHandle instrumentHandle) = 0;
  virtual int32 ModAccFetchCompositeEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* compositeRMSEVMMean, float64* compositePeakEVMMaximum) = 0;
  virtual int32 ModAccFetchFrequencyErrorMean(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* frequencyErrorMean) = 0;
  virtual int32 ModAccFetchFrequencyErrorPerSlotMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 frequencyErrorPerSlotMaximum[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchIQGainImbalancePerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 iqGainImbalancePerSubcarrierMean[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 iqQuadratureErrorPerSubcarrierMean[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchInBandEmissionTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 inBandEmission[], float32 inBandEmissionMask[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPBCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pbchdmrsConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPBCHDMRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchdmrsConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPBCHDMRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchdmrsConstellationI[], float32 pbchdmrsConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchdmrsrmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchdmrsrmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPBCHDataConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pbchDataConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPBCHDataConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchDataConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPBCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchDataConstellationI[], float32 pbchDataConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchDataRMSEVMPerSubcarrierMean[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchDataRMSEVMPerSymbolMean[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH1024QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam1024Constellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam1024Constellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH1024QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam1024ConstellationI[], float32 qam1024ConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH16QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam16Constellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam16Constellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH16QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam16ConstellationI[], float32 qam16ConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH256QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam256Constellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam256Constellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH256QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam256ConstellationI[], float32 qam256ConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH4096QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam4096Constellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam4096Constellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH4096QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam4096ConstellationI[], float32 qam4096ConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH64QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam64Constellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam64Constellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH64QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam64ConstellationI[], float32 qam64ConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH8PSKConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle psk8Constellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 psk8Constellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCH8PSKConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 psk8ConstellationI[], float32 psk8ConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschdmrsConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschdmrsConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCHDMRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschdmrsConstellationI[], float32 pdschdmrsConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCHDataConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschDataConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCHDataConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschDataConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschDataConstellationI[], float32 pdschDataConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCHDemodulatedBits(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int8 bits[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCHPTRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschptrsConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschptrsConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCHPTRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschptrsConstellationI[], float32 pdschptrsConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCHQPSKConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qpskConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qpskConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPDSCHQPSKConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qpskConstellationI[], float32 qpskConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPSSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pssConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPSSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pssConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPSSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pssConstellationI[], float32 pssConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pssrmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPSSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pssrmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPUSCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle puschdmrsConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschdmrsConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPUSCHDMRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschdmrsConstellationI[], float32 puschdmrsConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPUSCHDataConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle puschDataConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPUSCHDataConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschDataConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPUSCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschDataConstellationI[], float32 puschDataConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPUSCHDemodulatedBits(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int8 bits[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPUSCHPTRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle puschptrsConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschptrsConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPUSCHPTRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschptrsConstellationI[], float32 puschptrsConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPUSCHPhaseOffsetTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 puschPhaseOffset[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPeakEVMHighPerSymbolMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMHighPerSymbolMaximum[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPeakEVMLowPerSymbolMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMLowPerSymbolMaximum[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPeakEVMPerSlotMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMPerSlotMaximum[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPeakEVMPerSubcarrierMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMPerSubcarrierMaximum[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchPeakEVMPerSymbolMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMPerSymbolMaximum[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchRMSEVMHighPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmHighPerSymbolMean[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchRMSEVMLowPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmLowPerSymbolMean[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchRMSEVMPerSlotMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmPerSlotMean[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchSSSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle sssConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchSSSConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 sssConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchSSSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 sssConstellationI[], float32 sssConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 sssrmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchSSSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 sssrmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchSpectralFlatnessTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectralFlatness[], float32 spectralFlatnessLowerMask[], float32 spectralFlatnessUpperMask[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchSubblockInBandEmissionTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 subblockInBandEmission[], float64 subblockInBandEmissionMask[], float64 subblockInBandEmissionRBIndices[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchTransientPeriodLocationsTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 transientPeriodLocations[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccValidateCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* calibrationDataValid) = 0;
  virtual int32 OBWCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) = 0;
  virtual int32 OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType) = 0;
  virtual int32 OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval) = 0;
  virtual int32 OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* occupiedBandwidth, float64* absolutePower, float64* startFrequency, float64* stopFrequency) = 0;
  virtual int32 OBWFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 PVTCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) = 0;
  virtual int32 PVTCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod) = 0;
  virtual int32 PVTCfgOFFPowerExclusionPeriods(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offPowerExclusionBefore, float64 offPowerExclusionAfter) = 0;
  virtual int32 PVTFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* absoluteOFFPowerBefore, float64* absoluteOFFPowerAfter, float64* absoluteONPower, float64* burstWidth) = 0;
  virtual int32 PVTFetchMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 absoluteOFFPowerBefore[], float64 absoluteOFFPowerAfter[], float64 absoluteONPower[], float64 burstWidth[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 PVTFetchSignalPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 signalPower[], float32 absoluteLimit[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 PVTFetchWindowedSignalPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 windowedSignalPower[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID) = 0;
  virtual int32 ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[]) = 0;
  virtual int32 SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) = 0;
  virtual int32 SEMCfgComponentCarrierRatedOutputPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 componentCarrierRatedOutputPower) = 0;
  virtual int32 SEMCfgComponentCarrierRatedOutputPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 componentCarrierRatedOutputPower[], int32 numberOfElements) = 0;
  virtual int32 SEMCfgNumberOfOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets) = 0;
  virtual int32 SEMCfgOffsetAbsoluteLimit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 absoluteLimitStart, float64 absoluteLimitStop) = 0;
  virtual int32 SEMCfgOffsetAbsoluteLimitArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 absoluteLimitStart[], float64 absoluteLimitStop[], int32 numberOfElements) = 0;
  virtual int32 SEMCfgOffsetBandwidthIntegral(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandwidthIntegral) = 0;
  virtual int32 SEMCfgOffsetBandwidthIntegralArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandwidthIntegral[], int32 numberOfElements) = 0;
  virtual int32 SEMCfgOffsetFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetStartFrequency, float64 offsetStopFrequency, int32 offsetSideband) = 0;
  virtual int32 SEMCfgOffsetFrequencyArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetStartFrequency[], float64 offsetStopFrequency[], int32 offsetSideband[], int32 numberOfElements) = 0;
  virtual int32 SEMCfgOffsetLimitFailMask(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 limitFailMask) = 0;
  virtual int32 SEMCfgOffsetLimitFailMaskArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 limitFailMask[], int32 numberOfElements) = 0;
  virtual int32 SEMCfgOffsetRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetRBW, int32 offsetRBWFilterType) = 0;
  virtual int32 SEMCfgOffsetRBWFilterArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetRBW[], int32 offsetRBWFilterType[], int32 numberOfElements) = 0;
  virtual int32 SEMCfgOffsetRelativeLimit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 relativeLimitStart, float64 relativeLimitStop) = 0;
  virtual int32 SEMCfgOffsetRelativeLimitArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 relativeLimitStart[], float64 relativeLimitStop[], int32 numberOfElements) = 0;
  virtual int32 SEMCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval) = 0;
  virtual int32 SEMCfgUplinkMaskType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 uplinkMaskType) = 0;
  virtual int32 SEMFetchComponentCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absolutePower, float64* peakAbsolutePower, float64* peakFrequency, float64* relativePower) = 0;
  virtual int32 SEMFetchComponentCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 relativePower[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 SEMFetchLowerOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower) = 0;
  virtual int32 SEMFetchLowerOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 SEMFetchLowerOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAbsolutePower, float64* totalRelativePower, float64* peakAbsolutePower, float64* peakFrequency, float64* peakRelativePower) = 0;
  virtual int32 SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 totalAbsolutePower[], float64 totalRelativePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 peakRelativePower[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus) = 0;
  virtual int32 SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], float32 compositeMask[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 SEMFetchSubblockMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* subblockPower, float64* integrationBandwidth, float64* frequency) = 0;
  virtual int32 SEMFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAggregatedPower) = 0;
  virtual int32 SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower) = 0;
  virtual int32 SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAbsolutePower, float64* totalRelativePower, float64* peakAbsolutePower, float64* peakFrequency, float64* peakRelativePower) = 0;
  virtual int32 SEMFetchUpperOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 totalAbsolutePower[], float64 totalRelativePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 peakRelativePower[], int32 arraySize, int32* actualArraySize) = 0;
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
  virtual int32 TXPFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* averagePowerMean, float64* peakPowerMaximum) = 0;
  virtual int32 TXPFetchPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 power[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout) = 0;
  virtual int32 WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout) = 0;
};

}  // namespace nirfmxnr_grpc
#endif  // NIRFMXNR_GRPC_LIBRARY_WRAPPER_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/nirfmxnr/nirfmxnr_mock_library.h sha256=6b51e8c253ff489807960318953ff102a95553e7e24f409c9d1deaab72f4ceae bytes=54516 -->
## FILE: generated/nirfmxnr/nirfmxnr_mock_library.h

- repository: `ni/grpc-device`
- source_path: `generated/nirfmxnr/nirfmxnr_mock_library.h`
- sha256: `6b51e8c253ff489807960318953ff102a95553e7e24f409c9d1deaab72f4ceae`
- bytes: 54516

````c
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Mock of LibraryInterface for NI-RFMXNR
//---------------------------------------------------------------------
#ifndef NIRFMXNR_GRPC_MOCK_LIBRARY_H
#define NIRFMXNR_GRPC_MOCK_LIBRARY_H

#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include "nirfmxnr_library_interface.h"

namespace ni {
namespace tests {
namespace unit {

class NiRFmxNRMockLibrary : public nirfmxnr_grpc::NiRFmxNRLibraryInterface {
 public:
  MOCK_METHOD(int32, ACPCfgAveraging, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType), (override));
  MOCK_METHOD(int32, ACPCfgMeasurementMethod, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod), (override));
  MOCK_METHOD(int32, ACPCfgNoiseCompensationEnabled, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled), (override));
  MOCK_METHOD(int32, ACPCfgNumberOfENDCOffsets, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfENDCOffsets), (override));
  MOCK_METHOD(int32, ACPCfgNumberOfEUTRAOffsets, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfEUTRAOffsets), (override));
  MOCK_METHOD(int32, ACPCfgNumberOfNROffsets, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfNROffsets), (override));
  MOCK_METHOD(int32, ACPCfgNumberOfUTRAOffsets, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfUTRAOffsets), (override));
  MOCK_METHOD(int32, ACPCfgPowerUnits, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnits), (override));
  MOCK_METHOD(int32, ACPCfgRBWFilter, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType), (override));
  MOCK_METHOD(int32, ACPCfgSweepTime, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval), (override));
  MOCK_METHOD(int32, ACPFetchAbsolutePowersTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 absolutePowersTrace[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ACPFetchComponentCarrierMeasurement, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absolutePower, float64* relativePower), (override));
  MOCK_METHOD(int32, ACPFetchComponentCarrierMeasurementArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 relativePower[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ACPFetchOffsetMeasurement, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* lowerRelativePower, float64* upperRelativePower, float64* lowerAbsolutePower, float64* upperAbsolutePower), (override));
  MOCK_METHOD(int32, ACPFetchOffsetMeasurementArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 lowerRelativePower[], float64 upperRelativePower[], float64 lowerAbsolutePower[], float64 upperAbsolutePower[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ACPFetchRelativePowersTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 relativePowersTrace[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ACPFetchSpectrum, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ACPFetchSubblockMeasurement, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* subblockPower, float64* integrationBandwidth, float64* frequency), (override));
  MOCK_METHOD(int32, ACPFetchTotalAggregatedPower, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAggregatedPower), (override));
  MOCK_METHOD(int32, ACPValidateNoiseCalibrationData, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32* noiseCalibrationDataValid), (override));
  MOCK_METHOD(int32, AbortMeasurements, (niRFmxInstrHandle instrumentHandle, char selectorString[]), (override));
  MOCK_METHOD(int32, AnalyzeIQ1Waveform, (niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved), (override));
  MOCK_METHOD(int32, AnalyzeIQ1WaveformInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iq[], int32 arraySize, int32 reset, int64 reserved), (override));
  MOCK_METHOD(int32, AnalyzeIQ1WaveformSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iqi[], float32 iqq[], int32 arraySize, int32 reset, int64 reserved), (override));
  MOCK_METHOD(int32, AnalyzeNWaveformsIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], NIComplexSingle iq[], int32 iqSize[], int32 arraySize, int32 reset), (override));
  MOCK_METHOD(int32, AnalyzeNWaveformsIQInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], float32 iq[], int32 iqSize[], int32 arraySize, int32 reset), (override));
  MOCK_METHOD(int32, AnalyzeNWaveformsIQSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], float32 iqi[], float32 iqq[], int32 iqSize[], int32 arraySize, int32 reset), (override));
  MOCK_METHOD(int32, AnalyzeNWaveformsSpectrum, (niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], float32 spectrum[], int32 spectrumSize[], int32 arraySize, int32 reset), (override));
  MOCK_METHOD(int32, AnalyzeSpectrum1Waveform, (niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 spectrum[], int32 arraySize, int32 reset, int64 reserved), (override));
  MOCK_METHOD(int32, AutoLevel, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval, float64* referenceLevel), (override));
  MOCK_METHOD(int32, BuildBandwidthPartString, (char selectorString[], int32 bandwidthPartNumber, int32 selectorStringOutLength, char selectorStringOut[]), (override));
  MOCK_METHOD(int32, BuildCORESETClusterString, (char selectorString[], int32 coresetClusterNumber, int32 selectorStringOutLength, char selectorStringOut[]), (override));
  MOCK_METHOD(int32, BuildCORESETString, (char selectorString[], int32 coresetNumber, int32 selectorStringOutLength, char selectorStringOut[]), (override));
  MOCK_METHOD(int32, BuildCarrierString, (char selectorString[], int32 carrierNumber, int32 selectorStringOutLength, char selectorStringOut[]), (override));
  MOCK_METHOD(int32, BuildListStepString, (char listName[], char resultName[], int32 stepNumber, int32 selectorStringLength, char selectorString[]), (override));
  MOCK_METHOD(int32, BuildListString, (char listName[], char resultName[], int32 selectorStringLength, char selectorString[]), (override));
  MOCK_METHOD(int32, BuildOffsetString, (char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[]), (override));
  MOCK_METHOD(int32, BuildPDCCHString, (char selectorString[], int32 pdcchNumber, int32 selectorStringOutLength, char selectorStringOut[]), (override));
  MOCK_METHOD(int32, BuildPDSCHClusterString, (char selectorString[], int32 pdschClusterNumber, int32 selectorStringOutLength, char selectorStringOut[]), (override));
  MOCK_METHOD(int32, BuildPDSCHString, (char selectorString[], int32 pdschNumber, int32 selectorStringOutLength, char selectorStringOut[]), (override));
  MOCK_METHOD(int32, BuildPUSCHClusterString, (char selectorString[], int32 puschClusterNumber, int32 selectorStringOutLength, char selectorStringOut[]), (override));
  MOCK_METHOD(int32, BuildPUSCHString, (char selectorString[], int32 puschNumber, int32 selectorStringOutLength, char selectorStringOut[]), (override));
  MOCK_METHOD(int32, BuildSignalString, (char signalName[], char resultName[], int32 selectorStringLength, char selectorString[]), (override));
  MOCK_METHOD(int32, BuildSubblockString, (char selectorString[], int32 subblockNumber, int32 selectorStringOutLength, char selectorStringOut[]), (override));
  MOCK_METHOD(int32, BuildUserString, (char selectorString[], int32 userNumber, int32 selectorStringOutLength, char selectorStringOut[]), (override));
  MOCK_METHOD(int32, CHPCfgAveraging, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType), (override));
  MOCK_METHOD(int32, CHPCfgRBWFilter, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType), (override));
  MOCK_METHOD(int32, CHPCfgSweepTime, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval), (override));
  MOCK_METHOD(int32, CHPFetchComponentCarrierMeasurement, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absolutePower, float64* relativePower), (override));
  MOCK_METHOD(int32, CHPFetchComponentCarrierMeasurementArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 relativePower[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, CHPFetchSpectrum, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, CHPFetchSubblockPower, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* subblockPower), (override));
  MOCK_METHOD(int32, CHPFetchTotalAggregatedPower, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAggregatedPower), (override));
  MOCK_METHOD(int32, CHPValidateNoiseCalibrationData, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32* noiseCalibrationDataValid), (override));
  MOCK_METHOD(int32, CfgDigitalEdgeTrigger, (niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger), (override));
  MOCK_METHOD(int32, CfgExternalAttenuation, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation), (override));
  MOCK_METHOD(int32, CfgFrequency, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency), (override));
  MOCK_METHOD(int32, CfgFrequencyReference, (niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency), (override));
  MOCK_METHOD(int32, CfgIQPowerEdgeTrigger, (niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdgeSlope, float64 iqPowerEdgeLevel, float64 triggerDelay, int32 triggerMinQuietTimeMode, float64 triggerMinQuietTimeDuration, int32 iqPowerEdgeLevelType, int32 enableTrigger), (override));
  MOCK_METHOD(int32, CfgMechanicalAttenuation, (niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue), (override));
  MOCK_METHOD(int32, CfgRF, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation), (override));
  MOCK_METHOD(int32, CfgRFAttenuation, (niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue), (override));
  MOCK_METHOD(int32, CfgReferenceLevel, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel), (override));
  MOCK_METHOD(int32, CfgSelectedPortsMultiple, (niRFmxInstrHandle instrumentHandle, char selectorString[], char selectedPorts[]), (override));
  MOCK_METHOD(int32, CfgSoftwareEdgeTrigger, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger), (override));
  MOCK_METHOD(int32, CfggNodeBCategory, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 gNodeBCategory), (override));
  MOCK_METHOD(int32, CheckMeasurementStatus, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32* isDone), (override));
  MOCK_METHOD(int32, ClearAllNamedResults, (niRFmxInstrHandle instrumentHandle, char selectorString[]), (override));
  MOCK_METHOD(int32, ClearNamedResult, (niRFmxInstrHandle instrumentHandle, char selectorString[]), (override));
  MOCK_METHOD(int32, ClearNoiseCalibrationDatabase, (niRFmxInstrHandle instrumentHandle, char selectorString[]), (override));
  MOCK_METHOD(int32, CloneSignalConfiguration, (niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[]), (override));
  MOCK_METHOD(int32, Close, (niRFmxInstrHandle instrumentHandle, int32 forceDestroy), (override));
  MOCK_METHOD(int32, Commit, (niRFmxInstrHandle instrumentHandle, char selectorString[]), (override));
  MOCK_METHOD(int32, CreateList, (niRFmxInstrHandle instrumentHandle, char listName[]), (override));
  MOCK_METHOD(int32, CreateListStep, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32* createdStepIndex), (override));
  MOCK_METHOD(int32, CreateSignalConfiguration, (niRFmxInstrHandle instrumentHandle, char signalName[]), (override));
  MOCK_METHOD(int32, DeleteList, (niRFmxInstrHandle instrumentHandle, char listName[]), (override));
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
  MOCK_METHOD(int32, LoadFromGenerationConfigurationFile, (niRFmxInstrHandle instrumentHandle, char selectorString[], char filePath[], int32 configurationIndex), (override));
  MOCK_METHOD(int32, ModAccAutoLevel, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout), (override));
  MOCK_METHOD(int32, ModAccCfgMeasurementMode, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMode), (override));
  MOCK_METHOD(int32, ModAccCfgNoiseCompensationEnabled, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled), (override));
  MOCK_METHOD(int32, ModAccCfgReferenceWaveform, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, NIComplexSingle referenceWaveform[], int32 arraySize), (override));
  MOCK_METHOD(int32, ModAccCfgReferenceWaveformInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 referenceWaveform[], int32 arraySize), (override));
  MOCK_METHOD(int32, ModAccCfgReferenceWaveformSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 referenceWaveformI[], float32 referenceWaveformQ[], int32 arraySize), (override));
  MOCK_METHOD(int32, ModAccClearNoiseCalibrationDatabase, (niRFmxInstrHandle instrumentHandle), (override));
  MOCK_METHOD(int32, ModAccFetchCompositeEVM, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* compositeRMSEVMMean, float64* compositePeakEVMMaximum), (override));
  MOCK_METHOD(int32, ModAccFetchFrequencyErrorMean, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* frequencyErrorMean), (override));
  MOCK_METHOD(int32, ModAccFetchFrequencyErrorPerSlotMaximumTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 frequencyErrorPerSlotMaximum[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchIQGainImbalancePerSubcarrierMeanTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 iqGainImbalancePerSubcarrierMean[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 iqQuadratureErrorPerSubcarrierMean[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchInBandEmissionTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 inBandEmission[], float32 inBandEmissionMask[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPBCHDMRSConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pbchdmrsConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPBCHDMRSConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchdmrsConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPBCHDMRSConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchdmrsConstellationI[], float32 pbchdmrsConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchdmrsrmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchdmrsrmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPBCHDataConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pbchDataConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPBCHDataConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchDataConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPBCHDataConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchDataConstellationI[], float32 pbchDataConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchDataRMSEVMPerSubcarrierMean[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pbchDataRMSEVMPerSymbolMean[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH1024QAMConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam1024Constellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam1024Constellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH1024QAMConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam1024ConstellationI[], float32 qam1024ConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH16QAMConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam16Constellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam16Constellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH16QAMConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam16ConstellationI[], float32 qam16ConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH256QAMConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam256Constellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam256Constellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH256QAMConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam256ConstellationI[], float32 qam256ConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH4096QAMConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam4096Constellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam4096Constellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH4096QAMConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam4096ConstellationI[], float32 qam4096ConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH64QAMConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam64Constellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam64Constellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH64QAMConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam64ConstellationI[], float32 qam64ConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH8PSKConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle psk8Constellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 psk8Constellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCH8PSKConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 psk8ConstellationI[], float32 psk8ConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCHDMRSConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschdmrsConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschdmrsConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCHDMRSConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschdmrsConstellationI[], float32 pdschdmrsConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCHDataConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschDataConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCHDataConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschDataConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCHDataConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschDataConstellationI[], float32 pdschDataConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCHDemodulatedBits, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int8 bits[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCHPTRSConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschptrsConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschptrsConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCHPTRSConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschptrsConstellationI[], float32 pdschptrsConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCHQPSKConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qpskConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qpskConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPDSCHQPSKConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qpskConstellationI[], float32 qpskConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPSSConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pssConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPSSConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pssConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPSSConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pssConstellationI[], float32 pssConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pssrmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPSSRMSEVMPerSymbolMeanTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 pssrmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPUSCHDMRSConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle puschdmrsConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschdmrsConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPUSCHDMRSConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschdmrsConstellationI[], float32 puschdmrsConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPUSCHDataConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle puschDataConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPUSCHDataConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschDataConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPUSCHDataConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschDataConstellationI[], float32 puschDataConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPUSCHDemodulatedBits, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int8 bits[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPUSCHPTRSConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle puschptrsConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschptrsConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPUSCHPTRSConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschptrsConstellationI[], float32 puschptrsConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPUSCHPhaseOffsetTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 puschPhaseOffset[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPeakEVMHighPerSymbolMaximumTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMHighPerSymbolMaximum[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPeakEVMLowPerSymbolMaximumTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMLowPerSymbolMaximum[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPeakEVMPerSlotMaximumTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMPerSlotMaximum[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPeakEVMPerSubcarrierMaximumTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMPerSubcarrierMaximum[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchPeakEVMPerSymbolMaximumTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 peakEVMPerSymbolMaximum[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchRMSEVMHighPerSymbolMeanTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmHighPerSymbolMean[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchRMSEVMLowPerSymbolMeanTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmLowPerSymbolMean[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchRMSEVMPerSlotMeanTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmPerSlotMean[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchRMSEVMPerSubcarrierMeanTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchRMSEVMPerSymbolMeanTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 rmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchSSSConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle sssConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchSSSConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 sssConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchSSSConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 sssConstellationI[], float32 sssConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 sssrmsevmPerSubcarrierMean[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchSSSRMSEVMPerSymbolMeanTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 sssrmsevmPerSymbolMean[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchSpectralFlatnessTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectralFlatness[], float32 spectralFlatnessLowerMask[], float32 spectralFlatnessUpperMask[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchSubblockInBandEmissionTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 subblockInBandEmission[], float64 subblockInBandEmissionMask[], float64 subblockInBandEmissionRBIndices[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchTransientPeriodLocationsTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 transientPeriodLocations[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccValidateCalibrationData, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32* calibrationDataValid), (override));
  MOCK_METHOD(int32, OBWCfgAveraging, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType), (override));
  MOCK_METHOD(int32, OBWCfgRBWFilter, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType), (override));
  MOCK_METHOD(int32, OBWCfgSweepTime, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval), (override));
  MOCK_METHOD(int32, OBWFetchMeasurement, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* occupiedBandwidth, float64* absolutePower, float64* startFrequency, float64* stopFrequency), (override));
  MOCK_METHOD(int32, OBWFetchSpectrum, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, PVTCfgAveraging, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType), (override));
  MOCK_METHOD(int32, PVTCfgMeasurementMethod, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod), (override));
  MOCK_METHOD(int32, PVTCfgOFFPowerExclusionPeriods, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offPowerExclusionBefore, float64 offPowerExclusionAfter), (override));
  MOCK_METHOD(int32, PVTFetchMeasurement, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* absoluteOFFPowerBefore, float64* absoluteOFFPowerAfter, float64* absoluteONPower, float64* burstWidth), (override));
  MOCK_METHOD(int32, PVTFetchMeasurementArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 absoluteOFFPowerBefore[], float64 absoluteOFFPowerAfter[], float64 absoluteONPower[], float64 burstWidth[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, PVTFetchSignalPowerTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 signalPower[], float32 absoluteLimit[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, PVTFetchWindowedSignalPowerTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 windowedSignalPower[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ResetAttribute, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID), (override));
  MOCK_METHOD(int32, ResetToDefault, (niRFmxInstrHandle instrumentHandle, char selectorString[]), (override));
  MOCK_METHOD(int32, SEMCfgAveraging, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType), (override));
  MOCK_METHOD(int32, SEMCfgComponentCarrierRatedOutputPower, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 componentCarrierRatedOutputPower), (override));
  MOCK_METHOD(int32, SEMCfgComponentCarrierRatedOutputPowerArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 componentCarrierRatedOutputPower[], int32 numberOfElements), (override));
  MOCK_METHOD(int32, SEMCfgNumberOfOffsets, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets), (override));
  MOCK_METHOD(int32, SEMCfgOffsetAbsoluteLimit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 absoluteLimitStart, float64 absoluteLimitStop), (override));
  MOCK_METHOD(int32, SEMCfgOffsetAbsoluteLimitArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 absoluteLimitStart[], float64 absoluteLimitStop[], int32 numberOfElements), (override));
  MOCK_METHOD(int32, SEMCfgOffsetBandwidthIntegral, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandwidthIntegral), (override));
  MOCK_METHOD(int32, SEMCfgOffsetBandwidthIntegralArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandwidthIntegral[], int32 numberOfElements), (override));
  MOCK_METHOD(int32, SEMCfgOffsetFrequency, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetStartFrequency, float64 offsetStopFrequency, int32 offsetSideband), (override));
  MOCK_METHOD(int32, SEMCfgOffsetFrequencyArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetStartFrequency[], float64 offsetStopFrequency[], int32 offsetSideband[], int32 numberOfElements), (override));
  MOCK_METHOD(int32, SEMCfgOffsetLimitFailMask, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 limitFailMask), (override));
  MOCK_METHOD(int32, SEMCfgOffsetLimitFailMaskArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 limitFailMask[], int32 numberOfElements), (override));
  MOCK_METHOD(int32, SEMCfgOffsetRBWFilter, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetRBW, int32 offsetRBWFilterType), (override));
  MOCK_METHOD(int32, SEMCfgOffsetRBWFilterArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetRBW[], int32 offsetRBWFilterType[], int32 numberOfElements), (override));
  MOCK_METHOD(int32, SEMCfgOffsetRelativeLimit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 relativeLimitStart, float64 relativeLimitStop), (override));
  MOCK_METHOD(int32, SEMCfgOffsetRelativeLimitArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 relativeLimitStart[], float64 relativeLimitStop[], int32 numberOfElements), (override));
  MOCK_METHOD(int32, SEMCfgSweepTime, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval), (override));
  MOCK_METHOD(int32, SEMCfgUplinkMaskType, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 uplinkMaskType), (override));
  MOCK_METHOD(int32, SEMFetchComponentCarrierMeasurement, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absolutePower, float64* peakAbsolutePower, float64* peakFrequency, float64* relativePower), (override));
  MOCK_METHOD(int32, SEMFetchComponentCarrierMeasurementArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 relativePower[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, SEMFetchLowerOffsetMargin, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower), (override));
  MOCK_METHOD(int32, SEMFetchLowerOffsetMarginArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, SEMFetchLowerOffsetPower, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAbsolutePower, float64* totalRelativePower, float64* peakAbsolutePower, float64* peakFrequency, float64* peakRelativePower), (override));
  MOCK_METHOD(int32, SEMFetchLowerOffsetPowerArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 totalAbsolutePower[], float64 totalRelativePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 peakRelativePower[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, SEMFetchMeasurementStatus, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus), (override));
  MOCK_METHOD(int32, SEMFetchSpectrum, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], float32 compositeMask[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, SEMFetchSubblockMeasurement, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* subblockPower, float64* integrationBandwidth, float64* frequency), (override));
  MOCK_METHOD(int32, SEMFetchTotalAggregatedPower, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAggregatedPower), (override));
  MOCK_METHOD(int32, SEMFetchUpperOffsetMargin, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower), (override));
  MOCK_METHOD(int32, SEMFetchUpperOffsetMarginArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, SEMFetchUpperOffsetPower, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalAbsolutePower, float64* totalRelativePower, float64* peakAbsolutePower, float64* peakFrequency, float64* peakRelativePower), (override));
  MOCK_METHOD(int32, SEMFetchUpperOffsetPowerArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 totalAbsolutePower[], float64 totalRelativePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 peakRelativePower[], int32 arraySize, int32* actualArraySize), (override));
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
  MOCK_METHOD(int32, TXPFetchMeasurement, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* averagePowerMean, float64* peakPowerMaximum), (override));
  MOCK_METHOD(int32, TXPFetchPowerTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 power[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, WaitForAcquisitionComplete, (niRFmxInstrHandle instrumentHandle, float64 timeout), (override));
  MOCK_METHOD(int32, WaitForMeasurementComplete, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout), (override));
};

}  // namespace unit
}  // namespace tests
}  // namespace ni
#endif  // NIRFMXNR_GRPC_MOCK_LIBRARY_H
````
