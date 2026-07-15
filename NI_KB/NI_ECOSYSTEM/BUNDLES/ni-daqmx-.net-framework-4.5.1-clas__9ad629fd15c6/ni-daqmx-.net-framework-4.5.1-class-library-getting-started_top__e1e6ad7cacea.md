# NI DOCUMENT BUNDLE: ni-daqmx-.net-framework-4.5.1-class-library-getting-started

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started start=1 end=33 -->
<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=copyright.html language=enus -->
## TOPIC 00001: Copyright

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `copyright.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/copyright.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: Under the copyright laws, this publication may not be reproduced or transmitted in any form, electronic or mechanical, including photocopying, recording, storing in an information retrieval system, or translating, in whole or in part, without the prior written consent of National Instruments Corpora

Copyright

#### End-User License Agreements and Third-Party Legal Notices

Under the copyright laws, this publication may not be reproduced or transmitted in any form, electronic or mechanical, including photocopying, recording, storing in an information retrieval system, or translating, in whole or in part, without the prior written consent of National Instruments Corporation.

National Instruments respects the intellectual property of others, and we ask our users to do the same. NI software is protected by copyright and other intellectual property laws. Where NI software may be used to reproduce software or other materials belonging to others, you may use NI software only to reproduce materials that you may reproduce in accordance with the terms of any applicable license or other legal restriction.

You can find end-user license agreements (EULAs) and third-party legal notices in the following locations:

- Notices are located in the 
 <National Instruments>\_Legal Information and 
 <National Instruments> directories.
- EULAs are located in the 
 <National Instruments>\Shared\MDF\Legal\license directory.
- Review 
 <National Instruments>\_Legal Information.txt for information on including legal information in installers built with NI products.

If you are an agency, department, or other entity of the United States Government ("Government"), the use, duplication, reproduction, release, modification, disclosure or transfer of the technical data included in this manual is governed by the Restricted Rights provisions under Federal Acquisition Regulation 52.227-14 for civilian agencies and Defense Federal Acquisition Regulation Supplement Section 252.227-7014 and 252.227-7015 for military agencies.

Content from the IVI specifications reproduced with permission from the IVI Foundation.

The IVI Foundation and its member companies make no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The IVI Foundation and its member companies shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material.

Parent topic:

Legal Information

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=export-compliance.html language=enus -->
## TOPIC 00002: Export Compliance Information

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `export-compliance.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/export-compliance.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the Export Compliance Information at ni.com/legal/export-compliance for the National Instruments global trade compliance policy and how to obtain relevant HTS codes, ECCNs, and other import/export data.

Export Compliance Information

Refer to the 
 *Export Compliance Information* at 
 ni.com/legal/export-compliance for the National Instruments global trade compliance policy and how to obtain relevant HTS codes, ECCNs, and other import/export data.

Parent topic:

Legal Information

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=fx451netdaqmxmapping.html language=enus -->
## TOPIC 00003: Mapping the NI-DAQmx .NET API to the NI-DAQmx C API

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `fx451netdaqmxmapping.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/fx451netdaqmxmapping.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table maps NI-DAQmx .NET API members to corresponding NI-DAQmx C API members. All .NET members are in the DAQmx namespace. .NET API Member C API Member AdvanceTrigger ConfigureDigitalEdgeTrigger DAQmxCfgDigEdgeAdvTrig ConfigureNone DAQmxDisableAdvTrig SendSoftwareTrigger DAQmxSendSoftw

Mapping the NI-DAQmx .NET API to the NI-DAQmx C API

The following table maps NI-DAQmx .NET API members to corresponding NI-DAQmx C API members. All .NET members are in the DAQmx namespace.

| .NET API Member | C API Member |
| --- | --- |
| AdvanceTrigger |  |
| ConfigureDigitalEdgeTrigger | DAQmxCfgDigEdgeAdvTrig |
| ConfigureNone | DAQmxDisableAdvTrig |
| SendSoftwareTrigger | DAQmxSendSoftwareTrigger |
| AIChannel |  |
| CalibrationDate | DAQmxGetAIChanCalCalDate |
| CalibrationDate | DAQmxSetAIChanCalCalDate |
| CalibrationExpirationDate | DAQmxGetAIChanCalExpDate |
| CalibrationExpirationDate | DAQmxGetAIChanCalExpDate |
| PerformBridgeOffsetNullingCalibration | DAQmxPerformBridgeOffsetNullingCal |
| PerformBridgeOffsetNullingCalibration | DAQmxPerformBridgeOffsetNullingCalEx |
| PerformBridgeShuntCalibration | DAQmxPerformBridgeShuntCal |
| PerformBridgeShuntCalibration | DAQmxPerformBridgeShuntCalEx |
| PerformStrainShuntCalibration | DAQmxPerformStrainShuntCal |
| PerformStrainShuntCalibration | DAQmxPerformStrainShuntCalEx |
| PerformThermocoupleLeadOffsetNullingCalibration | DAQmxPerformThrmcplLeadOffsetNullingCal |
| AIChannelCollection |  |
| CreateAccelerationChargeChannel | DAQmxCreateAIAccelChargeChan |
| CreateAccelerationFourWireDCVoltageChannel | DAQmxCreateAIAccel4WireDCVoltageChan |
| CreateAccelerometerChannel | DAQmxCreateAIAccelChan |
| CreateBridgeChannel | DAQmxCreateAIBridgeChan |
| CreateChargeChannel | DAQmxCreateAIChargeChan |
| CreateCurrentChannel | DAQmxCreateAICurrentChan |
| CreateCurrentRmsChannel | DAQmxCreateAICurrentRMSChan |
| CreateForceBridgePolynomialChannel | DAQmxCreateAIForceBridgePolynomialChan |
| CreateForceBridgeTwoPointLinearChannel | DAQmxCreateAIForceBridgeTwoPointLinChan |
| CreateForceBridgeTwoPointLinearChannel | DAQmxCreateAIForceBridgeTwoPointLinChan |
| CreateForceIepeChannel | DAQmxCreateAIForceIEPEChan |
| CreateFrequencyVoltageChannel | DAQmxCreateAIFreqVoltageChan |
| CreateLvdtChannel | DAQmxCreateAIPosLVDTChan |
| CreateMicrophoneChannel | DAQmxCreateAIMicrophoneChan |
| CreatePressureBridgePolynomialChannel | DAQmxCreateAIPressureBridgePolynomialChan |
| CreatePressureBridgeTableChannel | DAQmxCreateAIPressureBridgeTableChan |
| CreatePressureBridgeTwoPointLinearChannel | DAQmxCreateAIPressureBridgeTwoPointLinChan |
| CreateResistanceChannel | DAQmxCreateAIResistanceChan |
| CreateRtdChannel | DAQmxCreateAIRTDChan |
| CreateRvdtChannel | DAQmxCreateAIPosRVDTChan |
| CreateStrainGageChannel | DAQmxCreateAIStrainGageChan |
| CreateThermistorVExChannel | DAQmxCreateAITempBuiltInSensorChan |
| CreateThermistorVExChannel | DAQmxCreateAIThrmstrChanVex |
| CreateThermocoupleChannel | DAQmxCreateAIThrmcplChan |
| CreateThermocoupleChannel | DAQmxCreateAIThrmcplChan |
| CreateTorqueBridgePolynomialChannel | DAQmxCreateAITorqueBridgePolynomialChan |
| CreateTorqueBridgeTableChannel | DAQmxCreateAITorqueBridgeTableChan |
| CreateTorqueBridgeTwoPointLinearChannel | DAQmxCreateAITorqueBridgeTwoPointLinChan |
| CreateVelocityIepeChannel | DAQmxCreateAIVelocityIEPEChan |
| CreateVoltageChannel | DAQmxCreateAIVoltageChan |
| CreateVoltageRmsChannel | DAQmxCreateAIVoltageRMSChan |
| CreateVoltageChannelWithExcitation | DAQmxCreateAIVoltageChanWithExcit |
| CreateTedsAccelerometerChannel | DAQmxCreateTEDSAIAccelChan |
| CreateTedsBridgeChannel | DAQmxCreateTEDSAIBridgeChan |
| CreateTedsCurrentChannel | DAQmxCreateTEDSAICurrentChan |
| CreateTedsForceBridgeChannel | DAQmxCreateTEDSAIForceBridgeChan |
| CreateTedsForceIepeChannel | DAQmxCreateTEDSAIForceIEPEChan |
| CreateTedsMicrophoneChannel | DAQmxCreateTEDSAIMicrophoneChan |
| CreateTedsPressureBridgeChannel | DAQmxCreateTEDSAIPressureBridgeChan |
| CreateTedsResistanceChannel | DAQmxCreateTEDSAIResistanceChan |
| CreateTedsRtdChannel | DAQmxCreateTEDSAIRTDChan |
| CreateTedsRtdChannel | DAQmxCreateTEDSAIPosRVDTChan |
| CreateTedsStrainGageChannel | DAQmxCreateTEDSAIStrainGageChan |
| CreateTedsThermistorIExChannel | DAQmxCreateTEDSAIThrmstrChanIex |
| CreateTedsThermistorVExChannel | DAQmxCreateTEDSAIThrmstrChanVex |
| CreateTedsThermocoupleChannel | DAQmxCreateTEDSAIThrmcplChan |
| CreateTedsTorqueBridgeChannel | DAQmxCreateTEDSAITorqueBridgeChan |
| CreateTedsVoltageChannel | DAQmxCreateTEDSAIVoltageChan |
| CreateTedsVoltageChannelWithExcitation | DAQmxCreateTEDSAIVoltageChanWithExcit |
| CreateTedsLvdtChannel | DAQmxCreateTEDSAIPosLVDTChan |
| Item | DAQmxGetNthTaskChannel |
| AnalogMultiChannelReader |  |
| ReadMultiSample | DAQmxReadAnalogF64 |
| ReadSingleSample | DAQmxReadAnalogF64 |
| AnalogSingleChannelReader |  |
| ReadMultiSample | DAQmxReadAnalogF64 |
| ReadSingleSample | DAQmxReadAnalogScalarF64 |
| AnalogUnscaledReader |  |
| ReadInt16 | DAQmxReadBinaryI16 |
| ReadInt32 | DAQmxReadBinaryI32 |
| ReadUInt16 | DAQmxReadBinaryU16 |
| ReadUInt32 | DAQmxReadBinaryU32 |
| AnalogMultiChannelWriter |  |
| WriteMultiSample | DAQmxWriteAnalogF64 |
| WriteSingleSample | DAQmxWriteAnalogF64 |
| AnalogSingleChannelWriter |  |
| WriteMultiSample | DAQmxWriteAnalogF64 |
| WriteSingleSample | DAQmxWriteAnalogScalarF64 |
| AnalogUnscaledWriter |  |
| WriteInt16 | DAQmxWriteBinaryI16 |
| WriteInt32 | DAQmxWriteBinaryI32 |
| WriteUInt16 | DAQmxWriteBinaryU16 |
| WriteUInt32 | DAQmxWriteBinaryU32 |
| AOChannelCollection |  |
| CreateCurrentChannel | DAQmxCreateAOCurrentChan |
| CreateFunctionGenerationChannel | DAQmxCreateAOFuncGenChan |
| CreateVoltageChannel | DAQmxCreateAOVoltageChan |
| Item | DAQmxGetNthTaskChannel |
| CIChannelCollection |  |
| CreateAngularEncoderChannel | DAQmxCreateCIAngEncoderChan |
| CreateAngularVelocityChannel | DAQmxCreateCIAngVelocityChan |
| CreateCountEdgesChannel | DAQmxCreateCICountEdgesChan |
| CreateDutyCycleChannel | DAQmxCreateCIDutyCycleChan |
| CreateFrequencyChannel | DAQmxCreateCIFreqChan |
| CreateLinearEncoderChannel | DAQmxCreateCILinEncoderChan |
| CreateLinearVelocityChannel | DAQmxCreateCILinVelocityChan |
| CreateGpsTimestampChannel | DAQmxCreateCIGPSTimestampChan |
| CreatePeriodChannel | DAQmxCreateCIPeriodChan |
| CreatePulseChannelFrequency | DAQmxCreateCIPulseChanFreq |
| CreatePulseChannelTicks | DAQmxCreateCIPulseChanTicks |
| CreatePulseChannelTime | DAQmxCreateCIPulseChanTime |
| CreatePulseWidthChannel | DAQmxCreateCIPulseWidthChan |
| CreateSemiPeriodChannel | DAQmxCreateCISemiPeriodChan |
| CreateTwoEdgeSeparationChannel | DAQmxCreateCITwoEdgeSepChan |
| Item | DAQmxGetNthTaskChannel |
| COChannelCollection |  |
| CreatePulseChannelFrequency | DAQmxCreateCOPulseChanFreq |
| CreatePulseChannelTicks | DAQmxCreateCOPulseChanTicks |
| CreatePulseChannelTime | DAQmxCreateCOPulseChanTime |
| Item | DAQmxGetNthTaskChannel |
| CounterMultiChannelReader |  |
| ReadMultiSampleDouble | DAQmxReadCounterF64 |
| ReadMultiSampleUInt32 | DAQmxReadCounterU32 |
| ReadSingleSampleDouble | DAQmxReadCounterScalarF64 |
| ReadSingleSampleUInt32 | DAQmxReadCounterScalarU32 |
| CounterMultiChannelWriter |  |
| WriteSingleSample | DAQmxWriteCtrFreq |
| WriteSingleSample | DAQmxWriteCtrTicks |
| WriteSingleSample | DAQmxWriteCtrTime |
| CounterSingleChannelReader |  |
| ReadMultiSampleDouble | DAQmxReadCounterF64 |
| ReadMultiSamplePulseFrequency | DAQmxReadCtrFreq |
| ReadMultiSamplePulseTime | DAQmxReadCtrTime |
| ReadMultiSamplePulseTicks | DAQmxReadCtrTicks |
| ReadMultiSampleUInt32 | DAQmxReadCounterU32 |
| ReadSingleSampleDouble | DAQmxReadCounterScalarF64 |
| ReadSingleSamplePulseFrequency | DAQmxReadCtrFreqScalar |
| ReadSingleSamplePulseTime | DAQmxReadCtrTimeScalar |
| ReadSingleSamplePulseTicks | DAQmxReadCtrTicksScalar |
| ReadSingleSampleUInt32 | DAQmxReadCounterScalarU32 |
| CounterSingleChannelWriter |  |
| WriteSingleSample | DAQmxWriteCtrFreqScalar |
| WriteSingleSample | DAQmxWriteCtrTicksScalar |
| WriteSingleSample | DAQmxWriteCtrTimeScalar |
| DaqBuffer |  |
| InputBufferSize | DAQmxCfgInputBuffer |
| OutputBufferSize | DAQmxCfgOutputBuffer |
| DaqStream |  |
| ReadRaw | DAQmxReadRaw |
| WriteRaw | DAQmxWriteRaw |
| DaqSystem |  |
| AddNetworkDevice | DAQmxAddNetworkDevice |
| CloseSwitchRelays | DAQmxSwitchCloseRelays |
| ConnectSwitchChannels | DAQmxSwitchConnect |
| ConnectSwitchChannels | DAQmxSwitchConnectMulti |
| CreateSwitchScanTask | DAQmxSwitchCreateScanList |
| CreateWatchdogTimerTask | DAQmxCreateWatchdogTimerTask |
| ConnectTerminals | DAQmxConnectTerms |
| DeleteGlobalChannel | DAQmxDeleteSavedGlobalChan |
| DeleteScale | DAQmxDeleteSavedScale |
| DeleteTask | DAQmxDeleteSavedTask |
| DisconnectAll | DAQmxSwitchDisconnectAll |
| DisconnectSwitchChannels | DAQmxSwitchDisconnect |
| DisconnectSwitchChannels | DAQmxSwitchDisconnectMulti |
| DisconnectTerminals | DAQmxDisconnectTerms |
| GetAnalogPowerUpStatesWithOutputType | DAQmxGetAnalogPowerUpStatesWithOutputType |
| GetDevicePowerUpState | DAQmxGetAnalogPowerUpStates |
| GetDevicePowerUpState | DAQmxGetDigitalPowerUpStates |
| GetDevicePowerUpState | DAQmxGetDigitalPullUpPullDownStates |
| GetLogicFamilyPowerUpState | DAQmxGetDigitalLogicFamilyPowerUpState |
| GetSwitchRelayCount | DAQmxSwitchGetSingleRelayCount |
| GetSwitchRelayCounts | DAQmxSwitchGetMultiRelayCount |
| GetSwitchRelayPosition | DAQmxSwitchGetSingleRelayPos |
| GetSwitchRelayPositions | DAQmxSwitchGetMultiRelayPos |
| LoadTask | DAQmxLoadTask |
| OpenSwitchRelays | DAQmxSwitchOpenRelays |
| SaveGlobalChannel | DAQmxSaveGlobalChan |
| SaveScale | DAQmxSaveScale |
| SaveTask | DAQmxSaveTask |
| SetAnalogPowerUpStatesWithOutputType | DAQmxSetAnalogPowerUpStatesWithOutputType |
| SetDevicePowerUpState | DAQmxSetAnalogPowerUpStates |
| SetDevicePowerUpState | DAQmxSetDigitalPowerUpStates |
| SetDevicePowerUpState | DAQmxSetDigitalPullUpPullDownStates |
| SetLogicFamilyPowerUpState | DAQmxSetDigitalLogicFamilyPowerUpState |
| SwitchFindPath | DAQmxSwitchFindPath |
| TristateOutputTerminal | DAQmxTristateOutputTerm |
| Device |  |
| ChangeExternalCalibrationPassword | DAQmxChangeExtCalPassword |
| DeleteNetworkDevice | DAQmxDeleteNetworkDevice |
| ExternalCalibrationDate | DAQmxGetExtCalLastDateAndTime |
| GetPossibleSCExpressCalibrationAccessoryConnections | DAQmxGetPossibleSCExpressCalAccConnections |
| ReserveNetworkDevice | DAQmxReserveNetworkDevice |
| Reset | DAQmxResetDevice |
| RestoreLastExternalCalibration | DAQmxRestoreLastExtCalConst |
| SelfCalibrationDateTime | DAQmxSelfCal |
| SelfTest | DAQmxSelfTestDevic |
| StartExternalCalibration | DAQmxInitExtCal |
| UnreserveNetworkDevice | DAQmxUnreserveNetworkDevice |
| DIChannelCollection |  |
| CreateChannel | DAQmxCreateDIChan |
| Item | DAQmxGetNthTaskChannel |
| DigitalMultiChannelReader |  |
| ReadMultiSamplePortByte | DAQmxReadDigitalLines |
| ReadMultiSamplePortInt16 | DAQmxReadDigitalLines |
| ReadMultiSamplePortInt32 | DAQmxReadDigitalLines |
| ReadMultiSamplePortUInt16 | DAQmxReadDigitalLines |
| ReadMultiSamplePortUInt32 | DAQmxReadDigitalLines |
| ReadSingleSamplePortByte | DAQmxReadDigitalU8 |
| ReadSingleSamplePortUInt16 | DAQmxReadDigitalU16 |
| ReadSingleSamplePortUInt32 | DAQmxReadDigitalU32 |
| ReadSingleSampleSingleLine | DAQmxReadDigitalScalarU32 |
| DigitalMultiChannelWriter |  |
| WriteMultiSamplePort | DAQmxWriteDigitalLines |
| WriteSingleSamplePortByte | DAQmxWriteDigitalU8 |
| WriteSingleSamplePortUInt16 | DAQmxWriteDigitalU16 |
| WriteSingleSamplePortUInt32 | DAQmxWriteDigitalU32 |
| WriteSingleSampleSingleLine | DAQmxWriteDigitalScalarU32 |
| DigitalSingleChannelReader |  |
| ReadMultiSamplePortByte | DAQmxReadDigitalLines |
| ReadMultiSamplePortInt16 | DAQmxReadDigitalLines |
| ReadMultiSamplePortInt32 | DAQmxReadDigitalLines |
| ReadMultiSamplePortUInt16 | DAQmxReadDigitalLines |
| ReadMultiSamplePortUInt32 | DAQmxReadDigitalLines |
| ReadSingleSampleSingleLine | DAQmxReadDigitalU32 |
| ReadSingleSamplePortByte | DAQmxReadDigitalU8 |
| ReadSingleSamplePortUInt16 | DAQmxReadDigitalU16 |
| ReadSingleSamplePortUInt32 | DAQmxReadDigitalU32 |
| DigitalSingleChannelWriter |  |
| WriteMultiSamplePort | DAQmxWriteDigitalLines |
| WriteSingleSamplePortByte | DAQmxWriteDigitalU8 |
| WriteSingleSamplePortUInt16 | DAQmxWriteDigitalU16 |
| WriteSingleSamplePortUInt32 | DAQmxWriteDigitalU32 |
| WriteSingleSampleSingleLine | DAQmxWriteDigitalU32 |
| DOChannelCollection |  |
| CreateChannel | DAQmxCreateDOChan |
| Item | DAQmxGetNthTaskChannel |
| ExportSignals |  |
| ExportHardwareSignal | DAQmxExportSignal |
| ExternalCalibrationSession |  |
| Adjust1102 | DAQmxAdjust1102Cal |
| Adjust1104 | DAQmxAdjust1104Cal |
| Adjust1112 | DAQmxAdjust1112Cal |
| Adjust1122 | DAQmxAdjust1122Cal |
| Adjust1124 | DAQmxAdjust1124Cal |
| Adjust1125 | DAQmxAdjust1125Cal |
| Adjust1126 | DAQmxAdjust1126Cal |
| Adjust1141 | DAQmxAdjust1141Cal |
| Adjust1142 | DAQmxAdjust1142Cal |
| Adjust1143 | DAQmxAdjust1143Cal |
| Adjust1502 | DAQmxAdjust1502Cal |
| Adjust1503 | DAQmxAdjust1503Cal |
| Adjust1503Current | DAQmxAdjust1503CurrentCal |
| Adjust1520 | DAQmxAdjust1520Cal |
| Adjust1521 | DAQmxAdjust1521Cal |
| Adjust153x | DAQmxAdjust153xCal |
| Adjust1540 | DAQmxAdjust1540Cal |
| Adjust4204 | DAQmxAdjust4204Cal |
| Adjust4220 | DAQmxAdjust4220Cal |
| Adjust4224 | DAQmxAdjust4224Cal |
| Adjust4300 | DAQmxAdjust4300Cal |
| Adjust4302 | DAQmxAdjust4302Cal |
| Adjust4303 | DAQmxAdjust4303Cal |
| Adjust4304 | DAQmxAdjust4304Cal |
| Adjust4305 | DAQmxAdjust4305Cal |
| Adjust4309 | DAQmxAdjust4309Cal |
| Adjust4310 | DAQmxAdjust4310Cal |
| Adjust433x | DAQmxAdjust433xCal |
| Adjust4353 | DAQmxAdjust4353Cal |
| Adjust9201 | DAQmxAdjust9201Cal |
| Adjust9203Gain | DAQmxAdjust9203GainCal |
| Adjust9203Offset | DAQmxAdjust9203OffsetCal |
| Adjust9205 | DAQmxAdjust9205Cal |
| Adjust9206 | DAQmxAdjust9206Cal |
| Adjust9207Gain | DAQmxAdjust9207GainCal |
| Adjust9207Offset | DAQmxAdjust9207OffsetCal |
| Adjust9208Gain | DAQmxAdjust9208GainCal |
| Adjust9208Offset | DAQmxAdjust9208OffsetCal |
| Adjust9209Gain | DAQmxAdjust9209GainCal |
| Adjust9209Offset | DAQmxAdjust9209OffsetCal |
| Adjust9210 | DAQmxAdjust9210Cal |
| Adjust9211 | DAQmxAdjust9211Cal |
| Adjust9212 | DAQmxAdjust9212Cal |
| Adjust9213 | DAQmxAdjust9213Cal |
| Adjust9214 | DAQmxAdjust9214Cal |
| Adjust9215 | DAQmxAdjust9215Cal |
| Adjust9216 | DAQmxAdjust9216Cal |
| Adjust9217 | DAQmxAdjust9217Cal |
| Adjust9218 | DAQmxAdjust9218Cal |
| Adjust9219 | DAQmxAdjust9219Cal |
| Adjust9221 | DAQmxAdjust9221Cal |
| Adjust9222 | DAQmxAdjust9222Cal |
| Adjust9223 | DAQmxAdjust9223Cal |
| Adjust9224 | DAQmxAdjust9224Cal |
| Adjust9225 | DAQmxAdjust9225Cal |
| Adjust9226 | DAQmxAdjust9226Cal |
| Adjust9227 | DAQmxAdjust9227Cal |
| Adjust9228 | DAQmxAdjust9228Cal |
| Adjust9230 | DAQmxAdjust9230Cal |
| Adjust9231 | DAQmxAdjust9231Cal |
| Adjust9232 | DAQmxAdjust9232Cal |
| Adjust9234Gain | DAQmxAdjust9234GainCal |
| Adjust9234Offset | DAQmxAdjust9234OffsetCal |
| Adjust9238 | DAQmxAdjust9238Cal |
| Adjust9242 | DAQmxAdjust9242Cal |
| Adjust9244 | DAQmxAdjust9244Cal |
| Adjust9246 | DAQmxAdjust9246Cal |
| Adjust9247 | DAQmxAdjust9247Cal |
| Adjust9250 | DAQmxAdjust9250Cal |
| Adjust9251 | DAQmxAdjust9251Cal |
| Adjust9252 | DAQmxAdjust9252Cal |
| Adjust9253 | DAQmxAdjust9253Cal |
| Adjust9260 | DAQmxAdjust9260Cal |
| Adjust9262 | DAQmxAdjust9262Cal |
| Adjust9263 | DAQmxAdjust9263Cal |
| Adjust9264 | DAQmxAdjust9264Cal |
| Adjust9265 | DAQmxAdjust9265Cal |
| Adjust9266 | DAQmxAdjust9266Cal |
| Adjust9269 | DAQmxAdjust9269Cal |
| Adjust9775 | DAQmxAdjust9775Cal |
| Adjust11601 | DAQmxAdjust11601Cal |
| Adjust11603 | DAQmxAdjust11603Cal |
| Adjust11605 | DAQmxAdjust11605Cal |
| Adjust11613 | DAQmxAdjust11613Cal |
| Adjust11614 | DAQmxAdjust11614Cal |
| Adjust11634 | DAQmxAdjust11634Cal |
| AdjustAOSeries | DAQmxAOSeriesCalAdjust |
| AdjustDsa4463 | DAQmxAdjust4463Cal |
| AdjustDsa4480 | DAQmxAdjust4480Cal |
| AdjustDsa4610 | DAQmxAdjust4610Cal |
| AdjustDsaAI | DAQmxAdjustDSAAICal DAQmxAdjustDSAAICalEx DAQmxAdjustDSAAICalEx |
| AdjustDsaAO | DAQmxAdjustDSAAOCal |
| AdjustDsaAOTimebase | DAQmxAdjustDSAAOTimebaseCal |
| AdjustDsaTimebase | DAQmxAdjustDSATimebaseCal |
| AdjustESeries | DAQmxESeriesCalAdjust |
| AdjustMSeries | DAQmxMSeriesCalAdjust |
| AdjustSCBaseboard | DAQmxSCBaseboardCalAdjust |
| AdjustSSeries | DAQmxSSeriesCalAdjust |
| AdjustTioTimebase | DAQmxAdjustTIOTimebaseCal |
| AdjustXSeries | DAQmxXSeriesCalAdjust |
| ConnectSCExpressCalibrationAccessoryChannels | DAQmxConnectSCExpressCalAccChans |
| CSeriesSetCalibrationTemperature | DAQmxCSeriesSetCalTemp |
| DsaSetCalibrationTemperature | DAQmxDSASetCalTemp |
| FieldDAQSetCalibrationTemperature | DAQmxFieldDAQSetCalTemp |
| DisconnectSCExpressCalibrationAccessoryChannels | DAQmxDisconnectSCExpressCalAccChans |
| Get4302AdjustmentPoints | DAQmxGet4302CalAdjustPoints |
| Get4303AdjustmentPoints | DAQmxGet4303CalAdjustPoints |
| Get4304AdjustmentPoints | DAQmxGet4304CalAdjustPoints |
| Get4305AdjustmentPoints | DAQmxGet4305CalAdjustPoints |
| Get9201AdjustmentPoints | DAQmxGet9201CalAdjustPoints |
| Get9203AdjustmentPoints | DAQmxGet9203CalAdjustPoints |
| Get9207AdjustmentPoints | DAQmxGet9207CalAdjustPoints |
| Get9208AdjustmentPoints | DAQmxGet9208CalAdjustPoints |
| Get9209AdjustmentPoints | DAQmxGet9209CalAdjustPoints |
| Get9212AdjustmentPoints | DAQmxGet9212CalAdjustPoints |
| Get9213AdjustmentPoints | DAQmxGet9213CalAdjustPoints |
| Get9214AdjustmentPoints | DAQmxGet9214CalAdjustPoints |
| Get9215AdjustmentPoints | DAQmxGet9215CalAdjustPoints |
| Get9216AdjustmentPoints | DAQmxGet9216CalAdjustPoints |
| Get9217AdjustmentPoints | DAQmxGet9217CalAdjustPoints |
| Get9218AdjustmentPoints | DAQmxGet9218CalAdjustPoints |
| Get9219AdjustmentPoints | DAQmxGet9219CalAdjustPoints |
| Get9222AdjustmentPoints | DAQmxGet9222CalAdjustPoints |
| Get9223AdjustmentPoints | DAQmxGet9223CalAdjustPoints |
| Get9224AdjustmentPoints | DAQmxGet9224CalAdjustPoints |
| Get9225AdjustmentPoints | DAQmxGet9225CalAdjustPoints |
| Get9226AdjustmentPoints | DAQmxGet9226CalAdjustPoints |
| Get9227AdjustmentPoints | DAQmxGet9227CalAdjustPoints |
| Get9228AdjustmentPoints | DAQmxGet9228CalAdjustPoints |
| Get9230AdjustmentPoints | DAQmxGet9230CalAdjustPoints |
| Get9231AdjustmentPoints | DAQmxGet9231CalAdjustPoints |
| Get9232AdjustmentPoints | DAQmxGet9232CalAdjustPoints |
| Get9234AdjustmentPoints | DAQmxGet9234CalAdjustPoints |
| Get9238AdjustmentPoints | DAQmxGet9238CalAdjustPoints |
| Get9242AdjustmentPoints | DAQmxGet9242CalAdjustPoints |
| Get9244AdjustmentPoints | DAQmxGet9244CalAdjustPoints |
| Get9246AdjustmentPoints | DAQmxGet9246CalAdjustPoints |
| Get9247AdjustmentPoints | DAQmxGet9247CalAdjustPoints |
| Get9250AdjustmentPoints | DAQmxGet9250CalAdjustPoints |
| Get9251AdjustmentPoints | DAQmxGet9251CalAdjustPoints |
| Get9252AdjustmentPoints | DAQmxGet9252CalAdjustPoints |
| Get9253AdjustmentPoints | DAQmxGet9253CalAdjustPoints |
| Get9260AdjustmentPoints | DAQmxGet9260CalAdjustPoints |
| Get9262AdjustmentPoints | DAQmxGet9262CalAdjustPoints |
| Get9263AdjustmentPoints | DAQmxGet9263CalAdjustPoints |
| Get9264AdjustmentPoints | DAQmxGet9264CalAdjustPoints |
| Get9265AdjustmentPoints | DAQmxGet9265CalAdjustPoints |
| Get9266AdjustmentPoints | DAQmxGet9266CalAdjustPoints |
| Get9269AdjustmentPoints | DAQmxGet9269CalAdjustPoints |
| Get9775AdjustmentPoints | DAQmxGet9775CalAdjustPoints |
| Get11601AdjustmentPoints | DAQmxGet11601CalAdjustPoints |
| Get11603AdjustmentPoints | DAQmxGet11603CalAdjustPoints |
| Get11605AdjustmentPoints | DAQmxGet11605CalAdjustPoints |
| Get11613AdjustmentPoints | DAQmxGet11613CalAdjustPoints |
| Get11614AdjustmentPoints | DAQmxGet11614CalAdjustPoints |
| Get11634AdjustmentPoints | DAQmxGet11634CalAdjustPoints |
| GetDsa4463AdjustmentPoints | DAQmxGet4463AdjustPoints |
| SaveChangesAndDispose | DAQmxCloseExtCal |
| SetSCExpressCalibrationAccessoryBridgeOutput | DAQmxSetSCExpressCalAccBridgeOutput |
| Setup1102 | DAQmxSetup1102Cal |
| Setup1104 | DAQmxSetup1104Cal |
| Setup1112 | DAQmxSetup1112Cal |
| Setup1122 | DAQmxSetup1122Cal |
| Setup1124 | DAQmxSetup1124Cal |
| Setup1125 | DAQmxSetup1125Cal |
| Setup1126 | DAQmxSetup1126Cal |
| Setup1141 | DAQmxSetup1141Cal |
| Setup1142 | DAQmxSetup1142Cal |
| Setup1143 | DAQmxSetup1143Cal |
| Setup1502 | DAQmxSetup1502Cal |
| Setup1503 | DAQmxSetup1503Cal |
| Setup1520 | DAQmxSetup1520Cal |
| Setup1521 | DAQmxSetup1521Cal |
| Setup153x | DAQmxSetup153xCal |
| Setup1540 | DAQmxSetup1540Cal |
| Setup4302 | DAQmxSetup4302Cal |
| Setup4303 | DAQmxSetup4303Cal |
| Setup4304 | DAQmxSetup4304Cal |
| Setup4305 | DAQmxSetup4305Cal |
| Setup433x | DAQmxSetup433xCal |
| Setup9218 | DAQmxSetup9218Cal |
| Setup9219 | DAQmxSetup9219Cal |
| Setup9242 | DAQmxSetup9242Cal |
| Setup9244 | DAQmxSetup9244Cal |
| Setup9260 | DAQmxSetup9260Cal |
| Setup9262 | DAQmxSetup9262Cal |
| Setup9263 | DAQmxSetup9263Cal |
| Setup9264 | DAQmxSetup9264Cal |
| Setup9265 | DAQmxSetup9265Cal |
| Setup9266 | DAQmxSetup9266Cal |
| Setup9269 | DAQmxSetup9269Cal |
| Setup11605 | DAQmxSetup11605Cal |
| Setup11634 | DAQmxSetup11634Cal |
| SetupDsa4463 | DAQmxSetup4463Cal |
| SetupDsaAOTimebase | DAQmxSetupDSAAOTimebaseCal |
| LinearScale |  |
| LinearScale constructor | DAQmxCreateLinScale |
| PolynomialScale |  |
| PolynomialScale constructor | DAQmxCreatePolynomialScale |
| ReverseCoefficients | DAQmxCalculateReversePolyCoeff |
| PhysicalChannel |  |
| ClearTeds | DAQmxClearTEDS |
| ConfigureTeds | DAQmxConfigureTEDS |
| WriteTedsData | DAQmxWriteToTEDSFromArray |
| WriteTedsData | DAQmxWriteToTEDSFromFile |
| RangeMapScale |  |
| RangeMapScale constructor | DAQmxCreateMapScale |
| ReferenceTrigger |  |
| ConfigureAnalogEdgeTrigger | DAQmxCfgAnlgEdgeRefTrig |
| ConfigureAnalogMultiEdgeTrigger | DAQmxCfgAnlgMultiEdgeRefTrig |
| ConfigureAnalogWindowTrigger | DAQmxCfgAnlgWindowRefTrig |
| ConfigureDigitalEdgeTrigger | DAQmxCfgDigEdgeRefTrig |
| ConfigureDigitalPatternTrigger | DAQmxCfgDigPatternRefTrig |
| ConfigureNone | DAQmxDisableRefTrig |
| SinglePoint |  |
| WaitForNextSampleClock | DAQmxWaitForNextSampleClock |
| StartTrigger |  |
| ConfigureAnalogEdgeTrigger | DAQmxCfgAnlgEdgeStartTrig |
| ConfigureAnalogMultiEdgeTrigger | DAQmxCfgAnlgMultiEdgeStartTrig |
| ConfigureAnalogWindowTrigger | DAQmxCfgAnlgWindowStartTrig |
| ConfigureDigitalEdgeTrigger | DAQmxCfgDigEdgeStartTrig |
| ConfigureDigitalPatternTrigger | DAQmxCfgDigPatternStartTrig |
| ConfigureNone | DAQmxDisableStartTrig |
| ConfigureTimeTrigger | DAQmxCfgTimeStartTrig |
| Switch |  |
| SetTopologyAndReset | DAQmxSwitchSetTopologyAndReset |
| WaitForSettling | DAQmxSwitchWaitForSettling |
| TableScale |  |
| TableScale constructor | DAQmxCreateTableScale |
| Task |  |
| AddGlobalChannel | DAQmxAddGlobalChansToTask |
| ConfigureLogging | DAQmxConfigureLogging |
| Control | DAQmxTaskControl |
| CounterOutput | DAQmxRegisterSignalEvent |
| DigitalChangeDetection | DAQmxRegisterSignalEvent |
| Devices | DAQmxGetNthTaskDevice |
| Dispose | DAQmxClearTask |
| Done | DAQmxRegisterDoneEvent |
| EveryNSamplesRead | DAQmxRegisterEveryNSamplesEvent |
| EveryNSamplesWritten | DAQmxRegisterEveryNSamplesEvent |
| IsDone | DAQmxIsTaskDone |
| SampleClock | DAQmxRegisterSignalEvent |
| SampleComplete | DAQmxRegisterSignalEvent |
| Start | DAQmxStartTask |
| StartNewFile | DAQmxStartNewFile |
| Stop | DAQmxStopTask |
| Task constructor | DAQmxCreateTask |
| WaitForValidTimestamp | DAQmxWaitForValidTimestamp |
| WaitUntilDone | DAQmxWaitUntilTaskDone |
| Timing |  |
| ConfigureChangeDetection | DAQmxCfgChangeDetectionTiming |
| ConfigureHandshaking | DAQmxCfgHandshakingTiming |
| ConfigureHandshakingBurstExportClock | DAQmxCfgBurstHandshakingTimingExportClock |
| ConfigureHandshakingBurstImportClock | DAQmxCfgBurstHandshakingTimingImportClock |
| ConfigureImplicit | DAQmxCfgImplicitTiming |
| ConfigurePipelinedSampleClock | DAQmxCfgPipelinedSampClkTiming |
| ConfigureSampleClock | DAQmxCfgSampClkTiming |
| Watchdog |  |
| ClearExpiration | DAQmxControlWatchdogTask |
| ResetTimer | DAQmxControlWatchdogTask |

Parent topic:

NI-DAQmx .NET Class Library Help

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=legal-info.html language=enus -->
## TOPIC 00004: Legal Information

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `legal-info.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/legal-info.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: Limited Warranty Copyright Trademarks Patents Export Compliance Information Warning Regarding Use of NI Products

Legal Information

[Limited Warranty](limited-warranty.html)

[Copyright](copyright.html)

[Trademarks](trademarks.html)

[Patents](patents.html)

[Export Compliance Information](export-compliance.html)

[Warning Regarding Use of NI Products](warning.html)

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=limited-warranty.html language=enus -->
## TOPIC 00005: Limited Warranty

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `limited-warranty.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/limited-warranty.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: This document is provided "as is" and is subject to being changed, without notice, in future editions. For the latest version, refer to ni.com/manuals. NI reviews this document carefully for technical accuracy; however, NI MAKES NO EXPRESS OR IMPLIED WARRANTIES AS TO THE ACCURACY OF THE INFORMATION

Limited Warranty

This document is provided "as is" and is subject to being changed, without notice, in future editions. For the latest version, refer to 
 ni.com/manuals. NI reviews this document carefully for technical accuracy; however, NI MAKES NO EXPRESS OR IMPLIED WARRANTIES AS TO THE ACCURACY OF THE INFORMATION CONTAINED HEREIN AND SHALL NOT BE LIABLE FOR ANY ERRORS.

NI warrants that its hardware products will be free of defects in materials and workmanship that cause the product to fail to substantially conform to the applicable NI published specifications for one (1) year from the date of invoice.

For a period of ninety (90) days from the date of invoice, NI warrants that (i) its software products will perform substantially in accordance with the applicable documentation provided with the software and (ii) the software media will be free from defects in materials and workmanship.

If NI receives notice of a defect or non-conformance during the applicable warranty period, NI will, in its discretion: (i) repair or replace the affected product, or (ii) refund the fees paid for the affected product. Repaired or replaced hardware will be warranted for the remainder of the original warranty period or ninety (90) days, whichever is longer. If NI elects to repair or replace the product, NI may use new or refurbished parts or products that are equivalent to new in performance and reliability and are at least functionally equivalent to the original part or product.

You must obtain an RMA number from NI before returning any product to NI. NI reserves the right to charge a fee for examining and testing hardware not covered by the Limited Warranty.

This Limited Warranty does not apply if the defect of the product resulted from improper or inadequate maintenance, installation, repair, or calibration (performed by a party other than NI); unauthorized modification; improper environment; use of an improper hardware or software key; improper use or operation outside of the specification for the product; improper voltages; accident, abuse, or neglect; or a hazard such as lightning, flood, or other act of nature.

THE REMEDIES SET FORTH ABOVE ARE EXCLUSIVE AND THE CUSTOMER’S SOLE REMEDIES, AND SHALL APPLY EVEN IF SUCH REMEDIES FAIL OF THEIR ESSENTIAL PURPOSE.

EXCEPT AS EXPRESSLY SET FORTH HEREIN, PRODUCTS ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND AND NI DISCLAIMS ALL WARRANTIES, EXPRESSED OR IMPLIED, WITH RESPECT TO THE PRODUCTS, INCLUDING ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE OR NON-INFRINGEMENT, AND ANY WARRANTIES THAT MAY ARISE FROM USAGE OF TRADE OR COURSE OF DEALING. NI DOES NOT WARRANT, GUARANTEE, OR MAKE ANY REPRESENTATIONS REGARDING THE USE OF OR THE RESULTS OF THE USE OF THE PRODUCTS IN TERMS OF CORRECTNESS, ACCURACY, RELIABILITY, OR OTHERWISE. NI DOES NOT WARRANT THAT THE OPERATION OF THE PRODUCTS WILL BE UNINTERRUPTED OR ERROR FREE.

In the event that you and NI have a separate signed written agreement with warranty terms covering the products, then the warranty terms in the separate agreement shall control.

Parent topic:

Legal Information

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmx64bitsupport.html language=enus -->
## TOPIC 00006: Working with 64-bit .NET Support for NI-DAQmx

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmx64bitsupport.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmx64bitsupport.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the NI-DAQmx .NET platform-specific assembly for the 64-bit (x64) platform to create 64-bit NI-DAQmx applications. This assembly, NationalInstruments.DAQmx.dll , is located in the Program Files\National Instruments\<Product Name>\DotNET\Assemblies (64-bit)\Current directory. The assembly

Working with 64-bit .NET Support for NI-DAQmx

You can use the NI-DAQmx .NET platform-specific assembly for the 64-bit (x64) platform to create 64-bit NI-DAQmx applications. This assembly, 
 NationalInstruments.DAQmx.dll , is located in the 
 Program Files\National Instruments\<Product Name>\DotNET\Assemblies (64-bit)\Current directory.

The assembly name for the 64-bit platform-specific assembly is the same as the assembly name for the 32-bit platform-specific assembly, 
 NationalInstruments.DAQmx.dll, and the location for the 32-bit (x86) platform-specific assembly is located in the 
 Program Files\National Instruments\ProductName\DotNET\Assemblies\Current directory.

Note

Not all NI DAQ hardware supported by NI-DAQmx is supported in 64-bit user mode. Refer to the 
 *NI-DAQ Readme* for more information, installed at 
 Start»All Programs»National Instruments»NI-DAQ»NI-DAQ Readme.

#### Processor Architectures and the .NET CLR

The .NET Framework, versions 2.0 and later, includes different versions of the Common Language Runtime (CLR) for different processor architectures. Processor architectures supported by the CLR include x86, Itanium, and x64. x86 is a 32-bit architecture, while Itanium and x64 are 64-bit architectures.

Different variants of Windows operating systems exist to support different architectures. For example, Windows Vista 32-bit supports the x86 architecture and Windows Vista 64-bit supports the x64 architecture. Additionally, the x64 architecture supports the x86 instruction set, allowing 64-bit versions of Windows to include the WOW64 emulator. Consequently, both the 32-bit x86 version of the CLR and the 64-bit x64 version of the CLR can run on 64-bit versions of Windows. Applications that run under the x86 version of the CLR are 32-bit applications. Applications that run under the 64-bit version of the CLR are 64-bit applications. 64-bit applications cannot load 32-bit assemblies, and 32-bit applications cannot load 64-bit assemblies.

#### Platform-Specific and Platform-Agnostic Assemblies

Every assembly built for the.NET Framework 2.0 and later specifies a target platform. The target platform indicates whether the assembly can be run with the 32-bit, x86 version of the CLR or the 64-bit, x64 version of the CLR. Target platforms supported by NI assemblies include x86, x64, and AnyCPU.

The x86 target platform indicates that the assembly is compiled for and can be run only under the 32-bit, x86 version of the CLR. The x64 target platform indicates that the assembly is compiled for and can be run only under the 64-bit, x64 version of the CLR. The AnyCPU target platform indicates that the assembly is compiled in a manner that allows it to be run under any version of the CLR. Assemblies with target platform set to x86 or x64 are referred to as platform-specific assemblies. Assemblies with target platform set to AnyCPU are referred to as platform-agnostic assemblies.

The following table summarizes the preceding information:

| Assembly Target Platform | Compilers | Operating Systems | CLR Versions | Assembly Type |
| --- | --- | --- | --- | --- |
| x86 | Visual C#, Visual Basic .NET | 32-bit, 64-bit | x86 | Platform-Specific |
| x64 | Visual C#, Visual Basic .NET | 64-bit | x64 | Platform-Specific |
| AnyCPU | Visual C#, Visual Basic .NET | 32-bit, 64-bit | x86, x64 | Platform-Agnostic |

The following example demonstrates how platform-specific and platform-agnostic assemblies are used in platform-specific and platform-agnostic applications.

If you have the following three assemblies:

| Assembly Name | Target Platform |
| --- | --- |
| Assembly1_AnyCPU.dll | Any CPU (AnyCPU in Visual Basic) |
| Assembly2_x86.dll | x86 |
| Assembly3_x64.dll | x64 |

And the following three applications:

| Application Name | Target Platform |
| --- | --- |
| Application1_AnyCPU.exe | Any CPU (AnyCPU in Visual Basic) |
| Application2_x86.exe | x86 |
| Application3_x64.exe | x64 |

1. Application1_AnyCPU.exe runs as a 32-bit process. The application can load 
 Assembly1_AnyCPU.dll and 
 Assembly2_x86.dll , because these assemblies are Any CPU and x86 assemblies, respectively. The application generates a BadImageFormatException if it tries to load 
 Assembly3_x64.dll , because an x64 assembly cannot be loaded into a 32-bit process.
2. Application2_x86.exe runs as a 32-bit process. The application can load 
 Assembly1_AnyCPU.dll and 
 Assembly2_x86.dll , because these assemblies are Any CPU and x86 DLLs, respectively. The application generates a 
 BadImageFormatException if it tries to load 
 Assembly3_x64.dll , because an x64 assembly cannot be loaded into a 32-bit process.
3. Application3_x64.exe does not run because a 32-bit operating system cannot run a 64-bit application.

1. Application1_AnyCPU.exe runs as a 64-bit process. The application can load 
 Assembly1_AnyCPU.dll and 
 Assembly3_x64.dll , because these assemblies are Any CPU and x64, respectively. The application generates a 
 BadImageFormatException when it tries to load 
 Assembly2_x86.dll , because an x86 assembly cannot be loaded into a 64-bit process.
2. Application2_x86.exe runs as a 32-bit process, under the WOW64 emulator. The application can load 
 Assembly1_AnyCPU.dll and 
 Assembly2_x86.dll , because these assemblies are Any CPU and x86, respectively. The application generates a 
 BadImageFormatException when it tries to load 
 Assembly3_x64.dll , because an x64 assembly cannot be loaded into a 32-bit process.
3. Application3_x64.exe runs as a 64-bit process. The application can load 
 Assembly1_AnyCPU.dll and 
 Assembly3_x64.dll , because these assemblies are Any CPU and x64, respectively. The application generates a 
 BadImageFormatException when it tries to load 
 Assembly2_x86.dll , because an x86 assembly cannot be loaded into a 64-bit process.

#### Platform-Specific Assembly Runtime Reference Resolution

When you run a platform-agnostic or x64 platform-specific application on a 64-bit operating system and your application references a platform-specific assembly, the CLR automatically uses the x64 assembly, even if the project used to build the application references an x86 version of a platform-specific assembly.

Note

BadImageFormatException

#### Platform-Specific and Platform-Agnostic Assemblies

Some NI class libraries include platform-specific assemblies and some include platform-agnostic assemblies. Class libraries, such as the NI-DAQmx .NET library, that include platform-specific assemblies include two versions of the assembly, one that supports the x86 platform and one that supports the x64 platform. Both versions of the assembly have the same name, but they are installed to different locations:

- NI .NET x86 and Any CPU assemblies are, by default, installed in the 
 Program Files(x86)\National Instruments\<Product Name>\DotNET\Assemblies\Current directory.
- NI .NET x64 assemblies are, by default, installed in the 
 Program Files(x86)\National Instruments\<Product Name>\DotNET\Assemblies (64-bit)\Current directory.

#### Using a 32-bit Assembly in a 64-bit Project

When you compile a project with target platform set to x64 with a reference to an x86 assembly, the compiler generates a warning. Change the project target platform to x86 or AnyCPU to resolve this warning.

- The Visual C# compiler warning is: 
 Warning CS1607 Assembly generation -- Referenced assembly targets a different processor . Refer to Warning CS1607 for more information.
- The Visual Basic .NET compiler warning is: 
 Warning BC40010: Possible problem detected while building assembly '<assemblyname>'. Refer to Warning BC40010 for more information.

Tip

#### .NET Framework Array Size Limitation

The .NET Framework 4.0 CLR (both 32-bit and 64-bit versions) and earlier versions limit the maximum size of a single object, including arrays, to 2 gigabytes (GB). As a result of this 2 GB maximum, the number of items that an array can contain depends on the type and what the type contains.

As a consequence of this array size limitation, NI .NET arrays cannot return the same number of items as the corresponding C API can in an unmanaged layer, as unmanaged 64-bit applications can reference blocks of memory larger than 2 GB.

These restrictions typically affect input and output operations. For example, the NI-DAQmx .NET class library restricts the number of samples you can obtain in each read operation.

In .NET Framework 4.5, you can use the <gcAllowVeryLargeObjects> element to enable arrays that are greater than 2 gigabytes (GB) in total size. NI .NET class libraries do not support arrays greater than 2 GB in size; therefore, using arrays greater than 2 GB in NI .NET class libraries could result in errors or unexpected behavior.

#### Deploying 64-bit Applications

To facilitate use in Visual Studio Setup projects, all NI .NET class libraries that support 64-bit include both 32-bit and 64-bit deployment merge modules. This is true regardless of whether the class library includes platform-specific or platform-agnostic assemblies.

Parent topic:

NI-DAQmx .NET Class Library Help

Related information:

- Running 32-bit Applications
- <gcAllowVeryLargeObjects> Element
- Warning BC40010
- Warning CS1607
- System.BadImageFormatException

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxanalograndw.html language=enus -->
## TOPIC 00007: Analog Waveform Reads and Writes with the NI-DAQmx .NET Library

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxanalograndw.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxanalograndw.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: The recommended way of performing multi-sample analog reads and writes with the NI-DAQmx .NET library is to use waveform reads and writes. These methods use the AnalogWaveform<TData> type to encapsulate analog samples over time.

Analog Waveform Reads and Writes with the NI-DAQmx .NET Library

The recommended way of performing multi-sample analog reads and writes with the NI-DAQmx .NET library is to use waveform reads and writes.

These methods use the AnalogWaveform<TData> type to encapsulate analog samples over time.

Parent topic:

Reading and Writing with NI-DAQmx Streams

Related information:

- AnalogWaveform<TData> Class

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxanalogwaveformreads.html language=enus -->
## TOPIC 00008: Analog Waveform Reads

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxanalogwaveformreads.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxanalogwaveformreads.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: To perform an analog waveform read, call AnalogSingleChannelReader.ReadWaveform or AnalogMultiChannelReader.ReadWaveform. NI-DAQmx returns an AnalogWaveform<TData> or an array of AnalogWaveform<TData> objects, respectively. Each AnalogWaveform<TData> returned represents one channel and may contain t

Analog Waveform Reads

To perform an analog waveform read, call 
 AnalogSingleChannelReader.ReadWaveform or 
 AnalogMultiChannelReader.ReadWaveform.

NI-DAQmx returns an 
 **AnalogWaveform<TData>** or an array of AnalogWaveform<TData> objects, respectively. Each AnalogWaveform<TData> returned represents one channel and may contain timing information or extended properties, depending on the value of the WaveformAttributeMode property on the DaqStream class.

NI-DAQmx can only determine the sample interval for a waveform read if the task is using sample clock timing. In all other cases, the waveform returned has its SampleIntervalMode set to None. For more information, refer to 
 *Waveform Timing Limitations* in the 
 *NI-DAQmx Help* and the WaveformTiming class.

NI-DAQmx returns the following extended properties:

- NI_ChannelName —The name of the channel.
- NI_UnitDescription —Describes the units for the channel.

The following example demonstrates how to perform an analog waveform read on a task with a single channel:

VB.NET

```text
' Given a Task instance "myTask", 
' Create the reader and attach it to the stream 
Dim reader as AnalogSingleChannelReader = New AnalogSingleChannelReader(myTask.Stream)
' Perform the read 
Dim data as AnalogWaveform(Of Double) = reader.ReadWaveform(100)
```

C#

```text
// Given a Task instance "myTask", 
// Create the reader and attach it to the stream
AnalogSingleChannelReader reader = new AnalogSingleChannelReader(myTask.Stream);
// Perform the read
AnalogWaveform<double> data = reader.ReadWaveform(100);
```

The following example demonstrates how to perform an analog waveform read on a task with multiple channels:

VB.NET

```text
' Given a Task instance "myTask", 
' Create the reader and attach it to the stream 
Dim reader as AnalogMultiChannelReader = New AnalogMultiChannelReader(myTask.Stream)
' Perform the read 
Dim data as AnalogWaveform(Of Double)() = reader.ReadWaveform(100)
```

C#

```text
// Given a Task instance "myTask", 
// Create the reader and attach it to the stream
AnalogMultiChannelReader reader = new AnalogMultiChannelReader(myTask.Stream);
// Perform the read
AnalogWaveform<double>[] data = reader.ReadWaveform(100);
```

Parent topic:

Analog Waveform Reads and Writes with the NI-DAQmx .NET Library

Related information:

- AnalogSingleChannelReader.ReadWaveform Method
- AnalogMultiChannelReader.ReadWaveform Method
- AnalogWaveform<TData> Class
- WaveformTiming Class
- Waveform Timing Limitations

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxanalogwaveformwrites.html language=enus -->
## TOPIC 00009: Analog Waveform Writes

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxanalogwaveformwrites.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxanalogwaveformwrites.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: To perform an analog waveform write, call the AnalogSingleChannelWriter.WriteWaveform or AnalogMultiChannelWriter.WriteWaveform method with one AnalogWaveform<TData> or array of AnalogWaveform<TData> objects, respectively, for each channel. When performing a write, NI-DAQmx ignores timing informatio

Analog Waveform Writes

To perform an analog waveform write, call the 
 AnalogSingleChannelWriter.WriteWaveform or 
 AnalogMultiChannelWriter.WriteWaveform method with one AnalogWaveform<TData> or array of AnalogWaveform<TData> objects, respectively, for each channel.

When performing a write, NI-DAQmx ignores timing information and extended properties set on the AnalogWaveform<TData>; to configure timing, you must use the ConfigureSampleClock method instead.

The following example demonstrates how to perform an analog waveform write on a task with a single channel:

VB.NET

```text
' Given a Task instance "myTask", 
' Initialize the data 
Dim data As AnalogWaveform(Of Double) = New AnalogWaveform(Of Double)(100)
' Create the writer and attach it to the stream 
Dim writer As AnalogSingleChannelWriter = New AnalogSingleChannelWriter(myTask.Stream)
' Perform the write
writer.WriteWaveform(True, data)
```

C#

```text
// Given a Task instance "myTask", 
// Initialize the data
AnalogWaveform<double> data = new AnalogWaveform<double>(100);
// Create the writer and attach it to the stream
AnalogSingleChannelWriter writer = new AnalogSingleChannelWriter(myTask.Stream);
// Perform the write
writer.WriteWaveform(true, data);
```

The following example demonstrates how to perform an analog waveform write on a task with multiple channels:

VB.NET

```text
' Given a Task instance "myTask", 
' Initialize the data 
Dim data(2) As AnalogWaveform(Of Double)
data(0) = New AnalogWaveform(Of Double)(100)
data(1) = New AnalogWaveform(Of Double)(100)
' Create the writer and attach it to the stream 
Dim writer As AnalogMultiChannelWriter = New AnalogMultiChannelWriter(myTask.Stream)
' Perform the write
writer.WriteWaveform(True, data)
```

C#

```text
// Given a Task instance "myTask", 
// Initialize the data
AnalogWaveform<double>[] data = new AnalogWaveform<double>[2];
data[0] = new AnalogWaveform<double>(100);
data[1] = new AnalogWaveform<double>(100);
// Create the writer and attach it to the stream
AnalogMultiChannelWriter writer = new AnalogMultiChannelWriter(myTask.Stream);
// Perform the write
writer.WriteWaveform(true, data);
```

Parent topic:

Analog Waveform Reads and Writes with the NI-DAQmx .NET Library

Related information:

- AnalogSingleChannelWriter.WriteWaveform Method
- AnalogMultiChannelWriter.WriteWaveform Method
- AnalogWaveform<TData> Class
- ConfigureSampleClock Method

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxasyncrandw.html language=enus -->
## TOPIC 00010: Asynchronous Reads and Writes

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxasyncrandw.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxasyncrandw.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-DAQmx library follows the .NET Framework asynchronous programming model (APM) or IAsyncResult pattern for asynchronous operations. Refer to Asynchronous Programming Model (APM) in the .NET Framework Developer's Guide for more information. You start an asynchronous operation in the NI-DAQmx li

Asynchronous Reads and Writes

Note

IAsyncResult

Asynchronous Programming Model (APM)

.NET Framework Developer's Guide

You start an asynchronous operation in the NI-DAQmx library by calling a BeginRead or BeginWrite method on a reader or writer class. This method returns an instance of the IAsyncResult interface that represents the asynchronous operation. This interface provides methods for determining if the operation has completed, for waiting until the operation is complete, and other operations. Optionally, you can pass a delegate to the BeginRead or BeginWrite method if you want to receive a callback when the operation completes.

Call an EndRead or EndWrite method on the reader or writer class to finish an asynchronous operation. Call the EndRead or EndWrite method that matches the BeginRead or BeginWrite method that you called to start the operation. When the EndRead or EndWrite method is called, any exception that occurred during the asynchronous operation is thrown. If the operation is not yet complete, EndRead or EndWrite waits for it to complete. In the case of a read operation, the data that was read is returned from the EndRead method. You can call the EndRead or EndWrite method from inside a callback, as shown in the following example:

VB.NET

```text
Class DAQmxAsyncRead

    Private reader As AnalogSingleChannelReader

    Public Sub New(ByVal myTask As Task)
        'Create the reader
        reader = New AnalogSingleChannelReader(myTask.Stream)
        'Acquire 100 samples 
        Dim handle As IAsyncResult
        handle = reader.BeginReadMultiSample(100, AddressOf OnDataReady, Nothing)
    End Sub 

    Public Sub OnDataReady(i As IAsyncResult)
        'Retrieve the data that was read. 
        'At this point, any exceptions that occurred during the asynchronous read are thrown 
        Dim data As Double()
        data = reader.EndReadMultiSample(i)

        'You can call the BeginReadMultiSample method here again 
    End Sub 

End Class
```

C#

```text
class DAQmxAsyncRead
{
    private AnalogSingleChannelReader reader = null;

    public DAQmxAsyncRead(Task myTask)
    {
        // Create the reader.
        reader = new AnalogSingleChannelReader(myTask.Stream);
        // Acquire 100 samples.
        IAsyncResult handle = reader.BeginReadMultiSample(100, OnDataReady, null);
    }

    public void OnDataReady(IAsyncResult i)
    {
        // Retrieve the data that was read. 
        // At this point, any exceptions that occurred during the asynchronous read are thrown.
        double[] data = reader.EndReadMultiSample(i);

        // You can call the BeginReadMultiSample method here again.
    }
}
```

Note

Parent topic:

Reading and Writing with NI-DAQmx Streams

Related concepts:

- Events

Related information:

- Asynchronous Programming Model (APM)
- System.Threading.ManualResetEvent Class
- System.IAsyncResult

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxasynctaskdisp.html language=enus -->
## TOPIC 00011: Safe Task Disposal When Using Asynchronous Callbacks

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxasynctaskdisp.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxasynctaskdisp.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you acquire or generate data using an asynchronous callback and you have SynchronizeCallbacks set to False, the callback executes on a thread other than the main thread. This document refers to the other thread as a worker thread. Because you do not have control over switching between the main th

Safe Task Disposal When Using Asynchronous Callbacks

If you acquire or generate data using an asynchronous callback and you have 
 SynchronizeCallbacks set to False, the callback executes on a thread other than the main thread. This document refers to the other thread as a worker thread.

Because you do not have control over switching between the main thread and the worker thread, an exception could be thrown when the worker thread tries to access the Task after the main thread has disposed the Task. To safely dispose the Task, when you do not have control over thread switching, you need a synchronization mechanism by which the main thread can wait for the worker thread to complete all callbacks before the main thread disposes the Task. Also, the main thread needs to notify the worker thread not to initiate additional read or write calls that could queue new callbacks before the worker thread completes pending callbacks.

The following sections explain how to safely dispose the Task when working with asynchronous callbacks.

Execution Path for Using ManualResetEvent to Safely Dispose Task

This diagram demonstrates the execution path for using ManualResetEvent to safely dispose a task.

[IMAGE alt='1378' src='GUID-1C41758E-5B50-4EE4-8871-6434B4DA78C6-a5.png']

Using ManualResetEvent to Safely Dispose a Task

VB.NET

```text
Imports System
Imports System.Threading
Imports NationalInstruments
Imports NationalInstruments.DAQmx

Public Class Program

    Shared Sub Main()
        Dim daqReader As SafeTaskDisposer = New SafeTaskDisposer()
        daqReader.StartAcquisition()
        Console.WriteLine("Press enter key to terminate the task...")
        Console.Read()
        daqReader.Dispose()
    End Sub 

End Class 

Public Class SafeTaskDisposer
    Implements IDisposable
    Private runningTaskWaitHandle As ManualResetEvent 
    ' Used for synchronization while disposing task 
    Private runningTask As Task
    Private continuousTask As Task
    Private analogReader As AnalogMultiChannelReader
    Private analogCallback As AsyncCallback
    Private data As AnalogWaveform(Of Double)()

    Public Sub New()
        runningTaskWaitHandle = New ManualResetEvent(True) 
        ' Instantiate wait handle 
    End Sub 

#Region "IDisposable Members" 

    ' Dispose method executes on main thread 
    Public Sub Dispose() Implements IDisposable.Dispose
        SafelyDisposeTask()
    End Sub 

#End Region 

    ' StartAcquisition method executes on main thread 
    Public Sub StartAcquisition()
        Try
            continuousTask = New Task()
            ' Configure the task and create required channels in task
            continuousTask.AIChannels.CreateVoltageChannel("dev1/ai0:3", "", AITerminalConfiguration.Differential, -10.0, 10.0, AIVoltageUnits.Volts)
            continuousTask.Timing.ConfigureSampleClock("", 1000, SampleClockActiveEdge.Rising, SampleQuantityMode.ContinuousSamples, 1000)
            continuousTask.Control(TaskAction.Verify)
            analogReader = New AnalogMultiChannelReader(continuousTask.Stream)
            analogReader.SynchronizeCallbacks = False
            analogCallback = New AsyncCallback(AddressOf AnalogReadCallback)
            ' Create a reference (runningTask) to the task running (continuousTask)
            runningTask = continuousTask
            analogReader.BeginReadWaveform(Convert.ToInt32(continuousTask.Timing.SamplesPerChannel), analogCallback, continuousTask)
        Catch ex As DaqException
            ' Exception thrown
            runningTask = Nothing
            continuousTask.Dispose()
        End Try 
    End Sub 

    ' StopAcquisition method executes on main thread 
    Public Sub StopAcquisition()
        SafelyDisposeTask()
    End Sub 

    ' AnalogReadCallback method executes on 
    '   - worker thread when SynchronizeCallback is set to false (current behavior) 
    '   - main thread when SynchronizeCallback is set to true 
    Private Sub AnalogReadCallback(ByVal ar As IAsyncResult)
        Try 
            ' Check to see whether the task is still running 
            If runningTask IsNot Nothing AndAlso ReferenceEquals(runningTask, ar.AsyncState) Then
                data = analogReader.EndReadWaveform(ar)

                ' If ProcessData is updating UI components created on the main thread, then 
                ' invoke ProcessData on the main thread when SynchronizeCallback is  
                ' set to false.
                ProcessData()

                analogReader.BeginReadWaveform(Convert.ToInt32(continuousTask.Timing.SamplesPerChannel), analogCallback, continuousTask)
            Else 
                ' Signal waiting thread to proceed
                SignalThread()
            End If 
        Catch ex As DaqException
            ' Exception thrown
            runningTask = Nothing
            continuousTask.Dispose()
            ' Signal waiting thread to proceed
            SignalThread()
        End Try 

    End Sub 

    ' ProcessData method executes on same thread on which AnalogReadCallback executes 
    Private Sub ProcessData()
        ' If this method is updating UI components created on the main thread, then invoke 
        ' the UI code or this entire method on the main thread when SynchronizeCallback 
        ' is set to false. 
    End Sub 

    ' SafelyDisposeTask method executes on main thread 
    Private Sub SafelyDisposeTask()
        If runningTask IsNot Nothing Then 
            If Not analogReader.SynchronizeCallbacks Then 
                ' When SynchronizeCallback is false, the callback will be executed on 
                ' the worker thread. In this case, wait for the pending callback to be 
                ' completed before disposing task. 


                ' Reset wait handle to wait for callback, which is on the worker thread
                runningTaskWaitHandle.Reset()

                ' Set runningTask to Nothing to indicate the callback, not to initiate  
                ' additional reads
                runningTask = Nothing 

                ' Wait for pending callback on worker thread.  
                '   - If the last operation on runningTaskWaitHandle is Set (in SignalThread),  
                '     WaitOne will not wait and proceed to execute the next line of code.  
                '   - If the last operation on runningTaskWaitHandle is Reset (in  
                '     SafelyDisposeTask), WaitOne will make the main thread wait for the  
                '     signal (Set Operation on runningTaskWaitHandle) 
                runningTaskWaitHandle.WaitOne()
            Else 
                ' When SynchronizeCallback is true, this method and the callback will  
                ' be executed on the main thread. In that case, there is no need to wait for pending  
                ' callback to be completed before disposing task, because the callack  
                ' and this method cannot execute at the same time. 


                ' Set runningTask to Nothing to indicate the callback, not to initiate  
                ' additional reads
                runningTask = Nothing 
            End If 
        End If 
        ' Safe to dispose task. 
        If continuousTask IsNot Nothing Then
            continuousTask.Dispose()
        End If 
    End Sub 

    ' SignalThread method executes on worker thread 
    Private Sub SignalThread()
        ' When SynchronizeCallback is false, the callback will be executed on the worker  
        ' thread. In that case, while disposing task, the main thread is waiting on the callback 
        ' which is executing on the worker thread to be completed. Signal (call Set  
        ' operation on runningTaskWaitHandle) the main thread to proceed 
        If Not analogReader.SynchronizeCallbacks Then
            runningTaskWaitHandle.Set()
        End If 
    End Sub 
End Class
```

C#

```text
using System;
using System.Threading;
using NationalInstruments;
using NationalInstruments.DAQmx;

public class Program
{
    static void Main(string[] args)
    {
        SafeTaskDisposer daqReader = new SafeTaskDisposer();
        daqReader.StartAcquisition();
        Console.WriteLine("Press Enter key to terminate the task...");
        Console.Read();
        daqReader.Dispose();
    }
}
public class SafeTaskDisposer : IDisposable
{
    private ManualResetEvent runningTaskWaitHandle; 
    // Used for synchronization while disposing task 
    private Task runningTask;
    private Task continuousTask;
    private AnalogMultiChannelReader analogReader;
    private AsyncCallback analogCallback;
    private AnalogWaveform<double>[] data;

    public SafeTaskDisposer()
    {
        runningTaskWaitHandle = new ManualResetEvent(true); 
        // Instantiate wait handle
    }

    #region IDisposable Members

    // Dispose method executes on the main thread 
    public void Dispose()
    {
        SafelyDisposeTask();
    }

    #endregion 

    // StartAcquisition method executes on the main thread 
    public void StartAcquisition()
    {
        try
        {
            continuousTask = new Task();
            // Configure the task and create required channels in task
            continuousTask.AIChannels.CreateVoltageChannel("dev1/ai0:3", "", AITerminalConfiguration.Differential, -10.0, 10.0, AIVoltageUnits.Volts);
            continuousTask.Timing.ConfigureSampleClock("", 1000, SampleClockActiveEdge.Rising, SampleQuantityMode.ContinuousSamples, 1000);
            continuousTask.Control(TaskAction.Verify);
            analogReader = new AnalogMultiChannelReader(continuousTask.Stream);
            analogReader.SynchronizeCallbacks = false;
            analogCallback = new AsyncCallback(AnalogReadCallback);
            // Create a reference (runningTask) to the task running (continuousTask)
            runningTask = continuousTask;
            analogReader.BeginReadWaveform(Convert.ToInt32(continuousTask.Timing.SamplesPerChannel), analogCallback, continuousTask);
        }
        catch (DaqException ex)
        {
            // Exception thrown
            runningTask = null;
            continuousTask.Dispose();
        }
    }

    // StopAcquisition method executes on the main thread 
    public void StopAcquisition()
    {
        SafelyDisposeTask();
    }

    // AnalogReadCallback method executes on 
    //   - worker thread when SynchronizeCallback is set to false (current behavior) 
    //   - main thread when SynchronizeCallback is set to true 
    private void AnalogReadCallback(IAsyncResult ar)
    {
        try
        {
            // Check to see whether the task is still running 
            if (runningTask != null && runningTask == ar.AsyncState)
            {
                data = analogReader.EndReadWaveform(ar);

                // If ProcessData is updating UI components created on the main thread, then 
                // invoke ProcessData on the main thread when SynchronizeCallback is  
                // set to false.
                ProcessData();

                analogReader.BeginReadWaveform(Convert.ToInt32(continuousTask.Timing.SamplesPerChannel), analogCallback, continuousTask);
            }
            else
            {
                // Signal waiting thread to proceed
                SignalThread();

            }
        }
        catch (DaqException ex)
        {
            // Exception thrown
            runningTask = null;
            continuousTask.Dispose();
            // Signal waiting thread to proceed
            SignalThread();
        }
    }

    // ProcessData method executes on same thread on which AnalogReadCallback executes 
    private void ProcessData()
    {
        // If this method is updating UI components created on the main thread, then invoke 
        // the UI code or this entire method on the main thread when SynchronizeCallback 
        // is set to false.
    }

    // SafelyDisposeTask method executes on the main thread 
    private void SafelyDisposeTask()
    {
        if (runningTask != null)
        {
            if (!analogReader.SynchronizeCallbacks)
            {
                // When SynchronizeCallback is false, the callback will be executed on  
                // the worker thread. In that case, wait for the pending callback to be  
                // completed before disposing task. 

                // Reset wait handle to wait for callback, which is on the worker thread
                runningTaskWaitHandle.Reset();

                // Set runningTask to null to indicate the callback, not to initiate  
                // additional reads
                runningTask = null;

                // Wait for pending callback on the worker thread.  
                //   - If the last operation on runningTaskWaitHandle is Set (in SignalThread),  
                //     WaitOne will not wait and proceed to execute the next line of code. 
                //   - If the last operation on runningTaskWaitHandle is Reset (in  
                //     SafelyDisposeTask), WaitOne will make the main thread wait for the signal  
                //     (Set Operation on runningTaskWaitHandle)

                runningTaskWaitHandle.WaitOne();
            }
            else
            {
                // When SynchronizeCallback is true, this method and the callback will  
                // be executed on the main thread. In that case, there is no need to wait for pending  
                // callback to be completed before disposing task, because the callback  
                // and this method cannot execute at the same time. 

                // Set runningTask to null to indicate the callback, not to initiate  
                // additional reads
                runningTask = null;
            }
        }
        // Safe to dispose task 
        if (continuousTask != null)
        {
            continuousTask.Dispose();
        }
    }

    // SignalThread method executes on the worker thread 
    private void SignalThread()
    {
        // When SynchronizeCallback is false, the callback will be executed on the worker  
        // thread. In that case, while disposing task, the main thread is waiting on the callback 
        // which is executing on the worker thread to be completed. Signal (call Set  
        // operation on runningTaskWaitHandle) the main thread to proceed 
        if (!analogReader.SynchronizeCallbacks)
        {
            runningTaskWaitHandle.Set();
        }
    }
}
```

Special Threading Considerations

- If you update any UI component from a thread other than the thread on which that component was created, you might get an 
 InvalidOperationException . Refer to 
 How to: Make Thread-Safe Calls to Windows Forms Controls for more details.
- Calls to update any UI component should be asynchronous (non-blocking); if the calls are not asynchronous, you risk race conditions and deadlock in your application. These issues could occur because National Instruments recommends you use a synchronizing mechanism to dispose Task .
- Using memory-optimized read methods in these situations could cause a loss of data integrity.

Parent topic:

Tasks

Related information:

- Task Class
- System.Threading.ManualResetEvent Class
- How to: Make Thread-Safe Calls to Windows Forms Controls

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxchannels.html language=enus -->
## TOPIC 00012: Channels

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxchannels.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can associate the following types of channels with a Task in the NI-DAQmx .NET class library: Analog input channels—AIChannel class Analog output channels—AOChannel class Digital input channels—DIChannel class Digital output channels—DOChannel Counter input channels—CIChannel class Counter outpu

Channels

You can associate the following types of channels with a Task in the NI-DAQmx .NET class library:

- Analog input channels— AIChannel class
- Analog output channels— AOChannel class
- Digital input channels— DIChannel class
- Digital output channels— DOChannel
- Counter input channels— CIChannel class
- Counter output channels— COChannel class

These classes contain properties that are specific to a particular type of channel. For instance, properties such as Count are only applicable to counters and are only available on the CIChannel and COChannel classes.

#### Example: Simple Analog Input Voltage Channel

To create a channel, you can use one of the many create channel methods on the channel collections. The following example creates a simple analog input voltage channel:

#### VB.NET

```text
myTask.AIChannels.CreateVoltageChannel( _
    "dev1/ai1", _
    "myChannel", _
    AITerminalConfiguration.Differential, _
    -10.0, _
    10.0, _
    AIVoltageUnits.Volts _
)
```

#### C#

```text
myTask.AIChannels.CreateVoltageChannel(
    "dev1/ai1", // The physical name of the channel 
    "myChannel", // The name to associate with this channel
    AITerminalConfiguration.Differential, // Differential wiring 
    -10.0, // 10 V minimum 
    10.0, // 10 V maximum
    AIVoltageUnits.Volts // Use volts
);
```

#### Example: Channel Indexer

Each collection provides an indexer in Visual C# (the Item method in Visual Basic) that you can use to retrieve a channel associated with a Task object.

Each channel indexer in NI-DAQmx returns a new Channel object which acts as a proxy to configure the Task in terms of the referenced channel. As a result, you can call methods or access properties on a channel, and the effect of these methods and properties persists for the lifetime of the Task. However, NI-DAQmx does not support the removal of channels from existing tasks, so calling Dispose on a Channel releases resources used by the channel proxy object, not the channel itself.

Consider the following two cases, assuming that we have an instance of a Task containing an analog input channel and the Taskhas been verified:

Case 1

#### VB.NET

```text
Dim channel As AIChannel = myTask.AIChannels(0)
MyChannel.Description = "Accessing channel"
MyChannel.Dispose()
Dim description As String = MyChannel.Description
```

#### C#

```text
AIChannel channel = myTask.AIChannels[0];
MyChannel.Description = "Accessing channel";
MyChannel.Dispose();
string description = MyChannel.Description;
```

Case 2

#### VB.NET

```text
myTask.AIChannels(0).Description = "Accessing channel"
myTask.AIChannels(0).Dispose()
Dim description As String = myTask.AIChannels(0).Description
```

#### C#

```text
myTask.AIChannels[0].Description = "Accessing channel";
myTask.AIChannels[0].Dispose();
string description = myTask.AIChannels[0].Description;
```

The channel being accessed in both Case 1 and Case 2 is the same, but Case 1 throws an exception because you cannot access an object once it has been disposed.

In contrast, the Dispose call in Case 2 essentially creates a new AIChannel proxy object and then immediately disposes it. The next line creates a new AIChannelproxy object and then retrieves its Description property. The value of this Description property is set to the same value as it was before the AIChannel proxy object was disposed, which ensures that the state of the Task is preserved.

Note

AIChannelCollection

Task

AOChannelCollection

DIChannelCollection

DOChannelCollection

CIChannelCollection

COChannelCollection

#### Example 2: Channel Indexer

You can use the indexer to retrieve a channel associated with a Task object, as shown in the following example:

#### VB.NET

```text
'Retrieve an AI channel with the virtual name "myChannel" 
Dim ch as AIChannel
ch = myTask.AIChannels.Item("myChannel")
```

#### C#

```text
// Retrieve an AI channel with the virtual name "myChannel"
AIChannel ch = myTask.AIChannels["myChannel"];
```

The name you pass to the indexer must be the virtual name of the channel, not the physical name. If you use a comma or colon in the name, you also can use the indexer to retrieve a channel object that represents multiple channels, as shown in the following example:

#### VB.NET

```text
'The AIChannel object, myAIChannel, represents both myChannel0 and myChannel1 
Dim myAIChannel as AIChannel
myAIChannel = myTask.AIChannels.Item("myChannel0,myChannel1")
'Setting this property on myAIChannel sets the property for both channels
myAIChannel.Maximum = 10 
'This is an equivalent approach using colon: 
Dim myAIChannel as AIChannel
myAIChannel = myTask.AIChannels.Item("myChannel0:1")
myAIChannel.Maximum = 10
```

#### C#

```text
// The AIChannel object, myAIChannel, represents both myChanne0 and myChannel1
AIChannel myAIChannel = myTask.AIChannels["myChannel0,myChannel1"];
// Setting this property on myAIChannel sets the property for both channels
myAIChannel.Maximum = 10;
// This is an equivalent approach using colon:
AIChannel myAIChannel = myTask.AIChannels["myChannel0:1"];
myAIChannel.Maximum = 10;
```

#### Example: Channel Indexer Overload

Each channel collection also provides an overload of the indexer that accepts an integer parameter. You can use the overload to retrieve the 
 nth channel in the collection, or use it in a 
 for loop to iterate over the collection, as shown in the following example:

#### VB.NET

```text
'Retrieve the fourth channel 
Dim fourthLine as DOChannel
fourthLine = myTask.DOChannels.Item(3) 
'Note that the index is zero-based 

'Iterate over the all of the channels 
For i As Integer = 0 to myTask.DOChannels.Count - 1
    Console.WriteLine(myTask.DOChannels.Item(i).VirtualName)
Next
```

#### C#

```text
// Retrieve the fourth channel
DOChannel fourthLine = myTask.DOChannels[3]; 
// Note that the index is zero-based 

// Iterate over the all of the channels 
for(int i = 0; i < myTask.DOChannels.Count; i++ )
{
    Console.WriteLine(myTask.DOChannels[i].VirtualName);
}
```

Parent topic:

NI-DAQmx .NET Class Library Help

Related information:

- Task Class

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxcreatingtask.html language=enus -->
## TOPIC 00013: Creating an NI-DAQmx Task from an Existing Task in MAX

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxcreatingtask.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxcreatingtask.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use the NI-DAQmx .NET library to load a task that you have already configured and saved in Measurement & Automation Explorer (MAX). You create and configure NI-DAQmx tasks in MAX through an interactive, graphical interface, which does not require writing code. You can load tasks saved in MAX

Creating an NI-DAQmx Task from an Existing Task in MAX

You can use the NI-DAQmx .NET library to load a task that you have already configured and saved in Measurement & Automation Explorer (MAX).

You create and configure NI-DAQmx tasks in MAX through an interactive, graphical interface, which does not require writing code. You can load tasks saved in MAX and then run the tasks in any programming language that has access to an NI-DAQmx library including C, Visual C#, Visual Basic .NET, and LabVIEW.

Complete the following steps to create a task in MAX:

1. From the Start menu, select 
 Start»Program Files»National Instruments»Measurement & Automation Explorer to launch MAX.
2. In the left-hand pane, right-click 
 Data Neighborhood and select 
 Create New.
3. Select 
 NI-DAQmx Task and select 
 Next.
4. Follow the on-screen steps to create and configure the NI-DAQmx task.

The following code shows how to load a task saved in MAX using Visual C# or Visual Basic .NET:

VB.NET

```text
Dim myTask as Task
myTask = DaqSystem.Local.LoadTask("mySavedTaskName")
```

C#

```text
Task myTask = DaqSystem.Local.LoadTask("mySavedTaskName");
```

Note

Deployment

NI-DAQmx

Parent topic:

Task Creation

Related information:

- Task Class
- DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxdigitalrandw.html language=enus -->
## TOPIC 00014: Digital Waveform Reads and Writes with the NI-DAQmx .NET Class Library

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxdigitalrandw.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxdigitalrandw.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: The recommended way of performing multi-sample digital reads and writes with the NI-DAQmx .NET library is to use waveform reads and writes. These methods use the DigitalWaveform type to encapsulate digital samples over time.

Digital Waveform Reads and Writes with the NI-DAQmx .NET Class Library

The recommended way of performing multi-sample digital reads and writes with the NI-DAQmx .NET library is to use waveform reads and writes.

These methods use the DigitalWaveform type to encapsulate digital samples over time.

Parent topic:

Reading and Writing with NI-DAQmx Streams

Related information:

- DigitalWaveform Class

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxdigitalwaveformreads.html language=enus -->
## TOPIC 00015: Digital Waveform Reads

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxdigitalwaveformreads.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxdigitalwaveformreads.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: To perform a digital waveform read, call DigitalSingleChannelReader.ReadWaveform or DigitalMultiChannelReader.ReadWaveform. NI-DAQmx returns a DigitalWaveform or an array of DigitalWaveform objects, respectively. Each DigitalWaveform returned represents one channel and may contain timing information

Digital Waveform Reads

To perform a digital waveform read, call 
 DigitalSingleChannelReader.ReadWaveform or 
 DigitalMultiChannelReader.ReadWaveform.

NI-DAQmx returns a DigitalWaveform or an array of DigitalWaveform objects, respectively. Each DigitalWaveform returned represents one channel and may contain timing information or extended properties, depending on the value of the WaveformAttributeMode property on the DaqStream class.

NI-DAQmx can only determine the sample interval for a waveform read if the task is using sample clock timing. In all other cases, the waveform returned has its SampleIntervalMode set to None. For more information, refer to 
 *Waveform Timing Limitations* in the 
 *NI-DAQmx Help* and the WaveformTiming class.

NI-DAQmx returns the following extended properties:

- NI_ChannelName —The name of the channel.
- NI_UnitDescription —Describes the units for the channel.

The following example demonstrates how to perform a digital waveform read on a task with a single channel:

VB.NET

```text
' Given a Task instance "myTask", 
' Create the reader and attach it to the stream 
Dim reader as DigitalSingleChannelReader = New DigitalSingleChannelReader(myTask.Stream)
' Perform the read 
Dim data as DigitalWaveform = reader.ReadWaveform(100)
```

C#

```text
// Given a Task instance "myTask", 
// Create the reader and attach it to the stream
DigitalSingleChannelReader reader = new DigitalSingleChannelReader(myTask.Stream);
// Perform the read
DigitalWaveform data = reader.ReadWaveform(100);
```

The following example demonstrates how to perform a digital waveform read on a task with multiple channels:

VB.NET

```text
' Given a Task instance "myTask", 
' Create the reader and attach it to the stream 
Dim reader as DigitalMultiChannelReader = New DigitalMultiChannelReader(myTask.Stream)
' Perform the read 
Dim data as DigitalWaveform() = reader.ReadWaveform(100)
```

C#

```text
// Given a Task instance "myTask", 
// Create the reader and attach it to the stream
DigitalMultiChannelReader reader = new DigitalMultiChannelReader(myTask.Stream);
// Perform the read
DigitalWaveform[] data = reader.ReadWaveform(100);
```

Parent topic:

Digital Waveform Reads and Writes with the NI-DAQmx .NET Class Library

Related information:

- DigitalSingleChannelReader.ReadWaveform Method
- DigitalMultiChannelReader.ReadWaveform Method
- DigitalWaveform Class
- WaveformTiming Class
- Waveform Timing Limitations

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxdigitalwaveformwrites.html language=enus -->
## TOPIC 00016: Digital Waveform Writes

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxdigitalwaveformwrites.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxdigitalwaveformwrites.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: To perform a digital waveform write, call the DigitalSingleChannelWriter.WriteWaveform or DigitalMultiChannelWriter.WriteWaveform method with one DigitalWaveform or an array of DigitalWaveform objects, respectively, for each channel. When performing a write, NI-DAQmx ignores timing information and e

Digital Waveform Writes

To perform a digital waveform write, call the 
 DigitalSingleChannelWriter.WriteWaveform or 
 DigitalMultiChannelWriter.WriteWaveform method with one DigitalWaveform or an array of DigitalWaveform objects, respectively, for each channel.

When performing a write, NI-DAQmx ignores timing information and extended properties set on the DigitalWaveform; to configure timing, you must use the ConfigureSampleClock method instead.

The following example demonstrates how to perform a digital waveform write on a task with a single channel:

VB.NET

```text
' Given a Task instance "myTask", 
' Initialize the data 
Dim data As DigitalWaveform = New DigitalWaveform(100, 8)
' Create the writer and attach it to the stream 
Dim writer As DigitalSingleChannelWriter = New DigitalSingleChannelWriter(myTask.Stream)
' Perform the write
writer.WriteWaveform(True, data)
```

C#

```text
// Given a Task instance "myTask", 
// Initialize the data
DigitalWaveform data = new DigitalWaveform(100, 8);
// Create the reader and attach it to the stream
DigitalSingleChannelWriter writer = new DigitalSingleChannelWriter(myTask.Stream);
// Perform the write
writer.WriteWaveform(true, data);
```

The following example demonstrates how to perform a digital waveform write on a task with multiple channels:

VB.NET

```text
' Given a Task instance "myTask", 
' Initialize the data 
Dim data(2) As DigitalWaveform
data(0) = New DigitalWaveform(100, 8)
data(1) = New DigitalWaveform(100, 8)
' Create the writer and attach it to the stream 
Dim writer As DigitalMultiChannelWriter = New DigitalMultiChannelWriter(myTask.Stream)
' Perform the write
writer.WriteWaveform(True, data)
```

C#

```text
// Given a Task instance "myTask", 
// Initialize the data
DigitalWaveform[] data = new DigitalWaveform[2];
data[0] = new DigitalWaveform(100, 8);
data[1] = new DigitalWaveform(100, 8);
// Create the reader and attach it to the stream
DigitalMultiChannelWriter writer = new DigitalMultiChannelWriter(myTask.Stream);
// Perform the write
writer.WriteWaveform(true, data);
```

Parent topic:

Digital Waveform Reads and Writes with the NI-DAQmx .NET Class Library

Related information:

- DigitalSingleChannelWriter.WriteWaveform Method
- DigitalMultiChannelWriter.WriteWaveform Method
- DigitalWaveform Class
- ConfigureSampleClock Method

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxerrorcodes.html language=enus -->
## TOPIC 00017: NI-DAQmx Driver Error Codes

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxerrorcodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxerrorcodes.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: Error Code Description Error -209886 Setting the specified property does not allow multiple task configuration of the sample clock. Error -209885 A property is set to a value that is not supported by multiple task configuration of the sample clock. Error -209884 A common sample rate for all specifie

NI-DAQmx Driver Error Codes

| Error Code | Description |
| --- | --- |
| Error -209886 | Setting the specified property does not allow multiple task configuration of the sample clock. |
| Error -209885 | A property is set to a value that is not supported by multiple task configuration of the sample clock. |
| Error -209884 | A common sample rate for all specified tasks could not be found. If your application contains both fast- and slow-sampled devices, consider enabling allow repeated samples. |
| Error -209883 | A common sample rate for all specified tasks could not be found. |
| Error -209882 | The task contains multiple devices or chassis. Multiple task configuration only supports tasks with a single device or chassis. |
| Error -209881 | The task does not support configuring its sample clock rate via multiple task configuration. |
| Error -209880 | Specified operation cannot be performed because the debug session's target task may have a registered timing source. The debug session does not support debugging tasks with registered timing sources. |
| Error -209879 | Specified operation cannot be performed because the debug session's target task has logging enabled. The debug session does not support debugging tasks with logging enabled. Turn off logging for the target task and try again. |
| Error -209878 | Specified operation cannot be performed because the debug session's target task has registered events. The debug session does not support debugging tasks with registered events. Unregister the events for the target task and try again. |
| Error -209877 | Specified operation cannot be performed because the debug session's target task is invalid or does not exist. |
| Error -209876 | Requested function is not supported by the device. |
| Error -209875 | Multiple tasks were found that match the debug session target settings.The debug session does not support debugging more than one task at a time. Change the target settings to match a specific task and try again. |
| Error -209874 | A task was not found that matches the debug session target settings. |
| Error -209873 | Specified operation cannot be performed because it is not supported in a debug session. |
| Error -209872 | Specified operation cannot be performed because it is not permitted in monitor mode.Make sure the debug session is in control mode before requesting this operation. |
| Error -209871 | Attempt to get property failed because your device contains multiple banks, and the property has different values for different banks. Get this property one bank at a time by changing the active device name to specify each individual bank. |
| Error -209870 | Timing source creation has failed because another timing source has already been registered for this task. |
| Error -209869 | Requested value is not a supported value for this hardware revision. However, it may be supported on later revisions. Visit ni.com/info, and enter the info code "fielddaqfilter" for additional information. |
| Error -209868 | To set the sensor power supply voltage level, you must specify the sensor power configuration. |
| Error -209867 | To enable the sensor power supply, you must specify the sensor power voltage level. |
| Error -209866 | The hardware cannot acquire data from the configured scanlist. Please enter the info code that follows at ni.com/info for additional information. |
| Error -209865 | All internal routes have been reserved. If you are using time-based synchronization, please refer to info code "TimeTriggerLimits" at ni.com/info for additional information. |
| Error -209864 | The requested Reset Delay cannot be set based on your task configuration. If you are using C Series modules from different chassis in the same task, it is possible that the sample rate and module types cannot be synchronized effectively. |
| Error -209863 | Exceeded total number of time triggers available. Try disabling time triggers that are enabled on one or more DAQ tasks in your system. If no more time triggers can be disabled, try disabling other features that require internal routing resources. Please refer to info code "TimeTriggerLimits" at ni.com/info for more information. |
| Error -209862 | Exceeded total number of timestamps available. Try disabling timestamps that are user-defined or enabled by default on one or more DAQ tasks in your system. |
| Error -209861 | One or more devices in your task are not running the IEEE 802.1AS or IEEE 1588 synchronization protocol. Use the NI-Sync LabVIEW API to enable 802.1AS or 1588. Refer to the NI-Sync help or LabVIEW examples for more information. |
| Error -209860 | One or more devices could not be added to your task because they have existing coherency requirements that conflict with the new requirements of your current task. Stop the task(s) that use devices in this task and try running it again. |
| Error -209859 | The devices in your task must be synchronized to one another using the IEEE 802.1AS or IEEE 1588 synchronization protocol. Connect the devices, either directly or via an 802.1AS or 1588-capable switch. |
| Error -209858 | FieldDAQ bank name specified is invalid. FieldDAQ bank names are of the form <FieldDAQ name>-Bank<Bank number>. For example, FieldDAQ1-Bank1. |
| Error -209857 | Task contains physical channels on one or more devices that do not support the DAQmx hardware-timed single-point sample mode. |
| Error -209856 | Bank type in the source storage does not match the bank type in the destination. |
| Error -209855 | FieldDAQ device does not support the specified number of banks. The bank number specified may be too large. Change the bank number to be a valid bank number. |
| Error -209854 | The simulated FieldDAQ bank is not supported on this simulated FieldDAQ. |
| Error -209853 | The IsSimulated flags for FieldDAQ and banks must match. Change the IsSimulated flags in the import file so that they match. |
| Error -209852 | The specified device is no longer supported within the NI-DAQmx API. |
| Error -209851 | The requested Sample Timing Engine does not support Use Only Onboard Memory. |
| Error -209850 | Task name specified conflicts with an existing task name in another project. |
| Error -209849 | A time Arm Start Trigger and time Start Trigger are configured. Ensure the Arm Start Trigger comes first. |
| Error -209848 | The time trigger cannot be configured because your device has lost synchronization lock to the grand master. |
| Error -209847 | Specified value is not supported for this property. Supported values are -1 (infinite window) or non-negative numbers up to 15.768000e9. |
| Error -209846 | The property cannot be queried before or during a data acquisition. You must explicitly commit, run, and stop your task before attempting to read this property. |
| Error -209845 | The Sample Clock Timebase property you have requested is not supported by this task because it contains a reference clock device. Use the Reference Clock properties instead. |
| Error -209844 | Attempted to query a timestamp before it is available. Use the DAQmx Wait for Valid Timestamp VI/function to wait until the desired timestamp is available. |
| Error -209843 | Time operations are not supported by this device or task type. |
| Error -209842 | Timestamp requested is not enabled for this task. |
| Error -209841 | A time sync pulse and time start trigger are configured. Ensure the sync pulse comes first and the difference between them is larger than the task sync time. |
| Error -209840 | The configured time trigger is in the past. |
| Error -209839 | A time trigger configured is too far in the future. Use I/O Device Timescale instead of Host Timescale, configure the trigger at a point in the future closer to the trigger time, or schedule the trigger closer in time to the current Host Timescale time. |
| Error -209838 | Synchronization lock was lost during operation. If the occasional loss of synchronization is acceptable, change the Synchronization Unlock Behavior property to ignore sync loss. Otherwise, go to ni.com for more information about sync loss management. |
| Error -209837 | The timescales for time start trigger and time sync pulse must be the same. |
| Error -209836 | The devices in your task cannot be synchronized. This may be because there are no available synchronization mechanisms between the devices. Some synchronization paths are not available in interactive tools like the DAQ Assistant. To determine whether synchronization between these devices is possible, try deploying and executing your task in your application environment. |
| Error -209835 | The specified property requires all associated channels to use the same range as specified by the Maximum and Minimum properties. Try setting the same Maximum and Minimum Values on each channel or change the conflicting property. |
| Error -209834 | Sample rate exceeds the maximum sample rate for the number of channels and property values specified. Reduce the sample rate or number of channels. Changing the specified property values may also increase the maximum possible sample rate. |
| Error -209833 | DAQmx Wait for Valid Timestamp is not supported by one or more devices in this task. |
| Error -209832 | Specified Trigger Window has elapsed without a trigger being detected. |
| Error -209831 | Not all devices in the task support the specified Trigger configuration. |
| Error -209830 | Not all devices in the task support the specified Data Transfer Mechanism. |
| Error -209829 | Onboard device memory overflow. Because of system and/or bus-bandwidth limitations, the driver could not read data from the device fast enough to keep up with the data transfer throughput. Reduce the maximum data transfer rate of the device. You can also increase bandwidth by reducing the number of programs your computer is executing. |
| Error -209828 | All channels used for the analog trigger source must be on the same device. Remove trigger configurations from the task until all of the sources are channels from the same device. |
| Error -209827 | The device does not support using more than one trigger type at a time with the specified task configuration. Configure the device to use only one trigger type or to use a configuration that supports using multiple trigger types. |
| Error -209826 | Multiple source triggering requires the same number of values for all user-specified trigger configurations. |
| Error -209825 | The specified AO DAC range must be consistent with all reserved tasks on this device. Ensure that all reserved tasks on this device use the same value for the AO.DAC.Ref.Val channel attribute/property. |
| Error -209824 | The waveforms passed to DAQmx Write claim to be sampled at inconsistent rates. Check to make sure the data is sampled at the correct rate and either re-sample the data or correct the dt element of the waveforms. |
| Error -209823 | The function called is no longer supported by DAQmx. |
| Error -209822 | Negative duration values other than -1 are not supported. -1 indicates to read all samples. |
| Error -209821 | No samples were acquired within the specified duration. Increase the duration or sample rate so that at least one sample is acquired. |
| Error -209820 | The specified duration is too long. Specify a shorter duration. |
| Error -209819 | Duration-based reads are supported only in sample clock timing mode. |
| Error -209818 | The selected LED state is invalid. |
| Error -209817 | A device in your watchdog task does not support different output state types. Set all channels to the same output state type or remove the channels from the task. |
| Error -209816 | Self-test of the device has failed because the measured power supply voltage is outside of tolerance. Please contact National Instruments technical support. |
| Error -209815 | DAQmx Write does not support multiple samples in Hardware-Timed Single-Point tasks. Specify a single sample. |
| Error -209814 | You cannot use onboard regeneration for a task with this many channels. Reduce the number of channels in the task, use fewer modules with more the 16-bits of precision, or set the AO.UseOnlyOnBrdMem attribute/property to false. |
| Error -209813 | To create watchdog task on this device, you must specify expiration states for all lines. Specify states for the missing channels. |
| Error -209812 | The selected shunt source option for the shunt calibration is not valid for this device. |
| Error -209811 | The selected shunt select option for the shunt calibration is not valid for this device. |
| Error -209810 | This device does not support shunt calibration for the requested configuration of shunt select and shunt source. Refer to the shunt calibration documentation for your application development environment for more information. |
| Error -209809 | The selected channels do not support buffered operations when alone in a task. Add an additional channel which supports buffered operations to the task or reconfigure the task to use On-Demand timing. |
| Error -209808 | The specified feature is not supported on the attached accessory. Refer to your accessory documentation for accessories that support the requested feature. |
| Error -209807 | The threshold voltage value must be consistent when using the same terminal with RSE terminal configuration as a source for multiple inputs. For example, do not set 2.0 V on PFI0 for one input, and 3.0 V on PFI0 for another input. |
| Error -209806 | NI-DAQmx is not installed on the target system, is incompatible, or the installation is corrupt. Install or repair the driver software. |
| Error -209804 | Your device has lost synchronization lock to the grand master. Any timestamp values for the task may be invalid, but the task was not stopped because the SyncUnlockBehavior property is set to "Ignore Lost Sync Lock." To query the status of your device, read either the ReadSyncUnlockedChansExist or WriteSyncUnlockedChansExist property. |
| Error -209803 | The Onboard Memory Empty value of the AO.DataXferReqCond attribute/property is not supported on this device. The value of this attribute/property is coerced to a different value after Output.BufSize is set. You can emulate the behavior of the Onboard Memory Empty value by setting Output.BufSize to a lower value. The minimum value for this attribute/property is 2. |
| Error -209802 | DAQmx Wait for Next Sample Clock detected one or more missed sample clocks since the last call to Wait for Next Sample Clock which indicates that your program is not keeping up with the sample clock. To remove this warning, slow down the sample clock, or else change your application so that it can keep up with the sample clock. |
| Error -209801 | DAQmx Write did not complete before the arrival of the next sample clock which indicates that your program is not keeping up with the hardware clock. To remove this warning, slow down the hardware clock, or else change your application so that it can keep up with the hardware clock. |
| Error -209800 | DAQmx Read did not complete before the arrival of the next sample clock or change detection event, which indicates that your program is not keeping up with the hardware clock or the external change event. For tasks using sample clock timing, slow down the hardware clock or else change your application so that it can keep up with the hardware clock. For tasks using change detection timing, decrease the frequency of your event or else change your application so that it can keep up with the change event. |
| Error -201510 | The digital filtering properties must be consistent when using the same terminal as a source for multiple inputs. For example, digital filtering can either be enabled with the same minimum pulse width configuration whenever PFI0 is used, or disabled for all cases. |
| Error -201509 | The logic level behavior must be consistent when using the same terminal as a source for multiple inputs. For example, do not enable the pull-up on PFI0 for one input, and set it to none on PFI0 for another input. |
| Error -201508 | The terminal configuration must be consistent when using the same terminal as a source for multiple inputs. For example, do not set PFI0 to differential for one input, and PFI0 to RSE for another input. |
| Error -201507 | A fatal hardware clocking error has occurred. The device is unusable until you restart it. If the problem persists, please contact National Instruments Technical Support. |
| Error -201506 | A hardware clocking error has occurred. Try the operation again. If the problem persists, please contact National Instruments Technical Support. |
| Error -201505 | The chassis requires at least one DAQ device directly cabled to it. Edit the chassis and assign a device. |
| Error -201504 | A fatal hardware clocking error has occurred. The device is unusable until you restart it. If you are using an external reference clock, make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -201503 | The AI timing engine cannot be used for counter tasks. You can select a different timing engine or let the driver automatically select one. |
| Error -200078 | Using USB DAQ devices on Windows XP might result in corrupt data or other errors. Visit ni.com/info and enter info code "WindowsXPUSBHotfix" to obtain a patch. |
| Error -200077 | The NI PXIe-5611 is not configured properly and needs to be associated with an AWG and LO. Right-click on the NI PXIe-5611 and select 'Configure' to associate the AWG and LO. For more information, refer to NI-RFSG documentation, RF Signal Generators Getting Started Guide. |
| Error -200076 | The NI PXIe-5611 is not configured and needs to be associated with an AWG and LO. Right-click on the NI PXIe-5611 and select 'Configure' to associate the AWG and LO. For more information, refer to NI-RFSG documentation, RF Signal Generators Getting Started Guide. |
| Error -200075 | The NI PXI-5610 is not configured properly and needs to be associated with an AWG. Right-click on the NI PXI-5610 and select 'Configure' to associate the AWG. For more information, refer to NI-RFSG documentation, RF Signal Generators Getting Started Guide. |
| Error -200074 | The NI PXI-5610 is not configured and needs to be associated with an AWG. Right-click on the NI PXI-5610 and select 'Configure' to associate the AWG. For more information, refer to NI-RFSG documentation, RF Signal Generators Getting Started Guide. |
| Error -200073 | The NI PXI-5665 is not configured properly. Right-click on the NI PXIe-5606 and select 'Configure' to associate the digitizer and LO. |
| Error -200072 | The NI PXIe-5606 is not associated with a digitizer or an LO. Right-click on the NI PXIe-5606 and select 'Configure' to associate the digitizer and LO. |
| Error -200071 | The NI PXIe-5667 (7 GHz) is not configured properly. Right-click on the NI PXIe-5605 and select 'Configure' to associate the digitizer and LO. You can also associate the NI PXIe-5605 with additional IF conditioning and RF conditioning modules. |
| Error -200070 | The NI PXI-5665 (14 GHz) is not configured properly. Right-click on the NI PXIe-5605 and select 'Configure' to associate the digitizer and LO. You can also associate the NI PXIe-5605 with additional IF conditioning and RF conditioning modules. |
| Error -200069 | The NI PXIe-5605 is not associated with a digitizer or an LO. Right-click on the NI PXIe-5605 and select 'Configure' to associate the digitizer and LO. You can also associate the NI PXIe-5605 with additional IF conditioning and RF conditioning modules. |
| Error -200068 | The NI PXIe-5667 (3.6 GHz) is not configured properly. Right-click on the NI PXIe-5603 and select 'Configure' to associate the digitizer and LO. You can also associate the NI PXIe-5603 with additional IF conditioning and RF conditioning modules. |
| Error -200067 | The NI PXIe-5665 (3.6 GHz) is not configured properly. Right-click on the NI PXIe-5603 and select 'Configure' to associate the digitizer and LO. You can also associate the NI PXIe-5603 with additional IF conditioning and RF conditioning modules. |
| Error -200066 | The NI PXIe-5603 is not associated with a digitizer or an LO. Right-click on the NI PXIe-5603 and select 'Configure' to associate the digitizer and LO. You can also associate the NI PXIe-5603 with additional IF conditioning and RF conditioning modules. |
| Error -200065 | The NI PXIe-5663E is not configured properly. Right-click on the NI PXIe-5601 and select 'Configure' to associate the digitizer and LO. |
| Error -200064 | The NI PXIe-5663 is not configured properly. Right-click on the NI PXIe-5601 and select 'Configure' to associate the digitizer and LO. |
| Error -200063 | The NI PXIe-5601 is not associated with a digitizer or an LO. Right-click on the NI PXIe-5601 and select 'Configure' to associate the digitizer and LO. |
| Error -200062 | The NI PXI-5661 is not configured properly. Right-click on the NI PXI-5600 and select 'Configure' to associate the digitizer. |
| Error -200061 | The NI PXI-5600 is not associated with a digitizer. Right-click on the NI PXI-5600 and select 'Configure' to associate the digitizer. |
| Error -200060 | The same data is being read repetitively. |
| Error -200059 | The selected ports are not connected, so there is nothing to disconnect. |
| Error -200058 | The connection count stored on the EEPROM is invalid. Write a value to Accessory Connection Count to fix the problem. Contact National Instruments if the problem persists. |
| Error -200057 | The network device already exists in the system. |
| Error -200056 | The connection count of the attached accessory has exceeded the recommended limit. Contact National Instruments if the accessory appears to be functioning improperly. |
| Error -200055 | Power-up state section of the device EEPROM appears to be corrupt. Reconfigure the digital power-up states and perform a self-calibration. |
| Error -200054 | EEPROM of the device appears to be corrupt. Contact National Instruments if the device appears to be functioning improperly. |
| Error -200053 | Sample Rate specified may exceed device capabilities for some devices in the task. Specify a slower sample rate, decrease the number of channels, or use a separate task for some of the devices in the task. |
| Error -200052 | Buffer size specified is not evenly divisible by 8 times the sector size. For optimal performance, use a buffer size that is a multiple of 8 times the sector size. Refer to the NI-DAQmx Help for more information. |
| Error -200051 | Input voltage limits exceeded. Protection circuity disabled the inputs, however proper voltage levels are now present, and the error state has been cleared. |
| Error -200050 | Output generation aborted by the reverse power protection circuitry of the device. Either the output signal exceeded the output power limit, or power was driven back into the output of the device by an external source. Error state has been cleared. |
| Error -200049 | Calibration changed the gain calibration constants only and not the offset calibration constants because the necessary offset calibration data was not available. This device needs a reference signal of 0.0 Volts at gains of 1, 15, 20, and 310 in order to perform an offset calibration. |
| Error -200048 | Requested property value exceeds device specification limits. Device performance is not guaranteed. Use values within device specifications, or set the Allow Out of Specification User Settings property to true. |
| Error -200047 | Self-calibration section of the EEPROM on the device appears to be corrupt. Perform a self-calibration on the device. |
| Error -200046 | External calibration section of the EEPROM on the device appears to be corrupt. Perform an external calibration on the device. |
| Error -200045 | EEPROM of the device appears to be corrupt. Contact National Instruments if the device appears to be functioning improperly. |
| Error -200044 | Invalid enumeration value was encountered during export. The exported file will require modification in order to successfully import. |
| Error -200043 | Date specified by the Channel Calibration Expiration Date property has expired. The channel calibration is applied in spite of this because the Apply Calibration if Expired property was set to true. To eliminate this warning, update the channel calibration, including the Expiration Date. |
| Error -200042 | Calibration constants stored in the EEPROM produced an invalid value for one or more analog output channels. The device will continue to function, but the accuracy of the generated signals may be compromised. An incorrect calibration might have been performed, or the calibration data in the EEPROM might have been corrupted. Perform an external calibration, perform a self-calibration, or contact National Instruments Technical Support. |
| Error -200041 | Calibration constants stored in EEPROM produced an invalid value for one or more analog input channels. The device will continue to function, but the accuracy of the measurements may be compromised. An incorrect calibration might have been performed, or the calibration data in the EEPROM might have been corrupted. Perform an external calibration, perform a self-calibration, or contact National Instruments Technical Support. |
| Error -200040 | Sample clock rate specified is so high that it violates the settling time requirements for the generation. Reduce the sample clock rate, or the accuracy of the generated signal might be compromised. |
| Error -200039 | Data may be invalid because the settling time of the enabled filter exceeds the period between two conversions on the analog-to-digital converter (ADC) for a task with more than one channel. Disable the filter by setting AI Lowpass Enable to false, acquire data from only one channel in the task, or increase the time between two ADC conversions by reducing the Sample Clock Rate, the Sample Clock Delay, and/or the number of channels in the task. |
| Error -200038 | Data may be invalid because the settling time of the enabled filter exceeds the period between two conversions on the analog-to-digital converter (ADC) for a task with more than one channel. Disable the filter by setting AI Lowpass Enable to false, increase the time between two ADC conversions by reducing the AI Convert Rate, or acquire data from only one channel in the task. |
| Error -200037 | Settings requested through a previous DAQmx Write were overwritten before they could be applied. This occurred either because DAQmx Write was invoked more than once between two consecutive sample clocks or because the frequency of the generated pulse train is lower than the sample clock rate (it takes more than one sample clock period to generate one period of the pulse train). The settings requested by the most recent DAQmx Write will be applied on the next sample clock. To avoid this warning, make sure that DAQmx Write is invoked exactly once between two consecutive sample clocks and that the frequency of the generated pulse train is higher than the sample clock rate. |
| Error -200036 | Requested Sample Clock Rate is higher than the maximum supported per device specifications. Reduce the Sample Clock Rate or use a device which supports the requested Sample Clock Rate. |
| Error -200035 | Clock rate specified is less than the minimum conversion rate of the ADC. Your data may be invalid. |
| Error -200034 | A sensor on the device detected a temperature approaching the device's maximum recommended operating temperature. The device will shut down if its temperature exceeds the maximum recommended operating temperature. To avoid the shutdown, ensure the device temperature does not get above the maximum recommended operating temperature. You can often prevent the shutdown by periodically cleaning fan filters. Refer to user documentation for more information. |
| Error -200033 | DAQmx Write was invoked more than once between two consecutive sample clocks. Only the last DAQmx Write took effect. To eliminate this warning, invoke DAQmx Write only once between two consecutive sample clocks. |
| Error -200032 | Output gain was coerced to the nearest acceptable value, because the original value was too high given the RF Frequency. |
| Error -200031 | Output gain was coerced to the nearest acceptable value, because the original value was too low given the RF Frequency. |
| Error -200030 | A sensor on the device detected a temperature approaching the device's maximum recommended operating temperature. The device will shut down if its temperature exceeds the maximum recommended operating temperature. To avoid the shutdown, ensure the device temperature does not get above the maximum recommended operating temperature. You can often prevent the shutdown by periodically cleaning fan filters. Refer to user documentation for more information. |
| Error -200029 | RIS acquisition was completed, but some of the bins were not filled with a sufficient number of samples to perform the requested RIS averaging. Data for those bins was computed from the available samples. Consider increasing the timeout for the operation. Refer to documentation for details about RIS acquisitions. |
| Error -200028 | Some of the last samples acquired during the finite DMA acquisition are possibly invalid due to counter limitations. Get the Number of Possibly Invalid Samples property to see how many samples might be invalid. Use continuous sample mode for DMA acquisitions with this type of counter. |
| Error -200027 | Sample clock rate has been coerced to the minimum supported value because the specified value was too low. For lower sample clock rates, use an external sample clock or an external sample clock timebase. |
| Error -200026 | Requested string could not fit into the given buffer. Only the first part of the string was copied into the buffer. To allow for the terminating NULL character, the number of characters copied into the buffer is equal to the size of the buffer minus one. Call the function twice. Call the function initially to determine the string size. Use the second function call to get the full string value. In the first function call, pass NULL for the buffer and zero for the buffer size. The positive return value of the function is the string size (which includes the terminating NULL). Use this value to allocate a buffer of sufficient size, then use this buffer in the second function call. |
| Error -200025 | User-defined information to be stored in the EEPROM is too long. Only the leading portion was saved. Refer to documentation for information about the maximum length allowed for user-defined information. |
| Error -200024 | One of more of the properties saved with a later version of NI-DAQ are not supported by the installed version of NI-DAQ and are ignored. Upgrade the installed version of NI-DAQ to a version compatible with the version used when saving the properties to take advantage of all the saved properties. |
| Error -200022 | Attempted writing a sample value that was too small. The driver automatically coerced it to the minimum supported value. |
| Error -200021 | Attempted writing a sample value that was too large. The driver automatically coerced it to the maximum supported value. |
| Error -200020 | Requested number of pretrigger samples per channel could not be configured, so it was coerced to the minimum supported value. |
| Error -200019 | Requested read offset could not be configured, so the offset was coerced to the minimum supported value. |
| Error -200018 | Specified convert rate is too low to be generated using the onboard AI convert clock with the given timebase. The rate was coerced to the slowest possible convert rate. For slower rates, you must use an external convert clock or an external convert clock timebase. |
| Error -200017 | Specified sample rate is lower than the lowest rate that can be generated using the onboard clock. The rate was coerced to the slowest possible sample rate. For slower rates, use an external sample clock or an external sample clock timebase. |
| Error -200016 | An attempt has been made to query the date/time of the last self calibration of a device that has never been self-calibrated using the NI-DAQmx API, so the date/time is invalid. Self-calibrate the board using the NI-DAQmx API. |
| Error -200015 | While writing to the buffer during a regeneration, the actual data generated might have alternated between old data and new data. That is, while the driver was replacing the old pattern in the buffer with the new pattern, the device might have generated a portion of new data, then a portion of old data, and then a portion of new data again. Reduce the sample rate, use a larger buffer, or refer to documentation about DAQmx Write for information about other ways to avoid this warning. |
| Error -200014 | The combination of sample rate and buffer size settings could result in a large number of interrupts, causing the system to hang. Decrease your sample rate, or increase your buffer size. For acquisitions without a reference trigger, you can disallow buffer overwrites. For generations, you can disable the regeneration of old samples. |
| Error -200013 | User-defined information string entered exceeds the maximum allowable string length. The string will be truncated to its maximum allowable length. |
| Error -200012 | Clock rate specified exceeds the maximum conversion rate of the ADC. ADC overrun errors are likely. |
| Error -200011 | Clock rate specified is so high that it violates the settling time requirements for the acquisition. Reduce the clock rate, or the accuracy of the measurement might be compromised. |
| Error -200010 | Finite acquisition or generation has been stopped before the requested number of samples were acquired or generated. |
| Error -200009 | Counter 1 DMA acquisition started while starting, committing, stopping, or uncommitting an analog output (AO) task. This could cause the counter acquisition to stop. If possible, use counter 0 instead of counter 1. Otherwise, start/commit the AO task before starting the counter 1 DMA acquisition, and stop/uncommit the AO task after stopping the counter 1 DMA acquisition. |
| Error -200008 | Counter 0 DMA acquisition started while starting, committing, stopping, or uncommitting an analog input (AI) task. This could cause the counter acquisition to stop. If possible, use counter 1 instead of counter 0. Otherwise, start/commit the AI task before starting the counter 0 DMA acquisition, and stop/uncommit the AI task after stopping the counter 0 DMA acquisition. |
| Error -200007 | PLL was unlocked. Your data might be invalid. |
| Error -200005 | ADC for one or more channels was overloaded. Your data might be invalid. |
| Error -200004 | Input termination resistor for one or more channels was overloaded. Your data might be invalid. |
| Error -200003 | Absolute timestamp counter has rolled over. |
| Error -200003 | Channel cannot be used more than once inside a list of channels. If you need to use the same physical channel more than once inside your list of channels, refer to that physical channel under different names. |
| Error -200004 | Data requested has been overwritten in the device memory. |
| Error -200005 | Data requested has not been acquired yet. |
| Error -200006 | Record requested has been overwritten in the device memory. |
| Error -200007 | Record requested has not been acquired yet . |
| Error -200008 | Stop trigger has not occurred yet. |
| Error -200009 | Timestamps have been overwritten. You can no longer read any data. |
| Error -200010 | Onboard device memory overflow. Because of system and/or bus-bandwidth limitations, the driver could not read data from the device fast enough to keep up with the device throughput. Reduce your sample rate. If your data transfer method is interrupts, try using DMA or USB Bulk. You can also use a product with more onboard memory or reduce the number of programs your computer is executing concurrently. |
| Error -200011 | Task cannot contain both input and output channels. Either use channels of one direction in a task or make two separate tasks. |
| Error -200012 | Specified physical channel does not support digital output. Change the direction of the task, use another terminal, or use another device. |
| Error -200014 | Terminal cannot appear multiple times within a single digital input or output task. |
| Error -200015 | Communication with SCXI failed. The communication cable to the SCXI hardware might have been disconnected or exposed to excessive noise. |
| Error -200016 | Onboard device memory underflow. Because of system and/or bus-bandwidth limitations, the driver could not write data to the device fast enough to keep up with the device output rate. Reduce your sample rate. If your data transfer method is interrupts, try using DMA or USB Bulk. You can also use a product with more onboard memory or reduce the number of programs your computer is executing concurrently. |
| Error -200017 | Onboard device memory underflow. Not enough new data has been sampled since the last read or the start of the measurement. Increase the sample rate, increase the timeout value, or decrease the number of samples to read. |
| Error -200018 | DAC conversion attempted before data to be converted was available. Decrease the output frequency to increase the period between DAC conversions, or reduce the size of your output buffer in order to write data more often. If you are using an external clock, check your signal for the presence of noise or glitches. |
| Error -200019 | ADC conversion attempted before the prior conversion was complete. Increase the period between ADC conversions. If you are using an external clock, check your signal for the presence of noise or glitches. |
| Error -200020 | Self-test of the device has failed. |
| Error -200022 | Resource requested by this task has already been reserved by a different task. |
| Error -200023 | Script contains an invalid character or symbol. Replace the invalid character with a valid symbol or alphanumeric character. |
| Error -200024 | Valid identifier expected but not found in script. The identifier should specify a valid waveform or script name. Identifiers cannot start with a number. |
| Error -200025 | Script name was expected, but not found in the script. |
| Error -200026 | Waveform name was expected, but not found in the script. |
| Error -200027 | Keyword was expected, but not found in the script. |
| Error -200028 | Waveform referenced in the script was not found in onboard memory. Write the waveform to the device before writing the script. |
| Error -200029 | Marker specified in a generate instruction exceeds the waveform boundaries. Change the marker position or positions to fit within the waveform, or increase the size of the waveform. |
| Error -200030 | Subset specified in a generate instruction exceeds the waveform boundaries. Change the subset start offset and/or subset length so the subset fits within the waveform, or increase the size of the waveform. |
| Error -200031 | Marker position specified is not a multiple of alignment quantum. |
| Error -200032 | Subset length specified is not valid. Change the subset length to be longer than zero samples and a multiple of the alignment quantum. |
| Error -200033 | Start offset of the subset is not a multiple of the alignment quantum. |
| Error -200034 | Marker position exceeds the length of the subset. |
| Error -200035 | Repeat loop is contained within too many levels of nested repeat loops. Unroll one of the "repeat" loops if possible, or change the script and run it several times. To unroll a loop, remove the "repeat" and "end repeat" instructions and explicitly replicate the instructions of the removed loop the desired number of times. |
| Error -200036 | Number of iterations specified for a finite "repeat" loop is invalid. |
| Error -200037 | "Clear trigger" instruction cannot be the last instruction of a "repeat" loop. |
| Error -200038 | "Wait" instruction cannot be the last instruction of a "repeat until" loop. |
| Error -200039 | Routing information associated with your device cannot be found. |
| Error -200040 | Source terminal to be routed could not be found on the device. Make sure the terminal name is valid for the specified device. Refer to Measurement & Automation Explorer for valid terminal names. |
| Error -200041 | Destination terminal to be routed could not be found on the device. Make sure the terminal name is valid for the specified device. Refer to Measurement & Automation Explorer or your hardware documentation for valid terminal names. |
| Error -200042 | Inversion requested is not possible. Either the hardware between the source and destination terminals does not support the inversion, or other routes in the task might be interfering with this route. |
| Error -200043 | Hardware necessary for this route is in use by another task or tasks. |
| Error -200044 | Route cannot be made between the source and destination terminals. Either the hardware does not support this route or other routes might be interfering with this route. |
| Error -200045 | Device was removed or powered down between task verification and reservation. Ensure that the device is not being reset. |
| Error -200046 | Invalid identifier at the end of the switch action. A connection separator, sequence separator, or valid switch action terminator must follow a switch action. |
| Error -200047 | Invalid identifier after the device identifier in the list entry. |
| Error -200048 | Invalid trigger line in the "<sac>" or "<wfa>" statement in the list entry. Refer to the documentation for valid trigger lines. |
| Error -200049 | Invalid value in the "<repeat>" statement in the list entry. The syntax for a repeat statement is "<repeat integer>". Refer to the documentation for valid integer values. |
| Error -200050 | Invalid channel name in the list entry. Refer to the documentation for valid channel names for the device in use. |
| Error -200051 | Invalid identifier after a separator in the list entry. |
| Error -200052 | Invalid identifier instead of an expected connection operator, "->", in the list entry. Refer to the documentation for proper syntax for connections involving channel ranges. |
| Error -200053 | Channels in switch actions cannot span different devices. |
| Error -200054 | Semicolon or a semicolon modifier must follow a connection range statement. Refer to the documentation for information on connection ranges and semicolon modifiers. |
| Error -200055 | Device identifier not specified in the list entry. |
| Error -200056 | Channel name not specified in the list entry. |
| Error -200057 | Duplicate device identifier in the device list. This is not allowed when waiting for devices to settle. |
| Error -200058 | Identifier in the list entry is too long. |
| Error -200059 | List cannot end with the connection separator "&". |
| Error -200060 | Fully specified path cannot contain a connection range. |
| Error -200061 | Invalid identifier in the list entry. The connection separator "&" or sequence separator "&&" was expected. |
| Error -200062 | Invalid identifier instead of an expected connection operator "->" in the list entry. |
| Error -200063 | Invalid identifier instead of an expected terminator in the list entry. |
| Error -200064 | Unexpected connection separator "&" or sequence separator "&&" in the list entry. |
| Error -200065 | Action at the designated position in the scanlist is not valid for the device. |
| Error -200066 | Connection operator is invalid at the designated point in the list entry. |
| Error -200067 | Settling time constraints for the device could not be satisfied. Refer to the documentation for details about settling time constraints. |
| Error -200068 | Scanning is not supported by the specified device. |
| Error -200069 | Device specified is not a valid switch device. |
| Error -200070 | Advance trigger type specified is not supported by the device. |
| Error -200071 | Number of physical channels is too large. |
| Error -200072 | Duplicate channels in the list of physical channels are not supported by this device. |
| Error -200073 | SCXI module specified in the hardware configuration was not found. Make sure that the SCXI chassis is powered on, the SCXI cable is properly connected between the chassis communicator and the SCXI module, and that the cabled module specified in the hardware configuration is present in the specified slot. |
| Error -200074 | Device unable to store calibration constants. Make sure that your hardware is properly installed, and test the regular operation of the device. |
| Error -200075 | Voltage data supplied is outside of the specified range. Change the range or the data. Refer to the documentation for more information about possible ranges. |
| Error -200076 | Current data supplied is outside of the specified range. |
| Error -200077 | Requested value is not a supported value for this property. The property value may be invalid because it conflicts with another property. |
| Error -200078 | Analog input (AI) task started or committed during a counter 0 DMA acquisition. If possible, use counter 1 instead of counter 0. Otherwise, start/commit the AI task before starting the counter 0 DMA acquisition. |
| Error -200079 | Analog output (AO) task started or committed during a counter 1 DMA acquisition. If possible, use counter 0 instead of counter 1. Otherwise, commit the AO task before starting the counter 1 DMA acquisition. |
| Error -200081 | Sample rate exceeds the maximum sample rate for the number of channels specified. Reduce the sample rate or the number of channels. Increasing the convert rate or reducing the sample delay might also alleviate the problem, if you set either of them. |
| Error -200082 | Minimum is greater than or equal to the maximum. Ensure the maximum value is greater than the minimum value. If using a custom scale, ensure that the scaled maximum is greater than the scaled minimum. |
| Error -200086 | Physical channel range syntax in the input string is invalid because multiple devices were listed in the string. |
| Error -200087 | Channel is not in the task, and the channel is not a valid global channel. Make sure that the channel is in the task or that the channel is a valid global channel. If you explicitly named the virtual channel in DAQmx Create Channel, you must use the name assigned to that channel. Also, check for typing errors. |
| Error -200088 | Task specified is invalid or does not exist. |
| Error -200089 | Task name specified conflicts with an existing task name. |
| Error -200090 | Shared library was not found. This error might be the result of an inadvertent deletion of an NI-DAQmx component. Reinstall NI-DAQmx, or download the latest version of the driver from the National Instruments website at ni.com. If the error is still returned, contact NI Technical Support. |
| Error -200091 | Shared library version installed is incorrect. This error might be the result of an incorrect installation of NI-DAQmx or a related software package. Reinstall NI-DAQmx, or download the latest version of the driver from the National Instruments website at ni.com. If the error is still returned, contact NI Technical Support. |
| Error -200092 | Function supported for channel-based tasks only. |
| Error -200093 | Attempted to retrieve channel properties from a multichannel task without selecting a specific channel. Use the Active Channel property to select a specific channel from which to retrieve properties. |
| Error -200094 | Digital waveform expected as input. |
| Error -200095 | Analog waveform expected as input. |
| Error -200096 | Number of samples to read must be -1 or greater. |
| Error -200097 | Attempted to retrieve channel properties from a multichannel task with more than one channel selected. You must select an individual channel to retrieve channel properties. If you are programming with LabVIEW, use the Active Channel property to specify the individual channel. |
| Error -200098 | Number of terminals requested cannot be greater than 1. |
| Error -200099 | Physical channel not specified. |
| Error -200100 | Specified DAQmx Read only can be used to read from a single channel. Use the multichannel DAQmx Read. |
| Error -200101 | Number of channels in data to write does not match the number of channels in the task. |
| Error -200102 | Pattern width specified does not match the number of lines in the digital channel. |
| Error -200103 | Number of samples to write must be the same for every channel. |
| Error -200104 | Bracket character ("[" or "]") at the specified position in the list is invalid. Matching bracket cannot be found. Check for nested fully specified paths or incorrectly paired brackets. |
| Error -200105 | Channel is invalid for the excitation mode of the SCXI-1122. Disable multiplexed excitation, or use one of the physical channels between ai0 and ai7. |
| Error -200106 | Property must have the same value for all channels on this device. |
| Error -200107 | Module specified in the hardware configuration is not the module found. Make sure that the module specified in the hardware configuration is present in the specified slot. |
| Error -200108 | Calibration session is already open on this device. You can have only one open calibration session for each device. Use the handle obtained when the calibration session for this device was originally opened. |
| Error -200109 | Password is longer than four characters. |
| Error -200110 | Password supplied is incorrect. |
| Error -200111 | Password is required for this operation. |
| Error -200112 | Calibration handle is invalid. Open a calibration session to get a valid calibration handle. Use the valid calibration handle obtained when the calibration session was opened. |
| Error -200113 | Device temperature is outside of the required range for calibration. |
| Error -200116 | Lines on the 8255 chip for this device are configured for output. Cannot tristate these lines at this time. Read values using an input task on another port. |
| Error -200117 | Port C cannot be used for data input/output in a handshaking task. |
| Error -200118 | Port reserved for handshaking. Cannot reserve this port or any of its lines for another task at this time. |
| Error -200119 | Port is configured for static digital operations by another task. Cannot configure this port or any of its lines for handshaking at this time. |
| Error -200120 | Port is configured for input. Cannot configure this port or any of its lines for output at this time. |
| Error -200121 | Port is configured for output. Cannot configure this port or any of its lines for input at this time. |
| Error -200122 | Lines 0 through 3 of this port are configured for input. Cannot configure these lines for output at this time. |
| Error -200123 | Lines 0 through 3 of this port are configured for output. Cannot configure these lines for input at this time. |
| Error -200124 | Lines 4 to 7 of this port are configured for input. Cannot configure these lines for output at this time. |
| Error -200125 | Lines 4 through 7 of this port are configured for output. Cannot configure these lines for input at this time. |
| Error -200126 | Lines on port C cannot be used for both handshaking control and static digital operations on an 8255 chip. Handshaking tasks automatically reserve some lines on port C as control lines. These lines cannot be reserved for static digital operations when the device is configured for handshaking. There are two likely causes for this error: 1. An attempt was made to reserve the lines for static digital operations when a handshaking task was previously configured. 2. An attempt was made to create a handshaking task when the lines were previously reserved for static digital operations. Refer to the documentation for information about which lines on port C are not available when the 8255 chip is in handshaking mode. |
| Error -200127 | Port 0 or any of its lines cannot be used to create a handshaking task. Use port 1 or port 2 of the 8255 chip on this device for handshaking. |
| Error -200128 | Property must have the same value for all repeated physical channels. Set the same property value for all of the channels. |
| Error -200130 | Timebase divisor cannot be set for an external clock. You cannot divide down an externally supplied clock. If you want to divide down an external clock, specifiy an external timebase source instead and set the clock source to be internal. |
| Error -200131 | Analog trigger source must be the first channel in the acquisition or a valid analog trigger terminal. If you explicitly named the virtual channel in DAQmx Create Channel, you must use the name assigned to that channel. |
| Error -200132 | External timebase rate must be specified to translate the derived clock or timebase rate into ticks. Set the external timebase rate, or set the divisor instead of the clock or timebase rate. |
| Error -200133 | Counter timebase source, counter timebase rate, master timebase divisor, and master timebase rate settings are inconsistent with one another. The conflicting properties must satisfy the following constraint: Master Timebase Rate / Master Timebase Divisor = Counter Timebase Rate |
| Error -200134 | Counter timebase source and counter timebase rate settings are inconsistent with one another. For internal counter timebase source selections, if the counter timebase rate is set, its value must match the rate corresponding to the counter timebase source. For example, 20 MHz corresponds to a rate of 20,000,000 Hz. |
| Error -200135 | Counter timebase source and counter timebase master timebase divisor settings are inconsistent with one another. If the divisor is specified, the following must apply: Master Timebase Rate / Counter Timebase Master Timebase Divisor = Rate corresponding to Counter Timebase Source. |
| Error -200136 | Frequency and Initial Delay property values are inconsistent with one or more counter timebase properties. The conflicting properties must satisfy the following constraint: Counter Timebase Rate / Counter Maximum Count <= X <= Counter Timebase Rate / 2 where X = Frequency and 1 / Initial Delay, and where Counter Timebase Rate = Master Timebase Rate / Counter Timebase Master Timebase Divisor or is inferred from the Counter Timebase Source selection. |
| Error -200137 | Initial Delay, High Time, and Low Time property values are inconsistent with one or more counter timebase properties. The conflicting properties must satisfy the following restraint: 2 / Counter Timebase Rate <= X <= Counter Maximum Count/ Counter Timebase Rate where X = Initial Delay, High Time, and Low Time, and where Counter Timebase Rate = Master Timebase Rate / Counter Timebase Master Timebase Divisor or is inferred from the Counter Timebase Source selection. |
| Error -200138 | A timebase could not be selected that covers the entire range specified in the Maximum and Minimum properties. The conflicting properties must satisfy the following constraints: Maximum <= Counter Maximum Count / Counter Timebase Rate Minimum >= 2 / Counter Timebase Rate. |
| Error -200139 | A timebase could not be selected that covers the entire range specified in the Maximum and Minimum properties. The conflicting properties must satisfy the following constraints: Maximum <= Counter Timebase Rate / 2 Minimum >= Counter Timebase Rate / Counter Maximum Count. |
| Error -200140 | Two consecutive active edges of the input signal occurred without a counter timebase edge. Use a faster counter timebase. |
| Error -200141 | Data was overwritten before it could be read by the system. If Data Transfer Mechanism is Interrupts, try using DMA or USB Bulk. Otherwise, divide the input signal before taking the measurement. |
| Error -200142 | Internal timebase could not be found that matches the rate specified in the Counter Timebase Rate property. |
| Error -200143 | Counter timebase rate must be specified for external counter timebase sources in order for frequency and/or time calculations to be made correctly. Set the Counter Timebase Rate property to the appropriate value for your external source. |
| Error -200144 | Pause trigger is only valid for continuous pulse generations. Change the sample mode to continuous, or do not use the pause trigger. |
| Error -200145 | Pause trigger is only valid for event counting if sample clock is not used. |
| Error -200146 | Pause and start triggers cannot both be active in this task. |
| Error -200147 | There cannot be multiple counters in the same task for input operations. Use a separate task for each counter. |
| Error -200148 | FREQOUT counter cannot generate the desired frequency. The FREQOUT counter is a 4-bit counter that can divide either the master timebase rate / 2 or the master timebase rate / 200 by a number between one and 16. Choose a frequency within this range. |
| Error -200149 | External timebase rate must be specified to translate the delay into ticks. Set the external timebase rate, or set the delay in units of ticks. |
| Error -200150 | Channel is not available when the module is in parallel mode. |
| Error -200151 | Your SCXI system is not set up for performing analog input operations on given channels. The SCXI module cabled to your digitizer cannot route analog signals from other modules to the digitizer, or is not configured to route them. To perform the desired operation with multiple SCXI modules and one digitizer, cable the digitizer to one of the analog input modules. The module your channels are on is one such module. Then, update the chassis configuration in MAX to reflect cabling change, and ensure that the cabled module is in multiplexed mode. Alternatively, you can use multiple digitizers and SCXI modules in parallel mode. For detailed information about cabling, refer to documentation. |
| Error -200152 | Data read from the EEPROM on the device is invalid. Verify that any accessories configured with this device are connected. If the problem continues, contact National Instruments Technical Support. The device might need to be recalibrated or repaired by NI. |
| Error -200153 | Reference voltage applied for calibration is outside the range defined for calibration of this device. Ensure that the reference voltage falls within the range specified for this device. |
| Error -200154 | Reference current applied for calibration is outside the range defined for calibration of this device. Ensure that the reference current falls within the range specified for this device. |
| Error -200155 | Reference resistance applied for calibration is outside the range defined for calibration of this device. Ensure that the reference resistance falls within the range specified for this device. |
| Error -200156 | Reference frequency applied for calibration is outside the range defined for calibration of this device. Ensure that the reference frequency falls within the range specified for this device. |
| Error -200157 | Device could not complete the calibration operation. Calibration could fail for the following reasons: 1. The actual reference signal applied for calibration was different from the value you specified. Ensure that the reference signal applied is the same as the values that were input. 2. The reference signal was not stable over the period of time that the hardware was being calibrated. Ensure that the reference signal specified is free of noise and does not drift over the duration of the calibration. 3. The device is not functioning properly. |
| Error -200158 | Requested operation could not be performed because the necessary digital lines could not be reserved by SCXI. Another task might have reserved these lines previously. For example, E Series devices use lines 0, 1, 2, and 4 on port 0 to communicate with the SCXI module. |
| Error -200159 | Requested operation could not be performed because the digital lines are being used for communication with SCXI or a TEDS carrier. For example, E Series devices use lines 0, 1, 2, and 4 on port 0 to communicate with a SCXI module. Therefore, you cannot use lines 0, 1, 2, and 4 for regular digital I/O. |
| Error -200160 | Channel could not be created. All channels must be created before the task is verified. Before I/O can be performed or properties can be retrieved, tasks are verified. Channels must be created before these actions can occur. |
| Error -200161 | Device to which the sensor is attached does not have an available internal excitation source. Select another device with an available internal excitation source or supply external excitation. |
| Error -200162 | 2-wire resistance configuration is incompatible with voltage excitation. |
| Error -200163 | Completion resistance value, R1, cannot be zero if the circuit uses voltage excitation. |
| Error -200166 | Output buffer underwrite. Your application was unable to write samples to the background buffer fast enough for the device to get new samples at the specified sample rate. To avoid this error, you can do any the following: 1. Increase the size of the background buffer by configuring the buffer. 2. Increase the number of samples you write each time you invoke a write operation. 3. Write samples more often. 4. Reduce your sample rate. 5. Change the data transfer mechanism from interrupts to DMA. 6. Initially write a sufficient number of samples to satisfy the specified data transfer request condition. 7. Reduce the number of applications that your computer is executing concurrently. In addition, if you do not need to ensure that each sample is generated once and only once, you can set the regeneration mode to allow regeneration. |
| Error -200167 | Device cannot acquire from _cjTemp and other channels in the same task. Create one task for reading _cjTemp and another task for the other channels. |
| Error -200168 | Number of channels to acquire exceeds the device maximum. Reduce the number of channels. In some cases, you can access a large number of channels if they are identically configured and created consecutively. Refer to the documentation for more information. |
| Error -200169 | Memory mapping can be enabled only if Data Transfer Mechanism is Programmed IO. Enable memory mapping only when Data Transfer Mechanism is Programmed IO. |
| Error -200170 | Physical channel specified does not exist on this device. Refer to the documentation for channels available on this device. |
| Error -200171 | Virtual channel cannot be created. Another virtual channel with this name already exists. |
| Error -200172 | Buffer size must be zero when Data Transfer Mechanism is Programmed IO. Set buffer size to zero or Data Transfer Mechanism to something other than Programmed IO. |
| Error -200173 | The combination of Sample Timebase Rate and Master Timebase Rate you specified is invalid. The driver computed the Sample Timebase Source Divisor by dividing the Master Timebase Rate by the Sample Timebase Rate. The resulting value for the Sample Timebase Source Divisor is not supported by your device. Refer to the documentation for more information about these three properties. |
| Error -200175 | Hardware is not responding. Ensure your hardware is powered on and all cables are properly connected. |
| Error -200176 | Operation is not permitted while the switch device is scanning. |
| Error -200177 | Operation is permitted only while the switch device is scanning. |
| Error -200178 | Task was created with a settling time different from the current settling time. When scanning, you must use the original settling time specified when the task was created. |
| Error -200179 | Explicit connection between the channels already exists. You can make only one connection between these channels. |
| Error -200180 | Path between two switch channels is not available. |
| Error -200181 | Channel name specified is not valid for the switch device. |
| Error -200182 | Switch channels cannot be disconnected because there is no explicit path between them. |
| Error -200183 | Switch channel names cannot be duplicated in the path string. |
| Error -200184 | Leg in path cannot contain two channels that are already directly connected. |
| Error -200185 | Path contains a leg with two channels that cannot be directly connected. |
| Error -200186 | Channels used to make the connection between two endpoints must be reserved for routing. |
| Error -200187 | Channel cannot be connected to itself. |
| Error -200188 | Connection cannot be made between the specified channels because they are connected to different source channels. |
| Error -200189 | Explicit connection cannot be made to a switch channel that is reserved for routing. |
| Error -200190 | Disconnection path is not the same as the existing path. You can programmatically find out the existing path. Refer to your documentation for details. |
| Error -200191 | Task was created with a topology different from the current topology. When scanning, you must use the original topology specified when the task was created. |
| Error -200192 | Switch device supports continuous scanning only. |
| Error -200193 | Switch device does not support this operation. |
| Error -200194 | Hardware was unexpectedly powered off and back on. To recover, reset the device (either programmatically or by using Measurement & Automation Explorer). |
| Error -200195 | Switch configuration has caused the switch device to exceed its power limit because there were too many closed relays. The switch was disabled. Reset it by doing one of the following: 1. Call DAQmx Switch Set Topology And Reset. 2. Call DAQmx Device Reset. 3. Use Measurement & Automation Explorer. |
| Error -200196 | Action at the end of the scan list is not valid for this device. |
| Error -200197 | Device does not support this property. |
| Error -200198 | Topology specified is invalid. Make sure the spelling of the topology is correct and that the switch supports that topology. |
| Error -200199 | Switch device must be reset before scanning. Reset the device by doing one of the following: 1. Call DAQmx Switch Set Topology And Reset. 2. Call DAQmx Device Reset. 3. Use Measurement & Automation Explorer. |
| Error -200200 | Switch channel is already in exclusive use within another connection. |
| Error -200201 | Switch scan list is too large to fit in the onboard memory of the device. |
| Error -200202 | Relay name is invalid. |
| Error -200203 | Switch hardware is incapable of driving multiple trigger lines simultaneously. |
| Error -200204 | Unexpected identifier within the fully-specified path in the list. |
| Error -200205 | Topology does not support scanning. |
| Error -200206 | Advance trigger and Advance Complete event must use the same polarity in this particular switch device. |
| Error -200207 | Device identifier in the list entry is invalid. |
| Error -200208 | Range statement in the list entry contains an invalid character sequence. |
| Error -200209 | Duplicate device identifier found in the terminal list when trying to set the property. Only one instance of the device identifier is permitted. |
| Error -200210 | Multiple device identifiers from one chassis are not allowed in the terminal list. |
| Error -200211 | Multiple relay names were specified for a single relay operation. |
| Error -200212 | Measurement units specified for the channel are not valid for the Measurement Type of the channel. |
| Error -200213 | Pretrigger Samples per Channel requested plus minimum number of posttrigger samples exceed the requested Number of Samples per Channel. Decrease the number of Pretrigger Samples per Channel, or increase Number of Samples per Channel. |
| Error -200214 | Analog trigger circuitry unavailable on the device. Select a non-analog trigger type, or use a device with analog triggering hardware. |
| Error -200215 | Memory Mapping is not supported for buffered operations. Turn Memory Mapping off, set Buffer Size to 0, or do not configure the buffer for the operation. |
| Error -200216 | Buffered operations cannot use a Data Transfer Mechanism of Programmed I/O for this device and Channel Type. Non-buffered operations cannot use a Data Transfer Mechanism of Interrupts or DMA for this device and Channel Type. |
| Error -200217 | Buffered operations cannot use On Demand for Sample Timing Type. Set your buffer size to 0 for On Demand sample timing. Otherwise, configure your sample clock, or change your sample timing type for buffered operations. |
| Error -200218 | Data Transfer Mechanism must be Programmed I/O when not using hardware timing. Set Data Transfer Mechanism to Programmed I/O, configure your sample clock timing, or set Sample Timing Type to Sample Clock. |
| Error -200219 | Analog output virtual channels cannot be created out of order with respect to their physical channel numbers for the type of device you are using. For example, a virtual channel using physical channel ao0 must be created before a virtual channel with physical channel ao1. |
| Error -200220 | Device identifier is invalid. |
| Error -200221 | Amount of time allocated to perform this operation was exceeded. |
| Error -200222 | Acquisition has been stopped to prevent an input buffer overwrite. Your application was unable to read samples from the buffer fast enough to prevent new samples from overwriting unread data. To avoid this error, you can do any of the following: 1. Increase the size of the buffer. 2. Increase the number of samples you read each time you invoke a read operation. 3. Read samples more often. 4. Reduce the sample rate. 5. If your data transfer method is interrupts, try using DMA or USB Bulk. 6. Reduce the number of applications your computer is running concurrently. In addition, if you do not need to read every sample that is acquired, you can configure the overwrite mode to overwrite unread data, and then use the Relative To and Offset properties to read the desired samples. |
| Error -200223 | Specified threshold and hysteresis values for this channel create a triggering range that is not supported by your device. On the SCXI-1126, threshold minus hysteresis must be between -0.5 and 4.48. |
| Error -200224 | No registered trigger lines could be found between the devices in the route. If you have a PXI chassis, identify the chassis correctly in MAX, and make sure it has been configured properly. If you are using PCI devices, make sure they are connected with a RTSI cable and that the RTSI cable is registered in MAX. Otherwise, make sure there is an available trigger line on the trigger bus shared between the devices. |
| Error -200225 | Trigger line requested could not be reserved because it is already in use. |
| Error -200226 | Trigger bus to which the device is connected does not have any free trigger lines for the driver to choose. To free up trigger lines, you can do any of the following: 1. Stop other tasks that are connected to the same trigger bus as this device. 2. Use DAQmx Disconnect Route to stop any immediate routes that span this trigger bus. 3. Make more trigger lines on this trigger bus available to the driver. |
| Error -200227 | Device does not have any free trigger lines for the device driver to choose. Although there might be trigger lines available on the respective trigger bus, the device cannot use the trigger bus because the device does not have enough free resources to do so. To free up trigger lines, you can do any of the following: 1. Stop other tasks that are connected to this device. 2. Use DAQmx Disconnect Route to stop any immediate routes that span this trigger bus and device. |
| Error -200228 | Buffer is too small to fit the string. |
| Error -200229 | Buffer is too small to fit read data. |
| Error -200230 | NULL pointer was passed for a required parameter. |
| Error -200231 | Property requested cannot be set. |
| Error -200232 | Property requested cannot be read. |
| Error -200233 | Property specified is not valid for this function. |
| Error -200234 | Buffer is too small for requested samples to be written. |
| Error -200235 | Explanation could not be found for the requested status code. Verify that the requested status code is correct. |
| Error -200236 | Property requested cannot be reset. |
| Error -200237 | Hardware clocking error occurred. If you are using an external reference clock, make sure it is connected and within the jitter and voltage level specifications, and its rate is correctly specified. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200238 | Hardware clocking error occurred. If you are using an external reference clock, make sure it is connected and within the jitter and voltage level specifications at all times, and its rate is correctly specified. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200239 | Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200240 | Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, make sure it is connected and within the jitter and voltage specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200241 | Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, make sure it is connected and within the jitter and voltage specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200242 | Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, make sure it is connected and within the jitter and voltage specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200243 | Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, make sure it is connected and within the jitter and voltage specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200244 | Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200245 | PLL could not phase-lock to the external reference clock. Make sure your reference clock is connected and that it is within the jitter and voltage specifications. Also, make sure the reference clock rate is correctly specified. |
| Error -200246 | PLL has lost phase-lock to the external reference clock. Make sure your reference clock is connected and that it is within the jitter and voltage level specifications at all times. Also, make sure the reference clock rate is correctly specified at all times. |
| Error -200247 | Integer was expected but not found in the script. Insert an appropriate integer at this location in the script. |
| Error -200248 | Specified marker position is too close to the end of the last "generate" statement in a "repeat until" loop. Move the marker position farther away from the end of the last "generate" statement in the "repeat until" loop. |
| Error -200249 | Length of waveform subset is too small for the last "generate" statement in a "repeat until" loop. |
| Error -200250 | Length of waveform is too small for the last "generate" statement in a "repeat until" loop. |
| Error -200251 | No DMA channels or USB Bulk Endpoints are available. Either shut down other tasks that might be using these resources or consider changing your data transfer mechanism to Interrupts if supported. |
| Error -200252 | Terminal cannot be tristated because it is busy. Disconnect any routes spanning this terminal, or stop any tasks using this terminal. |
| Error -200253 | Terminal could not be tristated because the hardware cannot tristate this terminal. |
| Error -200254 | Terminal for the device is invalid. |
| Error -200255 | Built-in temperature sensor is not supported on this channel. This channel is not configured to support a built-in temperature sensor. Make sure the accessory specified in the hardware configuration is correct and that the hardware supports a built-in temperature sensor on this channel. |
| Error -200256 | Specified topology cannot be used to reset the switch, because that topology is not supported by the connected terminal block. Refer to the documentation for supported topologies for the given terminal block, or disconnect the terminal block from the switch. |
| Error -200257 | Excitation property must be the same for related physical channels. Refer to the documentation for information about setting excitation across related physical channels. |
| Error -200258 | Gain value conflicts with specified AI Minimum and AI Maximum properties. The specified gain and AI Minimum and/or AI Maximum would cause the device to exceed the hardware limit. Lower the gain, or adjust AI Minimum and/or AI Maximum. |
| Error -200259 | Value selected for this jumper-controlled property must match the value specified in Measurement & Automation Explorer. Make sure the value specified in Measurement & Automation Explorer matches the value in your program and that the value corresponds to the selection made using the jumper on the device. |
| Error -200260 | Memory mapping has been enabled, and the sample clock has been configured; but the buffer size has not been set, and the data transfer mechanism has either not been set or was set to something other than Programmed I/O. Set the buffer size to 0, and/or change the data transfer mechanism to Programmed I/O. |
| Error -200261 | An attempt has been made to use an analog trigger in multiple situations with differing properties. Change the analog trigger properties so they are the same, or do not use an analog trigger for all situations. |
| Error -200262 | An attempt has been made to configure a trigger without configuring the appropriate sample clock properties or when Sample Timing Type was set to On Demand. Configure the sample clock type to something other than On Demand to use a trigger. |
| Error -200263 | Device supports an analog channel as the source of an analog pause trigger only when it is the only channel in the task. Remove all of the channels currently in the task except the channel that will be used as the analog trigger source, or change the analog trigger source to a terminal. |
| Error -200264 | Device supports an analog channel as the source of an analog reference trigger only when it is the only channel in the task. Remove all of the channels currently in the task except the channel that will be used as the analog trigger source, or change the analog trigger source to a terminal. |
| Error -200265 | An attempt has been made to use an invalid analog trigger source. Ensure that the trigger source you specify matches the name of the virtual channel in the task or matches the name of a non-scannable terminal that the device can use as an analog trigger source. |
| Error -200266 | Minimum and maximum values for the channel are not symmetric. |
| Error -200267 | Product of AO channel properties Maximum Value and Gain exceeds the maximum voltage for the device. |
| Error -200268 | Specified Offset is too small given AO Gain and Minimum Value. The following constraint must hold: Offset > (Gain * Minimum Value / 2) |
| Error -200269 | Specified Offset is too large for the given AO Gain and Maximum Value. The following constraint must hold: Offset < (Gain * Maximum Value / 2) |
| Error -200270 | Interpolation rate specified is not possible for the given sample rate. |
| Error -200271 | Product of AO Channel properties Minimum Value and Gain exceeds the minimum voltage for the device. |
| Error -200272 | Sample clock rate requested is too low for the selected divide-down clock. Use the high resolution clock, or increase your sample rate. |
| Error -200273 | Sample clock rate and the sample clock divisor values are inconsistent with one another. Consider settting either the sample clock rate or the sample clock divisor, but not both. This allows the driver to automatically select an appropriate value for the other property. Alternatively, make sure the sample clock rate and sample clock divisor satisfy the following constraint: rate = timebase / divisor |
| Error -200274 | Sample clock rate desired is too high for an external clock being brought in through the backplane. Bring in your external sample clock through one of the higher-frequency front panel connectors, or use a lower sample rate. |
| Error -200275 | Sample rate desired is too low for an external clock being brought in through the ClkIn connector. Change the sample rate so it is within limits, or use DDC_ClkIn to bring in your sample clock. |
| Error -200276 | Reference clock source and sample clock source cannot be the same. Use different terminals to bring in your reference clock and sample clock, or use only one of them at a time. |
| Error -200277 | Invalid combination of position and offset. The position and offset specified a sample prior to the first sample acquired (sample 0). Make sure any negative read offset specified will select a valid sample when combined with the read position. |
| Error -200278 | Attempted to read a sample beyond the final sample acquired. The acquisition has stopped, therefore the sample specified by the combination of position and offset will never be available. Specify a position and offset which selects a sample up to, but not beyond, the final sample acquired. The final sample acquired can be determined by querying the total samples acquired after an acquisition has stopped. |
| Error -200279 | The application is not able to keep up with the hardware acquisition. Increasing the buffer size, reading the data more frequently, or specifying a fixed number of samples to read instead of reading all available samples might correct the problem. |
| Error -200281 | Reading relative to the reference trigger or relative to the start of pretrigger samples position before the acquisition is complete. Wait for the acquisition to complete before reading, or increase your read timeout. Also, make sure the hardware is set up and wired correctly, the signal for the reference trigger is correct, and that the reference trigger occurs while the device is acquiring data. |
| Error -200282 | Reading relative to the reference trigger or relative to the start of a pretrigger sample is not supported with the current task configuration. If you have not configured a reference trigger or if one of your devices is utilizing an onboard buffer to transfer data after an acquisition has completed, reading relative to reference trigger or relative to the first pretrigger sample is not supported. Configure a reference trigger, or configure read position differently. |
| Error -200283 | Acquisition has stopped to prevent the intermediate buffer from overflowing. The background was running too fast for the application to keep up, and the application was unable to read samples from the intermediate buffer fast enough to prevent losing samples. To avoid this error, you might reduce the sample rate, reduce the number of applications your computer is executing concurrently, or not read any samples until the acquisition is complete. |
| Error -200284 | Some or all of the samples requested have not yet been acquired. To wait for the samples to become available use a longer read timeout or read later in your program. To make the samples available sooner, increase the sample rate. If your task uses a start trigger, make sure that your start trigger is configured correctly. It is also possible that you configured the task for external timing, and no clock was supplied. If this is the case, supply an external clock. |
| Error -200286 | No data is available to read, because no acquisition has been started. Start the acquisition before attempting to read data, either explicitly or by enabling auto start and stop. |
| Error -200287 | Attempted to write to an invalid combination of position and offset. The position and offset specified a sample prior to the first sample generated (sample 0). Make sure any negative write offset specified will select a valid sample when combined with the write position. |
| Error -200288 | Attempted to write a sample beyond the final sample generated. The generation has stopped, therefore the sample specified by the combination of position and offset will never be available. Specify a position and offset which selects a sample up to, but not beyond, the final sample generated. The final sample generated can be determined by querying the total samples generated after a generation has stopped. |
| Error -200289 | Attempted to write samples that have already been generated or have already been sent to the device for generation. Increasing the buffer size or writing the data more frequently might correct the problem. |
| Error -200290 | The generation has stopped to prevent the regeneration of old samples. Your application was unable to write samples to the background buffer fast enough to prevent old samples from being regenerated. To avoid this error, you can do any of the following: 1. Increase the size of the background buffer by configuring the buffer. 2. Increase the number of samples you write each time you invoke a write operation. 3. Write samples more often. 4. Reduce the sample rate. 5. If your data transfer method is interrupts, try using DMA or USB Bulk. 6. Reduce the number of applications your computer is executing concurrently. In addition, if you do not need to write every sample that is generated, you can configure the regeneration mode to allow regeneration, and then use the Position and Offset attributes to write the desired samples. |
| Error -200291 | The generation has stopped because an intermediate buffer overflowed. The background was running too fast for the application to keep up, and the application was unable to write samples to the intermediate buffer fast enough to prevent regenerating old samples. To avoid this error, you can reduce the sample rate, reduce the number of applications your computer is executing concurrently, or write all samples before the generation starts. |
| Error -200292 | Some or all of the samples to write could not be written to the buffer yet. More space will free up as samples currently in the buffer are generated. To wait for more space to become available, use a longer write timeout. To make the space available sooner, increase the sample rate. |
| Error -200293 | The generation is not yet started, and not enough space is available in the buffer. Configure a larger buffer, or start the generation before writing more data than will fit in the buffer. |
| Error -200294 | Not enough samples were written to satisfy the initial data transfer request condition. To successfully start a generation, increase the number of samples initially written to the buffer before starting. Alternatively, decrease the number of samples required to start by changing the data transfer request condition. |
| Error -200295 | Attempt was made to write samples after start of generation where only onboard memory was used. In this case, all samples must be written to the device before the start of generation. No samples may be updated once the generation has started. If you wish to modify samples in the generation after the start of the generation, do not enable the onboard memory. |
| Error -200297 | This property is unavailable when using onboard memory. |
| Error -200300 | Invalid timing type for this channel. |
| Error -200301 | Cannot update the Pulse Generation property. The pulse generation with previous property settings must complete a full cycle before the property can be updated. |
| Error -200302 | Signal being measured is slower than the specified measurement time. Increase the measurement time, or use a different measurement method. |
| Error -200303 | External sample clock source must be specified for this application. |
| Error -200304 | External master timebase rate must be specified for this channel given the selected measurement units. Specify the master timebase rate, or use ticks as the measurements units. |
| Error -200305 | Desired finite pulse train generation is not possible. Change the number of samples to be generated, increase the rate of the pulse train, or choose a different timebase source. Refer to the documentation for more details. |
| Error -200306 | An attempt was made to set the Samples per Channel property to a value greater than the maximum supported number. |
| Error -200307 | Specified master timebase rate does not match specified master timebase source. Do not set the master timebase rate when you are using an internal master timebase source. In this case, the driver sets the master timebase rate for you. |
| Error -200308 | Specified sample timebase rate does not match specified sample timebase source. Do not set the sample timebase rate when you are using an internal sample timebase source. In this case, the driver sets the sample timebase rate for you. |
| Error -200309 | Specified master timebase divisor (belonging to sample clock timebase) is not appropriate for the specified sample timebase source. Do not set the master timebase divisor when you are using an internal sample timebase source. In this case, the driver sets the master timebase divisor for you. |
| Error -200310 | The waveform you are trying to allocate on the device has been previously allocated. Make sure you are not trying to allocate the same waveform twice, or delete the existing waveform before allocating it again. |
| Error -200311 | You cannot write data outside the boundaries of your waveform. Make sure you are not trying to write more data than your waveform can accomodate and that your write location and write offset are set correctly. |
| Error -200312 | Waveform is not in the device memory. Make sure you are referring to a previously allocated and/or written waveform by its correct name. Also, make sure that the waveform was not deleted. |
| Error -200313 | Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, make sure it is connected and within the jitter and voltage specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200314 | Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, make sure it is connected and within the jitter and voltage specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200315 | There is not enough free device memory for your waveform. Delete waveforms or scripts not in use to free memory. If you have deleted multiple waveforms or scripts, the memory might have become fragmented. To avoid fragmentation, you can change the order in which you write/delete your waveforms and scripts. |
| Error -200316 | Device data underflow. The device was not able to move data fast enough to keep up with the sample rate for the active script. Run the operation at a lower sample rate, or look for the following in the active script: markers might be too close together, waveforms might be too small, waits might be too short, or subsets might be too small. If you are using an external clock, the provided clock might have gone away during your generation. |
| Error -200317 | There is not enough free device memory for your script. Delete waveforms or scripts not in use to free memory. If you have deleted multiple waveforms or scripts, the memory might have become fragmented. To avoid fragmentation, you can change the order in which you write/delete your waveforms and scripts. |
| Error -200318 | Invalid excitation value specified to be used for scaling with full bridge configuration. Change the excitation value if you want it to be used for scaling with full bridge configuration. Alternatively, change the bridge configuration, or do not use excitation value for scaling. |
| Error -200319 | Your SCXI system is not set up to perform the analog input operation on given channels. The SCXI module cabled to your digitizer cannot route AI Convert Clock from the digitizer to the other modules. To perform the desired operation with multiple SCXI modules and one digitizer, cable the digitizer to one of the modules that can route the AI Convert signal, such as the module your channels are on. After cabling the digitizer to the module, update the chassis configuration in Measurement & Automation Explorer to reflect the cabling change. For detailed information about cabling, refer to the documentation. |
| Error -200320 | Your SCXI system is not set up for analog input with simultaneous sample and hold on the given channels. The SCXI module cabled to your digitizer cannot route the signal needed for simultaneous sample and hold from the digitizer to the other modules. To perform the desired operation with multiple SCXI modules and one digitizer, cable the digitizer to one of the modules that can route the signal needed for simultaneous sample and hold. The simultaneous sample and hold module in your chassis is one such module. After cabling the digitizer to the module, update the chassis configuration in Measurement & Automation Explorer to reflect the cabling change. For detailed information about cabling, refer to the documentation. |
| Error -200321 | Attenuation Value conflicts with the specified AI Minimum and AI Maximum properties. The specified attenuation and AI Minimum and/or AI Maximum would cause the device to exceed the hardware limit. You should increase the Attenuation Value or adjust the AI Minimum and/or AI Maximum. |
| Error -200322 | Data transfer has been stopped to prevent the computer from becoming completely unresponsive. Could not transfer enough data to satisfy the data transfer requirements with Interrupts as the Data Transfer Mechanism. Reduce your Sample Clock Rate, use DMA as your Data Transfer Mechanism, or use a different Data Transfer Request Condition. |
| Error -200323 | Cannot perform a multidevice scan with Advance Trigger Type set to None. Without the advance trigger, the devices in the scan list cannot be synchronized. |
| Error -200324 | NI-DAQmx is unable to communicate with the device. Make sure the device is present in and accessible to the system, is not currently being reset, and is not reserved by another driver such as Traditional NI-DAQ (Legacy). |
| Error -200325 | Reverse coefficients must be specified to scale your data using the polynomial scale. |
| Error -200326 | An attempt has been made to perform a route when the source and the destination are the same terminal. In many cases, such as when configuring an external clock or a counter source, you must select a PFI, PXI Trigger, or RTSI line as the source terminal. |
| Error -200327 | You have specified an invalid value for dt in the waveform cluster. The value for dt must be greater than zero. |
| Error -200328 | Switch driver cannot open the topology configuration file for the switch device. A switch device cannot function without its configuration file. The configuration file is installed with the driver. The file might have been removed, renamed, or corrupted after installation. Make sure the configuration file is available to the driver at the expected location, or reinstall the product, as that will reinstall the configuration file. |
| Error -200329 | An error has occurred while attempting to configure the device for an analog input acquisition. If an external master timebase is being used, make sure the source is connected and generating an appropriate clock. Otherwise, contact National Instruments Technical Support. |
| Error -200330 | An attempt has been made to use the PFI0 terminal of the device for both an analog and digital source. Use a terminal other than PFI0 as the source of your digital signal. |
| Error -200331 | Specified sample rate is lower than the lowest rate that can be generated using the onboard clock. The rate has been coerced to the slowest possible sample rate. For slower rates, use an external sample clock or an external sample clock timebase. |
| Error -200332 | Specified sample rate is higher than the fastest rate supported by the device. |
| Error -200333 | Delay from the start trigger is shorter than the shortest delay that can be generated using the onboard clock with a timebase suitable for generating the sample clock. For shorter delays, use a sample clock timebase with a higher rate, if applicable. |
| Error -200334 | Delay from start trigger is longer than the longest delay that can be generated using the onboard clock with a timebase suitable for generating the sample clock. For longer delays, use a slower sample clock timebase rate, if applicable. |
| Error -200335 | Specified AI convert rate is higher than the fastest rate possible with the current timebase. |
| Error -200336 | Delay from the sample clock is shorter than the shortest delay that can be generated using the onboard clock with a timebase suitable for generating the convert clock. For shorter delays, use a faster convert clock timebase rate, if applicable. |
| Error -200337 | Delay from the sample clock is longer than the longest delay that can be generated using the onboard clock with a timebase suitable for generating the convert clock. For longer delays, use a slower convert clock timebase rate, if applicable. |
| Error -200338 | An attempt has been made to read the calibration temperature for a device without an internal temperature sensor. |
| Error -200339 | Pulse width measurement was started while the input signal was active, and no additional pulses were received, which caused the measurement not to complete during the specified timeout. When measuring a single pulse width, make sure the measurement counter is started before the pulse to be measured is active, or provide a timeout sufficient for at least one additional pulse to be measured. |
| Error -200340 | By setting Number of Samples per Channel to -1, you indicated that all available data should be read. This is not valid for acquisitions without a buffer. Specify a value greater than or equal to zero for Number of Samples per Channel. Do not specify a value of zero for Buffer Size when configuring the input buffer. |
| Error -200341 | Generation was configured to use only onboard memory, but the corresponding buffer is larger than onboard memory. Buffer size is provided implicitly when data is written or explicitly when the buffer is configured. Configure the generation so that the Use Only Onboard Memory property is false. Alternatively, you can make sure the number of samples written and/or the size of the configured buffer do not exceed the onboard memory size. |
| Error -200342 | Script is not in the device memory. Make sure you are referring to a previously written script by its correct name. Also, make sure the script has not been deleted. |
| Error -200343 | Driver cannot determine the number of samples to read for a continuous task that has not yet started. Start the task explicitly, or specify the number of samples to read in DAQmx Read. |
| Error -200344 | Requested number of samples per channel is invalid. The number of samples per channel must be an integer multiple of the number of samples per channel increment. |
| Error -200345 | Event delay is outside of the legal range. Change the value of the delay, and/or verify that the units are correct. |
| Error -200346 | Event pulse width is outside of the legal range. Change the value of the pulse width, and/or verify that the units are correct. |
| Error -200347 | Invalid intermediate buffer size. The size of the intermediate buffer must be an integer multiple of the intermediate buffer size increment. |
| Error -200348 | Scaled Values must be specified for the table scale. |
| Error -200349 | Prescaled Values must be specified for the table scale. |
| Error -200350 | Number of Prescaled Values needs to be equal to the number of Scaled Values in the table scale. |
| Error -200351 | Forward coefficients must be specified for the polynomial scale. |
| Error -200352 | Physical channel corresponding to the virtual channel specified for cold-junction compensation is already being used for a thermocouple measurement, so it cannot be used as the cold-junction compensation channel. |
| Error -200353 | Specified property value cannot be used, because it requires resources that are currently in use. |
| Error -200354 | Specified property value is not a valid terminal name. |
| Error -200355 | Specified property value cannot be used, because the hardware does not support it. |
| Error -200356 | Custom scale cannot be created. A saved scale with this name already exists. |
| Error -200357 | Measurement device cannot acquire data from the sensor in its current configuration. The voltage output range of your sensor does not overlap with the voltage input range of your measurement device. If your measurement device supports different gains or input ranges, try using a lower gain or a wider input range. If the device has a fixed gain/range, you might need to change sensor attribute settings such as Excitation Value or use a measurement device that supports a wider voltage input range. |
| Error -200358 | An attempt has been made to configure a reference trigger when the sample mode of the sample clock has been configured for continuous sampling. Reference trigger is only applicable for finite sampling. Change the sample mode to finite to use a reference trigger, or do not configure a reference trigger. |
| Error -200359 | Counter signals cannot be exported, because there is more than one counter channel in the task. Create separate tasks for each counter channel. |
| Error -200360 | CJC Source has been set to Channel, while the CJC channel has not been specified. Specify the CJC channel, or set CJC Source to a value other than Channel. |
| Error -200361 | Onboard device memory overflow. Because of system and/or bus-bandwidth limitations, the driver could not read data from the device fast enough to keep up with the device throughput. Reduce your sample rate. If your data transfer method is interrupts, try using DMA or USB Bulk. You can also use a product with more onboard memory or reduce the number of programs your computer is executing concurrently. |
| Error -200362 | The Overloaded Channels Exist property was not read prior to reading the specified property. The driver retrieves the overload state from the hardware when the application reads the Overloaded Channels Exist property. After the Overloaded Channels Exist property has been read, other information about overloaded channels may be read, such as which channels are overloaded. |
| Error -200363 | Specified inversion cannot be satisfied, because the hardware does not support it. |
| Error -200364 | Specified polarity is not supported by the hardware. |
| Error -200365 | Specified inversion cannot be satisfied, because it requires resources that are currently in use by another route. |
| Error -200366 | Specified inversion cannot be satisfied, because it requires resources that are currently in use by another route within this task. |
| Error -200367 | Specified polarity cannot be satisfied, because it requires resources that are currently in use by another route within this task. |
| Error -200368 | Specified route cannot be satisfied, because the hardware does not support it. |
| Error -200369 | Specified route cannot be satisfied, because it requires resources that are currently in use by another route. |
| Error -200370 | Specified route cannot be satisfied, because it requires resources that are currently in use by another route within this task. |
| Error -200371 | Requested multiple virtual channels that correspond to the same physical channel within a task. A task cannot contain multiple physical channels of a specified type. Use different physical channels for each virtual channel. |
| Error -200372 | Trigger type requested to be sent as the software trigger is invalid. |
| Error -200373 | Trigger type requested to be sent as software trigger is not supported for the specified task running on the given device. |
| Error -200374 | Signal type requested to be exported is not valid. |
| Error -200375 | Signal type requested to be exported is not supported for the specified task running on the given device. |
| Error -200376 | Requested creation of a separate channel for each line is not possible when a digital port is specified as the physical channel. Specify a range of digital lines, such as "Dev1/port0/line0:7", as the physical channel. |
| Error -200377 | Requested operation is not supported by the device during a scan. The device only supports operations on front-end channels (for example, ch0, ch1, ... or cjtemp) while scanning. Other operations, such as operations on analog bus channels (such as ab0 and ab1), are not supported by the device during a scan. Make sure your scan list contains only supported operations. |
| Error -200378 | Custom scale specified does not exist. |
| Error -200379 | External clock frequency and external clock divisor values result in an invalid cutoff frequency for this device. The relationship between cutoff frequency, external clock frequency, and external clock divisor is: cutoffFreq = extClkFreq / (100 * extClkDiv) Change your external clock frequency or external clock divisor. |
| Error -200380 | Strain gage calibration procedure has failed. Make sure the strain gages are connected to all the specified strain channels, the strain gage connections are appropriate for their bridge type configurations, the shunt resistor location is specified correctly, and your hardware jumpers (if any) are set up correctly. |
| Error -200381 | Unable to configure requested delay property given the current clock rate. Make sure the sample clock rate is greater than or equal to the phase shift DMC threshold of your device, or do not configure the delay. Consult your documentation for more information. |
| Error -200382 | Specified trigger type for pattern match mode could not be configured, because all pattern matchers are already in use. |
| Error -200383 | Reference Clock Source specified is invalid, given the Sample Clock Source. When Sample Clock Source is anything other than "OnboardClock", you must set Reference Clock Source to "None", and you cannot export the Reference Clock. |
| Error -200384 | Static output cannot be performed, because some data lines have already been reserved for a dynamic output. |
| Error -200385 | Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200386 | Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200387 | Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200388 | Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200389 | Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200390 | Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200391 | Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200392 | Specified output voltage is not valid with the given sample clock rate. Make sure your output voltage level is compatible with your sample clock rate by altering the output voltage level or the sample clock rate. Consult your documentation for more information. |
| Error -200393 | You are attempting to write to a read-only register. |
| Error -200394 | Requested value for the property is invalid, because it is not an unsigned integer. Even though the datatype of the property is a floating point number, the value must be an unsigned integer less than or equal to 9,007,199,254,740,992 (2^53). |
| Error -200395 | There are no shared trigger lines between the two devices which are acceptable to both devices. While each of these two devices support some shared trigger lines, none of these shared trigger lines work for both devices for the specified property and corresponding value. Consider routing the signal through the I/O connectors of the two devices, if applicable. |
| Error -200396 | There are no shared trigger lines between the two devices that are acceptable to both devices. While each of the two devices support some shared trigger lines, none of the shared trigger lines work for both devices for the specified source and destination terminals. Consider routing the signal through the I/O connectors of the two devices, if applicable. |
| Error -200397 | Unable to load NI-DAQmx dynamic link library NICAIU.DLL. Make sure that NI-DAQmx is installed on your computer. |
| Error -200398 | Unable to find function in NI-DAQmx dynamic link library NICAIU.DLL. The DLL exists on your computer, but the version is incorrect. Install the correct version of the DLL on your computer. |
| Error -200399 | No extended error information is available for the last error code. It is possible that there was a problem initializing the internal errors database. Please contact National Instruments Technical Support. |
| Error -200400 | Requested waveform length is invalid, because the number of samples is not an integer multiple of the waveform length increment. |
| Error -200401 | Number of points to compute over the range of x values is not positive. Specify a value greater than 0 for this input. |
| Error -200402 | Order of the reverse polynomial to compute is not positive. Specify a value greater than 0 for this input. |
| Error -200403 | Order of the reverse polynomial to compute is less than or equal to the number of points to compute over the range of x values. Reduce the order of the reverse polynomial or increase the number of points to compute over the range of x values. |
| Error -200404 | Forward and Reverse Coefficients for a polynomial scale are not specified. Each of these two sets of coefficients must contain at least one term. If only one set of coefficients is available, use the Compute Reverse Polynomial Coefficient utility to calculate the other set of coefficients. |
| Error -200405 | Forward Coefficients for a polynomial scale are not specified. This set of coefficients must contain at least one term. If the coefficients are not available, you can pass the supplied Reverse Coefficients to the Compute Reverse Polynomial Coefficients utility to calculate the required Forward Coefficients. |
| Error -200406 | Reverse Coefficients for a polynomial scale are not specified. This set of coefficients must contain at least one term. If the coefficients are not available, use the Compute Reverse Polynomial Coefficient utility to calculate the required coefficients from the supplied Forward Coefficients. |
| Error -200407 | Forward Coefficients for a polynomial scale are all set to zero. At least one of these coefficients must be non-zero. |
| Error -200408 | Reverse Coefficients for a polynomial scale are all set to zero. At least one of these coefficients must be non-zero. |
| Error -200409 | Slope for a linear scale is set to zero. The slope must be non-zero. |
| Error -200410 | Requested record number is invalid. Use the Records Done property to find out how many records are available. Record numbers start at 0. Use -1 for all available records. |
| Error -200411 | AC coupling is not allowed with 50 Ohm impedance for this device. Use DC coupling, or configure a different impedance setting. |
| Error -200412 | Requested analog input attenuation is invalid. |
| Error -200413 | Insufficient onboard memory for requested Number of Records and Samples per Channel combination. Reduce the Number of Records and/or Samples per Channel. |
| Error -200414 | Requested sample clock source is invalid. |
| Error -200415 | Requested reference clock source is invalid. |
| Error -200416 | Multiple records are not available with RIS. |
| Error -200417 | TDC is not enabled during RIS mode. TDC must be enabled when the digitizer is in the RIS mode. Enable TDC, or do not use RIS. |
| Error -200418 | Requested immediate trigger type while in RIS mode. Immediate triggering is not compatible with the RIS mode. Select a different trigger type, or do not use RIS. |
| Error -200419 | Requested Read Position is invalid in RIS mode. |
| Error -200420 | Requested sample rate exceeds maximum real-time sample rate. If you want a higher sampling rate and have a repetitive signal, enable RIS. |
| Error -200421 | Requested Hysteresis is not valid with the configured Trigger Level and AI Minimum. Configure the task so the following formula is satisfied: Trigger Level - Hysteresis > AI Minimum |
| Error -200422 | Requested Trigger Level is not valid with the configured AI Minimum and AI Maximum. Configure the instrument so the following formula is satisfied: AI Minimum < Trigger Level < AI Maximum |
| Error -200423 | Requested window trigger level is not valid with the configured AI Minimum and AI Maximum. Configure the instrument so the following formula is satisfied: AI Minimum < Window Trigger Level < AI Maximum |
| Error -200424 | Requested video trigger line number is incompatible with the chosen video signal format. |
| Error -200425 | Requested hysteresis is not valid with the configured trigger level and AI Maximum. Configure the task so the following formula is satisfied: Trigger Level + Hysteresis < AI Maximum |
| Error -200426 | Requested impedance for the external trigger is invalid. Specify an impedance that is appropriate for the external trigger, or choose a different trigger source. |
| Error -200427 | Configured reference clock rate is invalid. The reference clock rate must be within the valid range and a multiple of the increment value. |
| Error -200428 | Value passed to the Task/Channels In control is invalid. The value must refer to a valid task or valid virtual channels. |
| Error -200429 | Value passed to the Task/Channels In control is an empty string (or I/O control). The value must refer to a valid task or valid channels. |
| Error -200430 | I/O type of the physical channel does not match the I/O type required for the virtual channel you are creating. |
| Error -200431 | Selected physical channel does not support the measurement type required by the virtual channel you are creating. Create a channel of a measurement type that is supported by the physical channel, or select a physical channel that supports the measurement type. |
| Error -200432 | Selected physical channel does not support the output type required by the virtual channel you are creating. Create a channel of an output type that is supported by the physical channel, or select a physical channel that supports the output type. |
| Error -200433 | Scaled Values for a table scale must contain at least two values. |
| Error -200434 | Prescaled Values for a table scale must contain at least two values. |
| Error -200435 | Delay from sample clock is not available when an external convert source is specified. Change the convert source to onboard clock, or do not configure the delay from sample clock. |
| Error -200436 | Start trigger delay is not available when an external sample clock source is specified. Change the sample clock to onboard clock, or do not configure the start trigger delay. |
| Error -200437 | External calibration constants are invalid. Perform an external calibration. Contact National Instruments Technical Support if you need additional information. |
| Error -200438 | Invalid calibration area selected. Select self-calibration or external calibration. |
| Error -200439 | Requested operation only can be used during an external calibration session. |
| Error -200440 | Requested calibration close action is invalid. Select Store or Abort. |
| Error -200441 | Unable to detect the external stimulus frequency. Verify that the external stimulus is properly connected and has the correct frequency and amplitude. |
| Error -200442 | Unable to synchronize to the external stimulus frequency. Verify that the external stimulus has the correct frequency, amplitude, and stability. Consult the documentation for the calibration procedure for valid ranges. |
| Error -200443 | Attempt to store calibration constants without completing all the necessary external calibration steps. Refer to the documentation for the calibration procedure. Verify that all necessary steps are performed before closing the external calibration session. |
| Error -200444 | Invalid physical channel selected for calibration. |
| Error -200445 | Requested calibration function is not supported by the device. |
| Error -200446 | External stimulus voltage read was outside the expected range. Verify that the external stimulus voltage is properly connected and has the correct amplitude. |
| Error -200447 | Units for the channel must be set to From Custom Scale when a custom scale is used with a channel. |
| Error -200448 | DAC Range High is not equal to the DAC Reference Voltage Value. When you do not set the DAC Range High property, the driver always makes sure it is equal to the DAC Reference Voltage value. If you do set the DAC Range High property make sure DAC Range High and DAC Reference Voltage Value are equal. |
| Error -200449 | DAC Range Low must be equal to either the negative DAC Reference Voltage Value or to zero. If you do not set the DAC Range Low property, the driver sets it for you. Otherwise, make sure DAC Range Low is equal to either the negative DAC Reference Voltage Value or to zero. |
| Error -200450 | Specified property cannot be set while the task is running. |
| Error -200451 | You can get the specified property only while the task is committed or running. |
| Error -200452 | Specified property is not supported by the device or is not applicable to the task. |
| Error -200453 | Specified timeout value is not supported. Supported timeout values are 0 (try or check once and return), positive numbers up to 4294967, and -1 (try or check until success or error). |
| Error -200454 | You cannot get the specified property, because the task is not a buffered output task. |
| Error -200455 | You cannot get the specified property, because the task is not a buffered input task. |
| Error -200456 | Specified property is not supported, because the task is not an output task. |
| Error -200457 | Specified property is not supported, because the task is not an input task. |
| Error -200459 | Write failed, because there are no output channels in this task to which data can be written. |
| Error -200460 | Read failed, because there are no channels in this task from which data can be read. |
| Error -200461 | Specified channel name is invalid. |
| Error -200462 | Generation cannot be started because the output buffer is empty. Write data before starting a buffered generation. The following actions can empty the buffer: changing the size of the buffer, unreserving a task, setting the Regeneration Mode property, changing the Sample Mode, or configuring retriggering. |
| Error -200463 | Specified read or write operation failed, because the number of lines in the data for a channel does not match the number of lines in the channel. If you are using the Digital Waveform datatype, make sure the number of lines in the digital waveform matches the number of lines in the channel. If you are using boolean data, make sure the array dimension for lines in the data matches the number of lines in the channel. |
| Error -200464 | If performing a Write operation, the operation cannot be performed, because the number of channels in the specified data does not match the number of channels in this task. Adjust the data to match the number of channels in this task. If you are performing a read operation, the operation cannot be performed because this DAQmx Read only returns data from a single channel, and there are multiple channels in this task. Use the multichannel DAQmx Read. |
| Error -200465 | Specified digital channel contains more bits than what is supported by DAQmx Port Write. With the U8 version, channels must contain 8 bits or less; while for the U32 version, channels must contain 32 bits or less. |
| Error -200466 | Specified digital channel contains more bits than what is supported by DAQmx Port Read. With the U8 version, channels must contain 8 bits or less; while for the U32 version, channels must contain 32 bits or less. |
| Error -200467 | Specified string is not valid, because it is empty. |
| Error -200469 | Specified channel cannot be loaded, because it was saved with an incompatible, more recent version of NI-DAQ. Create the channel again, or upgrade NI-DAQ to a version compatible with the version used to save the channel. Consult the documentation for the version of NI-DAQ used to create the channel for more details. |
| Error -200470 | Specified task cannot be loaded, because it was saved with an incompatible, more recent version of NI-DAQ. Create the task again, or upgrade NI-DAQ to a version compatible with the version used to save the task. Consult the documentation for the version of NI-DAQ used to create the task for more details. |
| Error -200472 | Write cannot be performed when the auto start input to DAQmx Write is false, and timing for the task is not configured or Timing Type is set to On Demand. Set auto start to true, or configure timing and specify Timing Type other than On Demand. |
| Error -200473 | Read cannot be performed when the Auto Start property is false and the task is not running or committed. Start the task before reading, or set Auto Start to true. |
| Error -200474 | Specified operation did not complete, because the specified timeout expired. |
| Error -200475 | Specified operation can be performed only when the task is running. Start the task before requesting this operation. |
| Error -200477 | Specified operation cannot be performed when there are no devices in the task. |
| Error -200478 | Specified operation cannot be performed when there are no channels in the task. |
| Error -200479 | Specified operation cannot be performed while the task is running. |
| Error -200481 | Specified device cannot be added to the task, because it is already in the task. |
| Error -200482 | Specified device is not in the task. |
| Error -200483 | Specified virtual channel cannot be saved, because a virtual channel with that name already exists in Data Neighborhood in MAX. Save the virtual channel under a different name, or specify that the existing virtual channel should be replaced. |
| Error -200484 | Specified task cannot be saved, because a task with that name already exists in Data Neighborhood in MAX. Save the task under a different name, or specify that the existing task should be replaced. |
| Error -200485 | The specified task cannot be loaded, because it is not in Data Neighborhood. Check Data Neighborhood in MAX. Look for similar characters, such as the capital letter "O" and the number zero. |
| Error -200486 | Specified channel is not in the task. |
| Error -200488 | Specified virtual channel cannot be added to the task, because it does not exist. You cannot specify a physical channel. Instead, create a virtual channel using the DAQ Assistant or DAQmx Create Virtual Channel, and then add the virtual channel to the task. |
| Error -200489 | Specified channel cannot be added to the task, because a channel with the same name is already in the task. |
| Error -200490 | Sample value detected outside of the specified range. |
| Error -200491 | Reserved parameter must be zero. |
| Error -200492 | Reserved parameter must be NULL. |
| Error -200493 | Reserved character string parameter must be NULL or an empty string. |
| Error -200494 | Specified task cannot be loaded, because it requires a device that supports timing, and the associated device does not support timing. Create a new task without timing, or associate this task with a device that supports timing. |
| Error -200495 | An intermediate acquisition buffer has overflowed. The driver was unable to read samples from the intermediate buffer fast enough to prevent the buffer from overflowing. |
| Error -200496 | Pattern contains an invalid character. |
| Error -200497 | Attempted to enable output data lines that were not previously disabled. Make sure that you are enabling data lines for output only after explicitly disabling them. |
| Error -200498 | Syntax for a range of objects in the input string is invalid. For ranges of objects, specify a number immediately before and after every colon (":") in the input string. Or, if a name is specified after the colon, it must be identical to the name specified immediately before the colon. Colons are not allowed within the names of the individual objects. |
| Error -200499 | Value passed is not between 0 and 4,294,967,295 (unsigned 32-bit integer). |
| Error -200500 | Error code could not be found. Reinstalling the driver might fix the issue. Otherwise, contact National Instruments technical support. |
| Error -200501 | EEPROM contains an invalid calibration date and/or time. The calibration data in the EEPROM might have been corrupted. Perform an external calibration, perform a self-calibration, or contact National Instruments Technical Support. |
| Error -200502 | A measurement taken during adjustment of main path pre-amplifier offset produced an invalid calibration constant. Make sure that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, and repeat the calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National Instruments Technical Support. |
| Error -200503 | A measurement taken during adjustment of main path pre-amplifier gain produced an invalid calibration constant. Make sure that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, and repeat the calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National Instruments Technical Support. |
| Error -200504 | A measurement taken during adjustment of main path post-amplifier gain and offset produced an invalid calibration constant. Make sure that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, and repeat the calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National Instruments Technical Support. |
| Error -200505 | A measurement taken during adjustment of direct path gain produced an invalid calibration constant. Make sure that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, and repeat the calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National Instruments Technical Support. |
| Error -200506 | A measurement taken during adjustment of main path output impedance produced an invalid calibration constant. Make sure that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, and repeat the calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National Instruments Technical Support. |
| Error -200507 | A measurement taken during adjustment of direct path output impedance produced an invalid calibration constant. Make sure that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, and repeat the calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National Instruments Technical Support. |
| Error -200508 | A measurement taken during adjustment of the oscillator frequency produced an invalid calibration constant. Make sure that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, and repeat the calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National Instruments Technical Support. |
| Error -200509 | A measurement taken during adjustment of calibration ADC produced an invalid calibration constant. Make sure that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, and repeat the calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National Instruments Technical Support. |
| Error -200510 | Requested an invalid configuration value for adjusting the main path pre-amplifier offset. Refer to the documentation for a list of valid configuration values. |
| Error -200511 | Requested an invalid configuration value for adjusting the main path pre-amplifier gain. Refer to the documentation for a list of valid configuration values. |
| Error -200512 | Requested an invalid configuration value for adjusting the main path post-amplifier gain and offset. Refer to the documentation for a list of valid configuration values. |
| Error -200513 | Requested an invalid configuration value for adjusting the main path output impedance. Refer to the documentation for a list of valid configuration values. |
| Error -200514 | Requested an invalid configuration value for adjusting the direct path output impedance. Refer to the documentation for a list of valid configuration values. |
| Error -200515 | Specified number of reads to average from the calibration ADC is invalid. The number of reads to average must be greater than 0. |
| Error -200516 | Calibration constants stored in the EEPROM produced an invalid value for the gain DAC. An incorrect calibration might have been performed, or the calibration data in the EEPROM might have been corrupted. Perform an external calibration, perform a self-calibration, or contact National Instruments Technical Support. |
| Error -200517 | Calibration constants stored in the EEPROM produced an invalid value for the offset DAC. An incorrect calibration might have been performed, or the calibration data in the EEPROM might have been corrupted. Perform an external calibration, or a self-calibration, or contact National Instruments Technical Support. |
| Error -200518 | Calibration constants stored in the EEPROM produced an invalid value for the oscillator phase DAC. An incorrect calibration might have been performed, or the calibration data in the EEPROM might have been corrupted. Perform an external calibration, perform a self-calibration, or contact National Instruments Technical Support. |
| Error -200519 | Calibration constants stored in the EEPROM produced an invalid value for the oscillator frequency DAC. An incorrect calibration might have been performed, or the calibration data in the EEPROM might have been corrupted. Perform an external calibration, or contact National Instruments Technical Support. |
| Error -200520 | Calibration constants stored in the EEPROM and used to adjust reads from the cal ADC are invalid. An incorrect calibration might have been performed, or the calibration data in the EEPROM might have been corrupted. Perform an external calibration, or contact National Instruments Technical Support. |
| Error -200521 | A measurement taken during adjustment of the oscillator phase DAC produced an invalid calibration constant. Make sure that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, and repeat the calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National Instruments Technical Support. |
| Error -200522 | A self-calibration cannot be performed during external calibration. |
| Error -200523 | Read cannot be performed because this version of DAQmx Read only returns data from a single channel, and there are multiple channels in the task. Use the multichannel version of DAQmx Read. |
| Error -200524 | Write cannot be performed, because the number of channels in the data does not match the number of channels in the task. When writing, supply data for all channels in the task. Alternatively, modify the task to contain the same number of channels as the data written. |
| Error -200525 | Read cannot be performed because this version of DAQmx Read does not match the type of channels in the task. Use the version of DAQmx Read that corresponds to the channel type. |
| Error -200526 | Write cannot be performed because this version of DAQmx Write does not match the type of channels in the task. Use the version of DAQmx Write that corresponds to the channel type. |
| Error -200527 | Requested values of the Minimum and Maximum properties for the counter channel are not supported for the given type of device. The values that can be specified for Minimum and Maximum depend on the counter timebase rate. |
| Error -200528 | Requested line grouping is invalid. Either choose one channel for all lines or one channel for each line as the line grouping. |
| Error -200529 | Unexpected identifier following the switch operation in the connection list. Switch operations must be separated by a comma inside the connection list. |
| Error -200530 | Unexpected identifier following the relay name in the relay list. Relay names must be separated by a comma inside the relay list. |
| Error -200531 | Relay name is not specified in the list entry. |
| Error -200532 | Unexpected identifier following switch channel name. |
| Error -200533 | Identifier found in the script is too long. Use identifiers with no more than 511 characters. |
| Error -200534 | Waveform name is too long. Use waveform names with no more than 511 characters. |
| Error -200535 | Specified value is larger than the maximum value supported for this property. |
| Error -200536 | Specified value is smaller than the minimum value supported for this property. |
| Error -200537 | Supplied forward and reverse coefficients yield inconsistent results when they are used for computations related to this property. In other words, using the result of the forward scale as input to the reverse scale does not yield the original data. Based on the forward coefficients, the value for the property is invalid. Supply forward and reverse coefficients that yield consistent results. |
| Error -200538 | Action requested is invalid. |
| Error -200539 | Device does not support analog writes with multiple samples per channel. To output multiple samples, call DAQmx Analog Single Sample Write multiple times. |
| Error -200540 | DAC Reference Voltage Value is not set. When the DAC Reference Voltage Source property for a channel is set to External, the DAC Reference Voltage Value property must be set. Set the DAC Reference Voltage Value property so the value matches the reference voltage source connected to your device. Alternatively, consider using the internal DAC reference voltage source available on the device. |
| Error -200541 | Last Self Calibration Date/Time has not been stored on the device by NI-DAQmx. Self-calibrate the board using NI-DAQmx. Alternatively, externally calibrate the board using NI-DAQmx, and then call DAQmx Restore Last External Calibration Constants. |
| Error -200542 | Last Self Calibration Temperature has not been stored on the device by NI-DAQmx. Self-calibrate the board using NI-DAQmx. Alternatively, externally calibrate the board using NI-DAQmx, and then call DAQmx Restore Last External Calibration Constants. |
| Error -200543 | Last External Calibration Date/Time has not been stored on the device by NI-DAQmx. Externally calibrate the board using NI-DAQmx. |
| Error -200544 | Last External Calibration Temperature has not been stored on the device by NI-DAQmx. Externally calibrate the board using NI-DAQmx. |
| Error -200545 | Self-calibration failed. The self-calibration date has not changed. Disconnect the device from external signals, as they might introduce noise. Externally calibrate the device to recalibrate the onboard voltage reference that is used for self-calibration. |
| Error -200546 | External calibration failed, and the external calibration data has not been changed. Make sure that the reference signal used for the calibration is stable and that the voltage matches the value specified to the calibration software. Disconnect the device from any external signals that might be introducing noise. |
| Error -200547 | DAQmx Write failed, because a previous DAQmx Write automatically configured the output buffer size. The buffer size is equal to the original number of samples written per channel, so no more data can be written prior to starting the task. Start the generation before the second DAQmx Write, or set Auto Start to true in all occurences of DAQmx Write. To incrementally write into the buffer prior to starting the task, call DAQmx Configure Output Buffer before the first DAQmx Write. |
| Error -200548 | Requested coupling type is only valid when the trigger source is an external trigger channel. |
| Error -200549 | Self-calibration constants are invalid. Perform a self-calibration. Contact National Instruments Technical Support if you need additional information. |
| Error -200550 | Hardware clocking error occurred. If you are using an external reference or sample clock, make sure it is connected and within the jitter and voltage level specifications. Also, verify that its rate matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200551 | Hardware clocking error occurred. If you are using an external reference or sample clock, make sure it is connected and within the jitter and voltage level specifications at all times. Also, verify that its rate matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200552 | Specified string is not valid, because it contains an invalid character. |
| Error -200553 | Specified string is not valid, because its first character is a space character. |
| Error -200554 | Specified string is not valid, because its last character is a space character. |
| Error -200555 | Specified string is not valid, because its first character is an underscore. |
| Error -200556 | You only can get the specified property while the task is committed or while the task is running. Commit or start the task prior to getting the property. |
| Error -200557 | Specified property cannot be set while the task is running. Set the property prior to starting the task, or stop the task prior to setting the property. |
| Error -200558 | One task cannot contain multiple independent devices. Create one task for each independent device. |
| Error -200559 | Task cannot contain a channel with the specified channel type, because the task already contains channels with a different channel type. Create one task for each channel type. |
| Error -200560 | Wait Until Done did not indicate that the task was done within the specified timeout. Increase the timeout, check the program, and make sure connections for external timing and triggering are in place. |
| Error -200561 | Attempted writing analog data that is too large or too small. Change Minimum Value and Maximum Value to reflect the range of the channel. |
| Error -200562 | Attempted writing digital data that is not supported. |
| Error -200563 | Specified digital channel contains more bits than supported by the 8-bit version of DAQmx Port Read. Use a version of DAQmx Port Read that supports wider digital ports. |
| Error -200564 | Specified digital channel contains more bits than supported by the 32-bit version of DAQmx Read. Use a version of DAQmx Read that returns an array of Boolean values or digital waveforms. |
| Error -200565 | Specified digital channel contains more bits than supported by the 8-bit version of DAQmx Port Write. Use the version of DAQmx Port Write that supports wider digital ports. |
| Error -200566 | Specified digital channel contains more bits than supported by the 32-bit version of DAQmx Port Write. |
| Error -200567 | Generation cannot be started, because the buffer size was changed since the last write, and this change caused data to be lost. Write data after changing the buffer size. |
| Error -200568 | Generation cannot be started, because the Regeneration Mode property was changed since the last write, and this change caused data to be lost. Write data after changing the Regeneration Mode property. |
| Error -200569 | Type of channel collection used to access the specified channel does not match the channel type. Access the channel through the channel collection that matches the channel type. |
| Error -200570 | Requested channel index is invalid. The value of the index must be between one and the number of channels in the task. |
| Error -200571 | Input Source Select property is set to an internal source for channels in different channel groups. On this device, only one channel group at a time can be configured to use an internal source. Refer to the documentation for details. |
| Error -200572 | Input Source Select property is set differently for channels in one channel group on a device that supports only identical settings within a channel group. Refer to the documentation for more details. |
| Error -200573 | Input Source Select property is set to different internal sources on some channels. On this device, Input Source Select must be set to the same value for all channels with internal sources. Refer to the documentation for more details. |
| Error -200574 | Driver cannot complete the route, because the only way to make the route requires a trigger bus line, and no trigger bus has been configured in MAX for this device. If you have a PXI chassis, make sure it has been properly identified in MAX. If you are using a PCI device, create a RTSI cable in MAX that includes your PCI device even if you are not using any RTSI cables. |
| Error -200575 | Requested value for Samples per Channel is too high when a reference trigger is used. In this case, Samples per Channel cannot exceed the sum of Pretrigger Samples per Channel and the maximum Post-trigger Samples per Channel. Reduce Samples per Channel. Alternatively, consider performing an acquisition with Continuous Sample Mode, or increase the Pretrigger Samples per Channel. |
| Error -200576 | CJC Source cannot be set to Built-In for the specified thermocouple channel. The physical channel does not support a built-in CJC temperature sensor. If your hardware contains a CJC temperature sensor on the physical channel corresponding to the built-in CJC source, make sure that the hardware configuration (including any accessories and/or terminal blocks) is correct. Alternatively, specify a different CJC Source, or use hardware with a built-in CJC temperature sensor. |
| Error -200577 | Requested AI Minimum value is too large. |
| Error -200578 | Requested AI Minimum value is too small. |
| Error -200579 | Requested AI Maximum value is too large. |
| Error -200580 | Requested AI Maximum value is too small. |
| Error -200581 | Specified property is not supported, because Reference Clock Source is "None". |
| Error -200582 | Values for AO channel properties lead to an output voltage that exceeds the maximum for the device. |
| Error -200583 | Values of the AO channel properties lead to an output voltage that is less than the minimum for the device. |
| Error -200584 | Write failed, because the number of samples to write per channel is invalid. The number of samples to write per channel must be an integer multiple of the samples to write per channel increment. |
| Error -200585 | Hardware clocking error occurred. If you are using an external sample clock, make sure it is connected and within specifications. If you are generating your sample clock internally, please contact National Instruments Technical Support. |
| Error -200586 | Hardware clocking error occurred. If you are using an external sample clock, make sure it is connected and within specifications. If you are generating your sample clock internally, please contact National Instruments Technical Support. |
| Error -200587 | Requested operation could not be performed, because the specified digital lines are either reserved or the device is not present in NI-DAQmx. It is possible that these lines are reserved by another task, the device is being used through the Traditional NI-DAQ interface, or the device is being reset. You might also get the error if the specified resource is currently in use by LabVIEW network variables bound to the DAQ Channel, or if the DAQ Channel is being used in any OPC Client software. If you are using these lines with another task, wait for the task to complete. If you are using the device through the Traditional NI-DAQ interface, and you want to use it with NI-DAQmx, reset (initialize) the device using the Traditional NI-DAQ interface. If you are resetting the device, wait for the reset to finish. |
| Error -200588 | Specified event handler cannot be removed, because it is installed on a different NI-DAQmx object. Remove the event handler from the NI-DAQmx object on which it was installed. |
| Error -200589 | Specified event handler cannot be removed, because it has already been removed. |
| Error -200590 | Specified event handler cannot be removed, because it is invalid. It has never been installed on this or any other NI-DAQmx object. |
| Error -200591 | Negative buffer size was supplied. The buffer size must be zero or greater. |
| Error -200592 | Given range in the input string contains too many objects. Check the string. If necessary, split the input string into smaller ranges. |
| Error -200593 | Value of this property cannot be determined until the containing task is verified. Before attempting to get the value of this property, you must make sure the task has been verified. You can do this by starting the task, using the task control method to verify the task, reading from the task if the Read Auto Start property is true, or writing to the task and specifying true for the auto start parameter. |
| Error -200594 | Value passed for the direction parameter is invalid. Use one of the values of the corresponding enumeration. |
| Error -200595 | Invalid identifier at the beginning of the switch operation in the list entry. |
| Error -200596 | Channels in the switch operation span different devices. |
| Error -200597 | Specified output operation cannot be satisfied, because it requires lines that are currently in use by another output operation. |
| Error -200598 | Repetition of a number in the Prescaled Values is invalid for input operations. |
| Error -200599 | Repetition of a number in Scaled Values is invalid for output operations. |
| Error -200600 | NI-DAQmx cannot generate virtual channel names for some of the physical channels specified, because the numeric suffix of the resulting channel names would be too large. Either explicitly specify a virtual channel name for each physical channel name, or decrease the numeric suffix of the last set of virtual channel names. |
| Error -200601 | Property not supported by this scale type. |
| Error -200602 | Prescaled Minimum cannot be equal to Prescaled Maximum for input operations. |
| Error -200603 | Scaled Minimum cannot be equal to Scaled Maximum for output operations. |
| Error -200604 | NULL pointer was passed for a required parameter. |
| Error -200605 | Given range in the input string contains a number that is too large. Check the string. Use smaller numbers in the range, or replace the range with a comma-separated list. |
| Error -200606 | Requested channel index is invalid. The value of the index must be between one and the number of channels in the task. |
| Error -200607 | Two signals cannot be simultaneously exported on the same terminal. |
| Error -200608 | Acquisition cannot be started, because the selected buffer size is too small. Increase the buffer size. |
| Error -200609 | Generation cannot be started, because the selected buffer size is too small. Increase the buffer size. |
| Error -200610 | Requested sample clock source is invalid for output. The specified sample clock source terminal is only supported for input. |
| Error -200611 | Operation cannot be performed, because there are no channels of the requested type in the task. |
| Error -200612 | Requested channel index is invalid. The value of the index must be between 0 and the number of channels in the task minus one. |
| Error -200613 | Acquisition has been stopped to prevent an input buffer overwrite. Your application was unable to read samples from the buffer fast enough to prevent new samples from overwriting unread data. To avoid this error, you can do any of the following: 1. Increase the size of the buffer. 2. Increase the number of samples you read each time you invoke a read operation. 3. Read samples more often. 4. Reduce the sample rate. 5. If your data transfer method is interrupts, try using DMA or USB Bulk. 6. Reduce the number of applications your computer is running concurrently. In addition, if you do not need to read every sample that is acquired, use the Relative To and Offset properties to read the desired samples. |
| Error -200614 | Combination of Samples to Read, Position, and Offset results in an attempt to read past the end of the record. You only can read samples within the record. |
| Error -200615 | Hardware clocking error occurred. If you are using an external sample clock, make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200616 | Specified asynchronous operation handle is invalid. |
| Error -200617 | Output generation was aborted by the reverse power protection circuitry of the device. Either the output signal exceeded the output power limit, or power was being driven back into the output of the device by an external source. Correct the problem, then generate the signal again. |
| Error -200618 | Analog input virtual channels cannot be created out of order with respect to their physical channel numbers for the type of analog device you are using. For example, a virtual channel using physical channel ai0 must be created before a virtual channel with physical channel ai1. |
| Error -200619 | Chassis cannot be used for more than one scanning operation at the same time. Do only one scanning operation, or combine multiple scanning operations into a single operation. |
| Error -200620 | Requested multiple virtual channels that correspond to the same analog input physical channel within a single task. A task cannot contain multiple analog input physical channels for this type of device. Use different physical channels for each virtual channel. |
| Error -200621 | Onboard device memory underflow. Because of system and/or bus-bandwidth limitations, the driver could not write data to the device fast enough to keep up with the device output rate. Reduce your sample rate. If your data transfer method is interrupts, try using DMA or USB Bulk. You can also reduce the number of programs your computer is executing concurrently. |
| Error -200622 | Requested number of samples to write is invalid. Change the number of samples to be written to a number equal to or greater than zero. |
| Error -200623 | Device has shut down because a sensor on the device detected a temperature above the device's maximum recommended operating temperature. To use the device again, either turn the chassis/computer off until the device has cooled, or ensure the device has cooled, and reset the device (either programmatically or through Measurements & Automation Explorer). |
| Error -200624 | You have not specified an active channel when getting a property. Specify a single line as the active physical channel. |
| Error -200625 | You have specified more than one line as the active physical channel when getting a property. Specify a single line. |
| Error -200626 | An empty physical channel has been specified within the power up states array. Specify a correct physical channel. |
| Error -200627 | Hardware clocking error occurred. If you are using an external sample clock, make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200628 | Pause and reference triggers are both configured, which is not supported in this task. |
| Error -200629 | Requested different values for properties that must have equal values on this device. |
| Error -200630 | Requested write offset is invalid, because it is not an integer multiple of the write increment. |
| Error -200631 | Hardware clocking error occurred. If you are using an external sample clock, make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200632 | Hardware clocking error occurred. If you are using an external sample clock, make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support. |
| Error -200633 | Script name is the same as an existing waveform name. Make sure that the script name is different from the names of previously written or allocated waveforms. |
| Error -200634 | Waveform name is the same as an existing script name. Make sure that the waveform name is different from the names of previously written scripts. |
| Error -200635 | You have attempted to control a Watchdog Task, but the task supplied was not a Watchdog Task. |
| Error -200636 | For this device, any connection specified in the scan list must wait for a trigger (;). If your scan list contains an action sequence similar to "ch0->com0 &" or "ch0->com0 &&", change the action sequence to "ch0->com0;". |
| Error -200637 | For this device, an action separator (& or &&) is required after breaking a connection in the scan list. If your scan list contains an action sequence similar to "~ch0->com0;", change the action sequence to "~ch0->com0 &" or "~ch0->com0 &&". |
| Error -200638 | For this device, two consecutive wait for triggers are not supported after any connection in the scan list. If your scan list contains an action sequence similar to "ch0->com0;;", change the action sequence to "ch0->com0;". |
| Error -200639 | For this device, connections specified in the scan list must be disconnected before making new connections. If your scanlist contains an action sequence similar to "ch0->com0;;", change the action sequence to "ch0->com0; ~ch0->com0". |
| Error -200640 | For this device, send advance complete (<sac>) is not supported after any wait for triggers (;) in the scan list. If your scan list contains an action sequence similar to "ch0->com0; <sac>", change the action sequence to "ch0->com0;". |
| Error -200641 | Property cannot be set separately for each line. When setting this property, specify a virtual channel as the active channel. |
| Error -200642 | You have not specified an active channel when getting a property. Specify a single line as the active channel. |
| Error -200643 | You have specified more than one line when getting a property. Specify a single line as the active channel. |
| Error -200644 | Attempt to reset watchdog timer failed, because the timer had already expired. Clear expiration of the watchdog timer, or configure a longer watchdog timer timeout. |
| Error -200645 | Attempt to set the digital filter interval failed, because another task has already configured a different digital filter interval. Use the same digital filter interval in the two tasks, or wait for the other task to finish before starting or committing this task. |
| Error -200646 | Some of the physical channels in the task are configured for different filter intervals, which is not supported by this type of device. Configure all lines in the task to use the same digital filter interval. |
| Error -200647 | Specified physical channel does not support digital input. Change the direction of the task, use another terminal, or use another device. To read from digital output lines, create a digital output task and use DAQmx Read. |
| Error -200648 | Device identifier of the physical channel specified is not the same as the device used in the task. Use only the physical channels on the device used in the task. |
| Error -200649 | Specified a physical channel for change detection that is not contained by any channel in the task. Use only physical channels already contained by a channel, or create an additional channel containing the desired physical channel . |
| Error -200650 | Attempt to set programmable powerup state failed, because the specified physical channel only supports digital input, and the programmable powerup state does not apply. |
| Error -200651 | Attempt to set watchdog timer expiration state failed, because the specified physical channel only supports digital input, and watchdog timer expiration state does not apply. |
| Error -200652 | Attempt to set programmable powerup state failed, because only some of the channels from the port were specified. For this type of device, you must specify programmable powerup state for entire ports. |
| Error -200653 | Attempt to set programmable powerup state failed, because some of the lines in a port were tristated and others were not. For this type of device, programmable powerup states of all lines in a port have to be either tristated or not tristated. |
| Error -200654 | Attempt to set watchdog timer expiration state failed, because some of the lines in a port were tristated, and others were not. For this type of device, watchdog timer expiration states of all lines in a port have to be either tristated or not tristated. |
| Error -200655 | Attempted to read more samples than what was configured in the acquisition. Restart the acquisition, increase the Samples Per Channel property, or set the Sample Mode property to Continuous Samples. |
| Error -200656 | Operation failed, because an attempt was made to use only the onboard memory for generation when regeneration of data was not allowed. Set the Regeneration Mode property to Allow Regeneration or set the Use Only Onboard Memory property to false. |
| Error -200657 | Attempt to get property failed, because you specified multiple channels, and the property has different values for different channels. Get this property one channel at a time. |
| Error -200658 | Attempt to get property failed, because your task contains multiple channels, and the property has different values for different channels. Get this property one channel at a time using Active Channel to specify each individual channel. |
| Error -200659 | Attempt to get property failed, because the single channel you specified corresponds to multiple physical channels, and the property has different values for those different physical channels. Get this property one physical channel at a time. For digital channels, you might have to specify a single digital line. |
| Error -200660 | Requested Sample Clock Rate is not available because this task shares the Sample Clock Source or the Sample Clock Timebase with another task. The other task has already programmed one of those properties in a manner inconsistent with the requested Sample Clock Rate. Specify a Sample Clock Rate consistent with the settings in the other task, or change the settings in the other task. Refer to documentation for more detailed information. |
| Error -200661 | Requested operation is not supported because the Reference Clock Source is "None". |
| Error -200662 | Attempt to create a watchdog timer task failed because the device does not support the feature, or the wrong device type was specified. For NI CompactDAQ devices supporting this feature, specify the chassis name on which to create a watchdog timer task. |
| Error -200663 | Attempt to set programmable powerup states failed because the device does not support the feature. |
| Error -200664 | Specified operation cannot be performed because the task has not been started, committed, or reserved. Call DAQmx Start or DAQmx Control with action set to Commit or Reserve prior to requesting this operation. |
| Error -200665 | Expiration states requested are not supported by the lines in the port. For this device, the Watchdog Timer Expiration States must be either No Change for all lines in a port or a combination of values other than No Change for all lines in a port. For example, the combination of No Change for one line and High for another line is not supported, while a value of Low for one line and High for another line is supported. |
| Error -200666 | Attempt to configure a port or any of its lines for input failed, because this port is currently configured for digital output by the watchdog timer. Choose another port, or modify the watchdog timer task to set the expiration state of the port to Tristate or No Change. |
| Error -200667 | Attempt to configure a port or any of its lines to have an expiration state of Output failed, because the port or some of its lines are currently reserved for use by an input task. Set the expiration state of the port to Tristate or No Change, or choose a different port for digital input. |
| Error -200668 | Requested value is not a supported value for Watchdog Timer Timeout. Use special value -1.0 to indicate that the internal timer should be disabled, and the watchdog timer will expire based on the external expiration trigger, or specify another valid value. |
| Error -200669 | Attempt to set the Connect DAC Reference to Ground property failed, because the Allow Connecting DAC Reference to Ground property was not True. To connect DAQ reference to ground, you must set two properties to True: Connect DAC Reference to Ground and Allow Connecting DAC Reference to Ground. |
| Error -200670 | DAC Range Low is not equal in magnitude and opposite in sign from DAC Reference Value. If you do not set the DAC Range Low property, the driver sets it for you. Otherwise, ensure DAC Range Low and DAC Reference Voltage Value are equal in magnitude and opposite in sign. |
| Error -200671 | Switch device has been disabled to prevent it from exceeding its simultaneous relay drive limit. To recover, call DAQmx Disconnect All, or reset the device. The device can be reset either programmatically or by using Measurement & Automation Explorer. |
| Error -200672 | Input arrays are of different sizes. These arrays must have the same size. |
| Error -200673 | Multiple samples cannot be written using a single sample write. Ensure the waveform contains only a single sample. |
| Error -200674 | Switch operation failed due to a previous error. The device may have been powered off and back on. To use the device again, reset the device either programmatically or by using Measurement & Automation Explorer. |
| Error -200675 | Input Source Select is set to an internal source for channels in different channel groups. On this device, only one channel group at a time can be configured to use an internal source. Refer to documentation for details. |
| Error -200676 | Input Source Select property is set differently for channels in one channel group on a device that supports only identical settings within a channel group. Refer to documentation for details. |
| Error -200677 | Input Source Select property is set to different internal sources on some channels. On this device, Input Source Select must be set the same way for all channels with internal sources. Refer to documentation for details. |
| Error -200678 | Write failed because at least one of the lines in the task is also in a watchdog timer task whose watchdog timer has expired. Clear the expiration of the watchdog timer before writing by using DAQmx Control Watchdog Task, by restarting the watchdog timer task, or by resetting the device programmatically or through the Measurements & Automation Explorer. To prevent this error in the future reset the watchdog timer more frequently or increase the watchdog timer timeout. |
| Error -200679 | When Sample Mode is Hardware Timed Single Point, Memory Mapping for Programmed IO Enable cannot be true. Set Memory Mapping for Programmed IO Enable to false or change Sample Mode. |
| Error -200680 | Device has shut down because a sensor on the device detected a temperature above the device's maximum recommended operating temperature. To use the device again, either turn the chassis/computer off until the device has cooled, or ensure the device has cooled, and reset the device (either programmatically or through Measurements & Automation Explorer). |
| Error -200681 | Route failed because either the source or destination of the route is also a line in a watchdog timer task whose watchdog timer has expired. Clear the expiration of the watchdog timer before routing by using DAQmx Control Watchdog Task, by restarting the watchdog timer task, or by resetting the device programmatically or through Measurements & Automation Explorer. To prevent this error in the future reset the watchdog timer more frequently or increase the watchdog timer timeout. |
| Error -200682 | Data could not be read because the reference trigger master session is unavailable. To avoid this error, read data before closing the reference trigger master session. |
| Error -200683 | NI-DAQmx has detected a corrupt installation. Please re-install NI-DAQmx. If you continue to receive this message, please contact National Instruments for assistance. |
| Error -200684 | Pulse duty cycle specified is not supported for this device given the pulse frequency and Counter Timebase Rate. |
| Error -200685 | Pulse frequency specified is not supported for this device given the Counter Timebase Rate. |
| Error -200686 | Pulse high time specified is not supported for this device given the Counter Timebase Rate. |
| Error -200687 | Pulse low time specified is not supported for this device given the Counter Timebase Rate. |
| Error -200688 | Pulse high tick count specified is not supported for this device. |
| Error -200689 | Pulse low tick count specified is not supported for this device. |
| Error -200690 | Buffered operations are not supported if Sample Mode is Hardware Timed Single Point. Do not configure a buffer, or change the Sample Mode value. |
| Error -200691 | Buffered operations are not compatible with the requested Wait Mode. Do not configure a buffer, or set Wait Mode to Yield. |
| Error -200692 | Number of samples per channel to write multiplied by the number of channels in the task cannot be an odd number for this device. Adjust the number of samples per channel to write or the number of channels in the task so that their product is an integer multiple of two. |
| Error -200693 | Buffer size (in samples per channel) multiplied by the number of channels in the task cannot be an odd number for this device. Adjust the buffer size or the number of channels in the task so that their product is an integer multiple of two. |
| Error -200694 | AI Minimum was not specified for an operation that requires it. |
| Error -200695 | AI Maximum was not specified for an operation that requires it. |
| Error -200696 | Bridge offset nulling calibration is not supported by the specified channels. Specify only the analog input channels that are configured to measure sensors in a bridge configuration. |
| Error -200697 | Calibration data could not be acquired. Ensure that the device(s) are configured and functioning properly. |
| Error -200698 | Route failed because the PXI chassis is not identified. The existence of the source terminal depends on the chassis being identified. Use the Measurements & Automation Explorer (MAX) to identify your chassis. |
| Error -200699 | Route failed because the PXI chassis is not identified. The existence of the destination terminal depends on the chassis being identified. Use the Measurements & Automation Explorer (MAX) to identify your chassis. |
| Error -200700 | PXI_Star is not available as a source terminal for devices in PXI slot 2. PXI slot 2 has specific PXI_Star<n> lines, such as PXI_Star3. Move your device to one of slots 3 through 15, or select a different source terminal. |
| Error -200701 | PXI_Star is not available as a destination terminal for devices in PXI slot 2. PXI slot 2 has specific PXI_Star<n> lines, such as PXI_Star3. Move your device to one of slots 3 through 15, or select a different destination terminal. |
| Error -200702 | PXI_Star is not available as a destination terminal for devices in PXI slots 16 and above. Move your device to one of slots 3 through 15, or select a different destination terminal. |
| Error -200703 | PXI_Star is not available as a source terminal for devices in PXI slots 16 and above. Move your device to one of slots 3 through 15, or select a different source terminal. |
| Error -200704 | PXI_Star<n> is available as a source terminal only for devices in the star trigger controller slot (slot 2). To use PXI_Star (without any numbers), do not specify a star line number. To use PXI_Star<n>, move your device to slot 2. |
| Error -200705 | PXI_Star<n> is available as a destination terminal only for devices in the star trigger controller slot (slot 2). To use PXI_Star (without any numbers), do not specify a star line number. To use PXI_Star<n>, move your device to slot 2. |
| Error -200706 | PXI_Clk10In is available as a destination terminal only for devices in the star trigger controller slot (slot 2). Move your device to PXI slot 2. |
| Error -200708 | Getting a property that pertains to multiple items failed because the value was different for different items. Get the specified property for one item at a time. For example, if you are getting a property for two markers, such as "marker0:1" or "marker0, marker1", and the property values are different for the two markers, you must get them in two steps (one for marker0 and another for marker1). |
| Error -200709 | No TEDS sensor was detected on the specified physical channel. Ensure that your sensor is properly connected. If the sensor is connected to a TEDS interface device with addresses, make sure the configured address matches the address set on the interface device. |
| Error -200710 | Input Source Select property is set to an internal source with more than one channel in the task. On this device, an internal input source is supported only when there is one channel in the task. Remove all of the channels currently in the task except the channel that will be used to acquire the internal input source. |
| Error -200711 | An attempt has been made to use an analog trigger with the Input Source Select property set to an internal source. Either change the Input Source Select property ot specify an external source, or use a different analog trigger source. |
| Error -200712 | Digital input configuration failed because at least one of the lines in the task was in an expired watchdog task, and the expiration state of the line was set to output. Clear the expiration of the watchdog task by using DAQmx Control Task, by restarting the watchdog task, or by resetting the device either programmatically or by using Measurement & Automation Explorer. To prevent this error in the future, reset the watchdog timer more frequently or increase the watchdog timer timeout. |
| Error -200713 | Channels specified cannot appear in the same task on this device. Create a separate task for each of the channels specified. |
| Error -200714 | Acquisition has stopped because the driver could not transfer the data from the device to the computer memory fast enough. This was caused by computer system limitations. Reduce your sample clock rate, the number of channels in the task, or the number of programs your computer is executing concurrently. |
| Error -200715 | Digital input detected a new sample clock before the previous sample was latched into onboard memory. If you are using an external sample clock, ensure that it is connected, within the jitter and voltage level specifications, and without glitches. If applicable, reduce your sample clock rate or use a product capable of higher sample clock rates. |
| Error -200716 | Digital output detected a new sample clock edge before the previous sample could be written from the onboard memory. If you are using an external sample clock, ensure that it is connected, within jitter and voltage level specifications, and without glitches. If applicable, reduce your sample clock rate or use a product capable of higher sample clock rates. |
| Error -200717 | Measurement taken during calibration produced an invalid AI offset calibration constant. If performing an external calibration, ensure that the reference voltage value passed to the calibration VI or function is correct. Repeat the calibration. If the error persists, contact National Instruments Technical Support. |
| Error -200718 | Measurement taken during calibration produced an invalid AI gain calibration constant. If performing an external calibration, ensure that the reference voltage value passed to the calibration VI or function is correct. Repeat the calibration. If the error persists, contact National Instruments Technical Support. |
| Error -200719 | Measurement taken during calibration produced an invalid AO offset calibration constant. If performing an external calibration, ensure that the reference voltage value passed to the calibration VI or function is correct. Repeat the calibration. If the error persists, contact National Instruments Technical Support. |
| Error -200720 | Measurement taken during calibration produced an invalid AO gain calibration constant. If performing an external calibration, ensure that the reference voltage passed to the calibration VI or function is correct. Repeat the calibration. If the error persists, contact National Instruments Technical Support. |
| Error -200721 | Computed frequency resolution of the VCXO CalDAC circuitry is not sufficient to perform timebase calibration. Ensure that the reference frequency is stable and that the frequency passed to the calibration VI or function is correct. Repeat the external timebase calibration. If the error persists, contact National Instruments Technical Support. |
| Error -200722 | Timebase calibration algorithm failed to converge within the required tolerance. Ensure that the reference frequency is stable and that the frequency passed to the calibration VI or function is correct. Repeat the external timebase calibration. If the error persists, contact National Instruments Technical Support. |
| Error -200723 | Variance of the measured external reference frequency is too large to perform timebase calibration. Ensure that the reference frequency is stable. Repeat the external timebase calibration. If the error persists, contact National Instruments Technical Support. |
| Error -200724 | Digital Input Tristate property has different values for different channels in the task, which is not supported for this type of device. Change the property to a single value for all channels in the task, or use more than one task. |
| Error -200725 | Some or all of the lines in the task are used by another task for handshaking input. These lines cannot be used in a static input task. Use a line that is not in a handshaking input task or stop using the line in the handshaking input task. |
| Error -200726 | Some or all of the lines in the task are used by another task for static input. These lines cannot be used in a handshaking input task. Use a port that is not already used by a static input task or stop using the line in the static input task. |
| Error -200727 | Some or all of the lines in the task are used by another task for handshaking control. These lines cannot be used in a static input task. Use a line that is not also a control line in a handshaking task, or stop using the line for handshaking control. |
| Error -200728 | Some or all of the handshaking control lines for this task are used by another task for static input. These lines cannot be used for handshaking control. Use a port whose handshaking control lines are not already used by a static input task or stop using the lines for handshaking control. |
| Error -200729 | Value of the Tristate property for some or all of the channels in the task is False, and Sample Timing Type is Handshake, which is not supported by this device. Set the Tristate property to True for all channels or change the Sample Timing Type. |
| Error -200730 | Value of Tristate property for some or all of the channels in the task is False, and Sample Timing Type is Change Detection, which is not supported by this device. Set the Tristate property to True for all channels or change the Sample Timing Type. |
| Error -200731 | Sample Mode is Hardware Timed, and Sample Timing Type is On Demand, which is not supported by this device. Change Sample Mode or Sample Timing Type. |
| Error -200732 | Some of all of the lines in the task have had their Digital Filter Enable property set, which is not supported when the value of the Tristate property is False. Change the value of the Tristate property, or do not set the Digital Filter Enable property. |
| Error -200733 | Some or all of the lines in the task have ahd their Digital Filter Minimum Pulse Width property set, which is not supported when the value of the Tristate property is False. Change the value of the Tristate property, or do not set the Digital Filter Minimum Pulse Width property. |
| Error -200734 | Device does not support DMA for the Data Transfer Mechanism when performing non-buffered acquisitions. Set Data Transfer Mechanism to Programmed I/O. |
| Error -200735 | Given the specified Reference Clock Source, you must set the Reference Clock Rate to a value equal to the frequency of the supplied signal. |
| Error -200736 | FREQOUT counter cannot generate the desired frequency. The FREQOUT counter is a 4-bit counter that can divide either the 10 MHz Timebase or the 100 kHz Timebase by a number between one and sixteen. Chose a frequency within this range. |
| Error -200737 | For this type of device, the Input Buffer Size (in Samples per Channel) must be equal to the value of the Sample Quanity-Samples per Channel property when Sample Mode is Finite Samples. |
| Error -200738 | Specified timing source does not exist. |
| Error -200739 | Specified property is not supported for the given timing source. |
| Error -200740 | Task used as the timing source for a Timed Loop was started before the Timed Loop was executed. Let the Timed Loop start the task, or use the task without the Timed Loop. |
| Error -200741 | A TEDS sensor not supported by DAQmx is connected to the specified physical channel. Consider using MAX to create a Task, a Global Channel, or a Scale to acquire data using this sensor. |
| Error -200742 | Memory of the TEDS sensor connected to the specified physical channel is corrupted, as indicated by an invalid check-sum. Replace the sensor or have the sensor repaired. If the memory is the only defective part of the sensor, consider using MAX to create a Task, a Global Channel, or a Scale to acquire data using this sensor. |
| Error -200743 | For this device, a TEDS terminal block must be connected to the device and configured in MAX in order to perform a TEDS operation. |
| Error -200744 | Specified reference clock rate does not match the specified reference clock source. Do not set the refererence clock rate when you are using an internal reference clock source. In this case, the driver sets the reference clock rate for you. |
| Error -200745 | Frequency and Initial Delay property values are inconsistent with one or more counter timebase properties. The conflicting properties must satisfy the following constraints: Counter Timebase Rate / Counter Maximum Count <= Frequency <= Counter Timebase Rate / 4 Counter Timebase Rate / Counter Maximum Count <= 1 / Initial Delay <= Counter Timebase Rate / 2 If the Counter Timebase Rate is not specified, it is inferred from the Counter Timebase Source selection. |
| Error -200746 | Initial Delay, High Time, and Low Time property values are inconsistent with one or more counter timebase properties. The conflicting properties must satisfy the following constraints: 2 / Counter Timebase Rate <= Initial Delay <= Counter Maximum Count / Counter Timebase Rate 2 / Counter Timebase Rate <= High Time <= Counter Maximum Count / Counter Timebase Rate 2 / Counter Timebase Rate <= Low Time <= Counter Maximum Count / Counter Timebase Rate If the Counter Timebase Rate is not specified, it is inferred from the Counter Timebase Source selection. |
| Error -200747 | Acquisition type specified is not supported by the FREQOUT channel. To use the FREQOUT channel, set the acquisition type to a value supported by FREQOUT. To use specified output type, use a different counter output channel. |
| Error -200748 | DAQmx Write was invoked more than once between two consecutive sample clocks. When Sample Mode is Hardware Timed Single Point, invoke DAQmx Write only once between two consecutive sample clocks. |
| Error -200749 | Specified gain is not supported. |
| Error -200750 | Specified voltage is invalid for the given gain. |
| Error -200751 | Sample Timing Type was set to Change Detection but no physical channels on which to detect changes were specified. Specify the Change Detection Digital Input Rising and/or Falling Edge Physical Channels, or specify a different Sample Timing Type. |
| Error -200752 | You have specified more than one physical channel as the active channel which is not supported. Specify a single physical channel. |
| Error -200753 | TEDS sensor data or the Virtual TEDS data file contains an error which was detected during parsing. Ensure your TEDS sensor or Virtual TEDS data file conforms to the specification. If this is not possible, use custom scales with the sensor. |
| Error -200754 | TEDS template specifies parameters that are not supported by DAQmx. Use custom scales with this sensor. |
| Error -200755 | TEDS sensor data or Virtual TEDS data file contains multiple calibration templates. Only one calibration template is supported by DAQmx. Use custom scales with this sensor. |
| Error -200756 | Type of TEDS sensor associated with the channel is incompatible with the Measurement Type. Use the TEDS sensor for measurements compatible with the sensor. |
| Error -200757 | Sample Timing Type is set to On Demand which is not supported for analog input on this device. Set Sample Timing Type to Sample Clock. You can achieve this whlie setting related properties through DAQmx VIs or functions for configuring timing. |
| Error -200758 | Sample Timing Type is set to On Demand which is not supported for analog output on this device. Set Sample Timing Type to Sample Clock. You can achieve this while setting related properties through DAQmx VIs or functions for configuring timing. |
| Error -200759 | Range specified by the AO Maximum and Minimum Value, and AO Voltage Units properties does not lie within the range specified by the AO DAC Range High and Low properties. Change the values of these properties. If you do not specify AO DAC Range High and Low, the driver will set them based on other properties. |
| Error -200760 | Range specified by the AO Maximum and Minimum Value, and AO Voltage Units properties does not lie within the range specified by the AO Gain property. Change the values of these properties. If you do not specify AO Gain, the driver will set it based on other properties. |
| Error -200761 | Task cannot issue sync pulse because another task is currently running on this device. For this type of device, the task can issue a sync pulse if it is the only task running on the device. If your task is not being used for synchronization, set the Sync Pulse Source property to "" or "None" to avoid receiving an error. |
| Error -200762 | Task cannot issue sync pulse because the task has an external sample clock timebase. For this type of device, the task can issue a sync pulse if the Sample Clock Timebase Source is Onboard Clock. |
| Error -200763 | For analog input with the current Data Transfer Mechanism on this type of device, the input buffer size (in samples per channel) must be an integer multiple of the transfer size. Change the Data Transfer Mechanism or the input buffer size. |
| Error -200764 | TEDS sensor connected to the specified physical channel uses a linear mapping method and specifies the linear slope to be zero. Replace the sensor or have the sensor repaired. If the memory is the only defective part of the sensor, consider using MAX to create a Task, Global Channel, or a Scale to acquire data using this sensor. |
| Error -200765 | Mapping method of the TEDS sensor connected to the specified physical channel is invalid or is not supported by the driver. If the sensor is defective, replace it or have it repaired. Otherwise, consider using MAX to create a Task, Global Channel, or a Scale to acquire data using this sensor. |
| Error -200766 | Legacy template ID of the TEDS sensor connected to the specified physical channel is invalid or is not supported by the driver. If the sensor is defective, replace it or have it repaired. Otherwise, consider using MAX to create a Task, Global Channel, or a Scale to acquire data using this sensor. |
| Error -200767 | Data Transfer Mechanism is set to Programmed I/O which is not supported for buffered analog output. Change Data Transfer Mechanism or use non-buffered analog output. |
| Error -200768 | Data Transfer Mechanism is not set to Programmed I/O, the only value supported for non-buffered analog output. Set your Data Transfer Mechanism to Programmed I/O or use buffered analog output. |
| Error -200769 | Data Transfer Mechanism is not set to Programmed I/O, the only value supported when the Sample Mode is Hardware Timed Single Point. Set your Data Transfer Mechanism to Programmed I/O or change the Sample Mode. |
| Error -200770 | Digital Filter Enable and Digital Synchronization Enable properties cannot be true at the same time. |
| Error -200771 | Digital Filter Enable is set to true but the Minimum Pulse Width property is not configured. Configure the Minimum Pulse Width property or set Digital Filter Enable to false. |
| Error -200772 | Digital filtering is not available for the given terminal. |
| Error -200773 | Digital synchronization is not available for the given terminal. |
| Error -200774 | Terminal has already been configured with a different Minimum Pulse Width by another property in this task. |
| Error -200775 | Terminal has already been configured with a different Minimum Pulse Width by another task. |
| Error -200776 | Desired Minimum Pulse Width could not be produced. Minimum Pulse Width is affected by the Digital Filter Timebase Source and the Digital Filter Timebase Rate. To see how these two property settings can affect the Minimum Pulse Width, refer to product documentation for more details. |
| Error -200777 | Desired Minimum Pulse Width could not be produced by the device. |
| Error -200778 | Sample Mode is set to a value other than Hardware Timed Single Point. This is the only value supported for counter generations when Sample Timing Type is set to Sample Clock. Change the Sample Mode or the Sample Timing Type. |
| Error -200779 | Reverse Coefficients for a polynomial scale are not specified. This set of coefficients must contain at least one term. The polynomial scale class constructor has overloads that can calculate the Reverse Coefficients from the Forward Coefficients if only one set of coefficients is available. |
| Error -200780 | Forward Coefficients for a polynomial scale are not specified. This set of coefficients must contain at least one term. The polynomial scale class constructor has overloads that can calculate the Reverse Coefficients from the Forward Coefficients if only one set of coefficients is available. |
| Error -200781 | Forward and Reverse Coefficients for a polynomial scale are not specified. Each of these two sets of coefficients must contain at least one term. The polynomial scale class constructor has overloads that can calculate one set of coefficients from the other set if only one set is available. |
| Error -200782 | Reverse Coefficients for a polynomial scale are not specified. This set of coefficients must contain at least one term. |
| Error -200783 | Forward Coefficients for a polynomial scale are not specified. This set of coefficients must contain at least one term. |
| Error -200784 | Virtual TEDS file could not be found at the specified location. Specify correct location for the Virtual TEDS file. |
| Error -200785 | Timing source created is invalid because of the Sample Timing Type settings. To use this timing source with a Timed Loop, set the Sample Timing Type to Change Detection. You can configure the Sample Timing Type to Change Detection while setting related properties through the DAQmx Timing (Change Detection) VI or function. |
| Error -200786 | Requested Sample Clock Rate cannot be generated given the specified external Sample Clock Timebase Rate. To keep the specified Sample Clock Timebase Rate, use one of the Sample Clock Rates that can be generated. |
| Error -200787 | Specified Start Trigger Type is not supported for counter output tasks when the Sample Mode is Hardware Timed Single Point on this type of device. Set the Start Trigger Type to None to use this Sample Mode. |
| Error -200788 | Measured bridge offset is outside the limits allowed for offset nulling calibration for this device. Ensure your sensor is wired and functioning properly, and that its output offset is within device limits. |
| Error -200789 | Read cannot be performed because this version of DAQmx Read uses a data type that is too small for the channels in this task. Use a different version of DAQmx Read. |
| Error -200790 | Write cannot be performed because this version of DAQmx Write uses a data type that is too small for the channels in this task. Use a different version of DAQmx Write. |
| Error -200791 | TEDS cannot be configured for the specified channel. Ensure that your TEDS sensor is connected to the channel through a TEDS interface (for example BNC-2096, SC-2350, or SCXI-1314T), and that this interface is configured in MAX. Alternatively a virtual TEDS file can be used. |
| Error -200792 | You have specified more than one physical channel which is not supported. Specify a single physical channel. |
| Error -200793 | For a device of this type, setting the AO Idle Output Behavior to Maintain Existing Value is not supported when analog output is synchronized. |
| Error -200794 | You cannot use DAQmx Write for multiple counter channels within one task. If appropriate, create one task per counter output channel. To update multiple counter channels within one task use counter output properties. |
| Error -200795 | There was an overflow of the device onboard memory while performing a hardware timed non-buffered generation. Write only one sample per channel between two consecutive sample clocks to avoid this condition. |
| Error -200796 | Hardware timed non-buffered analog output could not be performed because Memory Mapping for Programmed I/O Enable was set to true. Disable memory mapping for hardware timed non-buffered analog output. |
| Error -200797 | An empty string was specified as a terminal name which is not supported. Specify a valid terminal name. |
| Error -200798 | Device does not support change detection for lines that do not allow digital input. Use lines that allow digital input for change detection. |
| Error -200799 | DAQmx Create Timing Source created an invalid source because the specified Sample Mode is not supported when the signal is Event Counting. To use this timing source with a Timed Loop, change the Sample Mode. |
| Error -200800 | Event source signal specified is not supported with the Measurement Type and/or Sample Timing Type of the task. |
| Error -200801 | DAQmx Create Timing Source created an invalid source because the requested signal is not supported for counter output. To use this task as the timing source with a Timed Loop, specify the Counter Output Event as the signal. |
| Error -200802 | Write cannot be performed when the task is not started, the sample timing type is something other than On Demand, and the output buffer size is zero. Call DAQmx Start before DAQmx Write, set auto start to true on DAQmx Write, modify the sample timing type, or change the output buffer size. |
| Error -200803 | Write cannot be performed before you start the task for on demand or hardware-timed single-point operations. Start the task before you write samples, set the autostart input on DAQmx Write to true, or use hardware timing with a sample mode of finite or continuous. |
| Error -200804 | Last External Calibration Date/Time is not available, because the last external calibration if the device was not performed using the NI-DAQmx API. Last External Calibration Date/Time will become available after you perform external calibration of the device using the NI-DAQmx API. |
| Error -200806 | Requested Minimum Pulse Width cannot be applied because the programmable filter clock has already been configured with a different Minimum Pulse Width by another task. For this type of device, there is only one programmable filter clock per device. |
| Error -200807 | Requested Minimum Pulse Width cannot be applied because the programmable filter clock has already been configured with a different Minimum Pulse Width when a different terminal was configured by the same task. For this type of device, there is only one programmable filter clock per device, and the device can use only one external timebase filter at a time. |
| Error -200808 | TEDS sensors cannot be configured on real-time (RT) systems. Use MAX to configure the TEDS sensor instead. |
| Error -200809 | TEDS sensors cannot be cleared on real-time (RT) systems. |
| Error -200810 | Requested string contains characters that cannot be interpreted by DAQmx due to installed language support and system locale settings. Ensure that the appropriate language support is installed on the system, and that the system locale is set correctly. For most Windows operating systems, this is done through the Regional Settings option in Control Panel. For a LabVIEW RT target, you should install "Language Support for LabVIEW RT" and change the locale setting for the remote system under the "System Settings" tab in MAX. |
| Error -200811 | Specified string contains characters that cannot be interpreted by DAQmx due to installed language support and system locale settings. If possible, do not use this character. Otherwise, ensure that the appropriate language support is installed on the system, and that the system locale is set correctly. For most Windows operating systems, this is done through the Regional Settings option in the Control Panel. For a LabVIEW RT target, you should install "Language Support for LabVIEW RT" and change the locale setting for the remote system under the "System Setting" tab in MAX. |
| Error -200812 | An attempt has been made to configure a trigger when analog output Sample Mode was set to Hardware Timed Single Point. Configure the analog output sample mode to something other than Hardware Timed Single Point to use a trigger. |
| Error -200813 | Selected Sample Mode is not supported with counter input position measurements. |
| Error -200814 | Onboard Clock is not supported as an Input Terminal for counter measurements. Refer to user documentation for a list of supported input terminals. |
| Error -200815 | TEDS sensor specifies a value for the Minimum Physical Value that is greater than or equal to the Maximum Physical Value. Replace the sensor or have the sensor repaired. If the memory is the only defective part of the sensor, consider using MAX to create a Task, a Global Channel, or a Scale to acquire data using this sensor. |
| Error -200816 | TEDS sensor specifies a value for the Minimum Electrical Value that is greater than or equal to the Maximum Electrical Value. Replace the sensor or have the sensor repaired. If the memory is the only defective part of the sensor, consider using MAX to create a Task, a Global Channel, or a Scale to acquire data using this sensor. |
| Error -200817 | Excitation Value can only be zero when the Input Terminal Configuration is set to Differential on this device. Change the Input Terminal Configuration or set the Excitation Value to zero. |
| Error -200818 | Device has shut down because a sensor on the device detected a temperature in excess of the maximum recommended operating temperature. Possible causes incude excessive current on the device channels and inadequate chassis cooling. To use the device again, reduce the current and/or improve the chassis cooling. Ensure that the device has cooled and reset the device (either programmatically or through Measurements & Automation Explorer). |
| Error -200819 | Programmed I/O is not supported as the Data Transfer Mechanism when the Use Only On Board Memory property is set to true. Change the Data Transfer Mechanism or set Use Only On Board Memory to false. |
| Error -200820 | Sample Mode of Hardware Timed Single Point is not supported for analog input channels on this type of device when the number of channels in the task is odd (not divisible by 2). Add a channel to the task, remove a channel from the task, or use a different Sample Mode. |
| Error -200821 | Sample Mode of Hardware Timed Single Point is not supported for analog input channels on this type of device. Use a different Sample Mode, or select a device which supports Hardware Timed Single Point. |
| Error -200822 | Attempt to write to the PROM on the TEDS failed because the TEDS sensor does not contain a PROM. Write the Basic TEDS data to the EEPROM of the sensor or replace the sensor. |
| Error -200823 | Attempt to write to the PROM on the TEDS sensor failed because the PROM has already been written and it cannot be rewritten. Do not write the Basic TEDS data to the TEDS sensor or replace the sensor. |
| Error -200824 | Attempt to write the Basic TEDS data to the EEPROM failed because the PROM on the TEDS sensor already contains Basic TEDS data. A TEDS sensor can contain the Basic TEDS data in either the PROM or the EEPROM, but not in both. Do not write the Basic TEDS data to the TEDS sensor or replace the sensor. |
| Error -200825 | Write failed because the data size is greater than the size of the EEPROM on the TEDS sensor. Make sure the data size does not exceed the EEPROM size. |
| Error -200826 | TEDS sensor data being written to the TEDS sensor contains an error. Ensure your TEDS sensor data conforms to the specification. |
| Error -200827 | Virtual TEDS data file being written to the TEDS sensor contains an error. Ensure your Virtual TEDS data file conforms to the specification. |
| Error -200828 | Writing to TEDS sensors is not supported on real-time (RT) systems. |
| Error -200829 | DAQmx Write failed because the counter channels have different Output Types. Writes to multiple counter output channels are supported only when all of the counters have identical Output Types. Use identical Output Types for all channels. Alternatively, create multiple tasks (one for each Output Type). |
| Error -200830 | On Demand Simultaneous Analog Output Enable and Memory Mapping for Programmed IO Enable cannot both be set to true for this device. |
| Error -200832 | DAQmx Read is not supported if the Sample Timing Type is On Demand, the Auto Start property is false, and the task is not running. Start the task before reading samples by calling DAQmx Start Task, set the Read.Auto Start property to true, or change the Sample Timing Type. |
| Error -200833 | DAQmx Read is not supported if the Sample Mode is Hardware Timed Single Point, the Auto Start property is false, and the task is not running. Start the task before reading samples by calling DAQmx Start Task, set the Read.Auto Start property to true, or change the Sample Mode. |
| Error -200834 | DAQmx Read is not supported for non-buffered acquisitions if the Auto Start property is false and the task is not running. Start the task before reading samples by calling DAQmx Start Task, set the Read.Auto Start property to true, or call DAQmx Configure Input Buffer with a buffer size greater than zero. |
| Error -200835 | SCXI device cannot be used in this task because the power to the device was turned off after the task had been created. Call DAQmx Clear Task and then create a new task to use this SCXI device. |
| Error -200836 | Attempt to write to the TEDS sensor failed, possibly because the sensor is not connected properly or because the sensor is defective. Make sure the TEDS sensor is properly connected. Write to the TEDS sensor again. If the write fails again, try using another TEDS sensor. You may need to have the original TEDS sensor repaired. |
| Error -200837 | Samples per Channel must be an integer multiple of the transfer size for this device with the current Data Transfer Mechanism. Change Samples per Channel or the Data Transfer Mechanism. |
| Error -200838 | Output buffer size (in samples per channel) must be an integer multiple of the transfer size for this device with the current Data Transfer Mechanism. Change the output buffer size or the Data Transfer Mechanism. |
| Error -200839 | Tristate property cannot be set to False for any channel in the task when Sample Timing Type is Sample Clock on this device. Set the Tristate property to True for all channels or change the Sample Timing Type. |
| Error -200840 | Prescaler value requested is not supported by this device, given the requested Timebase Source. Set Prescaler to 1, or change the Timebase Source. |
| Error -200841 | Prescaler value requested is not supported by this device, given the requested Input Terminal. Set Prescaler to 1, or change the Input Terminal. |
| Error -200842 | Data Transfer Mechanism is not set to Programmed I/O, the only value supported when the Sample Mode is Hardware Timed Single Point. Set your Data Transfer Mechanism to Programmed I/O or change the Sample Mode. |
| Error -200843 | DAQmx Read did not complete before the arrival of three sample clocks which indicates that your program is not keeping up with the hardware clock. Slow down the hardware clock or else change your application so that it can keep up with the hardware clock. |
| Error -200844 | Task contains a 'freqout' counter channel, which cannot be updated while the task is running. Create separate tasks for the 'freqout' channel and the other counter channels if you wish to write to the other counter channels. Alternatively, stop the task, reprogram the counters, and restart the task. |
| Error -200845 | Data Transfer Mechanism is not set to Programmed I/O or DMA, the only values supported for non-buffered operations for this device and Channel Type. Set your Data Transfer Mechanism to Programmed I/O or DMA, or use buffering. |
| Error -200846 | Write cannot be performed when the auto start input to DAQmx Write is false, task is not running, and timing for the task is not configured or Timing Type is set to On Demand. Set auto start to true, start the task, or configure timing and specify Timing Type other than On Demand. |
| Error -200847 | Data Transfer Mechanism is set to Programmed I/O, which is not supported for buffered operations for this device and Channel Type. Change Data Transfer Mechanism or do not use buffering. |
| Error -200848 | DAQmx Every N Samples Event is not supported within non-buffered tasks. To receive Every N Samples Event notifications, configure your task to use buffering. |
| Error -200849 | Number of samples to wait in a finite wait instruction must be a multiple of the alignment quantum. |
| Error -200850 | Number of samples to wait in a finite wait instruction must be greater than 0. |
| Error -200851 | Physical channel specified is not available through the cabled device connector used for the SCC carrier. To use the specified channel with an SCC, connect the SCC carrier to the appropriate connector on the cabled device and specify the new configuration through MAX. |
| Error -200852 | Given devices cannot be synchronized in a multiple-device task. Ensure that one of the devices in the task is in PXI slot 2, or specify the Synchronization Pulse Source and the Sample Clock Timebase Source to be from a device in PXI slot 2, even if that device is not in the task. |
| Error -200853 | Terminal specified must include the device name for the given multiple-device task. Include the device name in the terminal name. Example syntax is myDevice3/PFI4. |
| Error -200854 | Given devices cannot be synchronized in a multiple-device task because the Sample Clock Timebase Source specifies a different device from the Synchronization Pulse Source. Modify the Synchronization Pulse Source and/or the Sample Clock Timebase Source to be from the same device or leave one or both unspecified. |
| Error -200855 | Devices cannot be added to a task after configuring timing, triggering, buffers, and/or exported signals. Add all devices to the task before configuring other aspects of the task. |
| Error -200856 | Simulation disabling is not supported for this device, because it was created as a simulated device. |
| Error -200857 | Specified low pass cutoff frequency is not supported. |
| Error -200858 | To use Sample Clock as the Sample Timing Type for analog output on this device, call DAQmx Write before DAQmx Start. |
| Error -200859 | To use Sample Clock as the Sample Timing Type for analog output on this device, specify buffer size greater than 0 in DAQmx Configure Output Buffer. |
| Error -200860 | Combination of specified AI Maximum Sound Pressure Level and AI Microphone Sensitivity settings is not supported by the device. Consider using a microphone with lower sensitivity. If clipping signals at high levels is acceptable, you can use the microphone with specified sensitivity as long as you reduce the AI Maximum Sound Pressure. |
| Error -200861 | Combination of specified AI Maximum Sound Pressure Level, AI Microphone Sensitivity, and other related AI property settings is not supported by the device. Change the values of the related AI properties or do not set them at all. If you do not set the related AI properties, NI-DAQmx sets them for you. Alternatively, consider using a microphone with lower sensitivity. |
| Error -200862 | One or more devices from a multiple-device task are in an unidentified PXI chassis, which is not supported. Identify the PXI chassis in MAX. |
| Error -200863 | DAQmx Wait for Next Sample Clock is not supported by the given device for tasks containing channels of the given type or timing type. DAQmx Wait for Next Sample Clock is only supported for the hardware-timed single-point timing type. |
| Error -200864 | Data Transfer Request Condition being set to When Acquisition Complete is only supported when the Reference Trigger Type is other than None. Change the Data Transfer Request Condition or configure a reference trigger for the task. |
| Error -200865 | Data Transfer Request Condition is set to When Acquisition Complete, but the Number of Samples per Channel is greater than the On Board Buffer Size. Decrease the Number of Samples per Channel, remove some channels from the task, or change the Data Transfer Request Condition. |
| Error -200866 | Specified AO Maximum and Minimum Values are not supported given the specified AO DAC Reference and Offset Values. To keep the specified AO DAC Reference and Offset Values, change the AO Minimum and Maximum Values. To keep the specified AO Minimum and Maximum Values, supply higher reference voltage and specify the corresponding AO DAC Reference Value. Alternatively, supply an appropriate external DAC offset and specify the corresponding AO DAC Offset Value. When supplying an external DAC offset, to get the optimum accuracy, you should manually calibrate the offset. Refer to user documentation for details. |
| Error -200867 | Specified AO Maximum and Minimum Values are not supported given the specified AO DAC Reference Value. To keep the specified AO Minimum and Maximum Values, supply higher reference voltage and specify the corresponding AO DAC Reference Value. To keep the specified AO DAC Reference Value, change the AO Minimum and Maximum Values. Alternatively, supply an appropriate external DAC offset and specify the corresponding AO DAC Offset Value. When supplying an external DAC offset, to get the optimum accuracy, you should manually calibrate the offset. Refer to user documentation for details. |
| Error -200868 | Specified AO Maximum and Minimum Values are not supported given the specified AO DAC Reference Value. To keep the specified AO Minimum and Maximum Values, supply higher reference voltage and specify the corresponding AO DAC Reference Value. To keep the specified AO DAC Reference Value, change the AO Minimum and Maximum Values. |
| Error -200869 | Specified AO Maximum and Minimum Values are not supported given the specified AO DAC Offset Value. To keep the specified AO Minimum and Maximum Values, supply an appropriate offset and specify the corresponding AO DAC Offset Value. To keep the specified AO DAC Offset Value, change the AO Minimum and Maximum Values. Alternatively, supply an appropriate external DAC reference and specify the corresponding AO DAC Reference Value. |
| Error -200870 | Specified AO Maximum and Minimum Values are not supported given the specified AO DAC Offset Value. To keep the specified AO Minimum and Maximum Values, supply an appropriate offset and specify the corresponding AO DAC Offset Value. To keep the specified AO DAC Offset Value, change the AO Minimum and Maximum Values. |
| Error -200871 | Specified AO Maximum and Minimum Values are not supported given the specified AO DAC Range Low and High, and AO DAC Offset Value. To keep the specified AO DAC Range and Offset Values, change the AO Minimum and Maximum Values. To keep the specified AO Minimum and Maximum Values, supply higher reference voltage and specify the corresponding AO DAC Range. Alternatively, supply an appropriate external DAC offset and specify the corresponding AO DAC Offset Value. When supplying an external DAC offset, to get the optimum accuracy, you should manually calibrate the offset. Refer to user documentation for details. |
| Error -200872 | Specified AO Maximum and Minimum Values are not supported given the specified AO DAC Range Low and High. To keep the specified AO Minimum and Maximum Values, supply higher reference voltage and specify the corresponding AO DAC Range Low and High. To keep the specified AO DAC Range Low and High, change the AO Minimum and Maximum Values. Alternatively, supply an appropriate external DAC offset and specify the corresponding AO DAC Offset Value. When supplying an external DAC offset, to get the optimum accuracy, you should manually calibrate the offset. Refer to user documentation for details. |
| Error -200873 | Specified AO Maximum and Minimum Values are not supported given the specified AO DAC Range Low and High. To keep the specified AO Minimum and Maximum Values, supply higher reference voltage and specify the corresponding AO DAC Range Low and High. To keep the specified AO DAC Range Low and High, change the AO Minimum and Maximum Values. |
| Error -200874 | DAQmx Write is supported for counter output channels only while the task is running. To use DAQmx Write with the given task, invoke DAQmx Start prior to DAQmx Write. To specify the low and/or high time while the task is not running, set DAQmx properties instead of invoking DAQmx Write. |
| Error -200875 | DAQmx Write is supported for counter output channels only while the task is running. To use DAQmx Write with the given task, invoke DAQmx Start prior to DAQmx Write. To specify the frequency and/or the duty cycle while the task is not running, set DAQmx properties instead of invoking DAQmx Write. |
| Error -200876 | DAQmx Write is supported for counter output channels only while the task is running. To use DAQmx Write with the given task, invoke DAQmx Start prior to DAQmx Write. To specify the low and/or high ticks while the task is not running, set DAQmx properties instead of invoking DAQmx Write. |
| Error -200877 | Requested Every N Samples Event Interval is not supported for the given Data Transfer Mechanism and buffer size. To keep DMA or USB Bulk as the Data Transfer Mechanism, modify the buffer size and/or the Every N Samples Event Interval so the buffer size is an even multiple of the Every N Samples Event Interval. To keep the same Every N Samples Event Interval and buffer size, change the Data Transfer Mechanism to Interrupts if supported. |
| Error -200878 | Specified digital channel contains more bits than supported by the 16-bit version of DAQmx Port Read. Use a version of DAQmx Port Read that supports wider digital ports. |
| Error -200879 | Specified digital channel contains more bits than supported by the 16-bit version of DAQmx Port Write. Use the version of DAQmx Port Write that supports wider digital ports. |
| Error -200880 | Zero is not a supported value for the Every N Samples Event Interval. Specify an event interval greater than zero. |
| Error -200881 | Every N Samples Event registration has failed because the event is already registered within the task. Unregister the event before registering it again. |
| Error -200882 | Specified channel is not a valid global channel. Ensure that the Channel Name matches a channel in the Data Neighborhood in MAX. Check for typing errors. |
| Error -200883 | Task specified cannot be saved with interactive editing allowed, because the DAQ Assistant does not support at least one of the specified properties. Save the task with 'allow interactive editing' set to false, or specify only properties supported by the DAQ Assistant. |
| Error -200884 | Channel specified cannot be saved with interactive editing allowed, because the DAQ Assistant does not support at least one of the specified properties. Save the channel with 'allow interactive editing' set to false, or specify only properties supported by the DAQ Assistant. |
| Error -200885 | Combination of Reference Clock Source and Sample Clock Timebase Source specified is not supported by this device. To use the Reference Clock Source specified, do not set the Sample Clock Timebase Source. NI-DAQmx will set it to its default value: OnboardClock. To use the Sample Clock Timebase Source specified, do not set the Reference Clock Source. NI-DAQmx will set it to its default value: none. |
| Error -200886 | Start Trigger Digital Pattern Source requested is not supported because at least one of the corresponding channels is not tristated. Ensure all the corresponding channels are tristated or choose different channels. |
| Error -200887 | Start Trigger Digital Pattern Source requested is not supported because at least one of the corresponding channels is not in the task. Ensure all the corresponding channels are in the task or choose different channels. |
| Error -200888 | Reference Trigger Digital Pattern Source requested is not supported because at least one of the corresponding channels is not tristated. Ensure all the corresponding channels are tristated or choose different channels. |
| Error -200889 | Reference Trigger Digital Pattern Source requested is not supported because at least one of the corresponding channels is not in the task. Ensure all the corresponding channels are in the task or choose different channels. |
| Error -200890 | Active Edge requested is not supported because the Sample Clock Source is OnboardClock. To use the selected Sample Clock Source, set Sample Clock Active Edge to Rising Edge. |
| Error -200891 | Export of sample clock is supported by this device only when the Sample Clock Source is OnboardClock. Consider alternative methods for gaining access to the clock signal. |
| Error -200892 | When the Sample Timing Type is Change Detection and the Trigger Type is Digital Pattern Match, the relevant physical channels must be consistent for this device. Specifically, the Change Detection Rising Edge Physical Channels must match the physical channels from the Trigger Digital Pattern Source for which the Trigger Digital Pattern string is 0 or 1. |
| Error -200893 | Change Detection Rising and Falling Edge Physical Channels must be set identically on this device. |
| Error -200894 | Number of values specified via the Start Trigger Digital Pattern does not match the number of physical lines requested via the Start Trigger Digital Pattern Source. Change one or both of the properties so these two numbers are equal. |
| Error -200895 | Number of values specified in Reference Trigger Digital Pattern does not match the number of physical lines requested in Reference Trigger Digital Pattern Source. Change one or both of the properties so these two numbers are equal. |
| Error -200896 | Export of the requested trigger is supported on this device only when the corresponding Trigger Type is Digital Edge. |
| Error -200897 | Task contains a physical channel not supported by this device, given the requested Sample Timing Type. To keep the Sample Timing Type, use physical lines from port0/line0 through port3/line7. To access the requested channel, change the Sample Timing Type. |
| Error -200898 | Partial use of physical lines within a physical port is not supported by this device, given the requested Sample Timing Type. Consider specifying the entire port and tristating the lines you do not want driven. |
| Error -200899 | Port 1 cannot be used without port 0 on this device given the Sample Timing Type. You can use ports 0 and 2 by themselves. To use port 1, you also need to use port 0. |
| Error -200900 | Port 3 cannot be used without port 2 on this device given the Sample Timing Type. You can use ports 0 and 2 by themselves. To use port 3, you also need to use port 2. |
| Error -200901 | Digital Pattern string specified contains an invalid character. |
| Error -200902 | Data Voltage Low Level and Data Voltage High Level must be within a common voltage range. |
| Error -200903 | Reference clock is not supported by this device. Do not set the Reference Clock property. |
| Error -200904 | Start Trigger Type requested is not supported given the requested Timing Type. To use the requested Timing Type, do not set the Start Trigger Type property. NI-DAQmx automatically selects a compatible Start Trigger Type setting. To use the requested Start Trigger Type, select a different Timing Type. |
| Error -200905 | Handshake Trigger Type requested is not supported given the requested Timing Type. To use the requested Timing Type, do not set the Handshake Trigger Type property. NI-DAQmx automatically selects a compatible Handshake Trigger Type setting. To use the requested Handshake Trigger Type, select a different Timing Type. |
| Error -200906 | Pause Trigger Type requested is not supported given the requested Timing Type. To use the requested Timing Type, do not set the Pause Trigger Type property. NI-DAQmx automatically selects a compatible Pause Trigger Type setting. To use the requested Pause Trigger Type, select a different Timing Type. |
| Error -200907 | Reference Trigger Type requested is not supported given the requested Timing Type. To use the requested Timing Type, do not set the Reference Trigger Type property. NI-DAQmx automatically selects a compatible Reference Trigger Type setting. To use the requested Reference Trigger Type, select a different Timing Type. |
| Error -200908 | Sample Clock Source requested is not supported given the requested Timing Type. To use the requested Timing Type, do not set the Sample Clock Source property. NI-DAQmx automatically selects a compatible Sample Clock Source setting. To use the requested Sample Clock Source, select a different Timing Type. |
| Error -200909 | 20 Mhz Timebase Output Terminal requested is not supported given the requested Timing Type. To use the requested Timing Type, do not set the 20 Mhz Timebase Output Terminal property. NI-DAQmx automatically selects a compatible20 Mhz Timebase Output Terminal. To use the requested 20 Mhz Timebase Output Terminal, select a different Timing Type. |
| Error -200910 | Sample Clock Output Terminal requested is not supported given the requested Timing Type. To use the requested Timing Type, do not set the Sample Clock Output Terminal property. NI-DAQmx automatically selects a compatible Sample Clock Output Terminal. To use the requested Sample Clock Output Terminal, select a different Timing Type. |
| Error -200911 | Start Trigger Output Terminal requested is not supported given the requested Timing Type. To use the requested Timing Type, do not set the Start Trigger Output Terminal property. NI-DAQmx automatically selects a compatible Start Trigger Output Terminal. To use the requested Start Trigger Output Terminal, select a different Timing Type. |
| Error -200912 | Reference Trigger Output Terminal requested is not supported given the requested Timing Type. To use the requested Timing Type, do not set the Reference Trigger Output Terminal property. NI-DAQmx automatically selects a compatible Reference Trigger Output Terminal. To use the requested Reference Trigger Output Terminal, select a different Timing Type. |
| Error -200913 | Ready For Transfer Event Output Terminal requested is not supported given the requested Timing Type. To use the requested Timing Type, do not set the Ready For Transfer Event Output Terminal property. NI-DAQmx automatically selects a compatible Reference Trigger Event Output Terminal. To use the requested Ready For Transfer Trigger Event Output Terminal, select a different Timing Type. |
| Error -200914 | Change Detection Event Output Terminal requested is not supported given the requested Timing Type. To use the requested Timing Type, do not set the Change Detection Event Output Terminal property. NI-DAQmx automatically selects a compatible Change Detection Output Terminal. To use the requested Change Detection Event Output Terminal, select a different Timing Type. |
| Error -200915 | Handshake Event Output Terminal requested is not supported given the requested Timing Type. To use the requested Timing Type, do not set the Handshake Event Output Terminal property. NI-DAQmx automatically selects a compatible Handshake Event Output Terminal. To use the requested Handshake Event Output Terminal, select a different Timing Type. |
| Error -200916 | Sample Timebase Divisor requested is not supported given the requested Timing Type. To use the requested Timing Type, do not set the Sample Timebase Divisor property. NI-DAQmx automatically selects a compatible Sample Timebase Divisor. To use the requested Sample Timebase Divisor, select a different Timing Type. |
| Error -200917 | Every N Samples Event Interval requested must be an integer multiple of two for analog output tasks on this device. |
| Error -200918 | Global channel name specified is already used for a task in the Data Neighborhood. NI-DAQmx does not support overlapping task and global channel names. Select a different name. |
| Error -200919 | Task name specified is already used for a global channel in the Data Neighborhood. NI-DAQmx does not support overlapping task and global channel names. Select a different name. |
| Error -200920 | Requested Every N Samples Event Interval is not supported for the given buffer size. Modify the buffer size and/or the Every N Samples Event Interval so the buffer size is an even multiple of the Every N Samples Event Interval. |
| Error -200921 | Channel specified cannot be saved with interactive editing allowed, because the only digital channels with multiple lines supported by the DAQ Assistant are entire ports. Save the channel with 'allow interactive editing' set to false. Alternatively, change the channel so it contains an entire port, or break it up into channels with individual lines. |
| Error -200922 | Channel specified cannot be saved with interactive editing allowed, because the DAQ Assistant does not support digital channels with different settings for different lines. Save the channel with 'allow interactive editing' set to false. Alternatively, set all the lines in the channel identically, or break the channel up into channels with individual lines. |
| Error -200923 | Wait Mode property is not supported for the given non-buffered task. Do not use this property inside the task, or change the task to be buffered. |
| Error -200924 | Wait Mode specified is not supported for the given non-buffered task. Specify a different Wait Mode, or change the task to be buffered. |
| Error -200925 | Rising and Falling Edge Physical Channels for Change Detection requested are not supported because at least one of the channels is not tristated. Ensure all the corresponding channels are tristated or choose different channels. |
| Error -200926 | Rising and Falling Edge Physical Channels for Change Detection requested are not supported because at least one of the corresponding channels is not in the task. Ensure all the corresponding channels are in the task or choose different channels. |
| Error -200927 | Trigger Type was set to Digital Pattern Match but no physical channels were specified as the Digital Pattern Source. Specify physical channels for property. |
| Error -200928 | Pattern match hardware for this device can only be used for one trigger. |
| Error -200929 | Two specified ports alone are not supported given the Sample Timing Type on this device. To use only two ports, specify ports 0 and 1, or ports 2 and 3. To use the two ports specified, use four ports (0, 1, 2, and 3) on the device, and disregard data from the unwanted ports. |
| Error -200930 | Two specified ports alone are not supported given the Sample Timing Type on this device. To use only two ports, specify ports 0 and 1, or ports 2 and 3. To use the two ports specified, use four ports (0, 1, 2, and 3) on the device. Ensure the lines from the unwanted ports are unwired, tristated, or are connected so no equipment can be damaged. |
| Error -200931 | Three ports alone are not supported given the Sample Timing Type on this device. Specify four ports (0, 1, 2, and 3), and disregard data from the unwanted port. |
| Error -200932 | Three ports alone are not supported given the Sample Timing Type on this device. Specify four ports (0, 1, 2, and 3). Ensure the lines from the unwanted port are unwired, tristated, or are connected so no equipment can be damaged. |
| Error -200933 | Operation cannot be performed, because the Channel Calibration Expiration Date is not specified, and Channel Calibration Enable property is set to True. To use channel calibration, specify the Expiration Date; otherwise, set Channel Calibration Enable to false. |
| Error -200934 | Operation cannot be performed, because the Channel Calibration Expiration Date has passed, and the Channel Calibration Apply Calibration if Expired property is False. Update the channel calibration, including the Expiration Date, or set Apply Calibration If Expired to True. |
| Error -200935 | Operation cannot be performed, because the Channel Calibration Scale Type is not specified and Channel Calibration Enable property is set to True. To use channel calibration, specify the Scale Type; otherwise, set Channel Calibration Enable to false. |
| Error -200936 | Operation cannot be performed, because the Channel Calibration Table Pre-Scaled Values property is not specified when the Channel Calibration Scale Type is Table. |
| Error -200937 | Operation cannot be performed, because the Channel Calibration Table Scaled Values property is not specified when the Channel Calibration Scale Type is Table. |
| Error -200938 | Operation cannot be performed, because the number of elements in the array specified for the Channel Calibration Table Pre-Scaled Values property is not equal to the number of elements in the array specified for Channel Calibration Table Scaled Values. |
| Error -200939 | The Channel Calibration Table Scale Pre-Scaled Values specified is not supported, because one of the numbers appears more than once in the specified array. Ensure unique numbers are specified in the array. |
| Error -200940 | Operation cannot be performed, because the Channel Calibration Polynomial Forward Coefficients property is not specified when the Channel Calibration Scale Type is Polynomial. |
| Error -200941 | Operation cannot be performed, because the Channel Calibration Polynomial Reverse Coefficients property is not specified when the Channel Calibration Scale Type is Polynomial. |
| Error -200942 | Call mechanism set to synchronous event callbacks is not supported for DAQmx events on this platform. To use DAQmx events on this platform, set the call mechanism to asynchronous event callbacks. |
| Error -200943 | Operation failed because the Data Transfer Custom Threshold property is not set, and the Data Transfer Request Condition is set to Onboard Memory Custom Threshold. Specify a value for the Data Transfer Custom Threshold, or change the Data Transfer Request Condition. |
| Error -200944 | Operation failed because the Data Transfer Custom Threshold property is set, and no value is specified for the Data Transfer Request Condition. To use the specified Data Transfer Custom Threshold, set Data Transfer Request Condition to Onboard Memory Custom Threshold. If you set Data Transfer Request Condition to any value other than Onboard Memory Custom Threshold, the Data Transfer Custom Threshold property is ignored. |
| Error -200945 | Operation failed because the Data Transfer Request Condition is set to Onboard Memory Custom Threshold. This device supports this Data Transfer Request Condition only when the Data Transfer Mechanism is set to DMA. To use the specified Data Transfer Request Condition, set Data Transfer Mechanism to DMA. Otherwise, specify a different Data Transfer Request Condition. |
| Error -200946 | Task could not be started, because the driver could not write enough data to the device. This was due to system and/or bus-bandwidth limitations. Reduce the number of programs your computer is executing concurrently. If possible, perform operations with heavy bus usage sequentially instead of in parallel. If you can't eliminate the problem, contact National Instruments support at ni.com/support. |
| Error -200947 | DAQmx Events are not supported in this version of LabVIEW. To use DAQmx Events, install LabVIEW 7.1 and the LabVIEW 7.1.1 patch. The patch is available at ni.com/downloads. |
| Error -200948 | DAQmx tasks cannot provide a source for a Timed Loop and contain a DAQmx Signal Event at the same time. DAQmx Signal events include the Counter Output event, the Sample Complete Event, the Sample Clock Event, and the Digital Change Detection event. Tasks that contain a Timed Loop can contain DAQmx Events as long as the events are not a type of DAQmx Signal Event. See documentation for more details. |
| Error -200949 | You can only register one DAQmx Signal Event at a time on a task. DAQmx Signal events include the Counter Output event, the Sample Complete Event, the Sample Clock Event, and the Digital Change Detection event. Unregister the event before registering it again. |
| Error -200950 | Done Event registration has failed because the event is already registered within the task. Unregister the event before registering it again. |
| Error -200951 | DAQmx Write for counter output detected that no sample clock has occurred since the last call to write which means that the writes are happening at a rate that exceeds the sample clock rate. To avoid this problem use the Wait for Next Sample Clock in your application. |
| Error -200952 | Event Output Terminal cannot include the Trigger Source terminal in the same task for this device. |
| Error -200953 | Start Trigger Source cannot be the same as the Sample Clock Source in the same task for this device. |
| Error -200954 | Sample Clock Output Terminal cannot include the Start Trigger Source terminal in the same task for this device. |
| Error -200955 | Two channels in the task have different raw data format property values, which is not supported. All channels in the task must have identical raw data format property values when raw data compression is configured. Only include channels with identical raw data format property values in the task when compression is configured. |
| Error -200956 | Raw data compression has been configured for a channel that does not support raw data compression. Remove the channel from the task or set the Raw Data Compression Type to None. |
| Error -200957 | Compressed Sample Size exceeds the Resolution of the channel. Configure the Compressed Sample Size to be less than or equal to the channel Resolution. |
| Error -200958 | TEDS interface device configured in MAX was not detected. Make sure that the type of TEDS interface device configured in MAX is correct and that the device is properly connected. |
| Error -200959 | Two channels in the task have different raw data compression property values, which is not supported. All channels in the task must have the same raw data compression property values. |
| Error -200960 | DAQmx software event cannot be registered because the task is running. Register all your DAQmx software events prior to starting the task. |
| Error -200961 | Firmware for the device could not be downloaded, and the device cannot be used. This failure is due to a missing or damaged firmware image file. Reinstall the driver to eliminate this error. |
| Error -200962 | Firmware for this device could not be downloaded, and the device cannot be used. The failure may be due to damaged hardware. Contact National Instruments support at ni.com/support |
| Error -200963 | Requested Sample Timing Type is not allowed, because there is already another task with analog output channels from the same device configured for a different Sample Timing Type. This is not supported on this device. Change your application so that all the channels from this device are used in one task, set Sample Timing Type to On Demand for all tasks, or consider using two devices for the two tasks. |
| Error -200964 | Every N Samples Acquired Into Buffer Event cannot be registered, because it is not supported for output tasks. Use the Every N Samples Transferred From Buffer Event. |
| Error -200965 | Every N Samples Transferred from Buffer Event cannot be registered, because it is not supported for input tasks. Use the Every N Samples Acquired Into Buffer Event. |
| Error -200966 | Every N Samples Acquired Into Buffer Event registration has failed because the event is already registered within the task. Unregister the event before registering it again. |
| Error -200967 | Every N Samples Transferred From Buffer Event registration has failed because the event is already registered within the task. Unregister the event before registering it again. |
| Error -200968 | Requested operation cannot be performed inside the aysnchronous DAQmx Event callback thread. Use synchronous callback mechanism or perform the operation in a different thread. |
| Error -200969 | TEDS operation failed because the corresponding physical channel is not an analog input channel. |
| Error -200970 | Every N Samples Event Interval requested must be an integer multiple of two for analog input tasks on this device. |
| Error -200971 | Property cannot be set because the task is not running or committed. Start or commit the task prior to setting the specified property. |
| Error -200972 | Property cannot be set because the task is not running. Start the task prior to setting the specified property. |
| Error -200973 | Property cannot be queried because the task is not running. Start the task prior to getting the specified property. |
| Error -200974 | Allow Connecting DAC Reference to Ground at Runtime set to True is not supported by this device when DAC Reference Voltage Source is set to External. |
| Error -200975 | Querying the Counter Output Ready for New Value property is not supported by this device when the Sample Mode is set to Hardware Timed Single Point. Use DAQmx Wait for Next Sample Clock before DAQmx Write to make sure the counter is ready to accept the new value. |
| Error -200976 | Thermocouple CJC (cold junction compensation) Channel specified cannot be used for CJC because the corresponding physical channel does not support temperature measurement. Select a different CJC Channel, set CJC Source to Internal, or set CJC Source to Constant Value and use CJC Value to specify the temperature of the cold junction. |
| Error -200977 | Channel specified cannot be saved with Allow Interactive Editing set to True, because the DAQ Assistant does not support polynomial calibration scales. Save the channel with Allow Interactive Editing set to False, or use a table calibration scale. |
| Error -200978 | DAQmx Software Events cannot be registered with different call mechanisms on the same task. The software events for a task must all be registered with synchronous callbacks or they must be all registered with asynchronous callbacks. |
| Error -200979 | When you use synchronous events, you can clear, stop, abort, unreserve, or start a task only from the thread in which you registered synchronous events. |
| Error -200980 | DAQmx Every N Samples Transferred from Buffer Event is not supported by the channel types or devices in your task. |
| Error -200981 | DAQmx Every N Samples Acquired into Buffer Event is not supported by the channel types or devices in your task. |
| Error -200982 | DAQmx Signal Events are not supported by your device. DAQmx Signal events include the Counter Output event, the Sample Complete Event, the Sample Clock Event, and the Digital Change Detection event. |
| Error -200983 | You only can get the specified property while the task is reserved, committed or while the task is running. Reserve, commit or start the task prior to getting the property. |
| Error -200984 | Auto Start cannot be set to True when one or more DAQmx events are registered for the task. Set Auto Start to False and start the task manually. |
| Error -200985 | DAQmx Write parameter Auto Start cannot be set to True when one or more DAQmx events are registered for the task. Set Auto Start to false and start the task manually. |
| Error -200986 | DAQmx software event cannot be unregistered because the task is running. Unregister all your DAQmx software events prior to starting the task. |
| Error -200987 | DAQmx Signal Event type requested is not supported by the channel types or the devices in your task. DAQmx Signal events include the Counter Output event, the Sample Complete Event, the Sample Clock Event, and the Digital Change Detection event. Refer to product documentation for more details on which DAQmx Signal Events are supported by the channel types and devices in your task. |
| Error -200988 | Combination of requested values for Read Wait Mode and Wait ffor Next Sample Clock Wait Mode properties is not supported for the given task on this device. Set both properties to Wait for Interrupt or do not set either of the properties to Wait for Interrupt. |
| Error -200989 | Combination of requested values for Read Wait Mode and Wait for Next Sample Clock Wait Mode properties is not supported for the given task on this device. Set both properties to Wait for Interrupt or set Read Wait Mode to a value other than Wait for Interrupt. |
| Error -200990 | All synchronous events for the task must be registered from the same thread. |
| Error -200991 | Task cannot be stopped, because at least one installed event handler has not been removed. Remove all installed event handlers by calling CNiDAQmxEvent::RemoveEventHandler or CNiDAQmxEvent::RemoveAllEventHandlers. See the documentation for more information. |
| Error -200992 | DAQmx Software Events are generated too quickly for the driver to keep up, and some of them have been lost. Reduce the rate at which your application is generating the events. Consider reconfiguring the events you are using, or using different events. |
| Error -200993 | DAQmx Write failed, because it was called before the previously written value was output. This is likely a result of the sample clock period being shorter than the period of the generated pulse train. To correct this issue, increase your sample clock period and/or reduce the period of the generated pulse train. |
| Error -200994 | Requested property cannot be set while the task is running and the Sample Mode is set to Hardware Timing Single Point. Use DAQmx Write instead of setting the property. |
| Error -200995 | Requested Memory Mapping for Programmed IO Enable value, True, is not supported when Sample Mode is set to Hardware Timed Single Point. Change one or both of the properties. |
| Error -200996 | Data Transfer Mechanism is not set to Programmed I/O, which is the only value supported when the Sample Mode is Hardware Timed Single Point. Set your Data Transfer Mechanism to Programmed I/O or change the Sample Mode. |
| Error -200997 | Requested Sample Timing Type value, On Demand, is not supported when Sample Mode is Hardware Timed Single Point. Change Sample Timing Type and/or Sample Mode. |
| Error -200998 | Hardware Timed Single Point is not a supported Sample Mode for the specified Measurement Type. Change Sample Mode and/or Measurement Type. |
| Error -200999 | Requested property, Ready For New Value, is not supported when the Sample Timing Type is On Demand. To use the Ready For New Value property, change the Sample Timing Type. |
| Error -201000 | DAQmx Events are not supported in this version of LabVIEW. LabVIEW 8.0 or later is required to use DAQmx Events. |
| Error -201001 | Sample Clock Rate requested is supported only if Enhanced Alias Rejection Enable is True. Set Enhanced Alias Rejection Enable to True or increase the Sample Clock Rate. |
| Error -201002 | Sample Clock Rate must match the frequency of the internal timebase specified as the Sample Clock Source. To use the specified Sample Clock Rate, set the Sample Clock Source to OnboardClock. To use the specified timebase as the Sample Clock, set the Sample Clock Rate to the frequency of that timebase. |
| Error -201003 | Device cannot be accessed. Possible causes: Device is no longer present in the system. Device is not powered. Device is powered, but was temporarily without power. Device is damaged. Ensure the device is properly connected and powered. Turn the computer off and on again. If you suspect that the device is damaged, contact National Instruments at ni.com/support. |
| Error -201004 | Device does not support simultaneous calibration of multiple channels. Calibrate channels one channel at a time, passing individual channels to different invocations of DAQmx Setup Calibration. |
| Error -201005 | Invoke DAQmx Setup Calibration before invoking the corresponding DAQmx Adjust Calibration. |
| Error -201006 | Device does not support an external calibration password. |
| Error -201007 | "Generate" or finite "Wait" instruction expected before "If-Else" block. Insert a "Generate" or finite "Wait" instruction before the If-Else block. |
| Error -201008 | Waveform length is too small for the "Generate" instruction before the "If-Else" block. |
| Error -201009 | Length of waveform subset is too small for the "Generate" instruction before "If-Else" block. |
| Error -201010 | Marker position specified is too close to the end of the waveform in the "Generate" statement before the "If-Else" block. |
| Error -201011 | Wait duration is too small for the "Wait" instruction before the "If-Else" block. |
| Error -201012 | "Clear Trigger" instruction cannot be the last instruction in an "If-Else" block. |
| Error -201013 | "If-Else" blocks are not allowed in "Repeat Until" loops. |
| Error -201014 | "If-Else" blocks are not allowed in "Finite Repeat" loops. If possible, remove the "Repeat" and "End Repeat" instructions and explicitly duplicate the instructions originally in the loop the desired number of times. |
| Error -201015 | PLL lock operation failed or timed out. Ensure the module is fully inserted into the carrier. |
| Error -201016 | Too many compiled instructions in loop. "Generate" and "Wait" instructions each result in at least one compiled instruction. Each marker adds an additional compiled instruction. Clear instruction does not result in a compiled instruction. If possible, reduce the number of generate instructions by concatenating the waveforms on two or more consecutive generate instructions. |
| Error -201017 | Byte order marker of the specified file is not supported by NI-DAQmx. For tab-delimeted files, NI-DAQmx supports UTF-8, UTF-16 / UCS-2 little endian, and UTF-32 / UCS-4 little endian. For ini files, NI-DAQmx only supports UTF-8. Save the file in one of the supported formats with the appropriate byte order marker. |
| Error -201018 | You have selected an external clock source for the task, but the device importing the clock does not have the longest pipeline of all the devices in the task. This leads to an incomplete acquisition on that device because the device will not receive enough Sample Clock pulses. Route the external clock signal into the device with the longest pipeline. Refer to device documentation for information on pipeline depth. |
| Error -201019 | Pause triggering is not supported in a multi-device task. To configure pause triggering in a multi-device configuration, you must use no more than one device per task and manually route the clock signals in the application. |
| Error -201020 | Lines specified do not support change detection. Select lines that support change detection. |
| Error -201021 | Write recovery could not complete before detecting another Sample Clock pulse. Reduce the Sample Clock rate, increase the frequency of the generated pulse train, or set Write Recovery Mode to Poll. |
| Error -201022 | Write recovery could not complete before detecting another Sample Clock pulse. Reduce the Sample Clock rate or increase the frequency of the generated pulse train. |
| Error -201023 | DAQmx Write failed because the previously written value has not been generated. This error can occur if the Sample Clock period is shorter than the period of the generated pulse train. Reduce the Sample Clock rate, increase the frequency of the generated pulse train, or set Write Recovery Mode to Poll. |
| Error -201024 | DAQmx Write failed because the previously written value has not been generated. This error can occur if the Sample Clock period is shorter than the period of the generated pulse train. Reduce the Sample Clock rate or increase the frequency of the generated pulse train. |
| Error -201025 | Non-buffered hardware-timed operations are not supported for this device and Channel Type. Set the Buffer Size to greater than 0, do not configure Sample Clock timing, or set Sample Timing Type to On Demand. |
| Error -201026 | Data Transfer Mechanism is set to Programmed I/O which is not supported for hardware-timed operations for this device and Channel Type. Change Data Transfer Mechanism, do not configure Sample Clock timing, or set Sample Timing Type to On Demand. |
| Error -201027 | Counter task detected three or more missed Sample Clock pulses. Samples were lost before the application could read them. Decrease the Sample Clock rate or restructure the application so that DAQmx Read runs more frequently. Setting the Convert Error to Warning property to True does not eliminate the error, because samples were lost. |
| Error -201028 | Name specified is already in use. Specify a name that is not currently in use. |
| Error -201029 | Device specified is already connected to a RTSI cable. To connect the device to another RTSI cable, remove it from the RTSI cable to which it is currently connected. |
| Error -201030 | Device specified cannot be connected to a RTSI cable. If the device does not have a RTSI connector, you cannot connect it to a RTSI cable. If the device is a PXI device then it is automatically connected to the PXI backplane, and therefore does not need to be manually configured as connected to a RTSI cable. |
| Error -201031 | Address specified is already in use. Specify an address that is not in use. |
| Error -201032 | SCXI slot number specified is invalid. Specify a slot number that is valid for the specified chassis. |
| Error -201033 | Slot specified is already occupied. Either specify a slot that is unoccupied or remove the module occupying the desired slot. |
| Error -201034 | Cascade digitization mode is not supported for SCXI. Select a different digitization mode. |
| Error -201035 | Digitizing Device Channels property is specified, but the Digitization Mode property is not set to parallel. Either remove the Digitizing Device Channels property or set the Digitizing property to parallel. |
| Error -201036 | Format of the time value specified is invalid. Enter the time value in the format: YYYY-MM-DDTHH:mm:ssZ UTC Where YYYY is the four digit year, MM is the two digit month, DD is the two digit day of the month, HH is the two digit hour of the day (24 hour clock), mm is the two digit minutes into the hour, and ss is the two digit seconds into the minute. T is a literal separator between date and time. For example, the string: 2004-10-19T16:30:45Z UTC Represents October 19th, 2004 at 4:30:45 PM GMT. |
| Error -201037 | Time value specified is invalid. Ensure that the time entered has only valid values for each of the fields in the time format. For example: the month section must be between 01 and 12. |
| Error -201038 | Author property cannot be set on a local channel. Remove the author property from the local channel. |
| Error -201039 | Object lacks a required property. Add the required property to the object. |
| Error -201040 | Object specified contains an extra property. Remove the extra property from the object. |
| Error -201041 | Product type and product number specified do not refer to the same product. Remove either the product type or the product number from the object. |
| Error -201042 | Device specification provided does not match any hardware in the system. Change the device specification to match a device present in your system. You can also change your device specification to be less specific. |
| Error -201043 | Device specification provided matches more than one device in the system. Change the device specification to be more specific. |
| Error -201044 | Specified accessory name is invalid. The name of the accessory should be in this format: accessoryProductType / connectedDeviceIdentifier / connectorNumber Connector numbers start at zero. A device with only one connector only has a connector zero. |
| Error -201046 | Accessory type specified cannot be connected to the specified device. Enter an accessory type that can be connected to the device specified. |
| Error -201047 | Device and connector specified by the accessory can not be configured because there is already an accessory configured for that connector and device. Enter a device and connector that is not currently occupied, or remove the configuration of the existing accessory. |
| Error -201048 | Accessory setting specified does not apply to the accessory type. Remove the non-applicable accessory setting from the accessory specification. |
| Error -201049 | Digitizing device specified for the SCC carrier is not capable of digitizing for SCC carriers. Specify a device that is capable of digitizing for SCC carriers. |
| Error -201050 | Carrier specified for the SCC module could not be found. Ensure that the SCC carrier specified for the module is also defined in the configuration file. |
| Error -201051 | Controlling device specified for the TEDS interface is not capable of controlling a TEDS interface. |
| Error -201052 | Physical channels specified for the TEDS interface are too great in number for the specified type of TEDS interface. Reduce the number of physical channels specified. |
| Error -201053 | Physical channel specified for the TEDS interface is already connected to a TEDS interface. Enter a physical channel that is not currently occupied, or remove the existing physical channel configuration. |
| Error -201054 | Enumerated value specified is not a valid value for that enumeration. The enumerated value may have been exported from a later version of NI-DAQmx and is not supported by the version of NI-DAQmx installed on your system. Check the version specified in the file against the installed version of NI-DAQmx. You can upgrade the version of NI-DAQmx installed on your system, or change the value to one supported by the version of NI-DAQmx you have installed. |
| Error -201055 | Object contains two references to the same property. Remove one of the duplicate properties. |
| Error -201056 | Numeric value specified is in an invalid format. Remove any non-numeric characters from the specified numeric value. |
| Error -201057 | Hardware product type specified is invalid. Enter a valid product type. If the product number you entered is an actual product type, ensure the product type is appropriate for the object you are configuring. For example, do not use the product type of a PXI device where an SCXI module is expected. |
| Error -201058 | Hardware product number specified is invalid. Enter a valid product number. If the product number you entered is an actual product number, ensure the product type is appropriate for the object you are configuring. For example, do not use the product number of a PXI device where an SCXI module is expected. |
| Error -201059 | Device information retrieval failed because PXI chassis is not identified. Use MAX or nipxiconfig to identify your chassis. |
| Error -201060 | Syntax error encountered in INI file. Valid INI syntax allows for the following 3 types of lines: section headers, items, and comments. A section header begins with an open bracket and ends with a closed bracket. Example: [mySection] An item has an equals sign in between two strings. Example: myItem = 46 A comment begins with a semicolon. Example: ; This is my comment. |
| Error -201061 | Property specified cannot return its value because the custom scale for the channel does not include the value in the range or table of pre-scaled values. Ensure that the custom scale includes all potential values for this property in the range or table of pre-scaled values, or use a linear or polynomial scale. |
| Error -201062 | Selected lines do not support buffered operations. Ensure only lines that support buffered operations are being used in the task. If using change detection timing, the task must be changed to non-buffered to support these lines. |
| Error -201063 | Device ID value in the driver does not match the device ID value from the device. Ensure the correct driver is being used for this device. |
| Error -201064 | Configuration file is missing the required header fields. Add required header information at the top of the text file prior to any data. |
| Error -201065 | Configuration file contains property names or values that are not contained within a valid table. Add the appropriate start of table string prior to property names. |
| Error -201066 | Property setting found in a column with no property name heading. Remove the property setting from the column or add the property name to the table definition. |
| Error -201067 | Configuration file contains an invalid start of table identifier. The table identifier may have been exported from a later version of NI-DAQmx and is not supported by the version of NI-DAQmx installed on your system. Check the version specified in the file against the installed version of NI-DAQmx. You can upgrade the version of NI-DAQmx installed on your system, or remove the table from the file. |
| Error -201068 | Configuration file string contains invalid character escape sequence. |
| Error -201069 | Local channel name specified is invalid. Local channel names are of the form <task name>/<channel name>. Example: task1/chan1 |
| Error -201070 | Task does not include the Channels property. Specify the Channels property for this task. |
| Error -201071 | Task references a local channel from another task. Reference only global channels and local channels that belong to this task. |
| Error -201072 | Task references a local channel that does not exist in this task. Remove the reference to the missing local channel or create the local channel. |
| Error -201073 | Local channel specified is from a task that does not exist. Specify the task in question, move the local channel to an existing task, or change the local channel to a global channel. |
| Error -201074 | Import operation supports tasks, channels, and scales only, but a hardware object was found in the file. Remove the hardware objects from the input file. |
| Error -201075 | Import operation does not support tasks, channels, and scales, but such an object was found. Remove all tasks, channels, and scales from the input file. |
| Error -201076 | NI-DAQmx version specified in the input file is newer than the installed NI-DAQmx version. Change the version in the file to match the installed version. The import might still fail if the file contains properties that are not supported by the installed version of NI-DAQmx. |
| Error -201077 | Section name specified is invalid. The format of the section name is [<objectType> <objectName>]. Example: [DAQmxDevice Dev1] |
| Error -201078 | Section identifier specified is invalid. Refer to the NI-DAQmx configuration file documentation for a list of valid section identifiers. The section identifier may have been exported from a later version of NI-DAQmx and is not supported by the version of NI-DAQmx installed on your system. Check the version specified in the file against the installed version of NI-DAQmx. You can upgrade the version of NI-DAQmx installed on your system, or remove the section from the file. |
| Error -201079 | SCC slot number specified is invalid. Specify a slot number that is valid for the specified carrier. |
| Error -201080 | SCC specified cannot be placed in the slot specified. Specify a supported SCC for the given slot or specify a slot that supports the given SCC. |
| Error -201081 | Channel was listed more than once in the task. A task cannot contain a channel with the same name twice. Remove the duplicate entries from the configuration file. |
| Error -201082 | Hidden channel was listed more than once in the task. A task cannot contain a hidden channel with the same name twice. Remove the duplicate entries from the configuration file. |
| Error -201083 | Task must contain at least one channel. Add a channel to the task in the configuration file. |
| Error -201084 | Hidden channels listed for the task were not in the channels list for the task. Add the missing hidden channels to the channel list in the configuration file. |
| Error -201085 | Thermocouple CJC channel name property must be set when the thermocouple CJC source property is Channel. Set the thermocouple CJC channel name property or set the thermocouple CJC source property to a value other than Channel. |
| Error -201086 | Attribute name specified is invalid. Validate the attribute name using your ADE. The attribute may have been exported from a later version of NI-DAQmx and is not supported by the version of NI-DAQmx installed on your system. Check the version specified in the file against the installed version of NI-DAQmx. You can upgrade the version of NI-DAQmx installed on your system, or remove the attribute from the file. |
| Error -201087 | Task contains physical channels on one or more devices that require you to specify the Sample Clock rate. Use the Sample Clock Timing function/VI to specify a Sample Clock rate. You cannot specify a Sample Clock rate if Mode is set to On Demand. |
| Error -201088 | Task contains physical channels on one or more devices that require a different Sample Clock Timebase Source than the one specified. Do not specify the Sample Clock Timebase Source. DAQmx will set the Sample Clock Timebase Source appropriately. |
| Error -201089 | Task contains physical channels on one or more devices that require a different Sample Clock Timebase Rate than the one specified. Do not specify the Sample Clock Timebase Rate. DAQmx will set the Sample Clock Timebase Rate appropriately. |
| Error -201090 | Task contains physical channels on one or more devices that require the driver to select the Sync Pulse Source. Do not specify the Sync Pulse Source. DAQmx will set the Sync Pulse Source appropriately. |
| Error -201091 | Minimum delay time between the sync pulse and start must be specified when using an external Sync Pulse Source. Specify SyncPulse.MinDelayToStart. |
| Error -201092 | Sync pulse cannot be exported when using an external sync pulse source. Do not export the sync pulse, or use the internal chassis sync pulse source. |
| Error -201093 | Task contains physical channels that have incompatible hardware restrictions for their Sample Clock Rates. Remove incompatible physical channels from the task. |
| Error -201094 | An active device was specified for the attribute but it is not supported for channel expansion tasks. Do not specify an active device when setting the attribute or do not use channel expansion. |
| Error -201095 | Driver was unloaded and then reloaded at a different base address after the session was created. Session is unusable. Close and reopen the session. |
| Error -201096 | Sample clock timebase rate must be specified when using an external sample clock timebase. |
| Error -201097 | Sample Clock Rate requested is supported only if Enhanced Alias Rejection Enable is False. Set Enhanced Alias Rejection Enable to False or decrease the Sample Clock Rate. |
| Error -201098 | When enabling auto zero on this device, all channels that are using auto zero must have the same auto zero mode. Channels with auto zero disabled may be present in the same task as channels with auto zero enabled. Select the same auto zero mode for all channels that are using auto zero. |
| Error -201099 | Task specified cannot be saved because the DAQmx Timing properties were specified on a per device basis using the More: AI Convert: ActiveDevs property. |
| Error -201100 | Sample clock timebase divisor may not be specified when an external sample clock source is specified. Change the sample clock source to onboard clock or do not configure the sample clock timebase divisor. |
| Error -201101 | Number of channels in task exceeds the device maximum given the requested Timing Type. Reduce the number of channels or select a different Timing Type. |
| Error -201102 | Analog trigger source must be the first channel of the device in the acquisition or a valid analog trigger terminal. Create your channels in a different order so that this channel is first, select a different channel from this device, or select the first channel from another device in the task. If you explicitly named the virtual channel in DAQmx Create Channel you must use the name assigned to that channel. |
| Error -201103 | Device support an analog channel as the source of an analog pause trigger only when it is the only channel from this device in the task. Remove all of this device's channels currently in the task except the channel that will be used as the analog trigger source, change the analog trigger source to a terminal, or select a channel from another device that only has one channel in the task. |
| Error -201104 | An attempt has been made to use an analog trigger in multiple situations with differing properties. Change the analog trigger properties so they are the same, select an analog trigger source from another device for one of the triggers, or do not use an analog trigger for all situations. |
| Error -201105 | Resource requested by this task has already been reserved by a different task with conflicting settings. Unreserve any other tasks using this device, or change their settings to be compatible with this task. |
| Error -201106 | Physical channel specified may only be used if the C Series module is installed in a slot that supports this physical channel. Move your cDAQ module to a slot that supports this physical channel. |
| Error -201107 | Selected lines do not support buffered operations if the C Series module is installed in the specified slot. Ensure only lines that support buffered operations are being used in the task. If using change detection timing, the task must be changed to nonbuffered to support these lines. Move your cDAQ module to a slot that supports buffered operations. |
| Error -201108 | Device does not support both analog modulation and digital modulation simultaneously. |
| Error -201109 | You cannot use the Ref In/Out connector as both an input and an output at the same time. |
| Error -201110 | Digital Modulation User Defined Waveform is invalid. |
| Error -201111 | Device does not support User Defined Waveform with OOK modulation. |
| Error -201112 | Device component test failed. If problem persists, contact National Instruments technical support at www.ni.com/support. |
| Error -201113 | Power level is too low. OOK modulation requires the bypass path to be used, and power levels this low must use the main path. |
| Error -201114 | Multi-device tasks with channels from both 446x and 447x devices require a 446x device to be in PXI slot 2. |
| Error -201115 | Waveform length must be a multiple of the waveform quantum. |
| Error -201117 | Property setting must be identical for all channels in the task. |
| Error -201118 | Operation must be performed on the entire task. It cannot be performed only on specific devices in the task. Do not use the indexer, Item property in Visual Basic, or index operator in C++ to specify device names when performing this operation. |
| Error -201119 | Next Write is Last property not settable if Regeneration Mode is set to Allow Regeneration. |
| Error -201120 | Property requested is incompatible with the given Timing Response Mode. NI-DAQmx can automatically select a compatible property value for you. To use the requested Timing Response Mode, do not set the specified property and allow NI-DAQmx to set it for you. To use the requested property value, choose a different value for the Timing Response Mode. |
| Error -201121 | Task cannot be reserved because the CPU does not support the Streaming SIMD Extensions (SSE). |
| Error -201122 | Property requested is incompatible with the given Timing Type. NI-DAQmx can automatically select a compatible property value for you. To use the requested Timing Type, do not set the specified property and allow NI-DAQmx to set it for you. To use the requested property value, chose a different value for the Timing Type. |
| Error -201123 | Device supports an analog channel as the source of an analog reference trigger only when it is the only channel from this device in the task. Remove all of the channels from this device in the task except the channel that you want to use as the analog trigger source, change the analog trigger source to a terminal, or select a channel from another device that only has one channel in the task. |
| Error -201124 | Only one task is permitted to have the Digital Output Memory Mapping for Programmed I/O Enable set to true at a time. If the value is unset, NI-DAQmx will choose a value that is compatible with the system while reserving the task. Do not set the property to true explicitly, set the property to false explicitly, or set the value to the default value to allow NI-DAQmx to choose a value that is compatible with the system. |
| Error -201125 | Channel properties conflict. If Analog Input Source is _aignd_vs_aignd, then Analog Input Coupling must be set to GND. If Analog Input Source is _external_channel, then Analog Input Coupling must be DC. |
| Error -201126 | DAQmx Timing property specified requires per device configuration. Explicitly specify the device(s) to which this property should apply. |
| Error -201127 | Your ratiometric device must use excitation for scaling. The Use Excitation for Scaling property cannot be set to false on this device. Use excitation for scaling by setting the Use Excitation for Scaling property to true. This will cause NI-DAQmx to return ratiometric data instead of voltage data which is not supported by ratiometric devices. |
| Error -201128 | Device index requested is invalid. The value of the index must be between one and the number of devices in the task. |
| Error -201129 | Memory Mapping for Programmed IO Enable cannot be set to true when Output Drive Type is Open Collector. Change Output Drive Type to Active Drive or change Memory Mapping for Programmed IO Enable to false. |
| Error -201130 | Memory Mapping for Programmed IO Enable setting is not compatible with some of the physical channels in the task. Change Memory Mapping for Programmed IO Enable to false or do not create the task with the incompatible physical channels. |
| Error -201131 | Reference and start trigger sources cannot be the same. Make the reference and start trigger sources different from one another. |
| Error -201132 | Attempted to write a sample beyond the final finite sample. The sample specified by the combination of position and offset will never be writable. Specify a position and offset which selects a sample up to but not beyond the final sample to generate. |
| Error -201133 | Device cannot be configured for input or output because lines and/or terminals on this device are in use by another task or route. This operation requires temporarily reserving all lines and terminals for communication, which interferes with the other task or route. If possible, use DAQmx Control Task to reserve all tasks that use this device before committing any tasks that use this device. Otherwise, uncommit or unreserve the other task or disconnect the other route before attempting to configure the device for input or output. |
| Error -201134 | Number of values specified with Pause Trigger Digital Pattern property does not match the number of physical lines requested with the Pause Trigger Digital Pattern Source property. Change one or both of the properties so the two numbers are equal. |
| Error -201135 | Reference Trigger Digital Pattern Source property can be used only with the data lines of the devices. Do not specify a PFI or a RTSI line in the pattern match source. |
| Error -201136 | Pause Trigger Digital Pattern Source property can only be used with the data lines of the devices. Do not specify a PFI or a RTSI line in the pattern match source. |
| Error -201137 | Start Trigger Digital Pattern Source property can only be used with the data lines of the devices. Do not specify a PFI or a RTSI line in the pattern match source. |
| Error -201138 | Task cannot be restarted because the first sample is not available to generate. |
| Error -201139 | Hardware revision is newer that the latest revision supported by the currently installed driver. Please upgrade your driver to the version supplied with the device. Driver updates can also be downloaded from ni.com. |
| Error -201140 | Currently installed driver no longer supports this revision of the hardware. Please downgrade your driver to the version supplied with the device. Older driver versions can also be downloaded from ni.com. |
| Error -201141 | EEPROM format is newer than the latest revision supported by the currently installed driver. Either self-calibrate your device (this may modify the EEPROM format) or upgrade your driver to the version supplied with the device. Driver updates can also be downloaded from ni.com. If uncertain, contact National Instruments technical support. |
| Error -201142 | Currently installed driver no longer supports the EEPROM format. Either self-calibrate your device (this may modify the EEPROM format) or downgrade your driver to the version supplied with the device. Older driver versions can also be downloaded from ni.com. If uncertain, contact National Instruments technical support. |
| Error -201143 | Hardware external calibration data format is newer than the latest revision supported by the currently installed driver. Either externally calibrate your device (this may modify the calibration data) or upgrade your driver to the version supplied with the device. Driver updates can also be downloaded from ni.com. If uncertain, contact National Instruments technical support. |
| Error -201144 | Hardware self-calibration data format is newer than the latest revision supported by the currently installed driver. Either self-calibrate your device (this may modify the calibration data) or upgrade your driver to the version supplied with the device. Driver updates can also be downloaded form ni.com. If uncertain, contact National Instruments technical support. |
| Error -201145 | Currently installed driver no longer supports the hardware external calibration data format. Either externally calibrate your device (this may modify the calibration data) or downgrade your driver to the version supplied with the device. Older driver versions can also be downloaded from ni.com. If uncertain, contact National Instruments technical support. |
| Error -201146 | Currently installed driver no longer supports the hardware self-calibration data format. Either self-calibrate your device (this may modify the calibration data) or downgrade your driver to the version supplied with the device. Older driver versions can also be downloaded from ni.com. If uncertain, contact National Instruments technical support. |
| Error -201147 | Calibration procedure has failed to resolve the calibration data format conflict. Perform a complete external calibration on your device. This may modify the calibration data. |
| Error -201148 | Channel you are triggering on is not enabled. Enable the trigger source channel. |
| Error -201149 | Number of input/output points entered for the specified channel is insufficient for calibration. At least two points are needed because this device has only gain error calibration constants and not offset calibration constants. Enter more points to eliminate this error. |
| Error -201150 | Simulated device cannot be imported to replace a non-simulated device of the same name. Change the device name in the import file and try importing again. |
| Error -201151 | PXI slot and PXI chassis numbers are required when creating a new simulated PXI device. Add PXI slot and chassis number values for the device in the import file. |
| Error -201152 | IsSimulated flags for SCXI chassis and SCXI modules must have the same value. Either make both simulated or make both non-simulated in the import file. |
| Error -201153 | Non-simulated SCXI module cannot be connected to a simulated digitizer. Change the SCXI Module IsSimulated flag or change the SCXI Module so that it connects to a digitizer with the same simulation setting. |
| Error -201154 | Non-simulated SCXI module cannot be connected to a simulated cabled device. Change the SCXI module IsSimulated flag or change the SCXI module so that it connects to a cabled device with the same simulation flag setting. |
| Error -201155 | SCXI module type specified does not support simulation. Remove the module from the import file or change the module type. |
| Error -201156 | IsSimulated flags for an SCC carrier and all of the contained modules must be set to the same value. Change the IsSimulated flags to match. |
| Error -201157 | Non-simulated SCC carriers cannot be connected to simulated devices. Change the cabled device of the SCC carrier or change the IsSimulated flags on the SCC carrier to true. |
| Error -201158 | IsSimulated flag for cDAQ chassis and C Series modules must match. Change the IsSimulated flags in the import file so that they match. |
| Error -201159 | cDAQ chassis does not have a slot that matches the specified slot number. The slot number specified is probably too large. Change the slot number to be a valid slot number. |
| Error -201160 | Device type specified does not support simulation. Remove the IsSimulated flag from the import file for this device or change the device type to one that supports simulation. |
| Error -201161 | Specified cDAQ chassis slot is already occupied by a C Series module. Change the slot numbers of the C Series modules in your import file so that they are unique. |
| Error -201162 | Physical channel cannot be used by the task because an output task has reserved this line and the Digital Input Tristate property is set to true. Set the Digital Input Tristate property to false. |
| Error -201163 | Physical channel cannot be used by the task because an input task has reserved this line to be tristated. |
| Error -201164 | Sample clock cannot be exported in this mode when the sample clock comes from an external source or an external timebase source. |
| Error -201165 | Firmware for this device is too new. Downgrade the firmware for this device. If you need help downgrading, visit ni.com/support. |
| Error -201166 | Firmware for this device is corrupt. Contact National Instruments for help with this device. |
| Error -201167 | Firmware for this device could not be updated. Contact National Instruments for help with this device. |
| Error -201168 | Firmware for this device is too old. Upgrade the firmware for this device. |
| Error -201169 | Device import failed because the device is not supported by the installed version and/or platform of NI-DAQmx. Change the device type or do not import this device. |
| Error -201170 | Device import failed because the device does not support simulation and a device to overwrite could not be found. Change the device type or do not import this device. |
| Error -201171 | Minimum temperature specified for the thermocouple measurement falls outside of the accuracy limit when using polynomial scaling. Specify a value greater than the minumum temperature for polynomial scaling with this thermocouple type, or set the Thermocouple Scale Type property to Table. |
| Error -201172 | AI channels on this device do not support using DC coupling while using IEPE excitation. Set excitation source to none or the coupling mode to AC. |
| Error -201173 | Power supply configuration failed. Reboot or cycle the power on the device. |
| Error -201174 | SCXI-1600 does not support import through MAX. Deselect the SCXI-1600 in the import dialog or remove it from the import file. |
| Error -201175 | Dev.AssociatedResourceIDs property is not supported by the device. Remove the Dev.AssociatedResourceIDs property from the import file. |
| Error -201176 | Sample clock rate specified is too fast for the burst handshaking timing type. Change the sample clock rate to be equal to or less than the maximum value or consider using the pipelined sample clock timing type. If you use the pipelined sample clock timing type, refer to the device documentation for the differences between the burst handshake timing type and the pipelined sample clock timing type. |
| Error -201177 | Device is not usable. The firmware was recently upgraded, and the system was not powered down and restarted. Power down the computer and restart. |
| Error -201178 | Sample clock rate specified is too fast for the sample clock timing type. Change the sample clock rate to be equal to or less than the maximum value or consider using the pipelined sample clock timing type. If you use the pipelined sample clock timing type, refer to device documentation for the differences between the sample clock timing type and the pipelined sample clock timing type. |
| Error -201179 | db reference value must be greater than zero. |
| Error -201180 | Input cal data point must be an AC Voltage for this module. |
| Error -201181 | Input source in not valid. Ensure that AI Input Source and AI Coupling are not both set for the same task. |
| Error -201182 | Internal excitation voltage selected for calibration is not valid. |
| Error -201183 | Internal excitation frequency selected for calibration is not valid. |
| Error -201184 | Device specified for PXI backplane communication is not a PXI device. |
| Error -201185 | Device specified for PXI backplane communication is not in the PXI chassis. |
| Error -201186 | Device specified for PXI backplane communication is not in the rightmost slot of the PXI chassis. |
| Error -201187 | Cold junction compensation channel cannot be used unless the corresponding analog input channel is configured to measure temperature using a thermocouple. Use the thermocouple version of the DAQmx Create Channel VI/function to configure the channel. |
| Error -201188 | Onboard device memory overflow. Because of system and/or bus bandwidth limitations, the driver could not read data from the device fast enough to keep up with the device throughput. Reduce the number of programs your computer is executing concurrently or use a different computer to calibrate your device. |
| Error -201189 | Onboard device memory overflow. Because of system and/or bus bandwidth limitations, the driver could not read data from the device fast enough to keep up with the device throughput. This device supports high-speed (480Mb/s) USB but it is connected to a full-speed (12 Mb/s) USB port. Connect this device to a high-speed (480 Mb/s) USB port, reduce the number of programs your computer is executing concurrently, or use a different computer to calibrate your device. If you are using a USB hub, ensure that it supports high-speed operation. |
| Error -201190 | Device is currently not usable and must be placed into firmware loader mode. Unplug the device USB cable and plug it back in. If the device is plugged into a USB hub, ensure that you unplug the device from the hub. |
| Error -201191 | Property specified is not supported unless excitation is enabled. Enable excitation before attempting to access the property. |
| Error -201192 | Connection to target failed for the requested configuration operation. Confirm that NI-DAQmx is installed on the target. |
| Error -201193 | SCXI chassis address specified is invalid. Specify an SCXI chassis address between 0 and 31. |
| Error -201194 | Property cannot be read before reading the corresponding Channels Exist property. NI-DAQmx retrieves the channel state from the hardware when the application reads the corresponding Channels Exist property. After reading the corresponding Channels Exist property, you can retrieve other information about these channels. |
| Error -201195 | PCI Express interface layer error detected. Contact National Instruments for support. |
| Error -201196 | PCI Express interface layer error detected. Contact National Instruments for support. |
| Error -201197 | Circuit connected to the prototyping board causes channels to use too much power. Those channels were disabled to prevent the device from using too much power. Turn the prototyping board power switch to the off position; correct the circuit connected to the prototyping board; then turn the prototyping board power switch back on. |
| Error -201198 | Circuit connected to the prototyping board causes a short between the specified physical channel and the voltage source. The output of the function generator has been suspended to prevent the device from using too much power. Turn the prototyping board power switch to the off position; correct the circuit connected to the prototyping board; then turn the prototyping board power switch back on. |
| Error -201199 | Circuit connected to the prototyping board causes too much power to be drawn from the specified source. The output of the source has been suspended to prevent the device from using too much power. Turn the prototyping board power switch to the off position; correct the circuit connected to the prototyping board; then turn the prototyping board power switch back on. |
| Error -201200 | Requested operation could not be completed because the prototyping board has been removed or disabled. The prototyping board can be disabled by either switching the prototyping board switch to the off position, or by an incorrect connection on the prototyping board causing too much power to be drawn from the device. Ensure that all connections on the prototyping board are correct and that the prototyping board is properly inserted and powered on before attempting the operation. |
| Error -201201 | Offset error measured for this calibration task is out of range for the device. Ensure that the reference voltage is accurate, specified correctly, and connected to the correct channel. Also ensure that the measured output voltage is specified correctly and that the device is functioning properly. |
| Error -201202 | Gain error measured for this calibration task is out of range for the device. Ensure that the reference voltage is accurate, specified correctly, and connected to the correct channel. Also ensure that the measured output voltage is specified correctly and that the device is functioning properly. |
| Error -201203 | Virtual channel specified does not support the strain gage shunt calibration procedure. |
| Error -201204 | Virtual channel specified does not support the Wheatstone bridge shunt calibration procedure. |
| Error -201205 | Device simulation flag does not match the simulation flag of the RTSI cable. |
| Error -201206 | Task cannot contain a mixture of simulated devices and physical devices. Ensure the physical channels added to the task refer to all physical devices or all simulated devices. |
| Error -201207 | Active Device cannot be specified when reading or writing timing properties in this multidevice task, due to synchronization requirements. |
| Error -201208 | Sample rate specified is too fast for the ADC Timing Mode selected for this device. Decrease the sample rate or use a faster ADC Timing Mode. |
| Error -201209 | Waveform length is too small for the "generate" instruction before "break" block. |
| Error -201210 | Waveform subset length is too small for the "generate" instruction before "break" block. |
| Error -201211 | Wait duration is too small for the "wait" instruction before "break" block. |
| Error -201212 | Waveform length is too small for the "generate" instruction in "break" block. |
| Error -201213 | Waveform subset length is too small for the "generate" instruction in "break" block. |
| Error -201214 | Wait duration is too small for the "wait" instruction in "break" block. |
| Error -201215 | Marker position specified is either too close to the end or the beginning of the waveform, or too close to another marker in the "generate" statement in "break" block. |
| Error -201216 | "Wait until trigger" instruction not allowed in a "break" block. |
| Error -201217 | "Repeat until trigger" instruction not allowed in a "break" block. |
| Error -201218 | "If-Else" block not allowed in a "break" block. |
| Error -201219 | "Break" block cannot be nested in other "break" blocks. |
| Error -201220 | "Clear trigger" instruction not allowed in a "break" block. |
| Error -201221 | "Break" blocks are not allowed in finite or conditional loops. |
| Error -201222 | "Generate" or finite "wait" instruction expected before a "break" block. |
| Error -201223 | Tristate setting must be identical for all lines in the port. |
| Error -201224 | Tristate setting must be applied to all lines in the port. Include all lines in the port in the Active Channel list. |
| Error -201225 | Change detection timing cannot be used on this device while Memory Mapping for Programmed IO is enabled. Set MemMapEnable to false or use a different timing type. |
| Error -201226 | Memory Mapping for Programmed IO Enable setting must be the same for all virtual channels in the task. |
| Error -201227 | Timing engine requested can only be used with lines that span two contiguous ports. Use the default timing engine for the specified physical channels, use some lines from two contiguous ports, or use all of the physical data channels on the device. |
| Error -201228 | Watchdog timer task could not be created because one of the digital output lines in the task uses memory mapping for programmed I/O. Set DO.MemMapEnable to false for all lines in the task, or do not use a watchdog timer task. |
| Error -201229 | Memory mapping for programmed I/O cannot be enabled for the specified lines because a watchdog timer task uses these lines. Set DO.MemMapEnable to false for all lines in the task, or do not use a watchdog timer task. |
| Error -201230 | Simulation flag of the referenced device does not match the simulation flag of the target. |
| Error -201231 | Local channel is not referenced by the task specified in the local channel name. |
| Error -201232 | Target storage was altered by another process before the changes could be saved. |
| Error -201233 | Object specified could not be found in storage. |
| Error -201234 | Storage specified is not valid or could not be found. |
| Error -201235 | Required object dependency was not found in storage. |
| Error -201236 | Communication mode specified is not valid for the SCXI Chassis. |
| Error -201237 | Physical channel name specified is invalid. Physical channel names are of the form <device name>/<physical channel name>, for example, dev1/ai0. |
| Error -201238 | SCXI digitization is not supported by the device or physical channel. |
| Error -201239 | SCXI multiplexed digitization is not supported by the device. |
| Error -201240 | Digitization mode specified is not supported by the SCXI module. |
| Error -201241 | Connector 0 on the SCXI chassis communication device must be cabled to the SCXI module. |
| Error -201242 | SCXI chassis communication is not supported by the device. |
| Error -201243 | Address specified is invalid. |
| Error -201244 | Module type in the source storage does not match the module type in the destination. |
| Error -201245 | User defined information string entered exceeds the maximum allowable string length. |
| Error -201246 | Device cannot be created in MAX because the carrier contains no cartridge. Plug in a cartridge and attempt to create the device again. |
| Error -201247 | Device cannot be created in MAX because a driver could not be found for the device. You may need to upgrade NI-DAQmx. |
| Error -201248 | Device configuration may not be changed at this time because the device is locked. |
| Error -201249 | Wireless security setting is invalid. Ensure that all necessary settings are specified. |
| Error -201250 | Connection to the network device has timed out. The network device did not respond properly for a period of time. If timeouts persist, contact your system administrator. |
| Error -201251 | Device could not be found on the network. This usually indicates an incorrect hostname or a DNS failure. |
| Error -201252 | Device cannot be reached because no known route to the device exists on the network. |
| Error -201253 | Network is currently unavailable. This usually indicates an unplugged network cable, a failing network component, or an improperly configured network. |
| Error -201254 | Serial numbers of the network device do not match the serial numbers NI-DAQmx expected. Replace the original device or module and try again, or use the reconnect button in MAX to locate the original device. |
| Error -201255 | EEPROM of this device has changed since this task began. Restart the task or reset the device to refresh the EEPROM contents. |
| Error -201256 | Wireless channel specified is not available for this country code configuration. |
| Error -201257 | Country code is not configured. This setting is required to determine available wireless channels. |
| Error -201258 | Wireless configuration has been rejected by the device. |
| Error -201259 | Network configuration has been rejected by the device. |
| Error -201260 | Manual control attribute cannot be read when manual control is disabled. Enable manual control before reading this attribute. |
| Error -201261 | Sample clock rate cannot be changed at this time. When changing the Sample clock rate for a running task, one full period of the Sample clock must complete at the previous rate before NI-DAQmx can safely update the timing circuitry. |
| Error -201262 | Property specified is not supported for the bus type of the device. |
| Error -201263 | Firmware for this device could not be downloaded. To retry downloading the firmware, unplug the device and plug it back in. If this problem continues, contact National Instruments for assistance. |
| Error -201264 | Scaled waveform is too large. After multiplication by the software scaling factor, the magnitude of each sample must be less than 1.0. |
| Error -201265 | Input voltage limits exceeded. Protection circuity disabled the inputs. Ensure proper voltage levels on device inputs. |
| Error -201266 | Property requested was not found. The property is either not supported by the object or has not been set. |
| Error -201267 | User defined information string entered is of an invalid length. |
| Error -201268 | Current limit specified cannot be applied to the channel because all current limit resources on the device have been reserved. Use a current limit setting that is already in use for another channel, or free a current limit resource by disabling current limiting on all channels that use a common current limit. |
| Error -201269 | Calibration operation cannot be completed unless the prototyping board is powered on. |
| Error -201270 | Certificate provided is not in PEM (Privacy Enhanced Mail) format. Only PEM certificates are supported. |
| Error -201271 | Product at the address provided was not the expected type. This may be due to a module being replaced or IP addresses on the network being reassigned. Reconnect to the device in MAX or delete it from your system and rediscover it. |
| Error -201272 | IP address provided is invalid. IP addresses must be of the form x.x.x.x where x is a number from 0 to 255. |
| Error -201273 | Network device is already in use by another host. |
| Error -201274 | Device specified is not supported in 64-bit applications. To use this device, configure your development environment to create a 32-bit application, or use a 32-bit development environment. Refer to the documentation for your development environment for more information. |
| Error -201275 | Device cannot be calibrated using the coupling specified. Calibrate using a different coupling mode. |
| Error -201276 | Certificate provided is not in PEM (Privacy-enhanced Electronic Mail) or DER (Distinguished Encoding Rules) format. Only PEM or DER certificates are accepted. |
| Error -201277 | Certificate file is too large to transfer to the device. |
| Error -201278 | Consecutive writes to a digital line occurred more frequently than the device can safely allow. |
| Error -201279 | Coupling specified conflicts with the Measurement Type of the channel. Configure the channel to use a coupling appropriate for the measurement and sensor. For example, use DC coupling for DC sensors. |
| Error -201280 | Vertical Offset is not supported by this device. |
| Error -201281 | Device does not support using more than one trigger at a time. Configure the device to use only one trigger, or use a device that supports using multiple triggers. |
| Error -201282 | Device power up failed. Try resetting the device. If the error persists contact National Instruments. |
| Error -201283 | Internal serial communication bus failed. Try resetting the device. If the error persists, contact National Instruments. |
| Error -201284 | Improper chassis power levels detected. The +3.3 V fuse on the device might have blown, or there might be a problem with the +3.3 V rail on the chassis. Try resetting the device. If the error persists, contact National Instruments. |
| Error -201285 | Improper chassis power levels detected. The +5 V fuse on the device might have blown, or there might be a problem with the +5 V rail on the chassis. Try resetting the device. If the error persists, contact National Instruments. |
| Error -201286 | Improper chassis power levels detected. The +12 V fuse on the device might have blown, or there might be a problem with the +12 V rail on the chassis. Try resetting the device. If the error persists, contact National Instruments. |
| Error -201287 | Improper chassis power levels detected. The -12 V fuse on the device might have blown, or there might be a problem with the -12 V rail on the chassis. Try resetting the device. If the error persists, contact National Instruments. |
| Error -201288 | Property specified cannot be set while the task is reserved. Set the property prior to reserving the task or unreserve the task prior to setting the property. |
| Error -201289 | Calibration procedure for your device does not support shorted inputs. Refer to the calibration procedure for your device for more information. |
| Error -201290 | WEP key must be either 10 or 26 characters long. |
| Error -201291 | Pulse specifications cannot be written to a finite counter output task on this device. |
| Error -201292 | Sample Clock Overrun and Underflow Behaviors must be set to consistent values. Either set Overrun Behavior to Stop Task and Error and Underflow Behavior to Halt Output and Error, or set Overrun Behavior to Ignore Overruns and Underflow Behavior to Pause Until Data Available. |
| Error -201293 | Device could not complete the calibration operation. Calibration could fail for the following reasons: 1. The actual reference signal applied for calibration was different from the value you specified. Ensure that the reference signal applied is the same as the values that were input. 2. The reference signal was not stable over the period of time that the hardware was being calibrated. Ensure that the reference signal specified is free of noise and does not drift over the duration of the calibration. 3. The device is not functioning properly. |
| Error -201294 | Device could not complete the calibration operation. Calibration could fail for the following reasons: 1. The actual reference signal applied for calibration was different from the value you specified. Ensure that the reference signal applied is the same as the values that were input. 2. The reference signal was not stable over the period of time that the hardware was being calibrated. Ensure that the reference signal specified is free of noise and does not drift over the duration of the calibration. 3. The device is not functioning properly. |
| Error -201295 | Device could not complete the calibration operation. Calibration could fail for the following reasons: 1. The actual reference signal applied for calibration was different from the value you specified. Ensure that the reference signal applied is the same as the values that were input. 2. The reference signal was not stable over the period of time that the hardware was being calibrated. Ensure that the reference signal specified is free of noise and does not drift over the duration of the calibration. 3. The device is not functioning properly. |
| Error -201296 | Sample Timing Type specified is not supported for counter output tasks on this device. Change the Sample Timing Type to Implicit. |
| Error -201297 | Sample and hold is not supported for SCXI modules in parallel mode using digitizer channels other than 0 through 7. Disable sample and hold, use only digitizer channels 0 through 7, or use multiplexed mode. |
| Error -201298 | Property specified is not supported in conjunction with a conflicting property. |
| Error -201299 | Log Only mode is only supported for buffered tasks. Either use Log and Read mode or configure the task as Finite or Continuous. |
| Error -201300 | Property specified is not supported when logging data. |
| Error -201301 | Reading samples is not supported in the specified logging mode. To access the samples while logging, either open the file being written to or use a different logging mode. |
| Error -201302 | File permission error. You do not have the correct permissions for the file. |
| Error -201303 | Logging to this file format is not supported by NI-DAQmx. Convert the file to TDMS version 2.0 or later, or specify a different file. |
| Error -201304 | File path specified is invalid, or the file is not a valid TDMS file. Specify the location of a valid TDMS file. |
| Error -201305 | Disk is full. Free up disk space, or specify a different file path. |
| Error -201306 | File specified is already opened for output by another task. Specify a different file path. |
| Error -201307 | Logging is not supported for this measurement type. Change the measurement type in order to use logging. |
| Error -201308 | Logging is not supported for finite counter tasks on this device. Change the Sample Mode of the task to continuous. |
| Error -201309 | Unable to write to disk. Ensure that the file is accessible. If the problem persists, try logging to a different file. |
| Error -201310 | TDMS support is not installed or is too old. Use an NI-DAQmx runtime that includes TDMS support, or install a supported version of TDMS from a stand-alone installer. |
| Error -201311 | File specified is already opened for output. NI-DAQmx requires exclusive write access. |
| Error -201312 | Logging is not supported for this channel and/or measurement type. Use a different measurement type or channel. |
| Error -201313 | Non-responsive counter detected. NI-DAQmx reset the counter. Counter timebases at the specified speed must remain periodic, otherwise the counter can become non-responsive. Use an internal timebase or an external timebase that remains periodic. |
| Error -201314 | Multiple Sample Clock pulses were detected within one period of the input signal. Use a Sample Clock rate that is slower than the input signal. If you are using an external Sample Clock, ensure that clock signal is within the jitter and voltage level specifications and without glitches. |
| Error -201315 | Events cannot be configured after writing samples to the task. |
| Error -201316 | Timebase specified is too fast for a hardware-timed single-point counter output task. |
| Error -201317 | Multiple counters are not allowed in a buffered counter output task. |
| Error -201318 | Sample Clock pulse occurred before a pulse could be generated using the previous pulse specification. Use a Sample Clock that is slower than the pulse train you want to generate. |
| Error -201319 | Sample Clock pulse occurred before the previous sample was acquired from all channels in the task. Use a Sample Clock rate that allows time for the device to acquire samples from all channels. If you are using an external Sample Clock, ensure that clock signal is within the jitter and voltage level specifications and without glitches. |
| Error -201320 | Retriggering can only be enabled for finite task with a Start trigger configured. |
| Error -201321 | Memory-mapped task detected data corruption because the memory was accessed by another program, such as a debugger or virus scanner. Disable other programs that might access this memory, or disable memory mapping for the task. |
| Error -201322 | Memory mapping must be the same setting for all simultaneous tasks that use channels from a single subsystem. |
| Error -201323 | Sample Clock timing is not supported when using a two-counter measurement method. Use a one-counter measurement method, or use a different timing type. |
| Error -201324 | Multiple counters are not allowed in a single counter output task when using Sample Clock timing. |
| Error -201325 | Module specified cannot be used as the first stage of a dual -stage analog input channel. |
| Error -201326 | Module specified cannot be used as the second stage of a dual-stage analog input channel. |
| Error -201327 | Modules specified are not valid for dual-stage analog input channels. |
| Error -201328 | Second stage of a dual-stage analog input channel cannot be empty. |
| Error -201329 | Data Transfer Mechanism must be DMA when Sample Mode is Hardware Timed Single Point on this device. |
| Error -201330 | Pulse train specifications cannot be modified while the task is running if Auto Increment Count is greater than 0 |
| Error -201331 | Memory mapping is not supported on this device for non-buffered tasks using Sample Clock timing. Disable memory mapping or change the buffer size. |
| Error -201332 | Logging is not supported for output tasks. |
| Error -201333 | Required scaling parameter has not been specified. |
| Error -201334 | Linear scaling requires unique electrical and physical values. |
| Error -201335 | Table scaling requires the same number of electrical values as physical values. |
| Error -201336 | Bridge scales are not supported for this measurement type. Use a custom scale for additional scaling. |
| Error -201337 | Device names must be 254 characters or shorter. |
| Error -201338 | Shunt resistor location specified is not valid for this calibration procedure. |
| Error -201339 | External timebase rate specified is too fast for this device. Reduce the timebase rate to less than 1/4 the device oscillator frequency. |
| Error -201340 | Firmware on the device is out of date. Use Measurement & Automation Explorer to update the device firmware. |
| Error -201341 | Accessory cannot be connected while the task runs. The accessory uses different scaling or is unsupported. Ensure the accessory is seated properly and restart the task. |
| Error -201342 | Unsupported accessory is connected to the module. Insert a supported accessory and restart the task. |
| Error -201343 | Overcurrent detected in the power supply for the accessory connected to the module. Check the external wiring and ensure the accessory, if present, is properly seated. Then, reset the module using DAQmx Reset Device or Measurement & Automation Explorer. |
| Error -201344 | ADC Timing Mode property was set to Custom, but the Custom Timing Mode property was not set. Specify a value for Custom Timing Mode or change the ADC Timing Mode. |
| Error -201345 | Custom Timing Mode property is not supported unless the ADC Timing Mode property is set to Custom. Set ADC Timing Mode to Custom before setting Custom Timing Mode. |
| Error -201346 | Synchronization Type cannot be Slave without configuring the device to use an external Sync Pulse. Set the Synchronization Type to Master or configure the device to use an external Sync Pulse. |
| Error -201347 | Sync Pulse was not detected before attempting to start the task. Ensure you connected the source of the Sync Pulse to the device. |
| Error -201348 | Retriggered counter tasks do not support trigger skew correction. Set the Synchronization Type to Default or disable retriggering. |
| Error -201349 | Multidevice tasks using the specified devices do not support a Start Trigger and Reference Trigger from different devices. Using triggers from different devices can cause unwanted latency or incorrect behavior. Use triggers from a single device or manually synchronize the devices. |
| Error -201350 | Synchronization Type cannot be Slave unless you configure the device to use a trigger with an external source. Configure an external trigger or set Synchronization Type to None or Master. |
| Error -201351 | Memory mapping is not supported by this device for on-demand acquisitions. |
| Error -201352 | Analog bus line(s) in use by another device. Verify other devices are not currently using the analog bus line(s). If you intend to share the line(s) between devices, ensure the Analog Bus Sharing Enabled property is True for all shared channels. |
| Error -201353 | Analog bus needed by the current operation is invalid. Verify that all carriers connected using expansion bridge(s) are functioning properly. |
| Error -201354 | Cards specified cannot be used to create a SwitchBlock device. Use the current set of cards as single-card devices, or use a different set of cards to create a valid combination. |
| Error -201355 | Switch device has been disabled to prevent it from exceeding the power limit for the carrier. To recover, call DAQmx Disconnect All, or reset the device. The device can be reset either programmatically or by using Measurement & Automation Explorer. Refer to your device documentation for more information. |
| Error -201356 | Topology specified is not supported by this card. |
| Error -201357 | Device must consist of at least one card. |
| Error -201358 | Simulation flag must be the same for the cards, devices, and carrier. |
| Error -201359 | Multicard devices must consist of cards contained in the same carrier. |
| Error -201360 | Carrier slot number specified for the card is invalid. |
| Error -201361 | Sync pulse cannot originate from the specified device for this combination of devices. |
| Error -201362 | Analog reference trigger and sync pulse must come from the same device. |
| Error -201363 | Minimum and maximum values specified are outside the bounds of the specified physical values for the table. Change the table or the minimum and maximum value appropriately. |
| Error -201364 | Trigger detected that could not be acted upon by the device. Slow down your trigger source. |
| Error -201365 | Onboard regeneration cannot be used when there are more than 16 channels in the task. Reduce the number of channels in the task or set Use Only Onboard Memory to false. |
| Error -201366 | Reference Clock signal was not found at the specified source. |
| Error -201367 | Filtering or digital synchronization of an internal signal is not supported by the device. |
| Error -201368 | Invalid number of calibration adjustment points provided. Use DAQmx Adjust Calibration to provide calibration points for the device. |
| Error -201369 | Hostname specified is in use by another device. |
| Error -201370 | IP address specified is in use by another device. |
| Error -201371 | Multicast DNS service instance specified is in use by another device. |
| Error -201372 | Open thermocouple condition detected on thermocouple channel(s) you are attempting to calibrate. Ensure thermocouples are properly connected and functioning before performing lead offset nulling calibration. |
| Error -201373 | Output peer-to-peer streaming with the Stream statement is not allowed in a script with If Else, Repeat Until, or Break statements. |
| Error -201374 | Self-calibration failed. Performing an external calibration may fix the problem. |
| Error -201375 | Thermocouple lead offset nulling calibration is not supported by the specified channels. Make sure the device supports thermocouple lead offset nulling calibration. Make sure all channels are thermocouple channels. Make sure open thermocouple detection is enabled. Set skip unsupported channels to true. |
| Error -201376 | Data read from the EEPROM on the accessory attached to the device is invalid. Verify that any accessories configured with this device are connected. If the problem continues, contact National Instruments technical support. The device might need to be recalibrated or repaired by NI. |
| Error -201377 | Device is unusable while firmware update is in progress. |
| Error -201378 | Firmware version requested was not found on the system. |
| Error -201379 | Network devices are not supported on this platform. |
| Error -201380 | The requested operation is not supported by this device. |
| Error -201381 | One or more connections to external power rails are drawing too much power. The operation has been aborted to prevent the device from using too much power. Remove the connection(s) to the external power rails and restart your task. |
| Error -201382 | The file write size specified is not evenly divisible by the volume sector size. |
| Error -201383 | The file write size specified is too large. Performance can suffer if the file write size is larger than one-fourth the size of the buffer length. |
| Error -201384 | The simulated C Series module is not supported on this simulated chassis. |
| Error -201385 | Self-calibration failed to converge. Performing an external calibration may fix the problem. |
| Error -201386 | Self-calibration failed. Contact National Instruments technical support at ni.com/support. |
| Error -201387 | The DAQmx Adjust DSA AI Calibration with Gain and Coupling function/VI was executed more than once for the same combination of gain and coupling settings. Call the DAQmx Adjust DSA AI Calibration with Gain and Coupling function/VI only once for the following combination of gain and coupling settings: |
| Error -201388 | Network device is not reserved for this host. |
| Error -201389 | Modules were inserted or removed while the connection to the network device was lost. Reset the chassis using DAQmx Reset Device or Measurement & Automation Explorer and wait for the modules to be redetected before proceeding. |
| Error -201390 | Connection to the network device was lost. This can indicate an unplugged network cable, a failing network component, or a network device that is reserved by another host. |
| Error -201391 | Device could not complete calibration because calibration was not performed for all gain and coupling settings. Use DAQmx Adjust DSA AI Calibration function/VI to calibrate for the following gain and coupling settings: |
| Error -201392 | Device does not support configuring tristate logic level in software. |
| Error -201393 | Tristate logic level is not supported on output only lines. |
| Error -201394 | Tristate logic level is only port configurable for this device. |
| Error -201395 | The task is not buffered or has no channels. If the task is not buffered, use the scalar version of this function. If the task has no channels, add one to the task. |
| Error -201396 | Filter Delay Removal is not supported when an analog start trigger is in use. Change Filter Delay Removal to false when using an analog start trigger. Refer to Filter Delay Removal in your DSA documentation for more details. |
| Error -201397 | Change detection has detected interrupts occurring at a higher rate than can be handled. The change detection task has been stopped to prevent the device from being reset because of this condition. If this is the result of unwanted noise on a digital signal, use a digital filter to eliminate unwanted digital transitions. |
| Error -201398 | Requested value is not supported for this property. If you did not directly set this property to the unsupported value, check other properties that you have set, as they can influence the scaled value of this property. |
| Error -201399 | Multi-device timed DIO tasks require all modules to be the same type. You can select either all your serial digital modules or all your parallel digital modules in this task. |
| Error -201400 | Failed to reserve file size. File size pre-allocation might require you to run the application with administrator privileges. If the operating system uses User Account Control, configure this control properly. |
| Error -201401 | Retrieving properties from the network device failed. Make sure the device is connected. |
| Error -201402 | The samples per file specified is not evenly divisible by the file write size. Either change the samples per file or modify the file write size. If not explicitly set, the file write size can be inferred from the buffer size, which is based on the sample rate. |
| Error -201403 | You have specified a new file path but did not call DAQmx Start New File. To change the file path while logging, configure Logging.SampsPerFile or call DAQmx Start New File. |
| Error -201404 | One or more cards for your NI SwitchBlock device have been inserted and/or removed while your system was powered on. This can lead to unexpected behavior. Restart your system. |
| Error -201405 | An expansion bridge has been inserted or removed while your system is powered on. This can lead to unexpected behavior. Restart your system. |
| Error -201406 | The 5 V fuse on your NI SwitchBlock carrier is blown. Refer to your documentation for help with replacing the fuse. |
| Error -201407 | Specified property is not supported unless Sample Mode is set to Hardware Timed Single Point. |
| Error -201408 | Averaging of data is only supported when the Sample Mode is set to Hardware Timed Single Point and the Sample Clock source is external to the device. |
| Error -201409 | The requested delay from Sample Clock is out of range for a hardware-timed single-point acquisition. |
| Error -201410 | The requested Sample Clock rate is too fast for hardware-timed single point. Consider decreasing the Sample Clock rate, increasing the convert rate, or decreasing the delay from the Sample Clock. If using an external Sample Clock source, you might also decrease the number of samples to average. |
| Error -201411 | The accessory attached to the device does not support connections. Attach an accessory that supports connections. |
| Error -201412 | The specified accessory channels are not present on this device. The accessory channels should be specified for the device in the calibration session. |
| Error -201413 | There is no accessory attached to the device. |
| Error -201414 | The specified connection is not supported on the attached accessory. Refer to your accessory documentation for supported connections. |
| Error -201415 | The module is not supported by the NI 9163. |
| Error -201416 | Switch device has been disabled to prevent it from exceeding its simultaneous relay drive limit. To recover, disconnect a relay or channel. |
| Error -201417 | Timing is configured without supplying a clock signal. Either supply an external clock or use an internal timebase. |
| Error -201418 | Device firmware has not been updated because the firmware file uploaded is corrupt or is not a valid firmware image file. Please verify that the file specified is a valid National Instruments firmware image. |
| Error -201419 | Device firmware has not been updated because the firmware file uploaded is for a different type of device or an older revision of this device. Please verify that the firmware file is correct for this device. |
| Error -201420 | The network device is currently reserved by another host. Specify whether you want to override the other host's reservation. |
| Error -201421 | The accessory attached to the device does not support this property. |
| Error -201422 | Your SwitchBlock carrier contains one or more cards with power characteristics unknown to the driver. To protect the hardware from overheating, all devices within your carrier are disallowed from drawing power. Upgrade your software driver to the latest version or shutdown your system and remove any unknown or invalid card(s). |
| Error -201423 | Communication with the chassis has been interrupted. Check the cabling and/or the wireless signal to the chassis. Then reset the chassis using DAQmx Reset Device or Device Reset in MAX to re-establish communication. |
| Error -201424 | The multidevice task cannot be synchronized in its current configuration. |
| Error -201425 | The multidevice task does not have a method for synchronizing timing that is compatible with all of the included devices. |
| Error -201426 | One or more devices do not support multidevice tasks. |
| Error -201427 | The specified device is not supported within the NI-DAQmx API. |
| Error -201428 | More than one sync pulse was detected. For proper operation, only a single sync pulse signal can be provided to all DSA modules in a task. |
| Error -201429 | Start trigger delay is not available when a C Series Delta-Sigma module or a Reference Clock module is in the task. |
| Error -201430 | You have requested an invalid number of reference voltages to write. Ensure the number of values to write is the same as the number of entries in the array. |
| Error -201431 | Calibration offset adjustment has failed because the wrong channel was selected. Check the module calibration procedure to decide which channel to use for the calibration offset adjustment. |
| Error -201432 | Calibration adjustment cannot be completed on a device performing different types of measurements (for instance, voltage and current measurements). Make sure only one measurement type is being calibrated in each calibration session. |
| Error -201433 | Write failed because a watchdog timer task expired and changed the direction of the lines to tristate after the digital output task was committed. To avoid this, unreserve and recommit the digital output task after the watchdog timer expiration has been cleared to reconfigure the lines to output. |
| Error -201434 | Configuration failed because the task tried to change the direction of a line while the watchdog timer is expired. Clear the expiration of the watchdog timer task before trying to change the direction of any line, even if the line is not watched by the watchdog timer task. |
| Error -201435 | No samples provided to DAQmx Write to initialize buffered generation. |
| Error -201436 | Unable to route signals through the analog bus that are composed of different wire modes. Please disconnect any devices of different wire modes from the analog bus before routing this device through the analog bus. |
| Error -201437 | The timeout value specified exceeds the maximum timeout value supported by this device. |
| Error -201438 | The device was rebooted after a watchdog timer expired due to unresponsive firmware or hardware components. A watchdog timer that times out can cause digital output lines to change state. To clear this error, reset or power cycle the device. Please also contact National Instruments technical support. |
| Error -201439 | Retriggering is not allowed for finite Sample Clock-timed counter output tasks. Reconfigure the task to use a different sample timing type or disable retriggering. |
| Error -201440 | Neither an external reference clock nor a sample clock timebase has been specified. For multi-device synchronization, you must specify the sync pulse source and either an external reference clock or sample clock timebase. Refer to the device documentation for details on multi-device synchronization. |
| Error -201441 | On an NI 449x, specify either the sync pulse source or the sample clock timebase source but not both. |
| Error -201442 | Cannot measure two-edge separation with both the first and second terminal set to the same signal and both the first and second edge set to the same edge. To measure the period of a signal, use a counter input period task. Otherwise, change one of the terminals to a different signal, or change one of the edges to be different from the other. |
| Error -201443 | FREQOUT counter cannot generate the desired frequency. The 4-bit FREQOUT counter can divide the 20 MHz, 10 MHz (20 MHz / 2), or 100 kHz (20 MHz / 200) timebase by a number between 1 and 16. Choose a frequency within this range. |
| Error -201444 | Multidevice tasks cannot use the on-demand sample timing type. Configure timing to synchronize and acquire samples from multiple devices. |
| Error -201445 | You must configure strain gage channels for each arm of the rosette. Specify the strain gage channel names. |
| Error -201446 | Each tee rosette requires two physical channels. Make sure the physical channel list contains two physical channels for each tee rosette. |
| Error -201447 | The selected rosette requires three physical channels. Make sure the physical channel list contains three physical channels for each rosette. |
| Error -201448 | No rosette measurements specified. Please specify one or more rosette measurements. |
| Error -201449 | The requested port connection string is not in a valid format. The valid format is <device name>/port<port number> (e.g. Dev1/port2). |
| Error -201450 | The requested device does not support cDAQ Sync connections. |
| Error -201451 | The operation cannot be completed on only one port. Two ports are required. |
| Error -201452 | The operation has been aborted. |
| Error -201453 | Cannot find disconnected connections between devices in different states (present and simulated). Please check requested set. |
| Error -201454 | Carrier physically unable to contain the declared cards. |
| Error -201455 | cDAQ Sync connections are not allowed between physical and NI-DAQmx simulated devices. Use cDAQ Sync for either only physical devices or only NI-DAQmx simulated devices. |
| Error -201456 | The devices attempting to be configured for cDAQ Sync do not have a common sync connection strategy. |
| Error -201457 | cDAQ Sync cannot add a connection from a port to the same port. Add a connection to a different port instead. |
| Error -201458 | Specified timeout value is not supported. Set the timeout to to a value > 0 or -1 (wait infinitely). |
| Error -201459 | Specified devices do not support cDAQ Sync connections. Please select a different set of devices. |
| Error -201460 | No devices scanned support cDAQ Sync connections. Requesting an empty string only scans physical devices (present and offline) and ignores NI-DAQmx simulated devices. Please check your hardware configuration. |
| Error -201461 | Reference clock is not present. This task requires a reference clock to be present before configuring hardware. |
| Error -201462 | The attempted connection is not between an output port and an input port. Port 0 is input only. All other ports are output only. Please check your connection and try again. |
| Error -201463 | The requested ports are not reciprocal. Make sure that the ports point at each other. |
| Error -201464 | A hardware fault has occurred. Please contact National Instruments technical support. To clear the fault, power cycle the device. |
| Error -201465 | Cannot perform auto-configure on offline devices. Please remove offline devices from the requested set. |
| Error -201466 | Cannot auto-configure connections between devices in different states (present, offline, and simulated). Please check requested set. |
| Error -201467 | Associated channels have conflicting properties. Make the conflicting property values consistent across channels to fix the error. |
| Error -201468 | The requested cDAQ Sync device cannot be configured because the master timebase is not present. Tasks containing cDAQ Sync devices that export or import a timebase must be committed in cascading order from the source to the destination. Use DAQmx Control Task to commit the master timebase source task prior to committing or starting a slave task. |
| Error -201469 | You selected a different digitizer and communicator for an SCXI module that is in multiplexed mode. Configure the SCXI module with the digitizer set to the same mode as the chassis communicator in MAX. |
| Error -201470 | Invalid calibration adjustment point(s) provided. Use DAQmx Get Calibration Adjustment Points to retrieve valid adjustment values. |
| Error -201471 | The physical channel string contains multiple devices. You can include multiple physical channels on a single device (for example, "Dev1/ao0:3") but not multiple physical channels on multiple devices (for example, "Dev1/ao0:3, Dev2/ao2"). |
| Error -201472 | You must specify exactly one timestamp channel for a Navigation With Timestamp read call. |
| Error -201474 | The device is not supported on the local system, is incompatible, or the installation is corrupt. Install and/or repair the appropriate driver. |
| Error -201475 | Auxiliary power not detected. Verify that the auxiliary power source is properly connected to the device and that the auxiliary input fuse has not blown. Refer to the NI-DCPower documentation for information about replacing the input fuse. |
| Error -201476 | Task reservation failed because a watchdog timer task is reserved. Unreserve or commit the watchdog timer task to reserve a new task. |
| Error -201477 | Reservation of watchdog timer task failed because another task is reserved or running. Stop and unreserve all other tasks before reserving a watchdog timer task. |
| Error -201478 | Watchdog timer task has expired. Reset the chassis to resume normal operation. |
| Error -201479 | The attribute/property ArmStart.Term cannot be queried when a software arm start trigger is configured because it cannot be exported to any terminal. Configure an external arm start trigger and query the desired attribute/property. |
| Error -201480 | There is already a session open to the device from another process, or a calibration session is open. You must close the open session, exit the application holding the device, or release the device in the Soft Front Panel. |
| Error -201481 | If you specify an expiration state for any line on an NI 9401 in the range of line 0:3 or line 4:7, you must specify an expiration state for every line in that range. |
| Error -201482 | The current number of channels chosen for calibration is incorrect. You must specify all channels for calibration. |
| Error -201483 | The selected master for the configured multi-device task is not able to export signals. Make sure that the first channel in the task is from a device on a chassis that has an NI 9469 capable of exporting signals to the slave devices. If you have any delta-sigma modules in your task, at least one must be in the master chassis. For time-based synchronization, ensure all the chassis in the task are in the same synchronization network. |
| Error -201484 | The current task contains channels from both delta-sigma and non delta-sigma devices. Make sure the first channel in the task is from a delta-sigma device and that it is located in a chassis that is able to share signals with its slave chassis through an NI 9469, or the task is running on devices that support time-based network synchronization. |
| Error -201485 | Measured data size does not match reference data size. The module acquires data and receives reference data in different functions. Please make sure these calibration functions are executed the same number of times during calibration. |
| Error -201486 | You must call DAQmx Setup Calibration first in order to calibrate this module. |
| Error -201487 | You must disable automatic firmware updates before attempting to manually update the firmware of your device. |
| Error -201488 | Firmware update failed. System attempted to update a different device than what you specified. Try updating again. |
| Error -201489 | Invalid state for firmware update. You must call the firmware update action after calling beginFirmwareAction and before calling disposeFirmwareAction. |
| Error -201490 | Firmware version being installed is older than the currently installed firmware. |
| Error -201491 | Firmware version being installed matches the currently installed version. |
| Error -201492 | Attempted operation is not supported on simulated devices. |
| Error -201493 | Shunt calibration failed. The calculated gain adjust is out of range. Ensure that the shunt calibration terminals are connected properly and that the shunt resistance and shunt element location settings match how the hardware is wired. |
| Error -201494 | Device does not support simultaneous calibration of multiple channels. Calibrate channels one channel at a time passing individual channels to different invocations of DAQmx Adjust Calibration. |
| Error -201495 | Device calibration requires all ranges to be calibrated for a single channel. Calibrate the ranges specified in the procedure. |
| Error -201496 | Voltage settings not calibrated. Ensure all voltage settings are calibrated before trying to calibrate bridge settings. |
| Error -201497 | You must run setupCalibration before running getCalDataPoints. |
| Error -201498 | AI channels on this device do not support using AC coupling while not using IEPE excitation. Enable IEPE excitation or set the coupling mode to DC. |
| Error -201499 | The selected calibration mode cannot query calibration data points. Make sure you follow the calibration procedure. |
| Error -201500 | The channel in calibration adjustment did not call calibration setup. Make sure you call calibration setup before calibration adjustment for this channel. |
| Error -201501 | The reference value input of calibration adjustment is out of range. |
| Error -201502 | DAC Offset Voltage Value is not set. When the DAC Offset Voltage Source property for a channel is set to External, the DAC Offset Voltage Value property must be set. Set the DAC Offset Voltage Value property so the value matches the offset voltage source connected to your device. Alternatively, use the internal DAC offset voltage source available on the device. |
| Error -209800 | DAQmx Read did not complete before the arrival of the next sample clock or change detection event which indicates that your program is not keeping up with the hardware clock or the external change event. For tasks using sample clock timing, slow down the hardware clock or else change your application so that it can keep up with the hardware clock. For tasks using change detection timing, decrease the frequency of your event or else change your application so that it can keep up with the change event. |
| Error 200079 | When specifying "No Change" as a watchdog state on a DSA channel, the actual behavior is determined by the idle output behavior configured by the last task run on the module. |
| Error -209801 | DAQmx Write did not complete before the arrival of the next sample clock which indicates that your program is not keeping up with the hardware clock. Slow down the hardware clock or else change your application so that it can keep up with the hardware clock. |
| Error -209802 | DAQmx Wait for Next Sample Clock detected one or more missed sample clocks since the last call to Wait for Next Sample Clock which indicates that your program is not keeping up with the sample clock. To remove this error, slow down the sample clock, or else change your application so that it can keep up with the sample clock. Alternatively, consider setting the Convert Errors to Warnings property to true and then handling the warning case appropriately. |
| Error -209803 | DAQmx Wait for Next Sample Clock detected 3 or more missed sample clocks since the last call to Wait for Next Sample Clock which indicates your program is not keeping up with the sample clock, and data was subsequently lost before it could be read by the application. To remove this error, slow down the sample clock. Consider restructuring the application so you can call DAQmx Read more often. Setting the Convert Error to Warning property to True will not eliminate the error because the data is lost. |
| Error -209805 | Task with counter output detected a sample clock before the corresponding DAQmx Write was completed. This may have occurred because the frequency of the counter output is too low for the given sample clock rate. A full output period must complete before new data can be written. To avoid this problem make sure that the counter output frequency is significantly higher than the sample clock rate. |
| Error -200831 | On Demand Simultaneous Analog Output Enable cannot be set to true unless Sample Timing Type is On Demand. |
| Error -201045 | Device connector number specified is invalid. Enter a valid connector number. |
| Error -201116 | Hardware timed non-buffered analog output is not supported on this device. |

Parent topic:

NI-DAQmx .NET Class Library Help

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxevents.html language=enus -->
## TOPIC 00018: Events

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxevents.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxevents.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-DAQmx .NET library supports asynchronous notification of various occurrences using .NET events. Events in the NI-DAQmx .NET library are located on the Task class. The following events are supported: CounterOutput—Occurs when any of the counters used in the task reaches its terminal count. Dig

Events

The NI-DAQmx .NET library supports asynchronous notification of various occurrences using .NET events.

Events in the NI-DAQmx .NET library are located on the Task class. The following events are supported:

- CounterOutput —Occurs when any of the counters used in the task reaches its terminal count.
- DigitalChangeDetection —Occurs when a digital change is detected on any of the digital lines used in the task.
- Done —Occurs when the task finishes, either successfully or due to an error.
- EveryNSampleRead —Occurs when the EveryNSampleReadEventInterval user-defined number of samples is written from the device to the PC buffer. This event works only with devices that support buffered tasks.
- EveryNSampleWritten —Occurs when the EveryNSamplesWrittenEventInterval user-defined number of samples is written from the PC buffer to the device. This event works only with devices that support buffered tasks.
- SampleClock —Occurs on each pulse of the task's sample clock.
- SampleComplete —Occurs when each sample is acquired into the NI-DAQmx driver buffer and is ready for reading.

Asynchronous I/O vs. Events

The NI-DAQmx .NET library also supports asynchronous I/O, which is similar to events. With asynchronous I/O, you create callbacks to be executed when a read or write operation completes. The NI-DAQmx .NET library also supports the EveryNSamples event. With this event, you create callbacks to be executed after a certain number of samples has been processed. You can also use EveryNSamples to call into certain methods of the task and access properties of the task while the task is still running. For more information, refer to 
 *Asynchronous Reads and Writes*.

Event Handler Considerations

Some events might occur frequently depending on your task configuration. For example, SampleComplete occurs frequently for input tasks with high sampling rates. Your event handler must execute quickly enough to respond to every NI-DAQmx event, as each one occurs. If your event handler cannot keep up with NI-DAQmx, your NI-DAQmx operation might fail or your program might become unresponsive. If you experience these problems, you should shorten your event handler or reconfigure your task so that events occur less often. For example, if your application cannot keep up with the SampleComplete event, you can use asynchronous I/O to execute callbacks after a larger number of samples have been acquired or generated.

Events are registered at the driver level, and as a result, when working with UI, you have to keep in mind that, if the application closes without the task being stopped, events might still occur while the application attempts to close. In such scenarios, the event will try to be executed on a thread that might have ended already. This will yield an error. To avoid this, remember to stop the task before exiting the application.

Event handlers, in some cases, are executed using the 
 SynchronizationContext of the thread you use to execute the handler.

Parent topic:

NI-DAQmx .NET Class Library Help

Related concepts:

- Asynchronous Reads and Writes

Related information:

- Task Class
- EveryNSamplesReadEventInterval Property
- EveryNSamplesWrittenEventInterval Property

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxexamples.html language=enus -->
## TOPIC 00019: NI-DAQmx .NET Examples

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxexamples.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxexamples.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: When you install the Measurement Studio NI-DAQmx .NET class library, example programs are installed by default. The location of the Microsoft Visual Basic .NET and Visual C# examples are relative to the default installation directory. Name and Description Default Install Location AcqMultVoltageSampl

NI-DAQmx .NET Examples

When you install the Measurement Studio NI-DAQmx .NET class library, example programs are installed by default. The location of the Microsoft Visual Basic .NET and Visual C# examples are relative to the default installation directory.

| Name and Description | Default Install Location |
| --- | --- |
| AcqMultVoltageSamples_SWTimed This example demonstrates how to acquire a finite amount of data using a software timer. | Visual C#: Analog In\\Measure Voltage\\AcqMultVoltageSamples_SWTimed\\CS Visual Basic .NET: Analog In\\Measure Voltage\\AcqMultVoltageSamples_SWTimed\\VB |
| AcqOneVoltageSample This example demonstrates how to acquire a single reading from a constant or slowly varying signal. | Visual C#: Analog In\\Measure Voltage\\AcqOneVoltageSample\\CS Visual Basic .NET: Analog In\\Measure Voltage\\AcqOneVoltageSample\\VB |
| AcqStrainSamples This example demonstrates how to perform a strain measurement. | Visual C#: Analog In\\Measure Strain\\AcqStrainSamples\\CS Visual Basic .NET: Analog In\\Measure Strain\\AcqStrainSamples\\VB |
| AcqVoltageSamples_ExtClk This example demonstrates how to acquire a finite amount of data using an external clock. | Visual C#: Analog In\\Measure Voltage\\AcqVoltageSamples_ExtClk\\CS Visual Basic .NET: Analog In\\Measure Voltage\\AcqVoltageSamples_ExtClk\\VB |
| AcqVoltageSamples_IntClk This example demonstrates how to acquire a finite amount of data using an internal clock. | Visual C#: Analog In\\Measure Voltage\\AcqVoltageSamples_IntClk\\CS Visual Basic .NET: Analog In\\Measure Voltage\\AcqVoltageSamples_IntClk\\VB |
| AcqVoltageSamples_IntClkAnalogStart This example demonstrates how to acquire a finite amount of data using the DAQ device's internal clock, started by an analog edge condition. | Visual C#: Analog In\\Measure Voltage\\AcqVoltageSamples_IntClkAnalogStart\\CSVisual Basic .NET: Analog In\\Measure Voltage\\AcqVoltageSamples_IntClkAnalogStart\\VB |
| AcqVoltageSamples_IntClkDigRef This example demonstrates how to acquire a finite amount of data using an internal clock and a digital reference trigger. | Visual C#: Analog In\\Measure Voltage\\AcqVoltageSamples_IntClkDigRef\\CSVisual Basic .NET: Analog In\\Measure Voltage\\AcqVoltageSamples_IntClkDigRef\\VB |
| AcqVoltageSamples_IntClkDigStartAndRef This example demonstrates how to acquire a finite amount of data using an internal clock and a digital start and reference trigger. | Visual C#: Analog In\\Measure Voltage\\AcqVoltageSamples_IntClkDigStartAndRef\\CS Visual Basic .NET: Analog In\\Measure Voltage\\AcqVoltageSamples_IntClkDigStartAndRef\\VB |
| AIAOShardTimebaseAndTrig_DSA This example synchronizes the clocks and trigger on two Dynamic Signal Acquistion (DSA) devices and performs continuous analog input and output. NOTE: This example is intended to show low level synchronization of various devices. DSA and S Series devices now support including channels from multiple devices in a single task. DAQmx automatically synchronizes the devices in such a task. See the DAQmx Help>>NI-DAQmx Device Considerations>>Multidevice Tasks section for further details.NOTE: If you are using PXI DSA devices along with sample clock timebase synchronization, the master device must reside in PXI slot 2.NOTE: This code will not run "as-is" on a multifunction (MIO) DAQ device. | Visual C#: Synchronization\\Multi-Device\\AIAOShardTimebaseAndTrig_DSA\\CSVisual Basic .NET: Synchronization\\Multi-Device\\AIAOShardTimebaseAndTrig_DSA\\VB |
| AIContAcquisition This example demonstrates how to acquire a continuous amount of data using the DAQ device's internal clock. It also shows how to synchronize two devices for different device families (E Series, M Series, and DSA), to simultaneously acquire the data.NOTE: This example is intended to show low level synchronization of various devices. DSA and S Series devices now support including channels from multiple devices in a single task. DAQmx automatically synchronizes the devices in such a task. See the DAQmx Help>>NI-DAQmx Device Considerations>>Multidevice Tasks section for further details.NOTE: PXI 6115 and 6120 (S Series) devices don't require sharing of master timebase, because they auto-lock to Clock 10. For those devices sharing a start trigger is adequate.NOTE: For the PCI-6154 S Series device use the M Series (PCI) synchronization type to synchronize using the reference clock. | Visual C#: Synchronization\\Multi-Device\\AIContAcquisition\\CSVisual Basic .NET: Synchronization\\Multi-Device\\AIContAcquisition\\VB |
| AIFiniteAcquisition This example demonstrates how to acquire a finite amount of analog input data using two DAQ devices' internal clocks. It also synchronizes these devices depending on the device family (E Series, M Series, or DSA) to simultaneously acquire the data.NOTE: This example is intended to show low level synchronization of various devices. DSA and S Series devices now support including channels from multiple devices in a single task. DAQmx automatically synchronizes the devices in such a task. See the DAQmx Help>>NI-DAQmx Device Considerations>>Multidevice Tasks section for further details.NOTE: PXI 6115 and 6120 (S Series) devices don't require sharing of master timebase, because they auto-lock to Clock 10. For those devices sharing a start trigger is adequate.NOTE: For the PCI-6154 S Series device use the M Series (PCI) synchronization type to synchronize using the reference clock. | Visual C#: Synchronization\\Multi-Device\\AIFiniteAcquisition\\CS Visual Basic .NET: Synchronization\\Multi-Device\\AIFiniteAcquisition\\VB |
| ConAcqRTDSmps_IntClk_SCXI1102And1581 This example demonstrates how to acquire temperature from an RTD using the internal clock of the DAQ device.This example uses the SCXI 1102 module in conjunction with the SCXI 1581 module. | Visual C#: Analog In\\Measure Temperature\\ConAcqRTDSmps_IntClk_SCXI1102And1581\\CS Visual Basic .NET: Analog In\\Measure Temperature\\ConAcqRTDSmps_IntClk_SCXI1102And1581\\VB |
| ConAcqThmSmps_IntClk_SCXI1102And1581 This example demonstrates how to acquire temperature data from a thermistor using the DAQ device's internal clock. This example uses the SCXI 1102 module in conjunction with the SCXI 1581 module. | Visual C#: Analog In\\Measure Temperature\\ConAcqThmSmps_IntClk_SCXI1102And1581\\CS Visual Basic .NET: Analog In\\Measure Temperature\\ConAcqThmSmps_IntClk_SCXI1102And1581\\VB |
| ConAcqVoltSmpls_ConfigFilter_SCXI114x This example demonstrates how to acquire and filter an analog signal using the SCXI-114x. | Visual C#: Analog In\\Measure Voltage\\ConAcqVoltSmpls_ConfigFilter_SCXI114x\\CSVisual Basic .NET: Analog In\\Measure Voltage\\ConAcqVoltSmpls_ConfigFilter_SCXI114x\\VB |
| ContAccelSamp_IntClk_AnlgStart This example demonstrates how to create an analog input acceleration task and perform a continuous acquisition using option IEPE excitation, analog triggering, and overload detection. | Visual C#: Analog In\\Measure Acceleration\\ContAccelSamp_IntClk_AnlgStart\\CS Visual Basic .NET: Analog In\\Measure Acceleration\\ContAccelSamp_IntClk_AnlgStart\\VB |
| ContAccelSamp_IntClk_AnlgStart_SCXI This example demonstrates how to make continuous, hardware-timed acceleration measurements using an SCXI-153x module. | Visual C#: Analog In\\Measure Acceleration\\ContAccelSamp_IntClk_AnlgStart_SCXI\\CSVisual Basic .NET: Analog In\\Measure Acceleration\\ContAccelSamp_IntClk_AnlgStart_SCXI\\VB |
| ContAcq0_20mACurrentSamples_IntClk This example demonstrates how to continuously measure current using an internal hardware clock for timing. | Visual C#: Analog In\\Measure Current\\ContAcq0_20mACurrentSamples_IntClk\\CSVisual Basic .NET: Analog In\\Measure Current\\ContAcq0_20mACurrentSamples_IntClk\\VB |
| ContAcqCustomVoltageSamples_9237 This example performs Wheatstone Bridge measurements with offset nulling if desired. | Visual C#: Analog In\\Measure Wheatstone Bridge\\ContAcqCustomVoltageSamples_9237\\CS Visual Basic .NET: Analog In\\Measure Wheatstone Bridge\\ContAcqCustomVoltageSamples_9237\\VB |
| ContAcqFreq_IntClk_SCXI1126 This example demonstrates how to acquire frequency data from an SCXI-1126 using the DAQ device's internal clock. | Visual C#: Analog In\\Measure Frequency\\ContAcqFreq_IntClk_SCXI1126\\CS Visual Basic .NET: Analog In\\Measure Frequency\\ContAcqFreq_IntClk_SCXI1126\\VB |
| ContAcqLVDTSamples_IntClk_SCXI1540 This example demonstrates how to make a continuous, hardware-timed acceleration measurement using an SCXI-1540 module. | Visual C#: Analog In\\Measure Linear Position\\ContAcqLVDTSamples_IntClk_SCXI1540\\CSVisual Basic .NET: Analog In\\Measure Linear Position\\ContAcqLVDTSamples_IntClk_SCXI1540\\VB |
| ContAcqRTDSamples_IntClk This example demonstrates how to acquire temperature from an RTD using the internal clock of the DAQ device. | Visual C#: Analog In\\Measure Temperature\\ContAcqRTDSamples_IntClk\\CS Visual Basic .NET: Analog In\\Measure Temperature\\ContAcqRTDSamples_IntClk\\VB |
| ContAcqRVDTSamples_IntClk_SCXI1540 This example demonstrates how to make a continuous, hardware-timed acceleration measurement using an SCXI-1540 module. | Visual C#: Analog In\\Measure Rotary Position\\ContAcqRVDTSamples_IntClk_SCXI1540\\CS Visual Basic .NET: Analog In\\Measure Rotary Position\\ContAcqRVDTSamples_IntClk_SCXI1540\\VB |
| ContAcqSndPressureSamples_IntClk This example demonstrates how to acquire a continuous set of sound pressure data using the DAQ device's internal clock. | Visual C#: Analog In\\Measure Sound Pressure\\ContAcqSndPressureSamples_IntClk\\CS Visual Basic .NET: Analog In\\Measure Sound Pressure\\ContAcqSndPressureSamples_IntClk\\VB |
| ContAcqThermocoupleSamples_IntClk This example demonstrates how to continuously acquire temperature readings from one or more thermocouples. | Visual C#: Analog In\\Measure Temperature\\ContAcqThermocoupleSamples_IntClk\\CSVisual Basic .NET: Analog In\\Measure Temperature\\ContAcqThermocoupleSamples_IntClk\\VB |
| ContAcqVoltageSamples_ExtClkDigStart This example demonstrates how to continuously acquire analog voltage data using an external clock, started by a digital trigger. | Visual C#: Analog In\\Measure Voltage\\ContAcqVoltageSamples_ExtClkDigStart\\CS Visual Basic .NET: Analog In\\Measure Voltage\\ContAcqVoltageSamples_ExtClkDigStart\\VB |
| ContAcqVoltageSamples_IntClk This example demonstrates how to acquire a continuous amount of data using the DAQ device's internal clock. | Visual C#: Analog In\\Measure Voltage\\ContAcqVoltageSamples_IntClk\\CS Visual Basic .NET: Analog In\\Measure Voltage\\ContAcqVoltageSamples_IntClk\\VB |
| ContAcqVoltageSamples_IntClk_SWTrigger This example demonstrates how to perform an analog software triggered acquisition. The example allows the user to specify the triggering condition and the number of pre-trigger samples to acquire. | Visual C#: Analog In\\Measure Voltage\\ContAcqVoltageSamples_IntClk_SWTrigger\\CS Visual Basic .NET: Analog In\\Measure Voltage\\ContAcqVoltageSamples_IntClk_SWTrigger\\VB |
| ContAcqVoltageSamples_IntClk_ToFile This example demonstrates how to acquire, write to file, and load from disk a continuous amount of analog input data using the DAQ device's internal clock. | Visual C#: Analog In\\Measure Voltage\\ContAcqVoltageSamples_IntClk_ToFile\\CS Visual Basic .NET: Analog In\\Measure Voltage\\ContAcqVoltageSamples_IntClk_ToFile\\VB |
| ContAcqVoltageSamples_SWTimed This example demonstrates how to acquire a continuous amount of data using a software timer. | Visual C#: Analog In\\Measure Voltage\\ContAcqVoltageSamples_SWTimed\\CS Visual Basic .NET: Analog In\\Measure Voltage\\ContAcqVoltageSamples_SWTimed\\VB |
| ContAcqVoltageSmpls_IntClkAnalogStart This example demonstrates how to continuously acquire data using the DAQ device's internal clock and an analog slope start trigger. | Visual C#: Analog In\\Measure Voltage\\ContAcqVoltageSmpls_IntClkAnalogStart\\CS Visual Basic .NET: Analog In\\Measure Voltage\\ContAcqVoltageSmpls_IntClkAnalogStart\\VB |
| ContAcqVoltageSmps_IntClk_PauseTrigger This example demonstrates how to continuously acquire data using DAQ device's internal clock and a digital pause trigger. | Visual C#: Analog In\\Measure Voltage\\ContAcqVoltageSmps_IntClk_PauseTrigger\\CS Visual Basic .NET: Analog In\\Measure Voltage\\ContAcqVoltageSmps_IntClk_PauseTrigger\\VB |
| ContAcqVoltSmpls_EveryNSamplesEvent This example demonstrates how to use Every N Samples events to acquire a continuous amount of data using the DAQ device's internal clock. The Every N Samples events indicate when data is available from DAQmx. | Visual C#: Analog In\\Measure Voltage\\ContAcqVoltSmpls_EveryNSamplesEvent\\CSVisual Basic .NET: Analog In\\Measure Voltage\\ContAcqVoltSmpls_EveryNSamplesEvent\\VB |
| ContForceBridgeSampleswCal This example performs Wheatstone Bridge measurements with offset nulling if desired. | Visual C#: Analog In\\Measure Force\\ContForceBridgeSampleswCal\\CS Visual Basic .NET: Analog In\\Measure Force\\ContForceBridgeSampleswCal\\VB |
| ContGenCurrentUpdatesWfm_IntClk This example demonstrates how to output a continuous number of current samples to an Analog Output Channel using an internal sample clock. | Visual C#: Analog Out\\Generate Current\\ContGenCurrentUpdatesWfm_IntClk\\CSVisual Basic .NET: Analog Out\\Generate Current\\ContGenCurrentUpdatesWfm_IntClk\\VB |
| ContGenVoltageWfm_ExtClk This example demonstrates how to continuously output a periodic waveform using an external clock. | Visual C#: Analog Out\\Generate Voltage\\ContGenVoltageWfm_ExtClk\\CS Visual Basic .NET: Analog Out\\Generate Voltage\\ContGenVoltageWfm_ExtClk\\VB |
| ContGenVoltageWfm_ExtClkDigStart This example demonstrates how to continuously output a waveform using an external sample clock and a digital start trigger. | Visual C#: Analog Out\\Generate Voltage\\ContGenVoltageWfm_ExtClkDigStart\\CSVisual Basic .NET: Analog Out\\Generate Voltage\\ContGenVoltageWfm_ExtClkDigStart\\VB |
| ContGenVoltageWfm_IntClk This example demonstrates how to continuously output a periodic waveform using an internal sample clock. | Visual C#: Analog Out\\Generate Voltage\\ContGenVoltageWfm_IntClk\\CS Visual Basic .NET: Analog Out\\Generate Voltage\\ContGenVoltageWfm_IntClk\\VB |
| ContGenVoltageWfmIntClk_AnalogStart This example demonstrates how to continuously output a periodic waveform using an internal clock and an analog trigger signal. | Visual C#: Analog Out\\Generate Voltage\\ContGenVoltageWfmIntClk_AnalogStart\\CS Visual Basic .NET: Analog Out\\Generate Voltage\\ContGenVoltageWfmIntClk_AnalogStart\\VB |
| ContReadDigChan_ExtClk This example demonstrates how to continuously read values from a digital input channel using an external sample clock. | Visual C#: Digital\\Read Values\\ContReadDigChan_ExtClk\\CS Visual Basic .NET: Digital\\Read Values\\ContReadDigChan_ExtClk\\VB |
| ContReadDigChan_PipeSampClkwHshk This examples demostrates how to interface the NI 6536/7 to a synchonous FIFO. | Visual C#: Digital\\Read Values\\ContReadDigChan_PipeSampClkwHshk\\CS Visual Basic .NET: Digital\\Read Values\\ContReadDigChan_PipeSampClkwHshk\\VB |
| ContWriteDigChan_Burst This example demonstrates how to output a continuous digital waveform using burst handshaking mode.Note: This example program exports the sample clock from the device. To import the sample clock, call theConfigureHandshakingBurstExportClock method instead. | Visual C#: Digital\\Generate Values\\ContWriteDigChan_Burst\\CS Visual Basic .NET: Digital\\Generate Values\\ContWriteDigChan_Burst\\VB |
| ContWriteDigChan_PipeSampClk This examples demostrates how to interface the NI 6536/7 to a synchronous DAC with an output enable signal. | Visual C#: Digital\\Generate Values\\ContWriteDigChan_PipeSampClk\\CSVisual Basic .NET: Digital\\Generate Values\\ContWriteDigChan_PipeSampClk\\VB |
| ContWriteDigChan_PipeSampClkwHshk This examples demostrates how to interface the NI 6536/7 to a synchonous FIFO. | Visual C#: Digital\\Generate Values\\ContWriteDigChan_PipeSampClkwHshk\\CS Visual Basic .NET: Digital\\Generate Values\\ContWriteDigChan_PipeSampClkwHshk\\VB |
| ContWriteDigPort_ExtClk This example demonstrates how to output a continuous digital pattern using an external clock. | Visual C#: Digital\\Generate Values\\ContWriteDigPort_ExtClk\\CSVisual Basic .NET: Digital\\Generate Values\\ContWriteDigPort_ExtClk\\VB |
| CountDigEvents This example demonstrates how to count digital events on a Counter Input Channel. The Initial Count, Count Direction, and Edge are all configurable.This example shows how to count edges on the counter's default source pin, but could easily be expanded to count edges on any PFI, RTSI, or internal signal. Non-buffered event counting can also use a digital pause trigger which could be added to this example by configuring the Trigger object for the Task. | Visual C#: Counter\\Count Digital Events\\CountDigEvents\\CSVisual Basic .NET: Counter\\Count Digital Events\\CountDigEvents\\VB |
| CountDigEventsBuffContinuous_ExtClk This example demonstrates how to count buffered digital events on a Counter Input channel. The initial count, count direction, edge, and sample clock source are all configurable. Edges are counted on the counter's default input terminal (see I/O Connections Overview below for more information), but could easily be modified to count edges on a PFI or RTSI line.Note: For buffered event counting, an external sample clock is necessary to signal when a sample should be inserted into the buffer. Specify the source terminal of the external clock in the clock source text box when you run the example. | Visual C#: Counter\\Count Digital Events\\CountDigEventsBuffContinuous_ExtClk\\CS Visual Basic .NET: Counter\\Count Digital Events\\CountDigEventsBuffContinuous_ExtClk\\VB |
| Gen0_20mACurrent This example demonstrates how to generate a single current value on a single current output channel of a SCXI-1124 module and NI-6238/6239 M-Series devices. | Visual C#: Analog Out\\Generate Current\\Gen0_20mACurrent\\CS Visual Basic .NET: Analog Out\\Generate Current\\Gen0_20mACurrent\\VB |
| GenDigPulse This example demonstrates how to generate a single digital pulse from a counter output channel. The initial delay, high time, low time, and idle state are all software configurable. This example shows how to configure the pulse in terms of time, but can easily be modified to generate a pulse in terms of frequency and duty cycle or ticks. | Visual C#: Counter\\Generate Pulse\\GenDigPulse\\CS Visual Basic .NET: Counter\\Generate Pulse\\GenDigPulse\\VB |
| GenDigPulseTrain_ContBuff_ExtClk This example demonstrates how to generate a continuous buffered sample clocked digital pulse train from a Counter Output Channel. The Frequency, Duty Cycle, and Idle State are all configurable. The default data generated is a pulse train with a fixed frequency but a duty cycle that varies based on the Duty Cycle Max/Min and the signal type. The duty cycle will update with each sample clock edge. | Visual C#: Counter\\Generate Pulse\\GenDigPulseTrain_ContBuff_ExtClk\\CSVisual Basic .NET: Counter\\Generate Pulse\\GenDigPulseTrain_ContBuff_ExtClk\\VB |
| GenDigPulseTrain_Continuous This example demonstrates how to generate a continuous digital pulse train from a counter output channel. The frequency, duty cycle, and idle state are all configurable.This example shows how to configure the pulse in terms of frequency and duty cycle, but it can easily be modified to generate a pulse in terms of time or ticks. | Visual C#: Counter\\Generate Pulse\\GenDigPulseTrain_Continuous\\CS Visual Basic .NET: Counter\\Generate Pulse\\GenDigPulseTrain_Continuous\\VB |
| GenDigPulseTrainContinuous_DigStart This example demonstrates how to generate a continuous digital pulse train from a counter output channel using a digital start trigger. The frequency, duty cycle, and idle state are all configurable.This example shows how to configure the pulse in terms of frequency and duty cycle, but it can easily be modified to generate a pulse in terms of time or ticks. | Visual C#: Counter\\Generate Pulse\\GenDigPulseTrainContinuous_DigStart\\CS Visual Basic .NET: Counter\\Generate Pulse\\GenDigPulseTrainContinuous_DigStart\\VB |
| GenDigPulseTrainContinuous_PauseTrigger This example demonstrates how to generate a continuous digital pulse train from a counter output channel and controlled by an external digital pause trigger. The frequency, duty cycle, and idle state are all configurable.This example shows how to configure the pulse in terms of frequency and duty cycle, but can easily be modified to generate a pulse in terms of time or ticks. | Visual C#: Counter\\Generate Pulse\\GenDigPulseTrainContinuous_PauseTrigger\\CS Visual Basic .NET: Counter\\Generate Pulse\\GenDigPulseTrainContinuous_PauseTrigger\\VB |
| GenMultCurrentUpdates_IntClk This example demonstrates how to output a finite number of current samples to an Analog Output Channel using an internal sample clock. | Visual C#: Analog Out\\Generate Current\\GenMultCurrentUpdates_IntClk\\CS Visual Basic .NET: Analog Out\\Generate Current\\GenMultCurrentUpdates_IntClk\\VB |
| GenMultVoltUpdates_IntClk This example demonstrates how to output multiple voltage updates (samples) to an analog output channel. | Visual C#: Analog Out\\Generate Voltage\\GenMultVoltUpdates_IntClk\\CS Visual Basic .NET: Analog Out\\Generate Voltage\\GenMultVoltUpdates_IntClk\\VB |
| GenMultVoltUpdates_SWTimed This example demonstrates how to output multiple voltage updates (samples) to an analog output channel in a software timed loop. | Visual C#: Analog Out\\Generate Voltage\\GenMultVoltUpdates_SWTimed\\CS Visual Basic .NET: Analog Out\\Generate Voltage\\GenMultVoltUpdates_SWTimed\\VB |
| GenMultVoltUpdatesIntClk_DigStart This example demonstrates how to output multiple voltage updates (samples) to an analog output channel. The generation starts when a digital trigger is received. | Visual C#: Analog Out\\Generate Voltage\\GenMultVoltUpdatesIntClk_DigStart\\CS Visual Basic .NET: Analog Out\\Generate Voltage\\GenMultVoltUpdatesIntClk_DigStart\\VB |
| GenVoltageUpdate This example demonstrates how to output a single voltage update (sample) to an analog output channel. | Visual C#: Analog Out\\Generate Voltage\\GenVoltageUpdate\\CSVisual Basic .NET: Analog Out\\Generate Voltage\\GenVoltageUpdate\\VB |
| Meas2EdgeSeparation This example demonstrates how to measure two edge separation on a counter input channel. The first edge, second edge, minimum value, and maximum value are all configurable. This example measures two edge separation on the counter's default input terminals (see I/O Connections Overview below for more information), but could easily be expanded to measure two edge separation on any PFI, RTSI, or internal signal. Refer to your device documentation to see if your device supports two edge separation measurements. | Visual C#: Counter\\Measure 2 Edge Separation\\Meas2EdgeSeparation\\CS Visual Basic .NET: Counter\\Measure 2 Edge Separation\\Meas2EdgeSeparation\\VB |
| Meas2EdgeSeparation_BufCont This example demonstrates how to perform a continuous number of two edge separation measurements on a counter input channel. The first edge, second edge, minimum value, maximum value, and samples to read are all configurable. This example shows how to perform a two edge separation measurement on the counter's default input terminals (refer to the I/O Connections Overview below for more information), but could easily be expanded to measure two edge separation on any PFI, RTSI, or internal signal.Refer to your device documentation to see if your device supports two edge separation measurements. | Visual C#: Counter\\Measure 2 Edge Separation\\Meas2EdgeSeparation_BufCont\\CSVisual Basic .NET: Counter\\Measure 2 Edge Separation\\Meas2EdgeSeparation_BufCont\\VB |
| MeasAngularPositionBufferedCont_ExtClk This example demonstrates how to measure angular position using a quadrature encoder on a counter input channel. The decoding type, pulses per revolution, z-index enable, z-index phase, z-index value, and sample clock source are all configurable. Position is measured on the counter's default A, B, and Z input terminals (see I/O Connections Overview below for more information).Note: For buffered position measurement, an external sample clock is necessary to signal when a sample should be inserted into the buffer. This is set by the sample clock source. | Visual C#: Counter\\Measure Position\\MeasAngularPositionBufferedCont_ExtClk\\CS Visual Basic .NET: Counter\\Measure Position\\MeasAngularPositionBufferedCont_ExtClk\\VB |
| MeasBuffered_SemiPeriodFinite This example demonstrates how to measure semi-periods on a counter input channel. The minimum value, maximum value, sample mode, and samples per channel are all configurable.This example shows how to measure semi-period on the counter's default input terminal (see I/O Conections Overview below for more information), but can easily be expanded to measure semi-period on any PFI, RTSI, or internal signal by setting the properties on the CIChannel object.Semi-period measurement differs from pulse width measurement in that it measures both the high and the low pulses of a given signal. So for every period, two data points will be returned. | Visual C#: Counter\\Measure Period Or Pulse Width\\MeasBuffered_SemiPeriodFinite\\CS Visual Basic .NET: Counter\\Measure Period Or Pulse Width\\MeasBuffered_SemiPeriodFinite\\VB |
| MeasDigFreqBuffCont_ExtClk_ArmStart This example demonstrates how to continually measure the frequency on a Counter Input Channel with a sample clock and arm start trigger. This example shows how to measure frequency with a counter on any PFI, RTSI, or internal signal. | Visual C#: Counter\\Measure Digital Frequency\\MeasDigFreqBuffCont_ExtClk_ArmStart\\CS Visual Basic .NET: Counter\\Measure Digital Frequency\\MeasDigFreqBuffCont_ExtClk_ArmStart\\VB |
| MeasDigFreqBuffCont_LargeRange2Ctr This example demonstrates how to measure buffered frequency using two counters on a counter input channel. The divisor, maximum and minimum frequency values, and the edge parameter are configurable.This example shows how to measure frequency on the counter's default input terminal (see I/O Connections Overview below for more information), but could easily be expanded to measure frequency on any PFI, RTSI, or internal signal. Additionally, this example could be extended to measure frequency with other measurement methods for different frequency and quantization error requirements. | Visual C#: Counter\\Measure Digital Frequency\\MeasDigFreqBuffCont_LargeRange2Ctr\\CSVisual Basic .NET: Counter\\Measure Digital Frequency\\MeasDigFreqBuffCont_LargeRange2Ctr\\VB |
| MeasDigFrequency_LowFreq1Ctr This example demonstrates how to measure a frequency using one counter on a counter input channel. The starting edge, minimum value and maximum value are all configurable. This example shows how to measure frequency on the counter's default input terminal (see I/O Connections Overview below for more information), but could easily be expanded to measure frequency on any PFI, RTSI, or internal signal. Additionally, this example could be extended to measure frequency with two counters for different frequency and quantization error requirements. | Visual C#: Counter\\Measure Digital Frequency\\MeasDigFrequency_LowFreq1Ctr\\CSVisual Basic .NET: Counter\\Measure Digital Frequency\\MeasDigFrequency_LowFreq1Ctr\\VB |
| MeasDigPeriodsBufCon_HighFrq2Ctr This example demonstrates how to measure periods using two counters on a counter input channel. The measurement time, sample mode, and samples per read are configurable.This example shows how to measure period on the counters default input terminal, (see I/O Connections Overview below for more information), , but could easily be expanded to measure periods on any PFI, RTSI, or internal signal. Additionally, this example could be extended to measure period with other measurement methods for different frequency and quantization error requirements. | Visual C#: Counter\\Measure Period or Pulse Width\\MeasDigPeriodsBufCon_HighFrq2Ctr\\CS Visual Basic .NET: Counter\\Measure Period or Pulse Width\\MeasDigPeriodsBufCon_HighFrq2Ctr\\VB |
| MeasGpsTimestamp_BuffFinite This example demonstrates how to use a finite buffereded task to measure time using a GPS Timestamp Channel. The Synchronization Method, Synchronization Source, Sample Clock Source, and Samples per Channel are all configurable. | Visual C#: Counter\\Measure GPS Timestamp\\MeasGpsTimestamp_BuffFinite\\CSVisual Basic .NET: Counter\\Measure GPS Timestamp\\MeasGpsTimestamp_BuffFinite\\VB |
| MeasPulseWidth This example demonstrates how to measure pulse width on a counter input channel. The edge, minimum value and maximum value are all configurable.This example shows how to measure pulse width on the counter's default input terminal (see I/O Connections Overview below for more information), but could easily be expanded to measure pulse width on any PFI, RTSI, or internal signal. | Visual C#: Counter\\Measure Period Or Pulse Width\\MeasPulseWidth\\CSVisual Basic .NET: Counter\\Measure Period Or Pulse Width\\MeasPulseWidth\\VB |
| MeasPulseWidthBuf_SmplClk_Cont This example demonstrates how to continually measure pulsewidths on a Counter Input Channel using an external sampleclock. The Maximum and Minimum Values, Sample Clock Source, andSamples per Channel are all configurable.This example shows how to measure pulse width on the counter'sdefault input terminal (refer to section IV, I/O ConnectionsOverview, below for more information), but could easily beexpanded to measure pulse width on any PFI, RTSI, or internalsignal.Note: For sample clock measurements, an external sample clock isnecessary to signal when the counter should measure asample. This is set by the Sample Clock Source control. | Visual C#: Counter\\Measure Period or Pulse Width\\MeasPulseWidthBuf_SmplClk_Cont\\CS Visual Basic .NET: Counter\\Measure Period or Pulse Width\\MeasPulseWidthBuf_SmplClk_Cont\\VB |
| MeasureGpsTimestamp This example demonstrates how to use a GPS counter to update the current time. | Visual C#: Counter\\Measure GPS Timestamp\\MeasureGpsTimestamp\\CSVisual Basic .NET: Counter\\Measure GPS Timestamp\\MeasureGpsTimestamp\\VB |
| MultiFunctionSyncAI_ReadDigChan This example demonstrates how to continuously acquire analog and digital data at the same time, synchronized with one another on the same device. | Visual C#: Synchronization\\Multi-Function\\SyncAI_ReadDigChan\\CSVisual Basic .NET: Synchronization\\Multi-Function\\SyncAI_ReadDigChan\\VB |
| MultiFunctionSyncAIAO This example demonstrates how to continuously acquire and generate synchronized analog input and output, started by an external digital start trigger. | Visual C#: Synchronization\\Multi-Function\\SyncAIAO\\CS Visual Basic .NET: Synchronization\\Multi-Function\\SyncAIAO\\VB |
| PWMCounterOutput This example demonstrates how to do Pulse Width Modulation using Analog Input and Counter Output. | Visual C#: Control\\General\\PWMCounterOutput\\CS Visual Basic .NET: Control\\General\\PWMCounterOutput\\VB |
| ReadDigChan This example demonstrates how to read values from one or more digital input channels. | Visual C#: Digital\\Read Values\\ReadDigChan\\CS Visual Basic .NET: Digital\\Read Values\\ReadDigChan\\VB |
| ReadDigChan_ChangeDetection This example demonstrates how to read values from one or more digital input channels, using change detection timing. | Visual C#: Digital\\Read Values\\ReadDigChan_ChangeDetection\\CS Visual Basic .NET: Digital\\Read Values\\ReadDigChan_ChangeDetection\\VB |
| ReadDigChan_ChangeDetection_DigFilter This example demonstrates how to acquire filtered digital input via change detection and digital filtering. | Visual C#: Digital\\Read Values\\ReadDigChan_ChangeDetection_DigFilter\\CS Visual Basic .NET: Digital\\Read Values\\ReadDigChan_ChangeDetection_DigFilter\\VB |
| ReadDigChan_ChangeDetection_Events This example demonstrates how to read values from one or more digital input channels using the digital change detection event. | Visual C#: Digital\\Read Values\\ReadDigChan_ChangeDetection_Events\\CS Visual Basic .NET: Digital\\Read Values\\ReadDigChan_ChangeDetection_Events\\VB |
| ReadDigChan_IntClk_DigRef This example demonstrates how to acquire a finite amount of data (Waveform) using a digital reference trigger. | Visual C#: Digital\\Read Values\\ReadDigChan_IntClk_DigRef\\CS Visual Basic .NET: Digital\\Read Values\\ReadDigChan_IntClk_DigRef\\VB |
| ReadDigChan_IntClk_PatternMatchStart This example demonstrates how to acquire a finite amount of digital data (Waveform) using a pattern match start trigger (i.e. the acquisition begins when a specified pattern has been matched). | Visual C#: Digital\\Read Values\\ReadDigChan_IntClk_PatternMatchStart\\CS Visual Basic .NET: Digital\\Read Values\\ReadDigChan_IntClk_PatternMatchStart\\VB |
| ReadDigPort This example demonstrates how to read a single value from a digital port. | Visual C#: Digital\\Read Values\\ReadDigPort\\CS Visual Basic .NET: Digital\\Read Values\\ReadDigPort\\VB |
| ReadDigPort_ExtClk This example demonstrates how to read values from a digital port using an external sample clock. | Visual C#: Digital\\Read Values\\ReadDigPort_ExtClk\\CS Visual Basic .NET: Digital\\Read Values\\ReadDigPort_ExtClk\\VB |
| TdmsAcqVoltageSamples_IntClk This example demonstrates how to acquire a finite amount while simultaneously streaming that data to a binary file. | Visual C#: Analog In\\Measure Voltage\\TdmsAcqVoltageSamples_IntClk\\CS Visual Basic .NET: Analog In\\Measure Voltage\\TdmsAcqVoltageSamples_IntClk\\VB |
| TdmsAcqVoltageSamples_IntClk_LogOnly This example demonstrates how to acquire and stream data to a binary file. | Visual C#: Analog In\\Measure Voltage\\TdmsAcqVoltageSamples_IntClk_LogOnly\\CS Visual Basic .NET: Analog In\\Measure Voltage\\TdmsAcqVoltageSamples_IntClk_LogOnly\\VB |
| TdmsContAcqVoltageSamples_IntClk This example demonstrates how to acquire a continuous amount while simultaneously streaming that data to a binary file. | Visual C#: Analog In\\Measure Voltage\\TdmsContAcqVoltageSamples_IntClk\\CS Visual Basic .NET: Analog In\\Measure Voltage\\TdmsContAcqVoltageSamples_IntClk\\VB |
| TdmsContAcqVoltageSamples_IntClk_LogOnly This example demonstrates how to acquire and stream data to a binary file in a continuous manner. | Visual C#: Analog In\\Measure Voltage\\TdmsContAcqVoltageSamples_IntClk_LogOnly\\CSVisual Basic .NET: Analog In\\Measure Voltage\\TdmsContAcqVoltageSamples_IntClk_LogOnly\\VB |
| WriteDigChan This example demonstrates how to write values to a digital output channel. | Visual C#: Digital\\Generate Values\\WriteDigChan\\CS Visual Basic .NET: Digital\\Generate Values\\WriteDigChan\\VB |
| WriteDigChan_ExtClk This example demonstrates how to write values to a digital output channel using an external sample clock. | Visual C#: Digital\\Generate Values\\WriteDigChan_ExtClk\\CS Visual Basic .NET: Digital\\Generate Values\\WriteDigChan_ExtClk\\VB |
| WriteDigChan_WatchdogTimer This example demonstrates how to write values to a digital output channel, using a watchdog timer. | Visual C#: Digital\\Generate Values\\WriteDigChan_WatchdogTimer\\CSVisual Basic .NET: Digital\\Generate Values\\WriteDigChan_WatchdogTimer\\VB |
| WriteDigPort This example demonstrates how to write values to a digital output port. | Visual C#: Digital\\Generate Values\\WriteDigPort\\CS Visual Basic .NET: Digital\\Generate Values\\WriteDigPort\\VB |

Parent topic:

NI-DAQmx .NET Class Library Help

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxmain.html language=enus -->
## TOPIC 00020: NI-DAQmx .NET Class Library Help

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxmain.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxmain.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use this class library to communicate with and control an NI data acquisition (DAQ) device. Some DAQ devices are not currently supported by the NI-DAQmx driver. Refer to the NI-DAQmx Readme for a complete listing of supported hardware. This help file links to the .NET Framework 4.0 documenta

NI-DAQmx .NET Class Library Help

You can use this class library to communicate with and control an NI data acquisition (DAQ) device. Some DAQ devices are not currently supported by the NI-DAQmx driver. Refer to the 
 *NI-DAQmx Readme* for a complete listing of supported hardware.

Note

API reference for .NET Framework 4.5 support

API reference for .NET Framework 4.5.1 support

For additional information on developing applications using NI drivers and the .NET Framework, refer to 
 ni.com/mstudio or visit 
 ni.com/info and enter the Info Code 
 NIdotNET.

You can find example applications by selecting 
 National Instruments»NI-DAQmx»NI-DAQmx Examples in the Start menu.

Note

Measurement Studio Installer Builder

setup projects

merge modules

Related information:

- DAQmx Namespace
- ni.com/mstudio
- ni.com/info

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxmemlimitsreads.html language=enus -->
## TOPIC 00021: Memory Limitations in NI-DAQmx Read Methods

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxmemlimitsreads.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxmemlimitsreads.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: If your application includes a read method that returns an array object with a memory size that is larger than the .NET Framework limitation of 2 GB, NI-DAQmx reads samples until the limitation is met. However, if your application exceeds the available physical memory of your system, you could see a

Memory Limitations in NI-DAQmx Read Methods

If your application includes a read method that returns an array object with a memory size that is larger than the .NET Framework limitation of 2 GB, NI-DAQmx reads samples until the limitation is met. However, if your application exceeds the available physical memory of your system, you could see a decrease in performance, or your system could be in an unstable state.

Parent topic:

Reading and Writing with NI-DAQmx Streams

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxmemoptanalogreads.html language=enus -->
## TOPIC 00022: Memory-Optimized Analog Reads

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxmemoptanalogreads.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxmemoptanalogreads.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: Memory-optimized analog waveform reads are a special case of analog waveform reads where the NI-DAQmx .NET library attempts to re-use the memory utilized by an initialized AnalogWaveform<TData> of type Double instead of allocating memory for a new data array on every invocation. Memory is reallocate

Memory-Optimized Analog Reads

Memory-optimized analog waveform reads are a special case of analog waveform reads where the NI-DAQmx .NET library attempts to re-use the memory utilized by an initialized AnalogWaveform<TData> of type Double instead of allocating memory for a new data array on every invocation.

Memory is reallocated if the number of samples requested is greater than the current size of the AnalogWaveform<TData> of type Double instead of allocating memory for a new data array on every invocation. Memory is reallocated if the number of samples requested is greater than the current size of the AnalogWaveform<TData> of type Double. This allows for much more efficient memory usage when performing multiple analog waveform reads.

The following example demonstrates how to perform a memory-optimized analog waveform read on a task with a single channel:

VB.NET

```text
' Given a Task instance "myTask", 
' Create the reader and attach it to the stream 
Dim reader As AnalogSingleChannelReader = New AnalogSingleChannelReader(myTask.Stream)
' Perform the read 
Dim data As AnalogWaveform(Of Double) = New AnalogWaveform(Of Double)(100)
reader.MemoryOptimizedReadWaveform(100, data)
```

C#

```text
// Given a Task instance "myTask", 
// Create the reader and attach it to the stream
AnalogSingleChannelReader reader = new AnalogSingleChannelReader(myTask.Stream);
// Perform the read
AnalogWaveform<double> data = new AnalogWaveform<double>(100);
reader.MemoryOptimizedReadWaveform(100, data);
```

The following example demonstrates how to perform a memory-optimized analog waveform read on a task with multiple channels:

VB.NET

```text
' Given a Task instance "myTask", 
' Create the reader and attach it to the stream 
Dim reader As AnalogMultiChannelReader = New AnalogMultiChannelReader(myTask.Stream)
' Perform the read 
Dim data(0) As AnalogWaveform(Of Double)
data(0) = New AnalogWaveform(Of Double)(100)
reader.MemoryOptimizedReadWaveform(100, data)
```

C#

```text
// Given a Task instance "myTask", 
// Create the reader and attach it to the stream
AnalogMultiChannelReader reader = new AnalogMultiChannelReader(myTask.Stream);
// Perform the read
AnalogWaveform<double>[] data = new AnalogWaveform<double>[1];
data[0] = new AnalogWaveform<double>(100);
reader.MemoryOptimizedReadWaveform(100, data);
```

Parent topic:

Analog Waveform Reads and Writes with the NI-DAQmx .NET Library

Related information:

- AnalogWaveform<TData> Class

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxracecond.html language=enus -->
## TOPIC 00023: Race Conditions

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxracecond.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxracecond.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: When performing asynchronous continuous output writes, a race condition can exist between the first asynchronous write and the start of the task. The following example assumes: you want to write asynchronously; instances of Task, AnalogSingleChannelWriter, and AsyncCallback are created; and StartWri

Race Conditions

When performing asynchronous continuous output writes, a race condition can exist between the first asynchronous write and the start of the task.

The following example assumes: you want to write asynchronously; instances of Task, AnalogSingleChannelWriter, and AsyncCallback are created; and StartWrite and WriteCallback methods are initialized correctly.

VB.NET

```text
Public Sub StartWrite()
    writer.BeginWriteWaveform(False, data, AddressOf WriteCallback, null)
    myTask.Start()
End Sub 

Public Sub WriteCallback(ByVal ar As IAsyncResult)
    writer.EndWrite()
    writer.BeginWriteWaveform(False, data, AddressOf WriteCallback, null)
End Sub
```

C#

```text
public void StartWrite()
{
    writer.BeginWriteWaveform(false, data, WriteCallback, null);
    myTask.Start();
}

public void WriteCallback(IAsyncResult ar)
{
    writer.EndWrite();
    writer.BeginWriteWaveform(false, data, WriteCallback, null);
}
```

Note

BeginWrite

BeginWrite

The race condition can occur because the code includes an asynchronous write and an explicit task start, but NI-DAQmx cannot guarantee that the task will start after the write, since the write is asynchronous.

Due to the race condition, for digital counter continuous output tasks, the previous code can return an exception. However, for an analog continuous output task, the task goes into timed unbuffered mode and, without a buffer, the sample clock does not gate the data. While this is not ideal behavior, this use case is supported by NI-DAQmx.

You can use either of the following options to work around this race condition:

- Set the autostart parameter to true in the StartWrite method: 
 writer.BeginWriteWaveform(true, data, callback, null); With this option, you do not need the 
 myTask.Start(); line of code in the previous example.
- Start the Task inside the callback. You must ensure that the task only starts if the task has not already started.

Parent topic:

Reading and Writing with NI-DAQmx Streams

Related information:

- Task Class
- AnalogSingleChannelReader Class
- AsyncCallback Delegate

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxrandwstreams.html language=enus -->
## TOPIC 00024: Reading and Writing with NI-DAQmx Streams

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxrandwstreams.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxrandwstreams.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: To read and write with the NI-DAQmx .NET library, use reader, writer, and stream objects. This programming pattern is similar to the pattern used throughout the .NET Framework for file and network I/O. To perform I/O in the NI-DAQmx library: (Optional) Create a task object. Create an instance of a r

Reading and Writing with NI-DAQmx Streams

To read and write with the NI-DAQmx .NET library, use reader, writer, and stream objects.

This programming pattern is similar to the pattern used throughout the .NET Framework for file and network I/O.

To perform I/O in the NI-DAQmx library:

1. (Optional) Create a task object.
2. Create an instance of a reader or writer, passing the task's DaqStream (Task.Stream) in the constructor.
3. Perform reads or writes.

VB.NET

```text
'Given a Task instance "myTask", 
'Create the reader and attach it to the stream 
Dim reader as AnalogSingleChannelReader
reader = New AnalogSingleChannelReader(myTask.Stream)
'Perform the read 
Dim data as Double()
data = reader.ReadMultiSample(100)
```

C#

```text
// Given a Task instance "myTask", 
// Create the reader and attach it to the stream
AnalogSingleChannelReader reader = new AnalogSingleChannelReader(myTask.Stream);
// Perform the read 
double[] data = reader.ReadMultiSample(100);
```

Parent topic:

NI-DAQmx .NET Class Library Help

Related information:

- DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxrsandws.html language=enus -->
## TOPIC 00025: NI-DAQmx Readers and Writers

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxrsandws.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxrsandws.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-DAQmx .NET library provides the following reader and writer objects: AnalogSingleChannelReader AnalogSingleChannelWriter AnalogMultiChannelReader AnalogMultiChannelWriter AnalogUnscaledReader AnalogUnscaledWriter CounterSingleChannelReader CounterSingleChannelWriter CounterMultiChannelReader

NI-DAQmx Readers and Writers

The NI-DAQmx .NET library provides the following reader and writer objects:

- AnalogSingleChannelReader
- AnalogSingleChannelWriter
- AnalogMultiChannelReader
- AnalogMultiChannelWriter
- AnalogUnscaledReader
- AnalogUnscaledWriter
- CounterSingleChannelReader
- CounterSingleChannelWriter
- CounterMultiChannelReader
- CounterMultiChannelWriter
- DigitalSingleChannelReader
- DigitalSingleChannelWriter
- DigitalMultiChannelReader
- DigitalMultiChannelWriter

Choose a reader or writer class based on the application that you are developing. For instance, if you want to perform a digital read and have multiple channels in a task, choose the DigitalMultiChannelReader class.

Properties related to I/O, such as the ChannelsToRead or AvailableSamplesPerChannel are located on the DaqStream class, not any of the reader or writer classes.

Note

DaqSteam

Parent topic:

Reading and Writing with NI-DAQmx Streams

Related information:

- AnalogSingleChannelReader Class
- AnalogSingleChannelWriter Class
- AnalogMultiChannelReader Class
- AnalogMultiChannelWriter Class
- AnalogUnscaledReader Class
- AnalogUnscaledWriter Class
- CounterSingleChannelReader Class
- CounterSingleChannelWriter Class
- CounterMultiChannelReader Class
- CounterMultiChannelWriter Class
- DigitalSingleChannelReader Class
- DigitalSingleChannelWriter Class
- DigitalMultiChannelReader Class
- DigitalMultiChannelWriter Class
- DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxtaskbasedrouting.html language=enus -->
## TOPIC 00026: Immediate and Task-Based Routing

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxtaskbasedrouting.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxtaskbasedrouting.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-DAQmx .NET library supports both immediate and task-based routing functionality. Methods and properties related to immediate routing are located on the DaqSystem class. This class cannot be instantiated directly. Retrieve an instance of the DaqSystem class by querying the static Local propert

Immediate and Task-Based Routing

The NI-DAQmx .NET library supports both immediate and task-based routing functionality.

Methods and properties related to immediate routing are located on the DaqSystem class. This class cannot be instantiated directly. Retrieve an instance of the DaqSystem class by querying the static Local property, as shown in the following example:

VB.NET

```text
DaqSystem.Local.ConnectTerminals("dev1/RTSI2","dev2/RTSI3")
```

C#

```text
DaqSystem.Local.ConnectTerminals("dev1/RTSI2","dev2/RTSI3");
```

Task-based routing is performed by using sub-objects of an instance of the Task class. When you create a hardware trigger or export a hardware signal, you create a task-based route.

Parent topic:

Tasks

Related information:

- DaqSystem Class
- Immediate Routing
- Task-Based Routing

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxtaskcreation.html language=enus -->
## TOPIC 00027: Task Creation

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxtaskcreation.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxtaskcreation.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create a new NI-DAQmx task, create a new instance of the Task and optionally provide a name to associate with the task, as shown in the following example: VB.NET Dim myTask as New Task("MyAnalogInputTask") C# Task myTask = new Task("MyAnalogInputTask"); If you provide an empty string or a null re

Task Creation

To create a new NI-DAQmx task, create a new instance of the Task and optionally provide a name to associate with the task, as shown in the following example:

VB.NET

```text
Dim myTask as New Task("MyAnalogInputTask")
```

C#

```text
Task myTask = new Task("MyAnalogInputTask");
```

Note

Nothing

Note

Task

Parent topic:

Tasks

Related information:

- Task Class

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxtaskobjects.html language=enus -->
## TOPIC 00028: Task Objects

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxtaskobjects.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxtaskobjects.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: Most of the classes in the NI-DAQmx .NET library cannot be instantiated directly. These classes are used as sub-objects of the Task class. For example, to modify the SamplesPerChannel property of the Timing class, use the Timing property of the Task class to get an instance of the Timing class that

Task Objects

Most of the classes in the NI-DAQmx .NET library cannot be instantiated directly. These classes are used as sub-objects of the Task class.

For example, to modify the SamplesPerChannel property of the Timing class, use the Timing property of the Task class to get an instance of the Timing class that corresponds to the task. The following code demonstrates how to access the Timing object.

VB.NET

```text
'Create a new NI-DAQmx Task 
Dim myTask as New Task("myTask")
'Access the subobjects of the Task class
myTask.Timing.SamplesPerChannel = 1000
```

C#

```text
//Create a new NI-DAQmx Task
Task myTask = new Task("myTask");
//Access the subobjects of the Task class
myTask.Timing.SamplesPerChannel = 1000;
```

Parent topic:

Tasks

Related information:

- Task Class
- Task.Timing Property
- Timing.SamplesPerChannel Property

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxtasks.html language=enus -->
## TOPIC 00029: Tasks

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxtasks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxtasks.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: Most of the operations that you can perform with the NI-DAQmx library, such as acquiring data or generating a signal, require that you first create an NI-DAQmx task. In the NI-DAQmx .NET library, NI-DAQmx tasks are represented by instances of the Task class. In a program, you can create new NI-DAQmx

Tasks

Most of the operations that you can perform with the NI-DAQmx library, such as acquiring data or generating a signal, require that you first create an NI-DAQmx task.

In the NI-DAQmx .NET library, NI-DAQmx tasks are represented by instances of the Task class. In a program, you can create new NI-DAQmx tasks and dispose of them when the program ends. When a single task targets the same device and takes the same type of measurement, it must be disposed before it can be created and used again in the same application.

Parent topic:

NI-DAQmx .NET Class Library Help

Related information:

- Task Class

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=netdaqmxtaskstates.html language=enus -->
## TOPIC 00030: Task States

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `netdaqmxtaskstates.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/netdaqmxtaskstates.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: You do not need to explicitly change the state of a Task because NI-DAQmx tasks automatically transition from one state to another as necessary. However, you can explicitly modify the state of a Task. In some cases, explicitly managing when state transitions occur might result in improved performanc

Task States

You do not need to explicitly change the state of a Task because NI-DAQmx tasks automatically transition from one state to another as necessary. However, you can explicitly modify the state of a Task. In some cases, explicitly managing when state transitions occur might result in improved performance. In the NI-DAQmx .NET library, you can change the state of the task by calling the Control method with a value that indicates the new state, as shown in the following example:

VB.NET

```text
myTask.Control(TaskAction.Verify)
```

C#

```text
myTask.Control(TaskAction.Verify);
```

This example moves the task into the verified state. Refer to 
 *Explicit Versus Implicit State Transitions* for a description of when Task state transitions occur and when you might want to explicitly manage them, and refer to 
 *Task State Model* for the task state order and a description of each state.

Verified Tasks

In the NI-DAQmx library, you cannot query the value of most properties of a Task until that task is verified. If you attempt to query a property value before the task is verified, a 
 DaqException is thrown. The NI-DAQmx driver sets many properties to default values that are dynamically determined from the values of other properties. The driver cannot calculate these default values until it knows all the properties values for a specific Task. Verifying a task involves examining all of the properties that are associated with a Task and can be time-consuming.

Because the Task is not verified when properties are set, you might be able to set a property to an invalid value. However, an exception is not thrown until later in the program because some validity and consistency checks are performed on properties after the Task is verified. Use the Control method to verify the Task.

Parent topic:

Tasks

Related information:

- Task Class
- Task State Model
- Task.Control Property
- Explicit Versus Implicit State Transitions

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=patents.html language=enus -->
## TOPIC 00031: Patents

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `patents.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/patents.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: For patents covering the NI products/technology, refer to the appropriate location: Help»Patents in your software, the patents.txt file on your media, or the National Instruments Patent Notice at ni.com/patents.

Patents

Help»Patents

patents.txt

National Instruments Patent Notice

ni.com/patents

Parent topic:

Legal Information

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=trademarks.html language=enus -->
## TOPIC 00032: Trademarks

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `trademarks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/trademarks.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the NI Trademarks and Logo Guidelines at ni.com/trademarks for more information on NI trademarks. ARM, Keil, and µVision are trademarks or registered of ARM Ltd or its subsidiaries. LEGO, the LEGO logo, WEDO, and MINDSTORMS are trademarks of the LEGO Group. TETRIX by Pitsco is a trademark o

Trademarks

Refer to the 
 *NI Trademarks and Logo Guidelines* at 
 [ni.com/trademarks](http://www.ni.com/trademarks) for more information on NI trademarks.

ARM, Keil, and µVision are trademarks or registered of ARM Ltd or its subsidiaries.

LEGO, the LEGO logo, WEDO, and MINDSTORMS are trademarks of the LEGO Group.

TETRIX by Pitsco is a trademark of Pitsco, Inc.

FIELDBUS FOUNDATION™ and FOUNDATION™ are trademarks of the Fieldbus Foundation.

EtherCAT® is a registered trademark of and licensed by Beckhoff Automation GmbH.

CANopen® is a registered Community Trademark of CAN in Automation e.V.

DeviceNet™ and EtherNet/IP™ are trademarks of ODVA.

Go!, SensorDAQ, and Vernier are registered trademarks of Vernier Software & Technology. Vernier Software & Technology and vernier.com are trademarks or trade dress.

Xilinx is the registered trademark of Xilinx, Inc.

Taptite and Trilobular are registered trademarks of Research Engineering & Manufacturing Inc.

FireWire® is the registered trademark of Apple Inc.

Linux® is the registered trademark of Linus Torvalds in the U.S. and other countries.

Handle Graphics®, MATLAB®, Simulink®, Stateflow®, and xPC TargetBox® are registered trademarks, and Simulink Coder™, TargetBox™, and Target Language Compiler™ are trademarks of The MathWorks, Inc.

Tektronix®, Tek, and Tektronix, Enabling Technology are registered trademarks of Tektronix, Inc.

The Bluetooth® word mark is a registered trademark owned by the Bluetooth SIG, Inc.

The ExpressCard™ word mark and logos are owned by PCMCIA and any use of such marks by National Instruments is under license.

The mark LabWindows is used under a license from Microsoft Corporation. Windows is a registered trademark of Microsoft Corporation in the United States and other countries.

Other product and company names mentioned herein are trademarks or trade names of their respective companies.

Members of the National Instruments Alliance Partner Program are business entities independent from NI and have no agency, partnership, or joint-venture relationship with NI.

Parent topic:

Legal Information

<!--NI_TOPIC bundle=ni-daqmx-.net-framework-4.5.1-class-library-getting-started path=warning.html language=enus -->
## TOPIC 00033: WARNING REGARDING USE OF NATIONAL INSTRUMENTS PRODUCTS

- bundle_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- source_path: `warning.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/raw/resource/enus/warning.html
- document_id: `ni-daqmx-.net-framework-4.5.1-class-library-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: YOU ARE ULTIMATELY RESPONSIBLE FOR VERIFYING AND VALIDATING THE SUITABILITY AND RELIABILITY OF THE PRODUCTS WHENEVER THE PRODUCTS ARE INCORPORATED IN YOUR SYSTEM OR APPLICATION, INCLUDING THE APPROPRIATE DESIGN, PROCESS, AND SAFETY LEVEL OF SUCH SYSTEM OR APPLICATION. PRODUCTS ARE NOT DESIGNED, MANU

WARNING REGARDING USE OF NATIONAL INSTRUMENTS PRODUCTS

YOU ARE ULTIMATELY RESPONSIBLE FOR VERIFYING AND VALIDATING THE SUITABILITY AND RELIABILITY OF THE PRODUCTS WHENEVER THE PRODUCTS ARE INCORPORATED IN YOUR SYSTEM OR APPLICATION, INCLUDING THE APPROPRIATE DESIGN, PROCESS, AND SAFETY LEVEL OF SUCH SYSTEM OR APPLICATION.

PRODUCTS ARE NOT DESIGNED, MANUFACTURED, OR TESTED FOR USE IN LIFE OR SAFETY CRITICAL SYSTEMS, HAZARDOUS ENVIRONMENTS OR ANY OTHER ENVIRONMENTS REQUIRING FAIL-SAFE PERFORMANCE, INCLUDING IN THE OPERATION OF NUCLEAR FACILITIES; AIRCRAFT NAVIGATION; AIR TRAFFIC CONTROL SYSTEMS; LIFE SAVING OR LIFE SUSTAINING SYSTEMS OR SUCH OTHER MEDICAL DEVICES; OR ANY OTHER APPLICATION IN WHICH THE FAILURE OF THE PRODUCT OR SERVICE COULD LEAD TO DEATH, PERSONAL INJURY, SEVERE PROPERTY DAMAGE OR ENVIRONMENTAL HARM (COLLECTIVELY, "HIGH-RISK USES"). FURTHER, PRUDENT STEPS MUST BE TAKEN TO PROTECT AGAINST FAILURES, INCLUDING PROVIDING BACK-UP AND SHUT-DOWN MECHANISMS. NI EXPRESSLY DISCLAIMS ANY EXPRESS OR IMPLIED WARRANTY OF FITNESS OF THE PRODUCTS OR SERVICES FOR HIGH-RISK USES.

Parent topic:

Legal Information
