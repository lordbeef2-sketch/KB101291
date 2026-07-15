# NI DOCUMENT BUNDLE: ni-daqmx-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-c-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__additional__information.html language=enus -->
## TOPIC 00001: Additional Information

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__additional__information.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__additional__information.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNoneAttachmentsNameDescriptionNI-DAQmx ConceptsTroubleshooting

### Additional Information

#### Groups

None

#### Group members

None

#### Attachments

| Name | Description |
| --- | --- |
| NI-DAQmx Concepts |  |
| Troubleshooting |  |

Parent topic:

NIDAQmx.h

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__additional__information_concepts.html language=enus -->
## TOPIC 00002: NI-DAQmx Concepts

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__additional__information_concepts.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__additional__information_concepts.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For more information on important NI-DAQmx concepts, including measurement fundamentals and device considerations, refer to the NI-DAQmx Help.

### NI-DAQmx Concepts

For more information on important NI-DAQmx concepts, including measurement fundamentals and device considerations, refer to the [NI-DAQmx Help](/csh?context=nidaqmx_daqhelp_gettingstarteddaqmx).

Parent topic:

Additional Information

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration.html language=enus -->
## TOPIC 00003: Calibration

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsC Series CalibrationDSA CalibrationExternal CalibrationFieldDAQ CalibrationPXI-42xx CalibrationSC Express CalibrationSCXI CalibrationTestScale CalibrationTIO CalibrationGroup membersNameDescriptionDAQmxAOSeriesCalAdjustDAQmxAdjust64xxCalDAQmxESeriesCalAdjustDAQmxGetAIChanCalCalDateDAQmxGetAICh

### Calibration

#### Groups

- C Series Calibration
- DSA Calibration
- External Calibration
- FieldDAQ Calibration
- PXI-42xx Calibration
- SC Express Calibration
- SCXI Calibration
- TestScale Calibration
- TIO Calibration

#### Group members

| Name | Description |
| --- | --- |
| DAQmxAOSeriesCalAdjust |  |
| DAQmxAdjust64xxCal |  |
| DAQmxESeriesCalAdjust |  |
| DAQmxGetAIChanCalCalDate |  |
| DAQmxGetAIChanCalExpDate |  |
| DAQmxGetExtCalLastDateAndTime |  |
| DAQmxGetExtCalLastDateAndTimeEx |  |
| DAQmxGetSelfCalLastDateAndTime |  |
| DAQmxGetSelfCalLastDateAndTimeEx |  |
| DAQmxMSeriesCalAdjust |  |
| DAQmxPerformBridgeOffsetNullingCal |  |
| DAQmxPerformBridgeOffsetNullingCalEx |  |
| DAQmxPerformBridgeShuntCal |  |
| DAQmxPerformBridgeShuntCalEx |  |
| DAQmxPerformStrainShuntCal |  |
| DAQmxPerformStrainShuntCalEx |  |
| DAQmxPerformThrmcplLeadOffsetNullingCal |  |
| DAQmxRestoreLastExtCalConst |  |
| DAQmxSCBaseboardCalAdjust |  |
| DAQmxSSeriesCalAdjust |  |
| DAQmxSelfCal |  |
| DAQmxSetAIChanCalCalDate |  |
| DAQmxSetAIChanCalExpDate |  |
| DAQmxXSeriesCalAdjust |  |

#### Attachments

None

Parent topic:

Advanced Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration_1ga4155788ea5f7b0a0c454c3466e826ec1.html language=enus -->
## TOPIC 00004: DAQmxGetExtCalLastDateAndTimeEx

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration_1ga4155788ea5f7b0a0c454c3466e826ec1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration_1ga4155788ea5f7b0a0c454c3466e826ec1.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetExtCalLastDateAndTimeEx(const char deviceName[], CVIAbsoluteTime *timestamp)RemarksIndicates the last date and time that the device underwent an external calibration.ParametersNameDirectionTypeDescriptiondeviceName[in]const char[]Specifies the name to assign to the device

### DAQmxGetExtCalLastDateAndTimeEx

#### Syntax

int32 __CFUNC DAQmxGetExtCalLastDateAndTimeEx(const char deviceName[], CVIAbsoluteTime *timestamp)

#### Remarks

Indicates the last date and time that the device underwent an external calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| deviceName | [in] | const char[] | Specifies the name to assign to the device. If unspecified, NI-DAQmx chooses the device name. |
| timestamp | [out] | CVIAbsoluteTime * | A reference to the value of the timestamp. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration_1ga53e264ed22ae8efc4b7ca6c013ec1c4f.html language=enus -->
## TOPIC 00005: DAQmxMSeriesCalAdjust

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration_1ga53e264ed22ae8efc4b7ca6c013ec1c4f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration_1ga53e264ed22ae8efc4b7ca6c013ec1c4f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxMSeriesCalAdjust(CalHandle calHandle, float64 referenceVoltage)RemarksAdjusts the external calibration constants for an M Series device. You must connect a known voltage to the device and specify that voltage with referenceVoltage.ParametersNameDirectionTypeDescriptioncalHan

### DAQmxMSeriesCalAdjust

#### Syntax

int32 __CFUNC DAQmxMSeriesCalAdjust(CalHandle calHandle, float64 referenceVoltage)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an M Series device. You must connect a known voltage to the device and specify that voltage with referenceVoltage.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| referenceVoltage | [in] | float64 | The known voltage, in volts, to use as a reference for calibration. This voltage should be between +6.000 V and +9.999 V. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration_1ga7c9f15a1b22f65ef7137f5cf653ee557.html language=enus -->
## TOPIC 00006: DAQmxPerformBridgeOffsetNullingCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration_1ga7c9f15a1b22f65ef7137f5cf653ee557.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration_1ga7c9f15a1b22f65ef7137f5cf653ee557.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxPerformBridgeOffsetNullingCal(TaskHandle taskHandle, const char channel[])RemarksPerforms a bridge offset nulling calibration on the channels in the task. If the task measures both bridge-based sensors and non-bridge-based sensors, specify the names of the channels that meas

### DAQmxPerformBridgeOffsetNullingCal

#### Syntax

int32 __CFUNC DAQmxPerformBridgeOffsetNullingCal(TaskHandle taskHandle, const char channel[])

#### Remarks

Performs a bridge offset nulling calibration on the channels in the task. If the task measures both bridge-based sensors and non-bridge-based sensors, specify the names of the channels that measure bridge-based sensors in the channel parameter.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task used in this function. |
| channel | [in] | const char[] | A subset of virtual channels in the task that you want to calibrate. Use this parameter if you do not want to calibrate all the channels in the task or if some channels in the task measure non-bridge-based sensors. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration_1ga9bbbfc1857c6e187cebc644affc7efaf.html language=enus -->
## TOPIC 00007: DAQmxPerformStrainShuntCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration_1ga9bbbfc1857c6e187cebc644affc7efaf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration_1ga9bbbfc1857c6e187cebc644affc7efaf.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxPerformStrainShuntCal(TaskHandle taskHandle, const char channel[], float64 shuntResistorValue, int32 shuntResistorLocation, bool32 skipUnsupportedChannels)RemarksPerforms shunt calibration for the specified channels using a strain gage sensor.ParametersNameDirectionTypeDescr

### DAQmxPerformStrainShuntCal

#### Syntax

int32 __CFUNC DAQmxPerformStrainShuntCal(TaskHandle taskHandle, const char channel[], float64 shuntResistorValue, int32 shuntResistorLocation, bool32 skipUnsupportedChannels)

#### Remarks

Performs shunt calibration for the specified channels using a strain gage sensor.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task used in this function. |
| channel | [in] | const char[] | A subset of virtual channels in the task that you want to calibrate. Use this parameter if you do not want to calibrate all the channels in the task or if some channels in the task measure non-bridge-based sensors. If the input is empty, the function will attempt to perform shunt calibration on all the channels in the task. |
| shuntResistorValue | [in] | float64 | The resistance, in ohms, of the shunt resistor. |
| shuntResistorLocation | [in] | int32 | The location of the shunt resistor. Refer to the NI-DAQmx Help for more information on bridge configurations. ValueDescriptionDAQmx_Val_R1 (12465)R1DAQmx_Val_R2 (12466)R2DAQmx_Val_R3 (12467)R3DAQmx_Val_R4 (14813)R4 |
| Value | Description |  |  |
| DAQmx_Val_R1 (12465) | R1 |  |  |
| DAQmx_Val_R2 (12466) | R2 |  |  |
| DAQmx_Val_R3 (12467) | R3 |  |  |
| DAQmx_Val_R4 (14813) | R4 |  |  |
| skipUnsupportedChannels | [in] | bool32 | Specifies whether or not to skip channels that do not support shunt calibration. If skipUnsupportedChannels is TRUE, shunt calibration will be performed only on supported channels. If FALSE, shunt calibration will be performed on channels specified by channelNames. The default is FALSE. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration_1ga9f31a3bb7429289fb5a54cb297db0cca.html language=enus -->
## TOPIC 00008: DAQmxXSeriesCalAdjust

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration_1ga9f31a3bb7429289fb5a54cb297db0cca.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration_1ga9f31a3bb7429289fb5a54cb297db0cca.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxXSeriesCalAdjust(CalHandle calHandle, float64 referenceVoltage)RemarksAdjusts the external calibration constants for an X Series device. You must connect a known voltage to the device and specify that voltage with referenceVoltage.ParametersNameDirectionTypeDescriptioncalHan

### DAQmxXSeriesCalAdjust

#### Syntax

int32 __CFUNC DAQmxXSeriesCalAdjust(CalHandle calHandle, float64 referenceVoltage)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an X Series device. You must connect a known voltage to the device and specify that voltage with referenceVoltage.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| referenceVoltage | [in] | float64 | The known voltage, in volts, to use as a reference for calibration. This voltage should be between +6.000 V and +8.500 V. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration_1gaa0edb9d93eb30267f6a630c98efe9db2.html language=enus -->
## TOPIC 00009: DAQmxGetAIChanCalExpDate

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration_1gaa0edb9d93eb30267f6a630c98efe9db2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration_1gaa0edb9d93eb30267f6a630c98efe9db2.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetAIChanCalExpDate(TaskHandle taskHandle, const char channelName[], uInt32 *year, uInt32 *month, uInt32 *day, uInt32 *hour, uInt32 *minute)RemarksIndicates the last date and time that the channel underwent an external channel calibration.ParametersNameDirectionTypeDescripti

### DAQmxGetAIChanCalExpDate

#### Syntax

int32 __CFUNC DAQmxGetAIChanCalExpDate(TaskHandle taskHandle, const char channelName[], uInt32 *year, uInt32 *month, uInt32 *day, uInt32 *hour, uInt32 *minute)

#### Remarks

Indicates the last date and time that the channel underwent an external channel calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task used in this function. |
| channelName | [in] | const char[] | Name of the local or global channel to query calibration for. |
| year | [out] | uInt32 * | The last year that the channel underwent an external channel calibration. |
| month | [out] | uInt32 * | The last month that the channel underwent an external channel calibration. |
| day | [out] | uInt32 * | The last day that the channel underwent an external channel calibration. |
| hour | [out] | uInt32 * | The last hour, on a 24-hour clock, that the channel underwent an external channel calibration. |
| minute | [out] | uInt32 * | The last minute that the channel underwent an external channel calibration. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration_1gaa3d975b8533f51dda223453a47319a2f.html language=enus -->
## TOPIC 00010: DAQmxGetExtCalLastDateAndTime

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration_1gaa3d975b8533f51dda223453a47319a2f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration_1gaa3d975b8533f51dda223453a47319a2f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetExtCalLastDateAndTime(const char deviceName[], uInt32 *year, uInt32 *month, uInt32 *day, uInt32 *hour, uInt32 *minute)RemarksIndicates the last date and time that the device underwent an external calibration.ParametersNameDirectionTypeDescriptiondeviceName[in]const char[]

### DAQmxGetExtCalLastDateAndTime

#### Syntax

int32 __CFUNC DAQmxGetExtCalLastDateAndTime(const char deviceName[], uInt32 *year, uInt32 *month, uInt32 *day, uInt32 *hour, uInt32 *minute)

#### Remarks

Indicates the last date and time that the device underwent an external calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| deviceName | [in] | const char[] | Specifies the name to assign to the device. If unspecified, NI-DAQmx chooses the device name. |
| year | [out] | uInt32 * | The last year that the device underwent an external calibration. |
| month | [out] | uInt32 * | The last month that the device underwent an external calibration. |
| day | [out] | uInt32 * | The last day that the device underwent an external calibration. |
| hour | [out] | uInt32 * | The last hour, on a 24-hour clock, that the device underwent an external calibration. |
| minute | [out] | uInt32 * | The last minute that the device underwent an external calibration. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration_1gaad008c9b94acd3d5510d157590332984.html language=enus -->
## TOPIC 00011: DAQmxGetSelfCalLastDateAndTime

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration_1gaad008c9b94acd3d5510d157590332984.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration_1gaad008c9b94acd3d5510d157590332984.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetSelfCalLastDateAndTime(const char deviceName[], uInt32 *year, uInt32 *month, uInt32 *day, uInt32 *hour, uInt32 *minute)RemarksIndicates the last date and time that the device underwent a self-calibration.ParametersNameDirectionTypeDescriptiondeviceName[in]const char[]Spec

### DAQmxGetSelfCalLastDateAndTime

#### Syntax

int32 __CFUNC DAQmxGetSelfCalLastDateAndTime(const char deviceName[], uInt32 *year, uInt32 *month, uInt32 *day, uInt32 *hour, uInt32 *minute)

#### Remarks

Indicates the last date and time that the device underwent a self-calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| deviceName | [in] | const char[] | Specifies the name to assign to the device. If unspecified, NI-DAQmx chooses the device name. |
| year | [out] | uInt32 * | The last year that the device underwent a self-calibration. |
| month | [out] | uInt32 * | The last month that the device underwent a self-calibration. |
| day | [out] | uInt32 * | The last day that the device underwent a self-calibration. |
| hour | [out] | uInt32 * | The last hour, on a 24-hour clock, that the device underwent a self-calibration. |
| minute | [out] | uInt32 * | The last minute that the device underwent a self-calibration. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration_1gabb597c9e3daeadee65b4ca9a422f12f6.html language=enus -->
## TOPIC 00012: DAQmxRestoreLastExtCalConst

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration_1gabb597c9e3daeadee65b4ca9a422f12f6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration_1gabb597c9e3daeadee65b4ca9a422f12f6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxRestoreLastExtCalConst(const char deviceName[])RemarksSets the self-calibration constants of the device to the the current external calibration constants. National Instruments sets the external calibration constants at the factory, and those constants remain in effect until

### DAQmxRestoreLastExtCalConst

#### Syntax

int32 __CFUNC DAQmxRestoreLastExtCalConst(const char deviceName[])

#### Remarks

Sets the [self-calibration constants](/csh?context=nidaqmx_mxcncpts_calibration) of the device to the the current [external calibration constants](/csh?context=nidaqmx_mxcncpts_calibration). National Instruments sets the external calibration constants at the factory, and those constants remain in effect until you perform a new external calibration on the device. This function nullifies any self-calibration you perform on the device. If you have never performed a self-calibration on the device, this function has no effect.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| deviceName | [in] | const char[] | Specifies the name to assign to the device. If unspecified, NI-DAQmx chooses the device name. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration_1gac1d240c75cff515738f0dfbc657c1bb2.html language=enus -->
## TOPIC 00013: DAQmxPerformStrainShuntCalEx

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration_1gac1d240c75cff515738f0dfbc657c1bb2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration_1gac1d240c75cff515738f0dfbc657c1bb2.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxPerformStrainShuntCalEx(TaskHandle taskHandle, const char channel[], float64 shuntResistorValue, int32 shuntResistorLocation, int32 shuntResistorSelect, int32 shuntResistorSource, bool32 skipUnsupportedChannels)RemarksPerforms shunt calibration for the specified channels usi

### DAQmxPerformStrainShuntCalEx

#### Syntax

int32 __CFUNC DAQmxPerformStrainShuntCalEx(TaskHandle taskHandle, const char channel[], float64 shuntResistorValue, int32 shuntResistorLocation, int32 shuntResistorSelect, int32 shuntResistorSource, bool32 skipUnsupportedChannels)

#### Remarks

Performs shunt calibration for the specified channels using a strain gage sensor.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task used in this function. |
| channel | [in] | const char[] | A subset of virtual channels in the task that you want to calibrate. Use this parameter if you do not want to calibrate all the channels in the task or if some channels in the task measure non-bridge-based sensors. If the input is empty, the function will attempt to perform shunt calibration on all the channels in the task. |
| shuntResistorValue | [in] | float64 | The resistance, in ohms, of the shunt resistor. |
| shuntResistorLocation | [in] | int32 | The location of the shunt resistor. Refer to the NI-DAQmx Help for more information on bridge configurations. ValueDescriptionDAQmx_Val_R1 (12465)R1DAQmx_Val_R2 (12466)R2DAQmx_Val_R3 (12467)R3DAQmx_Val_R4 (14813)R4 |
| Value | Description |  |  |
| DAQmx_Val_R1 (12465) | R1 |  |  |
| DAQmx_Val_R2 (12466) | R2 |  |  |
| DAQmx_Val_R3 (12467) | R3 |  |  |
| DAQmx_Val_R4 (14813) | R4 |  |  |
| shuntResistorSelect | [in] | int32 | The shunt calibration switch to use. NameDescriptionDAQmx_Val_ASwitch A.DAQmx_Val_BSwitch B. |
| Name | Description |  |  |
| DAQmx_Val_A | Switch A. |  |  |
| DAQmx_Val_B | Switch B. |  |  |
| shuntResistorSource | [in] | int32 | The shunt resistor to use. NameDescriptionDAQmx_Val_InternalInternal shunt resistor.DAQmx_Val_ExternalExternal shunt resistor. |
| Name | Description |  |  |
| DAQmx_Val_Internal | Internal shunt resistor. |  |  |
| DAQmx_Val_External | External shunt resistor. |  |  |
| skipUnsupportedChannels | [in] | bool32 | Specifies whether or not to skip channels that do not support shunt calibration. If skipUnsupportedChannels is TRUE, shunt calibration will be performed only on supported channels. If FALSE, shunt calibration will be performed on channels specified by channelNames. The default is FALSE. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration_1gacb50de25351135e0b0c62cb4375faedc.html language=enus -->
## TOPIC 00014: DAQmxESeriesCalAdjust

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration_1gacb50de25351135e0b0c62cb4375faedc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration_1gacb50de25351135e0b0c62cb4375faedc.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxESeriesCalAdjust(CalHandle calHandle, float64 referenceVoltage)RemarksAdjusts the external calibration constants on an E-Series device. You must supply a known voltage to the device and specify that voltage with referenceVoltage.ParametersNameDirectionTypeDescriptioncalHandl

### DAQmxESeriesCalAdjust

#### Syntax

int32 __CFUNC DAQmxESeriesCalAdjust(CalHandle calHandle, float64 referenceVoltage)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants on an E-Series device. You must [supply a known voltage to the device](/csh?context=nidaqmx_mxdevconsid_calsigeseries) and specify that voltage with referenceVoltage.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| referenceVoltage | [in] | float64 | The known voltage, in volts, to use as a reference for calibration. This voltage should be between +6.000 V and +9.999 V. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration_1gad21ae6e7f30ae942f61a305c7d6efb26.html language=enus -->
## TOPIC 00015: DAQmxPerformBridgeShuntCalEx

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration_1gad21ae6e7f30ae942f61a305c7d6efb26.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration_1gad21ae6e7f30ae942f61a305c7d6efb26.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxPerformBridgeShuntCalEx(TaskHandle taskHandle, const char channel[], float64 shuntResistorValue, int32 shuntResistorLocation, int32 shuntResistorSelect, int32 shuntResistorSource, float64 bridgeResistance, bool32 skipUnsupportedChannels)RemarksPerforms shunt calibration for

### DAQmxPerformBridgeShuntCalEx

#### Syntax

int32 __CFUNC DAQmxPerformBridgeShuntCalEx(TaskHandle taskHandle, const char channel[], float64 shuntResistorValue, int32 shuntResistorLocation, int32 shuntResistorSelect, int32 shuntResistorSource, float64 bridgeResistance, bool32 skipUnsupportedChannels)

#### Remarks

Performs shunt calibration for the specified channels using a bridge sensor.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task used in this function. |
| channel | [in] | const char[] | A subset of virtual channels in the task that you want to calibrate. Use this parameter if you do not want to calibrate all the channels in the task or if some channels in the task measure non-bridge-based sensors. If the input is empty, the function will attempt to perform shunt calibration on all the channels in the task. |
| shuntResistorValue | [in] | float64 | The resistance, in ohms, of the shunt resistor. |
| shuntResistorLocation | [in] | int32 | The location of the shunt resistor. Refer to the NI-DAQmx Help for more information on bridge configurations. ValueDescriptionDAQmx_Val_R1 (12465)R1DAQmx_Val_R2 (12466)R2DAQmx_Val_R3 (12467)R3DAQmx_Val_R4 (14813)R4 |
| Value | Description |  |  |
| DAQmx_Val_R1 (12465) | R1 |  |  |
| DAQmx_Val_R2 (12466) | R2 |  |  |
| DAQmx_Val_R3 (12467) | R3 |  |  |
| DAQmx_Val_R4 (14813) | R4 |  |  |
| shuntResistorSelect | [in] | int32 | The shunt calibration switch to use. NameDescriptionDAQmx_Val_ASwitch A.DAQmx_Val_BSwitch B. |
| Name | Description |  |  |
| DAQmx_Val_A | Switch A. |  |  |
| DAQmx_Val_B | Switch B. |  |  |
| shuntResistorSource | [in] | int32 | The shunt resistor to use. NameDescriptionDAQmx_Val_InternalInternal shunt resistor.DAQmx_Val_ExternalExternal shunt resistor. |
| Name | Description |  |  |
| DAQmx_Val_Internal | Internal shunt resistor. |  |  |
| DAQmx_Val_External | External shunt resistor. |  |  |
| bridgeResistance | [in] | float64 | The resistance, in ohms, of the bridge sensor. |
| skipUnsupportedChannels | [in] | bool32 | Specifies whether or not to skip channels that do not support shunt calibration. If skipUnsupportedChannels is TRUE, shunt calibration will be performed only on supported channels. If FALSE, shunt calibration will be performed on channels specified by channelNames. The default is FALSE. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration_1gadfefec6b67e9948cc311a03c91443d57.html language=enus -->
## TOPIC 00016: DAQmxPerformThrmcplLeadOffsetNullingCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration_1gadfefec6b67e9948cc311a03c91443d57.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration_1gadfefec6b67e9948cc311a03c91443d57.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxPerformThrmcplLeadOffsetNullingCal(TaskHandle taskHandle, const char channel[], bool32 skipUnsupportedChannels)RemarksPerforms thermocouple lead offset nulling calibration on the channels in the task to compensate for offsets introduced by open thermocouple detection. Keep t

### DAQmxPerformThrmcplLeadOffsetNullingCal

#### Syntax

int32 __CFUNC DAQmxPerformThrmcplLeadOffsetNullingCal(TaskHandle taskHandle, const char channel[], bool32 skipUnsupportedChannels)

#### Remarks

Performs thermocouple lead offset nulling calibration on the channels in the task to compensate for offsets introduced by open thermocouple detection. Keep the measured temperature as constant as possible while performing this adjustment.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task used in this function. |
| channel | [in] | const char[] | A subset of virtual channels in the task that you want to calibrate. Use this parameter if you do not want to calibrate all the channels in the task or if some channels in the task have open thermocouple detection disabled. |
| skipUnsupportedChannels | [in] | bool32 | Specifies whether or not to skip channels that do not support calibration. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration_1gae646df2bda1c429677ccfa3acec2e5fd.html language=enus -->
## TOPIC 00017: DAQmxGetSelfCalLastDateAndTimeEx

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration_1gae646df2bda1c429677ccfa3acec2e5fd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration_1gae646df2bda1c429677ccfa3acec2e5fd.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetSelfCalLastDateAndTimeEx(const char deviceName[], CVIAbsoluteTime *timestamp)RemarksIndicates the last date and time that the device underwent a self-calibration.ParametersNameDirectionTypeDescriptiondeviceName[in]const char[]Specifies the name to assign to the device. If

### DAQmxGetSelfCalLastDateAndTimeEx

#### Syntax

int32 __CFUNC DAQmxGetSelfCalLastDateAndTimeEx(const char deviceName[], CVIAbsoluteTime *timestamp)

#### Remarks

Indicates the last date and time that the device underwent a self-calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| deviceName | [in] | const char[] | Specifies the name to assign to the device. If unspecified, NI-DAQmx chooses the device name. |
| timestamp | [out] | CVIAbsoluteTime * | A reference to the value of the timestamp. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration_1gae6afb0448c3674f6c64b741d06508dd7.html language=enus -->
## TOPIC 00018: DAQmxSetAIChanCalCalDate

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration_1gae6afb0448c3674f6c64b741d06508dd7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration_1gae6afb0448c3674f6c64b741d06508dd7.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetAIChanCalCalDate(TaskHandle taskHandle, const char channelName[], uInt32 year, uInt32 month, uInt32 day, uInt32 hour, uInt32 minute)RemarksSets the date and time that the channel underwent a channel calibration.ParametersNameDirectionTypeDescriptiontaskHandle[in]TaskHandl

### DAQmxSetAIChanCalCalDate

#### Syntax

int32 __CFUNC DAQmxSetAIChanCalCalDate(TaskHandle taskHandle, const char channelName[], uInt32 year, uInt32 month, uInt32 day, uInt32 hour, uInt32 minute)

#### Remarks

Sets the date and time that the channel underwent a channel calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task used in this function. |
| channelName | [in] | const char[] | Name of the local or global channel to calibrate. |
| year | [in] | uInt32 | The last year that the channel underwent a channel calibration. |
| month | [in] | uInt32 | The last month that the channel underwent a channel calibration. |
| day | [in] | uInt32 | The last day that the channel underwent a channel calibration. |
| hour | [in] | uInt32 | The last hour, on a 24-hour clock, that the channel underwent a channel calibration. |
| minute | [in] | uInt32 | The last minute that the channel underwent a channel calibration. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration_1gaec6de32102d0a3cfd685cb895e0d6fbd.html language=enus -->
## TOPIC 00019: DAQmxSCBaseboardCalAdjust

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration_1gaec6de32102d0a3cfd685cb895e0d6fbd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration_1gaec6de32102d0a3cfd685cb895e0d6fbd.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSCBaseboardCalAdjust(CalHandle calHandle, float64 referenceVoltage)RemarksAdjusts the external calibration constants on for the baseboard of an SC Series device. You must connect a known voltage to the device and specify that voltage with referenceVoltage.ParametersNameDirec

### DAQmxSCBaseboardCalAdjust

#### Syntax

int32 __CFUNC DAQmxSCBaseboardCalAdjust(CalHandle calHandle, float64 referenceVoltage)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants on for the baseboard of an SC Series device. You must connect a known voltage to the device and specify that voltage with referenceVoltage.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| referenceVoltage | [in] | float64 | The known voltage, in volts, to use as a reference for calibration. This voltage should be between +6.000 V and +9.999 V. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration_1ga57753960a184c6fe23fd9e4555c47195.html language=enus -->
## TOPIC 00020: DAQmxCSeriesSetCalTemp

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration_1ga57753960a184c6fe23fd9e4555c47195.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration_1ga57753960a184c6fe23fd9e4555c47195.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCSeriesSetCalTemp(CalHandle calHandle, float64 temperature)RemarksSpecifies the temperature of a C Series device for the current external calibration session.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created u

### DAQmxCSeriesSetCalTemp

#### Syntax

int32 __CFUNC DAQmxCSeriesSetCalTemp(CalHandle calHandle, float64 temperature)

#### Remarks

Specifies the temperature of a C Series device for the current external calibration session.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| temperature | [in] | float64 | The temperature of the device, in degrees Celsius. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration.html language=enus -->
## TOPIC 00021: Adjust C Series Calibration

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxAdjust9201CalDAQmxAdjust9202CalDAQmxAdjust9203GainCalDAQmxAdjust9203OffsetCalDAQmxAdjust9204CalDAQmxAdjust9205CalDAQmxAdjust9206CalDAQmxAdjust9207GainCalDAQmxAdjust9207OffsetCalDAQmxAdjust9208GainCalDAQmxAdjust9208OffsetCalDAQmxAdjust9209GainCalDAQmxAdjust9

### Adjust C Series Calibration

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxAdjust9201Cal |  |
| DAQmxAdjust9202Cal |  |
| DAQmxAdjust9203GainCal |  |
| DAQmxAdjust9203OffsetCal |  |
| DAQmxAdjust9204Cal |  |
| DAQmxAdjust9205Cal |  |
| DAQmxAdjust9206Cal |  |
| DAQmxAdjust9207GainCal |  |
| DAQmxAdjust9207OffsetCal |  |
| DAQmxAdjust9208GainCal |  |
| DAQmxAdjust9208OffsetCal |  |
| DAQmxAdjust9209GainCal |  |
| DAQmxAdjust9209OffsetCal |  |
| DAQmxAdjust9210Cal |  |
| DAQmxAdjust9211Cal |  |
| DAQmxAdjust9212Cal |  |
| DAQmxAdjust9213Cal |  |
| DAQmxAdjust9214Cal |  |
| DAQmxAdjust9215Cal |  |
| DAQmxAdjust9216Cal |  |
| DAQmxAdjust9217Cal |  |
| DAQmxAdjust9218Cal |  |
| DAQmxAdjust9219Cal |  |
| DAQmxAdjust9220Cal |  |
| DAQmxAdjust9221Cal |  |
| DAQmxAdjust9222Cal |  |
| DAQmxAdjust9223Cal |  |
| DAQmxAdjust9224Cal |  |
| DAQmxAdjust9225Cal |  |
| DAQmxAdjust9226Cal |  |
| DAQmxAdjust9227Cal |  |
| DAQmxAdjust9228Cal |  |
| DAQmxAdjust9230Cal |  |
| DAQmxAdjust9231Cal |  |
| DAQmxAdjust9232Cal |  |
| DAQmxAdjust9234GainCal |  |
| DAQmxAdjust9234OffsetCal |  |
| DAQmxAdjust9238Cal |  |
| DAQmxAdjust9242Cal |  |
| DAQmxAdjust9244Cal |  |
| DAQmxAdjust9246Cal |  |
| DAQmxAdjust9247Cal |  |
| DAQmxAdjust9250Cal |  |
| DAQmxAdjust9251Cal |  |
| DAQmxAdjust9252Cal |  |
| DAQmxAdjust9253Cal |  |
| DAQmxAdjust9260Cal |  |
| DAQmxAdjust9262Cal |  |
| DAQmxAdjust9263Cal |  |
| DAQmxAdjust9264Cal |  |
| DAQmxAdjust9265Cal |  |
| DAQmxAdjust9266Cal |  |
| DAQmxAdjust9269Cal |  |
| DAQmxAdjust9320Cal |  |
| DAQmxAdjust9628AICal |  |
| DAQmxAdjust9628AOCal |  |
| DAQmxAdjust9629AICal |  |
| DAQmxAdjust9629AOCal |  |
| DAQmxAdjust9638AICal |  |
| DAQmxAdjust9638AOCal |  |
| DAQmxAdjust9775Cal |  |

#### Attachments

None

Parent topic:

C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga039233afda6a639df5932ffc89435b76.html language=enus -->
## TOPIC 00022: DAQmxAdjust9203OffsetCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga039233afda6a639df5932ffc89435b76.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga039233afda6a639df5932ffc89435b76.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9203OffsetCal(CalHandle calHandle, const char channelNames[], float64 rangeMin, float64 rangeMax)RemarksAdjusts the external calibration offset constants for an NI 9203.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session t

### DAQmxAdjust9203OffsetCal

#### Syntax

int32 __CFUNC DAQmxAdjust9203OffsetCal(CalHandle calHandle, const char channelNames[], float64 rangeMin, float64 rangeMax)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) offset constants for an NI 9203.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| rangeMin | [in] | float64 | The minimum value in the range, in amps. |
| rangeMax | [in] | float64 | The maximum value in the range, in amps. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga1171ab8163ad975bd0cc12e390aa949a.html language=enus -->
## TOPIC 00023: DAQmxAdjust9262Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga1171ab8163ad975bd0cc12e390aa949a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga1171ab8163ad975bd0cc12e390aa949a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9262Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9262.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9262Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9262Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9262.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga17a613041bdbd5114b9999c272a87b9f.html language=enus -->
## TOPIC 00024: DAQmxAdjust9215Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga17a613041bdbd5114b9999c272a87b9f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga17a613041bdbd5114b9999c272a87b9f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9215Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9215.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9215Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9215Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9215.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga1a7da77c9455e15132fcabfacf9b1403.html language=enus -->
## TOPIC 00025: DAQmxAdjust9238Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga1a7da77c9455e15132fcabfacf9b1403.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga1a7da77c9455e15132fcabfacf9b1403.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9238Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9238.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9238Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9238Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9238.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga2943e25ced8bc4f4b613561b7dcb6af1.html language=enus -->
## TOPIC 00026: DAQmxAdjust9216Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga2943e25ced8bc4f4b613561b7dcb6af1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga2943e25ced8bc4f4b613561b7dcb6af1.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9216Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9216.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9216Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9216Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9216.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga297ad9d26f99f2e75883a50937f4fc72.html language=enus -->
## TOPIC 00027: DAQmxAdjust9266Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga297ad9d26f99f2e75883a50937f4fc72.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga297ad9d26f99f2e75883a50937f4fc72.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9266Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9266.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9266Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9266Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9266.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga2fdef0663434fcbaba997c9ac63b5952.html language=enus -->
## TOPIC 00028: DAQmxAdjust9265Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga2fdef0663434fcbaba997c9ac63b5952.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga2fdef0663434fcbaba997c9ac63b5952.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9265Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9265.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9265Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9265Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9265.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga31ea7b195aff46a10aca8fb0fda45b7c.html language=enus -->
## TOPIC 00029: DAQmxAdjust9210Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga31ea7b195aff46a10aca8fb0fda45b7c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga31ea7b195aff46a10aca8fb0fda45b7c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9210Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9210.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9210Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9210Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9210.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga3e16cc4ac0c6d9bbe85169b2221efc71.html language=enus -->
## TOPIC 00030: DAQmxAdjust9208GainCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga3e16cc4ac0c6d9bbe85169b2221efc71.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga3e16cc4ac0c6d9bbe85169b2221efc71.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9208GainCal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration gain constants for an NI 9208.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the

### DAQmxAdjust9208GainCal

#### Syntax

int32 __CFUNC DAQmxAdjust9208GainCal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) gain constants for an NI 9208.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga3e6440e0f9ba9483ea542b7dd51a20ab.html language=enus -->
## TOPIC 00031: DAQmxAdjust9202Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga3e6440e0f9ba9483ea542b7dd51a20ab.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga3e6440e0f9ba9483ea542b7dd51a20ab.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9202Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9202.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9202Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9202Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9202.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga492671f0b74d2f574b39de344d12cec2.html language=enus -->
## TOPIC 00032: DAQmxAdjust9208OffsetCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga492671f0b74d2f574b39de344d12cec2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga492671f0b74d2f574b39de344d12cec2.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9208OffsetCal(CalHandle calHandle, const char channelNames[])RemarksAdjusts the external calibration offset constants for an NI 9208.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxInitE

### DAQmxAdjust9208OffsetCal

#### Syntax

int32 __CFUNC DAQmxAdjust9208OffsetCal(CalHandle calHandle, const char channelNames[])

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) offset constants for an NI 9208.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga49cd0c2994bf177b36bac4fa0ead63b9.html language=enus -->
## TOPIC 00033: DAQmxAdjust9212Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga49cd0c2994bf177b36bac4fa0ead63b9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga49cd0c2994bf177b36bac4fa0ead63b9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9212Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9212.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9212Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9212Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9212.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga5879aea6da92f9cca511fe1f5754501b.html language=enus -->
## TOPIC 00034: DAQmxAdjust9246Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga5879aea6da92f9cca511fe1f5754501b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga5879aea6da92f9cca511fe1f5754501b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9246Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9246.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9246Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9246Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9246.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga593513ed2c7f74fefd8f770dc00af506.html language=enus -->
## TOPIC 00035: DAQmxAdjust9242Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga593513ed2c7f74fefd8f770dc00af506.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga593513ed2c7f74fefd8f770dc00af506.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9242Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9242.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9242Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9242Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9242.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga5afd6d9ee7a8926dcf146aa49a348f71.html language=enus -->
## TOPIC 00036: DAQmxAdjust9209GainCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga5afd6d9ee7a8926dcf146aa49a348f71.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga5afd6d9ee7a8926dcf146aa49a348f71.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9209GainCal(CalHandle calHandle, const char channelNames[], int32 terminalConfig, float64 value)RemarksAdjusts the external calibration gain constants for an NI 9209.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that

### DAQmxAdjust9209GainCal

#### Syntax

int32 __CFUNC DAQmxAdjust9209GainCal(CalHandle calHandle, const char channelNames[], int32 terminalConfig, float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) gain constants for an NI 9209.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| terminalConfig | [in] | int32 | The input terminal configuration for the channel. ValueDescriptionDAQmx_Val_RSEReferenced single-ended modeDAQmx_Val_DiffDifferential mode |
| Value | Description |  |  |
| DAQmx_Val_RSE | Referenced single-ended mode |  |  |
| DAQmx_Val_Diff | Differential mode |  |  |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga5b869402ce2cbbdb1ef073998ef86582.html language=enus -->
## TOPIC 00037: DAQmxAdjust9628AICal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga5b869402ce2cbbdb1ef073998ef86582.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga5b869402ce2cbbdb1ef073998ef86582.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9628AICal(CalHandle calHandle, const char channelNames[], float64 rangeMin, float64 rangeMax, float64 value)RemarksAdjusts the external calibration constants for a 9628.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session t

### DAQmxAdjust9628AICal

#### Syntax

int32 __CFUNC DAQmxAdjust9628AICal(CalHandle calHandle, const char channelNames[], float64 rangeMin, float64 rangeMax, float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for a 9628.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| rangeMin | [in] | float64 | The minimum value in the range. |
| rangeMax | [in] | float64 | The maximum value in the range. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga6e218d9a03af475289070060c06bf40e.html language=enus -->
## TOPIC 00038: DAQmxAdjust9218Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga6e218d9a03af475289070060c06bf40e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga6e218d9a03af475289070060c06bf40e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9218Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9218.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9218Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9218Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9218.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga6e6cee1024cb45655c8d0785757bc9d6.html language=enus -->
## TOPIC 00039: DAQmxAdjust9247Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga6e6cee1024cb45655c8d0785757bc9d6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga6e6cee1024cb45655c8d0785757bc9d6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9247Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9247.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9247Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9247Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9247.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga6f497a671cb34217c38fefca4753739e.html language=enus -->
## TOPIC 00040: DAQmxAdjust9201Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga6f497a671cb34217c38fefca4753739e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga6f497a671cb34217c38fefca4753739e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9201Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9201.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9201Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9201Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9201.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga6fce275d63e9f863d6ff276e19d1618f.html language=enus -->
## TOPIC 00041: DAQmxAdjust9231Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga6fce275d63e9f863d6ff276e19d1618f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga6fce275d63e9f863d6ff276e19d1618f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9231Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9231.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9231Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9231Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9231.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga7e6f6060bff0b9099dd14283a2b3a405.html language=enus -->
## TOPIC 00042: DAQmxAdjust9228Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga7e6f6060bff0b9099dd14283a2b3a405.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga7e6f6060bff0b9099dd14283a2b3a405.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9228Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9228.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9228Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9228Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9228.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga8595accfe4e5eebd8204222ab7a2879a.html language=enus -->
## TOPIC 00043: DAQmxAdjust9225Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga8595accfe4e5eebd8204222ab7a2879a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga8595accfe4e5eebd8204222ab7a2879a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9225Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9225.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9225Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9225Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9225.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga8a97355aac29ec22786836e0fa51b563.html language=enus -->
## TOPIC 00044: DAQmxAdjust9226Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga8a97355aac29ec22786836e0fa51b563.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga8a97355aac29ec22786836e0fa51b563.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9226Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9226.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9226Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9226Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9226.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga910a6785ea6cd5cc9aff5bc65e930381.html language=enus -->
## TOPIC 00045: DAQmxAdjust9207OffsetCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga910a6785ea6cd5cc9aff5bc65e930381.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga910a6785ea6cd5cc9aff5bc65e930381.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9207OffsetCal(CalHandle calHandle, const char channelNames[])RemarksAdjusts the external calibration offset constants for an NI 9207.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxInitE

### DAQmxAdjust9207OffsetCal

#### Syntax

int32 __CFUNC DAQmxAdjust9207OffsetCal(CalHandle calHandle, const char channelNames[])

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) offset constants for an NI 9207.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga91793753e77fbd870a5e4c3aaed626e3.html language=enus -->
## TOPIC 00046: DAQmxAdjust9638AICal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga91793753e77fbd870a5e4c3aaed626e3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1ga91793753e77fbd870a5e4c3aaed626e3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9638AICal(CalHandle calHandle, const char channelNames[], float64 rangeMin, float64 rangeMax, float64 value)RemarksAdjusts the external calibration constants for a 9638.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session t

### DAQmxAdjust9638AICal

#### Syntax

int32 __CFUNC DAQmxAdjust9638AICal(CalHandle calHandle, const char channelNames[], float64 rangeMin, float64 rangeMax, float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for a 9638.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| rangeMin | [in] | float64 | The minimum value in the range. |
| rangeMax | [in] | float64 | The maximum value in the range. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gaa11a4c0382c0bb25a9a9d884acacbfc3.html language=enus -->
## TOPIC 00047: DAQmxAdjust9234GainCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gaa11a4c0382c0bb25a9a9d884acacbfc3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gaa11a4c0382c0bb25a9a9d884acacbfc3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9234GainCal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration gain constants for an NI 9234.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the

### DAQmxAdjust9234GainCal

#### Syntax

int32 __CFUNC DAQmxAdjust9234GainCal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) gain constants for an NI 9234.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gaa7d88a7bf677f9837ba99e16a5386f3d.html language=enus -->
## TOPIC 00048: DAQmxAdjust9232Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gaa7d88a7bf677f9837ba99e16a5386f3d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gaa7d88a7bf677f9837ba99e16a5386f3d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9232Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9232.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9232Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9232Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9232.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gabb07c8c445f5cc85959b265a17851862.html language=enus -->
## TOPIC 00049: DAQmxAdjust9263Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gabb07c8c445f5cc85959b265a17851862.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gabb07c8c445f5cc85959b265a17851862.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9263Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9263.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9263Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9263Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9263.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gac827e5940f8f61d6685de38060aaa81f.html language=enus -->
## TOPIC 00050: DAQmxAdjust9217Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gac827e5940f8f61d6685de38060aaa81f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gac827e5940f8f61d6685de38060aaa81f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9217Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9217.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9217Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9217Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9217.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gac8df7a102a56c99654cc0ceffb991aa3.html language=enus -->
## TOPIC 00051: DAQmxAdjust9320Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gac8df7a102a56c99654cc0ceffb991aa3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gac8df7a102a56c99654cc0ceffb991aa3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9320Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9320.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9320Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9320Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9320.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gac91364aa24d1f5c416f60741f9403357.html language=enus -->
## TOPIC 00052: DAQmxAdjust9213Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gac91364aa24d1f5c416f60741f9403357.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gac91364aa24d1f5c416f60741f9403357.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9213Cal(CalHandle calHandle, const char channelNames[], float64 rangeMin, float64 rangeMax, float64 value)RemarksAdjusts the external calibration constants for an NI 9213.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session

### DAQmxAdjust9213Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9213Cal(CalHandle calHandle, const char channelNames[], float64 rangeMin, float64 rangeMax, float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9213.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| rangeMin | [in] | float64 | The minimum value in the range, in volts. |
| rangeMax | [in] | float64 | The maximum value in the range, in volts. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gac9f3bbf34fe42b7d719a6e2ecb21afcc.html language=enus -->
## TOPIC 00053: DAQmxAdjust9260Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gac9f3bbf34fe42b7d719a6e2ecb21afcc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gac9f3bbf34fe42b7d719a6e2ecb21afcc.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9260Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9260.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9260Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9260Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9260.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gaca9184d50a1a15067d212acddffcaadd.html language=enus -->
## TOPIC 00054: DAQmxAdjust9203GainCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gaca9184d50a1a15067d212acddffcaadd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gaca9184d50a1a15067d212acddffcaadd.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9203GainCal(CalHandle calHandle, const char channelNames[], float64 rangeMin, float64 rangeMax, float64 value)RemarksAdjusts the external calibration gain constants for an NI 9203.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibratio

### DAQmxAdjust9203GainCal

#### Syntax

int32 __CFUNC DAQmxAdjust9203GainCal(CalHandle calHandle, const char channelNames[], float64 rangeMin, float64 rangeMax, float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) gain constants for an NI 9203.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| rangeMin | [in] | float64 | The minimum value in the range, in amps. |
| rangeMax | [in] | float64 | The maximum value in the range, in amps. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gacae698bfa4c992fd9624cd77b4254ee6.html language=enus -->
## TOPIC 00055: DAQmxAdjust9224Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gacae698bfa4c992fd9624cd77b4254ee6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gacae698bfa4c992fd9624cd77b4254ee6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9224Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9224.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9224Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9224Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9224.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gacd10601f82eed167727568e71b97f958.html language=enus -->
## TOPIC 00056: DAQmxAdjust9221Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gacd10601f82eed167727568e71b97f958.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gacd10601f82eed167727568e71b97f958.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9221Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9221.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9221Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9221Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9221.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gadc65c6383b713b14abc8f381fbecfc40.html language=enus -->
## TOPIC 00057: DAQmxAdjust9214Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gadc65c6383b713b14abc8f381fbecfc40.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gadc65c6383b713b14abc8f381fbecfc40.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9214Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9214.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9214Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9214Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9214.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gadf47661a871faf419ee2633ce2b4b8b4.html language=enus -->
## TOPIC 00058: DAQmxAdjust9211Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gadf47661a871faf419ee2633ce2b4b8b4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gadf47661a871faf419ee2633ce2b4b8b4.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9211Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9211.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9211Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9211Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9211.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gae7282c4e819fb07f6635f90cce0436df.html language=enus -->
## TOPIC 00059: DAQmxAdjust9250Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gae7282c4e819fb07f6635f90cce0436df.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gae7282c4e819fb07f6635f90cce0436df.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9250Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9250.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9250Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9250Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9250.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gaf295436dd56822599f9aa0d2f7ae4a00.html language=enus -->
## TOPIC 00060: DAQmxAdjust9251Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gaf295436dd56822599f9aa0d2f7ae4a00.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gaf295436dd56822599f9aa0d2f7ae4a00.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9251Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9251.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9251Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9251Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9251.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gaf915cdf641691690479ad577c311a939.html language=enus -->
## TOPIC 00061: DAQmxAdjust9264Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gaf915cdf641691690479ad577c311a939.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gaf915cdf641691690479ad577c311a939.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9264Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9264.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9264Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9264Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9264.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gafba67ced8789f867a08107a70c0f0558.html language=enus -->
## TOPIC 00062: DAQmxAdjust9269Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gafba67ced8789f867a08107a70c0f0558.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__adjust__c__series__calibration_1gafba67ced8789f867a08107a70c0f0558.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust9269Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for an NI 9269.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIni

### DAQmxAdjust9269Cal

#### Syntax

int32 __CFUNC DAQmxAdjust9269Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9269.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga1f9dfe1c193328fa921bcb9a6699370c.html language=enus -->
## TOPIC 00063: DAQmxGet9250CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga1f9dfe1c193328fa921bcb9a6699370c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga1f9dfe1c193328fa921bcb9a6699370c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9250CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibrati

### DAQmxGet9250CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9250CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga2000e054efa11027b39ac3596c40b91e.html language=enus -->
## TOPIC 00064: DAQmxGet9224CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga2000e054efa11027b39ac3596c40b91e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga2000e054efa11027b39ac3596c40b91e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9224CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibrati

### DAQmxGet9224CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9224CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga28bba81ddab81dd7a4ba90252f5dfc22.html language=enus -->
## TOPIC 00065: DAQmxGet9628AICalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga28bba81ddab81dd7a4ba90252f5dfc22.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga28bba81ddab81dd7a4ba90252f5dfc22.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9628AICalAdjustPoints(CalHandle calHandle, float64 rangeMin, float64 rangeMax, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in

### DAQmxGet9628AICalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9628AICalAdjustPoints(CalHandle calHandle, float64 rangeMin, float64 rangeMax, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| rangeMin | [in] | float64 | The minimum value in the range. |
| rangeMax | [in] | float64 | The maximum value in the range. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga325575ba580203ca81247693118414b3.html language=enus -->
## TOPIC 00066: DAQmxGet9221CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga325575ba580203ca81247693118414b3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga325575ba580203ca81247693118414b3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9221CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the c

### DAQmxGet9221CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9221CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga3b534d36c7f0b24b244fbeee51b44bd4.html language=enus -->
## TOPIC 00067: DAQmxGet9629AOCalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga3b534d36c7f0b24b244fbeee51b44bd4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga3b534d36c7f0b24b244fbeee51b44bd4.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9629AOCalAdjustPoints(CalHandle calHandle, int32 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the DAC values with which to configure the device under calibration.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that

### DAQmxGet9629AOCalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9629AOCalAdjustPoints(CalHandle calHandle, int32 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the DAC values with which to configure the device under calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | int32 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga48b35fef75d7b36d2d5054bb5462403a.html language=enus -->
## TOPIC 00068: DAQmxGet9232CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga48b35fef75d7b36d2d5054bb5462403a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga48b35fef75d7b36d2d5054bb5462403a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9232CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the c

### DAQmxGet9232CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9232CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga4c0a48e9c25a8d733c059bd4a147d51d.html language=enus -->
## TOPIC 00069: DAQmxGet9207CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga4c0a48e9c25a8d733c059bd4a147d51d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga4c0a48e9c25a8d733c059bd4a147d51d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9207CalAdjustPoints(CalHandle calHandle, const char channelNames[], float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA

### DAQmxGet9207CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9207CalAdjustPoints(CalHandle calHandle, const char channelNames[], float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga5261903bdaf6a2ac2857f740ae0bcc32.html language=enus -->
## TOPIC 00070: DAQmxGet9209CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga5261903bdaf6a2ac2857f740ae0bcc32.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga5261903bdaf6a2ac2857f740ae0bcc32.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9209CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the c

### DAQmxGet9209CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9209CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga527edc69ce098cf12ac7693484c210f1.html language=enus -->
## TOPIC 00071: DAQmxGet9213CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga527edc69ce098cf12ac7693484c210f1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga527edc69ce098cf12ac7693484c210f1.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9213CalAdjustPoints(CalHandle calHandle, float64 rangeMin, float64 rangeMax, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHan

### DAQmxGet9213CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9213CalAdjustPoints(CalHandle calHandle, float64 rangeMin, float64 rangeMax, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| rangeMin | [in] | float64 | The minimum value in the range, in volts. |
| rangeMax | [in] | float64 | The maximum value in the range, in volts. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga562342eccee3b78e1763029e1cc80dea.html language=enus -->
## TOPIC 00072: DAQmxGet9222CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga562342eccee3b78e1763029e1cc80dea.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga562342eccee3b78e1763029e1cc80dea.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9222CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the c

### DAQmxGet9222CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9222CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga5748e2256ee59b95af07118232f0a538.html language=enus -->
## TOPIC 00073: DAQmxGet9251CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga5748e2256ee59b95af07118232f0a538.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga5748e2256ee59b95af07118232f0a538.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9251CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibrati

### DAQmxGet9251CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9251CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga5a37c517be2a2e8021f176b50f8ced88.html language=enus -->
## TOPIC 00074: DAQmxGet9214CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga5a37c517be2a2e8021f176b50f8ced88.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga5a37c517be2a2e8021f176b50f8ced88.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9214CalAdjustPoints(CalHandle calHandle, const char channelNames[], float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]Ca

### DAQmxGet9214CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9214CalAdjustPoints(CalHandle calHandle, const char channelNames[], float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga5c97cf097c6c25488aec2f9871e22806.html language=enus -->
## TOPIC 00075: DAQmxGet9208CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga5c97cf097c6c25488aec2f9871e22806.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga5c97cf097c6c25488aec2f9871e22806.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9208CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference current values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the c

### DAQmxGet9208CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9208CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference current values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga5caf761eb86ae7251096ec1e8c786ebf.html language=enus -->
## TOPIC 00076: DAQmxGet9252CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga5caf761eb86ae7251096ec1e8c786ebf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga5caf761eb86ae7251096ec1e8c786ebf.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9252CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the c

### DAQmxGet9252CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9252CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga863e273075d2fe67137b9787cf30b6d0.html language=enus -->
## TOPIC 00077: DAQmxGet9203CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga863e273075d2fe67137b9787cf30b6d0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga863e273075d2fe67137b9787cf30b6d0.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9203CalAdjustPoints(CalHandle calHandle, float64 rangeMin, float64 rangeMax, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference current values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHan

### DAQmxGet9203CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9203CalAdjustPoints(CalHandle calHandle, float64 rangeMin, float64 rangeMax, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference current values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| rangeMin | [in] | float64 | The minimum value in the range, in amps. |
| rangeMax | [in] | float64 | The maximum value in the range, in amps. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga8ea8a9dd0e1af93726f83d7211097f24.html language=enus -->
## TOPIC 00078: DAQmxGet9238CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga8ea8a9dd0e1af93726f83d7211097f24.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga8ea8a9dd0e1af93726f83d7211097f24.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9238CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibrati

### DAQmxGet9238CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9238CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga8f32f2a828620180d50ee90fa51be082.html language=enus -->
## TOPIC 00079: DAQmxGet9638AOCalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga8f32f2a828620180d50ee90fa51be082.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga8f32f2a828620180d50ee90fa51be082.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9638AOCalAdjustPoints(CalHandle calHandle, int32 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the DAC values with which to configure the device under calibration.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that

### DAQmxGet9638AOCalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9638AOCalAdjustPoints(CalHandle calHandle, int32 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the DAC values with which to configure the device under calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | int32 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga90bd295519051609d7fbda95e33f25ed.html language=enus -->
## TOPIC 00080: DAQmxGet9628AOCalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga90bd295519051609d7fbda95e33f25ed.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga90bd295519051609d7fbda95e33f25ed.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9628AOCalAdjustPoints(CalHandle calHandle, int32 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the DAC values with which to configure the device under calibration.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that

### DAQmxGet9628AOCalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9628AOCalAdjustPoints(CalHandle calHandle, int32 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the DAC values with which to configure the device under calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | int32 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga96f3a683702a440df75996c76d477d35.html language=enus -->
## TOPIC 00081: DAQmxGet9212CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga96f3a683702a440df75996c76d477d35.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga96f3a683702a440df75996c76d477d35.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9212CalAdjustPoints(CalHandle calHandle, const char channelNames[], float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA

### DAQmxGet9212CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9212CalAdjustPoints(CalHandle calHandle, const char channelNames[], float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga980246002c5fca888eea251fca6851a4.html language=enus -->
## TOPIC 00082: DAQmxGet9202CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga980246002c5fca888eea251fca6851a4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1ga980246002c5fca888eea251fca6851a4.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9202CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the c

### DAQmxGet9202CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9202CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gaa0a58abb82106b54813e573dc197d687.html language=enus -->
## TOPIC 00083: DAQmxGet9265CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gaa0a58abb82106b54813e573dc197d687.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gaa0a58abb82106b54813e573dc197d687.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9265CalAdjustPoints(CalHandle calHandle, int32 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the DAC values with which to configure the device under calibration.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that y

### DAQmxGet9265CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9265CalAdjustPoints(CalHandle calHandle, int32 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the DAC values with which to configure the device under calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | int32 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gaa94289e2b36608d8e5f99782bcba8c6b.html language=enus -->
## TOPIC 00084: DAQmxGet9253CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gaa94289e2b36608d8e5f99782bcba8c6b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gaa94289e2b36608d8e5f99782bcba8c6b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9253CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibrati

### DAQmxGet9253CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9253CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gab5769b5817a4af2fdc6257a0239cd87a.html language=enus -->
## TOPIC 00085: DAQmxGet9260CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gab5769b5817a4af2fdc6257a0239cd87a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gab5769b5817a4af2fdc6257a0239cd87a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9260CalAdjustPoints(CalHandle calHandle, int32 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the DAC values with which to configure the device under calibration.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that y

### DAQmxGet9260CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9260CalAdjustPoints(CalHandle calHandle, int32 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the DAC values with which to configure the device under calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | int32 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gab920b246796831deec3d405feb81c16d.html language=enus -->
## TOPIC 00086: DAQmxGet9629AICalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gab920b246796831deec3d405feb81c16d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gab920b246796831deec3d405feb81c16d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9629AICalAdjustPoints(CalHandle calHandle, float64 rangeMin, float64 rangeMax, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in

### DAQmxGet9629AICalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9629AICalAdjustPoints(CalHandle calHandle, float64 rangeMin, float64 rangeMax, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| rangeMin | [in] | float64 | The minimum value in the range. |
| rangeMax | [in] | float64 | The maximum value in the range. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gabac4ab6fcc389a25882cb450abfdb7fd.html language=enus -->
## TOPIC 00087: DAQmxGet9216CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gabac4ab6fcc389a25882cb450abfdb7fd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gabac4ab6fcc389a25882cb450abfdb7fd.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9216CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the c

### DAQmxGet9216CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9216CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gac377e0a2a712ff9c0ac56e6a9119d4a3.html language=enus -->
## TOPIC 00088: DAQmxGet9775CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gac377e0a2a712ff9c0ac56e6a9119d4a3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gac377e0a2a712ff9c0ac56e6a9119d4a3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9775CalAdjustPoints(CalHandle calHandle, uInt32 coupling, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference

### DAQmxGet9775CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9775CalAdjustPoints(CalHandle calHandle, uInt32 coupling, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| coupling | [in] | uInt32 | Specifies the coupling setting to calibrate. ValueDescriptionDAQmx_Val_ACAC couplingDAQmx_Val_DCDC coupling |
| Value | Description |  |  |
| DAQmx_Val_AC | AC coupling |  |  |
| DAQmx_Val_DC | DC coupling |  |  |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gacb04e443738d892937beb3de560f04b6.html language=enus -->
## TOPIC 00089: DAQmxGet9264CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gacb04e443738d892937beb3de560f04b6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gacb04e443738d892937beb3de560f04b6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9264CalAdjustPoints(CalHandle calHandle, int32 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the DAC values with which to configure the device under calibration.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that y

### DAQmxGet9264CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9264CalAdjustPoints(CalHandle calHandle, int32 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the DAC values with which to configure the device under calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | int32 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gacec6bf5b5bf28449d21ec67de77bb293.html language=enus -->
## TOPIC 00090: DAQmxGet9234CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gacec6bf5b5bf28449d21ec67de77bb293.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gacec6bf5b5bf28449d21ec67de77bb293.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9234CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the c

### DAQmxGet9234CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9234CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gad648608ab8c8a99935d731d894b1449f.html language=enus -->
## TOPIC 00091: DAQmxGet9263CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gad648608ab8c8a99935d731d894b1449f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gad648608ab8c8a99935d731d894b1449f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9263CalAdjustPoints(CalHandle calHandle, int32 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the DAC values with which to configure the device under calibration.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that y

### DAQmxGet9263CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9263CalAdjustPoints(CalHandle calHandle, int32 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the DAC values with which to configure the device under calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | int32 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gadc0be249039f0955476b1f98c4ec31e2.html language=enus -->
## TOPIC 00092: DAQmxGet9247CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gadc0be249039f0955476b1f98c4ec31e2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gadc0be249039f0955476b1f98c4ec31e2.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9247CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the c

### DAQmxGet9247CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9247CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gaeab22375d9dbc6447ed552f4da4c37b7.html language=enus -->
## TOPIC 00093: DAQmxGet9262CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gaeab22375d9dbc6447ed552f4da4c37b7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__get__c_f785f10873e6e809484f1e132f7c6c41_1gaeab22375d9dbc6447ed552f4da4c37b7.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet9262CalAdjustPoints(CalHandle calHandle, int32 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the DAC values with which to configure the device under calibration.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that y

### DAQmxGet9262CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet9262CalAdjustPoints(CalHandle calHandle, int32 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the DAC values with which to configure the device under calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | int32 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get C Series Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration.html language=enus -->
## TOPIC 00094: Setup C Series Calibration

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxSetup9218CalDAQmxSetup9219CalDAQmxSetup9242CalDAQmxSetup9244CalDAQmxSetup9260CalDAQmxSetup9262CalDAQmxSetup9263CalDAQmxSetup9264CalDAQmxSetup9265CalDAQmxSetup9266CalDAQmxSetup9269CalDAQmxSetup9628AOCalDAQmxSetup9629AOCalDAQmxSetup9638AOCalAttachmentsNone

### Setup C Series Calibration

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxSetup9218Cal |  |
| DAQmxSetup9219Cal |  |
| DAQmxSetup9242Cal |  |
| DAQmxSetup9244Cal |  |
| DAQmxSetup9260Cal |  |
| DAQmxSetup9262Cal |  |
| DAQmxSetup9263Cal |  |
| DAQmxSetup9264Cal |  |
| DAQmxSetup9265Cal |  |
| DAQmxSetup9266Cal |  |
| DAQmxSetup9269Cal |  |
| DAQmxSetup9628AOCal |  |
| DAQmxSetup9629AOCal |  |
| DAQmxSetup9638AOCal |  |

#### Attachments

None

Parent topic:

C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga0b2549286e664456a33898a60e5614d7.html language=enus -->
## TOPIC 00095: DAQmxSetup9244Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga0b2549286e664456a33898a60e5614d7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga0b2549286e664456a33898a60e5614d7.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup9244Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksReads the specified value from the ADC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmxGet9244CalAdjustPoints function.ParametersNameDirecti

### DAQmxSetup9244Cal

#### Syntax

int32 __CFUNC DAQmxSetup9244Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Reads the specified value from the ADC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmxGet9244CalAdjustPoints function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The binary number to read from the ADC. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Setup C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga13f0c8812272f70f6ae943656433bdd9.html language=enus -->
## TOPIC 00096: DAQmxSetup9219Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga13f0c8812272f70f6ae943656433bdd9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga13f0c8812272f70f6ae943656433bdd9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup9219Cal(CalHandle calHandle, const char channelNames[], float64 rangeMin, float64 rangeMax, int32 measType, int32 bridgeConfig)RemarksSets up external calibration for an NI 9219 device.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibr

### DAQmxSetup9219Cal

#### Syntax

int32 __CFUNC DAQmxSetup9219Cal(CalHandle calHandle, const char channelNames[], float64 rangeMin, float64 rangeMax, int32 measType, int32 bridgeConfig)

#### Remarks

Sets up external calibration for an NI 9219 device.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| rangeMin | [in] | float64 | The minimum value in the range, in the units of the measurement type specified by measType. If your measType is RTD, you must specify your minimum range in ohms. |
| rangeMax | [in] | float64 | The maximum value in the range, in the units of the measurement type specified by measType. If your measType is RTD, you must specify your maximum range in ohms. |
| measType | [in] | int32 | the type of measurement for the device. ValueDescriptionDAQmx_Val_VoltageVoltageDAQmx_Val_CurrentCurrentDAQmx_Val_ResistanceResistanceDAQmx_Val_Temp_RTDRTDDAQmx_Val_BridgeWheatstone Bridge |
| Value | Description |  |  |
| DAQmx_Val_Voltage | Voltage |  |  |
| DAQmx_Val_Current | Current |  |  |
| DAQmx_Val_Resistance | Resistance |  |  |
| DAQmx_Val_Temp_RTD | RTD |  |  |
| DAQmx_Val_Bridge | Wheatstone Bridge |  |  |
| bridgeConfig | [in] | int32 | The type of Wheatstone bridge the sensor is. ValueDescriptionDAQmx_Val_FullBridgeSensor is a full bridge. If you set useExcitForScaling to TRUE, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation.DAQmx_Val_HalfBridgeSensor is a half bridge. If you set useExcitForScaling to TRUE, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation.DAQmx_Val_QuarterBridgeSensor is a quarter bridge. If you set useExcitForScaling to TRUE, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation.DAQmx_Val_NoBridgeSensor is not a Wheatstone bridge. |
| Value | Description |  |  |
| DAQmx_Val_FullBridge | Sensor is a full bridge. If you set useExcitForScaling to TRUE, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation. |  |  |
| DAQmx_Val_HalfBridge | Sensor is a half bridge. If you set useExcitForScaling to TRUE, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation. |  |  |
| DAQmx_Val_QuarterBridge | Sensor is a quarter bridge. If you set useExcitForScaling to TRUE, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation. |  |  |
| DAQmx_Val_NoBridge | Sensor is not a Wheatstone bridge. |  |  |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Setup C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga2962c1e53daf4981f3c7821591ca07f1.html language=enus -->
## TOPIC 00097: DAQmxSetup9265Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga2962c1e53daf4981f3c7821591ca07f1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga2962c1e53daf4981f3c7821591ca07f1.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup9265Cal(CalHandle calHandle, const char channelNames[], int32 value)RemarksWrites the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmxGet9265CalAdjustPoints function.ParametersNameDir

### DAQmxSetup9265Cal

#### Syntax

int32 __CFUNC DAQmxSetup9265Cal(CalHandle calHandle, const char channelNames[], int32 value)

#### Remarks

Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmxGet9265CalAdjustPoints function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | int32 | The binary number to write to the DAC. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Setup C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga42f31fe33e2378e7a8e47260eb716687.html language=enus -->
## TOPIC 00098: DAQmxSetup9628AOCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga42f31fe33e2378e7a8e47260eb716687.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga42f31fe33e2378e7a8e47260eb716687.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup9628AOCal(CalHandle calHandle, const char channelNames[], int32 value)RemarksInitializes an NI 9628 device for calibrating the specified channel type. Refer to the calibration procedure for your device for specific calibration instructions.ParametersNameDirectionTypeDes

### DAQmxSetup9628AOCal

#### Syntax

int32 __CFUNC DAQmxSetup9628AOCal(CalHandle calHandle, const char channelNames[], int32 value)

#### Remarks

Initializes an NI 9628 device for calibrating the specified channel type. Refer to the calibration procedure for your device for specific calibration instructions.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | int32 | The binary number to write to the DAC. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Setup C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga7370f5174bfadbcf6f42c14a83c37f44.html language=enus -->
## TOPIC 00099: DAQmxSetup9266Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga7370f5174bfadbcf6f42c14a83c37f44.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga7370f5174bfadbcf6f42c14a83c37f44.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup9266Cal(CalHandle calHandle, const char channelNames[], int32 value)RemarksWrites the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmxGet9266CalAdjustPoints function.ParametersNameDir

### DAQmxSetup9266Cal

#### Syntax

int32 __CFUNC DAQmxSetup9266Cal(CalHandle calHandle, const char channelNames[], int32 value)

#### Remarks

Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmxGet9266CalAdjustPoints function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | int32 | The binary number to write to the DAC. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Setup C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga9888737c3678f134d7817af9869a3cb3.html language=enus -->
## TOPIC 00100: DAQmxSetup9264Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga9888737c3678f134d7817af9869a3cb3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1ga9888737c3678f134d7817af9869a3cb3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup9264Cal(CalHandle calHandle, const char channelNames[], int32 value)RemarksWrites the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmxGet9264CalAdjustPoints function.ParametersNameDir

### DAQmxSetup9264Cal

#### Syntax

int32 __CFUNC DAQmxSetup9264Cal(CalHandle calHandle, const char channelNames[], int32 value)

#### Remarks

Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmxGet9264CalAdjustPoints function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | int32 | The binary number to write to the DAC. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Setup C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1gade122ada159c7f100fed506bfc971ca6.html language=enus -->
## TOPIC 00101: DAQmxSetup9242Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1gade122ada159c7f100fed506bfc971ca6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__c__series__calibration__setup__c__series__calibration_1gade122ada159c7f100fed506bfc971ca6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup9242Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksReads the specified value from the ADC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmxGet9242CalAdjustPoints function.ParametersNameDirecti

### DAQmxSetup9242Cal

#### Syntax

int32 __CFUNC DAQmxSetup9242Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Reads the specified value from the ADC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmxGet9242CalAdjustPoints function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The binary number to read from the ADC. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Setup C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration.html language=enus -->
## TOPIC 00102: DSA Calibration

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxAdjust4463CalDAQmxAdjust4610CalDAQmxAdjustDSAAICalDAQmxAdjustDSAAICalExDAQmxAdjustDSAAICalWithGainAndCouplingDAQmxAdjustDSAAOCalDAQmxAdjustDSAAOTimebaseCalDAQmxAdjustDSATimebaseCalDAQmxDSASetCalTempDAQmxGet4463AdjustPointsDAQmxSetup4463CalDAQmxSetup4480CalD

### DSA Calibration

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxAdjust4463Cal |  |
| DAQmxAdjust4610Cal |  |
| DAQmxAdjustDSAAICal |  |
| DAQmxAdjustDSAAICalEx |  |
| DAQmxAdjustDSAAICalWithGainAndCoupling |  |
| DAQmxAdjustDSAAOCal |  |
| DAQmxAdjustDSAAOTimebaseCal |  |
| DAQmxAdjustDSATimebaseCal |  |
| DAQmxDSASetCalTemp |  |
| DAQmxGet4463AdjustPoints |  |
| DAQmxSetup4463Cal |  |
| DAQmxSetup4480Cal |  |
| DAQmxSetupDSAAOTimebaseCal |  |

#### Attachments

None

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1ga5ac7c0c9992a2f92b66abea20f416a3c.html language=enus -->
## TOPIC 00103: DAQmxSetupDSAAOTimebaseCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1ga5ac7c0c9992a2f92b66abea20f416a3c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1ga5ac7c0c9992a2f92b66abea20f416a3c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetupDSAAOTimebaseCal(CalHandle calHandle, float64 *expectedFrequency)RemarksGenerates a sine wave of a fixed frequency from the DSA device. You must measure the frequency of the generated sine wave and pass that value into the DAQmxAdjustDSAAOTimebaseCal.ParametersNameDirec

### DAQmxSetupDSAAOTimebaseCal

#### Syntax

int32 __CFUNC DAQmxSetupDSAAOTimebaseCal(CalHandle calHandle, float64 *expectedFrequency)

#### Remarks

Generates a sine wave of a fixed frequency from the DSA device. You must measure the frequency of the generated sine wave and pass that value into the DAQmxAdjustDSAAOTimebaseCal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

DSA Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1ga5bb89a536a93eb638d9c906dd6cd1a9f.html language=enus -->
## TOPIC 00104: DAQmxAdjustDSATimebaseCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1ga5bb89a536a93eb638d9c906dd6cd1a9f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1ga5bb89a536a93eb638d9c906dd6cd1a9f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjustDSATimebaseCal(CalHandle calHandle, float64 referenceFrequency)RemarksAdjusts the external calibration constant for the timebase of a DSA device with an adjustable oscillator. You must connect a sinusoidal signal with a known frequency to the device and specify that fr

### DAQmxAdjustDSATimebaseCal

#### Syntax

int32 __CFUNC DAQmxAdjustDSATimebaseCal(CalHandle calHandle, float64 referenceFrequency)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constant for the timebase of a DSA device with an adjustable oscillator. You must connect a sinusoidal signal with a known frequency to the device and specify that frequency with **referenceFrequency**.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| referenceFrequency | [in] | float64 | The frequency, in hertz, of the signal to use as a reference for calibration. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

DSA Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1ga6183953be7d188407363f086c0ffee80.html language=enus -->
## TOPIC 00105: DAQmxDSASetCalTemp

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1ga6183953be7d188407363f086c0ffee80.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1ga6183953be7d188407363f086c0ffee80.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxDSASetCalTemp(CalHandle calHandle, float64 temperature)RemarksSpecifies the temperature of a DSA device for the current external calibration session.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the

### DAQmxDSASetCalTemp

#### Syntax

int32 __CFUNC DAQmxDSASetCalTemp(CalHandle calHandle, float64 temperature)

#### Remarks

Specifies the temperature of a DSA device for the current external calibration session.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| temperature | [in] | float64 | The temperature of the device, in degrees Celsius. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

DSA Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1ga71b77db4ba5e1a6357eee8cc5833175a.html language=enus -->
## TOPIC 00106: DAQmxSetup4463Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1ga71b77db4ba5e1a6357eee8cc5833175a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1ga71b77db4ba5e1a6357eee8cc5833175a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup4463Cal(CalHandle calHandle, const char channelNames[], int32 terminalConfig, float64 gain, float64 outputVoltage)RemarksGenerates a specified voltage from the device. You must measure the voltage and pass that value into the DAQmxAdjust4463Cal.ParametersNameDirectionTy

### DAQmxSetup4463Cal

#### Syntax

int32 __CFUNC DAQmxSetup4463Cal(CalHandle calHandle, const char channelNames[], int32 terminalConfig, float64 gain, float64 outputVoltage)

#### Remarks

Generates a specified voltage from the device. You must measure the voltage and pass that value into the DAQmxAdjust4463Cal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| terminalConfig | [in] | int32 | The input terminal configuration for the channel. ValueDescriptionDAQmx_Val_DiffDifferential modeDAQmx_Val_PseudoDiffPseudodifferential mode |
| Value | Description |  |  |
| DAQmx_Val_Diff | Differential mode |  |  |
| DAQmx_Val_PseudoDiff | Pseudodifferential mode |  |  |
| gain | [in] | float64 | The gain setting to calibrate. |
| outputVoltage | [in] | float64 | The output voltage to generate, in Hz. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

DSA Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1ga9800b56ab7498f593ffae14dbd63dc61.html language=enus -->
## TOPIC 00107: DAQmxAdjustDSAAICalWithGainAndCoupling

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1ga9800b56ab7498f593ffae14dbd63dc61.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1ga9800b56ab7498f593ffae14dbd63dc61.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjustDSAAICalWithGainAndCoupling(CalHandle calHandle, int32 coupling, float64 gain, float64 referenceVoltage)RemarksAdjusts the external calibration constants for the analog input section of a DSA device with the specified gain and coupling configuration. You must connect a

### DAQmxAdjustDSAAICalWithGainAndCoupling

#### Syntax

int32 __CFUNC DAQmxAdjustDSAAICalWithGainAndCoupling(CalHandle calHandle, int32 coupling, float64 gain, float64 referenceVoltage)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for the analog input section of a DSA device with the specified gain and coupling configuration. You must connect a known voltage to the device and specify that voltage with the **referenceVoltage** parameter.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| coupling | [in] | int32 | The coupling setting, in decibels, to use for calibration. |
| gain | [in] | float64 | The gain setting, in decibels, to use for calibration. |
| referenceVoltage | [in] | float64 | The known voltage, in volts, to use as a reference for calibration. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

DSA Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1gae03fe40ced1223837d603c4e90e0eec3.html language=enus -->
## TOPIC 00108: DAQmxAdjust4610Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1gae03fe40ced1223837d603c4e90e0eec3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__dsa__calibration_1gae03fe40ced1223837d603c4e90e0eec3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust4610Cal(CalHandle calHandle, const char channelName[], float64 gain, float64 offset)RemarksAdjusts the external calibration gain constants for an NI 4610.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created

### DAQmxAdjust4610Cal

#### Syntax

int32 __CFUNC DAQmxAdjust4610Cal(CalHandle calHandle, const char channelName[], float64 gain, float64 offset)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) gain constants for an NI 4610.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelName | [in] | const char[] | The physical channel(s) to calibrate. |
| gain | [in] | float64 | The gain setting to calibrate. |
| offset | [in] | float64 | The offset at which to begin a read operation. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

DSA Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__external__calibration.html language=enus -->
## TOPIC 00109: External Calibration

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__external__calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__external__calibration.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxChangeExtCalPasswordDAQmxCloseExtCalDAQmxInitExtCalAttachmentsNone

### External Calibration

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxChangeExtCalPassword |  |
| DAQmxCloseExtCal |  |
| DAQmxInitExtCal |  |

#### Attachments

None

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__external__calibration_1ga14a3cd5d8cfcca647d2ccf367a2d457f.html language=enus -->
## TOPIC 00110: DAQmxChangeExtCalPassword

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__external__calibration_1ga14a3cd5d8cfcca647d2ccf367a2d457f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__external__calibration_1ga14a3cd5d8cfcca647d2ccf367a2d457f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxChangeExtCalPassword(const char deviceName[], const char password[], const char newPassword[])RemarksChanges the external calibration password of the device.ParametersNameDirectionTypeDescriptiondeviceName[in]const char[]Specifies the name to assign to the device. If unspeci

### DAQmxChangeExtCalPassword

#### Syntax

int32 __CFUNC DAQmxChangeExtCalPassword(const char deviceName[], const char password[], const char newPassword[])

#### Remarks

Changes the external calibration password of the device.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| deviceName | [in] | const char[] | Specifies the name to assign to the device. If unspecified, NI-DAQmx chooses the device name. |
| password | [in] | const char[] | The current calibration password for the device. This password is case sensitive. The default password for all NI products is NI. |
| newPassword | [in] | const char[] | The new password for the device. This password can be no longer than four characters. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__external__calibration_1ga2751dc7b0e8c5c4da97c57a79262032d.html language=enus -->
## TOPIC 00111: DAQmxInitExtCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__external__calibration_1ga2751dc7b0e8c5c4da97c57a79262032d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__external__calibration_1ga2751dc7b0e8c5c4da97c57a79262032d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxInitExtCal(const char deviceName[], const char password[], CalHandle *calHandle)RemarksStarts an external calibration session on a device.ParametersNameDirectionTypeDescriptiondeviceName[in]const char[]Specifies the name to assign to the device. If unspecified, NI-DAQmx choo

### DAQmxInitExtCal

#### Syntax

int32 __CFUNC DAQmxInitExtCal(const char deviceName[], const char password[], CalHandle *calHandle)

#### Remarks

Starts an [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) session on a device.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| deviceName | [in] | const char[] | Specifies the name to assign to the device. If unspecified, NI-DAQmx chooses the device name. |
| password | [in] | const char[] | The current calibration password for the device. This password is case sensitive. The default password for all NI products is NI. |
| calHandle | [out] | CalHandle * | A reference to the calibration session. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__external__calibration_1gaa64406e9a5d0a6e2db2899d7d0234baf.html language=enus -->
## TOPIC 00112: DAQmxCloseExtCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__external__calibration_1gaa64406e9a5d0a6e2db2899d7d0234baf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__external__calibration_1gaa64406e9a5d0a6e2db2899d7d0234baf.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCloseExtCal(CalHandle calHandle, int32 action)RemarksCloses an open external calibration session.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxInitExtCal function. action[in]int32Specifies h

### DAQmxCloseExtCal

#### Syntax

int32 __CFUNC DAQmxCloseExtCal(CalHandle calHandle, int32 action)

#### Remarks

Closes an open [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) session.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| action | [in] | int32 | Specifies how to close the calibration session. ValueDescriptionDAQmx_Val_Action_CommitSaves the calibration changes made in the sessionDAQmx_Val_Action_CancelCloses the session without saving any calibration changes |
| Value | Description |  |  |
| DAQmx_Val_Action_Commit | Saves the calibration changes made in the session |  |  |
| DAQmx_Val_Action_Cancel | Closes the session without saving any calibration changes |  |  |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration_1ga516c3e41ce8aedab15d5db3110c23427.html language=enus -->
## TOPIC 00113: DAQmxFieldDAQSetCalTemp

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration_1ga516c3e41ce8aedab15d5db3110c23427.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration_1ga516c3e41ce8aedab15d5db3110c23427.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxFieldDAQSetCalTemp(CalHandle calHandle, float64 temperature)RemarksSpecifies the temperature of a FieldDAQ device for the current external calibration session.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created

### DAQmxFieldDAQSetCalTemp

#### Syntax

int32 __CFUNC DAQmxFieldDAQSetCalTemp(CalHandle calHandle, float64 temperature)

#### Remarks

Specifies the temperature of a FieldDAQ device for the current external calibration session.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| temperature | [in] | float64 | The temperature of the device, in degrees Celsius. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

FieldDAQ Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__adjust__fielddaq__calibration.html language=enus -->
## TOPIC 00114: Adjust FieldDAQ Calibration

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__adjust__fielddaq__calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__adjust__fielddaq__calibration.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxAdjust11601CalDAQmxAdjust11603CalDAQmxAdjust11605CalDAQmxAdjust11613CalDAQmxAdjust11614CalDAQmxAdjust11634CalDAQmxAdjust11637CalAttachmentsNone

### Adjust FieldDAQ Calibration

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxAdjust11601Cal |  |
| DAQmxAdjust11603Cal |  |
| DAQmxAdjust11605Cal |  |
| DAQmxAdjust11613Cal |  |
| DAQmxAdjust11614Cal |  |
| DAQmxAdjust11634Cal |  |
| DAQmxAdjust11637Cal |  |

#### Attachments

None

Parent topic:

FieldDAQ Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__adjust__fielddaq__calibration_1ga2cd2da3e771e2e111ac957e8ee162ee3.html language=enus -->
## TOPIC 00115: DAQmxAdjust11603Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__adjust__fielddaq__calibration_1ga2cd2da3e771e2e111ac957e8ee162ee3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__adjust__fielddaq__calibration_1ga2cd2da3e771e2e111ac957e8ee162ee3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust11603Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for a FD-11603.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIn

### DAQmxAdjust11603Cal

#### Syntax

int32 __CFUNC DAQmxAdjust11603Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for a FD-11603.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust FieldDAQ Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__adjust__fielddaq__calibration_1ga578814bf452631251fddd524800cafaa.html language=enus -->
## TOPIC 00116: DAQmxAdjust11634Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__adjust__fielddaq__calibration_1ga578814bf452631251fddd524800cafaa.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__adjust__fielddaq__calibration_1ga578814bf452631251fddd524800cafaa.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust11634Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for a FD-11634.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIn

### DAQmxAdjust11634Cal

#### Syntax

int32 __CFUNC DAQmxAdjust11634Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for a FD-11634.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust FieldDAQ Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__get__fie5d8b72fdbee7a78eda5fc1ad755e47c4_1ga0fafad0bd2b33cfcc583b46bf2b9725f.html language=enus -->
## TOPIC 00117: DAQmxGet11613CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__get__fie5d8b72fdbee7a78eda5fc1ad755e47c4_1ga0fafad0bd2b33cfcc583b46bf2b9725f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__get__fie5d8b72fdbee7a78eda5fc1ad755e47c4_1ga0fafad0bd2b33cfcc583b46bf2b9725f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet11613CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the

### DAQmxGet11613CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet11613CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get FieldDAQ Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__get__fie5d8b72fdbee7a78eda5fc1ad755e47c4_1ga1ac3d5f657db38009854a0104a6948fc.html language=enus -->
## TOPIC 00118: DAQmxGet11601CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__get__fie5d8b72fdbee7a78eda5fc1ad755e47c4_1ga1ac3d5f657db38009854a0104a6948fc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__get__fie5d8b72fdbee7a78eda5fc1ad755e47c4_1ga1ac3d5f657db38009854a0104a6948fc.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet11601CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the

### DAQmxGet11601CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet11601CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get FieldDAQ Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__get__fie5d8b72fdbee7a78eda5fc1ad755e47c4_1ga6450a67dd03bfa979396c020e7b50132.html language=enus -->
## TOPIC 00119: DAQmxGet11603CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__get__fie5d8b72fdbee7a78eda5fc1ad755e47c4_1ga6450a67dd03bfa979396c020e7b50132.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__get__fie5d8b72fdbee7a78eda5fc1ad755e47c4_1ga6450a67dd03bfa979396c020e7b50132.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet11603CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the

### DAQmxGet11603CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet11603CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get FieldDAQ Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__setup__fielddaq__calibration.html language=enus -->
## TOPIC 00120: Setup FieldDAQ Calibration

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__setup__fielddaq__calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__setup__fielddaq__calibration.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxSetup11605CalDAQmxSetup11634CalDAQmxSetup11637CalAttachmentsNone

### Setup FieldDAQ Calibration

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxSetup11605Cal |  |
| DAQmxSetup11634Cal |  |
| DAQmxSetup11637Cal |  |

#### Attachments

None

Parent topic:

FieldDAQ Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__setup__fielddaq__calibration_1ga0da5326cdb22100701bcfd3c9df4248a.html language=enus -->
## TOPIC 00121: DAQmxSetup11637Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__setup__fielddaq__calibration_1ga0da5326cdb22100701bcfd3c9df4248a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__setup__fielddaq__calibration_1ga0da5326cdb22100701bcfd3c9df4248a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup11637Cal(CalHandle calHandle, const char channelNames[], int32 bridgeConfig, float64 voltageExcitation)RemarksSets up external calibration of a single channel for a FD-11637 device.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibratio

### DAQmxSetup11637Cal

#### Syntax

int32 __CFUNC DAQmxSetup11637Cal(CalHandle calHandle, const char channelNames[], int32 bridgeConfig, float64 voltageExcitation)

#### Remarks

Sets up external calibration of a single channel for a FD-11637 device.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| bridgeConfig | [in] | int32 | The type of Wheatstone bridge the sensor is. ValueDescriptionDAQmx_Val_FullBridgeSensor is a full bridge. If you set useExcitForScaling to TRUE, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation.DAQmx_Val_HalfBridgeSensor is a half bridge. If you set useExcitForScaling to TRUE, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation.DAQmx_Val_QuarterBridgeSensor is a quarter bridge. If you set useExcitForScaling to TRUE, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation.DAQmx_Val_NoBridgeSensor is not a Wheatstone bridge. |
| Value | Description |  |  |
| DAQmx_Val_FullBridge | Sensor is a full bridge. If you set useExcitForScaling to TRUE, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation. |  |  |
| DAQmx_Val_HalfBridge | Sensor is a half bridge. If you set useExcitForScaling to TRUE, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation. |  |  |
| DAQmx_Val_QuarterBridge | Sensor is a quarter bridge. If you set useExcitForScaling to TRUE, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation. |  |  |
| DAQmx_Val_NoBridge | Sensor is not a Wheatstone bridge. |  |  |
| voltageExcitation | [in] | float64 | Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Setup FieldDAQ Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__setup__fielddaq__calibration_1ga26c937aa8ca3aeefd49740d0377ec000.html language=enus -->
## TOPIC 00122: DAQmxSetup11605Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__setup__fielddaq__calibration_1ga26c937aa8ca3aeefd49740d0377ec000.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__fielddaq__calibration__setup__fielddaq__calibration_1ga26c937aa8ca3aeefd49740d0377ec000.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup11605Cal(CalHandle calHandle, float64 rangeMin, float64 rangeMax)RemarksInitializes the NI FD-11605 device with the specified range. Refer to the calibration procedure for your device for specific calibration instructions.ParametersNameDirectionTypeDescriptioncalHandle[

### DAQmxSetup11605Cal

#### Syntax

int32 __CFUNC DAQmxSetup11605Cal(CalHandle calHandle, float64 rangeMin, float64 rangeMax)

#### Remarks

Initializes the NI FD-11605 device with the specified range. Refer to the calibration procedure for your device for specific calibration instructions.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| rangeMin | [in] | float64 | The minimum value in the range. |
| rangeMax | [in] | float64 | The maximum value in the range. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Setup FieldDAQ Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__pxi-42xx__calibration_1ga8097ad77192757ede7ee4b9a16c285ad.html language=enus -->
## TOPIC 00123: DAQmxAdjust4204Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__pxi-42xx__calibration_1ga8097ad77192757ede7ee4b9a16c285ad.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__pxi-42xx__calibration_1ga8097ad77192757ede7ee4b9a16c285ad.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust4204Cal(CalHandle calHandle, const char channelNames[], float64 lowPassFreq, bool32 trackHoldEnabled, float64 inputVal)RemarksAdjusts the internal and external calibration constants for the SCMP pod on the PXI-4204 device. You must supply a known voltage to the device

### DAQmxAdjust4204Cal

#### Syntax

int32 __CFUNC DAQmxAdjust4204Cal(CalHandle calHandle, const char channelNames[], float64 lowPassFreq, bool32 trackHoldEnabled, float64 inputVal)

#### Remarks

Adjusts the internal and external calibration constants for the SCMP pod on the PXI-4204 device. You must supply a known voltage to the device and specify that voltage with inputVal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| lowPassFreq | [in] | float64 | The low pass cutoff frequency, in hertz, (6 or 10000) on the SCMP pod to calibrate. |
| trackHoldEnabled | [in] | bool32 | Specifies whether calibrating for trackHold is enabled or disabled. |
| inputVal | [in] | float64 | The known voltage, in volts, to use as a reference for calibration. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

PXI-42xx Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__pxi-42xx__calibration_1gadf21be6c123aca91c5cd53e5c25fac8f.html language=enus -->
## TOPIC 00124: DAQmxAdjust4220Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__pxi-42xx__calibration_1gadf21be6c123aca91c5cd53e5c25fac8f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__pxi-42xx__calibration_1gadf21be6c123aca91c5cd53e5c25fac8f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust4220Cal(CalHandle calHandle, const char channelNames[], float64 gain, float64 inputVal)RemarksAdjusts the internal and external calibration constants for the SCMP pod on the PXI-4220 device. You must supply a known voltage to the device and specify that voltage with in

### DAQmxAdjust4220Cal

#### Syntax

int32 __CFUNC DAQmxAdjust4220Cal(CalHandle calHandle, const char channelNames[], float64 gain, float64 inputVal)

#### Remarks

Adjusts the internal and external calibration constants for the SCMP pod on the PXI-4220 device. You must supply a known voltage to the device and specify that voltage with inputVal. This device needs reference signals of 0.0 volts at gains of 1, 15, 20, and 310 on a particular channel in order to perform an offset calibration for that channel. If those points are not manually supplied, they will be automatically measured internally with sample and hold enabled.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| gain | [in] | float64 | The gain value on the SCMP pod to calibrate. |
| inputVal | [in] | float64 | The known voltage, in volts, to use as a reference for calibration. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

PXI-42xx Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__pxi-42xx__calibration_1gafdcf3477817de4c9b50afa522df842c3.html language=enus -->
## TOPIC 00125: DAQmxAdjust4224Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__pxi-42xx__calibration_1gafdcf3477817de4c9b50afa522df842c3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__pxi-42xx__calibration_1gafdcf3477817de4c9b50afa522df842c3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust4224Cal(CalHandle calHandle, const char channelNames[], float64 gain, float64 inputVal)RemarksAdjusts the internal and external calibration constants for the SCMP pod on the PXI-4224 device. You must supply a known voltage to the device and specify that voltage with in

### DAQmxAdjust4224Cal

#### Syntax

int32 __CFUNC DAQmxAdjust4224Cal(CalHandle calHandle, const char channelNames[], float64 gain, float64 inputVal)

#### Remarks

Adjusts the internal and external calibration constants for the SCMP pod on the PXI-4224 device. You must supply a known voltage to the device and specify that voltage with inputVal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| gain | [in] | float64 | The gain value on the SCMP pod to calibrate. |
| inputVal | [in] | float64 | The known voltage, in volts, to use as a reference for calibration. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

PXI-42xx Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration.html language=enus -->
## TOPIC 00126: SC Express Calibration

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxAdjust4300CalDAQmxAdjust4302CalDAQmxAdjust4303CalDAQmxAdjust4304CalDAQmxAdjust4305CalDAQmxAdjust4309CalDAQmxAdjust4310CalDAQmxAdjust4311CalDAQmxAdjust4322CalDAQmxAdjust4339CalDAQmxAdjust433xCalDAQmxAdjust4353CalDAQmxAdjust4357CalDAQmxConnectSCExpressCalAccC

### SC Express Calibration

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxAdjust4300Cal |  |
| DAQmxAdjust4302Cal |  |
| DAQmxAdjust4303Cal |  |
| DAQmxAdjust4304Cal |  |
| DAQmxAdjust4305Cal |  |
| DAQmxAdjust4309Cal |  |
| DAQmxAdjust4310Cal |  |
| DAQmxAdjust4311Cal |  |
| DAQmxAdjust4322Cal |  |
| DAQmxAdjust4339Cal |  |
| DAQmxAdjust433xCal |  |
| DAQmxAdjust4353Cal |  |
| DAQmxAdjust4357Cal |  |
| DAQmxConnectSCExpressCalAccChans |  |
| DAQmxDisconnectSCExpressCalAccChans |  |
| DAQmxGet4302CalAdjustPoints |  |
| DAQmxGet4303CalAdjustPoints |  |
| DAQmxGet4304CalAdjustPoints |  |
| DAQmxGet4305CalAdjustPoints |  |
| DAQmxGet4322CalAdjustPoints |  |
| DAQmxGet4339CalAdjustPoints |  |
| DAQmxGetPossibleSCExpressCalAccConnections |  |
| DAQmxSetSCExpressCalAccBridgeOutput |  |
| DAQmxSetup4302Cal |  |
| DAQmxSetup4303Cal |  |
| DAQmxSetup4304Cal |  |
| DAQmxSetup4305Cal |  |
| DAQmxSetup4322Cal |  |
| DAQmxSetup4339Cal |  |
| DAQmxSetup433xCal |  |

#### Attachments

None

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga130f97d3adf29fe3afff754c57fdee5c.html language=enus -->
## TOPIC 00127: DAQmxSetup433xCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga130f97d3adf29fe3afff754c57fdee5c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga130f97d3adf29fe3afff754c57fdee5c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup433xCal(CalHandle calHandle, const char channelNames[], float64 excitationVoltage)RemarksInitializes an NI PXIe-433x device with the specified excitation voltage value for calibration.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibra

### DAQmxSetup433xCal

#### Syntax

int32 __CFUNC DAQmxSetup433xCal(CalHandle calHandle, const char channelNames[], float64 excitationVoltage)

#### Remarks

Initializes an NI PXIe-433x device with the specified excitation voltage value for calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| excitationVoltage | [in] | float64 | The excitation voltage setting to calibrate. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga1796d4aac6a7b700ed2cf1fdbac581b4.html language=enus -->
## TOPIC 00128: DAQmxAdjust4300Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga1796d4aac6a7b700ed2cf1fdbac581b4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga1796d4aac6a7b700ed2cf1fdbac581b4.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust4300Cal(CalHandle calHandle, float64 refVoltage)RemarksAdjusts the external calibration constants for an NI PXIe-4300. You must connect a known voltage to the device and specify that voltage with refVoltage.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA

### DAQmxAdjust4300Cal

#### Syntax

int32 __CFUNC DAQmxAdjust4300Cal(CalHandle calHandle, float64 refVoltage)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4300. You must connect a known voltage to the device and specify that voltage with **refVoltage**.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| refVoltage | [in] | float64 | Specifies in volts the known voltage to use as a reference for calibration. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga42301345c7b2b1addc3f88c8a10cef42.html language=enus -->
## TOPIC 00129: DAQmxAdjust4309Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga42301345c7b2b1addc3f88c8a10cef42.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga42301345c7b2b1addc3f88c8a10cef42.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust4309Cal(CalHandle calHandle, float64 refVoltage)RemarksAdjusts the external calibration constants for an NI PXIe-4309.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxInitExtCal function.

### DAQmxAdjust4309Cal

#### Syntax

int32 __CFUNC DAQmxAdjust4309Cal(CalHandle calHandle, float64 refVoltage)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4309.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| refVoltage | [in] | float64 | Specifies the reference value collected when verifying the calibration. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga51129c249477e27b9f6e4a6d6b5927f1.html language=enus -->
## TOPIC 00130: DAQmxSetup4303Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga51129c249477e27b9f6e4a6d6b5927f1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga51129c249477e27b9f6e4a6d6b5927f1.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup4303Cal(CalHandle calHandle, const char channelNames[], float64 rangeMin, float64 rangeMax)RemarksInitializes an NI PXIe-4303 device with the specified range for calibration.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration sessi

### DAQmxSetup4303Cal

#### Syntax

int32 __CFUNC DAQmxSetup4303Cal(CalHandle calHandle, const char channelNames[], float64 rangeMin, float64 rangeMax)

#### Remarks

Initializes an NI PXIe-4303 device with the specified range for calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| rangeMax | [in] | float64 | The maximum value in the range. |
| rangeMin | [in] | float64 | The minimum value in the range. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga560e57941b99ab85cf7302e49d6e7b9d.html language=enus -->
## TOPIC 00131: DAQmxGet4303CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga560e57941b99ab85cf7302e49d6e7b9d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga560e57941b99ab85cf7302e49d6e7b9d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet4303CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the c

### DAQmxGet4303CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet4303CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |
| adjustmentPoints | [out] | float64 * | The adjustment points returned by this function. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga5b4595475079c672e67a0c1e62e6bf2e.html language=enus -->
## TOPIC 00132: DAQmxGet4304CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga5b4595475079c672e67a0c1e62e6bf2e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga5b4595475079c672e67a0c1e62e6bf2e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet4304CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the c

### DAQmxGet4304CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet4304CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |
| adjustmentPoints | [out] | float64 * | The adjustment points returned by this function. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga64c39546b3cdd2ebfc3428454a52e975.html language=enus -->
## TOPIC 00133: DAQmxGet4305CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga64c39546b3cdd2ebfc3428454a52e975.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga64c39546b3cdd2ebfc3428454a52e975.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet4305CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the c

### DAQmxGet4305CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet4305CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |
| adjustmentPoints | [out] | float64 * | The adjustment points returned by this function. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga65aa49c3e19aa437bece3987de127e75.html language=enus -->
## TOPIC 00134: DAQmxConnectSCExpressCalAccChans

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga65aa49c3e19aa437bece3987de127e75.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga65aa49c3e19aa437bece3987de127e75.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxConnectSCExpressCalAccChans(CalHandle calHandle, const char channelNames[], const char connection[])RemarksConfigures a connection on the SC Express accessory for the specified physical channel(s).ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the

### DAQmxConnectSCExpressCalAccChans

#### Syntax

int32 __CFUNC DAQmxConnectSCExpressCalAccChans(CalHandle calHandle, const char channelNames[], const char connection[])

#### Remarks

Configures a connection on the SC Express accessory for the specified physical channel(s).

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| connection | [in] | const char[] | Specifies how channels on the SC Express accessory should be configured. The resulting configuration could connect channels to a particular external signal or some onboard terminal. The supported connections depend on the accessory. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga67fcb256f2495236d0fb3a3211c5edaf.html language=enus -->
## TOPIC 00135: DAQmxAdjust4310Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga67fcb256f2495236d0fb3a3211c5edaf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga67fcb256f2495236d0fb3a3211c5edaf.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust4310Cal(CalHandle calHandle, float64 refVoltage)RemarksAdjusts the external calibration constants for an NI PXIe-4310.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxInitExtCal function.

### DAQmxAdjust4310Cal

#### Syntax

int32 __CFUNC DAQmxAdjust4310Cal(CalHandle calHandle, float64 refVoltage)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4310.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| refVoltage | [in] | float64 | Specifies the reference value collected when verifying the calibration. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga76316853a12350f2128c68913fe1361a.html language=enus -->
## TOPIC 00136: DAQmxAdjust4302Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga76316853a12350f2128c68913fe1361a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga76316853a12350f2128c68913fe1361a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust4302Cal(CalHandle calHandle, float64 refVoltage)RemarksAdjusts the external calibration constants for an NI 4302. You must connect a known voltage to the device and specify that voltage with refVoltage.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA refer

### DAQmxAdjust4302Cal

#### Syntax

int32 __CFUNC DAQmxAdjust4302Cal(CalHandle calHandle, float64 refVoltage)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 4302. You must connect a known voltage to the device and specify that voltage with **refVoltage**.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| refVoltage | [in] | float64 | Specifies in volts the known voltage to use as a reference for calibration. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga79c87ab9b4d695c5ce8a123649434c70.html language=enus -->
## TOPIC 00137: DAQmxSetup4339Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga79c87ab9b4d695c5ce8a123649434c70.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga79c87ab9b4d695c5ce8a123649434c70.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup4339Cal(CalHandle calHandle, const char channelNames[], int32 calMode, float64 rangeMax, float64 rangeMin, float64 excitationVoltage)RemarksInitializes an NI PXIe-4339 device with the specified mode, range, and excitation for calibration.ParametersNameDirectionTypeDescr

### DAQmxSetup4339Cal

#### Syntax

int32 __CFUNC DAQmxSetup4339Cal(CalHandle calHandle, const char channelNames[], int32 calMode, float64 rangeMax, float64 rangeMin, float64 excitationVoltage)

#### Remarks

Initializes an NI PXIe-4339 device with the specified mode, range, and excitation for calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| calMode | [in] | int32 | The calibration mode for the device. ValueDescriptionDAQmx_Val_VoltageVoltage modeDAQmx_Val_BridgeRatiometric mode (V/V) |
| Value | Description |  |  |
| DAQmx_Val_Voltage | Voltage mode |  |  |
| DAQmx_Val_Bridge | Ratiometric mode (V/V) |  |  |
| rangeMax | [in] | float64 | The maximum value in the range. |
| rangeMin | [in] | float64 | The minimum value in the range. |
| excitationVoltage | [in] | float64 | The excitation voltage setting to calibrate. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga852680ce66faa3e513a95a0ebdc4ee4b.html language=enus -->
## TOPIC 00138: DAQmxAdjust4357Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga852680ce66faa3e513a95a0ebdc4ee4b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga852680ce66faa3e513a95a0ebdc4ee4b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust4357Cal(CalHandle calHandle, const char channelNames[], const float64 refVals[], int32 numRefVals)RemarksAdjusts the external calibration constants for an NI PXIe-4357. Refer to the calibration procedure for your device for specific calibration instructions.ParametersN

### DAQmxAdjust4357Cal

#### Syntax

int32 __CFUNC DAQmxAdjust4357Cal(CalHandle calHandle, const char channelNames[], const float64 refVals[], int32 numRefVals)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4357. Refer to the calibration procedure for your device for specific calibration instructions.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| refVals | [in] | const float64[] | Specifies the reference value of each physical channel measured using a calibrator. |
| numRefVals | [in] | int32 | Specifies the number of reference values to use for calibration. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga88864edcb2ff2baf7fb855ad15c719fc.html language=enus -->
## TOPIC 00139: DAQmxGet4339CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga88864edcb2ff2baf7fb855ad15c719fc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1ga88864edcb2ff2baf7fb855ad15c719fc.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet4339CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference voltage values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the c

### DAQmxGet4339CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet4339CalAdjustPoints(CalHandle calHandle, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference voltage values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |
| adjustmentPoints | [out] | float64 * | The adjustment points returned by this function. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gaa58beae9dab27f0b37d32203e450180f.html language=enus -->
## TOPIC 00140: DAQmxDisconnectSCExpressCalAccChans

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gaa58beae9dab27f0b37d32203e450180f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gaa58beae9dab27f0b37d32203e450180f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxDisconnectSCExpressCalAccChans(CalHandle calHandle)RemarksDisconnects the configured connection on an SC Express accessory and connects the accessory in the default configuration.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration sessi

### DAQmxDisconnectSCExpressCalAccChans

#### Syntax

int32 __CFUNC DAQmxDisconnectSCExpressCalAccChans(CalHandle calHandle)

#### Remarks

Disconnects the configured connection on an SC Express accessory and connects the accessory in the default configuration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gaa911548731544f3f670d8452934a30ea.html language=enus -->
## TOPIC 00141: DAQmxAdjust4322Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gaa911548731544f3f670d8452934a30ea.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gaa911548731544f3f670d8452934a30ea.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust4322Cal(CalHandle calHandle, const char channelNames[], float64 refVal)RemarksAdjusts the external calibration constants for an NI PXIe-4322.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DA

### DAQmxAdjust4322Cal

#### Syntax

int32 __CFUNC DAQmxAdjust4322Cal(CalHandle calHandle, const char channelNames[], float64 refVal)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4322.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to use. |
| refVal | [in] | float64 | Specifies the reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gab8f7867d660c7388cde85297ef54e64e.html language=enus -->
## TOPIC 00142: DAQmxAdjust433xCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gab8f7867d660c7388cde85297ef54e64e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gab8f7867d660c7388cde85297ef54e64e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust433xCal(CalHandle calHandle, float64 refVoltage, float64 refExcitation, int32 shuntLocation)RemarksAdjusts the external calibration constants for an NI PXIe-433x device.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session t

### DAQmxAdjust433xCal

#### Syntax

int32 __CFUNC DAQmxAdjust433xCal(CalHandle calHandle, float64 refVoltage, float64 refExcitation, int32 shuntLocation)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-433x device.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| refVoltage | [in] | float64 | The voltage across the AI+ and AI- terminals, measured using a DMM. |
| refExcitation | [in] | float64 | The voltage across the EX+ and EX- terminals, measured using a second DMM. |
| shuntLocation | [in] | int32 | The resistive leg of the Wheatstone bridge that has an external shunt resistor connected in parallel. ValueDescriptionDAQmx_Val_R3R3DAQmx_Val_R4R4DAQmx_Val_NoneNo shunt resistor connected |
| Value | Description |  |  |
| DAQmx_Val_R3 | R3 |  |  |
| DAQmx_Val_R4 | R4 |  |  |
| DAQmx_Val_None | No shunt resistor connected |  |  |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gad84126437a0b2000e9cbcd07895c28cf.html language=enus -->
## TOPIC 00143: DAQmxSetup4304Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gad84126437a0b2000e9cbcd07895c28cf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gad84126437a0b2000e9cbcd07895c28cf.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup4304Cal(CalHandle calHandle, const char channelNames[], float64 rangeMin, float64 rangeMax)RemarksInitializes an NI PXIe-4304 device with the specified range for calibration.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration sessi

### DAQmxSetup4304Cal

#### Syntax

int32 __CFUNC DAQmxSetup4304Cal(CalHandle calHandle, const char channelNames[], float64 rangeMin, float64 rangeMax)

#### Remarks

Initializes an NI PXIe-4304 device with the specified range for calibration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| rangeMax | [in] | float64 | The maximum value in the range. |
| rangeMin | [in] | float64 | The minimum value in the range. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gadea331a74532d6af6a2e9963d6739a59.html language=enus -->
## TOPIC 00144: DAQmxGetPossibleSCExpressCalAccConnections

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gadea331a74532d6af6a2e9963d6739a59.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gadea331a74532d6af6a2e9963d6739a59.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetPossibleSCExpressCalAccConnections(const char deviceName[], const char channelNames[], char *connections, uInt32 connectionsBufferSize)RemarksGets the available connections on an SC Express accessory for the specified physical channel(s). Connections specify how channels

### DAQmxGetPossibleSCExpressCalAccConnections

#### Syntax

int32 __CFUNC DAQmxGetPossibleSCExpressCalAccConnections(const char deviceName[], const char channelNames[], char *connections, uInt32 connectionsBufferSize)

#### Remarks

Gets the available connections on an SC Express accessory for the specified physical channel(s). Connections specify how channels on the SC Express accessory should be configured. The resulting configuration could connect channels to a particular external signal or an onboard terminal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| deviceName | [in] | const char[] | Specifies the name to assign to the device. If unspecified, NI-DAQmx chooses the device name. |
| channelNames | [in] | const char[] | The physical channel(s) to use. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gaec9f3ad96317e6f371caf5b93e1fd598.html language=enus -->
## TOPIC 00145: DAQmxSetup4322Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gaec9f3ad96317e6f371caf5b93e1fd598.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__sc__express__calibration_1gaec9f3ad96317e6f371caf5b93e1fd598.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup4322Cal(CalHandle calHandle, const char channelNames[], int32 outputType, float64 outputVal)RemarksWrites the specified value to the DAC on the specified physical channel(s) for an NI PXIe-4322. This device requires a sweep of values obtained from the calibration proced

### DAQmxSetup4322Cal

#### Syntax

int32 __CFUNC DAQmxSetup4322Cal(CalHandle calHandle, const char channelNames[], int32 outputType, float64 outputVal)

#### Remarks

Writes the specified value to the DAC on the specified physical channel(s) for an NI PXIe-4322. This device requires a sweep of values obtained from the calibration procedure.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| outputType | [in] | int32 | Specifies the output type of the measurement for the device. ValueDescriptionDAQmx_Val_VoltageVoltage generationDAQmx_Val_CurrentCurrent generation |
| Value | Description |  |  |
| DAQmx_Val_Voltage | Voltage generation |  |  |
| DAQmx_Val_Current | Current generation |  |  |
| outputVal | [in] | float64 | Specifies, in the units of outputType, the value to write to the physical channel. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration.html language=enus -->
## TOPIC 00146: SCXI Calibration

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxAdjust1102CalDAQmxAdjust1104CalDAQmxAdjust1112CalDAQmxAdjust1122CalDAQmxAdjust1124CalDAQmxAdjust1125CalDAQmxAdjust1126CalDAQmxAdjust1141CalDAQmxAdjust1142CalDAQmxAdjust1143CalDAQmxAdjust1502CalDAQmxAdjust1503CalDAQmxAdjust1503CurrentCalDAQmxAdjust1520CalDAQ

### SCXI Calibration

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxAdjust1102Cal |  |
| DAQmxAdjust1104Cal |  |
| DAQmxAdjust1112Cal |  |
| DAQmxAdjust1122Cal |  |
| DAQmxAdjust1124Cal |  |
| DAQmxAdjust1125Cal |  |
| DAQmxAdjust1126Cal |  |
| DAQmxAdjust1141Cal |  |
| DAQmxAdjust1142Cal |  |
| DAQmxAdjust1143Cal |  |
| DAQmxAdjust1502Cal |  |
| DAQmxAdjust1503Cal |  |
| DAQmxAdjust1503CurrentCal |  |
| DAQmxAdjust1520Cal |  |
| DAQmxAdjust1521Cal |  |
| DAQmxAdjust153xCal |  |
| DAQmxAdjust1540Cal |  |
| DAQmxSetup1102Cal |  |
| DAQmxSetup1104Cal |  |
| DAQmxSetup1112Cal |  |
| DAQmxSetup1122Cal |  |
| DAQmxSetup1124Cal |  |
| DAQmxSetup1125Cal |  |
| DAQmxSetup1126Cal |  |
| DAQmxSetup1141Cal |  |
| DAQmxSetup1142Cal |  |
| DAQmxSetup1143Cal |  |
| DAQmxSetup1502Cal |  |
| DAQmxSetup1503Cal |  |
| DAQmxSetup1520Cal |  |
| DAQmxSetup1521Cal |  |
| DAQmxSetup153xCal |  |
| DAQmxSetup1540Cal |  |

#### Attachments

None

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga007d6244ce117bf6390e9fdb0af5a5a9.html language=enus -->
## TOPIC 00147: DAQmxSetup1502Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga007d6244ce117bf6390e9fdb0af5a5a9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga007d6244ce117bf6390e9fdb0af5a5a9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup1502Cal(CalHandle calHandle, const char channelName[], float64 gain)RemarksSets the SCXI-1502 module to the specified gain value. Calibration I/O points can be measured by supplying reference signals to the specified channel and measuring the outputs. Specify each of th

### DAQmxSetup1502Cal

#### Syntax

int32 __CFUNC DAQmxSetup1502Cal(CalHandle calHandle, const char channelName[], float64 gain)

#### Remarks

Sets the SCXI-1502 module to the specified gain value. Calibration I/O points can be measured by supplying reference signals to the specified channel and measuring the outputs. Specify each of these points using the DAQmxAdjust1502Cal function.

Note

The terminal where the module output is measured depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the module user manual for more information on the routing of module output.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelName | [in] | const char[] | The physical channel to calibrate. |
| gain | [in] | float64 | The gain value to calibrate. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SCXI Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga08e4f3219cfd4ef4163692c60a9a9799.html language=enus -->
## TOPIC 00148: DAQmxSetup1112Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga08e4f3219cfd4ef4163692c60a9a9799.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga08e4f3219cfd4ef4163692c60a9a9799.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup1112Cal(CalHandle calHandle, const char channelName[])RemarksSpecifies the channel on the SCXI-1112 module for calibration. Measure calibration input/output points by supplying reference signals to the specified channel and measuring the outputs. Specify each of these p

### DAQmxSetup1112Cal

#### Syntax

int32 __CFUNC DAQmxSetup1112Cal(CalHandle calHandle, const char channelName[])

#### Remarks

Specifies the channel on the SCXI-1112 module for calibration. Measure calibration input/output points by supplying reference signals to the specified channel and measuring the outputs. Specify each of these points using the DAQmxAdjust1112Cal function.

Note

The terminal where module output is measured depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0+/- pins of the rear signal connector. Refer to the module user manual for more information on the routing of module output.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelName | [in] | const char[] | The physical channel to calibrate. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SCXI Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga10715071b99fcb3f9b0e89eb56da43e6.html language=enus -->
## TOPIC 00149: DAQmxAdjust1141Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga10715071b99fcb3f9b0e89eb56da43e6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga10715071b99fcb3f9b0e89eb56da43e6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust1141Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)RemarksAdjusts the external calibration constants for the SCXI-1141 module. You must supply a known voltage to the device and specify that voltage with refVoltage.ParametersNameDirectionTypeDescription

### DAQmxAdjust1141Cal

#### Syntax

int32 __CFUNC DAQmxAdjust1141Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)

#### Remarks

Adjusts the external calibration constants for the SCXI-1141 module. You must supply a known voltage to the device and specify that voltage with refVoltage.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| refVoltage | [in] | float64 | The known voltage, in volts, to use as a reference for calibration. |
| measOutput | [in] | float64 | The voltage measured at the output of the module. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SCXI Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga1d718a97be4776db7fc29350b46842bc.html language=enus -->
## TOPIC 00150: DAQmxAdjust1126Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga1d718a97be4776db7fc29350b46842bc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga1d718a97be4776db7fc29350b46842bc.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust1126Cal(CalHandle calHandle, float64 refFreq, float64 measOutput)RemarksAdjusts the calibration constants for the SCXI-1126 module. You must measure the voltage generated by a previous call to the DAQmxSetup1126Cal function and specify the measurement with measOutput.P

### DAQmxAdjust1126Cal

#### Syntax

int32 __CFUNC DAQmxAdjust1126Cal(CalHandle calHandle, float64 refFreq, float64 measOutput)

#### Remarks

Adjusts the calibration constants for the SCXI-1126 module. You must measure the voltage generated by a previous call to the DAQmxSetup1126Cal function and specify the measurement with measOutput.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| refFreq | [in] | float64 | The known frequency, in hertz, to use as a reference for calibration. |
| measOutput | [in] | float64 | The voltage measured at the output of the module. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SCXI Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga4947a58772bd5d7364b40d6fa9356656.html language=enus -->
## TOPIC 00151: DAQmxAdjust1503Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga4947a58772bd5d7364b40d6fa9356656.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga4947a58772bd5d7364b40d6fa9356656.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust1503Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)RemarksAdjusts the calibration constants for the SCXI-1503 module. You must supply a known voltage to the device and specify that voltage with refVoltage.ParametersNameDirectionTypeDescriptioncalHandle

### DAQmxAdjust1503Cal

#### Syntax

int32 __CFUNC DAQmxAdjust1503Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)

#### Remarks

Adjusts the calibration constants for the SCXI-1503 module. You must supply a known voltage to the device and specify that voltage with refVoltage.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| refVoltage | [in] | float64 | The known voltage, in volts, to use as a reference for calibration. |
| measOutput | [in] | float64 | The voltage measured at the output of the module. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SCXI Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga60e857a0adf67436f413df245afc3dfd.html language=enus -->
## TOPIC 00152: DAQmxSetup1142Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga60e857a0adf67436f413df245afc3dfd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga60e857a0adf67436f413df245afc3dfd.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup1142Cal(CalHandle calHandle, const char channelName[], float64 gain)RemarksSets the SCXI-1142 module to the specified gain value. Calibration input/output points can be measured by supplying reference signals to the specified channel and measuring the outputs. Each of t

### DAQmxSetup1142Cal

#### Syntax

int32 __CFUNC DAQmxSetup1142Cal(CalHandle calHandle, const char channelName[], float64 gain)

#### Remarks

Sets the SCXI-1142 module to the specified gain value. Calibration input/output points can be measured by supplying reference signals to the specified channel and measuring the outputs. Each of these points should be specified using the DAQmxAdjust1142Cal function.

Note

The terminal where the module output is measured depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the module user manual for more information on the routing of module output.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelName | [in] | const char[] | The physical channel to calibrate. |
| gain | [in] | float64 | The gain value to calibrate. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SCXI Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga6105ff59e8122eff0cd3dffc2ec78dcf.html language=enus -->
## TOPIC 00153: DAQmxAdjust1112Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga6105ff59e8122eff0cd3dffc2ec78dcf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga6105ff59e8122eff0cd3dffc2ec78dcf.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust1112Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)RemarksAdjusts the calibration constants for the SCXI-1112 module. You must measure the voltage generated by a previous call to the DAQmxSetup1112Cal function and specify the measurement with measOutpu

### DAQmxAdjust1112Cal

#### Syntax

int32 __CFUNC DAQmxAdjust1112Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)

#### Remarks

Adjusts the calibration constants for the SCXI-1112 module. You must measure the voltage generated by a previous call to the DAQmxSetup1112Cal function and specify the measurement with measOutput.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| refVoltage | [in] | float64 | The known voltage, in volts, to use as a reference for calibration. |
| measOutput | [in] | float64 | The voltage measured at the output of the module. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SCXI Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga6896034318b7707ec2892d3bf21b2ece.html language=enus -->
## TOPIC 00154: DAQmxAdjust1520Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga6896034318b7707ec2892d3bf21b2ece.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga6896034318b7707ec2892d3bf21b2ece.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust1520Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)RemarksAdjusts the external calibration constants for the SCXI-1520 module. You must supply a known voltage to the device and specify that voltage with refVoltage. This device needs reference signals o

### DAQmxAdjust1520Cal

#### Syntax

int32 __CFUNC DAQmxAdjust1520Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)

#### Remarks

Adjusts the external calibration constants for the SCXI-1520 module. You must supply a known voltage to the device and specify that voltage with refVoltage. This device needs reference signals of 0.0 volts at gains of 1, 15, 20, and 310 on a particular channel in order to perform an offset calibration for that channel.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| refVoltage | [in] | float64 | The known voltage, in volts, to use as a reference for calibration. |
| measOutput | [in] | float64 | The voltage measured at the output of the module. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SCXI Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga7344a0472341406217830a70ce4faf6e.html language=enus -->
## TOPIC 00155: DAQmxSetup1521Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga7344a0472341406217830a70ce4faf6e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga7344a0472341406217830a70ce4faf6e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup1521Cal(CalHandle calHandle, const char channelName[])RemarksSpecifies the channel on the SCXI-1521 module for calibration. Calibration input/output points can be measured by supplying reference signals to the specified channel and measuring the outputs. Specify each of

### DAQmxSetup1521Cal

#### Syntax

int32 __CFUNC DAQmxSetup1521Cal(CalHandle calHandle, const char channelName[])

#### Remarks

Specifies the channel on the SCXI-1521 module for calibration. Calibration input/output points can be measured by supplying reference signals to the specified channel and measuring the outputs. Specify each of these points using the DAQmxAdjust1521Cal function.

Note

The terminal where module output is measured depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the module user manual for more information on the routing of module output.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelName | [in] | const char[] | The physical channel to calibrate. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SCXI Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga7360576a16998319d7687f2524fcbaa2.html language=enus -->
## TOPIC 00156: DAQmxSetup1503Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga7360576a16998319d7687f2524fcbaa2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga7360576a16998319d7687f2524fcbaa2.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup1503Cal(CalHandle calHandle, const char channelName[], float64 gain)RemarksSets the SCXI-1503 module to the specified gain value. Calibration I/O points can be measured by supplying reference signals to the specified channel and measuring the outputs. Specify each of th

### DAQmxSetup1503Cal

#### Syntax

int32 __CFUNC DAQmxSetup1503Cal(CalHandle calHandle, const char channelName[], float64 gain)

#### Remarks

Sets the SCXI-1503 module to the specified gain value. Calibration I/O points can be measured by supplying reference signals to the specified channel and measuring the outputs. Specify each of these points using the DAQmxAdjust1503Cal function.

Note

The terminal where the module output is measured depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the module user manual for more information on the routing of module output.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelName | [in] | const char[] | The physical channel to calibrate. |
| gain | [in] | float64 | The gain value to calibrate. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SCXI Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga7425d0de0ad41774c11d700ed0359990.html language=enus -->
## TOPIC 00157: DAQmxAdjust1102Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga7425d0de0ad41774c11d700ed0359990.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1ga7425d0de0ad41774c11d700ed0359990.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust1102Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)RemarksAdjusts the external calibration constants for the SCXI-1102 module. You must supply a known voltage to the device and specify that voltage with refVoltage.ParametersNameDirectionTypeDescription

### DAQmxAdjust1102Cal

#### Syntax

int32 __CFUNC DAQmxAdjust1102Cal(CalHandle calHandle, float64 refVoltage, float64 measOutput)

#### Remarks

Adjusts the external calibration constants for the SCXI-1102 module. You must supply a known voltage to the device and specify that voltage with refVoltage.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| refVoltage | [in] | float64 | The known voltage, in volts, to use as a reference for calibration. |
| measOutput | [in] | float64 | The voltage measured at the output of the module. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SCXI Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1gab45fffba0fa31d51540548fecb425fa6.html language=enus -->
## TOPIC 00158: DAQmxSetup1124Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1gab45fffba0fa31d51540548fecb425fa6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1gab45fffba0fa31d51540548fecb425fa6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup1124Cal(CalHandle calHandle, const char channelName[], int32 range, uInt32 dacValue)RemarksWrites the specified binary value to the D/A circuitry on the specified channel at the specified range. Measure and specify the voltage or current generated in a subsequent call t

### DAQmxSetup1124Cal

#### Syntax

int32 __CFUNC DAQmxSetup1124Cal(CalHandle calHandle, const char channelName[], int32 range, uInt32 dacValue)

#### Remarks

Writes the specified binary value to the D/A circuitry on the specified channel at the specified range. Measure and specify the voltage or current generated in a subsequent call to the DAQmxAdjust1124Cal function.

Note

Specify at least two calibration points for each channel/range being calibrated. The recommended binary data to use for voltage ranges are 0 and 4095. The recommended binary data to use for the current range is 255 and 4095.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelName | [in] | const char[] | The physical channel to calibrate. |
| range | [in] | int32 | The range to calibrate. |
| dacValue | [in] | uInt32 | The binary number to write to the DAC circuitry. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SCXI Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1gab77d05138806ebc1935ea8e7f44c0a07.html language=enus -->
## TOPIC 00159: DAQmxSetup1125Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1gab77d05138806ebc1935ea8e7f44c0a07.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1gab77d05138806ebc1935ea8e7f44c0a07.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup1125Cal(CalHandle calHandle, const char channelName[], float64 gain)RemarksSets the SCXI-1125 module to the specified gain value. Calibration input/output points can be measured by supplying reference signals to the specified channel and measuring the outputs. Each of t

### DAQmxSetup1125Cal

#### Syntax

int32 __CFUNC DAQmxSetup1125Cal(CalHandle calHandle, const char channelName[], float64 gain)

#### Remarks

Sets the SCXI-1125 module to the specified gain value. Calibration input/output points can be measured by supplying reference signals to the specified channel and measuring the outputs. Each of these points should be specified using the DAQmxAdjust1125Cal function.

Note

The terminal where module output is measured will depend on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0+/- pins of the rear signal connector. Please refer to the module user manual for more information on the routing of module output.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelName | [in] | const char[] | The physical channel(s) to calibrate. |
| gain | [in] | float64 | The gain value to calibrate. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SCXI Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1gac58c95cce14e9de121cb5f16ed6a22ae.html language=enus -->
## TOPIC 00160: DAQmxSetup1126Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1gac58c95cce14e9de121cb5f16ed6a22ae.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1gac58c95cce14e9de121cb5f16ed6a22ae.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup1126Cal(CalHandle calHandle, const char channelName[], float64 upperFreqLimit)RemarksSpecifies the channel and upper frequency limit on the SCXI-1126 module for calibration. Calibration input/output points can be measured by supplying reference signals to the specified

### DAQmxSetup1126Cal

#### Syntax

int32 __CFUNC DAQmxSetup1126Cal(CalHandle calHandle, const char channelName[], float64 upperFreqLimit)

#### Remarks

Specifies the channel and upper frequency limit on the SCXI-1126 module for calibration. Calibration input/output points can be measured by supplying reference signals to the specified channel and measuring the outputs. Specify each of these points using the DAQmxAdjust1126Cal function.

Note

The terminal where the module output is measured depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the module user manual for more information on the routing of module output.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelName | [in] | const char[] | The physical channel to calibrate. |
| upperFreqLimit | [in] | float64 | The high frequency limit in hertz, with 0 Hz as the low frequency limit, which most closely encapsulates the ranges to be calibrated. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SCXI Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1gac6ab3f2a3f1131197b6e981d5fd68cb1.html language=enus -->
## TOPIC 00161: DAQmxSetup1540Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1gac6ab3f2a3f1131197b6e981d5fd68cb1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1gac6ab3f2a3f1131197b6e981d5fd68cb1.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup1540Cal(CalHandle calHandle, const char channelName[], float64 excitationVoltage, float64 excitationFreq)RemarksSets the SCXI-1540 module to the specified gain value. Calibration input/output points can be measured by supplying reference signals to the specified channel

### DAQmxSetup1540Cal

#### Syntax

int32 __CFUNC DAQmxSetup1540Cal(CalHandle calHandle, const char channelName[], float64 excitationVoltage, float64 excitationFreq)

#### Remarks

Sets the SCXI-1540 module to the specified gain value. Calibration input/output points can be measured by supplying reference signals to the specified channel and measuring the outputs. Each of these points should be specified using the DAQmxAdjust1540Cal function.

Note

The terminal where the module output is measured depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the module user manual for more information on the routing of module output.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelName | [in] | const char[] | The physical channel to calibrate. |
| excitationVoltage | [in] | float64 | The RMS value of the internal AC excitation voltage. |
| excitationFreq | [in] | float64 | The frequency of the internal AC excitation voltage. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SCXI Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1gae082b6fef1b061ee30a2c96a5a719089.html language=enus -->
## TOPIC 00162: DAQmxSetup153xCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1gae082b6fef1b061ee30a2c96a5a719089.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__scxi__calibration_1gae082b6fef1b061ee30a2c96a5a719089.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup153xCal(CalHandle calHandle, const char channelName[], float64 gain)RemarksSets the SCXI-153x module to the specified gain value. Calibration input/output points can be measured by supplying reference signals to the specified channel and measuring the outputs. Each of t

### DAQmxSetup153xCal

#### Syntax

int32 __CFUNC DAQmxSetup153xCal(CalHandle calHandle, const char channelName[], float64 gain)

#### Remarks

Sets the SCXI-153x module to the specified gain value. Calibration input/output points can be measured by supplying reference signals to the specified channel and measuring the outputs. Each of these points should be specified using the DAQmxAdjust153xCal function.

Note

The terminal where the module output is measured depends on the configuration of the module in MAX. National Instruments recommends cabling the module to the digitizer so that the output appears on the MCH0± pins of the rear signal connector. Refer to the module user manual for more information on the routing of module output.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelName | [in] | const char[] | The physical channel to calibrate. |
| gain | [in] | float64 | The gain value to calibrate. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

SCXI Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration.html language=enus -->
## TOPIC 00163: TestScale Calibration

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdjust TestScale CalibrationGet TestScale Calibration Adjustment PointsSetup TestScale CalibrationGroup membersNoneAttachmentsNone

### TestScale Calibration

#### Groups

- Adjust TestScale Calibration
- Get TestScale Calibration Adjustment Points
- Setup TestScale Calibration

#### Group members

None

#### Attachments

None

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration__adjust__testscale__calibration_1gacbea871cc432f048726194605e32ed20.html language=enus -->
## TOPIC 00164: DAQmxAdjust15110Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration__adjust__testscale__calibration_1gacbea871cc432f048726194605e32ed20.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration__adjust__testscale__calibration_1gacbea871cc432f048726194605e32ed20.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjust15110Cal(CalHandle calHandle, const char channelNames[], float64 value)RemarksAdjusts the external calibration constants for a TS-15110.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandleA reference to the calibration session that you created using the DAQmxIn

### DAQmxAdjust15110Cal

#### Syntax

int32 __CFUNC DAQmxAdjust15110Cal(CalHandle calHandle, const char channelNames[], float64 value)

#### Remarks

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for a TS-15110.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | float64 | The reference value measured using a calibrator. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Adjust TestScale Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration__get__te5fadf99fb59c92e70734c1025c9895a8.html language=enus -->
## TOPIC 00165: Get TestScale Calibration Adjustment Points

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration__get__te5fadf99fb59c92e70734c1025c9895a8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration__get__te5fadf99fb59c92e70734c1025c9895a8.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxGet15110CalAdjustPointsDAQmxGet15200CalAdjustPointsAttachmentsNone

### Get TestScale Calibration Adjustment Points

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxGet15110CalAdjustPoints |  |
| DAQmxGet15200CalAdjustPoints |  |

#### Attachments

None

Parent topic:

TestScale Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration__get__te5fadf99fb59c92e70734c1025c9895a8_1ga186318b3d40888abb805dd27d9743b9a.html language=enus -->
## TOPIC 00166: DAQmxGet15200CalAdjustPoints

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration__get__te5fadf99fb59c92e70734c1025c9895a8_1ga186318b3d40888abb805dd27d9743b9a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration__get__te5fadf99fb59c92e70734c1025c9895a8_1ga186318b3d40888abb805dd27d9743b9a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGet15200CalAdjustPoints(CalHandle calHandle, int32 powerCalibrationType, float64 *adjustmentPoints, uInt32 bufferSize)RemarksReturns the reference values to be used by a reference device to create a reference signal.ParametersNameDirectionTypeDescriptioncalHandle[in]CalHandl

### DAQmxGet15200CalAdjustPoints

#### Syntax

int32 __CFUNC DAQmxGet15200CalAdjustPoints(CalHandle calHandle, int32 powerCalibrationType, float64 *adjustmentPoints, uInt32 bufferSize)

#### Remarks

Returns the reference values to be used by a reference device to create a reference signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| powerCalibrationType | [in] | int32 | The calibration type for the device. ValueDescriptionDAQmx_Val_PowerCalibrationType_RemoteVoltageRemote VoltageDAQmx_Val_PowerCalibrationType_LocalVoltageLocal VoltageDAQmx_Val_PowerCalibrationType_CurrentCurrent |
| Value | Description |  |  |
| DAQmx_Val_PowerCalibrationType_RemoteVoltage | Remote Voltage |  |  |
| DAQmx_Val_PowerCalibrationType_LocalVoltage | Local Voltage |  |  |
| DAQmx_Val_PowerCalibrationType_Current | Current |  |  |
| adjustmentPoints | [in] | float64 * | The adjustment points returned by this function. |
| bufferSize | [in] | uInt32 | The size of the buffer, in elements, containing the calibration adjustment points. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Get TestScale Calibration Adjustment Points

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration__setup__testscale__calibration_1ga68dd3792d686cdb32e86878730fd514f.html language=enus -->
## TOPIC 00167: DAQmxSetup15110Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration__setup__testscale__calibration_1ga68dd3792d686cdb32e86878730fd514f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration__setup__testscale__calibration_1ga68dd3792d686cdb32e86878730fd514f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup15110Cal(CalHandle calHandle, const char channelNames[], int32 value)RemarksInitializes a TS-15110 device for calibrating the specified channel type. Refer to the calibration procedure for your device for specific calibration instructions.ParametersNameDirectionTypeDesc

### DAQmxSetup15110Cal

#### Syntax

int32 __CFUNC DAQmxSetup15110Cal(CalHandle calHandle, const char channelNames[], int32 value)

#### Remarks

Initializes a TS-15110 device for calibrating the specified channel type. Refer to the calibration procedure for your device for specific calibration instructions.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| value | [in] | int32 | The binary number to write to the DAC. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Setup TestScale Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration__setup__testscale__calibration_1gacc87c737332130e379db5520c2230441.html language=enus -->
## TOPIC 00168: DAQmxSetup15200Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration__setup__testscale__calibration_1gacc87c737332130e379db5520c2230441.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__testscale__calibration__setup__testscale__calibration_1gacc87c737332130e379db5520c2230441.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSetup15200Cal(CalHandle calHandle, const char channelNames[], float64 adjustmentPoint, int32 powerCalibrationType)RemarksInitializes a TS-15200 device for calibrating the specified channel type. Refer to the calibration procedure for your device for specific calibration inst

### DAQmxSetup15200Cal

#### Syntax

int32 __CFUNC DAQmxSetup15200Cal(CalHandle calHandle, const char channelNames[], float64 adjustmentPoint, int32 powerCalibrationType)

#### Remarks

Initializes a TS-15200 device for calibrating the specified channel type. Refer to the calibration procedure for your device for specific calibration instructions.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | The physical channel(s) to calibrate. |
| adjustmentPoint | [in] | float64 | The value to adjust. |
| powerCalibrationType | [in] | int32 | The calibration type for the device. ValueDescriptionDAQmx_Val_PowerCalibrationType_RemoteVoltageRemote VoltageDAQmx_Val_PowerCalibrationType_LocalVoltageLocal VoltageDAQmx_Val_PowerCalibrationType_CurrentCurrent |
| Value | Description |  |  |
| DAQmx_Val_PowerCalibrationType_RemoteVoltage | Remote Voltage |  |  |
| DAQmx_Val_PowerCalibrationType_LocalVoltage | Local Voltage |  |  |
| DAQmx_Val_PowerCalibrationType_Current | Current |  |  |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Setup TestScale Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__calibration__tio__calibration_1gad3e8bfd92ff8c024a12879fc84515876.html language=enus -->
## TOPIC 00169: DAQmxAdjustTIOTimebaseCal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__calibration__tio__calibration_1gad3e8bfd92ff8c024a12879fc84515876.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__calibration__tio__calibration_1gad3e8bfd92ff8c024a12879fc84515876.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAdjustTIOTimebaseCal(CalHandle calHandle, float64 referenceFrequency)RemarksAdjusts the external calibration constant for the timebase of a TIO device. You must connect a sinusoidal signal with a known frequency to the device and specify that frequency with referenceFrequenc

### DAQmxAdjustTIOTimebaseCal

#### Syntax

int32 __CFUNC DAQmxAdjustTIOTimebaseCal(CalHandle calHandle, float64 referenceFrequency)

#### Remarks

Adjusts the external calibration constant for the timebase of a TIO device. You must connect a sinusoidal signal with a known frequency to the device and specify that frequency with **referenceFrequency**.

Note

You cannot calibrate PXI-6608 devices with this function. Refer to KnowledgeBase 40KGCD2F for more information.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| calHandle | [in] | CalHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| referenceFrequency | [in] | float64 | Specifies in hertz the frequency of the signal to use as a reference for calibration. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

TIO Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__cdaq__sync__functions_1ga6e0d6809ebaeae63895b509e496c13f6.html language=enus -->
## TOPIC 00170: DAQmxGetDisconnectedCDAQSyncPorts

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__cdaq__sync__functions_1ga6e0d6809ebaeae63895b509e496c13f6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__cdaq__sync__functions_1ga6e0d6809ebaeae63895b509e496c13f6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetDisconnectedCDAQSyncPorts(char portList[], uInt32 portListSize)RemarksGets the list of ports disconnected after calling DAQmxAreConfiguredCDAQSyncPortsDisconnected. Disconnected ports are pairs of ports that are declared as being connected, but cannot be verified.Paramete

### DAQmxGetDisconnectedCDAQSyncPorts

#### Syntax

int32 __CFUNC DAQmxGetDisconnectedCDAQSyncPorts(char portList[], uInt32 portListSize)

#### Remarks

Gets the list of ports disconnected after calling DAQmxAreConfiguredCDAQSyncPortsDisconnected. Disconnected ports are pairs of ports that are declared as being connected, but cannot be verified.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| portList | [out] | char[] | The list of port unverified port connections, in comma-separated format. Unverified port connections are specified in pairs. For example, "dev1/port0, dev4/port2" indicates an unverified connection between dev1/port0 and dev4/port2. If you specify a NULL string or a string of size 0, this function returns a string of a size required to fit the port list. |
| portListSize | [out] | uInt32 | The number of cDAQ Sync ports disconnected. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

cDAQ Sync Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__cdaq__sync__functions_1gaa1ee6f7fc1713ed5767b4432ad0159d7.html language=enus -->
## TOPIC 00171: DAQmxAreConfiguredCDAQSyncPortsDisconnected

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__cdaq__sync__functions_1gaa1ee6f7fc1713ed5767b4432ad0159d7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__cdaq__sync__functions_1gaa1ee6f7fc1713ed5767b4432ad0159d7.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAreConfiguredCDAQSyncPortsDisconnected(const char chassisDevicesPorts[], float64 timeout, bool32 *disconnectedPortsExist)RemarksVerifies configured cDAQ Sync connections between devices. Failures generally indicate a wiring issue or that a device has been powered off or remo

### DAQmxAreConfiguredCDAQSyncPortsDisconnected

#### Syntax

int32 __CFUNC DAQmxAreConfiguredCDAQSyncPortsDisconnected(const char chassisDevicesPorts[], float64 timeout, bool32 *disconnectedPortsExist)

#### Remarks

Verifies configured cDAQ Sync connections between devices. Failures generally indicate a wiring issue or that a device has been powered off or removed. Stop all NI-DAQmx tasks running on the devices prior to running this function because any running tasks cause the verification process to fail.

Note

Verification toggles lines on ports during configuration.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| chassisDevicesPorts | [in] | const char[] | Specifies the names of the CompactDAQ chassis, C Series modules, or cDAQ Sync ports in comma separated form to search. If no names are specified, all cDAQ Sync ports on non-simulated devices are scanned. |
| timeout | [in] | float64 | The amount of time, in seconds, to wait for the device to respond before timing out. If a timeout occurs, no configuration is changed. |
| disconnectedPortsExist | [out] | bool32 * | Indicates if any port connections are unverified. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

cDAQ Sync Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__cdaq__sync__functions_1gab65e2aba8081a8be975e186deb919c7e.html language=enus -->
## TOPIC 00172: DAQmxAutoConfigureCDAQSyncConnections

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__cdaq__sync__functions_1gab65e2aba8081a8be975e186deb919c7e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__cdaq__sync__functions_1gab65e2aba8081a8be975e186deb919c7e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxAutoConfigureCDAQSyncConnections(const char chassisDevicesPorts[], float64 timeout)RemarksDetects and configures cDAQ Sync connections between devices. Stop all NI-DAQmx tasks running on the devices prior to running this function because any running tasks cause auto-configur

### DAQmxAutoConfigureCDAQSyncConnections

#### Syntax

int32 __CFUNC DAQmxAutoConfigureCDAQSyncConnections(const char chassisDevicesPorts[], float64 timeout)

#### Remarks

Detects and configures cDAQ Sync connections between devices. Stop all NI-DAQmx tasks running on the devices prior to running this function because any running tasks cause auto-configuration to fail.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| chassisDevicesPorts | [in] | const char[] | Specifies the names of the CompactDAQ chassis, C Series modules, or cDAQ Sync ports in comma separated form to search. If no names are specified, all cDAQ Sync ports on connected, non-simulated devices are scanned. |
| timeout | [in] | float64 | The amount of time, in seconds, to wait for the device to respond before timing out. If a timeout occurs, no configuration is changed. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

cDAQ Sync Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__cdaq__sync__functions_1gadbad9ae7b76e629f7e51ed6cf893466a.html language=enus -->
## TOPIC 00173: DAQmxRemoveCDAQSyncConnection

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__cdaq__sync__functions_1gadbad9ae7b76e629f7e51ed6cf893466a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__cdaq__sync__functions_1gadbad9ae7b76e629f7e51ed6cf893466a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxRemoveCDAQSyncConnection(const char portList[])RemarksRemoves a cDAQ Sync connection between devices. The connection is not verified.ParametersNameDirectionTypeDescriptionportList[in]const char[]Specifies the cDAQ Sync ports to disconnect. ReturnsThe error code returned by t

### DAQmxRemoveCDAQSyncConnection

#### Syntax

int32 __CFUNC DAQmxRemoveCDAQSyncConnection(const char portList[])

#### Remarks

Removes a cDAQ Sync connection between devices. The connection is not verified.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| portList | [in] | const char[] | Specifies the cDAQ Sync ports to disconnect. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

cDAQ Sync Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__device__control.html language=enus -->
## TOPIC 00174: Device Control

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__device__control.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__device__control.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsWatchdogGroup membersNameDescriptionDAQmxResetDeviceDAQmxSelfTestDeviceAttachmentsNone

### Device Control

#### Groups

- Watchdog

#### Group members

| Name | Description |
| --- | --- |
| DAQmxResetDevice |  |
| DAQmxSelfTestDevice |  |

#### Attachments

None

Parent topic:

Advanced Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__device__control_1ga7cab5ff6d335e87c9346cb5be403398b.html language=enus -->
## TOPIC 00175: DAQmxSelfTestDevice

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__device__control_1ga7cab5ff6d335e87c9346cb5be403398b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__device__control_1ga7cab5ff6d335e87c9346cb5be403398b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSelfTestDevice(const char deviceName[])RemarksCauses a device to self-test.ParametersNameDirectionTypeDescriptiondeviceName[in]const char[]Specifies the name to assign to the device. If unspecified, NI-DAQmx chooses the device name. ReturnsThe error code returned by the func

### DAQmxSelfTestDevice

#### Syntax

int32 __CFUNC DAQmxSelfTestDevice(const char deviceName[])

#### Remarks

Causes a device to self-test.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| deviceName | [in] | const char[] | Specifies the name to assign to the device. If unspecified, NI-DAQmx chooses the device name. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Device Control

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__device__control_1ga8318d14e0d92584209dd48c1465a20f8.html language=enus -->
## TOPIC 00176: DAQmxResetDevice

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__device__control_1ga8318d14e0d92584209dd48c1465a20f8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__device__control_1ga8318d14e0d92584209dd48c1465a20f8.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxResetDevice(const char deviceName[])RemarksImmediately aborts all tasks associated with a device and returns the device to an initialized state. Aborting a task stops and releases any resources the task reserved. This function does not wait for the device to reset before con

### DAQmxResetDevice

#### Syntax

int32 __CFUNC DAQmxResetDevice(const char deviceName[])

#### Remarks

Immediately aborts all tasks associated with a device and returns the device to an [initialized](/csh?context=nidaqmx_mxdevconsid_initstates) state. Aborting a task stops and releases any resources the task reserved. This function does not wait for the device to reset before continuing execution. When resetting a chassis, attached modules are unavailable. If you attempt to reset an attached module during this time, you will receive an error.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| deviceName | [in] | const char[] | Specifies the name to assign to the device. If unspecified, NI-DAQmx chooses the device name. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Device Control

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__device__control__watchdog.html language=enus -->
## TOPIC 00177: Watchdog

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__device__control__watchdog.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__device__control__watchdog.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxCfgWatchdogAOExpirStatesDAQmxCfgWatchdogCOExpirStatesDAQmxCfgWatchdogDOExpirStatesDAQmxControlWatchdogTaskDAQmxCreateWatchdogTimerTaskDAQmxCreateWatchdogTimerTaskExAttachmentsNone

### Watchdog

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxCfgWatchdogAOExpirStates |  |
| DAQmxCfgWatchdogCOExpirStates |  |
| DAQmxCfgWatchdogDOExpirStates |  |
| DAQmxControlWatchdogTask |  |
| DAQmxCreateWatchdogTimerTask |  |
| DAQmxCreateWatchdogTimerTaskEx |  |

#### Attachments

None

Parent topic:

Device Control

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__device__control__watchdog_1gad03e01085069dc998dc1b08b4fade06d.html language=enus -->
## TOPIC 00178: DAQmxCfgWatchdogCOExpirStates

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__device__control__watchdog_1gad03e01085069dc998dc1b08b4fade06d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__device__control__watchdog_1gad03e01085069dc998dc1b08b4fade06d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCfgWatchdogCOExpirStates(TaskHandle taskHandle, const char channelNames[], const int32 expirStateArray[], uInt32 arraySize)RemarksConfigures the counter output channel expiration states for a watchdog timer task.ParametersNameDirectionTypeDescriptiontaskHandle[in]TaskHandleA

### DAQmxCfgWatchdogCOExpirStates

#### Syntax

int32 __CFUNC DAQmxCfgWatchdogCOExpirStates(TaskHandle taskHandle, const char channelNames[], const int32 expirStateArray[], uInt32 arraySize)

#### Remarks

Configures the counter output channel expiration states for a watchdog timer task.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | A reference to the calibration session that you created using the DAQmxInitExtCal function. |
| channelNames | [in] | const char[] | A string specifying a list or range of physical channel(s) to use. |
| expirStateArray | [in] | const int32[] | The array containing the states to set the corresponding channels to when the watchdog timer expires. Each element of the array corresponds to the channels specified in channelNames. ValueDescriptionDAQmx_Val_HighHigh logic.DAQmx_Val_LowLow logic.DAQmx_Val_NoChangeExpiration does not affect the state of the counter output. The channels retain their states at the time of the watchdog timer expiration, and no further counter generation runs. |
| Value | Description |  |  |
| DAQmx_Val_High | High logic. |  |  |
| DAQmx_Val_Low | Low logic. |  |  |
| DAQmx_Val_NoChange | Expiration does not affect the state of the counter output. The channels retain their states at the time of the watchdog timer expiration, and no further counter generation runs. |  |  |
| arraySize | [in] | uInt32 | The size of expirStateArray. This must correspond to the number of channels specified in channelNames. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Watchdog

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__real-time__obsolete.html language=enus -->
## TOPIC 00179: Obsolete

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__real-time__obsolete.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__real-time__obsolete.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxIsReadOrWriteLateAttachmentsNone

### Obsolete

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxIsReadOrWriteLate |  |

#### Attachments

None

Parent topic:

Real-Time

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__signal__routing.html language=enus -->
## TOPIC 00180: Signal Routing

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__signal__routing.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__signal__routing.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxConnectTermsDAQmxDisconnectTermsDAQmxTristateOutputTermAttachmentsNone

### Signal Routing

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxConnectTerms |  |
| DAQmxDisconnectTerms |  |
| DAQmxTristateOutputTerm |  |

#### Attachments

None

Parent topic:

Advanced Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__storage.html language=enus -->
## TOPIC 00181: Storage

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__storage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__storage.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxDeleteSavedGlobalChanDAQmxDeleteSavedScaleDAQmxDeleteSavedTaskDAQmxSaveGlobalChanDAQmxSaveScaleDAQmxSaveTaskAttachmentsNone

### Storage

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxDeleteSavedGlobalChan |  |
| DAQmxDeleteSavedScale |  |
| DAQmxDeleteSavedTask |  |
| DAQmxSaveGlobalChan |  |
| DAQmxSaveScale |  |
| DAQmxSaveTask |  |

#### Attachments

None

Parent topic:

Advanced Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__storage_1ga031404b988aa0db51af08987ca0f4e8f.html language=enus -->
## TOPIC 00182: DAQmxDeleteSavedGlobalChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__storage_1ga031404b988aa0db51af08987ca0f4e8f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__storage_1ga031404b988aa0db51af08987ca0f4e8f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxDeleteSavedGlobalChan(const char channelName[])RemarksDeletes the specified global virtual channel from MAX. This function does not remove the global virtual channel from tasks that use it.ParametersNameDirectionTypeDescriptionchannelName[in]const char[]Name of the global vi

### DAQmxDeleteSavedGlobalChan

#### Syntax

int32 __CFUNC DAQmxDeleteSavedGlobalChan(const char channelName[])

#### Remarks

Deletes the specified [global virtual channel](/csh?context=nidaqmx_mxcncpts_chans) from MAX. This function does not remove the global virtual channel from [tasks](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that use it.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| channelName | [in] | const char[] | Name of the global virtual channel to delete. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Storage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__storage_1ga5f838487ff59e920e199f29fcc105ccf.html language=enus -->
## TOPIC 00183: DAQmxSaveScale

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__storage_1ga5f838487ff59e920e199f29fcc105ccf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__storage_1ga5f838487ff59e920e199f29fcc105ccf.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSaveScale(const char scaleName[], const char saveAs[], const char author[], uInt32 options)RemarksSaves the specified custom scale to MAX. Developers can also programmatically save global channels and scales.ParametersNameDirectionTypeDescriptionscaleName[in]const char[]Name

### DAQmxSaveScale

#### Syntax

int32 __CFUNC DAQmxSaveScale(const char scaleName[], const char saveAs[], const char author[], uInt32 options)

#### Remarks

Saves the specified [custom scale](/csh?context=nidaqmx_mxcncpts_customscales) to MAX. Developers can also [programmatically save global channels and scales](https://www.ni.com/en/support/documentation/supplemental/21/programmatic-channel-saves-in-ni-daqmx.html?srsltid=AfmBOooVtkMROwXSb4xw-nja24Anv47uJQBvOfa31xgkDs502lP1P-_D).

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| scaleName | [in] | const char[] | Name of the custom scale to save. |
| saveAs | [in] | const char[] | Name to save the custom scale as. If you pass an empty string ("") or NULL, the name currently assigned to the scale is used. |
| author | [in] | const char[] | Name to store with the custom scale. |
| options | [in] | uInt32 | Use this parameter to set certain options. You can combine options with the bitwise-OR operator ('\|') to set multiple options. Pass a value of zero if no options need to be set. ValueDescriptionDAQmx_Val_Save_OverwriteOverwrite a custom scale of the same name if one is already saved in MAX. If you do not set this flag and a custom scale of the same name is already saved in MAX, the function returns an error.DAQmx_Val_Save_AllowInteractiveEditingAllow the custom scale to be edited in the DAQ Assistant.DAQmx_Val_Save_AllowInteractiveDeletionAllow the custom scale to be deleted through MAX. |
| Value | Description |  |  |
| DAQmx_Val_Save_Overwrite | Overwrite a custom scale of the same name if one is already saved in MAX. If you do not set this flag and a custom scale of the same name is already saved in MAX, the function returns an error. |  |  |
| DAQmx_Val_Save_AllowInteractiveEditing | Allow the custom scale to be edited in the DAQ Assistant. |  |  |
| DAQmx_Val_Save_AllowInteractiveDeletion | Allow the custom scale to be deleted through MAX. |  |  |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Storage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__storage_1ga64f055d78f21d68f637d10274cc5d239.html language=enus -->
## TOPIC 00184: DAQmxDeleteSavedScale

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__storage_1ga64f055d78f21d68f637d10274cc5d239.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__storage_1ga64f055d78f21d68f637d10274cc5d239.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxDeleteSavedScale(const char scaleName[])RemarksDeletes the specified custom scale from MAX. This function does not remove the custom scale from virtual channels that use it.ParametersNameDirectionTypeDescriptionscaleName[in]const char[]Name of the custom scale to delete. Ret

### DAQmxDeleteSavedScale

#### Syntax

int32 __CFUNC DAQmxDeleteSavedScale(const char scaleName[])

#### Remarks

Deletes the specified [custom scale](/csh?context=nidaqmx_mxcncpts_customscales) from MAX. This function does not remove the custom scale from [virtual channels](/csh?context=nidaqmx_mxcncpts_chans) that use it.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| scaleName | [in] | const char[] | Name of the custom scale to delete. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Storage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__storage_1ga954d04d24b3191cba8edbf2b5466a020.html language=enus -->
## TOPIC 00185: DAQmxSaveGlobalChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__storage_1ga954d04d24b3191cba8edbf2b5466a020.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__storage_1ga954d04d24b3191cba8edbf2b5466a020.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSaveGlobalChan(TaskHandle taskHandle, const char channelName[], const char saveAs[], const char author[], uInt32 options)RemarksSaves the specified local or global virtual channel to MAX as a global virtual channel. You must specify both the local or global virtual channel t

### DAQmxSaveGlobalChan

#### Syntax

int32 __CFUNC DAQmxSaveGlobalChan(TaskHandle taskHandle, const char channelName[], const char saveAs[], const char author[], uInt32 options)

#### Remarks

Saves the specified [local or global virtual channel](/csh?context=nidaqmx_mxcncpts_chans) to MAX as a global virtual channel. You must specify both the local or global virtual channel to save and a task that contains that channel. Programmatically saved global virtual channels cannot be viewed in the DAQ Assistant for versions of NI-DAQ earlier than 7.4. To view a programmatically saved global virtual channel in an earlier version of NI-DAQ, first use the DAQ Assistant in NI-DAQ 7.4 or later to save the global virtual channel. Developers can also [programmatically save global channels and scales](https://www.ni.com/en/support/documentation/supplemental/21/programmatic-channel-saves-in-ni-daqmx.html?srsltid=AfmBOooVtkMROwXSb4xw-nja24Anv47uJQBvOfa31xgkDs502lP1P-_D).

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task that contains the local or global virtual channel you want to save. |
| channelName | [in] | const char[] | Name of the local or global virtual channel to save. |
| saveAs | [in] | const char[] | Name to save the global virtual channel as. If you pass an empty string ("") or NULL, the name currently assigned to the global virtual channel will be used. |
| author | [in] | const char[] | Name to store with the global virtual channel. |
| options | [in] | uInt32 | Use this parameter to set certain options. You can combine options with the bitwise-OR operator ('\|') to set multiple options. Pass a value of zero if no options need to be set. ValueDescriptionDAQmx_Val_Save_OverwriteOverwrite a global virtual channel of the same name if one is already saved in MAX. If you do not set this flag and a global virtual channel of the same name is already saved in MAX, the function returns an error.DAQmx_Val_Save_AllowInteractiveEditingAllow the global virtual channel to be edited in the DAQ Assistant. If you set this flag, the DAQ Assistant must support all global virtual channel settings.DAQmx_Val_Save_AllowInteractiveDeletionAllow the global virtual channel to be deleted through MAX. |
| Value | Description |  |  |
| DAQmx_Val_Save_Overwrite | Overwrite a global virtual channel of the same name if one is already saved in MAX. If you do not set this flag and a global virtual channel of the same name is already saved in MAX, the function returns an error. |  |  |
| DAQmx_Val_Save_AllowInteractiveEditing | Allow the global virtual channel to be edited in the DAQ Assistant. If you set this flag, the DAQ Assistant must support all global virtual channel settings. |  |  |
| DAQmx_Val_Save_AllowInteractiveDeletion | Allow the global virtual channel to be deleted through MAX. |  |  |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Storage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__storage_1gae436c6c7406e2389ba37d347518a3756.html language=enus -->
## TOPIC 00186: DAQmxSaveTask

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__storage_1gae436c6c7406e2389ba37d347518a3756.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__storage_1gae436c6c7406e2389ba37d347518a3756.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSaveTask(TaskHandle taskHandle, const char saveAs[], const char author[], uInt32 options)RemarksSaves the specified task and any local channels it contains to MAX. This function does not save global channels. Use DAQmxSaveGlobalChan to save global channels. Programmatically

### DAQmxSaveTask

#### Syntax

int32 __CFUNC DAQmxSaveTask(TaskHandle taskHandle, const char saveAs[], const char author[], uInt32 options)

#### Remarks

Saves the specified [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) and any [local channels](/csh?context=nidaqmx_mxcncpts_chans) it contains to MAX. This function does not save global channels. Use [DAQmxSaveGlobalChan](group__ni-daqmx__c__functions__advanced__functions__storage_1ga954d04d24b3191cba8edbf2b5466a020.html) to save global channels. Programmatically saved tasks cannot be viewed in the DAQ Assistant for versions of NI-DAQ earlier than 7.4. To view a programmatically saved task in an earlier version of NI-DAQ, first use the DAQ Assistant in NI-DAQ 7.4 or later to save the task. Developers can also [programmatically save global channels and scales](https://www.ni.com/en/support/documentation/supplemental/21/programmatic-channel-saves-in-ni-daqmx.html?srsltid=AfmBOooVtkMROwXSb4xw-nja24Anv47uJQBvOfa31xgkDs502lP1P-_D).

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to save. |
| saveAs | [in] | const char[] | Name to save the task as. If you pass an empty string ("") or NULL, the name currently assigned to the task will be used. |
| author | [in] | const char[] | Name to store with the task. |
| options | [in] | uInt32 | Use this parameter to set certain options. You can combine options with the bitwise-OR operator ('\|') to set multiple options. Pass a value of zero if no options need to be set. ValueDescriptionDAQmx_Val_Save_OverwriteOverwrite a task of the same name if one is already saved in MAX. If you do not set this flag and a task of the same name is already saved in MAX, the function returns an error.DAQmx_Val_Save_AllowInteractiveEditingAllow the task to be edited in the DAQ Assistant. If you set this flag, the DAQ Assistant must support all task settings.DAQmx_Val_Save_AllowInteractiveDeletionAllow the task to be deleted through MAX. |
| Value | Description |  |  |
| DAQmx_Val_Save_Overwrite | Overwrite a task of the same name if one is already saved in MAX. If you do not set this flag and a task of the same name is already saved in MAX, the function returns an error. |  |  |
| DAQmx_Val_Save_AllowInteractiveEditing | Allow the task to be edited in the DAQ Assistant. If you set this flag, the DAQ Assistant must support all task settings. |  |  |
| DAQmx_Val_Save_AllowInteractiveDeletion | Allow the task to be deleted through MAX. |  |  |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Storage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__switch__functions.html language=enus -->
## TOPIC 00187: Switch Functions

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__switch__functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__switch__functions.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxSwitchCloseRelaysDAQmxSwitchConnectDAQmxSwitchConnectMultiDAQmxSwitchCreateScanListDAQmxSwitchCreateScanListExDAQmxSwitchDisconnectDAQmxSwitchDisconnectAllDAQmxSwitchDisconnectMultiDAQmxSwitchFindPathDAQmxSwitchGetMultiRelayCountDAQmxSwitchGetMultiRelayPosD

### Switch Functions

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxSwitchCloseRelays |  |
| DAQmxSwitchConnect |  |
| DAQmxSwitchConnectMulti |  |
| DAQmxSwitchCreateScanList |  |
| DAQmxSwitchCreateScanListEx |  |
| DAQmxSwitchDisconnect |  |
| DAQmxSwitchDisconnectAll |  |
| DAQmxSwitchDisconnectMulti |  |
| DAQmxSwitchFindPath |  |
| DAQmxSwitchGetMultiRelayCount |  |
| DAQmxSwitchGetMultiRelayPos |  |
| DAQmxSwitchGetSingleRelayCount |  |
| DAQmxSwitchGetSingleRelayPos |  |
| DAQmxSwitchOpenRelays |  |
| DAQmxSwitchSetTopologyAndReset |  |
| DAQmxSwitchWaitForSettling |  |

#### Attachments

None

Parent topic:

Advanced Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__switch__functions_1ga041dd87d7811e69af464fab08f936f82.html language=enus -->
## TOPIC 00188: DAQmxSwitchGetSingleRelayPos

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__switch__functions_1ga041dd87d7811e69af464fab08f936f82.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__switch__functions_1ga041dd87d7811e69af464fab08f936f82.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSwitchGetSingleRelayPos(const char relayName[], uInt32 *relayPos)RemarksReturns the current position of a single relay.ParametersNameDirectionTypeDescriptionrelayName[in]const char[]The relay you want to query. relayPos[out]uInt32 *The position of the relay. ValueDescription

### DAQmxSwitchGetSingleRelayPos

#### Syntax

int32 __CFUNC DAQmxSwitchGetSingleRelayPos(const char relayName[], uInt32 *relayPos)

#### Remarks

Returns the current position of a single relay.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| relayName | [in] | const char[] | The relay you want to query. |
| relayPos | [out] | uInt32 * | The position of the relay. ValueDescriptionDAQmx_Val_OpenRelay is open.DAQmx_Val_ClosedRelay is closed. |
| Value | Description |  |  |
| DAQmx_Val_Open | Relay is open. |  |  |
| DAQmx_Val_Closed | Relay is closed. |  |  |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Switch Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__switch__functions_1ga29a7d81f2767200889ed735be00e37cd.html language=enus -->
## TOPIC 00189: DAQmxSwitchOpenRelays

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__switch__functions_1ga29a7d81f2767200889ed735be00e37cd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__switch__functions_1ga29a7d81f2767200889ed735be00e37cd.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSwitchOpenRelays(const char relayList[], bool32 waitForSettling)RemarksOpens the specified relays. If you set waitForSettling to TRUE, this function waits only after opening all relays. If you want to wait for settling after opening each relay, use this function multiple tim

### DAQmxSwitchOpenRelays

#### Syntax

int32 __CFUNC DAQmxSwitchOpenRelays(const char relayList[], bool32 waitForSettling)

#### Remarks

Opens the specified relays. If you set waitForSettling to TRUE, this function waits only after opening all relays. If you want to wait for settling after opening each relay, use this function multiple times to open each relay separately. When you operate relays directly, you circumvent the protection offered channel usage types. Avoid using this function when you use [DAQmxSwitchConnect](group__ni-daqmx__c__functions__advanced__functions__switch__functions_1gac6b35f4f4fc3705d636b6e044e436cf2.html) and [DAQmxSwitchDisconnect](group__ni-daqmx__c__functions__advanced__functions__switch__functions_1gae1c927990ae3d053dd6e2f99efacbb9a.html). This function does not pass the changes you make to those functions.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| relayList | [in] | const char[] | A set of relays to open. |
| waitForSettling | [in] | bool32 | If TRUE, this function waits for the switches to settle before returning. If FALSE, the function returns immediately after the operation. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Switch Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__switch__functions_1ga29f1a82e38161f5e5aa08572406ead72.html language=enus -->
## TOPIC 00190: DAQmxSwitchGetMultiRelayPos

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__switch__functions_1ga29f1a82e38161f5e5aa08572406ead72.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__switch__functions_1ga29f1a82e38161f5e5aa08572406ead72.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSwitchGetMultiRelayPos(const char relayList[], uInt32 relayPos[], uInt32 relayPosArraySize, uInt32 *numRelayPossRead)RemarksReturns the current position of a set of relays.ParametersNameDirectionTypeDescriptionrelayList[in]const char[]The set of relays you want to query. rel

### DAQmxSwitchGetMultiRelayPos

#### Syntax

int32 __CFUNC DAQmxSwitchGetMultiRelayPos(const char relayList[], uInt32 relayPos[], uInt32 relayPosArraySize, uInt32 *numRelayPossRead)

#### Remarks

Returns the current position of a set of relays.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| relayList | [in] | const char[] | The set of relays you want to query. |
| relayPosArraySize | [in] | uInt32 | The size of relayPos. If you pass 0, this function returns the number of samples needed to allocate. |
| relayPos | [out] | uInt32[] | The position of each specified relay. The order of this array corresponds to the order of relayList. If you pass NULL, this function returns the number of samples needed to allocate. ValueDescriptionDAQmx_Val_OpenRelay is open.DAQmx_Val_ClosedRelay is closed. |
| Value | Description |  |  |
| DAQmx_Val_Open | Relay is open. |  |  |
| DAQmx_Val_Closed | Relay is closed. |  |  |
| numRelayPossRead | [out] | uInt32 * | The number of relay positions read by the function. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A negative value indicates an error. For this function, if you pass NULL for the buffer or 0 for the buffer size, this function returns the number of samples needed to allocate. For example, malloc (n*sizeof(uInt32));

Parent topic:

Switch Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__switch__functions_1ga2e0598bbb57e94a9928079b453574d79.html language=enus -->
## TOPIC 00191: DAQmxSwitchCreateScanList

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__switch__functions_1ga2e0598bbb57e94a9928079b453574d79.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__switch__functions_1ga2e0598bbb57e94a9928079b453574d79.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSwitchCreateScanList(const char scanList[], TaskHandle *taskHandle)RemarksCreates a new switch scanning task that uses the specified scan list and applies it to the specified task.ParametersNameDirectionTypeDescriptionscanList[in]const char[]Uses a special syntax to specify

### DAQmxSwitchCreateScanList

#### Syntax

int32 __CFUNC DAQmxSwitchCreateScanList(const char scanList[], TaskHandle *taskHandle)

#### Remarks

Creates a new switch scanning task that uses the specified scan list and applies it to the specified task.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| scanList | [in] | const char[] | Uses a special syntax to specify the sequence of connections and disconnections for the task. |
| taskHandle | [out] | TaskHandle * | The task created by this function. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Switch Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__switch__functions_1ga687d0f7d3f30e5b533f4b729918dffd7.html language=enus -->
## TOPIC 00192: DAQmxSwitchCloseRelays

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__switch__functions_1ga687d0f7d3f30e5b533f4b729918dffd7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__switch__functions_1ga687d0f7d3f30e5b533f4b729918dffd7.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSwitchCloseRelays(const char relayList[], bool32 waitForSettling)RemarksCloses the specified relays. If you set waitForSettling to TRUE, this function waits only after closing all relays. If you want to wait for settling after closing each relay, use this function multiple t

### DAQmxSwitchCloseRelays

#### Syntax

int32 __CFUNC DAQmxSwitchCloseRelays(const char relayList[], bool32 waitForSettling)

#### Remarks

Closes the specified relays. If you set waitForSettling to TRUE, this function waits only after closing all relays. If you want to wait for settling after closing each relay, use this function multiple times to close each relay separately. When you operate relays directly, you circumvent the protection that channel usage types offer. Avoid using this function when you use the [DAQmxSwitchConnect](group__ni-daqmx__c__functions__advanced__functions__switch__functions_1gac6b35f4f4fc3705d636b6e044e436cf2.html) function or the [DAQmxSwitchDisconnect](group__ni-daqmx__c__functions__advanced__functions__switch__functions_1gae1c927990ae3d053dd6e2f99efacbb9a.html) function. This function does not pass the changes you make to those functions.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| relayList | [in] | const char[] | A set of relays to close. |
| waitForSettling | [in] | bool32 | If TRUE, this function waits for the switches to settle before returning. If FALSE, the function returns immediately after the operation. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Switch Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__switch__functions_1gab6440eb100cda68095b384310b887130.html language=enus -->
## TOPIC 00193: DAQmxSwitchWaitForSettling

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__switch__functions_1gab6440eb100cda68095b384310b887130.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__switch__functions_1gab6440eb100cda68095b384310b887130.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSwitchWaitForSettling(const char deviceName[])RemarksWaits for the settling time on the device to expire. The device resets this time and begins counting down again when the device performs an operation. This function can return immediately if no operation happened recently.

### DAQmxSwitchWaitForSettling

#### Syntax

int32 __CFUNC DAQmxSwitchWaitForSettling(const char deviceName[])

#### Remarks

Waits for the settling time on the device to expire. The device resets this time and begins counting down again when the device performs an operation. This function can return immediately if no operation happened recently.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| deviceName | [in] | const char[] | Specifies the name to assign to the device. If unspecified, NI-DAQmx chooses the device name. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Switch Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__switch__functions_1gac6b35f4f4fc3705d636b6e044e436cf2.html language=enus -->
## TOPIC 00194: DAQmxSwitchConnect

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__switch__functions_1gac6b35f4f4fc3705d636b6e044e436cf2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__switch__functions_1gac6b35f4f4fc3705d636b6e044e436cf2.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSwitchConnect(const char switchChannel1[], const char switchChannel2[], bool32 waitForSettling)RemarksMakes a connection between two switch channels. When using this function, specify only the two connection endpoints using switchChannel1 and switchChannel2. The function the

### DAQmxSwitchConnect

#### Syntax

int32 __CFUNC DAQmxSwitchConnect(const char switchChannel1[], const char switchChannel2[], bool32 waitForSettling)

#### Remarks

Makes a connection between two switch channels. When using this function, specify only the two connection endpoints using switchChannel1 and switchChannel2. The function then attempts to find an available path between the two channels.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| switchChannel1 | [in] | const char[] | The first channel to connect. |
| switchChannel2 | [in] | const char[] | The second channel to connect. |
| waitForSettling | [in] | bool32 | If TRUE, this function waits for the switches to settle before returning. If FALSE, the function returns immediately after the operation. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Switch Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__switch__functions_1gaccf1d8cca979debe2d2e873e4dd48ccc.html language=enus -->
## TOPIC 00195: DAQmxSwitchCreateScanListEx

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__switch__functions_1gaccf1d8cca979debe2d2e873e4dd48ccc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__switch__functions_1gaccf1d8cca979debe2d2e873e4dd48ccc.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxSwitchCreateScanListEx(const char taskName[], const char scanList[], TaskHandle *taskHandle)RemarksCreates a new switch scanning task that uses the specified scan list and applies it to the specified task.ParametersNameDirectionTypeDescriptiontaskName[in]const char[]Name ass

### DAQmxSwitchCreateScanListEx

#### Syntax

int32 __CFUNC DAQmxSwitchCreateScanListEx(const char taskName[], const char scanList[], TaskHandle *taskHandle)

#### Remarks

Creates a new switch scanning task that uses the specified scan list and applies it to the specified task.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskName | [in] | const char[] | Name assigned to the task. |
| scanList | [in] | const char[] | Uses a special syntax to specify the sequence of connections and disconnections for the task. |
| taskHandle | [out] | TaskHandle * | The task created by this function. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Switch Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__advanced__functions__teds_1gad1651dd3f68be280c1f86ea810707c99.html language=enus -->
## TOPIC 00196: DAQmxClearTEDS

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__advanced__functions__teds_1gad1651dd3f68be280c1f86ea810707c99.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__advanced__functions__teds_1gad1651dd3f68be280c1f86ea810707c99.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxClearTEDS(const char physicalChannel[])RemarksRemoves TEDS information from the physical channel you specify. This function temporarily overrides any TEDS configuration for the physical channel that you performed in MAX.ParametersNameDirectionTypeDescriptionphysicalChannel[i

### DAQmxClearTEDS

#### Syntax

int32 __CFUNC DAQmxClearTEDS(const char physicalChannel[])

#### Remarks

Removes TEDS information from the physical channel you specify. This function temporarily overrides any TEDS configuration for the physical channel that you performed in MAX.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| physicalChannel | [in] | const char[] | The name of the physical channel you want to clear. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

TEDS

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels.html language=enus -->
## TOPIC 00197: Create Analog Input Channels

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsObsoletePositionGroup membersNameDescriptionDAQmxCreateAIAccel4WireDCVoltageChanDAQmxCreateAIAccelChanDAQmxCreateAIAccelChargeChanDAQmxCreateAIBridgeChanDAQmxCreateAICalculatedPowerChanDAQmxCreateAIChargeChanDAQmxCreateAICurrentChanDAQmxCreateAICurrentRMSChanDAQmxCreateAIForceBridgePolynomialC

### Create Analog Input Channels

#### Groups

- Obsolete
- Position

#### Group members

| Name | Description |
| --- | --- |
| DAQmxCreateAIAccel4WireDCVoltageChan |  |
| DAQmxCreateAIAccelChan |  |
| DAQmxCreateAIAccelChargeChan |  |
| DAQmxCreateAIBridgeChan |  |
| DAQmxCreateAICalculatedPowerChan |  |
| DAQmxCreateAIChargeChan |  |
| DAQmxCreateAICurrentChan |  |
| DAQmxCreateAICurrentRMSChan |  |
| DAQmxCreateAIForceBridgePolynomialChan |  |
| DAQmxCreateAIForceBridgeTableChan |  |
| DAQmxCreateAIForceBridgeTwoPointLinChan |  |
| DAQmxCreateAIForceIEPEChan |  |
| DAQmxCreateAIFreqVoltageChan |  |
| DAQmxCreateAIMicrophoneChan |  |
| DAQmxCreateAIPressureBridgePolynomialChan |  |
| DAQmxCreateAIPressureBridgeTableChan |  |
| DAQmxCreateAIPressureBridgeTwoPointLinChan |  |
| DAQmxCreateAIRTDChan |  |
| DAQmxCreateAIResistanceChan |  |
| DAQmxCreateAIRosetteStrainGageChan |  |
| DAQmxCreateAIStrainGageChan |  |
| DAQmxCreateAITempBuiltInSensorChan |  |
| DAQmxCreateAIThrmcplChan |  |
| DAQmxCreateAIThrmstrChanIex |  |
| DAQmxCreateAIThrmstrChanVex |  |
| DAQmxCreateAITorqueBridgePolynomialChan |  |
| DAQmxCreateAITorqueBridgeTableChan |  |
| DAQmxCreateAITorqueBridgeTwoPointLinChan |  |
| DAQmxCreateAIVelocityIEPEChan |  |
| DAQmxCreateAIVoltageChan |  |
| DAQmxCreateAIVoltageChanWithExcit |  |
| DAQmxCreateAIVoltageRMSChan |  |

#### Attachments

None

Parent topic:

Channel Configuration/Creation

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga0256a5337cbe48c93b7450f39f27386e.html language=enus -->
## TOPIC 00198: DAQmxCreateAIVelocityIEPEChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga0256a5337cbe48c93b7450f39f27386e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga0256a5337cbe48c93b7450f39f27386e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateAIVelocityIEPEChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, float64 sensitivity, int32 sensitivityUnits, int32 currentExcitSource, float64 currentExcitVal

### DAQmxCreateAIVelocityIEPEChan

#### Syntax

int32 __CFUNC DAQmxCreateAIVelocityIEPEChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, float64 sensitivity, int32 sensitivityUnits, int32 currentExcitSource, float64 currentExcitVal, const char customScaleName[])

#### Remarks

Creates channel(s) that use an [IEPE velocity sensor](/csh?context=nidaqmx_measfunds_forcepiezo) to [measure velocity](/csh?context=nidaqmx_daqhelp_velocity).

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| physicalChannel | [in] | const char[] | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| terminalConfig | [in] | int32 | The input terminal configuration for the channel. ValueDescriptionDAQmx_Val_Cfg_DefaultAt run time, NI-DAQmx chooses the default terminal configuration for the channel.DAQmx_Val_RSEReferenced single-ended modeDAQmx_Val_NRSENon-referenced single-ended modeDAQmx_Val_DiffDifferential modeDAQmx_Val_PseudoDiffPseudodifferential mode |
| Value | Description |  |  |
| DAQmx_Val_Cfg_Default | At run time, NI-DAQmx chooses the default terminal configuration for the channel. |  |  |
| DAQmx_Val_RSE | Referenced single-ended mode |  |  |
| DAQmx_Val_NRSE | Non-referenced single-ended mode |  |  |
| DAQmx_Val_Diff | Differential mode |  |  |
| DAQmx_Val_PseudoDiff | Pseudodifferential mode |  |  |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | Specifies in which unit to return velocity measurements from the channel. ValueDescriptionDAQmx_Val_MetersPerSecondMeters per second.DAQmx_Val_InchesPerSecondInches per second.DAQmx_Val_FromCustomScaleUnits a custom scale specifies. Use customScaleName to specify a custom scale. |
| Value | Description |  |  |
| DAQmx_Val_MetersPerSecond | Meters per second. |  |  |
| DAQmx_Val_InchesPerSecond | Inches per second. |  |  |
| DAQmx_Val_FromCustomScale | Units a custom scale specifies. Use customScaleName to specify a custom scale. |  |  |
| sensitivity | [in] | float64 | The sensitivity of the sensor. This value is in the units you specify with the sensitivityUnits input. Refer to the sensor documentation to determine this value. |
| sensitivityUnits | [in] | int32 | The units of sensitivity. NameDescriptionDAQmx_Val_MillivoltsPerMillimeterPerSecondmVolts/mm/s.DAQmx_Val_MilliVoltsPerInchPerSecondmVolts/in/s. |
| Name | Description |  |  |
| DAQmx_Val_MillivoltsPerMillimeterPerSecond | mVolts/mm/s. |  |  |
| DAQmx_Val_MilliVoltsPerInchPerSecond | mVolts/in/s. |  |  |
| currentExcitSource | [in] | int32 | The source of excitation. ValueDescriptionDAQmx_Val_InternalUse the built-in excitation source of the device. You must use currentExcitVal to specify the amount of excitation.DAQmx_Val_ExternalUse an excitation source other than the built-in excitation source of the device. You must use currentExcitVal to specify the amount of excitation.DAQmx_Val_NoneSupply no excitation to the channel. You cannot use this value if the sensor requires excitation. |
| Value | Description |  |  |
| DAQmx_Val_Internal | Use the built-in excitation source of the device. You must use currentExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_External | Use an excitation source other than the built-in excitation source of the device. You must use currentExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_None | Supply no excitation to the channel. You cannot use this value if the sensor requires excitation. |  |  |
| currentExcitVal | [in] | float64 | The amount of excitation, in amperes, that the sensor requires. |
| customScaleName | [in] | const char[] | The name of a custom scale to apply to the channel. To use this parameter, you must set units to DAQmx_Val_FromCustomScale. If you do not set units to DAQmx_Val_FromCustomScale, you must set customScaleName to NULL. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Analog Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga14601c8fa84eff35374b3d60996f98a9.html language=enus -->
## TOPIC 00199: DAQmxCreateAICalculatedPowerChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga14601c8fa84eff35374b3d60996f98a9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga14601c8fa84eff35374b3d60996f98a9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateAICalculatedPowerChan(TaskHandle taskHandle, const char voltagePhysicalChannel[], const char currentPhysicalChannel[], const char nameToAssignToChannel[], int32 terminalConfig, float64 voltageMinVal, float64 voltageMaxVal, float64 currentMinVal, float64 currentMaxVal,

### DAQmxCreateAICalculatedPowerChan

#### Syntax

int32 __CFUNC DAQmxCreateAICalculatedPowerChan(TaskHandle taskHandle, const char voltagePhysicalChannel[], const char currentPhysicalChannel[], const char nameToAssignToChannel[], int32 terminalConfig, float64 voltageMinVal, float64 voltageMaxVal, float64 currentMinVal, float64 currentMaxVal, int32 units, int32 shuntResistorLoc, float64 extShuntResistorVal, const char customScaleName[])

#### Remarks

Creates channel(s) for calculated power measurement and adds the channel(s) to the task you specify with taskHandle.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| voltagePhysicalChannel | [in] | const char[] | The names of the voltage physical channels to use to create virtual power channels. You can specify a list or range of physical channels. |
| currentPhysicalChannel | [in] | const char[] | The names of the current physical channels to use to create virtual power channels. You can specify a list or range of physical channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| terminalConfig | [in] | int32 | The input terminal configuration for the channel. ValueDescriptionDAQmx_Val_Cfg_DefaultAt run time, NI-DAQmx chooses the default terminal configuration for the channel.DAQmx_Val_RSEReferenced single-ended modeDAQmx_Val_NRSENon-referenced single-ended modeDAQmx_Val_DiffDifferential modeDAQmx_Val_PseudoDiffPseudodifferential mode |
| Value | Description |  |  |
| DAQmx_Val_Cfg_Default | At run time, NI-DAQmx chooses the default terminal configuration for the channel. |  |  |
| DAQmx_Val_RSE | Referenced single-ended mode |  |  |
| DAQmx_Val_NRSE | Non-referenced single-ended mode |  |  |
| DAQmx_Val_Diff | Differential mode |  |  |
| DAQmx_Val_PseudoDiff | Pseudodifferential mode |  |  |
| voltageMinVal | [in] | float64 | The voltage minimum value, in units, that you expect to measure. |
| voltageMaxVal | [in] | float64 | The voltage maximum value, in units, that you expect to measure. |
| currentMinVal | [in] | float64 | The current minimum value, in units, that you expect to measure. |
| currentMaxVal | [in] | float64 | The current maximum value, in units, that you expect to measure. |
| units | [in] | int32 | The units to use to return the measurement. ValueDescriptionDAQmx_Val_WattsWattsDAQmx_Val_FromCustomScaleUnits a custom scale specifies. If you select this value, you must specify a custom scale name. |
| Value | Description |  |  |
| DAQmx_Val_Watts | Watts |  |  |
| DAQmx_Val_FromCustomScale | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |  |  |
| shuntResistorLoc | [in] | int32 | The location of the shunt resistor. ValueDescriptionDAQmx_Val_DefaultAt run time, NI-DAQmx chooses the default shunt resistor location for the channel.DAQmx_Val_InternalUse the built-in shunt resistor of the device.DAQmx_Val_ExternalUse a shunt resistor external to the device. You must specify the value of the shunt resistor in extShuntResistorVal. |
| Value | Description |  |  |
| DAQmx_Val_Default | At run time, NI-DAQmx chooses the default shunt resistor location for the channel. |  |  |
| DAQmx_Val_Internal | Use the built-in shunt resistor of the device. |  |  |
| DAQmx_Val_External | Use a shunt resistor external to the device. You must specify the value of the shunt resistor in extShuntResistorVal. |  |  |
| extShuntResistorVal | [in] | float64 | The value, in ohms, of an external shunt resistor. |
| customScaleName | [in] | const char[] | The name of a custom scale to apply to the channel. To use this parameter, you must set units to DAQmx_Val_FromCustomScale. If you do not set units to DAQmx_Val_FromCustomScale, you must set customScaleName to NULL. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Analog Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga3111dddf4f6eef35801096d09db7d574.html language=enus -->
## TOPIC 00200: DAQmxCreateAIRTDChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga3111dddf4f6eef35801096d09db7d574.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga3111dddf4f6eef35801096d09db7d574.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateAIRTDChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 rtdType, int32 resistanceConfig, int32 currentExcitSource, float64 currentExcitVal, float64 r0)RemarksCreates channel(s

### DAQmxCreateAIRTDChan

#### Syntax

int32 __CFUNC DAQmxCreateAIRTDChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 rtdType, int32 resistanceConfig, int32 currentExcitSource, float64 currentExcitVal, float64 r0)

#### Remarks

Creates channel(s) that use an [RTD](/csh?context=nidaqmx_measfunds_rtd) to measure temperature and adds the channel(s) to the task you specify with taskHandle.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| physicalChannel | [in] | const char[] | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | The units to use to return the measurement. NameDescriptionDAQmx_Val_DegCdegrees CelsiusDAQmx_Val_DegFdegrees FahrenheitDAQmx_Val_KelvinskelvinsDAQmx_Val_DegRdegrees Rankine |
| Name | Description |  |  |
| DAQmx_Val_DegC | degrees Celsius |  |  |
| DAQmx_Val_DegF | degrees Fahrenheit |  |  |
| DAQmx_Val_Kelvins | kelvins |  |  |
| DAQmx_Val_DegR | degrees Rankine |  |  |
| rtdType | [in] | int32 | The type of RTD connected to the channel. ValueDescriptionDAQmx_Val_Pt3750Pt3750DAQmx_Val_Pt3851Pt3851DAQmx_Val_Pt3911Pt3911DAQmx_Val_Pt3916Pt3916DAQmx_Val_Pt3920Pt3920DAQmx_Val_Pt3928Pt3928DAQmx_Val_CustomYou must specify the 'A', 'B', and 'C' constants for theCallendar-Van Dusen equation |
| Value | Description |  |  |
| DAQmx_Val_Pt3750 | Pt3750 |  |  |
| DAQmx_Val_Pt3851 | Pt3851 |  |  |
| DAQmx_Val_Pt3911 | Pt3911 |  |  |
| DAQmx_Val_Pt3916 | Pt3916 |  |  |
| DAQmx_Val_Pt3920 | Pt3920 |  |  |
| DAQmx_Val_Pt3928 | Pt3928 |  |  |
| DAQmx_Val_Custom | You must specify the 'A', 'B', and 'C' constants for theCallendar-Van Dusen equation |  |  |
| resistanceConfig | [in] | int32 | The configuration for resistance measurements. ValueDescriptionDAQmx_Val_2Wire2-wire mode.DAQmx_Val_3Wire3-wire mode.DAQmx_Val_4Wire4-wire mode. |
| Value | Description |  |  |
| DAQmx_Val_2Wire | 2-wire mode. |  |  |
| DAQmx_Val_3Wire | 3-wire mode. |  |  |
| DAQmx_Val_4Wire | 4-wire mode. |  |  |
| currentExcitSource | [in] | int32 | The source of excitation. ValueDescriptionDAQmx_Val_InternalUse the built-in excitation source of the device. You must use currentExcitVal to specify the amount of excitation.DAQmx_Val_ExternalUse an excitation source other than the built-in excitation source of the device. You must use currentExcitVal to specify the amount of excitation.DAQmx_Val_NoneSupply no excitation to the channel. You cannot use this value if the sensor requires excitation. |
| Value | Description |  |  |
| DAQmx_Val_Internal | Use the built-in excitation source of the device. You must use currentExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_External | Use an excitation source other than the built-in excitation source of the device. You must use currentExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_None | Supply no excitation to the channel. You cannot use this value if the sensor requires excitation. |  |  |
| currentExcitVal | [in] | float64 | The amount of excitation, in amperes, that the sensor requires. |
| r0 | [in] | float64 | The sensor resistance in ohms at 0 deg C for the Callendar-Van Dusen equation Refer to the sensor documentation to determine this value. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Analog Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga407b87343cc271196c53089ff2f9b383.html language=enus -->
## TOPIC 00201: DAQmxCreateAIForceBridgePolynomialChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga407b87343cc271196c53089ff2f9b383.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga407b87343cc271196c53089ff2f9b383.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateAIForceBridgePolynomialChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 bridgeConfig, int32 voltageExcitSource, float64 voltageExcitVal, float64 nominalBridgeResistance, con

### DAQmxCreateAIForceBridgePolynomialChan

#### Syntax

int32 __CFUNC DAQmxCreateAIForceBridgePolynomialChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 bridgeConfig, int32 voltageExcitSource, float64 voltageExcitVal, float64 nominalBridgeResistance, const float64 forwardCoeffs[], uInt32 numForwardCoeffs, const float64 reverseCoeffs[], uInt32 numReverseCoeffs, int32 electricalUnits, int32 physicalUnits, const char customScaleName[])

#### Remarks

Creates channel(s) that use a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure force or load](/csh?context=nidaqmx_daqhelp_force). Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this [scaling type](/csh?context=nidaqmx_measfunds_bridgescalingtypes), NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use the [DAQmxCalculateReversePolyCoeff](group__ni-daqmx__c__functions__scale__configuration_1ga09d15d5045ea859339545904559d95de.html) function to generate the other set. Specify different values for **units** and **physicalUnits** if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| physicalChannel | [in] | const char[] | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | Specifies in which unit to return force measurements from the channel. NameDescriptionDAQmx_Val_NewtonsnewtonsDAQmx_Val_PoundspoundsDAQmx_Val_KilogramForcekilograms-forceDAQmx_Val_FromCustomScaleUnits a custom scale specifies. Use customScaleName to specify a custom scale. |
| Name | Description |  |  |
| DAQmx_Val_Newtons | newtons |  |  |
| DAQmx_Val_Pounds | pounds |  |  |
| DAQmx_Val_KilogramForce | kilograms-force |  |  |
| DAQmx_Val_FromCustomScale | Units a custom scale specifies. Use customScaleName to specify a custom scale. |  |  |
| bridgeConfig | [in] | int32 | Specifies the Wheatstone bridge configuration connected to the channel. ValueDescriptionDAQmx_Val_FullBridgeFour active sensing elements in the bridgeDAQmx_Val_HalfBridgeTwo active sensing elements in the bridgeDAQmx_Val_QuarterBridgeOne active sensing element in the bridge |
| Value | Description |  |  |
| DAQmx_Val_FullBridge | Four active sensing elements in the bridge |  |  |
| DAQmx_Val_HalfBridge | Two active sensing elements in the bridge |  |  |
| DAQmx_Val_QuarterBridge | One active sensing element in the bridge |  |  |
| voltageExcitSource | [in] | int32 | The source of excitation. ValueDescriptionDAQmx_Val_InternalUse the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation.DAQmx_Val_ExternalUse an excitation source other than the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation.DAQmx_Val_NoneSupply no excitation to the channel. |
| Value | Description |  |  |
| DAQmx_Val_Internal | Use the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_External | Use an excitation source other than the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_None | Supply no excitation to the channel. |  |  |
| voltageExcitVal | [in] | float64 | Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values. |
| nominalBridgeResistance | [in] | float64 | Specifies in ohms the resistance of the bridge while not under load. |
| forwardCoeffs | [in] | const float64[] | An array of coefficients for the polynomial that converts electrical values to physical values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3. |
| numForwardCoeffs | [in] | uInt32 | The number of coefficients in the forwardCoeffs array. |
| reverseCoeffs | [in] | const float64[] | An array of coefficients for the polynomial that converts physical values to electrical values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3. |
| numReverseCoeffs | [in] | uInt32 | The number of coefficients in the reverseCoeffs array. |
| electricalUnits | [in] | int32 | Specifies from which electrical unit to scale data. Select the same unit that the sensor data sheet or calibration certificate uses for electrical values. ValueDescriptionDAQmx_Val_VoltsPerVoltvolts per voltDAQmx_Val_mVoltsPerVoltmillivolts per volt |
| Value | Description |  |  |
| DAQmx_Val_VoltsPerVolt | volts per volt |  |  |
| DAQmx_Val_mVoltsPerVolt | millivolts per volt |  |  |
| physicalUnits | [in] | int32 | Specifies to which physical units to scale electrical data. Select the same unit that the sensor data sheet or calibration certificate uses for physical values. ValueDescriptionDAQmx_Val_NewtonsnewtonsDAQmx_Val_PoundspoundsDAQmx_Val_KilogramForcekilograms-force |
| Value | Description |  |  |
| DAQmx_Val_Newtons | newtons |  |  |
| DAQmx_Val_Pounds | pounds |  |  |
| DAQmx_Val_KilogramForce | kilograms-force |  |  |
| customScaleName | [in] | const char[] | The name of a custom scale to apply to the channel. To use this parameter, you must set units to DAQmx_Val_FromCustomScale. If you do not set units to DAQmx_Val_FromCustomScale, you must set customScaleName to NULL. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Analog Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga4e2aeb0cb00398ba8f132c5407ea5d58.html language=enus -->
## TOPIC 00202: DAQmxCreateAIChargeChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga4e2aeb0cb00398ba8f132c5407ea5d58.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga4e2aeb0cb00398ba8f132c5407ea5d58.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateAIChargeChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, const char customScaleName[])RemarksCreates channel(s) that use a sensor with charge output.Paramete

### DAQmxCreateAIChargeChan

#### Syntax

int32 __CFUNC DAQmxCreateAIChargeChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, const char customScaleName[])

#### Remarks

Creates channel(s) that use a sensor with charge output.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task used in this function. |
| physicalChannel | [in] | const char[] | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| terminalConfig | [in] | int32 | The input terminal configuration for the channel. ValueDescriptionDAQmx_Val_Cfg_DefaultAt run time, NI-DAQmx chooses the default terminal configuration for the channel.DAQmx_Val_RSEReferenced single-ended modeDAQmx_Val_NRSENon-referenced single-ended modeDAQmx_Val_DiffDifferential modeDAQmx_Val_PseudoDiffPseudodifferential mode |
| Value | Description |  |  |
| DAQmx_Val_Cfg_Default | At run time, NI-DAQmx chooses the default terminal configuration for the channel. |  |  |
| DAQmx_Val_RSE | Referenced single-ended mode |  |  |
| DAQmx_Val_NRSE | Non-referenced single-ended mode |  |  |
| DAQmx_Val_Diff | Differential mode |  |  |
| DAQmx_Val_PseudoDiff | Pseudodifferential mode |  |  |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | The units to use to return from the channel. ValueDescriptionDAQmx_Val_FromCustomScaleUnits a custom scale specifies. If you select this value, you must specify a custom scale name.DAQmx_Val_CoulombsCoulombsDAQmx_Val_PicoCoulombsPicocoulombs |
| Value | Description |  |  |
| DAQmx_Val_FromCustomScale | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |  |  |
| DAQmx_Val_Coulombs | Coulombs |  |  |
| DAQmx_Val_PicoCoulombs | Picocoulombs |  |  |
| customScaleName | [in] | const char[] | The name of a custom scale to apply to the channel. To use this parameter, you must set units to DAQmx_Val_FromCustomScale. If you do not set units to DAQmx_Val_FromCustomScale, you must set customScaleName to NULL. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Analog Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga58a8c28527b09fa4182a2fab25fbfe57.html language=enus -->
## TOPIC 00203: DAQmxCreateAIPressureBridgeTwoPointLinChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga58a8c28527b09fa4182a2fab25fbfe57.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga58a8c28527b09fa4182a2fab25fbfe57.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateAIPressureBridgeTwoPointLinChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 bridgeConfig, int32 voltageExcitSource, float64 voltageExcitVal, float64 nominalBridgeResistance,

### DAQmxCreateAIPressureBridgeTwoPointLinChan

#### Syntax

int32 __CFUNC DAQmxCreateAIPressureBridgeTwoPointLinChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 bridgeConfig, int32 voltageExcitSource, float64 voltageExcitVal, float64 nominalBridgeResistance, float64 firstElectricalVal, float64 secondElectricalVal, int32 electricalUnits, float64 firstPhysicalVal, float64 secondPhysicalVal, int32 physicalUnits, const char customScaleName[])

#### Remarks

Creates channel(s) that use a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure pressure](/csh?context=nidaqmx_daqhelp_pressure). Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this [scaling type](/csh?context=nidaqmx_measfunds_bridgescalingtypes), NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. Specify different values for **units** and **physicalUnits** if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| physicalChannel | [in] | const char[] | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | Specifies in which unit to return pressure measurements from the channel. NameDescriptionDAQmx_Val_PoundsPerSquareInchpounds per square inchDAQmx_Val_BarbarDAQmx_Val_PascalspascalsDAQmx_Val_FromCustomScaleUnits a custom scale specifies. Use customScaleName to specify a custom scale. |
| Name | Description |  |  |
| DAQmx_Val_PoundsPerSquareInch | pounds per square inch |  |  |
| DAQmx_Val_Bar | bar |  |  |
| DAQmx_Val_Pascals | pascals |  |  |
| DAQmx_Val_FromCustomScale | Units a custom scale specifies. Use customScaleName to specify a custom scale. |  |  |
| bridgeConfig | [in] | int32 | Specifies the Wheatstone bridge configuration connected to the channel. ValueDescriptionDAQmx_Val_FullBridgeFour active sensing elements in the bridgeDAQmx_Val_HalfBridgeTwo active sensing elements in the bridgeDAQmx_Val_QuarterBridgeOne active sensing element in the bridge |
| Value | Description |  |  |
| DAQmx_Val_FullBridge | Four active sensing elements in the bridge |  |  |
| DAQmx_Val_HalfBridge | Two active sensing elements in the bridge |  |  |
| DAQmx_Val_QuarterBridge | One active sensing element in the bridge |  |  |
| voltageExcitSource | [in] | int32 | The source of excitation. ValueDescriptionDAQmx_Val_InternalUse the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation.DAQmx_Val_ExternalUse an excitation source other than the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation.DAQmx_Val_NoneSupply no excitation to the channel. |
| Value | Description |  |  |
| DAQmx_Val_Internal | Use the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_External | Use an excitation source other than the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_None | Supply no excitation to the channel. |  |  |
| voltageExcitVal | [in] | float64 | Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values. |
| nominalBridgeResistance | [in] | float64 | Specifies in ohms the resistance of the bridge while not under load. |
| firstElectricalVal | [in] | float64 | The first electrical value, corresponding to firstPhysicalVal. Specify this value in the unit indicated by electricalUnits. |
| secondElectricalVal | [in] | float64 | The second electrical value, corresponding to secondPhysicalVal. Specify this value in the unit indicated by electricalUnits. |
| electricalUnits | [in] | int32 | Specifies from which electrical unit to scale data. Select the same unit that the sensor data sheet or calibration certificate uses for electrical values. ValueDescriptionDAQmx_Val_VoltsPerVoltvolts per voltDAQmx_Val_mVoltsPerVoltmillivolts per volt |
| Value | Description |  |  |
| DAQmx_Val_VoltsPerVolt | volts per volt |  |  |
| DAQmx_Val_mVoltsPerVolt | millivolts per volt |  |  |
| firstPhysicalVal | [in] | float64 | The first physical value, corresponding to firstElectricalVal. Specify this value in the unit indicated by physicalUnits. |
| secondPhysicalVal | [in] | float64 | The second physical value, corresponding to secondElectricalValue. Specify this value in the unit indicated by physicalUnits. |
| physicalUnits | [in] | int32 | Specifies to which physical unit to scale electrical data. Select the same unit that the sensor data sheet or calibration certificate uses for physical values. ValueDescriptionDAQmx_Val_PoundsPerSquareInchpounds per square inchDAQmx_Val_BarbarDAQmx_Val_Pascalspascals |
| Value | Description |  |  |
| DAQmx_Val_PoundsPerSquareInch | pounds per square inch |  |  |
| DAQmx_Val_Bar | bar |  |  |
| DAQmx_Val_Pascals | pascals |  |  |
| customScaleName | [in] | const char[] | The name of a custom scale to apply to the channel. To use this parameter, you must set units to DAQmx_Val_FromCustomScale. If you do not set units to DAQmx_Val_FromCustomScale, you must set customScaleName to NULL. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Analog Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga79514ce1961338c419f0d6e1157e7b83.html language=enus -->
## TOPIC 00204: DAQmxCreateAIThrmstrChanVex

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga79514ce1961338c419f0d6e1157e7b83.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1ga79514ce1961338c419f0d6e1157e7b83.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateAIThrmstrChanVex(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 resistanceConfig, int32 voltageExcitSource, float64 voltageExcitVal, float64 a, float64 b, float64 c, float64 r1

### DAQmxCreateAIThrmstrChanVex

#### Syntax

int32 __CFUNC DAQmxCreateAIThrmstrChanVex(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 resistanceConfig, int32 voltageExcitSource, float64 voltageExcitVal, float64 a, float64 b, float64 c, float64 r1)

#### Remarks

Creates channel(s) that use a [thermistor](/csh?context=nidaqmx_measfunds_thermistors) to measure temperature and adds the channel(s) to the task you specify with taskHandle. Use this function when the thermistor requires voltage excitation.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| physicalChannel | [in] | const char[] | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | The units to use to return the measurement. NameDescriptionDAQmx_Val_DegCdegrees CelsiusDAQmx_Val_DegFdegrees FahrenheitDAQmx_Val_KelvinskelvinsDAQmx_Val_DegRdegrees Rankine |
| Name | Description |  |  |
| DAQmx_Val_DegC | degrees Celsius |  |  |
| DAQmx_Val_DegF | degrees Fahrenheit |  |  |
| DAQmx_Val_Kelvins | kelvins |  |  |
| DAQmx_Val_DegR | degrees Rankine |  |  |
| resistanceConfig | [in] | int32 | The configuration for resistance measurements. ValueDescriptionDAQmx_Val_2Wire2-wire mode.DAQmx_Val_3Wire3-wire mode.DAQmx_Val_4Wire4-wire mode. |
| Value | Description |  |  |
| DAQmx_Val_2Wire | 2-wire mode. |  |  |
| DAQmx_Val_3Wire | 3-wire mode. |  |  |
| DAQmx_Val_4Wire | 4-wire mode. |  |  |
| voltageExcitSource | [in] | int32 | The source of excitation. ValueDescriptionDAQmx_Val_InternalUse the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation.DAQmx_Val_ExternalUse an excitation source other than the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation.DAQmx_Val_NoneSupply no excitation to the channel. |
| Value | Description |  |  |
| DAQmx_Val_Internal | Use the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_External | Use an excitation source other than the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_None | Supply no excitation to the channel. |  |  |
| voltageExcitVal | [in] | float64 | Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values. |
| a | [in] | float64 | The A constant from the Steinhart-Hart thermistor equation. |
| b | [in] | float64 | The B constant from the Steinhart-Hart thermistor equation. |
| c | [in] | float64 | The C constant from the Steinhart-Hart thermistor equation. |
| r1 | [in] | float64 | The value, in ohms, of the reference resistor. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Analog Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1gaf3c2e5588e3464f607734acd27d52f79.html language=enus -->
## TOPIC 00205: DAQmxCreateAIAccel4WireDCVoltageChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1gaf3c2e5588e3464f607734acd27d52f79.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels_1gaf3c2e5588e3464f607734acd27d52f79.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateAIAccel4WireDCVoltageChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, float64 sensitivity, int32 sensitivityUnits, int32 voltageExcitSource, float64 voltageE

### DAQmxCreateAIAccel4WireDCVoltageChan

#### Syntax

int32 __CFUNC DAQmxCreateAIAccel4WireDCVoltageChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, float64 sensitivity, int32 sensitivityUnits, int32 voltageExcitSource, float64 voltageExcitVal, bool32 useExcitForScaling, const char customScaleName[])

#### Remarks

Creates channel(s) to measure acceleration. Use this function for custom sensors that require excitation. You can use the excitation to scale the measurement.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task used in this function. |
| physicalChannel | [in] | const char[] | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| terminalConfig | [in] | int32 | The input terminal configuration for the channel. ValueDescriptionDAQmx_Val_Cfg_DefaultAt run time, NI-DAQmx chooses the default terminal configuration for the channel.DAQmx_Val_RSEReferenced single-ended modeDAQmx_Val_NRSENon-referenced single-ended modeDAQmx_Val_DiffDifferential modeDAQmx_Val_PseudoDiffPseudodifferential mode |
| Value | Description |  |  |
| DAQmx_Val_Cfg_Default | At run time, NI-DAQmx chooses the default terminal configuration for the channel. |  |  |
| DAQmx_Val_RSE | Referenced single-ended mode |  |  |
| DAQmx_Val_NRSE | Non-referenced single-ended mode |  |  |
| DAQmx_Val_Diff | Differential mode |  |  |
| DAQmx_Val_PseudoDiff | Pseudodifferential mode |  |  |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | The units to use to return from the channel. ValueDescriptionDAQmx_Val_FromCustomScaleUnits a custom scale specifies. If you select this value, you must specify a custom scale name.DAQmx_Val_gGramsDAQmx_Val_MetersPerSecondSquaredMeters per second squaredDAQmx_Val_InchesPerSecondSquaredInches per second squared |
| Value | Description |  |  |
| DAQmx_Val_FromCustomScale | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |  |  |
| DAQmx_Val_g | Grams |  |  |
| DAQmx_Val_MetersPerSecondSquared | Meters per second squared |  |  |
| DAQmx_Val_InchesPerSecondSquared | Inches per second squared |  |  |
| sensitivity | [in] | float64 | The sensitivity of the sensor. This value is in the units you specify with the sensitivityUnits input. Refer to the sensor documentation to determine this value. |
| sensitivityUnits | [in] | int32 | The units of sensitivity. NameDescriptionDAQmx_Val_mVoltsPerGMillivolts per gramDAQmx_Val_VoltsPerGVolts per gram |
| Name | Description |  |  |
| DAQmx_Val_mVoltsPerG | Millivolts per gram |  |  |
| DAQmx_Val_VoltsPerG | Volts per gram |  |  |
| voltageExcitSource | [in] | int32 | The source of excitation. ValueDescriptionDAQmx_Val_InternalUse the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation.DAQmx_Val_ExternalUse an excitation source other than the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation.DAQmx_Val_NoneSupply no excitation to the channel. |
| Value | Description |  |  |
| DAQmx_Val_Internal | Use the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_External | Use an excitation source other than the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_None | Supply no excitation to the channel. |  |  |
| voltageExcitVal | [in] | float64 | Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values. |
| useExcitForScaling | [in] | bool32 | Whether the excitation voltage will be used to scale the returned data |
| customScaleName | [in] | const char[] | The name of a custom scale to apply to the channel. To use this parameter, you must set units to DAQmx_Val_FromCustomScale. If you do not set units to DAQmx_Val_FromCustomScale, you must set customScaleName to NULL. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Analog Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels__position_1ga56011cf58634d3a3ba23ff7dc9d8f9a1.html language=enus -->
## TOPIC 00206: DAQmxCreateAIPosRVDTChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels__position_1ga56011cf58634d3a3ba23ff7dc9d8f9a1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__input__channels__position_1ga56011cf58634d3a3ba23ff7dc9d8f9a1.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateAIPosRVDTChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, float64 sensitivity, int32 sensitivityUnits, int32 voltageExcitSource, float64 voltageExcitVal, float64 voltageExcitFreq,

### DAQmxCreateAIPosRVDTChan

#### Syntax

int32 __CFUNC DAQmxCreateAIPosRVDTChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, float64 sensitivity, int32 sensitivityUnits, int32 voltageExcitSource, float64 voltageExcitVal, float64 voltageExcitFreq, int32 ACExcitWireMode, const char customScaleName[])

#### Remarks

Creates channel(s) that use an [RVDT](/csh?context=nidaqmx_measfunds_rvdts) to measure angular position and adds the channel(s) to the task you specify with taskHandle.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| physicalChannel | [in] | const char[] | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | The units to use to return angular position measurements from the channel. NameDescriptionDAQmx_Val_DegreesDegreesDAQmx_Val_RadiansRadiansDAQmx_Val_FromCustomScaleUnits specified by a custom scale. Use customScaleName to specify a custom scale. |
| Name | Description |  |  |
| DAQmx_Val_Degrees | Degrees |  |  |
| DAQmx_Val_Radians | Radians |  |  |
| DAQmx_Val_FromCustomScale | Units specified by a custom scale. Use customScaleName to specify a custom scale. |  |  |
| sensitivity | [in] | float64 | The sensitivity of the sensor. This value is in the units you specify with the sensitivityUnits input. Refer to the sensor documentation to determine this value. |
| sensitivityUnits | [in] | int32 | The units of sensitivity. NameDescriptionDAQmx_Val_mVoltsPerVoltPerDegreemvolts/volt/degreeDAQmx_Val_mVoltsPerVoltPerRadianmvolts/volt/radian |
| Name | Description |  |  |
| DAQmx_Val_mVoltsPerVoltPerDegree | mvolts/volt/degree |  |  |
| DAQmx_Val_mVoltsPerVoltPerRadian | mvolts/volt/radian |  |  |
| voltageExcitSource | [in] | int32 | The source of excitation. ValueDescriptionDAQmx_Val_InternalUse the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation.DAQmx_Val_ExternalUse an excitation source other than the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation.DAQmx_Val_NoneSupply no excitation to the channel. |
| Value | Description |  |  |
| DAQmx_Val_Internal | Use the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_External | Use an excitation source other than the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_None | Supply no excitation to the channel. |  |  |
| voltageExcitVal | [in] | float64 | Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values. |
| voltageExcitFreq | [in] | float64 | The excitation frequency, in hertz, that the sensor requires. Refer to the sensor documentation to determine this value. |
| ACExcitWireMode | [in] | int32 | The number of leads on the sensor. Some sensors may require you to tie leads together to create a 4-wire, 5-wire, or 6-wire sensor. Refer to the documentation for your sensor for more information. ValueDescriptionDAQmx_Val_4Wire4-wire.DAQmx_Val_5Wire5-wire.DAQmx_Val_6Wire6-wire. |
| Value | Description |  |  |
| DAQmx_Val_4Wire | 4-wire. |  |  |
| DAQmx_Val_5Wire | 5-wire. |  |  |
| DAQmx_Val_6Wire | 6-wire. |  |  |
| customScaleName | [in] | const char[] | The name of a custom scale to apply to the channel. To use this parameter, you must set units to DAQmx_Val_FromCustomScale. If you do not set units to DAQmx_Val_FromCustomScale, you must set customScaleName to NULL. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Position

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__output__channel.html language=enus -->
## TOPIC 00207: Create Analog Output Channel

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__output__channel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__output__channel.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxCreateAOCurrentChanDAQmxCreateAOFuncGenChanDAQmxCreateAOVoltageChanAttachmentsNone

### Create Analog Output Channel

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxCreateAOCurrentChan |  |
| DAQmxCreateAOFuncGenChan |  |
| DAQmxCreateAOVoltageChan |  |

#### Attachments

None

Parent topic:

Channel Configuration/Creation

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__output__channel_1ga7146d8ebdf2336e5200c4d2549f67494.html language=enus -->
## TOPIC 00208: DAQmxCreateAOFuncGenChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__output__channel_1ga7146d8ebdf2336e5200c4d2549f67494.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__analog__output__channel_1ga7146d8ebdf2336e5200c4d2549f67494.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateAOFuncGenChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], int32 type, float64 freq, float64 amplitude, float64 offset)RemarksCreates a channel for continually generating a waveform on the selected physical channel.Parameters

### DAQmxCreateAOFuncGenChan

#### Syntax

int32 __CFUNC DAQmxCreateAOFuncGenChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], int32 type, float64 freq, float64 amplitude, float64 offset)

#### Remarks

Creates a channel for continually generating a waveform on the selected physical channel.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| physicalChannel | [in] | const char[] | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| type | [in] | int32 | Specifies the kind of waveform to generate. ValueDescriptionDAQmx_Val_SineSine waveDAQmx_Val_TriangleTriangle waveDAQmx_Val_SquareSawtooth waveDAQmx_Val_SawtoothSquare wave |
| Value | Description |  |  |
| DAQmx_Val_Sine | Sine wave |  |  |
| DAQmx_Val_Triangle | Triangle wave |  |  |
| DAQmx_Val_Square | Sawtooth wave |  |  |
| DAQmx_Val_Sawtooth | Square wave |  |  |
| freq | [in] | float64 | The frequency of the waveform to generate in hertz. |
| amplitude | [in] | float64 | The zero-to-peak amplitude of the waveform to generate in volts. Zero and negative values are valid. |
| offset | [in] | float64 | The voltage offset of the waveform to generate. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Analog Output Channel

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels.html language=enus -->
## TOPIC 00209: Create Counter Input Channels

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsPositionTimestampGroup membersNameDescriptionDAQmxCreateCIAngVelocityChanDAQmxCreateCICountEdgesChanDAQmxCreateCIDutyCycleChanDAQmxCreateCIFreqChanDAQmxCreateCILinVelocityChanDAQmxCreateCIPeriodChanDAQmxCreateCIPulseChanFreqDAQmxCreateCIPulseChanTicksDAQmxCreateCIPulseChanTimeDAQmxCreateCIPuls

### Create Counter Input Channels

#### Groups

- Position
- Timestamp

#### Group members

| Name | Description |
| --- | --- |
| DAQmxCreateCIAngVelocityChan |  |
| DAQmxCreateCICountEdgesChan |  |
| DAQmxCreateCIDutyCycleChan |  |
| DAQmxCreateCIFreqChan |  |
| DAQmxCreateCILinVelocityChan |  |
| DAQmxCreateCIPeriodChan |  |
| DAQmxCreateCIPulseChanFreq |  |
| DAQmxCreateCIPulseChanTicks |  |
| DAQmxCreateCIPulseChanTime |  |
| DAQmxCreateCIPulseWidthChan |  |
| DAQmxCreateCISemiPeriodChan |  |
| DAQmxCreateCITwoEdgeSepChan |  |

#### Attachments

None

Parent topic:

Channel Configuration/Creation

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1ga1b268044956f769aa24ad4053e06abb6.html language=enus -->
## TOPIC 00210: DAQmxCreateCIPulseChanTime

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1ga1b268044956f769aa24ad4053e06abb6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1ga1b268044956f769aa24ad4053e06abb6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateCIPulseChanTime(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units)RemarksCreates a channel to measure pulse specifications, returning the measurements as pairs of high time and low time, and add

### DAQmxCreateCIPulseChanTime

#### Syntax

int32 __CFUNC DAQmxCreateCIPulseChanTime(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units)

#### Remarks

Creates a channel to measure [pulse specifications](/csh?context=nidaqmx_mxcncpts_configtimemeas), returning the measurements as pairs of high time and low time, and adds the channel to the task you specify with taskHandle. With the exception of devices that support [multi-counter tasks](/csh?context=nidaqmx_mxdevconsid_multicounterdevices), you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signal to the [default input terminal](/csh?context=nidaqmx_mxdevconsid_countersigcon) of the counter unless you select a different input terminal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| counter | [in] | const char[] | The name of the counter to use to create virtual channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | The units to use to return the measurement. ValueDescriptionDAQmx_Val_Secondsseconds |
| Value | Description |  |  |
| DAQmx_Val_Seconds | seconds |  |  |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Counter Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1ga3f788a83572647b0e2b1967bdebd1efe.html language=enus -->
## TOPIC 00211: DAQmxCreateCIPulseChanFreq

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1ga3f788a83572647b0e2b1967bdebd1efe.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1ga3f788a83572647b0e2b1967bdebd1efe.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateCIPulseChanFreq(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units)RemarksCreates a channel to measure pulse specifications, returning the measurements as pairs of frequency and duty cycle, and a

### DAQmxCreateCIPulseChanFreq

#### Syntax

int32 __CFUNC DAQmxCreateCIPulseChanFreq(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units)

#### Remarks

Creates a channel to measure [pulse specifications](/csh?context=nidaqmx_mxcncpts_configtimemeas), returning the measurements as pairs of frequency and duty cycle, and adds the channel to the task you specify with taskHandle. With the exception of devices that support [multi-counter tasks](/csh?context=nidaqmx_mxdevconsid_multicounterdevices), you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signal to the [default input terminal](/csh?context=nidaqmx_mxdevconsid_countersigcon) of the counter unless you select a different input terminal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| counter | [in] | const char[] | The name of the counter to use to create virtual channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | The units to use to return the measurement. ValueDescriptionDAQmx_Val_Hzhertz |
| Value | Description |  |  |
| DAQmx_Val_Hz | hertz |  |  |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Counter Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1ga48a4f962e8752504edea1a0de6e39c74.html language=enus -->
## TOPIC 00212: DAQmxCreateCITwoEdgeSepChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1ga48a4f962e8752504edea1a0de6e39c74.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1ga48a4f962e8752504edea1a0de6e39c74.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateCITwoEdgeSepChan(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 firstEdge, int32 secondEdge, const char customScaleName[])RemarksCreates a channel that measures the amount of time betw

### DAQmxCreateCITwoEdgeSepChan

#### Syntax

int32 __CFUNC DAQmxCreateCITwoEdgeSepChan(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 firstEdge, int32 secondEdge, const char customScaleName[])

#### Remarks

Creates a channel that measures the amount of time between the rising or falling edge of one digital signal and the rising or falling edge of another digital signal. With the exception of devices that support [multi-counter tasks](/csh?context=nidaqmx_mxdevconsid_multicounterdevices), you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signals to the [default input terminals](/csh?context=nidaqmx_mxdevconsid_countersigcon) of the counter unless you select different input terminals.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| counter | [in] | const char[] | The name of the counter to use to create virtual channels. |
| nameToAssignToChannel | [in] | const char[] | The name to assign to the created virtual channel. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | The units to use to return the measurement. ValueDescriptionDAQmx_Val_SecondssecondsDAQmx_Val_TicksTimebase ticksDAQmx_Val_FromCustomScaleUnits a custom scale specifies. Use customScaleName to specify a custom scale. |
| Value | Description |  |  |
| DAQmx_Val_Seconds | seconds |  |  |
| DAQmx_Val_Ticks | Timebase ticks |  |  |
| DAQmx_Val_FromCustomScale | Units a custom scale specifies. Use customScaleName to specify a custom scale. |  |  |
| firstEdge | [in] | int32 | Specifies on which edge of the first signal to start each measurement. NameDescriptionDAQmx_Val_RisingStart each measurement on the rising edge of the first signal.DAQmx_Val_FallingStart each measurement on the falling edge of the first signal. |
| Name | Description |  |  |
| DAQmx_Val_Rising | Start each measurement on the rising edge of the first signal. |  |  |
| DAQmx_Val_Falling | Start each measurement on the falling edge of the first signal. |  |  |
| secondEdge | [in] | int32 | Specifies on which edge of the first signal to stop each measurement. NameDescriptionDAQmx_Val_RisingStop each measurement on the rising edge of the second signal.DAQmx_Val_FallingStop each measurement on the falling edge of the second signal. |
| Name | Description |  |  |
| DAQmx_Val_Rising | Stop each measurement on the rising edge of the second signal. |  |  |
| DAQmx_Val_Falling | Stop each measurement on the falling edge of the second signal. |  |  |
| customScaleName | [in] | const char[] | The name of a custom scale to apply to the channel. To use this parameter, you must set units to DAQmx_Val_FromCustomScale. If you do not set units to DAQmx_Val_FromCustomScale, you must set customScaleName to NULL. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Counter Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1gaaaaf9ed914a601d29d918e317f0da5de.html language=enus -->
## TOPIC 00213: DAQmxCreateCIPulseChanTicks

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1gaaaaf9ed914a601d29d918e317f0da5de.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1gaaaaf9ed914a601d29d918e317f0da5de.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateCIPulseChanTicks(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], const char sourceTerminal[], float64 minVal, float64 maxVal)RemarksCreates a channel to measure pulse specifications, returning the measurements as pairs of high ticks and

### DAQmxCreateCIPulseChanTicks

#### Syntax

int32 __CFUNC DAQmxCreateCIPulseChanTicks(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], const char sourceTerminal[], float64 minVal, float64 maxVal)

#### Remarks

Creates a channel to measure [pulse specifications](/csh?context=nidaqmx_mxcncpts_configtimemeas), returning the measurements as pairs of high ticks and low ticks, and adds the channel to the task you specify with taskHandle. With the exception of devices that support [multi-counter tasks](/csh?context=nidaqmx_mxdevconsid_multicounterdevices), you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signal to the [default input terminal](/csh?context=nidaqmx_mxdevconsid_countersigcon) of the counter unless you select a different input terminal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| counter | [in] | const char[] | The name of the counter to use to create virtual channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| sourceTerminal | [in] | const char[] | The originating terminal of the route. You can specify a terminal name. |
| minVal | [in] | float64 | The minimum value that you expect to measure. |
| maxVal | [in] | float64 | The maximum value that you expect to measure. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Counter Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1gab7c2c214f995c0b0a065940d739b3168.html language=enus -->
## TOPIC 00214: DAQmxCreateCIPulseWidthChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1gab7c2c214f995c0b0a065940d739b3168.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1gab7c2c214f995c0b0a065940d739b3168.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateCIPulseWidthChan(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 startingEdge, const char customScaleName[])RemarksCreates a channel to measure the width of a digital pulse and adds the

### DAQmxCreateCIPulseWidthChan

#### Syntax

int32 __CFUNC DAQmxCreateCIPulseWidthChan(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 startingEdge, const char customScaleName[])

#### Remarks

Creates a channel to [measure the width of a digital pulse](/csh?context=nidaqmx_daqhelp_measperiod) and adds the channel to the task you specify with taskHandle. startingEdge determines whether to measure a high pulse or a low pulse. With the exception of devices that support [multi-counter tasks](/csh?context=nidaqmx_mxdevconsid_multicounterdevices), you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signal to the [default input terminal](/csh?context=nidaqmx_mxdevconsid_countersigcon) of the counter unless you select a different input terminal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| counter | [in] | const char[] | The name of the counter to use to create virtual channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | The units to use to return the measurement. ValueDescriptionDAQmx_Val_SecondssecondsDAQmx_Val_TicksTimebase ticksDAQmx_Val_FromCustomScaleUnits a custom scale specifies. Use customScaleName to specify a custom scale. |
| Value | Description |  |  |
| DAQmx_Val_Seconds | seconds |  |  |
| DAQmx_Val_Ticks | Timebase ticks |  |  |
| DAQmx_Val_FromCustomScale | Units a custom scale specifies. Use customScaleName to specify a custom scale. |  |  |
| startingEdge | [in] | int32 | Specifies on which edge to begin measuring pulse width. ValueDescriptionDAQmx_Val_RisingRising edge(s).DAQmx_Val_FallingFalling edge(s). |
| Value | Description |  |  |
| DAQmx_Val_Rising | Rising edge(s). |  |  |
| DAQmx_Val_Falling | Falling edge(s). |  |  |
| customScaleName | [in] | const char[] | The name of a custom scale to apply to the channel. To use this parameter, you must set units to DAQmx_Val_FromCustomScale. If you do not set units to DAQmx_Val_FromCustomScale, you must set customScaleName to NULL. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Counter Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1gad7f76a3c13cd1acceb5015cbb57c5743.html language=enus -->
## TOPIC 00215: DAQmxCreateCIFreqChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1gad7f76a3c13cd1acceb5015cbb57c5743.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1gad7f76a3c13cd1acceb5015cbb57c5743.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateCIFreqChan(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 edge, int32 measMethod, float64 measTime, uInt32 divisor, const char customScaleName[])RemarksCreates a channel to measure the

### DAQmxCreateCIFreqChan

#### Syntax

int32 __CFUNC DAQmxCreateCIFreqChan(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 edge, int32 measMethod, float64 measTime, uInt32 divisor, const char customScaleName[])

#### Remarks

Creates a channel to measure the frequency of a digital signal and adds the channel to the task you specify with taskHandle. With the exception of devices that support [multi-counter tasks](/csh?context=nidaqmx_mxdevconsid_multicounterdevices), you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signal to the [default input terminal](/csh?context=nidaqmx_mxdevconsid_countersigcon) of the counter unless you select a different input terminal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| counter | [in] | const char[] | The name of the counter to use to create virtual channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | The units to use to return the measurement. NameDescriptionDAQmx_Val_HzhertzDAQmx_Val_TicksTimebase ticksDAQmx_Val_FromCustomScaleUnits by a custom scale. Use customScaleName to specify a custom scale. |
| Name | Description |  |  |
| DAQmx_Val_Hz | hertz |  |  |
| DAQmx_Val_Ticks | Timebase ticks |  |  |
| DAQmx_Val_FromCustomScale | Units by a custom scale. Use customScaleName to specify a custom scale. |  |  |
| edge | [in] | int32 | Specifies between which edges to measure the frequency or period of the signal. ValueDescriptionDAQmx_Val_RisingRising edge(s).DAQmx_Val_FallingFalling edge(s). |
| Value | Description |  |  |
| DAQmx_Val_Rising | Rising edge(s). |  |  |
| DAQmx_Val_Falling | Falling edge(s). |  |  |
| measMethod | [in] | int32 | The method used to calculate the period or frequency of the signal. ValueDescriptionDAQmx_Val_LowFreq1CtrUse one counter that uses a constant timebase to measure the input signal.DAQmx_Val_HighFreq2CtrUse two counters, one of which counts pulses of the signal to measure during the specified measurement time.DAQmx_Val_LargeRng2CtrUse one counter to divide the frequency of the input signal to create a lower-frequency signal that the second counter can more easily measure.Caution Refer to Quantization Error in the NI-DAQmx Help to choose a measurement method that will limit error in the frequency measurement. |
| Value | Description |  |  |
| DAQmx_Val_LowFreq1Ctr | Use one counter that uses a constant timebase to measure the input signal. |  |  |
| DAQmx_Val_HighFreq2Ctr | Use two counters, one of which counts pulses of the signal to measure during the specified measurement time. |  |  |
| DAQmx_Val_LargeRng2Ctr | Use one counter to divide the frequency of the input signal to create a lower-frequency signal that the second counter can more easily measure. |  |  |
| Caution Refer to Quantization Error in the NI-DAQmx Help to choose a measurement method that will limit error in the frequency measurement. |  |  |  |
| measTime | [in] | float64 | The length of time to measure the frequency or period of a digital signal, when measMethod is DAQmx_Val_HighFreq2Ctr. Measurement accuracy increases with increased measurement time and with increased signal frequency. Caution If you measure a high-frequency signal for too long a time, the count register could roll over, resulting in an incorrect measurement. |
| Caution If you measure a high-frequency signal for too long a time, the count register could roll over, resulting in an incorrect measurement. |  |  |  |
| divisor | [in] | uInt32 | The value by which to divide the input signal, when measMethod is DAQmx_Val_LargeRng2Ctr. The larger this value, the more accurate the measurement, but too large a value can cause the count register to roll over, resulting in an incorrect measurement. |
| customScaleName | [in] | const char[] | The name of a custom scale to apply to the channel. To use this parameter, you must set units to DAQmx_Val_FromCustomScale. If you do not set units to DAQmx_Val_FromCustomScale, you must set customScaleName to NULL. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Counter Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1gafff33171661e94431afbd5a0abf4f73e.html language=enus -->
## TOPIC 00216: DAQmxCreateCIPeriodChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1gafff33171661e94431afbd5a0abf4f73e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels_1gafff33171661e94431afbd5a0abf4f73e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateCIPeriodChan(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 edge, int32 measMethod, float64 measTime, uInt32 divisor, const char customScaleName[])RemarksCreates a channel to measure t

### DAQmxCreateCIPeriodChan

#### Syntax

int32 __CFUNC DAQmxCreateCIPeriodChan(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 edge, int32 measMethod, float64 measTime, uInt32 divisor, const char customScaleName[])

#### Remarks

Creates a channel to measure the period of a digital signal and adds the channel to the task you specify with taskHandle. With the exception of devices that support [multi-counter tasks](/csh?context=nidaqmx_mxdevconsid_multicounterdevices), you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signal to the [default input terminal](/csh?context=nidaqmx_mxdevconsid_countersigcon) of the counter unless you select a different input terminal.

Note

When **measMethod** is set to DAQmx_Val_LowFreq1Ctr, you must pass the values 0.000001 for **measTime** and 4 for **divisor**. These values will be ignored by the function, but if they are not passed, the function returns an error.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| counter | [in] | const char[] | The name of the counter to use to create virtual channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | The units to use to return the measurement. ValueDescriptionDAQmx_Val_SecondssecondsDAQmx_Val_TicksTimebase ticksDAQmx_Val_FromCustomScaleUnits a custom scale specifies. Use customScaleName to specify a custom scale. |
| Value | Description |  |  |
| DAQmx_Val_Seconds | seconds |  |  |
| DAQmx_Val_Ticks | Timebase ticks |  |  |
| DAQmx_Val_FromCustomScale | Units a custom scale specifies. Use customScaleName to specify a custom scale. |  |  |
| edge | [in] | int32 | Specifies between which edges to measure the frequency or period of the signal. ValueDescriptionDAQmx_Val_RisingRising edge(s).DAQmx_Val_FallingFalling edge(s). |
| Value | Description |  |  |
| DAQmx_Val_Rising | Rising edge(s). |  |  |
| DAQmx_Val_Falling | Falling edge(s). |  |  |
| measMethod | [in] | int32 | Specifies the method used to calculate the frequency or period of the signal. ValueDescriptionDAQmx_Val_LowFreq1CtrUse one counter that uses a constant timebase to measure the input signal.DAQmx_Val_HighFreq2CtrUse two counters, one of which counts pulses of the signal to measure during the specified measurement time.DAQmx_Val_LargeRng2CtrUse one counter to divide the frequency of the input signal to create a lower-frequency signal that the second counter can more easily measure. |
| Value | Description |  |  |
| DAQmx_Val_LowFreq1Ctr | Use one counter that uses a constant timebase to measure the input signal. |  |  |
| DAQmx_Val_HighFreq2Ctr | Use two counters, one of which counts pulses of the signal to measure during the specified measurement time. |  |  |
| DAQmx_Val_LargeRng2Ctr | Use one counter to divide the frequency of the input signal to create a lower-frequency signal that the second counter can more easily measure. |  |  |
| measTime | [in] | float64 | The length of time to measure the frequency or period of a digital signal, when measMethod is DAQmx_Val_HighFreq2Ctr. Measurement accuracy increases with increased measurement time and with increased signal frequency. Caution If you measure a high-frequency signal for too long a time, the count register could roll over, resulting in an incorrect measurement. |
| Caution If you measure a high-frequency signal for too long a time, the count register could roll over, resulting in an incorrect measurement. |  |  |  |
| divisor | [in] | uInt32 | The value by which to divide the input signal, when measMethod is DAQmx_Val_LargeRng2Ctr. The larger this value, the more accurate the measurement, but too large a value can cause the count register to roll over, resulting in an incorrect measurement. |
| customScaleName | [in] | const char[] | The name of a custom scale to apply to the channel. To use this parameter, you must set units to DAQmx_Val_FromCustomScale. If you do not set units to DAQmx_Val_FromCustomScale, you must set customScaleName to NULL. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Counter Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels__timestamp_1ga5f6664f04165b991e3847362fdf164ee.html language=enus -->
## TOPIC 00217: DAQmxCreateCIGPSTimestampChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels__timestamp_1ga5f6664f04165b991e3847362fdf164ee.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__input__channels__timestamp_1ga5f6664f04165b991e3847362fdf164ee.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateCIGPSTimestampChan(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], int32 units, int32 syncMethod, const char customScaleName[])RemarksCreates a channel that uses a special-purpose counter to take a timestamp and synchronizes that counte

### DAQmxCreateCIGPSTimestampChan

#### Syntax

int32 __CFUNC DAQmxCreateCIGPSTimestampChan(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], int32 units, int32 syncMethod, const char customScaleName[])

#### Remarks

Creates a channel that uses a special-purpose counter to [take a timestamp](/csh?context=nidaqmx_daqhelp_gpsstampmeas) and synchronizes that counter to a GPS receiver. With the exception of devices that support [multi-counter tasks](/csh?context=nidaqmx_mxdevconsid_multicounterdevices), you can create only one counter input channel at a time with this function because a task can contain only one counter input channel. To read from multiple counters simultaneously, use a separate task for each counter. Connect the input signal to the [default input terminal](/csh?context=nidaqmx_mxdevconsid_countersigcon) of the counter unless you select a different input terminal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| counter | [in] | const char[] | The name of the counter to use to create virtual channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| units | [in] | int32 | The units to use to return the timestamp. ValueDescriptionDAQmx_Val_SecondsSecondsDAQmx_Val_FromCustomScaleFrom custom scale |
| Value | Description |  |  |
| DAQmx_Val_Seconds | Seconds |  |  |
| DAQmx_Val_FromCustomScale | From custom scale |  |  |
| syncMethod | [in] | int32 | The method to use to synchronize the counter to a GPS receiver. ValueDescriptionDAQmx_Val_IRIGBIRIG-BDAQmx_Val_PPSPPSDAQmx_Val_NoneNone |
| Value | Description |  |  |
| DAQmx_Val_IRIGB | IRIG-B |  |  |
| DAQmx_Val_PPS | PPS |  |  |
| DAQmx_Val_None | None |  |  |
| customScaleName | [in] | const char[] | The name of a custom scale to apply to the channel. To use this parameter, you must set units to DAQmx_Val_FromCustomScale. If you do not set units to DAQmx_Val_FromCustomScale, you must set customScaleName to NULL. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Timestamp

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__output__channels_1gacc3278b426ecd7b06a00a93a9886763b.html language=enus -->
## TOPIC 00218: DAQmxCreateCOPulseChanFreq

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__output__channels_1gacc3278b426ecd7b06a00a93a9886763b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__output__channels_1gacc3278b426ecd7b06a00a93a9886763b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateCOPulseChanFreq(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], int32 units, int32 idleState, float64 initialDelay, float64 freq, float64 dutyCycle)RemarksCreates channel(s) to generate digital pulses that freq and dutyCycle define and

### DAQmxCreateCOPulseChanFreq

#### Syntax

int32 __CFUNC DAQmxCreateCOPulseChanFreq(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], int32 units, int32 idleState, float64 initialDelay, float64 freq, float64 dutyCycle)

#### Remarks

Creates channel(s) to [generate digital pulses](/csh?context=nidaqmx_daqhelp_generating_pulses) that freq and dutyCycle define and adds the channel to the task you specify with taskHandle. The pulses appear on the [default output terminal](/csh?context=nidaqmx_mxdevconsid_countersigcon) of the counter unless you select a different output terminal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| counter | [in] | const char[] | The name of the counter to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| units | [in] | int32 | The units in which to specify freq. NameDescriptionDAQmx_Val_Hzhertz |
| Name | Description |  |  |
| DAQmx_Val_Hz | hertz |  |  |
| idleState | [in] | int32 | The resting state of the output terminal. ValueDescriptionDAQmx_Val_HighHigh state.DAQmx_Val_LowLow state. |
| Value | Description |  |  |
| DAQmx_Val_High | High state. |  |  |
| DAQmx_Val_Low | Low state. |  |  |
| initialDelay | [in] | float64 | The amount of time in seconds to wait before generating the first pulse. |
| freq | [in] | float64 | The frequency at which to generate pulses. |
| dutyCycle | [in] | float64 | The width of the pulse divided by the pulse period. NI-DAQmx uses this ratio, combined with frequency, to determine pulse width and the interval between pulses. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Counter Output Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__output__channels_1gaf8f808683006d2892544be671ad82fcb.html language=enus -->
## TOPIC 00219: DAQmxCreateCOPulseChanTime

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__output__channels_1gaf8f808683006d2892544be671ad82fcb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__counter__output__channels_1gaf8f808683006d2892544be671ad82fcb.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateCOPulseChanTime(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], int32 units, int32 idleState, float64 initialDelay, float64 lowTime, float64 highTime)RemarksCreates channel(s) to generate digital pulses defined by the amount of time the

### DAQmxCreateCOPulseChanTime

#### Syntax

int32 __CFUNC DAQmxCreateCOPulseChanTime(TaskHandle taskHandle, const char counter[], const char nameToAssignToChannel[], int32 units, int32 idleState, float64 initialDelay, float64 lowTime, float64 highTime)

#### Remarks

Creates channel(s) to [generate digital pulses](/csh?context=nidaqmx_daqhelp_generating_pulses) defined by the amount of time the pulse is at a high state and the amount of time the pulse is at a low state and adds the channel to the task you specify with taskHandle. The pulses appear on the [default output terminal](/csh?context=nidaqmx_mxdevconsid_countersigcon) of the counter unless you select a different output terminal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| counter | [in] | const char[] | The name of the counter to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| units | [in] | int32 | The units in which to define pulse high and low time. ValueDescriptionDAQmx_Val_SecondsSeconds |
| Value | Description |  |  |
| DAQmx_Val_Seconds | Seconds |  |  |
| idleState | [in] | int32 | The resting state of the output terminal. ValueDescriptionDAQmx_Val_HighHigh state.DAQmx_Val_LowLow state. |
| Value | Description |  |  |
| DAQmx_Val_High | High state. |  |  |
| DAQmx_Val_Low | Low state. |  |  |
| initialDelay | [in] | float64 | The amount of time in seconds to wait before generating the first pulse. |
| lowTime | [in] | float64 | The amount of time the pulse is low, in seconds. |
| highTime | [in] | float64 | The amount of time the pulse is high, in seconds. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Counter Output Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__digital__input__channels.html language=enus -->
## TOPIC 00220: Create Digital Input Channels

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__digital__input__channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__digital__input__channels.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxCreateDIChanAttachmentsNone

### Create Digital Input Channels

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxCreateDIChan |  |

#### Attachments

None

Parent topic:

Channel Configuration/Creation

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__digital__input__channels_1ga3325b4a3660e51e9d6631460bab3ed94.html language=enus -->
## TOPIC 00221: DAQmxCreateDIChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__digital__input__channels_1ga3325b4a3660e51e9d6631460bab3ed94.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__digital__input__channels_1ga3325b4a3660e51e9d6631460bab3ed94.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateDIChan(TaskHandle taskHandle, const char lines[], const char nameToAssignToLines[], int32 lineGrouping)RemarksCreates channel(s) to measure digital signals and adds the channel(s) to the task you specify with taskHandle. You can group digital lines into one digital cha

### DAQmxCreateDIChan

#### Syntax

int32 __CFUNC DAQmxCreateDIChan(TaskHandle taskHandle, const char lines[], const char nameToAssignToLines[], int32 lineGrouping)

#### Remarks

Creates channel(s) to measure digital signals and adds the channel(s) to the task you specify with taskHandle. You can group digital [lines](/csh?context=nidaqmx_mxcncpts_linesports) into one [digital channel](/csh?context=nidaqmx_mxcncpts_virtchantypes) or separate them into multiple digital channels. If you specify one or more entire [ports](/csh?context=nidaqmx_mxcncpts_linesports) in lines by using port physical channel names, you cannot separate the ports into multiple channels. To separate ports into multiple channels, use this function multiple times with a different port each time.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| lines | [in] | const char[] | The names of the digital lines used to create a virtual channel. You can specify a list or range of lines. Specifying a port and no lines is the equivalent of specifying all the lines of that port in order. Therefore, if you specify Dev1/port0 and port 0 has eight lines, this is expanded to Dev1/port0/line0:7. |
| nameToAssignToLines | [in] | const char[] | The name of the created virtual channel(s). If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToLines, you must use the names when you refer to these channels in other NI-DAQmx functions. |
| lineGrouping | [in] | int32 | Specifies whether to group digital lines into one or more virtual channels. If you specify one or more entire ports in lines, you must set lineGrouping to DAQmx_Val_ChanForAllLines. ValueDescriptionDAQmx_Val_ChanPerLineOne channel for each lineDAQmx_Val_ChanForAllLinesOne channel for all lines |
| Value | Description |  |  |
| DAQmx_Val_ChanPerLine | One channel for each line |  |  |
| DAQmx_Val_ChanForAllLines | One channel for all lines |  |  |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create Digital Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__digital__output__channels.html language=enus -->
## TOPIC 00222: Create Digital Output Channels

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__digital__output__channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__digital__output__channels.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxCreateDOChanAttachmentsNone

### Create Digital Output Channels

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxCreateDOChan |  |

#### Attachments

None

Parent topic:

Channel Configuration/Creation

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__teds__analog__input__channels_1ga63269c7483b27ff014c57d7fcb9519b9.html language=enus -->
## TOPIC 00223: DAQmxCreateTEDSAIBridgeChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__teds__analog__input__channels_1ga63269c7483b27ff014c57d7fcb9519b9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__teds__analog__input__channels_1ga63269c7483b27ff014c57d7fcb9519b9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateTEDSAIBridgeChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 voltageExcitSource, float64 voltageExcitVal, const char customScaleName[])RemarksCreates a channel that measures

### DAQmxCreateTEDSAIBridgeChan

#### Syntax

int32 __CFUNC DAQmxCreateTEDSAIBridgeChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 voltageExcitSource, float64 voltageExcitVal, const char customScaleName[])

#### Remarks

Creates a channel that measures [voltage ratios](/csh?context=nidaqmx_measfunds_bridgescaling) from a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque). You must configure the physical channel(s) with TEDS information to use this function. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task to which to add the channels that this function creates. |
| physicalChannel | [in] | const char[] | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | Specifies in which unit to return measurements from the channel. NameDescriptionDAQmx_Val_FromTEDSUnits defined by TEDS information associated with the channel.DAQmx_Val_FromCustomScaleUnits a custom scale specifies. Use customScaleName to specify a custom scale. |
| Name | Description |  |  |
| DAQmx_Val_FromTEDS | Units defined by TEDS information associated with the channel. |  |  |
| DAQmx_Val_FromCustomScale | Units a custom scale specifies. Use customScaleName to specify a custom scale. |  |  |
| voltageExcitSource | [in] | int32 | The source of excitation. ValueDescriptionDAQmx_Val_InternalUse the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation.DAQmx_Val_ExternalUse an excitation source other than the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation.DAQmx_Val_NoneSupply no excitation to the channel. |
| Value | Description |  |  |
| DAQmx_Val_Internal | Use the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_External | Use an excitation source other than the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_None | Supply no excitation to the channel. |  |  |
| voltageExcitVal | [in] | float64 | Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values. |
| customScaleName | [in] | const char[] | The name of a custom scale to apply to the channel. To use this parameter, you must set units to DAQmx_Val_FromCustomScale. If you do not set units to DAQmx_Val_FromCustomScale, you must set customScaleName to NULL. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create TEDS Analog Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__teds__analog__input__channels_1ga747266781567da92fc4019020d75c891.html language=enus -->
## TOPIC 00224: DAQmxCreateTEDSAIThrmstrChanIex

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__teds__analog__input__channels_1ga747266781567da92fc4019020d75c891.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__teds__analog__input__channels_1ga747266781567da92fc4019020d75c891.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateTEDSAIThrmstrChanIex(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 resistanceConfig, int32 currentExcitSource, float64 currentExcitVal)RemarksCreates channel(s) that use a the

### DAQmxCreateTEDSAIThrmstrChanIex

#### Syntax

int32 __CFUNC DAQmxCreateTEDSAIThrmstrChanIex(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 resistanceConfig, int32 currentExcitSource, float64 currentExcitVal)

#### Remarks

Creates channel(s) that use a [thermistor](/csh?context=nidaqmx_measfunds_thermistors) to [measure temperature](/csh?context=nidaqmx_daqhelp_simtemp) and adds the channel(s) to the [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) you specify with taskHandle. Use this instance when the thermistor requires current excitation. You must configure the physical channel(s) with TEDS information to use this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task used in this function. |
| physicalChannel | [in] | const char[] | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | The units to use to return the measurement. NameDescriptionDAQmx_Val_DegCdegrees CelsiusDAQmx_Val_DegFdegrees FahrenheitDAQmx_Val_KelvinskelvinsDAQmx_Val_DegRdegrees Rankine |
| Name | Description |  |  |
| DAQmx_Val_DegC | degrees Celsius |  |  |
| DAQmx_Val_DegF | degrees Fahrenheit |  |  |
| DAQmx_Val_Kelvins | kelvins |  |  |
| DAQmx_Val_DegR | degrees Rankine |  |  |
| resistanceConfig | [in] | int32 | The configuration for resistance measurements. ValueDescriptionDAQmx_Val_2Wire2-wire mode.DAQmx_Val_3Wire3-wire mode.DAQmx_Val_4Wire4-wire mode. |
| Value | Description |  |  |
| DAQmx_Val_2Wire | 2-wire mode. |  |  |
| DAQmx_Val_3Wire | 3-wire mode. |  |  |
| DAQmx_Val_4Wire | 4-wire mode. |  |  |
| currentExcitSource | [in] | int32 | The source of excitation. ValueDescriptionDAQmx_Val_InternalUse the built-in excitation source of the device. You must use currentExcitVal to specify the amount of excitation.DAQmx_Val_ExternalUse an excitation source other than the built-in excitation source of the device. You must use currentExcitVal to specify the amount of excitation.DAQmx_Val_NoneSupply no excitation to the channel. You cannot use this value if the sensor requires excitation. |
| Value | Description |  |  |
| DAQmx_Val_Internal | Use the built-in excitation source of the device. You must use currentExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_External | Use an excitation source other than the built-in excitation source of the device. You must use currentExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_None | Supply no excitation to the channel. You cannot use this value if the sensor requires excitation. |  |  |
| currentExcitVal | [in] | float64 | The amount of excitation, in amperes, that the sensor requires. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create TEDS Analog Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__teds__analog__input__channels_1ga871832ae1a243ab377f7a1bdde60670f.html language=enus -->
## TOPIC 00225: DAQmxCreateTEDSAIAccelChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__teds__analog__input__channels_1ga871832ae1a243ab377f7a1bdde60670f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__teds__analog__input__channels_1ga871832ae1a243ab377f7a1bdde60670f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateTEDSAIAccelChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, int32 currentExcitSource, float64 currentExcitVal, const char customScaleName[])RemarksCreates ch

### DAQmxCreateTEDSAIAccelChan

#### Syntax

int32 __CFUNC DAQmxCreateTEDSAIAccelChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], int32 terminalConfig, float64 minVal, float64 maxVal, int32 units, int32 currentExcitSource, float64 currentExcitVal, const char customScaleName[])

#### Remarks

Creates channel(s) that use an [accelerometer](/csh?context=nidaqmx_measfunds_accelerometers) to [measure acceleration](/csh?context=nidaqmx_daqhelp_accel) and adds the channel(s) to the [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) you specify with taskHandle. You must configure the physical channel(s) with TEDS information to use this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task used in this function. |
| physicalChannel | [in] | const char[] | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| terminalConfig | [in] | int32 | The input terminal configuration for the channel. ValueDescriptionDAQmx_Val_Cfg_DefaultAt run time, NI-DAQmx chooses the default terminal configuration for the channel.DAQmx_Val_RSEReferenced single-ended modeDAQmx_Val_NRSENon-referenced single-ended modeDAQmx_Val_DiffDifferential modeDAQmx_Val_PseudoDiffPseudodifferential mode |
| Value | Description |  |  |
| DAQmx_Val_Cfg_Default | At run time, NI-DAQmx chooses the default terminal configuration for the channel. |  |  |
| DAQmx_Val_RSE | Referenced single-ended mode |  |  |
| DAQmx_Val_NRSE | Non-referenced single-ended mode |  |  |
| DAQmx_Val_Diff | Differential mode |  |  |
| DAQmx_Val_PseudoDiff | Pseudodifferential mode |  |  |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | The units to use to return acceleration measurements from the channel. NameDescriptionDAQmx_Val_AccelUnit_gG-force (g). 1 g is approximately equal to 9.81 m/s2.DAQmx_Val_FromCustomScaleUnits specified by a custom scale. Use customScaleName to specify a custom scale. |
| Name | Description |  |  |
| DAQmx_Val_AccelUnit_g | G-force (g). 1 g is approximately equal to 9.81 m/s2. |  |  |
| DAQmx_Val_FromCustomScale | Units specified by a custom scale. Use customScaleName to specify a custom scale. |  |  |
| currentExcitSource | [in] | int32 | The source of excitation. ValueDescriptionDAQmx_Val_InternalUse the built-in excitation source of the device. You must use currentExcitVal to specify the amount of excitation.DAQmx_Val_ExternalUse an excitation source other than the built-in excitation source of the device. You must use currentExcitVal to specify the amount of excitation.DAQmx_Val_NoneSupply no excitation to the channel. You cannot use this value if the sensor requires excitation. |
| Value | Description |  |  |
| DAQmx_Val_Internal | Use the built-in excitation source of the device. You must use currentExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_External | Use an excitation source other than the built-in excitation source of the device. You must use currentExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_None | Supply no excitation to the channel. You cannot use this value if the sensor requires excitation. |  |  |
| currentExcitVal | [in] | float64 | The amount of excitation, in amperes, that the sensor requires. |
| customScaleName | [in] | const char[] | The name of a custom scale to apply to the channel. To use this parameter, you must set units to DAQmx_Val_FromCustomScale. If you do not set units to DAQmx_Val_FromCustomScale, you must set customScaleName to NULL. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create TEDS Analog Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__teds__analog__input__channels_1ga88de7a03a874dc710f4e86ec739ae37a.html language=enus -->
## TOPIC 00226: DAQmxCreateTEDSAIThrmstrChanVex

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__teds__analog__input__channels_1ga88de7a03a874dc710f4e86ec739ae37a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__teds__analog__input__channels_1ga88de7a03a874dc710f4e86ec739ae37a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateTEDSAIThrmstrChanVex(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 resistanceConfig, int32 voltageExcitSource, float64 voltageExcitVal, float64 r1)RemarksCreates channel(s) th

### DAQmxCreateTEDSAIThrmstrChanVex

#### Syntax

int32 __CFUNC DAQmxCreateTEDSAIThrmstrChanVex(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 resistanceConfig, int32 voltageExcitSource, float64 voltageExcitVal, float64 r1)

#### Remarks

Creates channel(s) that use a [thermistor](/csh?context=nidaqmx_measfunds_thermistors) to [measure temperature](/csh?context=nidaqmx_daqhelp_simtemp) and adds the channel(s) to the [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) you specify with taskHandle. Use this instance when the thermistor requires voltage excitation. You must configure the physical channel(s) with TEDS information to use this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task used in this function. |
| physicalChannel | [in] | const char[] | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | The units to use to return the measurement. NameDescriptionDAQmx_Val_DegCdegrees CelsiusDAQmx_Val_DegFdegrees FahrenheitDAQmx_Val_KelvinskelvinsDAQmx_Val_DegRdegrees Rankine |
| Name | Description |  |  |
| DAQmx_Val_DegC | degrees Celsius |  |  |
| DAQmx_Val_DegF | degrees Fahrenheit |  |  |
| DAQmx_Val_Kelvins | kelvins |  |  |
| DAQmx_Val_DegR | degrees Rankine |  |  |
| resistanceConfig | [in] | int32 | The configuration for resistance measurements. ValueDescriptionDAQmx_Val_2Wire2-wire mode.DAQmx_Val_3Wire3-wire mode.DAQmx_Val_4Wire4-wire mode. |
| Value | Description |  |  |
| DAQmx_Val_2Wire | 2-wire mode. |  |  |
| DAQmx_Val_3Wire | 3-wire mode. |  |  |
| DAQmx_Val_4Wire | 4-wire mode. |  |  |
| voltageExcitSource | [in] | int32 | The source of excitation. ValueDescriptionDAQmx_Val_InternalUse the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation.DAQmx_Val_ExternalUse an excitation source other than the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation.DAQmx_Val_NoneSupply no excitation to the channel. |
| Value | Description |  |  |
| DAQmx_Val_Internal | Use the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_External | Use an excitation source other than the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_None | Supply no excitation to the channel. |  |  |
| voltageExcitVal | [in] | float64 | Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values. |
| r1 | [in] | float64 | The value, in ohms, of the reference resistor. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Create TEDS Analog Input Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__channel__configuration__creation__create__teds__analog__input__channels__position_1ga16d5e2f5f6f163646fc79a39fa61e9e3.html language=enus -->
## TOPIC 00227: DAQmxCreateTEDSAIPosLVDTChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__channel__configuration__creation__create__teds__analog__input__channels__position_1ga16d5e2f5f6f163646fc79a39fa61e9e3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__channel__configuration__creation__create__teds__analog__input__channels__position_1ga16d5e2f5f6f163646fc79a39fa61e9e3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxCreateTEDSAIPosLVDTChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 voltageExcitSource, float64 voltageExcitVal, float64 voltageExcitFreq, int32 ACExcitWireMode, const char custom

### DAQmxCreateTEDSAIPosLVDTChan

#### Syntax

int32 __CFUNC DAQmxCreateTEDSAIPosLVDTChan(TaskHandle taskHandle, const char physicalChannel[], const char nameToAssignToChannel[], float64 minVal, float64 maxVal, int32 units, int32 voltageExcitSource, float64 voltageExcitVal, float64 voltageExcitFreq, int32 ACExcitWireMode, const char customScaleName[])

#### Remarks

Creates channel(s) that use an [LVDT](/csh?context=nidaqmx_measfunds_lvdts) to [measure linear position](/csh?context=nidaqmx_daqhelp_lindisplacelvdt) and adds the channel(s) to the [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) you specify with taskHandle. You must configure the physical channel(s) with TEDS information to use this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task used in this function. |
| physicalChannel | [in] | const char[] | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignToChannel | [in] | const char[] | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, you can specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels. |
| minVal | [in] | float64 | The minimum value, in units, that you expect to measure. |
| maxVal | [in] | float64 | The maximum value, in units, that you expect to measure. |
| units | [in] | int32 | The units to use to return linear position measurements from the channel. NameDescriptionDAQmx_Val_MetersMetersDAQmx_Val_InchesInchesDAQmx_Val_FromCustomScaleUnits a custom scale specifies. Use customScaleName to specify a custom scale. |
| Name | Description |  |  |
| DAQmx_Val_Meters | Meters |  |  |
| DAQmx_Val_Inches | Inches |  |  |
| DAQmx_Val_FromCustomScale | Units a custom scale specifies. Use customScaleName to specify a custom scale. |  |  |
| voltageExcitSource | [in] | int32 | The source of excitation. ValueDescriptionDAQmx_Val_InternalUse the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation.DAQmx_Val_ExternalUse an excitation source other than the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation.DAQmx_Val_NoneSupply no excitation to the channel. |
| Value | Description |  |  |
| DAQmx_Val_Internal | Use the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_External | Use an excitation source other than the built-in excitation source of the device. If you select this value, you must use voltageExcitVal to specify the amount of excitation. |  |  |
| DAQmx_Val_None | Supply no excitation to the channel. |  |  |
| voltageExcitVal | [in] | float64 | Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values. |
| voltageExcitFreq | [in] | float64 | The excitation frequency, in hertz, that the sensor requires. Refer to the sensor documentation to determine this value. |
| ACExcitWireMode | [in] | int32 | The number of leads on the sensor. Some sensors may require you to tie leads together to create a 4-wire, 5-wire, or 6-wire sensor. Refer to the documentation for your sensor for more information. ValueDescriptionDAQmx_Val_4Wire4-wire.DAQmx_Val_5Wire5-wire.DAQmx_Val_6Wire6-wire. |
| Value | Description |  |  |
| DAQmx_Val_4Wire | 4-wire. |  |  |
| DAQmx_Val_5Wire | 5-wire. |  |  |
| DAQmx_Val_6Wire | 6-wire. |  |  |
| customScaleName | [in] | const char[] | The name of a custom scale to apply to the channel. To use this parameter, you must set units to DAQmx_Val_FromCustomScale. If you do not set units to DAQmx_Val_FromCustomScale, you must set customScaleName to NULL. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Position

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__error__handling.html language=enus -->
## TOPIC 00228: Error Handling

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__error__handling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__error__handling.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxGetErrorStringDAQmxGetExtendedErrorInfoAttachmentsNone

### Error Handling

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxGetErrorString |  |
| DAQmxGetExtendedErrorInfo |  |

#### Attachments

None

Parent topic:

NI-DAQmx C Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__error__handling_1ga3aab3885d2e6c3643dfd479fbf55692c.html language=enus -->
## TOPIC 00229: DAQmxGetErrorString

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__error__handling_1ga3aab3885d2e6c3643dfd479fbf55692c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__error__handling_1ga3aab3885d2e6c3643dfd479fbf55692c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetErrorString(int32 errorCode, char errorString[], uInt32 bufferSize)RemarksConverts the error number returned by an NI-DAQmx function into a meaningful error message. If you pass in a valid value for errorString and its bufferSize, this function returns as much of the avai

### DAQmxGetErrorString

#### Syntax

int32 __CFUNC DAQmxGetErrorString(int32 errorCode, char errorString[], uInt32 bufferSize)

#### Remarks

Converts the error number returned by an NI-DAQmx function into a meaningful error message. If you pass in a valid value for **errorString** and its **bufferSize**, this function returns as much of the available data as possible. If you pass NULL for **errorString** or 0 for **bufferSize**, this function returns the number of bytes you need to allocate.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| errorCode | [in] | int32 | An error code or warning returned by one of the NI-DAQmx Library functions. |
| bufferSize | [in] | uInt32 | The size, in bytes, of the buffer passed in the errorString. If you pass 0, this function returns the number of bytes you need to allocate. |
| errorString | [out] | char[] | The meaningful error message for the error number. If you pass NULL, this function returns the number of bytes you need to allocate. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A negative value indicates an error. If you pass in a valid value for **errorString** and its **bufferSize**, this function returns as much of the available data as possible. If you pass NULL for **errorString** or 0 for **bufferSize**, this function returns the number of bytes you need to allocate.

Parent topic:

Error Handling

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__export__hw__signals_1ga8132f06a11aa4934db7ab8856121caf7.html language=enus -->
## TOPIC 00230: DAQmxExportSignal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__export__hw__signals_1ga8132f06a11aa4934db7ab8856121caf7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__export__hw__signals_1ga8132f06a11aa4934db7ab8856121caf7.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxExportSignal(TaskHandle taskHandle, int32 signalID, const char outputTerminal[])RemarksRoutes a control signal to the specified terminal. The output terminal can reside on the device that generates the control signal or on a different device. Use this function to share clock

### DAQmxExportSignal

#### Syntax

int32 __CFUNC DAQmxExportSignal(TaskHandle taskHandle, int32 signalID, const char outputTerminal[])

#### Remarks

Routes a [control signal](/csh?context=nidaqmx_mxcncpts_timetrig) to the specified [terminal](/csh?context=nidaqmx_mxcncpts_termnames). The output terminal can reside on the device that generates the control signal or on a different device. Use this function to share clocks and triggers between multiple tasks and devices. The routes created by this function are [task-based routes](/csh?context=nidaqmx_mxcncpts_taskbasedrouting).

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| taskHandle | [in] | TaskHandle | The task used in this function. |
| signalID | [in] | int32 | The name of the trigger, clock, or event to export. ValueDescriptionDAQmx_Val_AIConvertClockClock that causes an analog-to-digital conversion on an E Series or M Series device. One conversion corresponds to a single sample from one channel.DAQmx_Val_10MHzRefClockOutput of an oscillator that you can use to synchronize multiple devices.DAQmx_Val_20MHzTimebaseClockOutput of an oscillator that is the onboard source of the Master Timebase. Other timebases are derived from this clock.DAQmx_Val_SampleClockClock the device uses to time each sample.DAQmx_Val_AdvanceTriggerTrigger that moves a switch to the next entry in a scan list.DAQmx_Val_ReferenceTriggerTrigger that establishes the reference point between pretrigger and posttrigger samples.DAQmx_Val_StartTriggerTrigger that begins a measurement or generation.DAQmx_Val_AdvCmpltEventSignal that a switch product generates after it both executes the command(s) in a scan list entry and waits for the settling time to elapse.DAQmx_Val_AIHoldCmpltEventSignal that an E Series or M Series device generates when the device latches analog input data (the ADC enters "hold" mode) and it is safe for any external switching hardware to remove the signal and replace it with the next signal. This event does not indicate the completion of the actual analog-to-digital conversion.DAQmx_Val_CounterOutputEventSignal that a counter generates. Each time the counter reaches terminal count, this signal toggles or pulses.DAQmx_Val_ChangeDetectionEventSignal that a static DIO device generates when the device detects a rising or falling edge on any of the lines or ports you selected when you configured change detection timing.DAQmx_Val_WDTExpiredEventSignal that a static DIO device generates when the watchdog timer expires. |
| Value | Description |  |  |
| DAQmx_Val_AIConvertClock | Clock that causes an analog-to-digital conversion on an E Series or M Series device. One conversion corresponds to a single sample from one channel. |  |  |
| DAQmx_Val_10MHzRefClock | Output of an oscillator that you can use to synchronize multiple devices. |  |  |
| DAQmx_Val_20MHzTimebaseClock | Output of an oscillator that is the onboard source of the Master Timebase. Other timebases are derived from this clock. |  |  |
| DAQmx_Val_SampleClock | Clock the device uses to time each sample. |  |  |
| DAQmx_Val_AdvanceTrigger | Trigger that moves a switch to the next entry in a scan list. |  |  |
| DAQmx_Val_ReferenceTrigger | Trigger that establishes the reference point between pretrigger and posttrigger samples. |  |  |
| DAQmx_Val_StartTrigger | Trigger that begins a measurement or generation. |  |  |
| DAQmx_Val_AdvCmpltEvent | Signal that a switch product generates after it both executes the command(s) in a scan list entry and waits for the settling time to elapse. |  |  |
| DAQmx_Val_AIHoldCmpltEvent | Signal that an E Series or M Series device generates when the device latches analog input data (the ADC enters "hold" mode) and it is safe for any external switching hardware to remove the signal and replace it with the next signal. This event does not indicate the completion of the actual analog-to-digital conversion. |  |  |
| DAQmx_Val_CounterOutputEvent | Signal that a counter generates. Each time the counter reaches terminal count, this signal toggles or pulses. |  |  |
| DAQmx_Val_ChangeDetectionEvent | Signal that a static DIO device generates when the device detects a rising or falling edge on any of the lines or ports you selected when you configured change detection timing. |  |  |
| DAQmx_Val_WDTExpiredEvent | Signal that a static DIO device generates when the watchdog timer expires. |  |  |
| outputTerminal | [in] | const char[] | The destination terminal of the exported signal. You can specify a string containing a comma-delimited list of terminal names. |

#### Returns

The error code returned by the function in the event of an error or warning. A value of 0 indicates success. A positive value indicates a warning. A negative value indicates an error.

Parent topic:

Export HW Signals

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter.html language=enus -->
## TOPIC 00231: Getter functions for attributes

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmxGetAIACExcitFreqDAQmxGetAIACExcitSyncEnableDAQmxGetAIACExcitWireModeDAQmxGetAIADCCustomTimingModeDAQmxGetAIADCTimingModeDAQmxGetAIAccel4WireDCVoltageSensitivityDAQmxGetAIAccel4WireDCVoltageSensitivityUnitsDAQmxGetAIAccelChargeSensitivityDAQmxGetAIAccelCharg

### Getter functions for attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmxGetAIACExcitFreq |  |
| DAQmxGetAIACExcitSyncEnable |  |
| DAQmxGetAIACExcitWireMode |  |
| DAQmxGetAIADCCustomTimingMode |  |
| DAQmxGetAIADCTimingMode |  |
| DAQmxGetAIAccel4WireDCVoltageSensitivity |  |
| DAQmxGetAIAccel4WireDCVoltageSensitivityUnits |  |
| DAQmxGetAIAccelChargeSensitivity |  |
| DAQmxGetAIAccelChargeSensitivityUnits |  |
| DAQmxGetAIAccelSensitivity |  |
| DAQmxGetAIAccelSensitivityUnits |  |
| DAQmxGetAIAccelUnits |  |
| DAQmxGetAIAcceldBRef |  |
| DAQmxGetAIAtten |  |
| DAQmxGetAIAutoZeroMode |  |
| DAQmxGetAIAveragingWinSize |  |
| DAQmxGetAIBridgeBalanceCoarsePot |  |
| DAQmxGetAIBridgeBalanceFinePot |  |
| DAQmxGetAIBridgeCfg |  |
| DAQmxGetAIBridgeElectricalUnits |  |
| DAQmxGetAIBridgeInitialRatio |  |
| DAQmxGetAIBridgeInitialVoltage |  |
| DAQmxGetAIBridgeNomResistance |  |
| DAQmxGetAIBridgePhysicalUnits |  |
| DAQmxGetAIBridgePolyForwardCoeff |  |
| DAQmxGetAIBridgePolyReverseCoeff |  |
| DAQmxGetAIBridgeScaleType |  |
| DAQmxGetAIBridgeShuntCalEnable |  |
| DAQmxGetAIBridgeShuntCalGainAdjust |  |
| DAQmxGetAIBridgeShuntCalSelect |  |
| DAQmxGetAIBridgeShuntCalShuntCalAActualResistance |  |
| DAQmxGetAIBridgeShuntCalShuntCalAResistance |  |
| DAQmxGetAIBridgeShuntCalShuntCalASrc |  |
| DAQmxGetAIBridgeShuntCalShuntCalBActualResistance |  |
| DAQmxGetAIBridgeShuntCalShuntCalBResistance |  |
| DAQmxGetAIBridgeTableElectricalVals |  |
| DAQmxGetAIBridgeTablePhysicalVals |  |
| DAQmxGetAIBridgeTwoPointLinFirstElectricalVal |  |
| DAQmxGetAIBridgeTwoPointLinFirstPhysicalVal |  |
| DAQmxGetAIBridgeTwoPointLinSecondElectricalVal |  |
| DAQmxGetAIBridgeTwoPointLinSecondPhysicalVal |  |
| DAQmxGetAIBridgeUnits |  |
| DAQmxGetAICalculatedPowerCurrentMax |  |
| DAQmxGetAICalculatedPowerCurrentMin |  |
| DAQmxGetAICalculatedPowerVoltageMax |  |
| DAQmxGetAICalculatedPowerVoltageMin |  |
| DAQmxGetAIChanCalApplyCalIfExp |  |
| DAQmxGetAIChanCalDesc |  |
| DAQmxGetAIChanCalEnableCal |  |
| DAQmxGetAIChanCalHasValidCalInfo |  |
| DAQmxGetAIChanCalOperatorName |  |
| DAQmxGetAIChanCalPolyForwardCoeff |  |
| DAQmxGetAIChanCalPolyReverseCoeff |  |
| DAQmxGetAIChanCalScaleType |  |
| DAQmxGetAIChanCalTablePreScaledVals |  |
| DAQmxGetAIChanCalTableScaledVals |  |
| DAQmxGetAIChanCalVerifAcqVals |  |
| DAQmxGetAIChanCalVerifRefVals |  |
| DAQmxGetAIChargeUnits |  |
| DAQmxGetAIChopEnable |  |
| DAQmxGetAIConvActiveEdge |  |
| DAQmxGetAIConvActiveEdgeEx |  |
| DAQmxGetAIConvDigFltrEnable |  |
| DAQmxGetAIConvDigFltrEnableEx |  |
| DAQmxGetAIConvDigFltrMinPulseWidth |  |
| DAQmxGetAIConvDigFltrMinPulseWidthEx |  |
| DAQmxGetAIConvDigFltrTimebaseRate |  |
| DAQmxGetAIConvDigFltrTimebaseRateEx |  |
| DAQmxGetAIConvDigFltrTimebaseSrc |  |
| DAQmxGetAIConvDigFltrTimebaseSrcEx |  |
| DAQmxGetAIConvDigSyncEnable |  |
| DAQmxGetAIConvDigSyncEnableEx |  |
| DAQmxGetAIConvMaxRate |  |
| DAQmxGetAIConvMaxRateEx |  |
| DAQmxGetAIConvRate |  |
| DAQmxGetAIConvRateEx |  |
| DAQmxGetAIConvSrc |  |
| DAQmxGetAIConvSrcEx |  |
| DAQmxGetAIConvTimebaseDiv |  |
| DAQmxGetAIConvTimebaseDivEx |  |
| DAQmxGetAIConvTimebaseSrc |  |
| DAQmxGetAIConvTimebaseSrcEx |  |
| DAQmxGetAICoupling |  |
| DAQmxGetAICurrentACRMSUnits |  |
| DAQmxGetAICurrentShuntLoc |  |
| DAQmxGetAICurrentShuntResistance |  |
| DAQmxGetAICurrentUnits |  |
| DAQmxGetAICustomScaleName |  |
| DAQmxGetAIDCOffset |  |
| DAQmxGetAIDataXferCustomThreshold |  |
| DAQmxGetAIDataXferMaxRate |  |
| DAQmxGetAIDataXferMech |  |
| DAQmxGetAIDataXferReqCond |  |
| DAQmxGetAIDevScalingCoeff |  |
| DAQmxGetAIDigFltrBandpassCenterFreq |  |
| DAQmxGetAIDigFltrBandpassWidth |  |
| DAQmxGetAIDigFltrCoeff |  |
| DAQmxGetAIDigFltrEnable |  |
| DAQmxGetAIDigFltrHighpassCutoffFreq |  |
| DAQmxGetAIDigFltrLowpassCutoffFreq |  |
| DAQmxGetAIDigFltrNotchCenterFreq |  |
| DAQmxGetAIDigFltrNotchWidth |  |
| DAQmxGetAIDigFltrOrder |  |
| DAQmxGetAIDigFltrResponse |  |
| DAQmxGetAIDigFltrType |  |
| DAQmxGetAIDigFltrTypes |  |
| DAQmxGetAIDitherEnable |  |
| DAQmxGetAIEddyCurrentProxProbeSensitivity |  |
| DAQmxGetAIEddyCurrentProxProbeSensitivityUnits |  |
| DAQmxGetAIEddyCurrentProxProbeUnits |  |
| DAQmxGetAIEnhancedAliasRejectionEnable |  |
| DAQmxGetAIExcitActualVal |  |
| DAQmxGetAIExcitDCorAC |  |
| DAQmxGetAIExcitIdleOutputBehavior |  |
| DAQmxGetAIExcitSense |  |
| DAQmxGetAIExcitSrc |  |
| DAQmxGetAIExcitUseForScaling |  |
| DAQmxGetAIExcitUseMultiplexed |  |
| DAQmxGetAIExcitVal |  |
| DAQmxGetAIExcitVoltageOrCurrent |  |
| DAQmxGetAIFilterDelay |  |
| DAQmxGetAIFilterDelayAdjustment |  |
| DAQmxGetAIFilterDelayUnits |  |
| DAQmxGetAIFilterEnable |  |
| DAQmxGetAIFilterFreq |  |
| DAQmxGetAIFilterOrder |  |
| DAQmxGetAIFilterResponse |  |
| DAQmxGetAIForceIEPESensorSensitivity |  |
| DAQmxGetAIForceIEPESensorSensitivityUnits |  |
| DAQmxGetAIForceReadFromChan |  |
| DAQmxGetAIForceUnits |  |
| DAQmxGetAIFreqHyst |  |
| DAQmxGetAIFreqThreshVoltage |  |
| DAQmxGetAIFreqUnits |  |
| DAQmxGetAIGain |  |
| DAQmxGetAIImpedance |  |
| DAQmxGetAIInputLimitsFaultDetectEnable |  |
| DAQmxGetAIInputLimitsFaultDetectLowerLimit |  |
| DAQmxGetAIInputLimitsFaultDetectUpperLimit |  |
| DAQmxGetAIInputSrc |  |
| DAQmxGetAIIsTEDS |  |
| DAQmxGetAILVDTSensitivity |  |
| DAQmxGetAILVDTSensitivityUnits |  |
| DAQmxGetAILVDTUnits |  |
| DAQmxGetAILeadWireResistance |  |
| DAQmxGetAILossyLSBRemovalCompressedSampSize |  |
| DAQmxGetAILowpassCutoffFreq |  |
| DAQmxGetAILowpassEnable |  |
| DAQmxGetAILowpassSwitchCapClkSrc |  |
| DAQmxGetAILowpassSwitchCapExtClkDiv |  |
| DAQmxGetAILowpassSwitchCapExtClkFreq |  |
| DAQmxGetAILowpassSwitchCapOutClkDiv |  |
| DAQmxGetAIMax |  |
| DAQmxGetAIMeasType |  |
| DAQmxGetAIMemMapEnable |  |
| DAQmxGetAIMicrophoneSensitivity |  |
| DAQmxGetAIMin |  |
| DAQmxGetAIOpenChanDetectEnable |  |
| DAQmxGetAIOpenThrmcplDetectEnable |  |
| DAQmxGetAIOvercurrentDetectEnable |  |
| DAQmxGetAIPowerSupplyFaultDetectEnable |  |
| DAQmxGetAIPowerUnits |  |
| DAQmxGetAIPressureUnits |  |
| DAQmxGetAIProbeAtten |  |
| DAQmxGetAIRTDA |  |
| DAQmxGetAIRTDB |  |
| DAQmxGetAIRTDC |  |
| DAQmxGetAIRTDR0 |  |
| DAQmxGetAIRTDType |  |
| DAQmxGetAIRVDTSensitivity |  |
| DAQmxGetAIRVDTSensitivityUnits |  |
| DAQmxGetAIRVDTUnits |  |
| DAQmxGetAIRawDataCompressionType |  |
| DAQmxGetAIRawSampJustification |  |
| DAQmxGetAIRawSampSize |  |
| DAQmxGetAIRemoveFilterDelay |  |
| DAQmxGetAIResistanceCfg |  |
| DAQmxGetAIResistanceUnits |  |
| DAQmxGetAIResolution |  |
| DAQmxGetAIResolutionUnits |  |
| DAQmxGetAIRngHigh |  |
| DAQmxGetAIRngLow |  |
| DAQmxGetAIRosetteStrainGageOrientation |  |
| DAQmxGetAIRosetteStrainGageRosetteMeasType |  |
| DAQmxGetAIRosetteStrainGageRosetteType |  |
| DAQmxGetAIRosetteStrainGageStrainChans |  |
| DAQmxGetAISampAndHoldEnable |  |
| DAQmxGetAISensorPowerCfg |  |
| DAQmxGetAISensorPowerType |  |
| DAQmxGetAISensorPowerVoltage |  |
| DAQmxGetAISoundPressureMaxSoundPressureLvl |  |
| DAQmxGetAISoundPressureUnits |  |
| DAQmxGetAISoundPressuredBRef |  |
| DAQmxGetAIStrainGageCfg |  |
| DAQmxGetAIStrainGageForceReadFromChan |  |
| DAQmxGetAIStrainGageGageFactor |  |
| DAQmxGetAIStrainGagePoissonRatio |  |
| DAQmxGetAIStrainUnits |  |
| DAQmxGetAITEDSUnits |  |
| DAQmxGetAITempUnits |  |
| DAQmxGetAITermCfg |  |
| DAQmxGetAIThrmcplCJCChan |  |
| DAQmxGetAIThrmcplCJCSrc |  |
| DAQmxGetAIThrmcplCJCVal |  |
| DAQmxGetAIThrmcplLeadOffsetVoltage |  |
| DAQmxGetAIThrmcplScaleType |  |
| DAQmxGetAIThrmcplType |  |
| DAQmxGetAIThrmstrA |  |
| DAQmxGetAIThrmstrB |  |
| DAQmxGetAIThrmstrC |  |
| DAQmxGetAIThrmstrR1 |  |
| DAQmxGetAITorqueUnits |  |
| DAQmxGetAIUsbXferReqCount |  |
| DAQmxGetAIUsbXferReqSize |  |
| DAQmxGetAIVelocityIEPESensorSensitivity |  |
| DAQmxGetAIVelocityIEPESensorSensitivityUnits |  |
| DAQmxGetAIVelocityIEPESensordBRef |  |
| DAQmxGetAIVelocityUnits |  |
| DAQmxGetAIVoltageACRMSUnits |  |
| DAQmxGetAIVoltageUnits |  |
| DAQmxGetAIVoltagedBRef |  |
| DAQmxGetAOCommonModeOffset |  |
| DAQmxGetAOCurrentUnits |  |
| DAQmxGetAOCustomScaleName |  |
| DAQmxGetAODACOffsetExtSrc |  |
| DAQmxGetAODACOffsetSrc |  |
| DAQmxGetAODACOffsetVal |  |
| DAQmxGetAODACRefAllowConnToGnd |  |
| DAQmxGetAODACRefConnToGnd |  |
| DAQmxGetAODACRefExtSrc |  |
| DAQmxGetAODACRefSrc |  |
| DAQmxGetAODACRefVal |  |
| DAQmxGetAODACRngHigh |  |
| DAQmxGetAODACRngLow |  |
| DAQmxGetAODataXferMech |  |
| DAQmxGetAODataXferReqCond |  |
| DAQmxGetAODevScalingCoeff |  |
| DAQmxGetAOEnhancedImageRejectionEnable |  |
| DAQmxGetAOFilterDelay |  |
| DAQmxGetAOFilterDelayAdjustment |  |
| DAQmxGetAOFilterDelayUnits |  |
| DAQmxGetAOFuncGenAmplitude |  |
| DAQmxGetAOFuncGenFMDeviation |  |
| DAQmxGetAOFuncGenFreq |  |
| DAQmxGetAOFuncGenModulationType |  |
| DAQmxGetAOFuncGenOffset |  |
| DAQmxGetAOFuncGenSquareDutyCycle |  |
| DAQmxGetAOFuncGenStartPhase |  |
| DAQmxGetAOFuncGenType |  |
| DAQmxGetAOGain |  |
| DAQmxGetAOIdleOutputBehavior |  |
| DAQmxGetAOLoadImpedance |  |
| DAQmxGetAOMax |  |
| DAQmxGetAOMemMapEnable |  |
| DAQmxGetAOMin |  |
| DAQmxGetAOOutputImpedance |  |
| DAQmxGetAOOutputType |  |
| DAQmxGetAOPowerAmpChannelEnable |  |
| DAQmxGetAOPowerAmpGain |  |
| DAQmxGetAOPowerAmpOffset |  |
| DAQmxGetAOPowerAmpOvercurrent |  |
| DAQmxGetAOPowerAmpScalingCoeff |  |
| DAQmxGetAOReglitchEnable |  |
| DAQmxGetAOResolution |  |
| DAQmxGetAOResolutionUnits |  |
| DAQmxGetAOTermCfg |  |
| DAQmxGetAOUsbXferReqCount |  |
| DAQmxGetAOUsbXferReqSize |  |
| DAQmxGetAOUseOnlyOnBrdMem |  |
| DAQmxGetAOVoltageCurrentLimit |  |
| DAQmxGetAOVoltageUnits |  |
| DAQmxGetAdvTrigType |  |
| DAQmxGetAnlgEdgeRefTrigCoupling |  |
| DAQmxGetAnlgEdgeRefTrigDigFltrEnable |  |
| DAQmxGetAnlgEdgeRefTrigDigFltrMinPulseWidth |  |
| DAQmxGetAnlgEdgeRefTrigDigFltrTimebaseRate |  |
| DAQmxGetAnlgEdgeRefTrigDigFltrTimebaseSrc |  |
| DAQmxGetAnlgEdgeRefTrigDigSyncEnable |  |
| DAQmxGetAnlgEdgeRefTrigHyst |  |
| DAQmxGetAnlgEdgeRefTrigLvl |  |
| DAQmxGetAnlgEdgeRefTrigSlope |  |
| DAQmxGetAnlgEdgeRefTrigSrc |  |
| DAQmxGetAnlgEdgeStartTrigCoupling |  |
| DAQmxGetAnlgEdgeStartTrigDigFltrEnable |  |
| DAQmxGetAnlgEdgeStartTrigDigFltrMinPulseWidth |  |
| DAQmxGetAnlgEdgeStartTrigDigFltrTimebaseRate |  |
| DAQmxGetAnlgEdgeStartTrigDigFltrTimebaseSrc |  |
| DAQmxGetAnlgEdgeStartTrigDigSyncEnable |  |
| DAQmxGetAnlgEdgeStartTrigHyst |  |
| DAQmxGetAnlgEdgeStartTrigLvl |  |
| DAQmxGetAnlgEdgeStartTrigSlope |  |
| DAQmxGetAnlgEdgeStartTrigSrc |  |
| DAQmxGetAnlgLvlPauseTrigCoupling |  |
| DAQmxGetAnlgLvlPauseTrigDigFltrEnable |  |
| DAQmxGetAnlgLvlPauseTrigDigFltrMinPulseWidth |  |
| DAQmxGetAnlgLvlPauseTrigDigFltrTimebaseRate |  |
| DAQmxGetAnlgLvlPauseTrigDigFltrTimebaseSrc |  |
| DAQmxGetAnlgLvlPauseTrigDigSyncEnable |  |
| DAQmxGetAnlgLvlPauseTrigHyst |  |
| DAQmxGetAnlgLvlPauseTrigLvl |  |
| DAQmxGetAnlgLvlPauseTrigSrc |  |
| DAQmxGetAnlgLvlPauseTrigWhen |  |
| DAQmxGetAnlgMultiEdgeRefTrigCouplings |  |
| DAQmxGetAnlgMultiEdgeRefTrigHysts |  |
| DAQmxGetAnlgMultiEdgeRefTrigLvls |  |
| DAQmxGetAnlgMultiEdgeRefTrigSlopes |  |
| DAQmxGetAnlgMultiEdgeRefTrigSrcs |  |
| DAQmxGetAnlgMultiEdgeStartTrigCouplings |  |
| DAQmxGetAnlgMultiEdgeStartTrigHysts |  |
| DAQmxGetAnlgMultiEdgeStartTrigLvls |  |
| DAQmxGetAnlgMultiEdgeStartTrigSlopes |  |
| DAQmxGetAnlgMultiEdgeStartTrigSrcs |  |
| DAQmxGetAnlgWinPauseTrigBtm |  |
| DAQmxGetAnlgWinPauseTrigCoupling |  |
| DAQmxGetAnlgWinPauseTrigDigFltrEnable |  |
| DAQmxGetAnlgWinPauseTrigDigFltrMinPulseWidth |  |
| DAQmxGetAnlgWinPauseTrigDigFltrTimebaseRate |  |
| DAQmxGetAnlgWinPauseTrigDigFltrTimebaseSrc |  |
| DAQmxGetAnlgWinPauseTrigDigSyncEnable |  |
| DAQmxGetAnlgWinPauseTrigSrc |  |
| DAQmxGetAnlgWinPauseTrigTop |  |
| DAQmxGetAnlgWinPauseTrigWhen |  |
| DAQmxGetAnlgWinRefTrigBtm |  |
| DAQmxGetAnlgWinRefTrigCoupling |  |
| DAQmxGetAnlgWinRefTrigDigFltrEnable |  |
| DAQmxGetAnlgWinRefTrigDigFltrMinPulseWidth |  |
| DAQmxGetAnlgWinRefTrigDigFltrTimebaseRate |  |
| DAQmxGetAnlgWinRefTrigDigFltrTimebaseSrc |  |
| DAQmxGetAnlgWinRefTrigDigSyncEnable |  |
| DAQmxGetAnlgWinRefTrigSrc |  |
| DAQmxGetAnlgWinRefTrigTop |  |
| DAQmxGetAnlgWinRefTrigWhen |  |
| DAQmxGetAnlgWinStartTrigBtm |  |
| DAQmxGetAnlgWinStartTrigCoupling |  |
| DAQmxGetAnlgWinStartTrigDigFltrEnable |  |
| DAQmxGetAnlgWinStartTrigDigFltrMinPulseWidth |  |
| DAQmxGetAnlgWinStartTrigDigFltrTimebaseRate |  |
| DAQmxGetAnlgWinStartTrigDigFltrTimebaseSrc |  |
| DAQmxGetAnlgWinStartTrigDigSyncEnable |  |
| DAQmxGetAnlgWinStartTrigSrc |  |
| DAQmxGetAnlgWinStartTrigTop |  |
| DAQmxGetAnlgWinStartTrigWhen |  |
| DAQmxGetArmStartTerm |  |
| DAQmxGetArmStartTrigTimescale |  |
| DAQmxGetArmStartTrigTimestampEnable |  |
| DAQmxGetArmStartTrigTimestampTimescale |  |
| DAQmxGetArmStartTrigTimestampVal |  |
| DAQmxGetArmStartTrigTrigWhen |  |
| DAQmxGetArmStartTrigType |  |
| DAQmxGetAuxPowerErrorChans |  |
| DAQmxGetAuxPowerErrorChansExist |  |
| DAQmxGetBufInputBufSize |  |
| DAQmxGetBufInputOnbrdBufSize |  |
| DAQmxGetBufOutputBufSize |  |
| DAQmxGetBufOutputOnbrdBufSize |  |
| DAQmxGetCIAngEncoderInitialAngle |  |
| DAQmxGetCIAngEncoderPulsesPerRev |  |
| DAQmxGetCIAngEncoderUnits |  |
| DAQmxGetCICount |  |
| DAQmxGetCICountEdgesActiveEdge |  |
| DAQmxGetCICountEdgesCountDirDigFltrEnable |  |
| DAQmxGetCICountEdgesCountDirDigFltrMinPulseWidth |  |
| DAQmxGetCICountEdgesCountDirDigFltrTimebaseRate |  |
| DAQmxGetCICountEdgesCountDirDigFltrTimebaseSrc |  |
| DAQmxGetCICountEdgesCountDirDigSyncEnable |  |
| DAQmxGetCICountEdgesCountDirHyst |  |
| DAQmxGetCICountEdgesCountDirLogicLvlBehavior |  |
| DAQmxGetCICountEdgesCountDirTermCfg |  |
| DAQmxGetCICountEdgesCountDirThreshVoltage |  |
| DAQmxGetCICountEdgesCountResetActiveEdge |  |
| DAQmxGetCICountEdgesCountResetDigFltrEnable |  |
| DAQmxGetCICountEdgesCountResetDigFltrMinPulseWidth |  |
| DAQmxGetCICountEdgesCountResetDigFltrTimebaseRate |  |
| DAQmxGetCICountEdgesCountResetDigFltrTimebaseSrc |  |
| DAQmxGetCICountEdgesCountResetDigSyncEnable |  |
| DAQmxGetCICountEdgesCountResetEnable |  |
| DAQmxGetCICountEdgesCountResetHyst |  |
| DAQmxGetCICountEdgesCountResetLogicLvlBehavior |  |
| DAQmxGetCICountEdgesCountResetResetCount |  |
| DAQmxGetCICountEdgesCountResetTerm |  |
| DAQmxGetCICountEdgesCountResetTermCfg |  |
| DAQmxGetCICountEdgesCountResetThreshVoltage |  |
| DAQmxGetCICountEdgesDigFltrEnable |  |
| DAQmxGetCICountEdgesDigFltrMinPulseWidth |  |
| DAQmxGetCICountEdgesDigFltrTimebaseRate |  |
| DAQmxGetCICountEdgesDigFltrTimebaseSrc |  |
| DAQmxGetCICountEdgesDigSyncEnable |  |
| DAQmxGetCICountEdgesDir |  |
| DAQmxGetCICountEdgesDirTerm |  |
| DAQmxGetCICountEdgesGateDigFltrEnable |  |
| DAQmxGetCICountEdgesGateDigFltrMinPulseWidth |  |
| DAQmxGetCICountEdgesGateDigFltrTimebaseRate |  |
| DAQmxGetCICountEdgesGateDigFltrTimebaseSrc |  |
| DAQmxGetCICountEdgesGateEnable |  |
| DAQmxGetCICountEdgesGateHyst |  |
| DAQmxGetCICountEdgesGateLogicLvlBehavior |  |
| DAQmxGetCICountEdgesGateTerm |  |
| DAQmxGetCICountEdgesGateTermCfg |  |
| DAQmxGetCICountEdgesGateThreshVoltage |  |
| DAQmxGetCICountEdgesGateWhen |  |
| DAQmxGetCICountEdgesHyst |  |
| DAQmxGetCICountEdgesInitialCnt |  |
| DAQmxGetCICountEdgesLogicLvlBehavior |  |
| DAQmxGetCICountEdgesTerm |  |
| DAQmxGetCICountEdgesTermCfg |  |
| DAQmxGetCICountEdgesThreshVoltage |  |
| DAQmxGetCICtrTimebaseActiveEdge |  |
| DAQmxGetCICtrTimebaseDigFltrEnable |  |
| DAQmxGetCICtrTimebaseDigFltrMinPulseWidth |  |
| DAQmxGetCICtrTimebaseDigFltrTimebaseRate |  |
| DAQmxGetCICtrTimebaseDigFltrTimebaseSrc |  |
| DAQmxGetCICtrTimebaseDigSyncEnable |  |
| DAQmxGetCICtrTimebaseMasterTimebaseDiv |  |
| DAQmxGetCICtrTimebaseRate |  |
| DAQmxGetCICtrTimebaseSrc |  |
| DAQmxGetCICustomScaleName |  |
| DAQmxGetCIDataXferMech |  |
| DAQmxGetCIDataXferReqCond |  |
| DAQmxGetCIDupCountPrevent |  |
| DAQmxGetCIDutyCycleDigFltrEnable |  |
| DAQmxGetCIDutyCycleDigFltrMinPulseWidth |  |
| DAQmxGetCIDutyCycleDigFltrTimebaseRate |  |
| DAQmxGetCIDutyCycleDigFltrTimebaseSrc |  |
| DAQmxGetCIDutyCycleLogicLvlBehavior |  |
| DAQmxGetCIDutyCycleStartingEdge |  |
| DAQmxGetCIDutyCycleTerm |  |
| DAQmxGetCIDutyCycleTermCfg |  |
| DAQmxGetCIEncoderAInputDigFltrEnable |  |
| DAQmxGetCIEncoderAInputDigFltrMinPulseWidth |  |
| DAQmxGetCIEncoderAInputDigFltrTimebaseRate |  |
| DAQmxGetCIEncoderAInputDigFltrTimebaseSrc |  |
| DAQmxGetCIEncoderAInputDigSyncEnable |  |
| DAQmxGetCIEncoderAInputLogicLvlBehavior |  |
| DAQmxGetCIEncoderAInputTerm |  |
| DAQmxGetCIEncoderAInputTermCfg |  |
| DAQmxGetCIEncoderBInputDigFltrEnable |  |
| DAQmxGetCIEncoderBInputDigFltrMinPulseWidth |  |
| DAQmxGetCIEncoderBInputDigFltrTimebaseRate |  |
| DAQmxGetCIEncoderBInputDigFltrTimebaseSrc |  |
| DAQmxGetCIEncoderBInputDigSyncEnable |  |
| DAQmxGetCIEncoderBInputLogicLvlBehavior |  |
| DAQmxGetCIEncoderBInputTerm |  |
| DAQmxGetCIEncoderBInputTermCfg |  |
| DAQmxGetCIEncoderDecodingType |  |
| DAQmxGetCIEncoderZIndexEnable |  |
| DAQmxGetCIEncoderZIndexPhase |  |
| DAQmxGetCIEncoderZIndexVal |  |
| DAQmxGetCIEncoderZInputDigFltrEnable |  |
| DAQmxGetCIEncoderZInputDigFltrMinPulseWidth |  |
| DAQmxGetCIEncoderZInputDigFltrTimebaseRate |  |
| DAQmxGetCIEncoderZInputDigFltrTimebaseSrc |  |
| DAQmxGetCIEncoderZInputDigSyncEnable |  |
| DAQmxGetCIEncoderZInputLogicLvlBehavior |  |
| DAQmxGetCIEncoderZInputTerm |  |
| DAQmxGetCIEncoderZInputTermCfg |  |
| DAQmxGetCIFilterDelay |  |
| DAQmxGetCIFilterDelayUnits |  |
| DAQmxGetCIFilterEnable |  |
| DAQmxGetCIFilterFreq |  |
| DAQmxGetCIFilterOrder |  |
| DAQmxGetCIFilterResponse |  |
| DAQmxGetCIFreqDigFltrEnable |  |
| DAQmxGetCIFreqDigFltrMinPulseWidth |  |
| DAQmxGetCIFreqDigFltrTimebaseRate |  |
| DAQmxGetCIFreqDigFltrTimebaseSrc |  |
| DAQmxGetCIFreqDigSyncEnable |  |
| DAQmxGetCIFreqDiv |  |
| DAQmxGetCIFreqEnableAveraging |  |
| DAQmxGetCIFreqHyst |  |
| DAQmxGetCIFreqLogicLvlBehavior |  |
| DAQmxGetCIFreqMeasMeth |  |
| DAQmxGetCIFreqMeasTime |  |
| DAQmxGetCIFreqStartingEdge |  |
| DAQmxGetCIFreqTerm |  |
| DAQmxGetCIFreqTermCfg |  |
| DAQmxGetCIFreqThreshVoltage |  |
| DAQmxGetCIFreqUnits |  |
| DAQmxGetCIGPSSyncMethod |  |
| DAQmxGetCIGPSSyncSrc |  |
| DAQmxGetCILinEncoderDistPerPulse |  |
| DAQmxGetCILinEncoderInitialPos |  |
| DAQmxGetCILinEncoderUnits |  |
| DAQmxGetCIMax |  |
| DAQmxGetCIMaxMeasPeriod |  |
| DAQmxGetCIMeasType |  |
| DAQmxGetCIMemMapEnable |  |
| DAQmxGetCIMin |  |
| DAQmxGetCINumPossiblyInvalidSamps |  |
| DAQmxGetCIOutputState |  |
| DAQmxGetCIPeriodDigFltrEnable |  |
| DAQmxGetCIPeriodDigFltrMinPulseWidth |  |
| DAQmxGetCIPeriodDigFltrTimebaseRate |  |
| DAQmxGetCIPeriodDigFltrTimebaseSrc |  |
| DAQmxGetCIPeriodDigSyncEnable |  |
| DAQmxGetCIPeriodDiv |  |
| DAQmxGetCIPeriodEnableAveraging |  |
| DAQmxGetCIPeriodHyst |  |
| DAQmxGetCIPeriodLogicLvlBehavior |  |
| DAQmxGetCIPeriodMeasMeth |  |
| DAQmxGetCIPeriodMeasTime |  |
| DAQmxGetCIPeriodStartingEdge |  |
| DAQmxGetCIPeriodTerm |  |
| DAQmxGetCIPeriodTermCfg |  |
| DAQmxGetCIPeriodThreshVoltage |  |
| DAQmxGetCIPeriodUnits |  |
| DAQmxGetCIPrescaler |  |
| DAQmxGetCIPulseFreqDigFltrEnable |  |
| DAQmxGetCIPulseFreqDigFltrMinPulseWidth |  |
| DAQmxGetCIPulseFreqDigFltrTimebaseRate |  |
| DAQmxGetCIPulseFreqDigFltrTimebaseSrc |  |
| DAQmxGetCIPulseFreqDigSyncEnable |  |
| DAQmxGetCIPulseFreqLogicLvlBehavior |  |
| DAQmxGetCIPulseFreqStartEdge |  |
| DAQmxGetCIPulseFreqTerm |  |
| DAQmxGetCIPulseFreqTermCfg |  |
| DAQmxGetCIPulseFreqUnits |  |
| DAQmxGetCIPulseTicksDigFltrEnable |  |
| DAQmxGetCIPulseTicksDigFltrMinPulseWidth |  |
| DAQmxGetCIPulseTicksDigFltrTimebaseRate |  |
| DAQmxGetCIPulseTicksDigFltrTimebaseSrc |  |
| DAQmxGetCIPulseTicksDigSyncEnable |  |
| DAQmxGetCIPulseTicksLogicLvlBehavior |  |
| DAQmxGetCIPulseTicksStartEdge |  |
| DAQmxGetCIPulseTicksTerm |  |
| DAQmxGetCIPulseTicksTermCfg |  |
| DAQmxGetCIPulseTimeDigFltrEnable |  |
| DAQmxGetCIPulseTimeDigFltrMinPulseWidth |  |
| DAQmxGetCIPulseTimeDigFltrTimebaseRate |  |
| DAQmxGetCIPulseTimeDigFltrTimebaseSrc |  |
| DAQmxGetCIPulseTimeDigSyncEnable |  |
| DAQmxGetCIPulseTimeLogicLvlBehavior |  |
| DAQmxGetCIPulseTimeStartEdge |  |
| DAQmxGetCIPulseTimeTerm |  |
| DAQmxGetCIPulseTimeTermCfg |  |
| DAQmxGetCIPulseTimeUnits |  |
| DAQmxGetCIPulseWidthDigFltrEnable |  |
| DAQmxGetCIPulseWidthDigFltrMinPulseWidth |  |
| DAQmxGetCIPulseWidthDigFltrTimebaseRate |  |
| DAQmxGetCIPulseWidthDigFltrTimebaseSrc |  |
| DAQmxGetCIPulseWidthDigSyncEnable |  |
| DAQmxGetCIPulseWidthLogicLvlBehavior |  |
| DAQmxGetCIPulseWidthStartingEdge |  |
| DAQmxGetCIPulseWidthTerm |  |
| DAQmxGetCIPulseWidthTermCfg |  |
| DAQmxGetCIPulseWidthUnits |  |
| DAQmxGetCISampClkOverrunBehavior |  |
| DAQmxGetCISampClkOverrunSentinelVal |  |
| DAQmxGetCISemiPeriodDigFltrEnable |  |
| DAQmxGetCISemiPeriodDigFltrMinPulseWidth |  |
| DAQmxGetCISemiPeriodDigFltrTimebaseRate |  |
| DAQmxGetCISemiPeriodDigFltrTimebaseSrc |  |
| DAQmxGetCISemiPeriodDigSyncEnable |  |
| DAQmxGetCISemiPeriodLogicLvlBehavior |  |
| DAQmxGetCISemiPeriodStartingEdge |  |
| DAQmxGetCISemiPeriodTerm |  |
| DAQmxGetCISemiPeriodTermCfg |  |
| DAQmxGetCISemiPeriodUnits |  |
| DAQmxGetCITCReached |  |
| DAQmxGetCIThreshVoltage |  |
| DAQmxGetCITimestampInitialSeconds |  |
| DAQmxGetCITimestampUnits |  |
| DAQmxGetCITwoEdgeSepFirstDigFltrEnable |  |
| DAQmxGetCITwoEdgeSepFirstDigFltrMinPulseWidth |  |
| DAQmxGetCITwoEdgeSepFirstDigFltrTimebaseRate |  |
| DAQmxGetCITwoEdgeSepFirstDigFltrTimebaseSrc |  |
| DAQmxGetCITwoEdgeSepFirstDigSyncEnable |  |
| DAQmxGetCITwoEdgeSepFirstEdge |  |
| DAQmxGetCITwoEdgeSepFirstLogicLvlBehavior |  |
| DAQmxGetCITwoEdgeSepFirstTerm |  |
| DAQmxGetCITwoEdgeSepFirstTermCfg |  |
| DAQmxGetCITwoEdgeSepSecondDigFltrEnable |  |
| DAQmxGetCITwoEdgeSepSecondDigFltrMinPulseWidth |  |
| DAQmxGetCITwoEdgeSepSecondDigFltrTimebaseRate |  |
| DAQmxGetCITwoEdgeSepSecondDigFltrTimebaseSrc |  |
| DAQmxGetCITwoEdgeSepSecondDigSyncEnable |  |
| DAQmxGetCITwoEdgeSepSecondEdge |  |
| DAQmxGetCITwoEdgeSepSecondLogicLvlBehavior |  |
| DAQmxGetCITwoEdgeSepSecondTerm |  |
| DAQmxGetCITwoEdgeSepSecondTermCfg |  |
| DAQmxGetCITwoEdgeSepUnits |  |
| DAQmxGetCIUsbXferReqCount |  |
| DAQmxGetCIUsbXferReqSize |  |
| DAQmxGetCIVelocityAngEncoderPulsesPerRev |  |
| DAQmxGetCIVelocityAngEncoderUnits |  |
| DAQmxGetCIVelocityDiv |  |
| DAQmxGetCIVelocityEncoderAInputDigFltrEnable |  |
| DAQmxGetCIVelocityEncoderAInputDigFltrMinPulseWidth |  |
| DAQmxGetCIVelocityEncoderAInputDigFltrTimebaseRate |  |
| DAQmxGetCIVelocityEncoderAInputDigFltrTimebaseSrc |  |
| DAQmxGetCIVelocityEncoderAInputLogicLvlBehavior |  |
| DAQmxGetCIVelocityEncoderAInputTerm |  |
| DAQmxGetCIVelocityEncoderAInputTermCfg |  |
| DAQmxGetCIVelocityEncoderBInputDigFltrEnable |  |
| DAQmxGetCIVelocityEncoderBInputDigFltrMinPulseWidth |  |
| DAQmxGetCIVelocityEncoderBInputDigFltrTimebaseRate |  |
| DAQmxGetCIVelocityEncoderBInputDigFltrTimebaseSrc |  |
| DAQmxGetCIVelocityEncoderBInputLogicLvlBehavior |  |
| DAQmxGetCIVelocityEncoderBInputTerm |  |
| DAQmxGetCIVelocityEncoderBInputTermCfg |  |
| DAQmxGetCIVelocityEncoderDecodingType |  |
| DAQmxGetCIVelocityLinEncoderDistPerPulse |  |
| DAQmxGetCIVelocityLinEncoderUnits |  |
| DAQmxGetCIVelocityMeasTime |  |
| DAQmxGetCOAutoIncrCnt |  |
| DAQmxGetCOConstrainedGenMode |  |
| DAQmxGetCOCount |  |
| DAQmxGetCOCtrTimebaseActiveEdge |  |
| DAQmxGetCOCtrTimebaseDigFltrEnable |  |
| DAQmxGetCOCtrTimebaseDigFltrMinPulseWidth |  |
| DAQmxGetCOCtrTimebaseDigFltrTimebaseRate |  |
| DAQmxGetCOCtrTimebaseDigFltrTimebaseSrc |  |
| DAQmxGetCOCtrTimebaseDigSyncEnable |  |
| DAQmxGetCOCtrTimebaseMasterTimebaseDiv |  |
| DAQmxGetCOCtrTimebaseRate |  |
| DAQmxGetCOCtrTimebaseSrc |  |
| DAQmxGetCODataXferMech |  |
| DAQmxGetCODataXferReqCond |  |
| DAQmxGetCOEnableInitialDelayOnRetrigger |  |
| DAQmxGetCOMemMapEnable |  |
| DAQmxGetCOOutputState |  |
| DAQmxGetCOOutputType |  |
| DAQmxGetCOPrescaler |  |
| DAQmxGetCOPulseDone |  |
| DAQmxGetCOPulseDutyCyc |  |
| DAQmxGetCOPulseFreq |  |
| DAQmxGetCOPulseFreqInitialDelay |  |
| DAQmxGetCOPulseFreqUnits |  |
| DAQmxGetCOPulseHighTicks |  |
| DAQmxGetCOPulseHighTime |  |
| DAQmxGetCOPulseIdleState |  |
| DAQmxGetCOPulseLowTicks |  |
| DAQmxGetCOPulseLowTime |  |
| DAQmxGetCOPulseTerm |  |
| DAQmxGetCOPulseTicksInitialDelay |  |
| DAQmxGetCOPulseTimeInitialDelay |  |
| DAQmxGetCOPulseTimeUnits |  |
| DAQmxGetCORdyForNewVal |  |
| DAQmxGetCOUsbXferReqCount |  |
| DAQmxGetCOUsbXferReqSize |  |
| DAQmxGetCOUseOnlyOnBrdMem |  |
| DAQmxGetCalAccConnectionCount |  |
| DAQmxGetCalDevTemp |  |
| DAQmxGetCalRecommendedAccConnectionCountLimit |  |
| DAQmxGetCalUserDefinedInfo |  |
| DAQmxGetCalUserDefinedInfoMaxSize |  |
| DAQmxGetCarrierSerialNum |  |
| DAQmxGetChanDescr |  |
| DAQmxGetChanIsGlobal |  |
| DAQmxGetChanSyncUnlockBehavior |  |
| DAQmxGetChanType |  |
| DAQmxGetChangeDetectDIFallingEdgePhysicalChans |  |
| DAQmxGetChangeDetectDIRisingEdgePhysicalChans |  |
| DAQmxGetChangeDetectDITristate |  |
| DAQmxGetDIAcquireOn |  |
| DAQmxGetDIDataXferMech |  |
| DAQmxGetDIDataXferReqCond |  |
| DAQmxGetDIDigFltrEnable |  |
| DAQmxGetDIDigFltrEnableBusMode |  |
| DAQmxGetDIDigFltrMinPulseWidth |  |
| DAQmxGetDIDigFltrTimebaseRate |  |
| DAQmxGetDIDigFltrTimebaseSrc |  |
| DAQmxGetDIDigSyncEnable |  |
| DAQmxGetDIInvertLines |  |
| DAQmxGetDILogicFamily |  |
| DAQmxGetDIMemMapEnable |  |
| DAQmxGetDINumLines |  |
| DAQmxGetDITristate |  |
| DAQmxGetDIUsbXferReqCount |  |
| DAQmxGetDIUsbXferReqSize |  |
| DAQmxGetDODataXferMech |  |
| DAQmxGetDODataXferReqCond |  |
| DAQmxGetDOGenerateOn |  |
| DAQmxGetDOInvertLines |  |
| DAQmxGetDOLineStatesDoneState |  |
| DAQmxGetDOLineStatesPausedState |  |
| DAQmxGetDOLineStatesStartState |  |
| DAQmxGetDOLogicFamily |  |
| DAQmxGetDOMemMapEnable |  |
| DAQmxGetDONumLines |  |
| DAQmxGetDOOutputDriveType |  |
| DAQmxGetDOOvercurrentAutoReenable |  |
| DAQmxGetDOOvercurrentLimit |  |
| DAQmxGetDOOvercurrentReenablePeriod |  |
| DAQmxGetDOTristate |  |
| DAQmxGetDOUsbXferReqCount |  |
| DAQmxGetDOUsbXferReqSize |  |
| DAQmxGetDOUseOnlyOnBrdMem |  |
| DAQmxGetDelayFromSampClkDelay |  |
| DAQmxGetDelayFromSampClkDelayEx |  |
| DAQmxGetDelayFromSampClkDelayUnits |  |
| DAQmxGetDelayFromSampClkDelayUnitsEx |  |
| DAQmxGetDevAIBridgeRngs |  |
| DAQmxGetDevAIChargeRngs |  |
| DAQmxGetDevAICouplings |  |
| DAQmxGetDevAICurrentIntExcitDiscreteVals |  |
| DAQmxGetDevAICurrentRngs |  |
| DAQmxGetDevAIDigFltrLowpassCutoffFreqDiscreteVals |  |
| DAQmxGetDevAIDigFltrLowpassCutoffFreqRangeVals |  |
| DAQmxGetDevAIFreqRngs |  |
| DAQmxGetDevAIGains |  |
| DAQmxGetDevAILowpassCutoffFreqDiscreteVals |  |
| DAQmxGetDevAILowpassCutoffFreqRangeVals |  |
| DAQmxGetDevAIMaxMultiChanRate |  |
| DAQmxGetDevAIMaxSingleChanRate |  |
| DAQmxGetDevAIMinRate |  |
| DAQmxGetDevAINumSampTimingEngines |  |
| DAQmxGetDevAINumSyncPulseSrcs |  |
| DAQmxGetDevAIPhysicalChans |  |
| DAQmxGetDevAIResistanceRngs |  |
| DAQmxGetDevAISampModes |  |
| DAQmxGetDevAISimultaneousSamplingSupported |  |
| DAQmxGetDevAISupportedMeasTypes |  |
| DAQmxGetDevAITrigUsage |  |
| DAQmxGetDevAIVoltageIntExcitDiscreteVals |  |
| DAQmxGetDevAIVoltageIntExcitRangeVals |  |
| DAQmxGetDevAIVoltageRngs |  |
| DAQmxGetDevAOCurrentRngs |  |
| DAQmxGetDevAOGains |  |
| DAQmxGetDevAOMaxRate |  |
| DAQmxGetDevAOMinRate |  |
| DAQmxGetDevAONumSampTimingEngines |  |
| DAQmxGetDevAONumSyncPulseSrcs |  |
| DAQmxGetDevAOPhysicalChans |  |
| DAQmxGetDevAOSampClkSupported |  |
| DAQmxGetDevAOSampModes |  |
| DAQmxGetDevAOSupportedOutputTypes |  |
| DAQmxGetDevAOTrigUsage |  |
| DAQmxGetDevAOVoltageRngs |  |
| DAQmxGetDevAccessoryProductNums |  |
| DAQmxGetDevAccessoryProductTypes |  |
| DAQmxGetDevAccessorySerialNums |  |
| DAQmxGetDevAnlgTrigSupported |  |
| DAQmxGetDevBusType |  |
| DAQmxGetDevCIMaxSize |  |
| DAQmxGetDevCIMaxTimebase |  |
| DAQmxGetDevCIPhysicalChans |  |
| DAQmxGetDevCISampClkSupported |  |
| DAQmxGetDevCISampModes |  |
| DAQmxGetDevCISupportedMeasTypes |  |
| DAQmxGetDevCITrigUsage |  |
| DAQmxGetDevCOMaxSize |  |
| DAQmxGetDevCOMaxTimebase |  |
| DAQmxGetDevCOPhysicalChans |  |
| DAQmxGetDevCOSampClkSupported |  |
| DAQmxGetDevCOSampModes |  |
| DAQmxGetDevCOSupportedOutputTypes |  |
| DAQmxGetDevCOTrigUsage |  |
| DAQmxGetDevChassisModuleDevNames |  |
| DAQmxGetDevCompactDAQChassisDevName |  |
| DAQmxGetDevCompactDAQSlotNum |  |
| DAQmxGetDevCompactRIOChassisDevName |  |
| DAQmxGetDevCompactRIOSlotNum |  |
| DAQmxGetDevDILines |  |
| DAQmxGetDevDIMaxRate |  |
| DAQmxGetDevDINumSampTimingEngines |  |
| DAQmxGetDevDIPorts |  |
| DAQmxGetDevDITrigUsage |  |
| DAQmxGetDevDOLines |  |
| DAQmxGetDevDOMaxRate |  |
| DAQmxGetDevDONumSampTimingEngines |  |
| DAQmxGetDevDOPorts |  |
| DAQmxGetDevDOTrigUsage |  |
| DAQmxGetDevDigTrigSupported |  |
| DAQmxGetDevIDPinMemFamilyCodes |  |
| DAQmxGetDevIDPinMemSerialNums |  |
| DAQmxGetDevIDPinMemSizes |  |
| DAQmxGetDevIDPinPinNames |  |
| DAQmxGetDevIDPinPinStatuses |  |
| DAQmxGetDevIsSimulated |  |
| DAQmxGetDevNumDMAChans |  |
| DAQmxGetDevNumTimeTrigs |  |
| DAQmxGetDevNumTimestampEngines |  |
| DAQmxGetDevPCIBusNum |  |
| DAQmxGetDevPCIDevNum |  |
| DAQmxGetDevPXIChassisNum |  |
| DAQmxGetDevPXISlotNum |  |
| DAQmxGetDevProductCategory |  |
| DAQmxGetDevProductNum |  |
| DAQmxGetDevProductType |  |
| DAQmxGetDevSerialNum |  |
| DAQmxGetDevTCPIPEthernetIP |  |
| DAQmxGetDevTCPIPHostname |  |
| DAQmxGetDevTCPIPWirelessIP |  |
| DAQmxGetDevTEDSHWTEDSSupported |  |
| DAQmxGetDevTerminals |  |
| DAQmxGetDevTimeTrigSupported |  |
| DAQmxGetDigEdgeAdvTrigDigFltrEnable |  |
| DAQmxGetDigEdgeAdvTrigEdge |  |
| DAQmxGetDigEdgeAdvTrigSrc |  |
| DAQmxGetDigEdgeArmStartTrigDigFltrEnable |  |
| DAQmxGetDigEdgeArmStartTrigDigFltrMinPulseWidth |  |
| DAQmxGetDigEdgeArmStartTrigDigFltrTimebaseRate |  |
| DAQmxGetDigEdgeArmStartTrigDigFltrTimebaseSrc |  |
| DAQmxGetDigEdgeArmStartTrigDigSyncEnable |  |
| DAQmxGetDigEdgeArmStartTrigEdge |  |
| DAQmxGetDigEdgeArmStartTrigSrc |  |
| DAQmxGetDigEdgeRefTrigDigFltrEnable |  |
| DAQmxGetDigEdgeRefTrigDigFltrMinPulseWidth |  |
| DAQmxGetDigEdgeRefTrigDigFltrTimebaseRate |  |
| DAQmxGetDigEdgeRefTrigDigFltrTimebaseSrc |  |
| DAQmxGetDigEdgeRefTrigDigSyncEnable |  |
| DAQmxGetDigEdgeRefTrigEdge |  |
| DAQmxGetDigEdgeRefTrigSrc |  |
| DAQmxGetDigEdgeStartTrigDigFltrEnable |  |
| DAQmxGetDigEdgeStartTrigDigFltrMinPulseWidth |  |
| DAQmxGetDigEdgeStartTrigDigFltrTimebaseRate |  |
| DAQmxGetDigEdgeStartTrigDigFltrTimebaseSrc |  |
| DAQmxGetDigEdgeStartTrigDigSyncEnable |  |
| DAQmxGetDigEdgeStartTrigEdge |  |
| DAQmxGetDigEdgeStartTrigSrc |  |
| DAQmxGetDigEdgeWatchdogExpirTrigEdge |  |
| DAQmxGetDigEdgeWatchdogExpirTrigSrc |  |
| DAQmxGetDigLvlPauseTrigDigFltrEnable |  |
| DAQmxGetDigLvlPauseTrigDigFltrMinPulseWidth |  |
| DAQmxGetDigLvlPauseTrigDigFltrTimebaseRate |  |
| DAQmxGetDigLvlPauseTrigDigFltrTimebaseSrc |  |
| DAQmxGetDigLvlPauseTrigDigSyncEnable |  |
| DAQmxGetDigLvlPauseTrigSrc |  |
| DAQmxGetDigLvlPauseTrigWhen |  |
| DAQmxGetDigPatternPauseTrigPattern |  |
| DAQmxGetDigPatternPauseTrigSrc |  |
| DAQmxGetDigPatternPauseTrigWhen |  |
| DAQmxGetDigPatternRefTrigPattern |  |
| DAQmxGetDigPatternRefTrigSrc |  |
| DAQmxGetDigPatternRefTrigWhen |  |
| DAQmxGetDigPatternStartTrigPattern |  |
| DAQmxGetDigPatternStartTrigSrc |  |
| DAQmxGetDigPatternStartTrigWhen |  |
| DAQmxGetExported10MHzRefClkOutputTerm |  |
| DAQmxGetExported20MHzTimebaseOutputTerm |  |
| DAQmxGetExportedAIConvClkOutputTerm |  |
| DAQmxGetExportedAIConvClkPulsePolarity |  |
| DAQmxGetExportedAIHoldCmpltEventOutputTerm |  |
| DAQmxGetExportedAIHoldCmpltEventPulsePolarity |  |
| DAQmxGetExportedAdvCmpltEventDelay |  |
| DAQmxGetExportedAdvCmpltEventOutputTerm |  |
| DAQmxGetExportedAdvCmpltEventPulsePolarity |  |
| DAQmxGetExportedAdvCmpltEventPulseWidth |  |
| DAQmxGetExportedAdvTrigOutputTerm |  |
| DAQmxGetExportedAdvTrigPulsePolarity |  |
| DAQmxGetExportedAdvTrigPulseWidth |  |
| DAQmxGetExportedAdvTrigPulseWidthUnits |  |
| DAQmxGetExportedChangeDetectEventOutputTerm |  |
| DAQmxGetExportedChangeDetectEventPulsePolarity |  |
| DAQmxGetExportedCtrOutEventOutputBehavior |  |
| DAQmxGetExportedCtrOutEventOutputTerm |  |
| DAQmxGetExportedCtrOutEventPulsePolarity |  |
| DAQmxGetExportedCtrOutEventToggleIdleState |  |
| DAQmxGetExportedDataActiveEventLvlActiveLvl |  |
| DAQmxGetExportedDataActiveEventOutputTerm |  |
| DAQmxGetExportedDividedSampClkTimebaseOutputTerm |  |
| DAQmxGetExportedHshkEventDelay |  |
| DAQmxGetExportedHshkEventInterlockedAssertOnStart |  |
| DAQmxGetExportedHshkEventInterlockedAssertedLvl |  |
| DAQmxGetExportedHshkEventInterlockedDeassertDelay |  |
| DAQmxGetExportedHshkEventOutputBehavior |  |
| DAQmxGetExportedHshkEventOutputTerm |  |
| DAQmxGetExportedHshkEventPulsePolarity |  |
| DAQmxGetExportedHshkEventPulseWidth |  |
| DAQmxGetExportedPauseTrigLvlActiveLvl |  |
| DAQmxGetExportedPauseTrigOutputTerm |  |
| DAQmxGetExportedRdyForStartEventLvlActiveLvl |  |
| DAQmxGetExportedRdyForStartEventOutputTerm |  |
| DAQmxGetExportedRdyForXferEventDeassertCond |  |
| DAQmxGetExportedRdyForXferEventDeassertCondCustomThreshold |  |
| DAQmxGetExportedRdyForXferEventLvlActiveLvl |  |
| DAQmxGetExportedRdyForXferEventOutputTerm |  |
| DAQmxGetExportedRefTrigOutputTerm |  |
| DAQmxGetExportedRefTrigPulsePolarity |  |
| DAQmxGetExportedSampClkDelayOffset |  |
| DAQmxGetExportedSampClkOutputBehavior |  |
| DAQmxGetExportedSampClkOutputTerm |  |
| DAQmxGetExportedSampClkPulsePolarity |  |
| DAQmxGetExportedSampClkTimebaseOutputTerm |  |
| DAQmxGetExportedStartTrigOutputTerm |  |
| DAQmxGetExportedStartTrigPulsePolarity |  |
| DAQmxGetExportedSyncPulseEventOutputTerm |  |
| DAQmxGetExportedWatchdogExpiredEventOutputTerm |  |
| DAQmxGetExtCalLastTemp |  |
| DAQmxGetExtCalRecommendedInterval |  |
| DAQmxGetFieldDAQBankDevNames |  |
| DAQmxGetFieldDAQDevName |  |
| DAQmxGetFirstSampClkOffset |  |
| DAQmxGetFirstSampClkTimescale |  |
| DAQmxGetFirstSampClkWhen |  |
| DAQmxGetFirstSampTimestampEnable |  |
| DAQmxGetFirstSampTimestampTimescale |  |
| DAQmxGetFirstSampTimestampVal |  |
| DAQmxGetHshkDelayAfterXfer |  |
| DAQmxGetHshkSampleInputDataWhen |  |
| DAQmxGetHshkStartCond |  |
| DAQmxGetHshkTrigType |  |
| DAQmxGetImplicitUnderflowBehavior |  |
| DAQmxGetInterlockedHshkTrigAssertedLvl |  |
| DAQmxGetInterlockedHshkTrigSrc |  |
| DAQmxGetLoggingFilePath |  |
| DAQmxGetLoggingFilePreallocationSize |  |
| DAQmxGetLoggingFileWriteSize |  |
| DAQmxGetLoggingMode |  |
| DAQmxGetLoggingPause |  |
| DAQmxGetLoggingSampsPerFile |  |
| DAQmxGetLoggingTDMSGroupName |  |
| DAQmxGetLoggingTDMSOperation |  |
| DAQmxGetMasterTimebaseRate |  |
| DAQmxGetMasterTimebaseSrc |  |
| DAQmxGetOnDemandSimultaneousAOEnable |  |
| DAQmxGetPauseTrigTerm |  |
| DAQmxGetPauseTrigType |  |
| DAQmxGetPersistedChanAllowInteractiveDeletion |  |
| DAQmxGetPersistedChanAllowInteractiveEditing |  |
| DAQmxGetPersistedChanAuthor |  |
| DAQmxGetPersistedScaleAllowInteractiveDeletion |  |
| DAQmxGetPersistedScaleAllowInteractiveEditing |  |
| DAQmxGetPersistedScaleAuthor |  |
| DAQmxGetPersistedTaskAllowInteractiveDeletion |  |
| DAQmxGetPersistedTaskAllowInteractiveEditing |  |
| DAQmxGetPersistedTaskAuthor |  |
| DAQmxGetPhysicalChanAIInputSrcs |  |
| DAQmxGetPhysicalChanAIPowerControlEnable |  |
| DAQmxGetPhysicalChanAIPowerControlType |  |
| DAQmxGetPhysicalChanAIPowerControlVoltage |  |
| DAQmxGetPhysicalChanAISensorPowerOpenChan |  |
| DAQmxGetPhysicalChanAISensorPowerOvercurrent |  |
| DAQmxGetPhysicalChanAISensorPowerTypes |  |
| DAQmxGetPhysicalChanAISensorPowerVoltageRangeVals |  |
| DAQmxGetPhysicalChanAISupportedMeasTypes |  |
| DAQmxGetPhysicalChanAITermCfgs |  |
| DAQmxGetPhysicalChanAOManualControlAmplitude |  |
| DAQmxGetPhysicalChanAOManualControlEnable |  |
| DAQmxGetPhysicalChanAOManualControlFreq |  |
| DAQmxGetPhysicalChanAOManualControlShortDetected |  |
| DAQmxGetPhysicalChanAOSupportedOutputTypes |  |
| DAQmxGetPhysicalChanAOSupportedPowerUpOutputTypes |  |
| DAQmxGetPhysicalChanAOTermCfgs |  |
| DAQmxGetPhysicalChanCISupportedMeasTypes |  |
| DAQmxGetPhysicalChanCOSupportedOutputTypes |  |
| DAQmxGetPhysicalChanDIChangeDetectSupported |  |
| DAQmxGetPhysicalChanDIPortWidth |  |
| DAQmxGetPhysicalChanDISampClkSupported |  |
| DAQmxGetPhysicalChanDISampModes |  |
| DAQmxGetPhysicalChanDOPortWidth |  |
| DAQmxGetPhysicalChanDOSampClkSupported |  |
| DAQmxGetPhysicalChanDOSampModes |  |
| DAQmxGetPhysicalChanDigPortLogicFamily |  |
| DAQmxGetPhysicalChanName |  |
| DAQmxGetPhysicalChanTEDSBitStream |  |
| DAQmxGetPhysicalChanTEDSMfgID |  |
| DAQmxGetPhysicalChanTEDSModelNum |  |
| DAQmxGetPhysicalChanTEDSSerialNum |  |
| DAQmxGetPhysicalChanTEDSTemplateIDs |  |
| DAQmxGetPhysicalChanTEDSVersionLetter |  |
| DAQmxGetPhysicalChanTEDSVersionNum |  |
| DAQmxGetPwrCurrentDevScalingCoeff |  |
| DAQmxGetPwrCurrentSetpoint |  |
| DAQmxGetPwrIdleOutputBehavior |  |
| DAQmxGetPwrOutputEnable |  |
| DAQmxGetPwrOutputState |  |
| DAQmxGetPwrRemoteSense |  |
| DAQmxGetPwrVoltageDevScalingCoeff |  |
| DAQmxGetPwrVoltageSetpoint |  |
| DAQmxGetReadAccessoryInsertionOrRemovalDetected |  |
| DAQmxGetReadAutoStart |  |
| DAQmxGetReadAvailSampPerChan |  |
| DAQmxGetReadChangeDetectHasOverflowed |  |
| DAQmxGetReadChannelsToRead |  |
| DAQmxGetReadCommonModeRangeErrorChans |  |
| DAQmxGetReadCommonModeRangeErrorChansExist |  |
| DAQmxGetReadCurrReadPos |  |
| DAQmxGetReadDevsWithInsertedOrRemovedAccessories |  |
| DAQmxGetReadDigitalLinesBytesPerChan |  |
| DAQmxGetReadExcitFaultChans |  |
| DAQmxGetReadExcitFaultChansExist |  |
| DAQmxGetReadInputLimitsFaultChans |  |
| DAQmxGetReadInputLimitsFaultChansExist |  |
| DAQmxGetReadNumChans |  |
| DAQmxGetReadOffset |  |
| DAQmxGetReadOpenChans |  |
| DAQmxGetReadOpenChansDetails |  |
| DAQmxGetReadOpenChansExist |  |
| DAQmxGetReadOpenCurrentLoopChans |  |
| DAQmxGetReadOpenCurrentLoopChansExist |  |
| DAQmxGetReadOpenThrmcplChans |  |
| DAQmxGetReadOpenThrmcplChansExist |  |
| DAQmxGetReadOverWrite |  |
| DAQmxGetReadOvercurrentChans |  |
| DAQmxGetReadOvercurrentChansExist |  |
| DAQmxGetReadOverloadedChans |  |
| DAQmxGetReadOverloadedChansExist |  |
| DAQmxGetReadOvertemperatureChans |  |
| DAQmxGetReadOvertemperatureChansExist |  |
| DAQmxGetReadPLLUnlockedChans |  |
| DAQmxGetReadPLLUnlockedChansExist |  |
| DAQmxGetReadPowerSupplyFaultChans |  |
| DAQmxGetReadPowerSupplyFaultChansExist |  |
| DAQmxGetReadRawDataWidth |  |
| DAQmxGetReadReadAllAvailSamp |  |
| DAQmxGetReadRelativeTo |  |
| DAQmxGetReadSleepTime |  |
| DAQmxGetReadSyncUnlockedChans |  |
| DAQmxGetReadSyncUnlockedChansExist |  |
| DAQmxGetReadTotalSampPerChanAcquired |  |
| DAQmxGetReadWaitMode |  |
| DAQmxGetRealTimeConvLateErrorsToWarnings |  |
| DAQmxGetRealTimeNumOfWarmupIters |  |
| DAQmxGetRealTimeReportMissedSamp |  |
| DAQmxGetRealTimeWaitForNextSampClkWaitMode |  |
| DAQmxGetRealTimeWriteRecoveryMode |  |
| DAQmxGetRefClkRate |  |
| DAQmxGetRefClkSrc |  |
| DAQmxGetRefTrigAutoTrigEnable |  |
| DAQmxGetRefTrigAutoTriggered |  |
| DAQmxGetRefTrigDelay |  |
| DAQmxGetRefTrigMaxNumTrigsToDetect |  |
| DAQmxGetRefTrigPretrigSamples |  |
| DAQmxGetRefTrigRetriggerWin |  |
| DAQmxGetRefTrigRetriggerable |  |
| DAQmxGetRefTrigTerm |  |
| DAQmxGetRefTrigTimestampEnable |  |
| DAQmxGetRefTrigTimestampTimescale |  |
| DAQmxGetRefTrigTimestampVal |  |
| DAQmxGetRefTrigTrigWin |  |
| DAQmxGetRefTrigType |  |
| DAQmxGetRemoteSenseErrorChans |  |
| DAQmxGetRemoteSenseErrorChansExist |  |
| DAQmxGetReverseVoltageErrorChans |  |
| DAQmxGetReverseVoltageErrorChansExist |  |
| DAQmxGetSampClkActiveEdge |  |
| DAQmxGetSampClkDigFltrEnable |  |
| DAQmxGetSampClkDigFltrMinPulseWidth |  |
| DAQmxGetSampClkDigFltrTimebaseRate |  |
| DAQmxGetSampClkDigFltrTimebaseSrc |  |
| DAQmxGetSampClkDigSyncEnable |  |
| DAQmxGetSampClkMaxRate |  |
| DAQmxGetSampClkOverrunBehavior |  |
| DAQmxGetSampClkRate |  |
| DAQmxGetSampClkSrc |  |
| DAQmxGetSampClkTerm |  |
| DAQmxGetSampClkTimebaseActiveEdge |  |
| DAQmxGetSampClkTimebaseDiv |  |
| DAQmxGetSampClkTimebaseMasterTimebaseDiv |  |
| DAQmxGetSampClkTimebaseRate |  |
| DAQmxGetSampClkTimebaseSrc |  |
| DAQmxGetSampClkTimebaseTerm |  |
| DAQmxGetSampClkUnderflowBehavior |  |
| DAQmxGetSampClkWriteWfmUseInitialWfmDT |  |
| DAQmxGetSampQuantSampMode |  |
| DAQmxGetSampQuantSampPerChan |  |
| DAQmxGetSampTimingEngine |  |
| DAQmxGetSampTimingType |  |
| DAQmxGetScaleDescr |  |
| DAQmxGetScaleLinSlope |  |
| DAQmxGetScaleLinYIntercept |  |
| DAQmxGetScaleMapPreScaledMax |  |
| DAQmxGetScaleMapPreScaledMin |  |
| DAQmxGetScaleMapScaledMax |  |
| DAQmxGetScaleMapScaledMin |  |
| DAQmxGetScalePolyForwardCoeff |  |
| DAQmxGetScalePolyReverseCoeff |  |
| DAQmxGetScalePreScaledUnits |  |
| DAQmxGetScaleScaledUnits |  |
| DAQmxGetScaleTablePreScaledVals |  |
| DAQmxGetScaleTableScaledVals |  |
| DAQmxGetScaleType |  |
| DAQmxGetSelfCalLastTemp |  |
| DAQmxGetSelfCalSupported |  |
| DAQmxGetStartTrigDelay |  |
| DAQmxGetStartTrigDelayUnits |  |
| DAQmxGetStartTrigMaxNumTrigsToDetect |  |
| DAQmxGetStartTrigRetriggerWin |  |
| DAQmxGetStartTrigRetriggerable |  |
| DAQmxGetStartTrigTerm |  |
| DAQmxGetStartTrigTimescale |  |
| DAQmxGetStartTrigTimestampEnable |  |
| DAQmxGetStartTrigTimestampTimescale |  |
| DAQmxGetStartTrigTimestampVal |  |
| DAQmxGetStartTrigTrigWhen |  |
| DAQmxGetStartTrigTrigWin |  |
| DAQmxGetStartTrigType |  |
| DAQmxGetSwitchChanAnlgBusSharingEnable |  |
| DAQmxGetSwitchChanBandwidth |  |
| DAQmxGetSwitchChanImpedance |  |
| DAQmxGetSwitchChanMaxACCarryCurrent |  |
| DAQmxGetSwitchChanMaxACCarryPwr |  |
| DAQmxGetSwitchChanMaxACSwitchCurrent |  |
| DAQmxGetSwitchChanMaxACSwitchPwr |  |
| DAQmxGetSwitchChanMaxACVoltage |  |
| DAQmxGetSwitchChanMaxDCCarryCurrent |  |
| DAQmxGetSwitchChanMaxDCCarryPwr |  |
| DAQmxGetSwitchChanMaxDCSwitchCurrent |  |
| DAQmxGetSwitchChanMaxDCSwitchPwr |  |
| DAQmxGetSwitchChanMaxDCVoltage |  |
| DAQmxGetSwitchChanUsage |  |
| DAQmxGetSwitchChanWireMode |  |
| DAQmxGetSwitchDevAutoConnAnlgBus |  |
| DAQmxGetSwitchDevNumColumns |  |
| DAQmxGetSwitchDevNumRelays |  |
| DAQmxGetSwitchDevNumRows |  |
| DAQmxGetSwitchDevNumSwitchChans |  |
| DAQmxGetSwitchDevPwrDownLatchRelaysAfterSettling |  |
| DAQmxGetSwitchDevRelayList |  |
| DAQmxGetSwitchDevSettled |  |
| DAQmxGetSwitchDevSettlingTime |  |
| DAQmxGetSwitchDevSwitchChanList |  |
| DAQmxGetSwitchDevTemperature |  |
| DAQmxGetSwitchDevTopology |  |
| DAQmxGetSwitchScanBreakMode |  |
| DAQmxGetSwitchScanRepeatMode |  |
| DAQmxGetSwitchScanWaitingForAdv |  |
| DAQmxGetSyncClkInterval |  |
| DAQmxGetSyncPulseMinDelayToStart |  |
| DAQmxGetSyncPulseResetDelay |  |
| DAQmxGetSyncPulseResetTime |  |
| DAQmxGetSyncPulseSrc |  |
| DAQmxGetSyncPulseSyncTime |  |
| DAQmxGetSyncPulseTerm |  |
| DAQmxGetSyncPulseTimeTimescale |  |
| DAQmxGetSyncPulseTimeWhen |  |
| DAQmxGetSyncPulseType |  |
| DAQmxGetSysDevNames |  |
| DAQmxGetSysGlobalChans |  |
| DAQmxGetSysNIDAQMajorVersion |  |
| DAQmxGetSysNIDAQMinorVersion |  |
| DAQmxGetSysNIDAQUpdateVersion |  |
| DAQmxGetSysScales |  |
| DAQmxGetSysTasks |  |
| DAQmxGetTaskChannels |  |
| DAQmxGetTaskComplete |  |
| DAQmxGetTaskDevices |  |
| DAQmxGetTaskName |  |
| DAQmxGetTaskNumChans |  |
| DAQmxGetTaskNumDevices |  |
| DAQmxGetTriggerSyncType |  |
| DAQmxGetWatchdogAOExpirState |  |
| DAQmxGetWatchdogAOOutputType |  |
| DAQmxGetWatchdogCOExpirState |  |
| DAQmxGetWatchdogDOExpirState |  |
| DAQmxGetWatchdogExpirTrigTrigOnNetworkConnLoss |  |
| DAQmxGetWatchdogExpirTrigType |  |
| DAQmxGetWatchdogHasExpired |  |
| DAQmxGetWatchdogTimeout |  |
| DAQmxGetWriteAccessoryInsertionOrRemovalDetected |  |
| DAQmxGetWriteCurrWritePos |  |
| DAQmxGetWriteDevsWithInsertedOrRemovedAccessories |  |
| DAQmxGetWriteDigitalLinesBytesPerChan |  |
| DAQmxGetWriteExternalOvervoltageChans |  |
| DAQmxGetWriteExternalOvervoltageChansExist |  |
| DAQmxGetWriteNumChans |  |
| DAQmxGetWriteOffset |  |
| DAQmxGetWriteOpenCurrentLoopChans |  |
| DAQmxGetWriteOpenCurrentLoopChansExist |  |
| DAQmxGetWriteOvercurrentChans |  |
| DAQmxGetWriteOvercurrentChansExist |  |
| DAQmxGetWriteOverloadedChans |  |
| DAQmxGetWriteOverloadedChansExist |  |
| DAQmxGetWriteOvertemperatureChans |  |
| DAQmxGetWriteOvertemperatureChansExist |  |
| DAQmxGetWritePowerSupplyFaultChans |  |
| DAQmxGetWritePowerSupplyFaultChansExist |  |
| DAQmxGetWriteRawDataWidth |  |
| DAQmxGetWriteRegenMode |  |
| DAQmxGetWriteRelativeTo |  |
| DAQmxGetWriteSleepTime |  |
| DAQmxGetWriteSpaceAvail |  |
| DAQmxGetWriteSyncUnlockedChans |  |
| DAQmxGetWriteSyncUnlockedChansExist |  |
| DAQmxGetWriteTotalSampPerChanGenerated |  |
| DAQmxGetWriteWaitMode |  |

#### Attachments

None

Parent topic:

Property Manipulation Functions

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga00774e63ded21b1f89bcdfe1f1141437.html language=enus -->
## TOPIC 00232: DAQmxGetPwrCurrentSetpoint

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga00774e63ded21b1f89bcdfe1f1141437.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga00774e63ded21b1f89bcdfe1f1141437.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetPwrCurrentSetpoint(TaskHandle taskHandle, const char channel[], float64 *data)RemarksDAQmxGetPwrCurrentSetpoint gets the Power Supply >> Current >> Setpoint property.

### DAQmxGetPwrCurrentSetpoint

#### Syntax

int32 __CFUNC DAQmxGetPwrCurrentSetpoint(TaskHandle taskHandle, const char channel[], float64 *data)

#### Remarks

DAQmxGetPwrCurrentSetpoint gets the [Power Supply >> Current >> Setpoint](group__ni-daqmx__c__properties__channel__power__supply__current_1ga243d6dabcbc0a57a9a6dc1d43a323b2a.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga026a4cfadf61d3b89a29a78ff378c5e7.html language=enus -->
## TOPIC 00233: DAQmxGetCIPeriodDigFltrTimebaseRate

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga026a4cfadf61d3b89a29a78ff378c5e7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga026a4cfadf61d3b89a29a78ff378c5e7.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetCIPeriodDigFltrTimebaseRate(TaskHandle taskHandle, const char channel[], float64 *data)RemarksDAQmxGetCIPeriodDigFltrTimebaseRate gets the Counter Input >> Period >> Input >> Digital Filter >> Timebase >> Rate property.

### DAQmxGetCIPeriodDigFltrTimebaseRate

#### Syntax

int32 __CFUNC DAQmxGetCIPeriodDigFltrTimebaseRate(TaskHandle taskHandle, const char channel[], float64 *data)

#### Remarks

DAQmxGetCIPeriodDigFltrTimebaseRate gets the [Counter Input >> Period >> Input >> Digital Filter >> Timebase >> Rate](group__ni-daqmx__c__properties__channel__counter__input__period__input__digital__filter__timebase_1ga9d0bcb490a5b361452fd5d2ed3ac2e45.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga026bc2df74760736e283ff5ad1059f82.html language=enus -->
## TOPIC 00234: DAQmxGetAnlgWinRefTrigCoupling

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga026bc2df74760736e283ff5ad1059f82.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga026bc2df74760736e283ff5ad1059f82.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetAnlgWinRefTrigCoupling(TaskHandle taskHandle, int32 *data)RemarksDAQmxGetAnlgWinRefTrigCoupling gets the Reference >> Analog Window >> Coupling property.

### DAQmxGetAnlgWinRefTrigCoupling

#### Syntax

int32 __CFUNC DAQmxGetAnlgWinRefTrigCoupling(TaskHandle taskHandle, int32 *data)

#### Remarks

DAQmxGetAnlgWinRefTrigCoupling gets the [Reference >> Analog Window >> Coupling](group__ni-daqmx__c__properties__trigger__reference__analog__window_1gae874e3e0846f5cb315893ed355320ef7.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga029bb4e5f63fcfa72ca383a9db9bc4c0.html language=enus -->
## TOPIC 00235: DAQmxGetAIBridgeShuntCalEnable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga029bb4e5f63fcfa72ca383a9db9bc4c0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga029bb4e5f63fcfa72ca383a9db9bc4c0.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetAIBridgeShuntCalEnable(TaskHandle taskHandle, const char channel[], bool32 *data)RemarksDAQmxGetAIBridgeShuntCalEnable gets the Analog Input >> General Properties >> Signal Conditioning >> Bridge >> Shunt Cal >> Shunt Cal Enable property.

### DAQmxGetAIBridgeShuntCalEnable

#### Syntax

int32 __CFUNC DAQmxGetAIBridgeShuntCalEnable(TaskHandle taskHandle, const char channel[], bool32 *data)

#### Remarks

DAQmxGetAIBridgeShuntCalEnable gets the [Analog Input >> General Properties >> Signal Conditioning >> Bridge >> Shunt Cal >> Shunt Cal Enable](group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal_1gaf92bd1eefecb0814750d4a4b334a89b2.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga02c0109f2ce2e2baef945c42113baf9e.html language=enus -->
## TOPIC 00236: DAQmxGetDigEdgeRefTrigEdge

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga02c0109f2ce2e2baef945c42113baf9e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga02c0109f2ce2e2baef945c42113baf9e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetDigEdgeRefTrigEdge(TaskHandle taskHandle, int32 *data)RemarksDAQmxGetDigEdgeRefTrigEdge gets the Reference >> Digital Edge >> Edge property.

### DAQmxGetDigEdgeRefTrigEdge

#### Syntax

int32 __CFUNC DAQmxGetDigEdgeRefTrigEdge(TaskHandle taskHandle, int32 *data)

#### Remarks

DAQmxGetDigEdgeRefTrigEdge gets the [Reference >> Digital Edge >> Edge](group__ni-daqmx__c__properties__trigger__reference__digital__edge_1ga133cc170fe2b310b257bb9d643e2d7b9.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga042a51c53b964b73f92203f7698a6c20.html language=enus -->
## TOPIC 00237: DAQmxGetSwitchDevSettled

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga042a51c53b964b73f92203f7698a6c20.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga042a51c53b964b73f92203f7698a6c20.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetSwitchDevSettled(const char deviceName[], bool32 *data)RemarksDAQmxGetSwitchDevSettled gets the Deprecated >> Is Settled property.

### DAQmxGetSwitchDevSettled

#### Syntax

int32 __CFUNC DAQmxGetSwitchDevSettled(const char deviceName[], bool32 *data)

#### Remarks

DAQmxGetSwitchDevSettled gets the [Deprecated >> Is Settled](group__ni-daqmx__c__properties__switchdevice__deprecated_1ga39c071a691e8d8fe66f9b861c77a9cd7.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga048be069938f9562e7305be59931e649.html language=enus -->
## TOPIC 00238: DAQmxGetCIEncoderBInputLogicLvlBehavior

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga048be069938f9562e7305be59931e649.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga048be069938f9562e7305be59931e649.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetCIEncoderBInputLogicLvlBehavior(TaskHandle taskHandle, const char channel[], int32 *data)RemarksDAQmxGetCIEncoderBInputLogicLvlBehavior gets the Counter Input >> Position >> B Input >> Logic Level Behavior property.

### DAQmxGetCIEncoderBInputLogicLvlBehavior

#### Syntax

int32 __CFUNC DAQmxGetCIEncoderBInputLogicLvlBehavior(TaskHandle taskHandle, const char channel[], int32 *data)

#### Remarks

DAQmxGetCIEncoderBInputLogicLvlBehavior gets the [Counter Input >> Position >> B Input >> Logic Level Behavior](group__ni-daqmx__c__properties__channel__counter__input__position__b__input_1ga1d1cdabe0faa92d09ede90548431c0f4.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga04c573a16765157781c54000f0a8a16c.html language=enus -->
## TOPIC 00239: DAQmxGetReadCommonModeRangeErrorChansExist

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga04c573a16765157781c54000f0a8a16c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga04c573a16765157781c54000f0a8a16c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetReadCommonModeRangeErrorChansExist(TaskHandle taskHandle, bool32 *data)RemarksDAQmxGetReadCommonModeRangeErrorChansExist gets the Status >> Common Mode Range Error >> Common Mode Range Error Channels Exist property.

### DAQmxGetReadCommonModeRangeErrorChansExist

#### Syntax

int32 __CFUNC DAQmxGetReadCommonModeRangeErrorChansExist(TaskHandle taskHandle, bool32 *data)

#### Remarks

DAQmxGetReadCommonModeRangeErrorChansExist gets the [Status >> Common Mode Range Error >> Common Mode Range Error Channels Exist](group__ni-daqmx__c__properties__read__status__common__mode__range__error_1gac7f149c120a6f1bfe1a95036a8636c04.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga04c9364aeb31feb560c7c2979e113cb9.html language=enus -->
## TOPIC 00240: DAQmxGetCIDutyCycleStartingEdge

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga04c9364aeb31feb560c7c2979e113cb9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga04c9364aeb31feb560c7c2979e113cb9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetCIDutyCycleStartingEdge(TaskHandle taskHandle, const char channel[], int32 *data)RemarksDAQmxGetCIDutyCycleStartingEdge gets the Counter Input >> Duty Cycle >> StartingEdge property.

### DAQmxGetCIDutyCycleStartingEdge

#### Syntax

int32 __CFUNC DAQmxGetCIDutyCycleStartingEdge(TaskHandle taskHandle, const char channel[], int32 *data)

#### Remarks

DAQmxGetCIDutyCycleStartingEdge gets the [Counter Input >> Duty Cycle >> StartingEdge](group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter__timebase_1ga371cf60d1ebb5c6fe65da140d34903d1.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga04d49dbeebead28b51bb2480232bc0ff.html language=enus -->
## TOPIC 00241: DAQmxGetCICtrTimebaseDigFltrTimebaseRate

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga04d49dbeebead28b51bb2480232bc0ff.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga04d49dbeebead28b51bb2480232bc0ff.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetCICtrTimebaseDigFltrTimebaseRate(TaskHandle taskHandle, const char channel[], float64 *data)RemarksDAQmxGetCICtrTimebaseDigFltrTimebaseRate gets the Counter Input >> General Properties >> Counter Timebase >> Digital Filter >> Timebase >> Rate property.

### DAQmxGetCICtrTimebaseDigFltrTimebaseRate

#### Syntax

int32 __CFUNC DAQmxGetCICtrTimebaseDigFltrTimebaseRate(TaskHandle taskHandle, const char channel[], float64 *data)

#### Remarks

DAQmxGetCICtrTimebaseDigFltrTimebaseRate gets the [Counter Input >> General Properties >> Counter Timebase >> Digital Filter >> Timebase >> Rate](group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase__digital__filter__timebase_1gaa82d02499d0f2bab14557b0b895ca030.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga04e25f3b7ca88a62270bc235aa90c44f.html language=enus -->
## TOPIC 00242: DAQmxGetCIFilterDelayUnits

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga04e25f3b7ca88a62270bc235aa90c44f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga04e25f3b7ca88a62270bc235aa90c44f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetCIFilterDelayUnits(TaskHandle taskHandle, const char channel[], int32 *data)RemarksDAQmxGetCIFilterDelayUnits gets the Counter Input >> General Properties >> Filter >> Filter Delay Units property.

### DAQmxGetCIFilterDelayUnits

#### Syntax

int32 __CFUNC DAQmxGetCIFilterDelayUnits(TaskHandle taskHandle, const char channel[], int32 *data)

#### Remarks

DAQmxGetCIFilterDelayUnits gets the [Counter Input >> General Properties >> Filter >> Filter Delay Units](group__ni-daqmx__c__properties__channel__counter__input__general__properties__filter_1ga524628da94f643c923414cb297d93e1f.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga0552e2b2785aed7846770ef6359f650f.html language=enus -->
## TOPIC 00243: DAQmxGetDigPatternPauseTrigWhen

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga0552e2b2785aed7846770ef6359f650f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga0552e2b2785aed7846770ef6359f650f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetDigPatternPauseTrigWhen(TaskHandle taskHandle, int32 *data)RemarksDAQmxGetDigPatternPauseTrigWhen gets the More >> Pause >> Digital Pattern >> Pause When property.

### DAQmxGetDigPatternPauseTrigWhen

#### Syntax

int32 __CFUNC DAQmxGetDigPatternPauseTrigWhen(TaskHandle taskHandle, int32 *data)

#### Remarks

DAQmxGetDigPatternPauseTrigWhen gets the [More >> Pause >> Digital Pattern >> Pause When](group__ni-daqmx__c__properties__trigger__more__pause__digital__pattern_1gafd73e5d6869ccc4d3e31f429ef5adf8f.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga05c199fcec3f1ad88c1747b8adbbbeca.html language=enus -->
## TOPIC 00244: DAQmxGetDevChassisModuleDevNames

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga05c199fcec3f1ad88c1747b8adbbbeca.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga05c199fcec3f1ad88c1747b8adbbbeca.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetDevChassisModuleDevNames(const char device[], char *data, uInt32 bufferSize)RemarksDAQmxGetDevChassisModuleDevNames gets the Chassis >> Module Device Names property.

### DAQmxGetDevChassisModuleDevNames

#### Syntax

int32 __CFUNC DAQmxGetDevChassisModuleDevNames(const char device[], char *data, uInt32 bufferSize)

#### Remarks

DAQmxGetDevChassisModuleDevNames gets the [Chassis >> Module Device Names](group__ni-daqmx__c__properties__device__chassis_1ga37a3f970e9f8de9070ee221e37434acd.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga0616f3a8eac8b9554522ad82a82b28a0.html language=enus -->
## TOPIC 00245: DAQmxGetReadChannelsToRead

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga0616f3a8eac8b9554522ad82a82b28a0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga0616f3a8eac8b9554522ad82a82b28a0.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetReadChannelsToRead(TaskHandle taskHandle, char *data, uInt32 bufferSize)RemarksDAQmxGetReadChannelsToRead gets the Channels to Read property.

### DAQmxGetReadChannelsToRead

#### Syntax

int32 __CFUNC DAQmxGetReadChannelsToRead(TaskHandle taskHandle, char *data, uInt32 bufferSize)

#### Remarks

DAQmxGetReadChannelsToRead gets the [Channels to Read](group__ni-daqmx__c__properties__read_1gad338eaacc8e88435cf18727f4562bb7f.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga099654fb7db607e66512b33a11cd6e99.html language=enus -->
## TOPIC 00246: DAQmxGetDevNumTimestampEngines

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga099654fb7db607e66512b33a11cd6e99.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga099654fb7db607e66512b33a11cd6e99.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetDevNumTimestampEngines(const char device[], uInt32 *data)RemarksDAQmxGetDevNumTimestampEngines gets the Time >> Number of Timestamp Engines property.

### DAQmxGetDevNumTimestampEngines

#### Syntax

int32 __CFUNC DAQmxGetDevNumTimestampEngines(const char device[], uInt32 *data)

#### Remarks

DAQmxGetDevNumTimestampEngines gets the [Time >> Number of Timestamp Engines](group__ni-daqmx__c__properties__device__time_1ga5e3d57b761eb2e23537c6f07a38cf9e0.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga0a051de11f25798436e09feb1ffb802b.html language=enus -->
## TOPIC 00247: DAQmxGetAIAutoZeroMode

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga0a051de11f25798436e09feb1ffb802b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga0a051de11f25798436e09feb1ffb802b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetAIAutoZeroMode(TaskHandle taskHandle, const char channel[], int32 *data)RemarksDAQmxGetAIAutoZeroMode gets the Analog Input >> General Properties >> Advanced >> High Accuracy Settings >> Auto Zero Mode property.

### DAQmxGetAIAutoZeroMode

#### Syntax

int32 __CFUNC DAQmxGetAIAutoZeroMode(TaskHandle taskHandle, const char channel[], int32 *data)

#### Remarks

DAQmxGetAIAutoZeroMode gets the [Analog Input >> General Properties >> Advanced >> High Accuracy Settings >> Auto Zero Mode](group__ni-daqmx__c__properties__channel__analog__input__general__properties__advanced__high__accuracy__settings_1gaed642febbea7270fedf9902cedd4df97.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga0ac3c2826e36f650bdbb129d407f5601.html language=enus -->
## TOPIC 00248: DAQmxGetDigLvlPauseTrigDigFltrTimebaseSrc

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga0ac3c2826e36f650bdbb129d407f5601.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga0ac3c2826e36f650bdbb129d407f5601.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetDigLvlPauseTrigDigFltrTimebaseSrc(TaskHandle taskHandle, char *data, uInt32 bufferSize)RemarksDAQmxGetDigLvlPauseTrigDigFltrTimebaseSrc gets the More >> Pause >> Digital Level >> Digital Filter >> Timebase >> Source property.

### DAQmxGetDigLvlPauseTrigDigFltrTimebaseSrc

#### Syntax

int32 __CFUNC DAQmxGetDigLvlPauseTrigDigFltrTimebaseSrc(TaskHandle taskHandle, char *data, uInt32 bufferSize)

#### Remarks

DAQmxGetDigLvlPauseTrigDigFltrTimebaseSrc gets the [More >> Pause >> Digital Level >> Digital Filter >> Timebase >> Source](group__ni-daqmx__c__properties__trigger__more__pause__digital__level__digital__filter__timebase_1ga1fbc1a7c77f642cd5a150872cfe45ebd.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga0b378ce15e8fdf3ee552bd67b3eb8f6c.html language=enus -->
## TOPIC 00249: DAQmxGetCOPulseHighTicks

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga0b378ce15e8fdf3ee552bd67b3eb8f6c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga0b378ce15e8fdf3ee552bd67b3eb8f6c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetCOPulseHighTicks(TaskHandle taskHandle, const char channel[], uInt32 *data)RemarksDAQmxGetCOPulseHighTicks gets the Counter Output >> Pulse >> Ticks >> High Ticks property.

### DAQmxGetCOPulseHighTicks

#### Syntax

int32 __CFUNC DAQmxGetCOPulseHighTicks(TaskHandle taskHandle, const char channel[], uInt32 *data)

#### Remarks

DAQmxGetCOPulseHighTicks gets the [Counter Output >> Pulse >> Ticks >> High Ticks](group__ni-daqmx__c__properties__channel__counter__output__pulse__ticks_1gaaaad7bad9dac5706cd41bb2b39eeb951.html) property.

Parent topic:

Getter functions for attributes

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__functions__property__manipulation__getter_1ga0bbb7a90c7ef6ccce6fabaecc97bb816.html language=enus -->
## TOPIC 00250: DAQmxGetStartTrigRetriggerable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__functions__property__manipulation__getter_1ga0bbb7a90c7ef6ccce6fabaecc97bb816.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__functions__property__manipulation__getter_1ga0bbb7a90c7ef6ccce6fabaecc97bb816.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __CFUNC DAQmxGetStartTrigRetriggerable(TaskHandle taskHandle, bool32 *data)RemarksDAQmxGetStartTrigRetriggerable gets the Start >> More >> Retriggerable property.

### DAQmxGetStartTrigRetriggerable

#### Syntax

int32 __CFUNC DAQmxGetStartTrigRetriggerable(TaskHandle taskHandle, bool32 *data)

#### Remarks

DAQmxGetStartTrigRetriggerable gets the [Start >> More >> Retriggerable](group__ni-daqmx__c__properties__trigger__start__more_1gaef8cfac3e4d50f25fd01e88170982691.html) property.

Parent topic:

Getter functions for attributes
