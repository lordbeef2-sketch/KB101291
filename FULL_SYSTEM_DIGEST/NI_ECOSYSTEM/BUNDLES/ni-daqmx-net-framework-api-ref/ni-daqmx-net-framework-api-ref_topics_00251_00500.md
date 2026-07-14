# NI DOCUMENT BUNDLE: ni-daqmx-net-framework-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-net-framework-api-ref start=251 end=500 -->
<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcalibrationscaletype.html language=enus -->
## TOPIC 00251: AIChannelCalibrationScaleType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcalibrationscaletype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcalibrationscaletype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method or equation form that the calibration scale uses. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIChannelCalibrationScaleTypeRemarksSpecifies the method or equation form that the calibration scale uses. Use this enumeration to get or set the value of CalibrationScaleType

### AIChannelCalibrationScaleType Enumeration

Specifies the method or equation form that the calibration scale uses.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIChannelCalibrationScaleType

#### Remarks

Specifies the method or equation form that the calibration scale uses. Use this enumeration to get or set the value of [CalibrationScaleType](nationalinstruments-daqmx-aichannel-calibrationscaletype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Polynomial | 10449 | Scale values by using an Nth order polynomial equation. |
| Table | 10450 | Map an array of prescaled values to an array of corresponding scaled values, with all other values scaled proportionally. |
| None | 10230 |  |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-all.html language=enus -->
## TOPIC 00252: All

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-all.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-all.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an AIChannel that operates on all of the channels in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel All { get; }RemarksAn AIChannel that operates on all of the channels in a task.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an

### All

Gets an [AIChannel](nationalinstruments-daqmx-aichannel.html) that operates on all of the channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) All { get; }

#### Remarks

An [AIChannel](nationalinstruments-daqmx-aichannel.html) that operates on all of the channels in a task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-copyto__array-int.html language=enus -->
## TOPIC 00253: CopyTo(Array, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-copyto__array-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-copyto__array-int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Copies the collection to an array or a portion of an array. This operation is not supported for AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic void CopyTo(Array array, int index)ParametersNameTypeDescriptionarrayArrayDestination array for the collection.indexintThe index in th

### CopyTo(Array, int)

Copies the collection to an array or a portion of an array. This operation is not supported for [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void CopyTo(Array array, int index)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| array | Array | Destination array for the collection. |
| index | int | The index in the target array at which you want to begin copying the collection to. |

#### Exceptions

| Type | Description |
| --- | --- |
| NotSupportedException | This method always throws a NotSupportedException. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-count.html language=enus -->
## TOPIC 00254: Count

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-count.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-count.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of elements in the collection. SyntaxNamespace: NationalInstruments.DAQmxpublic int Count { get; }RemarksThe number of elements contained in the collection.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Count

Gets the number of elements in the collection.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int Count { get; }

#### Remarks

The number of elements contained in the collection.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createaccelerationchargechannel__string-string-aiterminalconfiguration-double-double-aiaccelerationunits-double-aiaccelerationchargesensitivityunits.html language=enus -->
## TOPIC 00255: CreateAccelerationChargeChannel(string, string, AITerminalConfiguration, double, double, AIAccelerationUnits, double, AIAccelerationChargeSensitivityUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createaccelerationchargechannel__string-string-aiterminalconfiguration-double-double-aiaccelerationunits-double-aiaccelerationchargesensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createaccelerationchargechannel__string-string-aiterminalconfiguration-double-double-aiaccelerationunits-double-aiaccelerationchargesensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates channel(s) that use an accelerometer to measure acceleration and adds the channel(s) to the task you specify with taskHandle . SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateAccelerationChargeChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfigur

### CreateAccelerationChargeChannel(string, string, AITerminalConfiguration, double, double, AIAccelerationUnits, double, AIAccelerationChargeSensitivityUnits)

Creates channel(s) that use an accelerometer to measure acceleration and adds the channel(s) to the task you specify with *taskHandle* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateAccelerationChargeChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, AIAccelerationUnits units, double sensitivity, AIAccelerationChargeSensitivityUnits sensitivityUnits)

#### Remarks

Refer to [accelerometers](/csh?context=nidaqmx_daqhelp_accelerometers) in the *NI-DAQmx Help*.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignChannel | string | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel , you must use the names when you refer to these channels in other NI-DAQmx methods. |
| terminalConfiguration | AITerminalConfiguration | The input TerminalConfigurationTypes for the channel. |
| minimumValue | double | The minimum value, in units , that you expect to measure. |
| maximumValue | double | The maximum value, in units , that you expect to measure. |
| units | AIAccelerationUnits | The units to use to return acceleration measurements from the channel. |
| sensitivity | double | The sensitivity of the sensor. This value is in the units you specify with the sensitivityUnits input. Refer to the sensor documentation to determine this value. |
| sensitivityUnits | AIAccelerationChargeSensitivityUnits | The units of sensitivity . |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createaccelerationchargechannel__string-string-aiterminalconfiguration-double-double-string-double-aiaccelerationchargesensitivityunits.html language=enus -->
## TOPIC 00256: CreateAccelerationChargeChannel(string, string, AITerminalConfiguration, double, double, string, double, AIAccelerationChargeSensitivityUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createaccelerationchargechannel__string-string-aiterminalconfiguration-double-double-string-double-aiaccelerationchargesensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createaccelerationchargechannel__string-string-aiterminalconfiguration-double-double-string-double-aiaccelerationchargesensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates channel(s) that use an accelerometer to measure acceleration and adds the channel(s) to the task you specify with taskHandle . SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateAccelerationChargeChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfigur

### CreateAccelerationChargeChannel(string, string, AITerminalConfiguration, double, double, string, double, AIAccelerationChargeSensitivityUnits)

Creates channel(s) that use an accelerometer to measure acceleration and adds the channel(s) to the task you specify with *taskHandle* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateAccelerationChargeChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, string customScaleName, double sensitivity, AIAccelerationChargeSensitivityUnits sensitivityUnits)

#### Remarks

[FromCustomScale](nationalinstruments-daqmx-aiaccelerationunits.html). If you do not set units to [FromCustomScale](nationalinstruments-daqmx-aiaccelerationunits.html), you must set *customScaleName*  to null.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignChannel | string | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel , you must use the names when you refer to these channels in other NI-DAQmx methods. |
| terminalConfiguration | AITerminalConfiguration | The input TerminalConfigurationTypes for the channel. |
| minimumValue | double | The minimum value, in units , that you expect to measure. |
| maximumValue | double | The maximum value, in units , that you expect to measure. |
| customScaleName | string | The name of a custom scale to apply to the channel. To use this parameter, you must set units to |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sensitivity | double | The sensitivity of the sensor. This value is in the units you specify with the sensitivityUnits input. Refer to the sensor documentation to determine this value. |
| sensitivityUnits | AIAccelerationChargeSensitivityUnits | The units of sensitivity . |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createaccelerationfourwiredcvoltagechannel__string-string-aiterminalconfiguration-double-double-aiaccelerationunits-double-aiaccelerationfo...d249e446.html language=enus -->
## TOPIC 00257: CreateAccelerationFourWireDCVoltageChannel(string, string, AITerminalConfiguration, double, double, AIAccelerationUnits, double, AIAccelerationFourWireDCVoltageSensitivityUnits, AIExcitationSource, double, bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createaccelerationfourwiredcvoltagechannel__string-string-aiterminalconfiguration-double-double-aiaccelerationunits-double-aiaccelerationfo...d249e446.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createaccelerationfourwiredcvoltagechannel__string-string-aiterminalconfiguration-double-double-aiaccelerationunits-double-aiaccelerationfo...d249e446.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that measures acceleration using a 4-wire, DC voltage-based sensor connected to the channel. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateAccelerationFourWireDCVoltageChannel(string ph

### CreateAccelerationFourWireDCVoltageChannel(string, string, AITerminalConfiguration, double, double, AIAccelerationUnits, double, AIAccelerationFourWireDCVoltageSensitivityUnits, AIExcitationSource, double, bool)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that measures acceleration using a 4-wire, DC voltage-based sensor connected to the channel. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateAccelerationFourWireDCVoltageChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, AIAccelerationUnits units, double sensitivity, AIAccelerationFourWireDCVoltageSensitivityUnits sensitivityUnits, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, [MarshalAs(UnmanagedType.U1)] bool useExcitationForScaling)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. [CreateAccelerometerChannel(string, string, AITerminalConfiguration, double, double, double, AIAccelerometerSensitivityUnits, AIExcitationSource, double, AIAccelerationUnits)](nationalinstruments-daqmx-aichannelcollection-createaccelerometerchannel__string-string-aiterminalconfiguration-double-double-double-aiaccelerometersensitivityunits-aiexcitationsource-d...d249e1062.html) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignChannel | string | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel , you must use the names when you refer to these channels in other NI-DAQmx methods. |
| terminalConfiguration | AITerminalConfiguration | The input TerminalConfigurationTypes for the channel. |
| minimumValue | double | The minimum value, in units , that you expect to measure. |
| maximumValue | double | The maximum value, in units , that you expect to measure. |
| units | AIAccelerationUnits | The units to use to return acceleration measurements from the channel. |
| sensitivity | double | The sensitivity of the sensor. This value is in the units you specify with the sensitivityUnits input. Refer to the sensor documentation to determine this value. |
| sensitivityUnits | AIAccelerationFourWireDCVoltageSensitivityUnits | The units of sensitivity . |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values. |
| useExcitationForScaling | bool | Specifies whether NI-DAQmx divides the measurement by the excitation. You should typically set useExcitationForScaling to true for ratiometric transducers. If you set useExcitationForScaling to true , set maximumValue and minimumValue to reflect the scaling. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createaccelerationfourwiredcvoltagechannel__string-string-aiterminalconfiguration-double-double-string-double-aiaccelerationfourwiredcvolta...d249e651.html language=enus -->
## TOPIC 00258: CreateAccelerationFourWireDCVoltageChannel(string, string, AITerminalConfiguration, double, double, string, double, AIAccelerationFourWireDCVoltageSensitivityUnits, AIExcitationSource, double, bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createaccelerationfourwiredcvoltagechannel__string-string-aiterminalconfiguration-double-double-string-double-aiaccelerationfourwiredcvolta...d249e651.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createaccelerationfourwiredcvoltagechannel__string-string-aiterminalconfiguration-double-double-string-double-aiaccelerationfourwiredcvolta...d249e651.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that specifies the sensitivity of the 4-wire, DC voltage-based sensor connected to the channel. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateAccelerationFourWireDCVoltageChannel(string

### CreateAccelerationFourWireDCVoltageChannel(string, string, AITerminalConfiguration, double, double, string, double, AIAccelerationFourWireDCVoltageSensitivityUnits, AIExcitationSource, double, bool)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that specifies the sensitivity of the 4-wire, DC voltage-based sensor connected to the channel. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateAccelerationFourWireDCVoltageChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, string customScaleName, double sensitivity, AIAccelerationFourWireDCVoltageSensitivityUnits sensitivityUnits, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, [MarshalAs(UnmanagedType.U1)] bool useExcitationForScaling)

#### Remarks

[FromCustomScale](nationalinstruments-daqmx-aiaccelerationunits.html). If you do not set units to [FromCustomScale](nationalinstruments-daqmx-aiaccelerationunits.html), you must set *customScaleName*  to null.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. [CreateAccelerometerChannel(string, string, AITerminalConfiguration, double, double, double, AIAccelerometerSensitivityUnits, AIExcitationSource, double, AIAccelerationUnits)](nationalinstruments-daqmx-aichannelcollection-createaccelerometerchannel__string-string-aiterminalconfiguration-double-double-double-aiaccelerometersensitivityunits-aiexcitationsource-d...d249e1062.html) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignChannel | string | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel , you must use the names when you refer to these channels in other NI-DAQmx methods. |
| terminalConfiguration | AITerminalConfiguration | The input TerminalConfigurationTypes for the channel. |
| minimumValue | double | The minimum value, in units , that you expect to measure. |
| maximumValue | double | The maximum value, in units , that you expect to measure. |
| customScaleName | string | The name of a custom scale to apply to the channel. To use this parameter, you must set units to |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sensitivity | double | The sensitivity of the sensor. This value is in the units you specify with the sensitivityUnits input. Refer to the sensor documentation to determine this value. |
| sensitivityUnits | AIAccelerationFourWireDCVoltageSensitivityUnits | The units of sensitivity . |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | Specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values. |
| useExcitationForScaling | bool | Specifies whether NI-DAQmx divides the measurement by the excitation. You should typically set useExcitationForScaling to true for ratiometric transducers. If you set useExcitationForScaling to true , set maximumValue and minimumValue to reflect the scaling. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createaccelerometerchannel__string-string-aiterminalconfiguration-double-double-double-aiaccelerometersensitivityunits-aiexcitationsource-d...d249e1062.html language=enus -->
## TOPIC 00259: CreateAccelerometerChannel(string, string, AITerminalConfiguration, double, double, double, AIAccelerometerSensitivityUnits, AIExcitationSource, double, AIAccelerationUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createaccelerometerchannel__string-string-aiterminalconfiguration-double-double-double-aiaccelerometersensitivityunits-aiexcitationsource-d...d249e1062.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createaccelerometerchannel__string-string-aiterminalconfiguration-double-double-double-aiaccelerometersensitivityunits-aiexcitationsource-d...d249e1062.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses an accelerometer to measure acceleration. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateAccelerometerChannel(string physicalChannelName, string nameToAssignChannel, AITerminal

### CreateAccelerometerChannel(string, string, AITerminalConfiguration, double, double, double, AIAccelerometerSensitivityUnits, AIExcitationSource, double, AIAccelerationUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses an [accelerometer](/csh?context=nidaqmx_measfunds_accelerometers) to [measure acceleration](/csh?context=nidaqmx_daqhelp_accel). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateAccelerometerChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration configuration, double minimumValue, double maximumValue, double sensitivity, AIAccelerometerSensitivityUnits sensitivityUnits, AIExcitationSource currentExcitationSource, double currentExcitationValue, AIAccelerationUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateAccelerometerChannel(string, string, AITerminalConfiguration, double, double, double, AIAccelerometerSensitivityUnits, AIExcitationSource, double, AIAccelerationUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| configuration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| sensitivity | double | The sensitivity of the sensor. This value is in the units you specify with sensitivityUnits . Refer to sensor documentation to determine this value. |
| sensitivityUnits | AIAccelerometerSensitivityUnits | The units of sensitivity . |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amps that the sensor requires. |
| units | AIAccelerationUnits | The units to use to return the measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createaccelerometerchannel__string-string-aiterminalconfiguration-double-double-double-aiaccelerometersensitivityunits-aiexcitationsource-double-string.html language=enus -->
## TOPIC 00260: CreateAccelerometerChannel(string, string, AITerminalConfiguration, double, double, double, AIAccelerometerSensitivityUnits, AIExcitationSource, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createaccelerometerchannel__string-string-aiterminalconfiguration-double-double-double-aiaccelerometersensitivityunits-aiexcitationsource-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createaccelerometerchannel__string-string-aiterminalconfiguration-double-double-double-aiaccelerometersensitivityunits-aiexcitationsource-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale that uses an accelerometer to measure acceleration. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateAccelerometerChannel(string physicalChannelName, string

### CreateAccelerometerChannel(string, string, AITerminalConfiguration, double, double, double, AIAccelerometerSensitivityUnits, AIExcitationSource, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale that uses an [accelerometer](/csh?context=nidaqmx_measfunds_accelerometers) to [measure acceleration](/csh?context=nidaqmx_daqhelp_accel). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateAccelerometerChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration configuration, double minimumValue, double maximumValue, double sensitivity, AIAccelerometerSensitivityUnits sensitivityUnits, AIExcitationSource currentExcitationSource, double currentExcitationValue, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateAccelerometerChannel(string, string, AITerminalConfiguration, double, double, double, AIAccelerometerSensitivityUnits, AIExcitationSource, double, string) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| configuration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| sensitivity | double | The sensitivity of the sensor. This value is in the units you specify with sensitivityUnits . Refer to sensor documentation to determine this value. |
| sensitivityUnits | AIAccelerometerSensitivityUnits | The units of sensitivity . |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amps that the sensor requires. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createbridgechannel__string-string-double-double-aibridgeunits-aibridgeconfiguration-aiexcitationsource-double-double.html language=enus -->
## TOPIC 00261: CreateBridgeChannel(string, string, double, double, AIBridgeUnits, AIBridgeConfiguration, AIExcitationSource, double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createbridgechannel__string-string-double-double-aibridgeunits-aibridgeconfiguration-aiexcitationsource-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createbridgechannel__string-string-double-double-aibridgeunits-aibridgeconfiguration-aiexcitationsource-double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that measures voltage ratios from a Wheatstone bridge. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels

### CreateBridgeChannel(string, string, double, double, AIBridgeUnits, AIBridgeConfiguration, AIExcitationSource, double, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that measures [voltage ratios](/csh?context=nidaqmx_measfunds_bridgescaling) from a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque). Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html). Use a custom scale or other scaling code to convert the voltage ratios to physical units.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateBridgeChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIBridgeUnits units, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| units | AIBridgeUnits | The units to use to return the measurement. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createbridgechannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double.html language=enus -->
## TOPIC 00262: CreateBridgeChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createbridgechannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createbridgechannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that measures voltage ratios from a Wheatstone bridge, with the specified custom scale. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method a

### CreateBridgeChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that measures [voltage ratios](/csh?context=nidaqmx_measfunds_bridgescaling) from a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque), with the specified custom scale. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html). Use a custom scale or other scaling code to convert the voltage ratios to physical units.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateBridgeChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in custom scaled units. |
| maximumValue | double | The maximum value you expect to measure, in custom scaled units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createbuiltinsensortemperaturechannel__string-string-aitemperatureunits.html language=enus -->
## TOPIC 00263: CreateBuiltInSensorTemperatureChannel(string, string, AITemperatureUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createbuiltinsensortemperaturechannel__string-string-aitemperatureunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createbuiltinsensortemperaturechannel__string-string-aitemperatureunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel to measure temperature with a built-in sensor of a terminal block or device. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateBuiltInSensorTemperatureChannel(string physicalChannelName, st

### CreateBuiltInSensorTemperatureChannel(string, string, AITemperatureUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) to measure temperature with a built-in sensor of a terminal block or device. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateBuiltInSensorTemperatureChannel(string physicalChannelName, string nameToAssignChannel, AITemperatureUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

On SCXI modules, the built-in sensor might be the CJC sensor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateBuiltInSensorTemperatureChannel(string, string, AITemperatureUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| units | AITemperatureUnits | The units to use to return the measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createcalculatedpowerchannel__string-string-string-aiterminalconfiguration-double-double-double-double-aipowerunits-aicurrentshuntlocation-double-string.html language=enus -->
## TOPIC 00264: CreateCalculatedPowerChannel(string, string, string, AITerminalConfiguration, double, double, double, double, AIPowerUnits, AICurrentShuntLocation, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createcalculatedpowerchannel__string-string-string-aiterminalconfiguration-double-double-double-double-aipowerunits-aicurrentshuntlocation-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createcalculatedpowerchannel__string-string-string-aiterminalconfiguration-double-double-double-double-aipowerunits-aicurrentshuntlocation-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale and external shunt resistor to measure calculated power. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateCalculatedPowerChannel(string voltagePhysicalChann

### CreateCalculatedPowerChannel(string, string, string, AITerminalConfiguration, double, double, double, double, AIPowerUnits, AICurrentShuntLocation, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale and external shunt resistor to [measure calculated power](/csh?context=nidaqmx_daqhelp_measuring_calculated_power). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateCalculatedPowerChannel(string voltagePhysicalChannelName, string currentPhysicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double voltageMinimumValue, double voltageMaximumValue, double currentMinimumValue, double currentMaximumValue, AIPowerUnits units, AICurrentShuntLocation shuntResistorLoc, double externalShuntResistorValue, string customScaleName)

#### Remarks

This method creates a local virtual channel for every pair of voltage and current physical channel names you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx creates a default channel name. The format of this name is Power#, where # is an index number incremented to the first unique value. If you use default channel name to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method to fully specify the shunt resistor configuration.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateCalculatedPowerChannel(string, string, string, AITerminalConfiguration, double, double, double, double, AIPowerUnits, AICurrentShuntLocation, double, string) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| voltagePhysicalChannelName | string | The names of one or more voltage physical channels to use to create one or more local virtual power channels. |
| currentPhysicalChannelName | string | The names of one or more voltage physical channels to use to create one or more local virtual power channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual power channels. To use the default power channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| voltageMinimumValue | double | The voltage minimum value expected from the measurement, in units. |
| voltageMaximumValue | double | The voltage maximum value expected from the measurement, in units. |
| currentMinimumValue | double | The current minimum value expected from the measurement, in units. |
| currentMaximumValue | double | The current maximum value expected from the measurement, in units. |
| units | AIPowerUnits | The units to use to return the measurement. |
| shuntResistorLoc | AICurrentShuntLocation | The location of the shunt resistor. |
| externalShuntResistorValue | double | The value in ohms of an external shunt resistor. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createcalculatedpowerchannel__string-string-string-aiterminalconfiguration-double-double-double-double-aipowerunits-double.html language=enus -->
## TOPIC 00265: CreateCalculatedPowerChannel(string, string, string, AITerminalConfiguration, double, double, double, double, AIPowerUnits, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createcalculatedpowerchannel__string-string-string-aiterminalconfiguration-double-double-double-double-aipowerunits-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createcalculatedpowerchannel__string-string-string-aiterminalconfiguration-double-double-double-double-aipowerunits-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale and external shunt resistor to measure calculated power. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateCalculatedPowerChannel(string voltagePhysicalChann

### CreateCalculatedPowerChannel(string, string, string, AITerminalConfiguration, double, double, double, double, AIPowerUnits, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale and external shunt resistor to [measure calculated power](/csh?context=nidaqmx_daqhelp_measuring_calculated_power). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateCalculatedPowerChannel(string voltagePhysicalChannelName, string currentPhysicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double voltageMinimumValue, double voltageMaximumValue, double currentMinimumValue, double currentMaximumValue, AIPowerUnits units, double externalShuntResistorValue)

#### Remarks

This method creates a local virtual channel for every pair of voltage and current physical channel names you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx creates a default channel name. The format of this name is Power#, where # is an index number incremented to the first unique value. If you use default channel name to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method with devices that do not have a built-in shunt resistor. You must attach an external shunt resistor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateCalculatedPowerChannel(string, string, string, AITerminalConfiguration, double, double, double, double, AIPowerUnits, double) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| voltagePhysicalChannelName | string | The names of one or more voltage physical channels to use to create one or more local virtual power channels. |
| currentPhysicalChannelName | string | The names of one or more voltage physical channels to use to create one or more local virtual power channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual power channels. To use the default power channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| voltageMinimumValue | double | The voltage minimum value expected from the measurement, in units. |
| voltageMaximumValue | double | The voltage maximum value expected from the measurement, in units. |
| currentMinimumValue | double | The current minimum value expected from the measurement, in units. |
| currentMaximumValue | double | The current maximum value expected from the measurement, in units. |
| units | AIPowerUnits | The units to use to return the measurement. |
| externalShuntResistorValue | double | The value in ohms of an external shunt resistor. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createchargechannel__string-string-aiterminalconfiguration-double-double-aichargeunits.html language=enus -->
## TOPIC 00266: CreateChargeChannel(string, string, AITerminalConfiguration, double, double, AIChargeUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createchargechannel__string-string-aiterminalconfiguration-double-double-aichargeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createchargechannel__string-string-aiterminalconfiguration-double-double-aichargeunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel to measure acceleration using a charge-based sensor. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateChargeChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfig

### CreateChargeChannel(string, string, AITerminalConfiguration, double, double, AIChargeUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) to measure acceleration using a charge-based sensor. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateChargeChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, AIChargeUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. [CreateAccelerometerChannel(string, string, AITerminalConfiguration, double, double, double, AIAccelerometerSensitivityUnits, AIExcitationSource, double, AIAccelerationUnits)](nationalinstruments-daqmx-aichannelcollection-createaccelerometerchannel__string-string-aiterminalconfiguration-double-double-double-aiaccelerometersensitivityunits-aiexcitationsource-d...d249e1062.html) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignChannel | string | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel , you must use the names when you refer to these channels in other NI-DAQmx methods. |
| terminalConfiguration | AITerminalConfiguration | The input TerminalConfigurationTypes for the channel. |
| minimumValue | double | The minimum value, in units , that you expect to measure. |
| maximumValue | double | The maximum value, in units , that you expect to measure. |
| units | AIChargeUnits | The units to use to return acceleration measurements from the channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createchargechannel__string-string-aiterminalconfiguration-double-double-string.html language=enus -->
## TOPIC 00267: CreateChargeChannel(string, string, AITerminalConfiguration, double, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createchargechannel__string-string-aiterminalconfiguration-double-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createchargechannel__string-string-aiterminalconfiguration-double-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel to measure acceleration using a charge-based sensor. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateChargeChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfig

### CreateChargeChannel(string, string, AITerminalConfiguration, double, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) to measure acceleration using a charge-based sensor. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateChargeChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, string customScaleName)

#### Remarks

[FromCustomScale](nationalinstruments-daqmx-aiaccelerationunits.html). If you do not set units to [FromCustomScale](nationalinstruments-daqmx-aiaccelerationunits.html), you must set *customScaleName*  to null.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. [CreateAccelerometerChannel(string, string, AITerminalConfiguration, double, double, double, AIAccelerometerSensitivityUnits, AIExcitationSource, double, AIAccelerationUnits)](nationalinstruments-daqmx-aichannelcollection-createaccelerometerchannel__string-string-aiterminalconfiguration-double-double-double-aiaccelerometersensitivityunits-aiexcitationsource-d...d249e1062.html) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels. |
| nameToAssignChannel | string | The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel , you must use the names when you refer to these channels in other NI-DAQmx methods. |
| terminalConfiguration | AITerminalConfiguration | The input TerminalConfigurationTypes for the channel. |
| minimumValue | double | The minimum value, in units , that you expect to measure. |
| maximumValue | double | The maximum value, in units , that you expect to measure. |
| customScaleName | string | The name of a custom scale to apply to the channel. To use this parameter, you must set units to |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-aicurrentunits-aicurrentshuntlocation-double-string.html language=enus -->
## TOPIC 00268: CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, AICurrentUnits, AICurrentShuntLocation, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-aicurrentunits-aicurrentshuntlocation-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-aicurrentunits-aicurrentshuntlocation-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale and external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateCurrentChannel(string physicalChannelName, string nameToAss

### CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, AICurrentUnits, AICurrentShuntLocation, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale and external shunt resistor to [measure current](/csh?context=nidaqmx_daqhelp_measuring_current). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateCurrentChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, AICurrentUnits units, AICurrentShuntLocation shuntResistorLoc, double externalShuntResistorValue, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method to fully specify the shunt resistor configuration.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. [CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, double, string)](nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-double-string.html) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| units | AICurrentUnits | The units to use to return the measurement. |
| shuntResistorLoc | AICurrentShuntLocation | The location of the shunt resistor. |
| externalShuntResistorValue | double | The value in ohms of an external shunt resistor. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-aicurrentunits.html language=enus -->
## TOPIC 00269: CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, AICurrentUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-aicurrentunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-aicurrentunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateCurrentChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfig

### CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, AICurrentUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with an internal shunt resistor to [measure current](/csh?context=nidaqmx_daqhelp_measuring_current). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateCurrentChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, AICurrentUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method with devices that have a built-in shunt resistor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, AICurrentUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| units | AICurrentUnits | The units to use to return the measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-double-aicurrentunits.html language=enus -->
## TOPIC 00270: CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, double, AICurrentUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-double-aicurrentunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-double-aicurrentunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateCurrentChannel(string physicalChannelName, string nameToAssignChannel, AITer

### CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, double, AICurrentUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified external shunt resistor to [measure current](/csh?context=nidaqmx_daqhelp_measuring_current). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateCurrentChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, double externalShuntResistorValue, AICurrentUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method with devices that do not have a built-in shunt resistor. You must attach an external shunt resistor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, double, AICurrentUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| externalShuntResistorValue | double | The value in ohms of an external shunt resistor. |
| units | AICurrentUnits | The units to use to return the measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-double-string.html language=enus -->
## TOPIC 00271: CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale and external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateCurrentChannel(string physicalChannelName, string nameToAss

### CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale and external shunt resistor to [measure current](/csh?context=nidaqmx_daqhelp_measuring_current). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateCurrentChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, double externalShuntResistorValue, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method with devices that do not have a built-in shunt resistor. You must attach an external shunt resistor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, double, string) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| externalShuntResistorValue | double | The value in ohms of an external shunt resistor. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-string.html language=enus -->
## TOPIC 00272: CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale and an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateCurrentChannel(string physicalChannelName, string nameTo

### CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale and an internal shunt resistor to [measure current](/csh?context=nidaqmx_daqhelp_measuring_current). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateCurrentChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method with devices that have a built-in shunt resistor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, string) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createcurrentrmschannel__string-string-aiterminalconfiguration-double-double-aicurrentacrmsunits.html language=enus -->
## TOPIC 00273: CreateCurrentRmsChannel(string, string, AITerminalConfiguration, double, double, AICurrentAcrmsUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createcurrentrmschannel__string-string-aiterminalconfiguration-double-double-aicurrentacrmsunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createcurrentrmschannel__string-string-aiterminalconfiguration-double-double-aicurrentacrmsunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with an internal shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateCurrentRmsChannel(string physicalChannelName, string nameToAssignChannel, AITerminal

### CreateCurrentRmsChannel(string, string, AITerminalConfiguration, double, double, AICurrentAcrmsUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with an internal shunt resistor to [measure AC current](/csh?context=nidaqmx_daqhelp_measuring_current). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateCurrentRmsChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, AICurrentAcrmsUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method with devices that have a built-in shunt resistor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. [CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, AICurrentUnits)](nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-aicurrentunits.html) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| units | AICurrentAcrmsUnits | The units to use to return the measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createcurrentrmschannel__string-string-aiterminalconfiguration-double-double-double-aicurrentacrmsunits.html language=enus -->
## TOPIC 00274: CreateCurrentRmsChannel(string, string, AITerminalConfiguration, double, double, double, AICurrentAcrmsUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createcurrentrmschannel__string-string-aiterminalconfiguration-double-double-double-aicurrentacrmsunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createcurrentrmschannel__string-string-aiterminalconfiguration-double-double-double-aicurrentacrmsunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified external shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateCurrentRmsChannel(string physicalChannelName, string nameToAssignChannel,

### CreateCurrentRmsChannel(string, string, AITerminalConfiguration, double, double, double, AICurrentAcrmsUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified external shunt resistor to [measure AC current](/csh?context=nidaqmx_daqhelp_measuring_current). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateCurrentRmsChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, double externalShuntResistorValue, AICurrentAcrmsUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method with devices that do not have a built-in shunt resistor. You must attach an external shunt resistor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. [CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, double, AICurrentUnits)](nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-double-aicurrentunits.html) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value you expect to measure, in units . |
| maximumValue | double | The maximum value you expect to measure, in units . |
| externalShuntResistorValue | double | The value in ohms of an external shunt resistor. |
| units | AICurrentAcrmsUnits | The units to use to return the measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createcurrentrmschannel__string-string-aiterminalconfiguration-double-double-double-string.html language=enus -->
## TOPIC 00275: CreateCurrentRmsChannel(string, string, AITerminalConfiguration, double, double, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createcurrentrmschannel__string-string-aiterminalconfiguration-double-double-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createcurrentrmschannel__string-string-aiterminalconfiguration-double-double-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale and external shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateCurrentRmsChannel(string physicalChannelName, string nam

### CreateCurrentRmsChannel(string, string, AITerminalConfiguration, double, double, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale and external shunt resistor to [measure AC current](/csh?context=nidaqmx_daqhelp_measuring_current). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateCurrentRmsChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, double externalShuntResistorValue, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method with devices that do not have a built-in shunt resistor. You must attach an external shunt resistor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. [CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, double, string)](nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-double-string.html) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| externalShuntResistorValue | double | The value in ohms of an external shunt resistor. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createcurrentrmschannel__string-string-aiterminalconfiguration-double-double-string.html language=enus -->
## TOPIC 00276: CreateCurrentRmsChannel(string, string, AITerminalConfiguration, double, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createcurrentrmschannel__string-string-aiterminalconfiguration-double-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createcurrentrmschannel__string-string-aiterminalconfiguration-double-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale and an internal shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateCurrentRmsChannel(string physicalChannelName, string

### CreateCurrentRmsChannel(string, string, AITerminalConfiguration, double, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale and an internal shunt resistor to [measure AC current](/csh?context=nidaqmx_daqhelp_measuring_current). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateCurrentRmsChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method with devices that have a built-in shunt resistor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. [CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, string)](nationalinstruments-daqmx-aichannelcollection-createcurrentchannel__string-string-aiterminalconfiguration-double-double-string.html) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createdevicetemperaturechannel__string-string-aitemperatureunits.html language=enus -->
## TOPIC 00277: CreateDeviceTemperatureChannel(string, string, AITemperatureUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createdevicetemperaturechannel__string-string-aitemperatureunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createdevicetemperaturechannel__string-string-aitemperatureunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: The CreateDeviceTemperatureChannel method is deprecated. Please use the CreateBuiltInSensorTemperatureChannel method instead. Will warn if used Creates an AIChannel to measure temperature with a built-in sensor of a terminal block or device. This method adds one or more physical channels t

### CreateDeviceTemperatureChannel(string, string, AITemperatureUnits)

**Obsolete: The CreateDeviceTemperatureChannel method is deprecated. Please use the CreateBuiltInSensorTemperatureChannel method instead. Will warn if used** 
Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) to measure temperature with a built-in sensor of a terminal block or device. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html). The CreateDeviceTemperatureChannel(string, string, AITemperatureUnits) method has been deprecated in favor of the [CreateBuiltInSensorTemperatureChannel(string, string, AITemperatureUnits)](nationalinstruments-daqmx-aichannelcollection-createbuiltinsensortemperaturechannel__string-string-aitemperatureunits.html) method.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateDeviceTemperatureChannel(string physicalChannelName, string nameToAssignChannel, AITemperatureUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

On SCXI modules, the built-in sensor might be the CJC sensor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateDeviceTemperatureChannel(string, string, AITemperatureUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| units | AITemperatureUnits | The units to use to return the measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createeddycurrentproximityprobechannel__string-string-double-double-double-aieddycurrentproximityprobesensitivityunits-aieddycurrentproximityprobeunits.html language=enus -->
## TOPIC 00278: CreateEddyCurrentProximityProbeChannel(string, string, double, double, double, AIEddyCurrentProximityProbeSensitivityUnits, AIEddyCurrentProximityProbeUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createeddycurrentproximityprobechannel__string-string-double-double-double-aieddycurrentproximityprobesensitivityunits-aieddycurrentproximityprobeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createeddycurrentproximityprobechannel__string-string-double-double-double-aieddycurrentproximityprobesensitivityunits-aieddycurrentproximityprobeunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses an Eddy Current Proximity Probe to measure position. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateEddyCurrentProximityProbeChannel(string physicalChannelName, string nameToAs

### CreateEddyCurrentProximityProbeChannel(string, string, double, double, double, AIEddyCurrentProximityProbeSensitivityUnits, AIEddyCurrentProximityProbeUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses an [Eddy Current Proximity Probe](/csh?context=nidaqmx_measfunds_eddycurrentproximityprobe) to [measure position](/csh?context=nidaqmx_daqhelp_measuring_proximity). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateEddyCurrentProximityProbeChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, double sensitivity, AIEddyCurrentProximityProbeSensitivityUnits sensitivityUnits, AIEddyCurrentProximityProbeUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateEddyCurrentProximityProbeChannel(string, string, double, double, double, AIEddyCurrentProximityProbeSensitivityUnits, AIEddyCurrentProximityProbeUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| sensitivity | double | The sensitivity of the sensor. This value is in the units you specify with sensitivityUnits . Refer to the sensor documentation to determine this value. |
| sensitivityUnits | AIEddyCurrentProximityProbeSensitivityUnits | The units of sensitivity . |
| units | AIEddyCurrentProximityProbeUnits | Specifies the units to use to return position measurements from the channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createeddycurrentproximityprobechannel__string-string-double-double-double-aieddycurrentproximityprobesensitivityunits-string.html language=enus -->
## TOPIC 00279: CreateEddyCurrentProximityProbeChannel(string, string, double, double, double, AIEddyCurrentProximityProbeSensitivityUnits, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createeddycurrentproximityprobechannel__string-string-double-double-double-aieddycurrentproximityprobesensitivityunits-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createeddycurrentproximityprobechannel__string-string-double-double-double-aieddycurrentproximityprobesensitivityunits-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale that uses an Eddy Current Proximity Probe to measure position. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateEddyCurrentProximityProbeChannel(string phys

### CreateEddyCurrentProximityProbeChannel(string, string, double, double, double, AIEddyCurrentProximityProbeSensitivityUnits, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale that uses an [Eddy Current Proximity Probe](/csh?context=nidaqmx_measfunds_eddycurrentproximityprobe) to [measure position](/csh?context=nidaqmx_daqhelp_measuring_proximity). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateEddyCurrentProximityProbeChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, double sensitivity, AIEddyCurrentProximityProbeSensitivityUnits sensitivityUnits, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateEddyCurrentProximityProbeChannel(string, string, double, double, double, AIEddyCurrentProximityProbeSensitivityUnits, string) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| sensitivity | double | The sensitivity of the sensor. This value is in the units you specify with sensitivityUnits . Refer to the sensor documentation to determine this value. |
| sensitivityUnits | AIEddyCurrentProximityProbeSensitivityUnits | The units of sensitivity . |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createforcebridgepolynomialchannel__string-string-double-double-aiforceunits-aibridgeconfiguration-aiexcitationsource-double-double-double_...d249e4446.html language=enus -->
## TOPIC 00280: CreateForceBridgePolynomialChannel(string, string, double, double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createforcebridgepolynomialchannel__string-string-double-double-aiforceunits-aibridgeconfiguration-aiexcitationsource-double-double-double_...d249e4446.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createforcebridgepolynomialchannel__string-string-double-double-aiforceunits-aibridgeconfiguration-aiexcitationsource-double-double-double_...d249e4446.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electri

### CreateForceBridgePolynomialChannel(string, string, double, double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure force or load](/csh?context=nidaqmx_daqhelp_force). Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use [PolynomialScale](nationalinstruments-daqmx-polynomialscale.html) to generate the other set. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateForceBridgePolynomialChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIForceUnits units, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double[] forwardCoefficients, double[] reverseCoefficients, AIBridgeElectricalUnits electricalUnits, AIBridgePhysicalUnits physicalUnits)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| units | AIForceUnits | The units to use to return the measurement. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| forwardCoefficients | double[] | The array of the forward coefficients of the polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x3. |
| reverseCoefficients | double[] | The array of the reverse coefficients of the polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9y3. |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createforcebridgepolynomialchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-d...d249e4225.html language=enus -->
## TOPIC 00281: CreateForceBridgePolynomialChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createforcebridgepolynomialchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-d...d249e4225.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createforcebridgepolynomialchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-d...d249e4225.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a

### CreateForceBridgePolynomialChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure force or load](/csh?context=nidaqmx_daqhelp_force), with the specified custom scale. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use [PolynomialScale](nationalinstruments-daqmx-polynomialscale.html) to generate the other set. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateForceBridgePolynomialChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double[] forwardCoefficients, double[] reverseCoefficients, AIBridgeElectricalUnits electricalUnits, AIBridgePhysicalUnits physicalUnits)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in custom scaled units. |
| maximumValue | double | The maximum value you expect to measure, in custom scaled units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| forwardCoefficients | double[] | The array of the forward coefficients of the polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x3. |
| reverseCoefficients | double[] | The array of the reverse coefficients of the polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9y3. |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createforcebridgetablechannel__string-string-double-double-aiforceunits-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-...d249e4889.html language=enus -->
## TOPIC 00282: CreateForceBridgeTableChannel(string, string, double, double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createforcebridgetablechannel__string-string-double-double-aiforceunits-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-...d249e4889.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createforcebridgetablechannel__string-string-double-double-aiforceunits-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-...d249e4889.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrica

### CreateForceBridgeTableChannel(string, string, double, double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure force or load](/csh?context=nidaqmx_daqhelp_force). Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateForceBridgeTableChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIForceUnits units, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double[] electricalValues, AIBridgeElectricalUnits electricalUnits, double[] physicalValues, AIBridgePhysicalUnits physicalUnits)

#### Remarks

Specify different values for *physical units*  if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| units | AIForceUnits | The units to use to return the measurement. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| electricalValues | double[] | The array of electrical values that map to the values in physicalValues . Specify this value in the units specified with electricalUnits . |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| physicalValues | double[] | The array of physical values that map to the values in electricalValues . Specify this value in the units specified with physicalUnits . |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createforcebridgetablechannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-aibrid...d249e4665.html language=enus -->
## TOPIC 00283: CreateForceBridgeTableChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createforcebridgetablechannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-aibrid...d249e4665.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createforcebridgetablechannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-aibrid...d249e4665.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scali

### CreateForceBridgeTableChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure force or load](/csh?context=nidaqmx_daqhelp_force), with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateForceBridgeTableChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double[] electricalValues, AIBridgeElectricalUnits electricalUnits, double[] physicalValues, AIBridgePhysicalUnits physicalUnits)

#### Remarks

Specify different values for *physical units*  if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in custom scaled units. |
| maximumValue | double | The maximum value you expect to measure, in custom scaled units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| electricalValues | double[] | The array of electrical values that map to the values in physicalValues . Specify this value in the units specified with electricalUnits . |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| physicalValues | double[] | The array of physical values that map to the values in electricalValues . Specify this value in the units specified with physicalUnits . |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createforcebridgetwopointlinearchannel__string-string-double-double-aiforceunits-aibridgeconfiguration-aiexcitationsource-double-double-dou...d249e5110.html language=enus -->
## TOPIC 00284: CreateForceBridgeTwoPointLinearChannel(string, string, double, double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createforcebridgetwopointlinearchannel__string-string-double-double-aiforceunits-aibridgeconfiguration-aiexcitationsource-double-double-dou...d249e5110.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createforcebridgetwopointlinearchannel__string-string-double-double-aiforceunits-aibridgeconfiguration-aiexcitationsource-double-double-dou...d249e5110.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical v

### CreateForceBridgeTwoPointLinearChannel(string, string, double, double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure force or load](/csh?context=nidaqmx_daqhelp_force). Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateForceBridgeTwoPointLinearChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIForceUnits units, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double firstElectricalValue, double secondElectricalValue, AIBridgeElectricalUnits electricalUnits, double firstPhysicalValue, double secondPhysicalValue, AIBridgePhysicalUnits physicalUnits)

#### Remarks

Specify different values for *physical units*  if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| units | AIForceUnits | The units to use to return the measurement. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| firstElectricalValue | double | The first electrical value, corresponding to firstPhysicalValue . Specify this value in the units specified with electricalUnits . |
| secondElectricalValue | double | The second electrical value, corresponding to secondPhysicalValue . Specify this value in the units specified with electricalUnits . |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| firstPhysicalValue | double | The first physical value, corresponding to firstElectricalValue . Specify this value in the units specified with physicalUnits . |
| secondPhysicalValue | double | The second physical value, corresponding to secondElectricalValue . Specify this value in the units specified with physicalUnits . |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createforcebridgetwopointlinearchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double-do...d249e5358.html language=enus -->
## TOPIC 00285: CreateForceBridgeTwoPointLinearChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createforcebridgetwopointlinearchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double-do...d249e5358.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createforcebridgetwopointlinearchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double-do...d249e5358.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two po

### CreateForceBridgeTwoPointLinearChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure force or load](/csh?context=nidaqmx_daqhelp_force), with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateForceBridgeTwoPointLinearChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double firstElectricalValue, double secondElectricalValue, AIBridgeElectricalUnits electricalUnits, double firstPhysicalValue, double secondPhysicalValue, AIBridgePhysicalUnits physicalUnits)

#### Remarks

Specify different values for *physical units*  if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in custom scaled units. |
| maximumValue | double | The maximum value you expect to measure, in custom scaled units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| firstElectricalValue | double | The first electrical value, corresponding to firstPhysicalValue . Specify this value in the units specified with electricalUnits . |
| secondElectricalValue | double | The second electrical value, corresponding to secondPhysicalValue . Specify this value in the units specified with electricalUnits . |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| firstPhysicalValue | double | The first physical value, corresponding to firstElectricalValue . Specify this value in the units specified with physicalUnits . |
| secondPhysicalValue | double | The second physical value, corresponding to secondElectricalValue . Specify this value in the units specified with physicalUnits . |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createforceiepechannel__string-string-aiterminalconfiguration-double-double-aiforceunits-double-aiforceiepesensorsensitivityunits-aiexcitat...d249e5803.html language=enus -->
## TOPIC 00286: CreateForceIepeChannel(string, string, AITerminalConfiguration, double, double, AIForceUnits, double, AIForceIepeSensorSensitivityUnits, AIExcitationSource, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createforceiepechannel__string-string-aiterminalconfiguration-double-double-aiforceunits-double-aiforceiepesensorsensitivityunits-aiexcitat...d249e5803.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createforceiepechannel__string-string-aiterminalconfiguration-double-double-aiforceunits-double-aiforceiepesensorsensitivityunits-aiexcitat...d249e5803.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses an IEPE force sensor to measure force or load. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateForceIepeChannel(string physicalChannelName, string nameToAssignChannel, AITermina

### CreateForceIepeChannel(string, string, AITerminalConfiguration, double, double, AIForceUnits, double, AIForceIepeSensorSensitivityUnits, AIExcitationSource, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses an [IEPE force sensor](/csh?context=nidaqmx_measfunds_forcepiezo) to [measure force or load](/csh?context=nidaqmx_daqhelp_force). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateForceIepeChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, AIForceUnits units, double sensitivity, AIForceIepeSensorSensitivityUnits sensitivityUnits, AIExcitationSource currentExcitationSource, double currentExcitationValue)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of – 1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| units | AIForceUnits | The units to use to return the measurement. |
| sensitivity | double | The sensitivity of the sensor. This value is in the units you specify with sensitivityUnits . Refer to the sensor documentation to determine this value. |
| sensitivityUnits | AIForceIepeSensorSensitivityUnits | The units of sensitivity . |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation, in amperes, that the sensor requires. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createforceiepechannel__string-string-aiterminalconfiguration-double-double-string-double-aiforceiepesensorsensitivityunits-aiexcitationsource-double.html language=enus -->
## TOPIC 00287: CreateForceIepeChannel(string, string, AITerminalConfiguration, double, double, string, double, AIForceIepeSensorSensitivityUnits, AIExcitationSource, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createforceiepechannel__string-string-aiterminalconfiguration-double-double-string-double-aiforceiepesensorsensitivityunits-aiexcitationsource-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createforceiepechannel__string-string-aiterminalconfiguration-double-double-string-double-aiforceiepesensorsensitivityunits-aiexcitationsource-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses an IEPE force sensor to measure force or load, with the specified custom scale. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateForceIepeChannel(string physicalChannelName, stri

### CreateForceIepeChannel(string, string, AITerminalConfiguration, double, double, string, double, AIForceIepeSensorSensitivityUnits, AIExcitationSource, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses an [IEPE force sensor](/csh?context=nidaqmx_measfunds_forcepiezo) to [measure force or load](/csh?context=nidaqmx_daqhelp_force), with the specified custom scale. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateForceIepeChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, string customScaleName, double sensitivity, AIForceIepeSensorSensitivityUnits sensitivityUnits, AIExcitationSource currentExcitationSource, double currentExcitationValue)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of – 1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |
| sensitivity | double | The sensitivity of the sensor. This value is in the units you specify with sensitivityUnits . Refer to the sensor documentation to determine this value. |
| sensitivityUnits | AIForceIepeSensorSensitivityUnits | The units of sensitivity . |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation, in amperes, that the sensor requires. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createfrequencyvoltagechannel__string-string-double-double-double-double-aifrequencyunits.html language=enus -->
## TOPIC 00288: CreateFrequencyVoltageChannel(string, string, double, double, double, double, AIFrequencyUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createfrequencyvoltagechannel__string-string-double-double-double-double-aifrequencyunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createfrequencyvoltagechannel__string-string-double-double-double-double-aifrequencyunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel to measure frequency using a frequency-to-voltage converter. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateFrequencyVoltageChannel(string physicalChannelName, string nameToAssignChannel

### CreateFrequencyVoltageChannel(string, string, double, double, double, double, AIFrequencyUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) to [measure frequency](/csh?context=nidaqmx_daqhelp_meas_analog_freq) using a frequency-to-voltage converter. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateFrequencyVoltageChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, double thresholdVoltage, double hysteresis, AIFrequencyUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateFrequencyVoltageChannel(string, string, double, double, double, double, AIFrequencyUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| thresholdVoltage | double | The voltage level at which to recognize waveform repetitions. You should select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls. |
| hysteresis | double | A window, in volts, below thresholdVoltage . The input voltage must pass below thresholdVoltage minus hysteresis before NI-DAQmx recognizes a waveform repetition. Hysteresis can improve the measurement accuracy when the signal contains noise or jitter. |
| units | AIFrequencyUnits | The units to use to return the measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createfrequencyvoltagechannel__string-string-double-double-double-double-string.html language=enus -->
## TOPIC 00289: CreateFrequencyVoltageChannel(string, string, double, double, double, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createfrequencyvoltagechannel__string-string-double-double-double-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createfrequencyvoltagechannel__string-string-double-double-double-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale to measure frequency using a frequency-to-voltage converter. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateFrequencyVoltageChannel(string physicalChannel

### CreateFrequencyVoltageChannel(string, string, double, double, double, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale to [measure frequency](/csh?context=nidaqmx_daqhelp_meas_analog_freq) using a frequency-to-voltage converter. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateFrequencyVoltageChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, double thresholdVoltage, double hysteresis, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateFrequencyVoltageChannel(string, string, double, double, double, double, string) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| thresholdVoltage | double | The voltage level at which to recognize waveform repetitions. You should select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls. |
| hysteresis | double | A window, in volts, below thresholdVoltage . The input voltage must pass below thresholdVoltage minus hysteresis before NI-DAQmx recognizes a waveform repetition. Hysteresis can improve the measurement accuracy when the signal contains noise or jitter. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createlvdtchannel__string-string-double-double-double-ailvdtsensitivityunits-aiexcitationsource-double-double-aiacexcitationwiremode-ailvdtunits.html language=enus -->
## TOPIC 00290: CreateLvdtChannel(string, string, double, double, double, AILvdtSensitivityUnits, AIExcitationSource, double, double, AIACExcitationWireMode, AILvdtUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createlvdtchannel__string-string-double-double-double-ailvdtsensitivityunits-aiexcitationsource-double-double-aiacexcitationwiremode-ailvdtunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createlvdtchannel__string-string-double-double-double-ailvdtsensitivityunits-aiexcitationsource-double-double-aiacexcitationwiremode-ailvdtunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateLvdtChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, doub

### CreateLvdtChannel(string, string, double, double, double, AILvdtSensitivityUnits, AIExcitationSource, double, double, AIACExcitationWireMode, AILvdtUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses an [LVDT](/csh?context=nidaqmx_measfunds_lvdts) to [measure linear position](/csh?context=nidaqmx_daqhelp_lindisplacelvdt). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateLvdtChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, double sensitivity, AILvdtSensitivityUnits sensitivityUnits, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double voltageExcitationFrequency, AIACExcitationWireMode voltageExcitationWireMode, AILvdtUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateLvdtChannel(string, string, double, double, double, AILvdtSensitivityUnits, AIExcitationSource, double, double, AIACExcitationWireMode, AILvdtUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| sensitivity | double | The sensitivity of the sensor. This value is in the units you specify with sensitivityUnits . Refer to the sensor documentation to determine this value. |
| sensitivityUnits | AILvdtSensitivityUnits | The units of sensitivity . |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. |
| voltageExcitationFrequency | double | The excitation frequency that the sensor requires, in hertz. Refer to the sensor documentation to determine this value. |
| voltageExcitationWireMode | AIACExcitationWireMode | The number of leads on the sensor. Some sensors might require you to tie leads together to create a four- or five-wire sensor. Refer to the documentation for your sensor for more information. |
| units | AILvdtUnits | The units to use to return the measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createlvdtchannel__string-string-double-double-double-ailvdtsensitivityunits-aiexcitationsource-double-double-aiacexcitationwiremode-string.html language=enus -->
## TOPIC 00291: CreateLvdtChannel(string, string, double, double, double, AILvdtSensitivityUnits, AIExcitationSource, double, double, AIACExcitationWireMode, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createlvdtchannel__string-string-double-double-double-ailvdtsensitivityunits-aiexcitationsource-double-double-aiacexcitationwiremode-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createlvdtchannel__string-string-double-double-double-ailvdtsensitivityunits-aiexcitationsource-double-double-aiacexcitationwiremode-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateLvdtChannel(string physicalChannelName, string nameToAssignCh

### CreateLvdtChannel(string, string, double, double, double, AILvdtSensitivityUnits, AIExcitationSource, double, double, AIACExcitationWireMode, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale that uses an [LVDT](/csh?context=nidaqmx_measfunds_lvdts) to [measure linear position](/csh?context=nidaqmx_daqhelp_lindisplacelvdt). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateLvdtChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, double sensitivity, AILvdtSensitivityUnits sensitivityUnits, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double voltageExcitationFrequency, AIACExcitationWireMode voltageExcitationWireMode, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateLvdtChannel(string, string, double, double, double, AILvdtSensitivityUnits, AIExcitationSource, double, double, AIACExcitationWireMode, string) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| sensitivity | double | The sensitivity of the sensor. This value is in the units you specify with sensitivityUnits . Refer to the sensor documentation to determine this value. |
| sensitivityUnits | AILvdtSensitivityUnits | The units of sensitivity . |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. |
| voltageExcitationFrequency | double | The excitation frequency that the sensor requires, in hertz. Refer to the sensor documentation to determine this value. |
| voltageExcitationWireMode | AIACExcitationWireMode | The number of leads on the sensor. Some sensors might require you to tie leads together to create a four- or five-wire sensor. Refer to the documentation for your sensor for more information. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createmicrophonechannel__string-string-double-double-aiterminalconfiguration-aiexcitationsource-double-aisoundpressureunits.html language=enus -->
## TOPIC 00292: CreateMicrophoneChannel(string, string, double, double, AITerminalConfiguration, AIExcitationSource, double, AISoundPressureUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createmicrophonechannel__string-string-double-double-aiterminalconfiguration-aiexcitationsource-double-aisoundpressureunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createmicrophonechannel__string-string-double-double-aiterminalconfiguration-aiexcitationsource-double-aisoundpressureunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a microphone to measure sound pressure. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateMicrophoneChannel(string physicalChannelName, string nameToAssignChannel, double micropho

### CreateMicrophoneChannel(string, string, double, double, AITerminalConfiguration, AIExcitationSource, double, AISoundPressureUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a microphone to [measure sound pressure](/csh?context=nidaqmx_daqhelp_soundpress). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateMicrophoneChannel(string physicalChannelName, string nameToAssignChannel, double microphoneSensitivity, double maximumSoundPressureLevel, AITerminalConfiguration terminalConfiguration, AIExcitationSource currentExcitationSource, double currentExcitationValue, AISoundPressureUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateMicrophoneChannel(string, string, double, double, AITerminalConfiguration, AIExcitationSource, double, AISoundPressureUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| microphoneSensitivity | double | The sensitivity of the microphone. Specify this value in millivolts per pascal. |
| maximumSoundPressureLevel | double | The maximum instantaneous sound pressure level you expect to measure. This value is in decibels, referenced to 20 micropascals. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amperes that the sensor requires. Refer to the sensor documentation to determine this value. |
| units | AISoundPressureUnits | The units to use to return the sound pressure measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createmicrophonechannel__string-string-double-double-aiterminalconfiguration-aiexcitationsource-double-string.html language=enus -->
## TOPIC 00293: CreateMicrophoneChannel(string, string, double, double, AITerminalConfiguration, AIExcitationSource, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createmicrophonechannel__string-string-double-double-aiterminalconfiguration-aiexcitationsource-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createmicrophonechannel__string-string-double-double-aiterminalconfiguration-aiexcitationsource-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale that uses a microphone to measure sound pressure. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateMicrophoneChannel(string physicalChannelName, string name

### CreateMicrophoneChannel(string, string, double, double, AITerminalConfiguration, AIExcitationSource, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale that uses a microphone to [measure sound pressure](/csh?context=nidaqmx_daqhelp_soundpress). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateMicrophoneChannel(string physicalChannelName, string nameToAssignChannel, double microphoneSensitivity, double maximumSoundPressureLevel, AITerminalConfiguration terminalConfiguration, AIExcitationSource currentExcitationSource, double currentExcitationValue, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateMicrophoneChannel(string, string, double, double, AITerminalConfiguration, AIExcitationSource, double, string) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| microphoneSensitivity | double | The sensitivity of the microphone. Specify this value in millivolts per pascal. |
| maximumSoundPressureLevel | double | The maximum instantaneous sound pressure level you expect to measure. This value is in decibels, referenced to 20 micropascals. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amperes that the sensor requires. Refer to the sensor documentation to determine this value. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createpowerchannel__string-string-double-double-bool.html language=enus -->
## TOPIC 00294: CreatePowerChannel(string, string, double, double, bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createpowerchannel__string-string-double-double-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createpowerchannel__string-string-double-double-bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel to source and measure power. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreatePowerChannel(string physicalChannelName, string nameToAssignChannel, double voltageSetpoint, double currentSet

### CreatePowerChannel(string, string, double, double, bool)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) to source and measure power. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreatePowerChannel(string physicalChannelName, string nameToAssignChannel, double voltageSetpoint, double currentSetpoint, [MarshalAs(UnmanagedType.U1)] bool outputEnable)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreatePowerChannel(string, string, double, double, bool) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| voltageSetpoint | double | The voltage setpoint, in volts. |
| currentSetpoint | double | The current setpoint, in amperes. |
| outputEnable | bool | Whether to enable or disable the output. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createpressurebridgepolynomialchannel__string-string-double-double-aipressureunits-aibridgeconfiguration-aiexcitationsource-double-double-d...d249e7350.html language=enus -->
## TOPIC 00295: CreatePressureBridgePolynomialChannel(string, string, double, double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createpressurebridgepolynomialchannel__string-string-double-double-aipressureunits-aibridgeconfiguration-aiexcitationsource-double-double-d...d249e7350.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createpressurebridgepolynomialchannel__string-string-double-double-aipressureunits-aibridgeconfiguration-aiexcitationsource-double-double-d...d249e7350.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical v

### CreatePressureBridgePolynomialChannel(string, string, double, double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure pressure](/csh?context=nidaqmx_daqhelp_pressure). Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use [PolynomialScale](nationalinstruments-daqmx-polynomialscale.html) to generate the other set. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreatePressureBridgePolynomialChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIPressureUnits units, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double[] forwardCoefficients, double[] reverseCoefficients, AIBridgeElectricalUnits electricalUnits, AIBridgePhysicalUnits physicalUnits)

#### Remarks

Specify different values for *physical units*  if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| units | AIPressureUnits | The units to use to return the measurement. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| forwardCoefficients | double[] | The array of the forward coefficients of the polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x3. |
| reverseCoefficients | double[] | The array of the reverse coefficients of the polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9y3. |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createpressurebridgepolynomialchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr...d249e7125.html language=enus -->
## TOPIC 00296: CreatePressureBridgePolynomialChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createpressurebridgepolynomialchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr...d249e7125.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createpressurebridgepolynomialchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr...d249e7125.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a poly

### CreatePressureBridgePolynomialChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure pressure](/csh?context=nidaqmx_daqhelp_pressure), with the specified custom scale. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use [PolynomialScale](nationalinstruments-daqmx-polynomialscale.html) to generate the other set. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreatePressureBridgePolynomialChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double[] forwardCoefficients, double[] reverseCoefficients, AIBridgeElectricalUnits electricalUnits, AIBridgePhysicalUnits physicalUnits)

#### Remarks

Specify different values for *physical units*  if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in custom scaled units. |
| maximumValue | double | The maximum value you expect to measure, in custom scaled units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| forwardCoefficients | double[] | The array of the forward coefficients of the polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x3. |
| reverseCoefficients | double[] | The array of the reverse coefficients of the polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9y3. |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createpressurebridgetablechannel__string-string-double-double-aipressureunits-aibridgeconfiguration-aiexcitationsource-double-double-double...d249e7573.html language=enus -->
## TOPIC 00297: CreatePressureBridgeTableChannel(string, string, double, double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createpressurebridgetablechannel__string-string-double-double-aipressureunits-aibridgeconfiguration-aiexcitationsource-double-double-double...d249e7573.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createpressurebridgetablechannel__string-string-double-double-aipressureunits-aibridgeconfiguration-aiexcitationsource-double-double-double...d249e7573.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and

### CreatePressureBridgeTableChannel(string, string, double, double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure pressure](/csh?context=nidaqmx_daqhelp_pressure). Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreatePressureBridgeTableChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIPressureUnits units, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double[] electricalValues, AIBridgeElectricalUnits electricalUnits, double[] physicalValues, AIBridgePhysicalUnits physicalUnits)

#### Remarks

Specify different values for *physical units*  if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| units | AIPressureUnits | The units to use to return the measurement. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| electricalValues | double[] | The array of electrical values that map to the values in physicalValues . Specify this value in the units specified with electricalUnits . |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| physicalValues | double[] | The array of physical values that map to the values in electricalValues . Specify this value in the units specified with physicalUnits . |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createpressurebridgetablechannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-aib...d249e7794.html language=enus -->
## TOPIC 00298: CreatePressureBridgeTableChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createpressurebridgetablechannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-aib...d249e7794.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createpressurebridgetablechannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-aib...d249e7794.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling be

### CreatePressureBridgeTableChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure pressure](/csh?context=nidaqmx_daqhelp_pressure), with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreatePressureBridgeTableChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double[] electricalValues, AIBridgeElectricalUnits electricalUnits, double[] physicalValues, AIBridgePhysicalUnits physicalUnits)

#### Remarks

Specify different values for *physical units*  if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in custom scaled units. |
| maximumValue | double | The maximum value you expect to measure, in custom scaled units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| electricalValues | double[] | The array of electrical values that map to the values in physicalValues . Specify this value in the units specified with electricalUnits . |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| physicalValues | double[] | The array of physical values that map to the values in electricalValues . Specify this value in the units specified with physicalUnits . |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createpressurebridgetwopointlinearchannel__string-string-double-double-aipressureunits-aibridgeconfiguration-aiexcitationsource-double-doub...d249e8266.html language=enus -->
## TOPIC 00299: CreatePressureBridgeTwoPointLinearChannel(string, string, double, double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createpressurebridgetwopointlinearchannel__string-string-double-double-aipressureunits-aibridgeconfiguration-aiexcitationsource-double-doub...d249e8266.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createpressurebridgetwopointlinearchannel__string-string-double-double-aipressureunits-aibridgeconfiguration-aiexcitationsource-double-doub...d249e8266.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values

### CreatePressureBridgeTwoPointLinearChannel(string, string, double, double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure pressure](/csh?context=nidaqmx_daqhelp_pressure). Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreatePressureBridgeTwoPointLinearChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIPressureUnits units, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double firstElectricalValue, double secondElectricalValue, AIBridgeElectricalUnits electricalUnits, double firstPhysicalValue, double secondPhysicalValue, AIBridgePhysicalUnits physicalUnits)

#### Remarks

Specify different values for *physical units*  if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| units | AIPressureUnits | The units to use to return the measurement. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| firstElectricalValue | double | The first electrical value, corresponding to firstPhysicalValue . Specify this value in the units specified with electricalUnits . |
| secondElectricalValue | double | The second electrical value, corresponding to secondPhysicalValue . Specify this value in the units specified with electricalUnits . |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| firstPhysicalValue | double | The first physical value, corresponding to firstElectricalValue . Specify this value in the units specified with physicalUnits . |
| secondPhysicalValue | double | The second physical value, corresponding to secondElectricalValue . Specify this value in the units specified with physicalUnits . |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createpressurebridgetwopointlinearchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double...d249e8016.html language=enus -->
## TOPIC 00300: CreatePressureBridgeTwoPointLinearChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createpressurebridgetwopointlinearchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double...d249e8016.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createpressurebridgetwopointlinearchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double...d249e8016.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points

### CreatePressureBridgeTwoPointLinearChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure pressure](/csh?context=nidaqmx_daqhelp_pressure), with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreatePressureBridgeTwoPointLinearChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double firstElectricalValue, double secondElectricalValue, AIBridgeElectricalUnits electricalUnits, double firstPhysicalValue, double secondPhysicalValue, AIBridgePhysicalUnits physicalUnits)

#### Remarks

Specify different values for *physical units*  if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in custom scaled units. |
| maximumValue | double | The maximum value you expect to measure, in custom scaled units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| firstElectricalValue | double | The first electrical value, corresponding to firstPhysicalValue . Specify this value in the units specified with electricalUnits . |
| secondElectricalValue | double | The second electrical value, corresponding to secondPhysicalValue . Specify this value in the units specified with electricalUnits . |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| firstPhysicalValue | double | The first physical value, corresponding to firstElectricalValue . Specify this value in the units specified with physicalUnits . |
| secondPhysicalValue | double | The second physical value, corresponding to secondElectricalValue . Specify this value in the units specified with physicalUnits . |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createresistancechannel__string-string-double-double-airesistanceconfiguration-aiexcitationsource-double-airesistanceunits.html language=enus -->
## TOPIC 00301: CreateResistanceChannel(string, string, double, double, AIResistanceConfiguration, AIExcitationSource, double, AIResistanceUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createresistancechannel__string-string-double-double-airesistanceconfiguration-aiexcitationsource-double-airesistanceunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createresistancechannel__string-string-double-double-airesistanceconfiguration-aiexcitationsource-double-airesistanceunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel to measure resistance. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateResistanceChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue,

### CreateResistanceChannel(string, string, double, double, AIResistanceConfiguration, AIExcitationSource, double, AIResistanceUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) to [measure resistance](/csh?context=nidaqmx_daqhelp_measuring_resistance). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateResistanceChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIResistanceConfiguration resistanceConfiguration, AIExcitationSource currentExcitationSource, double currentExcitationValue, AIResistanceUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateResistanceChannel(string, string, double, double, AIResistanceConfiguration, AIExcitationSource, double, AIResistanceUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| resistanceConfiguration | AIResistanceConfiguration | The number of wires to use for resistive measurements. |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amperes that the sensor requires. Refer to sensor documentation to determine this value. |
| units | AIResistanceUnits | The units to use to return the measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createresistancechannel__string-string-double-double-airesistanceconfiguration-aiexcitationsource-double-string.html language=enus -->
## TOPIC 00302: CreateResistanceChannel(string, string, double, double, AIResistanceConfiguration, AIExcitationSource, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createresistancechannel__string-string-double-double-airesistanceconfiguration-aiexcitationsource-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createresistancechannel__string-string-double-double-airesistanceconfiguration-aiexcitationsource-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale to measure resistance. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateResistanceChannel(string physicalChannelName, string nameToAssignChannel, double min

### CreateResistanceChannel(string, string, double, double, AIResistanceConfiguration, AIExcitationSource, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale to [measure resistance](/csh?context=nidaqmx_daqhelp_measuring_resistance). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateResistanceChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIResistanceConfiguration resistanceConfiguration, AIExcitationSource currentExcitationSource, double currentExcitationValue, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateResistanceChannel(string, string, double, double, AIResistanceConfiguration, AIExcitationSource, double, string) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| resistanceConfiguration | AIResistanceConfiguration | The number of wires to use for resistive measurements. |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amperes that the sensor requires. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createrosettestraingagechannel__string-string-double-double-aistraingageconfiguration-double-aiexcitationsource-double-double-double-double...d249e8834.html language=enus -->
## TOPIC 00303: CreateRosetteStrainGageChannel(string, string, double, double, AIStrainGageConfiguration, double, AIExcitationSource, double, double, double, double, AIRosetteType, double, AIRosetteMeasurementType[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createrosettestraingagechannel__string-string-double-double-aistraingageconfiguration-double-aiexcitationsource-double-double-double-double...d249e8834.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createrosettestraingagechannel__string-string-double-double-aistraingageconfiguration-double-aiexcitationsource-double-double-double-double...d249e8834.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel to measure two-dimensional strain using a rosette strain gage. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateRosetteStrainGageChannel(string physicalChannelName, string nameToAssignChan

### CreateRosetteStrainGageChannel(string, string, double, double, AIStrainGageConfiguration, double, AIExcitationSource, double, double, double, double, AIRosetteType, double, AIRosetteMeasurementType[])

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) to [measure two-dimensional strain](/csh?context=nidaqmx_daqhelp_meas_strain) using a rosette strain gage. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateRosetteStrainGageChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIStrainGageConfiguration strainGageConfiguration, double leadWireResistance, AIExcitationSource excitationSource, double excitationValue, double gageFactor, double nominalGageResistance, double poissonRatio, AIRosetteType rosetteType, double rosetteStrainGageOrientation, AIRosetteMeasurementType[] rosetteMeasurementTypes)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels. If you use this input to provide your own names for the virtual channels, you must use the names when you refer to these channels in other methods.

**physicalChannelName Considerations**

For each rosette sensor, this method creates one strain virtual channel for each strain gage in the rosette, and one rosette virtual channel for each measurement specified in the rosette measurements array. For the [Tee](nationalinstruments-daqmx-airosettetype.html) type, at least 2 physical channels are required. For the [Rectangular](nationalinstruments-daqmx-airosettetype.html) and [Delta](nationalinstruments-daqmx-airosettetype.html) types, at least 3 physical channels are required. You are also able to specify a multiple of the required number of physical channels to create the virtual channels necessary for multiple rosette sensors. The order of these channels is critical for proper rosette measurements and should be in the order of the gages in the rosette. The gages in the rosette are typically labeled as A, B, and C or 1, 2, and 3 which is the order required by [DAQmx](nationalinstruments-daqmx.html). The [DAQmx](nationalinstruments-daqmx.html) physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a list or range of physical channels to this input.

**nameToAssignChannel Considerations**

| Name Format | Type |
| --- | --- |
| rosette._strainGage1 | Strain gage 1. |
| rosette._strainGage2 | Strain gage 2. |
| rosette._strainGage3 | Strain gage 3. |
| rosette._principalStrain1 | Principal strain 1. |
| rosette._principalStrain2 | Principal strain 2. |
| rosette._principalStrainAngle | Principal strain angle. |
| rosette._cartesianStrainX | Cartesian strain X. |
| rosette._cartesianStrainY | Cartesian strain Y. |
| rosette._cartesianShearStrainXY | Cartesian shear strain XY. |
| rosette._maximumShearStrain | Maximum shear strain. |
| rosette._maximumShearStrainAngle | Minimum shear strain. |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more virtual strain gage channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. |
| minimumValue | double | The minimum strain you expect to measure. This value applies to each strain gage in the rosette. |
| maximumValue | double | The maximum strain you expect to measure. This value applies to each strain gage in the rosette |
| strainGageConfiguration | AIStrainGageConfiguration | The bridge configuration for the strain gages. The possible values for this parameter are listed in AIStrainGageConfiguration. |
| leadWireResistance | double | The amount of resistance in ohms in the lead wires. Ideally, this value is the same for all leads. |
| excitationSource | AIExcitationSource | The source of excitation. The possible values for this parameter are listed in AIExcitationSource. |
| excitationValue | double | The amount of excitation in volts supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values. |
| gageFactor | double | The sensitivity of the strain gages and relates the change in electrical resistance to the change in strain. Each gage in the bridge must have the same gage factor. Refer to the sensor documentation to determine this value. |
| nominalGageResistance | double | The resistance in ohms of the gages in an unstrained position. Each gage in the bridge must have the same nominal gage resistance. The resistance across arms of the bridge that do not have strain gages must also be the same as the nominal gage resistance. Refer to the sensor documentation to determine this value. |
| poissonRatio | double | The ratio of lateral strain to axial strain in the material you are measuring. |
| rosetteType | AIRosetteType | The type of the rosette. The possible values for this parameter are listed in AIRosetteType. |
| rosetteStrainGageOrientation | double | The orientation, in degrees, of the gage with respect to the preferred X axis. |
| rosetteMeasurementTypes | AIRosetteMeasurementType[] | An array of AIRosetteMeasurementType that specifies the virtual channels to create for the rosette measurements. For each rosette sensor, this method creates one strain virtual channel for each strain gage in the rosette, and one rosette virtual channel for each measurement specified in the rosette measurements array. . |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-creatertdchannel__string-string-double-double-aitemperatureunits-airtdtype-airesistanceconfiguration-aiexcitationsource-double-double.html language=enus -->
## TOPIC 00304: CreateRtdChannel(string, string, double, double, AITemperatureUnits, AIRtdType, AIResistanceConfiguration, AIExcitationSource, double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-creatertdchannel__string-string-double-double-aitemperatureunits-airtdtype-airesistanceconfiguration-aiexcitationsource-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-creatertdchannel__string-string-double-double-aitemperatureunits-airtdtype-airesistanceconfiguration-aiexcitationsource-double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses an RTD to measure temperature. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateRtdChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double max

### CreateRtdChannel(string, string, double, double, AITemperatureUnits, AIRtdType, AIResistanceConfiguration, AIExcitationSource, double, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses an [RTD](/csh?context=nidaqmx_measfunds_rtd) to [measure temperature](/csh?context=nidaqmx_daqhelp_simtemp). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateRtdChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AITemperatureUnits units, AIRtdType type, AIResistanceConfiguration resistanceConfiguration, AIExcitationSource currentExcitationSource, double currentExcitationValue, double r0)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateRtdChannel(string, string, double, double, AITemperatureUnits, AIRtdType, AIResistanceConfiguration, AIExcitationSource, double, double) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| units | AITemperatureUnits | The units to use to return the measurement. |
| type | AIRtdType | The type of RTD connected to the channel. |
| resistanceConfiguration | AIResistanceConfiguration | The number of wires to use for resistive measurements. |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amperes that the sensor requires. |
| r0 | double | The sensor resistance in ohms at 0 degrees Celsius for the Callendar-Van Dusen equation. Refer to the sensor documentation for more information about this constant. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-creatervdtchannel__string-string-double-double-double-airvdtsensitivityunits-aiexcitationsource-double-double-aiacexcitationwiremode-airvdtunits.html language=enus -->
## TOPIC 00305: CreateRvdtChannel(string, string, double, double, double, AIRvdtSensitivityUnits, AIExcitationSource, double, double, AIACExcitationWireMode, AIRvdtUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-creatervdtchannel__string-string-double-double-double-airvdtsensitivityunits-aiexcitationsource-double-double-aiacexcitationwiremode-airvdtunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-creatervdtchannel__string-string-double-double-double-airvdtsensitivityunits-aiexcitationsource-double-double-aiacexcitationwiremode-airvdtunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses an RVDT to measure angular position. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateRvdtChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, dou

### CreateRvdtChannel(string, string, double, double, double, AIRvdtSensitivityUnits, AIExcitationSource, double, double, AIACExcitationWireMode, AIRvdtUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses an [RVDT](/csh?context=nidaqmx_measfunds_rvdts) to [measure angular position](/csh?context=nidaqmx_daqhelp_angdisplacervdt). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateRvdtChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, double sensitivity, AIRvdtSensitivityUnits sensitivityUnits, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double voltageExcitationFrequency, AIACExcitationWireMode voltageExcitationWireMode, AIRvdtUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateRvdtChannel(string, string, double, double, double, AIRvdtSensitivityUnits, AIExcitationSource, double, double, AIACExcitationWireMode, AIRvdtUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| sensitivity | double | The sensitivity of the sensor. This value is in the units you specify with sensitivityUnits . Refer to the sensor documentation to determine this value. |
| sensitivityUnits | AIRvdtSensitivityUnits | The units of sensitivity . |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. |
| voltageExcitationFrequency | double | The excitation frequency that the sensor requires, in hertz. Refer to the sensor documentation to determine this value. |
| voltageExcitationWireMode | AIACExcitationWireMode | The number of leads on the sensor. Some sensors might require you to tie leads together to create a four- or five-wire sensor. Refer to the documentation for your sensor for more information. |
| units | AIRvdtUnits | The units to use to return the measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-creatervdtchannel__string-string-double-double-double-airvdtsensitivityunits-aiexcitationsource-double-double-aiacexcitationwiremode-string.html language=enus -->
## TOPIC 00306: CreateRvdtChannel(string, string, double, double, double, AIRvdtSensitivityUnits, AIExcitationSource, double, double, AIACExcitationWireMode, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-creatervdtchannel__string-string-double-double-double-airvdtsensitivityunits-aiexcitationsource-double-double-aiacexcitationwiremode-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-creatervdtchannel__string-string-double-double-double-airvdtsensitivityunits-aiexcitationsource-double-double-aiacexcitationwiremode-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale that uses an RVDT to measure angular position. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateRvdtChannel(string physicalChannelName, string nameToAssignC

### CreateRvdtChannel(string, string, double, double, double, AIRvdtSensitivityUnits, AIExcitationSource, double, double, AIACExcitationWireMode, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale that uses an [RVDT](/csh?context=nidaqmx_measfunds_rvdts) to [measure angular position](/csh?context=nidaqmx_daqhelp_angdisplacervdt). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateRvdtChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, double sensitivity, AIRvdtSensitivityUnits sensitivityUnits, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double voltageExcitationFrequency, AIACExcitationWireMode voltageExcitationWireMode, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateRvdtChannel(string, string, double, double, double, AIRvdtSensitivityUnits, AIExcitationSource, double, double, AIACExcitationWireMode, string) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| sensitivity | double | The sensitivity of the sensor. This value is in the units you specify with sensitivityUnits . Refer to the sensor documentation to determine this value. |
| sensitivityUnits | AIRvdtSensitivityUnits | The units of sensitivity . |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. |
| voltageExcitationFrequency | double | The excitation frequency that the sensor requires, in hertz. Refer to the sensor documentation to determine this value. |
| voltageExcitationWireMode | AIACExcitationWireMode | The number of leads on the sensor. Some sensors require you to tie leads together to create a four- or five-wire sensor. Refer to the documentation for your sensor for more information. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createstraingagechannel__string-string-double-double-aistraingageconfiguration-aiexcitationsource-double-double-double-double-double-double-aistrainunits.html language=enus -->
## TOPIC 00307: CreateStrainGageChannel(string, string, double, double, AIStrainGageConfiguration, AIExcitationSource, double, double, double, double, double, double, AIStrainUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createstraingagechannel__string-string-double-double-aistraingageconfiguration-aiexcitationsource-double-double-double-double-double-double-aistrainunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createstraingagechannel__string-string-double-double-aistraingageconfiguration-aiexcitationsource-double-double-double-double-double-double-aistrainunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel to measure strain. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateStrainGageChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AISt

### CreateStrainGageChannel(string, string, double, double, AIStrainGageConfiguration, AIExcitationSource, double, double, double, double, double, double, AIStrainUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) to [measure strain](/csh?context=nidaqmx_daqhelp_meas_strain). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateStrainGageChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIStrainGageConfiguration strainGageConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double gageFactor, double initialBridgeVoltage, double nominalGageResistance, double poissonRatio, double leadWireResistance, AIStrainUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateStrainGageChannel(string, string, double, double, AIStrainGageConfiguration, AIExcitationSource, double, double, double, double, double, double, AIStrainUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| strainGageConfiguration | AIStrainGageConfiguration | The bridge configuration of the strain gage. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. |
| gageFactor | double | The sensitivity of the strain gages and relates the change in electrical resistance to the change in strain. Each gage in the bridge must have the same gage factor. Refer to the sensor documentation to determine this value. |
| initialBridgeVoltage | double | The output voltage of the bridge in the unloaded condition. NI-DAQmx subtracts this value from any measurements before applying scaling equations. Perform a voltage measurement on the bridge with no strain applied to determine this value. |
| nominalGageResistance | double | The resistance in ohms of the gages in an unstrained position. Each gage in the bridge must have the same nominal gage resistance. The resistance across arms of the bridge that do not have strain gages must also be the same as the nominal gage resistance. Refer to the sensor documentation to determine this value. |
| poissonRatio | double | The ratio of lateral strain to axial strain in the material you are measuring. |
| leadWireResistance | double | The amount in ohms of resistance in the lead wires. Ideally, this value is the same for all leads. |
| units | AIStrainUnits | The units to use to return the measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createstraingagechannel__string-string-double-double-aistraingageconfiguration-aiexcitationsource-double-double-double-double-double-double-string.html language=enus -->
## TOPIC 00308: CreateStrainGageChannel(string, string, double, double, AIStrainGageConfiguration, AIExcitationSource, double, double, double, double, double, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createstraingagechannel__string-string-double-double-aistraingageconfiguration-aiexcitationsource-double-double-double-double-double-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createstraingagechannel__string-string-double-double-aistraingageconfiguration-aiexcitationsource-double-double-double-double-double-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale to measure strain. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateStrainGageChannel(string physicalChannelName, string nameToAssignChannel, double minimum

### CreateStrainGageChannel(string, string, double, double, AIStrainGageConfiguration, AIExcitationSource, double, double, double, double, double, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale to [measure strain](/csh?context=nidaqmx_daqhelp_meas_strain). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateStrainGageChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIStrainGageConfiguration strainGageConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double gageFactor, double initialBridgeVoltage, double nominalGageResistance, double poissonRatio, double leadWireResistance, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateStrainGageChannel(string, string, double, double, AIStrainGageConfiguration, AIExcitationSource, double, double, double, double, double, double, string) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| strainGageConfiguration | AIStrainGageConfiguration | The bridge configuration of the strain gage. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. |
| gageFactor | double | The sensitivity of the strain gages and relates the change in electrical resistance to the change in strain. Each gage in the bridge must have the same gage factor. Refer to the sensor documentation to determine this value. |
| initialBridgeVoltage | double | The output voltage of the bridge in the unloaded condition. NI-DAQmx subtracts this value from any measurements before applying scaling equations. Perform a voltage measurement on the bridge with no strain applied to determine this value. |
| nominalGageResistance | double | The resistance in ohms of the gages in an unstrained position. Each gage in the bridge must have the same nominal gage resistance. The resistance across arms of the bridge that do not have strain gages must also be the same as the nominal gage resistance. Refer to the sensor documentation to determine this value. |
| poissonRatio | double | The ratio of lateral strain to axial strain in the material you are measuring. |
| leadWireResistance | double | The amount in ohms of resistance in the lead wires. Ideally, this value is the same for all leads. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsaccelerometerchannel__string-string-double-double-aiexcitationsource-double-aiaccelerationunits.html language=enus -->
## TOPIC 00309: CreateTedsAccelerometerChannel(string, string, double, double, AIExcitationSource, double, AIAccelerationUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsaccelerometerchannel__string-string-double-double-aiexcitationsource-double-aiaccelerationunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsaccelerometerchannel__string-string-double-double-aiexcitationsource-double-aiaccelerationunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses an accelerometer to measure acceleration. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsAccelerometerChannel(string physicalChannelName, string nameToAssignChannel, double

### CreateTedsAccelerometerChannel(string, string, double, double, AIExcitationSource, double, AIAccelerationUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses an [accelerometer](/csh?context=nidaqmx_measfunds_accelerometers) to [measure acceleration](/csh?context=nidaqmx_daqhelp_accel). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsAccelerometerChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIExcitationSource currentExcitationSource, double currentExcitationValue, AIAccelerationUnits units)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amps that the sensor requires. Refer to the sensor documentation to determine this value. |
| units | AIAccelerationUnits | The units to use to return the acceleration measurement from the channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsaccelerometerchannel__string-string-double-double-aiexcitationsource-double-string.html language=enus -->
## TOPIC 00310: CreateTedsAccelerometerChannel(string, string, double, double, AIExcitationSource, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsaccelerometerchannel__string-string-double-double-aiexcitationsource-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsaccelerometerchannel__string-string-double-double-aiexcitationsource-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale that uses an accelerometer to measure acceleration. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsAccelerometerChannel(string physicalChannelName, st

### CreateTedsAccelerometerChannel(string, string, double, double, AIExcitationSource, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale that uses an [accelerometer](/csh?context=nidaqmx_measfunds_accelerometers) to [measure acceleration](/csh?context=nidaqmx_daqhelp_accel). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsAccelerometerChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIExcitationSource currentExcitationSource, double currentExcitationValue, string customScaleName)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amps that the sensor requires. Refer to the sensor documentation to determine this value. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsbridgechannel__string-string-double-double-aibridgeunits-aiexcitationsource-double.html language=enus -->
## TOPIC 00311: CreateTedsBridgeChannel(string, string, double, double, AIBridgeUnits, AIExcitationSource, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsbridgechannel__string-string-double-double-aibridgeunits-aiexcitationsource-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsbridgechannel__string-string-double-double-aibridgeunits-aiexcitationsource-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that measures a a Wheatstone bridge. You must configure the physical channel(s) with TEDS information to use this method. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQ

### CreateTedsBridgeChannel(string, string, double, double, AIBridgeUnits, AIExcitationSource, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that measures a a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque). You must configure the physical channel(s) with TEDS information to use this method. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsBridgeChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIBridgeUnits units, AIExcitationSource voltageExcitationSource, double voltageExcitationValue)

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| units | AIBridgeUnits | The units to use to return the measurement. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsbridgechannel__string-string-double-double-string-aiexcitationsource-double.html language=enus -->
## TOPIC 00312: CreateTedsBridgeChannel(string, string, double, double, string, AIExcitationSource, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsbridgechannel__string-string-double-double-string-aiexcitationsource-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsbridgechannel__string-string-double-double-string-aiexcitationsource-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that measures a a Wheatstone bridge, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that sc

### CreateTedsBridgeChannel(string, string, double, double, string, AIExcitationSource, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that measures a a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque), with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsBridgeChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName, AIExcitationSource voltageExcitationSource, double voltageExcitationValue)

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in custom scaled units. |
| maximumValue | double | The maximum value you expect to measure, in custom scaled units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedscurrentchannel__string-string-aiterminalconfiguration-double-double-aicurrentunits.html language=enus -->
## TOPIC 00313: CreateTedsCurrentChannel(string, string, AITerminalConfiguration, double, double, AICurrentUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedscurrentchannel__string-string-aiterminalconfiguration-double-double-aicurrentunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedscurrentchannel__string-string-aiterminalconfiguration-double-double-aicurrentunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsCurrentChannel(string physicalChannelName, string nameToAssignChannel, AITerminalCo

### CreateTedsCurrentChannel(string, string, AITerminalConfiguration, double, double, AICurrentUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with an internal shunt resistor to [measure current](/csh?context=nidaqmx_daqhelp_measuring_current). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsCurrentChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, AICurrentUnits units)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| units | AICurrentUnits | The units to use to return the current measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedscurrentchannel__string-string-aiterminalconfiguration-double-double-double-aicurrentunits.html language=enus -->
## TOPIC 00314: CreateTedsCurrentChannel(string, string, AITerminalConfiguration, double, double, double, AICurrentUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedscurrentchannel__string-string-aiterminalconfiguration-double-double-double-aicurrentunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedscurrentchannel__string-string-aiterminalconfiguration-double-double-double-aicurrentunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsCurrentChannel(string physicalChannelName, string nameToAssignChannel, A

### CreateTedsCurrentChannel(string, string, AITerminalConfiguration, double, double, double, AICurrentUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified external shunt resistor to [measure current](/csh?context=nidaqmx_daqhelp_measuring_current). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsCurrentChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, double externalShuntResistorValue, AICurrentUnits units)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| externalShuntResistorValue | double | The value in ohms of an external shunt resistor. |
| units | AICurrentUnits | The units to use to return the current measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedscurrentchannel__string-string-aiterminalconfiguration-double-double-double-string.html language=enus -->
## TOPIC 00315: CreateTedsCurrentChannel(string, string, AITerminalConfiguration, double, double, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedscurrentchannel__string-string-aiterminalconfiguration-double-double-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedscurrentchannel__string-string-aiterminalconfiguration-double-double-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale and external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsCurrentChannel(string physicalChannelName, string nameT

### CreateTedsCurrentChannel(string, string, AITerminalConfiguration, double, double, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale and external shunt resistor to [measure current](/csh?context=nidaqmx_daqhelp_measuring_current). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsCurrentChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, double externalShuntResistorValue, string customScaleName)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| externalShuntResistorValue | double | The value in ohms of an external shunt resistor. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedscurrentchannel__string-string-aiterminalconfiguration-double-double-string.html language=enus -->
## TOPIC 00316: CreateTedsCurrentChannel(string, string, AITerminalConfiguration, double, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedscurrentchannel__string-string-aiterminalconfiguration-double-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedscurrentchannel__string-string-aiterminalconfiguration-double-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale and an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsCurrentChannel(string physicalChannelName, string na

### CreateTedsCurrentChannel(string, string, AITerminalConfiguration, double, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale and an internal shunt resistor to [measure current](/csh?context=nidaqmx_daqhelp_measuring_current). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsCurrentChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, string customScaleName)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsforcebridgechannel__string-string-double-double-aiforceunits-aiexcitationsource-double.html language=enus -->
## TOPIC 00317: CreateTedsForceBridgeChannel(string, string, double, double, AIForceUnits, AIExcitationSource, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsforcebridgechannel__string-string-double-double-aiforceunits-aiexcitationsource-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsforcebridgechannel__string-string-double-double-aiforceunits-aiexcitationsource-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure force or load. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to

### CreateTedsForceBridgeChannel(string, string, double, double, AIForceUnits, AIExcitationSource, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure force or load](/csh?context=nidaqmx_daqhelp_force). You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsForceBridgeChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIForceUnits units, AIExcitationSource voltageExcitationSource, double voltageExcitationValue)

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| units | AIForceUnits | The units to use to return the measurement. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsforcebridgechannel__string-string-double-double-string-aiexcitationsource-double.html language=enus -->
## TOPIC 00318: CreateTedsForceBridgeChannel(string, string, double, double, string, AIExcitationSource, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsforcebridgechannel__string-string-double-double-string-aiexcitationsource-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsforcebridgechannel__string-string-double-double-string-aiexcitationsource-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds

### CreateTedsForceBridgeChannel(string, string, double, double, string, AIExcitationSource, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure force or load](/csh?context=nidaqmx_daqhelp_force), with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsForceBridgeChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName, AIExcitationSource voltageExcitationSource, double voltageExcitationValue)

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsforceiepechannel__string-string-aiterminalconfiguration-double-double-aiforceunits-aiexcitationsource-double.html language=enus -->
## TOPIC 00319: CreateTedsForceIepeChannel(string, string, AITerminalConfiguration, double, double, AIForceUnits, AIExcitationSource, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsforceiepechannel__string-string-aiterminalconfiguration-double-double-aiforceunits-aiexcitationsource-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsforceiepechannel__string-string-aiterminalconfiguration-double-double-aiforceunits-aiexcitationsource-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses an IEPE force sensor to measure force or load. You must configure the physical channel(s) with TEDS information to use this method. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel Cre

### CreateTedsForceIepeChannel(string, string, AITerminalConfiguration, double, double, AIForceUnits, AIExcitationSource, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses an [IEPE force sensor](/csh?context=nidaqmx_measfunds_forcepiezo) to [measure force or load](/csh?context=nidaqmx_daqhelp_force). You must configure the physical channel(s) with TEDS information to use this method. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsForceIepeChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, AIForceUnits units, AIExcitationSource currentExcitationSource, double currentExcitationValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of – 1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| units | AIForceUnits | The units to use to return the measurement. |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amperes that the sensor requires. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsforceiepechannel__string-string-aiterminalconfiguration-double-double-string-aiexcitationsource-double.html language=enus -->
## TOPIC 00320: CreateTedsForceIepeChannel(string, string, AITerminalConfiguration, double, double, string, AIExcitationSource, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsforceiepechannel__string-string-aiterminalconfiguration-double-double-string-aiexcitationsource-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsforceiepechannel__string-string-aiterminalconfiguration-double-double-string-aiexcitationsource-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses an IEPE force sensor to measure force or load, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInst

### CreateTedsForceIepeChannel(string, string, AITerminalConfiguration, double, double, string, AIExcitationSource, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses an [IEPE force sensor](/csh?context=nidaqmx_measfunds_forcepiezo) to [measure force or load](/csh?context=nidaqmx_daqhelp_force), with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsForceIepeChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, string customScaleName, AIExcitationSource currentExcitationSource, double currentExcitationValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of – 1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value you expect to measure, in custom scaled units. |
| maximumValue | double | The maximum value you expect to measure, in custom scaled units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amperes that the sensor requires. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedslvdtchannel__string-string-double-double-aiexcitationsource-double-double-aiacexcitationwiremode-ailvdtunits.html language=enus -->
## TOPIC 00321: CreateTedsLvdtChannel(string, string, double, double, AIExcitationSource, double, double, AIACExcitationWireMode, AILvdtUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedslvdtchannel__string-string-double-double-aiexcitationsource-double-double-aiacexcitationwiremode-ailvdtunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedslvdtchannel__string-string-double-double-aiexcitationsource-double-double-aiacexcitationwiremode-ailvdtunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsLvdtChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue,

### CreateTedsLvdtChannel(string, string, double, double, AIExcitationSource, double, double, AIACExcitationWireMode, AILvdtUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses an [LVDT](/csh?context=nidaqmx_measfunds_lvdts) to [measure linear position](/csh?context=nidaqmx_daqhelp_lindisplacelvdt). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsLvdtChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double voltageExcitationFrequency, AIACExcitationWireMode voltageExcitationWireMode, AILvdtUnits units)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. Refer to the sensor documentation to determine this value. |
| voltageExcitationFrequency | double | The excitation frequency that the sensor requires, in hertz. Refer to the sensor documentation to determine this value. |
| voltageExcitationWireMode | AIACExcitationWireMode | The number of leads on the sensor. Some sensors require you to tie leads together to create a four- or five-wire sensor. Refer to the documentation for your sensor for more information. |
| units | AILvdtUnits | The units to use to return the linear position measurement from the channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedslvdtchannel__string-string-double-double-aiexcitationsource-double-double-aiacexcitationwiremode-string.html language=enus -->
## TOPIC 00322: CreateTedsLvdtChannel(string, string, double, double, AIExcitationSource, double, double, AIACExcitationWireMode, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedslvdtchannel__string-string-double-double-aiexcitationsource-double-double-aiacexcitationwiremode-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedslvdtchannel__string-string-double-double-aiexcitationsource-double-double-aiacexcitationwiremode-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsLvdtChannel(string physicalChannelName, string nameToAssi

### CreateTedsLvdtChannel(string, string, double, double, AIExcitationSource, double, double, AIACExcitationWireMode, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale that uses an [LVDT](/csh?context=nidaqmx_measfunds_lvdts) to [measure linear position](/csh?context=nidaqmx_daqhelp_lindisplacelvdt). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsLvdtChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double voltageExcitationFrequency, AIACExcitationWireMode voltageExcitationWireMode, string customScaleName)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. Refer to the sensor documentation to determine this value. |
| voltageExcitationFrequency | double | The excitation frequency that the sensor requires, in hertz. Refer to the sensor documentation to determine this value. |
| voltageExcitationWireMode | AIACExcitationWireMode | The number of leads on the sensor. Some sensors require you to tie leads together to create a four- or five-wire sensor. Refer to the documentation for your sensor for more information. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsmicrophonechannel__string-string-double-aiterminalconfiguration-aiexcitationsource-double-aisoundpressureunits.html language=enus -->
## TOPIC 00323: CreateTedsMicrophoneChannel(string, string, double, AITerminalConfiguration, AIExcitationSource, double, AISoundPressureUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsmicrophonechannel__string-string-double-aiterminalconfiguration-aiexcitationsource-double-aisoundpressureunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsmicrophonechannel__string-string-double-aiterminalconfiguration-aiexcitationsource-double-aisoundpressureunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a microphone to measure sound pressure. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsMicrophoneChannel(string physicalChannelName, string nameToAssignChannel, double maxi

### CreateTedsMicrophoneChannel(string, string, double, AITerminalConfiguration, AIExcitationSource, double, AISoundPressureUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a microphone to [measure sound pressure](/csh?context=nidaqmx_daqhelp_soundpress). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsMicrophoneChannel(string physicalChannelName, string nameToAssignChannel, double maximumSoundPressureLevel, AITerminalConfiguration terminalConfiguration, AIExcitationSource currentExcitationSource, double currentExcitationValue, AISoundPressureUnits units)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| maximumSoundPressureLevel | double | The maximum instantaneous sound pressure level you expect to measure. This value is in decibels, referenced to 20 micropascals. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amperes that the sensor requires. Refer to the sensor documentation to determine this value. |
| units | AISoundPressureUnits | The units to use to return the sound pressure measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsmicrophonechannel__string-string-double-aiterminalconfiguration-aiexcitationsource-double-string.html language=enus -->
## TOPIC 00324: CreateTedsMicrophoneChannel(string, string, double, AITerminalConfiguration, AIExcitationSource, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsmicrophonechannel__string-string-double-aiterminalconfiguration-aiexcitationsource-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsmicrophonechannel__string-string-double-aiterminalconfiguration-aiexcitationsource-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale that uses a microphone to measure sound pressure. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsMicrophoneChannel(string physicalChannelName, string

### CreateTedsMicrophoneChannel(string, string, double, AITerminalConfiguration, AIExcitationSource, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale that uses a microphone to [measure sound pressure](/csh?context=nidaqmx_daqhelp_soundpress). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsMicrophoneChannel(string physicalChannelName, string nameToAssignChannel, double maximumSoundPressureLevel, AITerminalConfiguration terminalConfiguration, AIExcitationSource currentExcitationSource, double currentExcitationValue, string customScaleName)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| maximumSoundPressureLevel | double | The maximum instantaneous sound pressure level you expect to measure. This value is in decibels, referenced to 20 micropascals. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amperes that the sensor requires. Refer to the sensor documentation to determine this value. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedspressurebridgechannel__string-string-double-double-aipressureunits-aiexcitationsource-double.html language=enus -->
## TOPIC 00325: CreateTedsPressureBridgeChannel(string, string, double, double, AIPressureUnits, AIExcitationSource, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedspressurebridgechannel__string-string-double-double-aipressureunits-aiexcitationsource-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedspressurebridgechannel__string-string-double-double-aipressureunits-aiexcitationsource-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure pressure. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the

### CreateTedsPressureBridgeChannel(string, string, double, double, AIPressureUnits, AIExcitationSource, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure pressure](/csh?context=nidaqmx_daqhelp_pressure). You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html). You must configure the physical channel(s) with TEDS information to use this method.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsPressureBridgeChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIPressureUnits units, AIExcitationSource voltageExcitationSource, double voltageExcitationValue)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| units | AIPressureUnits | The units to use to return the measurement. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedspressurebridgechannel__string-string-double-double-string-aiexcitationsource-double.html language=enus -->
## TOPIC 00326: CreateTedsPressureBridgeChannel(string, string, double, double, string, AIExcitationSource, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedspressurebridgechannel__string-string-double-double-string-aiexcitationsource-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedspressurebridgechannel__string-string-double-double-string-aiexcitationsource-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one

### CreateTedsPressureBridgeChannel(string, string, double, double, string, AIExcitationSource, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure pressure](/csh?context=nidaqmx_daqhelp_pressure), with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html). You must configure the physical channel(s) with TEDS information to use this method.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsPressureBridgeChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName, AIExcitationSource voltageExcitationSource, double voltageExcitationValue)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in custom scaled units. |
| maximumValue | double | The maximum value you expect to measure, in custom scaled units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsresistancechannel__string-string-double-double-airesistanceconfiguration-aiexcitationsource-double-airesistanceunits.html language=enus -->
## TOPIC 00327: CreateTedsResistanceChannel(string, string, double, double, AIResistanceConfiguration, AIExcitationSource, double, AIResistanceUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsresistancechannel__string-string-double-double-airesistanceconfiguration-aiexcitationsource-double-airesistanceunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsresistancechannel__string-string-double-double-airesistanceconfiguration-aiexcitationsource-double-airesistanceunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel to measure resistance. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsResistanceChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumVal

### CreateTedsResistanceChannel(string, string, double, double, AIResistanceConfiguration, AIExcitationSource, double, AIResistanceUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) to [measure resistance](/csh?context=nidaqmx_daqhelp_measuring_resistance). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsResistanceChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIResistanceConfiguration resistanceConfiguration, AIExcitationSource currentExcitationSource, double currentExcitationValue, AIResistanceUnits units)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| resistanceConfiguration | AIResistanceConfiguration | The number of wires to use for resistive measurements. |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amperes that the sensor requires. Refer to the sensor documentation to determine this value. |
| units | AIResistanceUnits | The units to use to return the resistance measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsresistancechannel__string-string-double-double-airesistanceconfiguration-aiexcitationsource-double-string.html language=enus -->
## TOPIC 00328: CreateTedsResistanceChannel(string, string, double, double, AIResistanceConfiguration, AIExcitationSource, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsresistancechannel__string-string-double-double-airesistanceconfiguration-aiexcitationsource-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsresistancechannel__string-string-double-double-airesistanceconfiguration-aiexcitationsource-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale to measure resistance. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsResistanceChannel(string physicalChannelName, string nameToAssignChannel, double

### CreateTedsResistanceChannel(string, string, double, double, AIResistanceConfiguration, AIExcitationSource, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale to [measure resistance](/csh?context=nidaqmx_daqhelp_measuring_resistance). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsResistanceChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIResistanceConfiguration resistanceConfiguration, AIExcitationSource currentExcitationSource, double currentExcitationValue, string customScaleName)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| resistanceConfiguration | AIResistanceConfiguration | The number of wires to use for resistive measurements. |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amperes that the sensor requires. Refer to the sensor documentation to determine this value. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsrtdchannel__string-string-double-double-aitemperatureunits-airesistanceconfiguration-aiexcitationsource-double.html language=enus -->
## TOPIC 00329: CreateTedsRtdChannel(string, string, double, double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsrtdchannel__string-string-double-double-aitemperatureunits-airesistanceconfiguration-aiexcitationsource-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsrtdchannel__string-string-double-double-aitemperatureunits-airesistanceconfiguration-aiexcitationsource-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses an RTD to measure temperature. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsRtdChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double

### CreateTedsRtdChannel(string, string, double, double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses an [RTD](/csh?context=nidaqmx_measfunds_rtd) to [measure temperature](/csh?context=nidaqmx_daqhelp_simtemp). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsRtdChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AITemperatureUnits units, AIResistanceConfiguration resistanceConfiguration, AIExcitationSource currentExcitationSource, double currentExcitationValue)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| units | AITemperatureUnits | The units to use to return the temperature measurement. |
| resistanceConfiguration | AIResistanceConfiguration | The number of wires to use for resistive measurements. |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amperes that the sensor requires. Refer to the sensor documentation to determine this value. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsrvdtchannel__string-string-double-double-aiexcitationsource-double-double-aiacexcitationwiremode-airvdtunits.html language=enus -->
## TOPIC 00330: CreateTedsRvdtChannel(string, string, double, double, AIExcitationSource, double, double, AIACExcitationWireMode, AIRvdtUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsrvdtchannel__string-string-double-double-aiexcitationsource-double-double-aiacexcitationwiremode-airvdtunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsrvdtchannel__string-string-double-double-aiexcitationsource-double-double-aiacexcitationwiremode-airvdtunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses an RVDT to measure angular position. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsRvdtChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue,

### CreateTedsRvdtChannel(string, string, double, double, AIExcitationSource, double, double, AIACExcitationWireMode, AIRvdtUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses an [RVDT](/csh?context=nidaqmx_measfunds_rvdts) to [measure angular position](/csh?context=nidaqmx_daqhelp_angdisplacervdt). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsRvdtChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double voltageExcitationFrequency, AIACExcitationWireMode voltageExcitationWireMode, AIRvdtUnits units)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. Refer to the sensor documentation to determine this value. |
| voltageExcitationFrequency | double | The excitation frequency that the sensor requires, in hertz. Refer to the sensor documentation to determine this value. |
| voltageExcitationWireMode | AIACExcitationWireMode | The number of leads on the sensor. Some sensors require you to tie leads together to create a four- or five-wire sensor. Refer to the documentation for your sensor for more information. |
| units | AIRvdtUnits | The units to use to return the angular position measurement from the channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsrvdtchannel__string-string-double-double-aiexcitationsource-double-double-aiacexcitationwiremode-string.html language=enus -->
## TOPIC 00331: CreateTedsRvdtChannel(string, string, double, double, AIExcitationSource, double, double, AIACExcitationWireMode, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsrvdtchannel__string-string-double-double-aiexcitationsource-double-double-aiacexcitationwiremode-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsrvdtchannel__string-string-double-double-aiexcitationsource-double-double-aiacexcitationwiremode-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses an RVDT to measure angular position. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsRvdtChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue,

### CreateTedsRvdtChannel(string, string, double, double, AIExcitationSource, double, double, AIACExcitationWireMode, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses an [RVDT](/csh?context=nidaqmx_measfunds_rvdts) to [measure angular position](/csh?context=nidaqmx_daqhelp_angdisplacervdt). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsRvdtChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double voltageExcitationFrequency, AIACExcitationWireMode voltageExcitationWireMode, string customScaleName)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. Refer to the sensor documentation to determine this value. |
| voltageExcitationFrequency | double | The excitation frequency that the sensor requires, in hertz. Refer to the sensor documentation to determine this value. |
| voltageExcitationWireMode | AIACExcitationWireMode | The number of leads on the sensor. Some sensors require you to tie leads together to create a four- or five-wire sensor. Refer to the documentation for your sensor for more information. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsstraingagechannel__string-string-double-double-aiexcitationsource-double-double-double-aistrainunits.html language=enus -->
## TOPIC 00332: CreateTedsStrainGageChannel(string, string, double, double, AIExcitationSource, double, double, double, AIStrainUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsstraingagechannel__string-string-double-double-aiexcitationsource-double-double-double-aistrainunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsstraingagechannel__string-string-double-double-aiexcitationsource-double-double-double-aistrainunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel to measure strain. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsStrainGageChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue,

### CreateTedsStrainGageChannel(string, string, double, double, AIExcitationSource, double, double, double, AIStrainUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) to [measure strain](/csh?context=nidaqmx_daqhelp_meas_strain). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsStrainGageChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double initialBridgeVoltage, double leadWireResistance, AIStrainUnits units)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. Refer to the sensor documentation to determine this value. |
| initialBridgeVoltage | double | The output voltage of the bridge in the unloaded condition. NI-DAQmx subtracts this value from any measurements before applying scaling equations. Perform a voltage measurement on the bridge with no strain applied to determine this value. |
| leadWireResistance | double | The amount of resistance in ohms in the lead wires. Ideally, this value is the same for all leads. |
| units | AIStrainUnits | The units to use to return the strain measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsstraingagechannel__string-string-double-double-aiexcitationsource-double-double-double-string.html language=enus -->
## TOPIC 00333: CreateTedsStrainGageChannel(string, string, double, double, AIExcitationSource, double, double, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsstraingagechannel__string-string-double-double-aiexcitationsource-double-double-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsstraingagechannel__string-string-double-double-aiexcitationsource-double-double-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale to measure strain. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsStrainGageChannel(string physicalChannelName, string nameToAssignChannel, double min

### CreateTedsStrainGageChannel(string, string, double, double, AIExcitationSource, double, double, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale to [measure strain](/csh?context=nidaqmx_daqhelp_meas_strain). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsStrainGageChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double initialBridgeVoltage, double leadWireResistance, string customScaleName)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. Refer to the sensor documentation to determine this value. |
| initialBridgeVoltage | double | The output voltage of the bridge in the unloaded condition. NI-DAQmx subtracts this value from any measurements before applying scaling equations. Perform a voltage measurement on the bridge with no strain applied to determine this value. |
| leadWireResistance | double | The amount of resistance in ohms in the lead wires. Ideally, this value is the same for all leads. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsthermistoriexchannel__string-string-double-double-aitemperatureunits-airesistanceconfiguration-aiexcitationsource-double.html language=enus -->
## TOPIC 00334: CreateTedsThermistorIExChannel(string, string, double, double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsthermistoriexchannel__string-string-double-double-aitemperatureunits-airesistanceconfiguration-aiexcitationsource-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsthermistoriexchannel__string-string-double-double-aitemperatureunits-airesistanceconfiguration-aiexcitationsource-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a thermistor to measure temperature. Use this method when the thermistor uses current excitation. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsThermistorIExChannel(string

### CreateTedsThermistorIExChannel(string, string, double, double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [thermistor](/csh?context=nidaqmx_measfunds_thermistors) to [measure temperature](/csh?context=nidaqmx_daqhelp_simtemp). Use this method when the thermistor uses current excitation. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsThermistorIExChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AITemperatureUnits units, AIResistanceConfiguration resistanceConfiguration, AIExcitationSource currentExcitationSource, double currentExcitationValue)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| units | AITemperatureUnits | The units to use to return the temperature measurement. |
| resistanceConfiguration | AIResistanceConfiguration | The number of wires to use for resistive measurements. |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amperes that the sensor requires. Refer to the sensor documentation to determine this value. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsthermistorvexchannel__string-string-double-double-aitemperatureunits-airesistanceconfiguration-aiexcitationsource-double-double.html language=enus -->
## TOPIC 00335: CreateTedsThermistorVExChannel(string, string, double, double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsthermistorvexchannel__string-string-double-double-aitemperatureunits-airesistanceconfiguration-aiexcitationsource-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsthermistorvexchannel__string-string-double-double-aitemperatureunits-airesistanceconfiguration-aiexcitationsource-double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a thermistor to measure temperature. Use this method when the thermistor uses voltage excitation. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsThermistorVExChannel(string

### CreateTedsThermistorVExChannel(string, string, double, double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, double, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [thermistor](/csh?context=nidaqmx_measfunds_thermistors) to [measure temperature](/csh?context=nidaqmx_daqhelp_simtemp). Use this method when the thermistor uses voltage excitation. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsThermistorVExChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AITemperatureUnits units, AIResistanceConfiguration resistanceConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double r1)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| units | AITemperatureUnits | The units to use to return the temperature measurement. |
| resistanceConfiguration | AIResistanceConfiguration | The number of wires to use for resistive measurements. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. Refer to the sensor documentation to determine this value. |
| r1 | double | The value of the reference resistor, in ohms. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsthermocouplechannel__string-string-double-double-aitemperatureunits-double.html language=enus -->
## TOPIC 00336: CreateTedsThermocoupleChannel(string, string, double, double, AITemperatureUnits, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsthermocouplechannel__string-string-double-double-aitemperatureunits-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsthermocouplechannel__string-string-double-double-aitemperatureunits-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a thermocouple to measure temperature using a constant value cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsThermocoupleChannel(string physicalC

### CreateTedsThermocoupleChannel(string, string, double, double, AITemperatureUnits, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [thermocouple](/csh?context=nidaqmx_measfunds_thermocouples) to [measure temperature](/csh?context=nidaqmx_daqhelp_simtemp) using a constant value cold-junction compensation. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsThermocoupleChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AITemperatureUnits units, double cjcValue)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| units | AITemperatureUnits | The units to use to return the temperature measurement. |
| cjcValue | double | The temperature in units of the cold-junction. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsthermocouplechannel__string-string-double-double-aitemperatureunits-string.html language=enus -->
## TOPIC 00337: CreateTedsThermocoupleChannel(string, string, double, double, AITemperatureUnits, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsthermocouplechannel__string-string-double-double-aitemperatureunits-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsthermocouplechannel__string-string-double-double-aitemperatureunits-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a thermocouple to measure temperature using a measurement on another channel for cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsThermocoupleChan

### CreateTedsThermocoupleChannel(string, string, double, double, AITemperatureUnits, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [thermocouple](/csh?context=nidaqmx_measfunds_thermocouples) to [measure temperature](/csh?context=nidaqmx_daqhelp_simtemp) using a measurement on another channel for cold-junction compensation. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsThermocoupleChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AITemperatureUnits units, string cjcChannel)

#### Remarks

>

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| units | AITemperatureUnits | The units to use to return the temperature measurement. |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| cjcChannel | string | The channel that acquires the temperature of the thermocouple cold-junction if you set AIThermocoupleCjcSource to Channel. You can use a global channel or another virtual channel already in the task. If the channel is a temperature channel, NI-DAQmx acquires the temperature in the correct units. Other channel types, such as a resistance channel with a custom sensor, must use a custom scale to scale values to degrees Celsius. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsthermocouplechannel__string-string-double-double-aitemperatureunits.html language=enus -->
## TOPIC 00338: CreateTedsThermocoupleChannel(string, string, double, double, AITemperatureUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsthermocouplechannel__string-string-double-double-aitemperatureunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsthermocouplechannel__string-string-double-double-aitemperatureunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a thermocouple to measure temperature using a built-in cold-junction compensation source. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsThermocoupleChannel(string physical

### CreateTedsThermocoupleChannel(string, string, double, double, AITemperatureUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [thermocouple](/csh?context=nidaqmx_measfunds_thermocouples) to [measure temperature](/csh?context=nidaqmx_daqhelp_simtemp) using a built-in cold-junction compensation source. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsThermocoupleChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AITemperatureUnits units)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| units | AITemperatureUnits | The units to use to return the temperature measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedstorquebridgechannel__string-string-double-double-aitorqueunits-aiexcitationsource-double.html language=enus -->
## TOPIC 00339: CreateTedsTorqueBridgeChannel(string, string, double, double, AITorqueUnits, AIExcitationSource, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedstorquebridgechannel__string-string-double-double-aitorqueunits-aiexcitationsource-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedstorquebridgechannel__string-string-double-double-aitorqueunits-aiexcitationsource-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure torque. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AI

### CreateTedsTorqueBridgeChannel(string, string, double, double, AITorqueUnits, AIExcitationSource, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure torque](/csh?context=nidaqmx_daqhelp_torque). You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsTorqueBridgeChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AITorqueUnits units, AIExcitationSource voltageExcitationSource, double voltageExcitationValue)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| units | AITorqueUnits | The units to use to return the measurement. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedstorquebridgechannel__string-string-double-double-string-aiexcitationsource-double.html language=enus -->
## TOPIC 00340: CreateTedsTorqueBridgeChannel(string, string, double, double, string, AIExcitationSource, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedstorquebridgechannel__string-string-double-double-string-aiexcitationsource-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedstorquebridgechannel__string-string-double-double-string-aiexcitationsource-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or

### CreateTedsTorqueBridgeChannel(string, string, double, double, string, AIExcitationSource, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure torque](/csh?context=nidaqmx_daqhelp_torque), with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsTorqueBridgeChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName, AIExcitationSource voltageExcitationSource, double voltageExcitationValue)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in custom scaled units. |
| maximumValue | double | The maximum value you expect to measure, in custom scaled units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsvoltagechannel__string-string-aiterminalconfiguration-double-double-aivoltageunits.html language=enus -->
## TOPIC 00341: CreateTedsVoltageChannel(string, string, AITerminalConfiguration, double, double, AIVoltageUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsvoltagechannel__string-string-aiterminalconfiguration-double-double-aivoltageunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsvoltagechannel__string-string-aiterminalconfiguration-double-double-aivoltageunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel to measure voltage. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsVoltageChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguratio

### CreateTedsVoltageChannel(string, string, AITerminalConfiguration, double, double, AIVoltageUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) to [measure voltage](/csh?context=nidaqmx_daqhelp_meas_volt). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsVoltageChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, AIVoltageUnits units)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

Note

If the measurement requires the use of internal excitation or you need the voltage to be scaled by the excitation, use [CreateTedsVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIExcitationSource, double, string)](nationalinstruments-daqmx-aichannelcollection-createtedsvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aiexcitationsource-double-string.html) instead.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| units | AIVoltageUnits | The units to use to return the voltage measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsvoltagechannel__string-string-aiterminalconfiguration-double-double-string.html language=enus -->
## TOPIC 00342: CreateTedsVoltageChannel(string, string, AITerminalConfiguration, double, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsvoltagechannel__string-string-aiterminalconfiguration-double-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsvoltagechannel__string-string-aiterminalconfiguration-double-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale to measure voltage. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsVoltageChannel(string physicalChannelName, string nameToAssignChannel, AITerminalCo

### CreateTedsVoltageChannel(string, string, AITerminalConfiguration, double, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale to [measure voltage](/csh?context=nidaqmx_daqhelp_meas_volt). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsVoltageChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, string customScaleName)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

Note

If the measurement requires the use of internal excitation or you need the voltage to be scaled by the excitation, use [CreateTedsVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIExcitationSource, double, string)](nationalinstruments-daqmx-aichannelcollection-createtedsvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aiexcitationsource-double-string.html) instead.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aiexcitationsource-double-aivoltageunits.html language=enus -->
## TOPIC 00343: CreateTedsVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIExcitationSource, double, AIVoltageUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aiexcitationsource-double-aivoltageunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aiexcitationsource-double-aivoltageunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsVoltageChannelWithExcitation(string physicalChannelName, string nameToAs

### CreateTedsVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIExcitationSource, double, AIVoltageUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsVoltageChannelWithExcitation(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration configuration, double minimumValue, double maximumValue, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, AIVoltageUnits units)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| configuration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. Refer to the sensor documentation to determine this value. |
| units | AIVoltageUnits | The units to use to return the voltage measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtedsvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aiexcitationsource-double-string.html language=enus -->
## TOPIC 00344: CreateTedsVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIExcitationSource, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtedsvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aiexcitationsource-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtedsvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aiexcitationsource-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTedsVoltageChannelWithExcitation(string phys

### CreateTedsVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIExcitationSource, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTedsVoltageChannelWithExcitation(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration configuration, double minimumValue, double maximumValue, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, string customScaleName)

#### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| configuration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. Refer to the sensor documentation to determine this value. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createthermistoriexchannel__string-string-double-double-aitemperatureunits-airesistanceconfiguration-aiexcitationsource-double-double-double-double.html language=enus -->
## TOPIC 00345: CreateThermistorIExChannel(string, string, double, double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, double, double, double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createthermistoriexchannel__string-string-double-double-aitemperatureunits-airesistanceconfiguration-aiexcitationsource-double-double-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createthermistoriexchannel__string-string-double-double-aitemperatureunits-airesistanceconfiguration-aiexcitationsource-double-double-double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a thermistor to measure temperature. Use this method when the thermistor uses current excitation. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateThermistorIExChannel(string phy

### CreateThermistorIExChannel(string, string, double, double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, double, double, double, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [thermistor](/csh?context=nidaqmx_measfunds_thermistors) to [measure temperature](/csh?context=nidaqmx_daqhelp_simtemp). Use this method when the thermistor uses current excitation. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateThermistorIExChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AITemperatureUnits units, AIResistanceConfiguration resistanceConfiguration, AIExcitationSource currentExcitationSource, double currentExcitationValue, double a, double b, double c)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateThermistorIExChannel(string, string, double, double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, double, double, double, double) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| units | AITemperatureUnits | The units to use to return the measurement. |
| resistanceConfiguration | AIResistanceConfiguration | The number of wires to use for resistive measurements. |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amperes that the sensor requires. |
| a | double | The A constant for the Steinhart-Hart thermistor equation. Consult the sensor documentation to determine the value for this constant. |
| b | double | The B constant for the Steinhart-Hart thermistor equation. Consult the sensor documentation to determine the value for this constant. |
| c | double | The C constant for the Steinhart-Hart thermistor equation. Consult the sensor documentation to determine the value for this constant. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createthermistorvexchannel__string-string-double-double-aitemperatureunits-airesistanceconfiguration-aiexcitationsource-double-double-double-double-double.html language=enus -->
## TOPIC 00346: CreateThermistorVExChannel(string, string, double, double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, double, double, double, double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createthermistorvexchannel__string-string-double-double-aitemperatureunits-airesistanceconfiguration-aiexcitationsource-double-double-double-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createthermistorvexchannel__string-string-double-double-aitemperatureunits-airesistanceconfiguration-aiexcitationsource-double-double-double-double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a thermistor to measure temperature. Use this method when the thermistor uses voltage excitation. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateThermistorVExChannel(string phy

### CreateThermistorVExChannel(string, string, double, double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, double, double, double, double, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [thermistor](/csh?context=nidaqmx_measfunds_thermistors) to [measure temperature](/csh?context=nidaqmx_daqhelp_simtemp). Use this method when the thermistor uses voltage excitation. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateThermistorVExChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AITemperatureUnits units, AIResistanceConfiguration resistanceConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double a, double b, double c, double r1)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateThermistorVExChannel(string, string, double, double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, double, double, double, double, double) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| units | AITemperatureUnits | The units to use to return the measurement. |
| resistanceConfiguration | AIResistanceConfiguration | The number of wires to use for resistive measurements. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. Refer to the sensor documentation to determine this value. |
| a | double | The A constant for the Steinhart-Hart thermistor equation. Consult the sensor documentation to determine the value for this constant. |
| b | double | The B constant for the Steinhart-Hart thermistor equation. Consult the sensor documentation to determine the value for this constant. |
| c | double | The C constant for the Steinhart-Hart thermistor equation. Consult the sensor documentation to determine the value for this constant. |
| r1 | double | The value of the dropping resistor, in ohms. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createthermocouplechannel__string-string-double-double-aithermocoupletype-aitemperatureunits-double.html language=enus -->
## TOPIC 00347: CreateThermocoupleChannel(string, string, double, double, AIThermocoupleType, AITemperatureUnits, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createthermocouplechannel__string-string-double-double-aithermocoupletype-aitemperatureunits-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createthermocouplechannel__string-string-double-double-aithermocoupletype-aitemperatureunits-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a thermocouple to measure temperature using a constant value cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateThermocoupleChannel(string physicalChann

### CreateThermocoupleChannel(string, string, double, double, AIThermocoupleType, AITemperatureUnits, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [thermocouple](/csh?context=nidaqmx_measfunds_thermocouples) to [measure temperature](/csh?context=nidaqmx_daqhelp_simtemp) using a constant value cold-junction compensation. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateThermocoupleChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIThermocoupleType thermocoupleType, AITemperatureUnits units, double cjcValue)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateThermocoupleChannel(string, string, double, double, AIThermocoupleType, AITemperatureUnits, double) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| thermocoupleType | AIThermocoupleType | The type of thermocouple connected to the channel. Thermocouple types differ in composition and measurement range. |
| units | AITemperatureUnits | The units to use to return the temperature measurement. |
| cjcValue | double | The temperature in units of the cold-junction. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createthermocouplechannel__string-string-double-double-aithermocoupletype-aitemperatureunits-string.html language=enus -->
## TOPIC 00348: CreateThermocoupleChannel(string, string, double, double, AIThermocoupleType, AITemperatureUnits, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createthermocouplechannel__string-string-double-double-aithermocoupletype-aitemperatureunits-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createthermocouplechannel__string-string-double-double-aithermocoupletype-aitemperatureunits-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a thermocouple to measure temperature using a measurement on another channel for cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateThermocoupleChannel(

### CreateThermocoupleChannel(string, string, double, double, AIThermocoupleType, AITemperatureUnits, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [thermocouple](/csh?context=nidaqmx_measfunds_thermocouples) to [measure temperature](/csh?context=nidaqmx_daqhelp_simtemp) using a measurement on another channel for cold-junction compensation. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateThermocoupleChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIThermocoupleType thermocoupleType, AITemperatureUnits units, string cjcChannel)

#### Remarks

>

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateThermocoupleChannel(string, string, double, double, AIThermocoupleType, AITemperatureUnits, string) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| thermocoupleType | AIThermocoupleType | The type of thermocouple connected to the channel. Thermocouple types differ in composition and measurement range. |
| units | AITemperatureUnits | The units to use to return the measurement. |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| cjcChannel | string | The channel that acquires the temperature of the thermocouple cold-junction if you set AIThermocoupleCjcSource to Channel. You can use a global channel or another virtual channel already in the task. If the channel is a temperature channel, NI-DAQmx acquires the temperature in the correct units. Other channel types, such as a resistance channel with a custom sensor, must use a custom scale to scale values to degrees Celsius. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createthermocouplechannel__string-string-double-double-aithermocoupletype-aitemperatureunits.html language=enus -->
## TOPIC 00349: CreateThermocoupleChannel(string, string, double, double, AIThermocoupleType, AITemperatureUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createthermocouplechannel__string-string-double-double-aithermocoupletype-aitemperatureunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createthermocouplechannel__string-string-double-double-aithermocoupletype-aitemperatureunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a thermocouple to measure temperature using a built-in cold-junction compensation source. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateThermocoupleChannel(string physicalChan

### CreateThermocoupleChannel(string, string, double, double, AIThermocoupleType, AITemperatureUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [thermocouple](/csh?context=nidaqmx_measfunds_thermocouples) to [measure temperature](/csh?context=nidaqmx_daqhelp_simtemp) using a built-in cold-junction compensation source. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateThermocoupleChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AIThermocoupleType thermocoupleType, AITemperatureUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateThermocoupleChannel(string, string, double, double, AIThermocoupleType, AITemperatureUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| thermocoupleType | AIThermocoupleType | The type of thermocouple connected to the channel. Thermocouple types differ in composition and measurement range. |
| units | AITemperatureUnits | The units to use to return the measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtorquebridgepolynomialchannel__string-string-double-double-aitorqueunits-aibridgeconfiguration-aiexcitationsource-double-double-doubl...d249e15976.html language=enus -->
## TOPIC 00350: CreateTorqueBridgePolynomialChannel(string, string, double, double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtorquebridgepolynomialchannel__string-string-double-double-aitorqueunits-aibridgeconfiguration-aiexcitationsource-double-double-doubl...d249e15976.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtorquebridgepolynomialchannel__string-string-double-double-aitorqueunits-aibridgeconfiguration-aiexcitationsource-double-double-doubl...d249e15976.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure torque. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical val

### CreateTorqueBridgePolynomialChannel(string, string, double, double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure torque](/csh?context=nidaqmx_daqhelp_torque). Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use [PolynomialScale](nationalinstruments-daqmx-polynomialscale.html) to generate the other set. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTorqueBridgePolynomialChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AITorqueUnits units, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double[] forwardCoefficients, double[] reverseCoefficients, AIBridgeElectricalUnits electricalUnits, AIBridgePhysicalUnits physicalUnits)

#### Remarks

Specify different values for *physical units*  if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| units | AITorqueUnits | The units to use to return the measurement. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| forwardCoefficients | double[] | The array of the forward coefficients of the polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x3. |
| reverseCoefficients | double[] | The array of the reverse coefficients of the polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9y3. |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtorquebridgepolynomialchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-...d249e16199.html language=enus -->
## TOPIC 00351: CreateTorqueBridgePolynomialChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtorquebridgepolynomialchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-...d249e16199.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtorquebridgepolynomialchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-...d249e16199.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polyno

### CreateTorqueBridgePolynomialChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure torque](/csh?context=nidaqmx_daqhelp_torque), with the specified custom scale. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use [PolynomialScale](nationalinstruments-daqmx-polynomialscale.html) to generate the other set. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTorqueBridgePolynomialChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double[] forwardCoefficients, double[] reverseCoefficients, AIBridgeElectricalUnits electricalUnits, AIBridgePhysicalUnits physicalUnits)

#### Remarks

Specify different values for *physical units*  if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in custom scaled units. |
| maximumValue | double | The maximum value you expect to measure, in custom scaled units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| forwardCoefficients | double[] | The array of the forward coefficients of the polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x3. |
| reverseCoefficients | double[] | The array of the reverse coefficients of the polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9y3. |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtorquebridgetablechannel__string-string-double-double-aitorqueunits-aibridgeconfiguration-aiexcitationsource-double-double-double_arr...d249e16639.html language=enus -->
## TOPIC 00352: CreateTorqueBridgeTableChannel(string, string, double, double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtorquebridgetablechannel__string-string-double-double-aitorqueunits-aibridgeconfiguration-aiexcitationsource-double-double-double_arr...d249e16639.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtorquebridgetablechannel__string-string-double-double-aitorqueunits-aibridgeconfiguration-aiexcitationsource-double-double-double_arr...d249e16639.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling betw

### CreateTorqueBridgeTableChannel(string, string, double, double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure torque](/csh?context=nidaqmx_daqhelp_torque), with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTorqueBridgeTableChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AITorqueUnits units, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double[] electricalValues, AIBridgeElectricalUnits electricalUnits, double[] physicalValues, AIBridgePhysicalUnits physicalUnits)

#### Remarks

Specify different values for *physical units*  if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| units | AITorqueUnits | The units to use to return the measurement. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| electricalValues | double[] | The array of electrical values that map to the values in physicalValues . Specify this value in the units specified with electricalUnits . |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| physicalValues | double[] | The array of physical values that map to the values in electricalValues . Specify this value in the units specified with physicalUnits . |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtorquebridgetablechannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-aibri...d249e16424.html language=enus -->
## TOPIC 00353: CreateTorqueBridgeTableChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtorquebridgetablechannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-aibri...d249e16424.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtorquebridgetablechannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double_arr1-aibri...d249e16424.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTorqueBridgeTableChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, d

### CreateTorqueBridgeTableChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits)

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTorqueBridgeTableChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double[] electricalValues, AIBridgeElectricalUnits electricalUnits, double[] physicalValues, AIBridgePhysicalUnits physicalUnits)

#### Remarks

Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

Specify different values for *physical units*  if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in custom scaled units. |
| maximumValue | double | The maximum value you expect to measure, in custom scaled units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| electricalValues | double[] | The array of electrical values that map to the values in physicalValues . Specify this value in the units specified with electricalUnits . |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| physicalValues | double[] | The array of physical values that map to the values in electricalValues . Specify this value in the units specified with physicalUnits . |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtorquebridgetwopointlinearchannel__string-string-double-double-aitorqueunits-aibridgeconfiguration-aiexcitationsource-double-double-d...d249e17101.html language=enus -->
## TOPIC 00354: CreateTorqueBridgeTwoPointLinearChannel(string, string, double, double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtorquebridgetwopointlinearchannel__string-string-double-double-aitorqueunits-aibridgeconfiguration-aiexcitationsource-double-double-d...d249e17101.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtorquebridgetwopointlinearchannel__string-string-double-double-aitorqueunits-aibridgeconfiguration-aiexcitationsource-double-double-d...d249e17101.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of

### CreateTorqueBridgeTwoPointLinearChannel(string, string, double, double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses a [Wheatstone bridge](/csh?context=nidaqmx_measfunds_bridgeforcepressuretorque) to [measure torque](/csh?context=nidaqmx_daqhelp_torque), with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTorqueBridgeTwoPointLinearChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, AITorqueUnits units, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double firstElectricalValue, double secondElectricalValue, AIBridgeElectricalUnits electricalUnits, double firstPhysicalValue, double secondPhysicalValue, AIBridgePhysicalUnits physicalUnits)

#### Remarks

Specify different values for *physical units*  if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measure, in units. |
| units | AITorqueUnits | The units to use to return the measurement. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| firstElectricalValue | double | The first electrical value, corresponding to firstPhysicalValue . Specify this value in the units specified with electricalUnits . |
| secondElectricalValue | double | The second electrical value, corresponding to secondPhysicalValue . Specify this value in the units specified with electricalUnits . |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| firstPhysicalValue | double | The first physical value, corresponding to firstElectricalValue . Specify this value in the units specified with physicalUnits . |
| secondPhysicalValue | double | The second physical value, corresponding to secondElectricalValue . Specify this value in the units specified with physicalUnits . |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createtorquebridgetwopointlinearchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double-d...d249e16859.html language=enus -->
## TOPIC 00355: CreateTorqueBridgeTwoPointLinearChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createtorquebridgetwopointlinearchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double-d...d249e16859.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createtorquebridgetwopointlinearchannel__string-string-double-double-string-aibridgeconfiguration-aiexcitationsource-double-double-double-d...d249e16859.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateTorqueBridgeTwoPointLinearChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitation

### CreateTorqueBridgeTwoPointLinearChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits)

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateTorqueBridgeTwoPointLinearChannel(string physicalChannelName, string nameToAssignChannel, double minimumValue, double maximumValue, string customScaleName, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, double nominalBridgeResistance, double firstElectricalValue, double secondElectricalValue, AIBridgeElectricalUnits electricalUnits, double firstPhysicalValue, double secondPhysicalValue, AIBridgePhysicalUnits physicalUnits)

#### Remarks

This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

Specify different values for *physical units*  if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| minimumValue | double | The minimum value you expect to measure, in custom scaled units. |
| maximumValue | double | The maximum value you expect to measure, in custom scaled units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |
| bridgeConfiguration | AIBridgeConfiguration | The type of Wheatstone bridge configuration connected to the channel. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation, in volts, that the sensor requires. |
| nominalBridgeResistance | double | The resistance, in ohms, of the bridge while not under load. |
| firstElectricalValue | double | The first electrical value, corresponding to firstPhysicalValue . Specify this value in the units specified with electricalUnits . |
| secondElectricalValue | double | The second electrical value, corresponding to secondPhysicalValue . Specify this value in the units specified with electricalUnits . |
| electricalUnits | AIBridgeElectricalUnits | Specifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate. |
| firstPhysicalValue | double | The first physical value, corresponding to firstElectricalValue . Specify this value in the units specified with physicalUnits . |
| secondPhysicalValue | double | The second physical value, corresponding to secondElectricalValue . Specify this value in the units specified with physicalUnits . |
| physicalUnits | AIBridgePhysicalUnits | Specifies to which physical units to scale electrical data. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createvelocityiepechannel__string-string-aiterminalconfiguration-double-double-aivelocityunits-double-aivelocityiepesensorsensitivityunits-...d249e17349.html language=enus -->
## TOPIC 00356: CreateVelocityIepeChannel(string, string, AITerminalConfiguration, double, double, AIVelocityUnits, double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createvelocityiepechannel__string-string-aiterminalconfiguration-double-double-aivelocityunits-double-aivelocityiepesensorsensitivityunits-...d249e17349.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createvelocityiepechannel__string-string-aiterminalconfiguration-double-double-aivelocityunits-double-aivelocityiepesensorsensitivityunits-...d249e17349.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses an IEPE velocity sensor to measure velocity. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateVelocityIepeChannel(string physicalChannelName, string nameToAssignChannel, AITermin

### CreateVelocityIepeChannel(string, string, AITerminalConfiguration, double, double, AIVelocityUnits, double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses an [IEPE velocity sensor](/csh?context=nidaqmx_measfunds_velocitytransducer) to measure velocity. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateVelocityIepeChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, AIVelocityUnits units, double sensitivity, AIVelocityIepeSensorSensitivityUnits sensitivityUnits, AIExcitationSource currentExcitationSource, double currentExcitationValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| units | AIVelocityUnits | The units to use to return the measurement. |
| sensitivity | double | The sensitivity of the sensor. This value is in the units you specify with sensitivityUnits . Refer to the sensor documentation to determine this value. |
| sensitivityUnits | AIVelocityIepeSensorSensitivityUnits | The units of sensitivity . |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amperes that the sensor requires. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createvelocityiepechannel__string-string-aiterminalconfiguration-double-double-string-double-aivelocityiepesensorsensitivityunits-aiexcitat...d249e17494.html language=enus -->
## TOPIC 00357: CreateVelocityIepeChannel(string, string, AITerminalConfiguration, double, double, string, double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createvelocityiepechannel__string-string-aiterminalconfiguration-double-double-string-double-aivelocityiepesensorsensitivityunits-aiexcitat...d249e17494.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createvelocityiepechannel__string-string-aiterminalconfiguration-double-double-string-double-aivelocityiepesensorsensitivityunits-aiexcitat...d249e17494.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel that uses an IEPE velocity sensor to measure velocity. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateVelocityIepeChannel(string physicalChannelName, string nameToAssignChannel, AITermin

### CreateVelocityIepeChannel(string, string, AITerminalConfiguration, double, double, string, double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, double)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) that uses an [IEPE velocity sensor](/csh?context=nidaqmx_measfunds_velocitytransducer) to measure velocity. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateVelocityIepeChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, string customScaleName, double sensitivity, AIVelocityIepeSensorSensitivityUnits sensitivityUnits, AIExcitationSource currentExcitationSource, double currentExcitationValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |
| sensitivity | double | The sensitivity of the sensor. This value is in the units you specify with sensitivityUnits . Refer to the sensor documentation to determine this value. |
| sensitivityUnits | AIVelocityIepeSensorSensitivityUnits | The units of sensitivity . |
| currentExcitationSource | AIExcitationSource | The source of excitation. |
| currentExcitationValue | double | The amount of excitation in amperes that the sensor requires. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createvoltagechannel__string-string-aiterminalconfiguration-double-double-aivoltageunits.html language=enus -->
## TOPIC 00358: CreateVoltageChannel(string, string, AITerminalConfiguration, double, double, AIVoltageUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createvoltagechannel__string-string-aiterminalconfiguration-double-double-aivoltageunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createvoltagechannel__string-string-aiterminalconfiguration-double-double-aivoltageunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel to measure voltage. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateVoltageChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, d

### CreateVoltageChannel(string, string, AITerminalConfiguration, double, double, AIVoltageUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) to [measure voltage](/csh?context=nidaqmx_daqhelp_meas_volt). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateVoltageChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, AIVoltageUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateVoltageChannel(string, string, AITerminalConfiguration, double, double, AIVoltageUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

Note

If the measurement requires the use of internal excitation or you need the voltage scaled by the excitation, use [CreateVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIBridgeConfiguration, AIExcitationSource, double, bool, string)](nationalinstruments-daqmx-aichannelcollection-createvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aibridgeconfiguration-aiexcitationsource-double-bool-string.html) instead.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| units | AIVoltageUnits | The units to use to return the measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createvoltagechannel__string-string-aiterminalconfiguration-double-double-string.html language=enus -->
## TOPIC 00359: CreateVoltageChannel(string, string, AITerminalConfiguration, double, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createvoltagechannel__string-string-aiterminalconfiguration-double-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createvoltagechannel__string-string-aiterminalconfiguration-double-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale to measure voltage. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateVoltageChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfig

### CreateVoltageChannel(string, string, AITerminalConfiguration, double, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale to [measure voltage](/csh?context=nidaqmx_daqhelp_meas_volt). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateVoltageChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateVoltageChannel(string, string, AITerminalConfiguration, double, double, string) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

Note

If the measurement requires the use of internal excitation or you need the voltage scaled by the excitation, use [CreateVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIBridgeConfiguration, AIExcitationSource, double, bool, string)](nationalinstruments-daqmx-aichannelcollection-createvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aibridgeconfiguration-aiexcitationsource-double-bool-string.html) instead.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aibridgeconfiguration-aiexcitationsource-double-boo...d249e17953.html language=enus -->
## TOPIC 00360: CreateVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIBridgeConfiguration, AIExcitationSource, double, bool, AIVoltageUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aibridgeconfiguration-aiexcitationsource-double-boo...d249e17953.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aibridgeconfiguration-aiexcitationsource-double-boo...d249e17953.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateVoltageChannelWithExcitation(string physicalChannelName, string nameToAssign

### CreateVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIBridgeConfiguration, AIExcitationSource, double, bool, AIVoltageUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateVoltageChannelWithExcitation(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration configuration, double minimumValue, double maximumValue, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, [MarshalAs(UnmanagedType.U1)] bool useExcitationForScaling, AIVoltageUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIBridgeConfiguration, AIExcitationSource, double, bool, AIVoltageUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| configuration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units . |
| maximumValue | double | The maximum value expected from the measurement, in units . |
| bridgeConfiguration | AIBridgeConfiguration | The bridge configuration. If you set bridgeConfiguration to NoBridge, useExcitationForScaling has no effect. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. |
| useExcitationForScaling | bool | true if NI-DAQmx divides the measurement by the excitation. Typically, you set useExcitationForScaling to true for ratiometric tranducers. If you set useExcitationForScaling to true, set maximumValue and minimumValue to reflect the scaling. For example, if you expect to acquire a voltage between –5 and 5, and you use an excitation of .10 volts to scale the measurement, set minimumValue to –50 and set maximumValue to 50. |
| units | AIVoltageUnits | The units to use to return the measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aibridgeconfiguration-aiexcitationsource-double-bool-string.html language=enus -->
## TOPIC 00361: CreateVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIBridgeConfiguration, AIExcitationSource, double, bool, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aibridgeconfiguration-aiexcitationsource-double-bool-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aibridgeconfiguration-aiexcitationsource-double-bool-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateVoltageChannelWithExcitation(string physical

### CreateVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIBridgeConfiguration, AIExcitationSource, double, bool, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateVoltageChannelWithExcitation(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration configuration, double minimumValue, double maximumValue, AIBridgeConfiguration bridgeConfiguration, AIExcitationSource voltageExcitationSource, double voltageExcitationValue, [MarshalAs(UnmanagedType.U1)] bool useExcitationForScaling, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIBridgeConfiguration, AIExcitationSource, double, bool, string) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| configuration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value expected from the measurement, in units. |
| maximumValue | double | The maximum value expected from the measurement, in units. |
| bridgeConfiguration | AIBridgeConfiguration | The bridge configuration. If you set bridgeConfiguration to NoBridge, useExcitationForScaling has no effect. |
| voltageExcitationSource | AIExcitationSource | The source of excitation. |
| voltageExcitationValue | double | The amount of excitation in volts that the sensor requires. |
| useExcitationForScaling | bool | true if NI-DAQmx divides the measurement by the excitation. Typically, you set useExcitationForScaling to true for ratiometric tranducers. If you set useExcitationForScaling to true, set maximumValue and minimumValue to reflect the scaling. For example, if you expect to acquire a voltage between –5 and 5, and you use an excitation of .10 volts to scale the measurement, set minimumValue to –50 and set maximumValue to 50. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createvoltagermschannel__string-string-aiterminalconfiguration-double-double-aivoltageacrmsunits.html language=enus -->
## TOPIC 00362: CreateVoltageRmsChannel(string, string, AITerminalConfiguration, double, double, AIVoltageAcrmsUnits)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createvoltagermschannel__string-string-aiterminalconfiguration-double-double-aivoltageacrmsunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createvoltagermschannel__string-string-aiterminalconfiguration-double-double-aivoltageacrmsunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel to measure AC voltage. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateVoltageRmsChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfigurat

### CreateVoltageRmsChannel(string, string, AITerminalConfiguration, double, double, AIVoltageAcrmsUnits)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) to [measure AC voltage](/csh?context=nidaqmx_daqhelp_meas_volt). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateVoltageRmsChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, AIVoltageAcrmsUnits units)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. [CreateVoltageChannel(string, string, AITerminalConfiguration, double, double, AIVoltageUnits)](nationalinstruments-daqmx-aichannelcollection-createvoltagechannel__string-string-aiterminalconfiguration-double-double-aivoltageunits.html) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

Note

If the measurement requires the use of internal excitation or you need the voltage scaled by the excitation, use [CreateVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIBridgeConfiguration, AIExcitationSource, double, bool, string)](nationalinstruments-daqmx-aichannelcollection-createvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aibridgeconfiguration-aiexcitationsource-double-bool-string.html) instead.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value you expect to measure, in units . |
| maximumValue | double | The maximum value you expect to measure, in units . |
| units | AIVoltageAcrmsUnits | The units to use to return the measurement. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-createvoltagermschannel__string-string-aiterminalconfiguration-double-double-string.html language=enus -->
## TOPIC 00363: CreateVoltageRmsChannel(string, string, AITerminalConfiguration, double, double, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-createvoltagermschannel__string-string-aiterminalconfiguration-double-double-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-createvoltagermschannel__string-string-aiterminalconfiguration-double-double-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AIChannel with the specified custom scale to measure AC voltage. This method adds one or more physical channels to the AIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel CreateVoltageRmsChannel(string physicalChannelName, string nameToAssignChannel, AITerminal

### CreateVoltageRmsChannel(string, string, AITerminalConfiguration, double, double, string)

Creates an [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified custom scale to [measure AC voltage](/csh?context=nidaqmx_daqhelp_meas_volt). This method adds one or more physical channels to the [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) CreateVoltageRmsChannel(string physicalChannelName, string nameToAssignChannel, AITerminalConfiguration terminalConfiguration, double minimumValue, double maximumValue, string customScaleName)

#### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for *nameToAssignChannel* . If you provide fewer local virtual channel names in *nameToAssignChannel*  than you create, NI-DAQmx [automatically assigns names](/csh?context=nidaqmx_mxcncpts_nameassignment) to the local virtual channels.

If you do not provide a value for *nameToAssignChannel* , NI-DAQmx uses the *physicalChannelName*  as the local virtual channel name. If you use *nameToAssignChannel*  to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. [CreateVoltageChannel(string, string, AITerminalConfiguration, double, double, string)](nationalinstruments-daqmx-aichannelcollection-createvoltagechannel__string-string-aiterminalconfiguration-double-double-string.html) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

Note

If the measurement requires the use of internal excitation or you need the voltage scaled by the excitation, use [CreateVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIBridgeConfiguration, AIExcitationSource, double, bool, string)](nationalinstruments-daqmx-aichannelcollection-createvoltagechannelwithexcitation__string-string-aiterminalconfiguration-double-double-aibridgeconfiguration-aiexcitationsource-double-bool-string.html) instead.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The names of one or more physical channels to use to create one or more local virtual channels. |
| nameToAssignChannel | string | One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty. |
| terminalConfiguration | AITerminalConfiguration | The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration. |
| minimumValue | double | The minimum value you expect to measure, in units. |
| maximumValue | double | The maximum value you expect to measurement, in units. |
| customScaleName | string | The name of the custom scale to apply to the local virtual channel. |

#### Returns

The newly created [AIChannel](nationalinstruments-daqmx-aichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-getenumerator.html language=enus -->
## TOPIC 00364: GetEnumerator()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-getenumerator.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-getenumerator.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an enumerator that you can use to iterate through the collection. SyntaxNamespace: NationalInstruments.DAQmxpublic IEnumerator GetEnumerator()RemarksFor a detailed explanation of this method, refer to GetEnumerator in the Microsoft .NET Framework documentation. ReturnsEnumerator for the coll

### GetEnumerator()

Returns an enumerator that you can use to iterate through the collection.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IEnumerator GetEnumerator()

#### Remarks

For a detailed explanation of this method, refer to GetEnumerator in the Microsoft .NET Framework documentation.

#### Returns

Enumerator for the collection.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-this__long.html language=enus -->
## TOPIC 00365: this[long index]

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-this__long.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-this__long.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the AIChannel at the specified index. In Visual C#, this property is the indexer. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel this[long index] { get; }RemarksThe AIChannel at the specified index. ChannelsParametersNameTypeDescriptionindexlongThe zero-based index of the entry to l

### this[long index]

Gets the [AIChannel](nationalinstruments-daqmx-aichannel.html) at the specified index. In Visual C#, this property is the indexer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) this[long index] { get; }

#### Remarks

The [AIChannel](nationalinstruments-daqmx-aichannel.html) at the specified index.

Channels

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| index | long | The zero-based index of the entry to locate in the collection. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### See Also

- AIChannel

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-this__string.html language=enus -->
## TOPIC 00366: this[string virtualChannelName]

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-this__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-this__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the AIChannel with the specified virtual channel name. In Visual C#, this property is the indexer. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannel this[string virtualChannelName] { get; }RemarksThe specified AIChannel.By using a comma or colon in virtualChannelName , you can retrieve

### this[string virtualChannelName]

Gets the [AIChannel](nationalinstruments-daqmx-aichannel.html) with the specified virtual channel name. In Visual C#, this property is the indexer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannel](nationalinstruments-daqmx-aichannel.html) this[string virtualChannelName] { get; }

#### Remarks

The specified [AIChannel](nationalinstruments-daqmx-aichannel.html).

By using a comma or colon in *virtualChannelName* , you can retrieve more than one channel at a time. For more information refer to [Channels](https://#).

Channels

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| virtualChannelName | string | One or more virtual channel names that the retrieved AIChannel operates on. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### See Also

- AIChannel

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection-tostring.html language=enus -->
## TOPIC 00367: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannelcollection.html language=enus -->
## TOPIC 00368: AIChannelCollection Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannelcollection.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannelcollection.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the collection of analog input channels for a Task. Derives fromMarshalByRefObjectICollectionSyntaxNamespace: NationalInstruments.DAQmxpublic class AIChannelCollection : MarshalByRefObject, ICollectionRemarksExample applications are located in the <Public Documents>\National Instruments\NI-

### AIChannelCollection Class

Contains the collection of analog input channels for a [Task](nationalinstruments-daqmx-task.html).

#### Derives from

- MarshalByRefObject
- ICollection

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AIChannelCollection : MarshalByRefObject, ICollection

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| All | Gets an AIChannel that operates on all of the channels in the task. |
| Count | Gets the number of elements in the collection. |
| this[long index] | Gets the AIChannel at the specified index. In Visual C#, this property is the indexer. |
| this[string virtualChannelName] | Gets the AIChannel with the specified virtual channel name. In Visual C#, this property is the indexer. |

#### Methods

| Name | Description |
| --- | --- |
| CopyTo(Array, int) | Copies the collection to an array or a portion of an array. This operation is not supported for AIChannelCollection. |
| CreateAccelerationChargeChannel(string, string, AITerminalConfiguration, double, double, string, double, AIAccelerationChargeSensitivityUnits) | Creates channel(s) that use an accelerometer to measure acceleration and adds the channel(s) to the task you specify with taskHandle . |
| CreateAccelerationChargeChannel(string, string, AITerminalConfiguration, double, double, AIAccelerationUnits, double, AIAccelerationChargeSensitivityUnits) | Creates channel(s) that use an accelerometer to measure acceleration and adds the channel(s) to the task you specify with taskHandle . |
| CreateAccelerationFourWireDCVoltageChannel(string, string, AITerminalConfiguration, double, double, AIAccelerationUnits, double, AIAccelerationFourWireDCVoltageSensitivityUnits, AIExcitationSource, double, bool) | Creates an AIChannel that measures acceleration using a 4-wire, DC voltage-based sensor connected to the channel. This method adds one or more physical channels to the AIChannelCollection. |
| CreateAccelerationFourWireDCVoltageChannel(string, string, AITerminalConfiguration, double, double, string, double, AIAccelerationFourWireDCVoltageSensitivityUnits, AIExcitationSource, double, bool) | Creates an AIChannel that specifies the sensitivity of the 4-wire, DC voltage-based sensor connected to the channel. This method adds one or more physical channels to the AIChannelCollection. |
| CreateAccelerometerChannel(string, string, AITerminalConfiguration, double, double, double, AIAccelerometerSensitivityUnits, AIExcitationSource, double, string) | Creates an AIChannel with the specified custom scale that uses an accelerometer to measure acceleration. This method adds one or more physical channels to the AIChannelCollection. |
| CreateAccelerometerChannel(string, string, AITerminalConfiguration, double, double, double, AIAccelerometerSensitivityUnits, AIExcitationSource, double, AIAccelerationUnits) | Creates an AIChannel that uses an accelerometer to measure acceleration. This method adds one or more physical channels to the AIChannelCollection. |
| CreateBridgeChannel(string, string, double, double, AIBridgeUnits, AIBridgeConfiguration, AIExcitationSource, double, double) | Creates an AIChannel that measures voltage ratios from a Wheatstone bridge. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the AIChannelCollection. Use a custom scale or other scaling code to convert the voltage ratios to physical units. |
| CreateBridgeChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double) | Creates an AIChannel that measures voltage ratios from a Wheatstone bridge, with the specified custom scale. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the AIChannelCollection. Use a custom scale or other scaling code to convert the voltage ratios to physical units. |
| CreateBuiltInSensorTemperatureChannel(string, string, AITemperatureUnits) | Creates an AIChannel to measure temperature with a built-in sensor of a terminal block or device. This method adds one or more physical channels to the AIChannelCollection. |
| CreateCalculatedPowerChannel(string, string, string, AITerminalConfiguration, double, double, double, double, AIPowerUnits, double) | Creates an AIChannel with the specified custom scale and external shunt resistor to measure calculated power. This method adds one or more physical channels to the AIChannelCollection. |
| CreateCalculatedPowerChannel(string, string, string, AITerminalConfiguration, double, double, double, double, AIPowerUnits, AICurrentShuntLocation, double, string) | Creates an AIChannel with the specified custom scale and external shunt resistor to measure calculated power. This method adds one or more physical channels to the AIChannelCollection. |
| CreateChargeChannel(string, string, AITerminalConfiguration, double, double, AIChargeUnits) | Creates an AIChannel to measure acceleration using a charge-based sensor. This method adds one or more physical channels to the AIChannelCollection. |
| CreateChargeChannel(string, string, AITerminalConfiguration, double, double, string) | Creates an AIChannel to measure acceleration using a charge-based sensor. This method adds one or more physical channels to the AIChannelCollection. |
| CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, AICurrentUnits) | Creates an AIChannel with an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
| CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, AICurrentUnits, AICurrentShuntLocation, double, string) | Creates an AIChannel with the specified custom scale and external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
| CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, string) | Creates an AIChannel with the specified custom scale and an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
| CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, double, AICurrentUnits) | Creates an AIChannel with the specified external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
| CreateCurrentChannel(string, string, AITerminalConfiguration, double, double, double, string) | Creates an AIChannel with the specified custom scale and external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
| CreateCurrentRmsChannel(string, string, AITerminalConfiguration, double, double, AICurrentAcrmsUnits) | Creates an AIChannel with an internal shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. |
| CreateCurrentRmsChannel(string, string, AITerminalConfiguration, double, double, string) | Creates an AIChannel with the specified custom scale and an internal shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. |
| CreateCurrentRmsChannel(string, string, AITerminalConfiguration, double, double, double, string) | Creates an AIChannel with the specified custom scale and external shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. |
| CreateCurrentRmsChannel(string, string, AITerminalConfiguration, double, double, double, AICurrentAcrmsUnits) | Creates an AIChannel with the specified external shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. |
| CreateDeviceTemperatureChannel(string, string, AITemperatureUnits) | Obsolete: The CreateDeviceTemperatureChannel method is deprecated. Please use the CreateBuiltInSensorTemperatureChannel method instead. Will warn if usedCreates an AIChannel to measure temperature with a built-in sensor of a terminal block or device. This method adds one or more physical channels to the AIChannelCollection. The CreateDeviceTemperatureChannel(string, string, AITemperatureUnits) method has been deprecated in favor of the CreateBuiltInSensorTemperatureChannel(string, string, AITemperatureUnits) method. |
| CreateEddyCurrentProximityProbeChannel(string, string, double, double, double, AIEddyCurrentProximityProbeSensitivityUnits, string) | Creates an AIChannel with the specified custom scale that uses an Eddy Current Proximity Probe to measure position. This method adds one or more physical channels to the AIChannelCollection. |
| CreateEddyCurrentProximityProbeChannel(string, string, double, double, double, AIEddyCurrentProximityProbeSensitivityUnits, AIEddyCurrentProximityProbeUnits) | Creates an AIChannel that uses an Eddy Current Proximity Probe to measure position. This method adds one or more physical channels to the AIChannelCollection. |
| CreateForceBridgePolynomialChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
| CreateForceBridgePolynomialChannel(string, string, double, double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
| CreateForceBridgeTableChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
| CreateForceBridgeTableChannel(string, string, double, double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
| CreateForceBridgeTwoPointLinearChannel(string, string, double, double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
| CreateForceBridgeTwoPointLinearChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
| CreateForceIepeChannel(string, string, AITerminalConfiguration, double, double, string, double, AIForceIepeSensorSensitivityUnits, AIExcitationSource, double) | Creates an AIChannel that uses an IEPE force sensor to measure force or load, with the specified custom scale. This method adds one or more physical channels to the AIChannelCollection. |
| CreateForceIepeChannel(string, string, AITerminalConfiguration, double, double, AIForceUnits, double, AIForceIepeSensorSensitivityUnits, AIExcitationSource, double) | Creates an AIChannel that uses an IEPE force sensor to measure force or load. This method adds one or more physical channels to the AIChannelCollection. |
| CreateFrequencyVoltageChannel(string, string, double, double, double, double, string) | Creates an AIChannel with the specified custom scale to measure frequency using a frequency-to-voltage converter. This method adds one or more physical channels to the AIChannelCollection. |
| CreateFrequencyVoltageChannel(string, string, double, double, double, double, AIFrequencyUnits) | Creates an AIChannel to measure frequency using a frequency-to-voltage converter. This method adds one or more physical channels to the AIChannelCollection. |
| CreateLvdtChannel(string, string, double, double, double, AILvdtSensitivityUnits, AIExcitationSource, double, double, AIACExcitationWireMode, AILvdtUnits) | Creates an AIChannel that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. |
| CreateLvdtChannel(string, string, double, double, double, AILvdtSensitivityUnits, AIExcitationSource, double, double, AIACExcitationWireMode, string) | Creates an AIChannel with the specified custom scale that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. |
| CreateMicrophoneChannel(string, string, double, double, AITerminalConfiguration, AIExcitationSource, double, AISoundPressureUnits) | Creates an AIChannel that uses a microphone to measure sound pressure. This method adds one or more physical channels to the AIChannelCollection. |
| CreateMicrophoneChannel(string, string, double, double, AITerminalConfiguration, AIExcitationSource, double, string) | Creates an AIChannel with the specified custom scale that uses a microphone to measure sound pressure. This method adds one or more physical channels to the AIChannelCollection. |
| CreatePowerChannel(string, string, double, double, bool) | Creates an AIChannel to source and measure power. This method adds one or more physical channels to the AIChannelCollection. |
| CreatePressureBridgePolynomialChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
| CreatePressureBridgePolynomialChannel(string, string, double, double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
| CreatePressureBridgeTableChannel(string, string, double, double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
| CreatePressureBridgeTableChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
| CreatePressureBridgeTwoPointLinearChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
| CreatePressureBridgeTwoPointLinearChannel(string, string, double, double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
| CreateResistanceChannel(string, string, double, double, AIResistanceConfiguration, AIExcitationSource, double, AIResistanceUnits) | Creates an AIChannel to measure resistance. This method adds one or more physical channels to the AIChannelCollection. |
| CreateResistanceChannel(string, string, double, double, AIResistanceConfiguration, AIExcitationSource, double, string) | Creates an AIChannel with the specified custom scale to measure resistance. This method adds one or more physical channels to the AIChannelCollection. |
| CreateRosetteStrainGageChannel(string, string, double, double, AIStrainGageConfiguration, double, AIExcitationSource, double, double, double, double, AIRosetteType, double, AIRosetteMeasurementType[]) | Creates an AIChannel to measure two-dimensional strain using a rosette strain gage. This method adds one or more physical channels to the AIChannelCollection. |
| CreateRtdChannel(string, string, double, double, AITemperatureUnits, AIRtdType, AIResistanceConfiguration, AIExcitationSource, double, double) | Creates an AIChannel that uses an RTD to measure temperature. This method adds one or more physical channels to the AIChannelCollection. |
| CreateRvdtChannel(string, string, double, double, double, AIRvdtSensitivityUnits, AIExcitationSource, double, double, AIACExcitationWireMode, string) | Creates an AIChannel with the specified custom scale that uses an RVDT to measure angular position. This method adds one or more physical channels to the AIChannelCollection. |
| CreateRvdtChannel(string, string, double, double, double, AIRvdtSensitivityUnits, AIExcitationSource, double, double, AIACExcitationWireMode, AIRvdtUnits) | Creates an AIChannel that uses an RVDT to measure angular position. This method adds one or more physical channels to the AIChannelCollection. |
| CreateStrainGageChannel(string, string, double, double, AIStrainGageConfiguration, AIExcitationSource, double, double, double, double, double, double, string) | Creates an AIChannel with the specified custom scale to measure strain. This method adds one or more physical channels to the AIChannelCollection. |
| CreateStrainGageChannel(string, string, double, double, AIStrainGageConfiguration, AIExcitationSource, double, double, double, double, double, double, AIStrainUnits) | Creates an AIChannel to measure strain. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsAccelerometerChannel(string, string, double, double, AIExcitationSource, double, AIAccelerationUnits) | Creates an AIChannel that uses an accelerometer to measure acceleration. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsAccelerometerChannel(string, string, double, double, AIExcitationSource, double, string) | Creates an AIChannel with the specified custom scale that uses an accelerometer to measure acceleration. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsBridgeChannel(string, string, double, double, string, AIExcitationSource, double) | Creates an AIChannel that measures a a Wheatstone bridge, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsBridgeChannel(string, string, double, double, AIBridgeUnits, AIExcitationSource, double) | Creates an AIChannel that measures a a Wheatstone bridge. You must configure the physical channel(s) with TEDS information to use this method. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsCurrentChannel(string, string, AITerminalConfiguration, double, double, string) | Creates an AIChannel with the specified custom scale and an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsCurrentChannel(string, string, AITerminalConfiguration, double, double, double, string) | Creates an AIChannel with the specified custom scale and external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsCurrentChannel(string, string, AITerminalConfiguration, double, double, double, AICurrentUnits) | Creates an AIChannel with the specified external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsCurrentChannel(string, string, AITerminalConfiguration, double, double, AICurrentUnits) | Creates an AIChannel with an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsForceBridgeChannel(string, string, double, double, string, AIExcitationSource, double) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsForceBridgeChannel(string, string, double, double, AIForceUnits, AIExcitationSource, double) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsForceIepeChannel(string, string, AITerminalConfiguration, double, double, string, AIExcitationSource, double) | Creates an AIChannel that uses an IEPE force sensor to measure force or load, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsForceIepeChannel(string, string, AITerminalConfiguration, double, double, AIForceUnits, AIExcitationSource, double) | Creates an AIChannel that uses an IEPE force sensor to measure force or load. You must configure the physical channel(s) with TEDS information to use this method. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsLvdtChannel(string, string, double, double, AIExcitationSource, double, double, AIACExcitationWireMode, string) | Creates an AIChannel with the specified custom scale that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsLvdtChannel(string, string, double, double, AIExcitationSource, double, double, AIACExcitationWireMode, AILvdtUnits) | Creates an AIChannel that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsMicrophoneChannel(string, string, double, AITerminalConfiguration, AIExcitationSource, double, string) | Creates an AIChannel with the specified custom scale that uses a microphone to measure sound pressure. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsMicrophoneChannel(string, string, double, AITerminalConfiguration, AIExcitationSource, double, AISoundPressureUnits) | Creates an AIChannel that uses a microphone to measure sound pressure. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsPressureBridgeChannel(string, string, double, double, AIPressureUnits, AIExcitationSource, double) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. You must configure the physical channel(s) with TEDS information to use this method. |
| CreateTedsPressureBridgeChannel(string, string, double, double, string, AIExcitationSource, double) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. You must configure the physical channel(s) with TEDS information to use this method. |
| CreateTedsResistanceChannel(string, string, double, double, AIResistanceConfiguration, AIExcitationSource, double, string) | Creates an AIChannel with the specified custom scale to measure resistance. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsResistanceChannel(string, string, double, double, AIResistanceConfiguration, AIExcitationSource, double, AIResistanceUnits) | Creates an AIChannel to measure resistance. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsRtdChannel(string, string, double, double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, double) | Creates an AIChannel that uses an RTD to measure temperature. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsRvdtChannel(string, string, double, double, AIExcitationSource, double, double, AIACExcitationWireMode, string) | Creates an AIChannel that uses an RVDT to measure angular position. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsRvdtChannel(string, string, double, double, AIExcitationSource, double, double, AIACExcitationWireMode, AIRvdtUnits) | Creates an AIChannel that uses an RVDT to measure angular position. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsStrainGageChannel(string, string, double, double, AIExcitationSource, double, double, double, AIStrainUnits) | Creates an AIChannel to measure strain. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsStrainGageChannel(string, string, double, double, AIExcitationSource, double, double, double, string) | Creates an AIChannel with the specified custom scale to measure strain. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsThermistorIExChannel(string, string, double, double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, double) | Creates an AIChannel that uses a thermistor to measure temperature. Use this method when the thermistor uses current excitation. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsThermistorVExChannel(string, string, double, double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, double, double) | Creates an AIChannel that uses a thermistor to measure temperature. Use this method when the thermistor uses voltage excitation. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsThermocoupleChannel(string, string, double, double, AITemperatureUnits, string) | Creates an AIChannel that uses a thermocouple to measure temperature using a measurement on another channel for cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsThermocoupleChannel(string, string, double, double, AITemperatureUnits, double) | Creates an AIChannel that uses a thermocouple to measure temperature using a constant value cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsThermocoupleChannel(string, string, double, double, AITemperatureUnits) | Creates an AIChannel that uses a thermocouple to measure temperature using a built-in cold-junction compensation source. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsTorqueBridgeChannel(string, string, double, double, string, AIExcitationSource, double) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsTorqueBridgeChannel(string, string, double, double, AITorqueUnits, AIExcitationSource, double) | Creates an AIChannel that uses a Wheatstone bridge to measure torque. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsVoltageChannel(string, string, AITerminalConfiguration, double, double, string) | Creates an AIChannel with the specified custom scale to measure voltage. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsVoltageChannel(string, string, AITerminalConfiguration, double, double, AIVoltageUnits) | Creates an AIChannel to measure voltage. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIExcitationSource, double, string) | Creates an AIChannel with the specified custom scale to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTedsVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIExcitationSource, double, AIVoltageUnits) | Creates an AIChannel to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the AIChannelCollection. |
| CreateThermistorIExChannel(string, string, double, double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, double, double, double, double) | Creates an AIChannel that uses a thermistor to measure temperature. Use this method when the thermistor uses current excitation. This method adds one or more physical channels to the AIChannelCollection. |
| CreateThermistorVExChannel(string, string, double, double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, double, double, double, double, double) | Creates an AIChannel that uses a thermistor to measure temperature. Use this method when the thermistor uses voltage excitation. This method adds one or more physical channels to the AIChannelCollection. |
| CreateThermocoupleChannel(string, string, double, double, AIThermocoupleType, AITemperatureUnits) | Creates an AIChannel that uses a thermocouple to measure temperature using a built-in cold-junction compensation source. This method adds one or more physical channels to the AIChannelCollection. |
| CreateThermocoupleChannel(string, string, double, double, AIThermocoupleType, AITemperatureUnits, double) | Creates an AIChannel that uses a thermocouple to measure temperature using a constant value cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. |
| CreateThermocoupleChannel(string, string, double, double, AIThermocoupleType, AITemperatureUnits, string) | Creates an AIChannel that uses a thermocouple to measure temperature using a measurement on another channel for cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTorqueBridgePolynomialChannel(string, string, double, double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTorqueBridgePolynomialChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTorqueBridgeTableChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits) |  |
| CreateTorqueBridgeTableChannel(string, string, double, double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double[], AIBridgeElectricalUnits, double[], AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
| CreateTorqueBridgeTwoPointLinearChannel(string, string, double, double, string, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits) |  |
| CreateTorqueBridgeTwoPointLinearChannel(string, string, double, double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, double, double, double, double, AIBridgeElectricalUnits, double, double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
| CreateVelocityIepeChannel(string, string, AITerminalConfiguration, double, double, AIVelocityUnits, double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, double) | Creates an AIChannel that uses an IEPE velocity sensor to measure velocity. This method adds one or more physical channels to the AIChannelCollection. |
| CreateVelocityIepeChannel(string, string, AITerminalConfiguration, double, double, string, double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, double) | Creates an AIChannel that uses an IEPE velocity sensor to measure velocity. This method adds one or more physical channels to the AIChannelCollection. |
| CreateVoltageChannel(string, string, AITerminalConfiguration, double, double, AIVoltageUnits) | Creates an AIChannel to measure voltage. This method adds one or more physical channels to the AIChannelCollection. |
| CreateVoltageChannel(string, string, AITerminalConfiguration, double, double, string) | Creates an AIChannel with the specified custom scale to measure voltage. This method adds one or more physical channels to the AIChannelCollection. |
| CreateVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIBridgeConfiguration, AIExcitationSource, double, bool, AIVoltageUnits) | Creates an AIChannel to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the AIChannelCollection. |
| CreateVoltageChannelWithExcitation(string, string, AITerminalConfiguration, double, double, AIBridgeConfiguration, AIExcitationSource, double, bool, string) | Creates an AIChannel with the specified custom scale to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the AIChannelCollection. |
| CreateVoltageRmsChannel(string, string, AITerminalConfiguration, double, double, string) | Creates an AIChannel with the specified custom scale to measure AC voltage. This method adds one or more physical channels to the AIChannelCollection. |
| CreateVoltageRmsChannel(string, string, AITerminalConfiguration, double, double, AIVoltageAcrmsUnits) | Creates an AIChannel to measure AC voltage. This method adds one or more physical channels to the AIChannelCollection. |
| GetEnumerator() | Returns an enumerator that you can use to iterate through the collection. |
| ToString() | Returns a string representation of the object. |

#### See Also

- Task
- AIChannels
- AIChannel

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichargeunits.html language=enus -->
## TOPIC 00369: AIChargeUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichargeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichargeunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return charge measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIChargeUnitsRemarksSpecifies the units to use to return charge measurements from the channel. Use this enumeration to get or set the value of ChargeUnits.MembersNameValue

### AIChargeUnits Enumeration

Specifies the units to use to return charge measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIChargeUnits

#### Remarks

Specifies the units to use to return charge measurements from the channel. Use this enumeration to get or set the value of [ChargeUnits](nationalinstruments-daqmx-aichannel-chargeunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Coulombs | 16102 | Coulombs. |
| PicoCoulombs | 16103 | PicoCoulombs. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiconvertactiveedge.html language=enus -->
## TOPIC 00370: AIConvertActiveEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiconvertactiveedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiconvertactiveedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the clock pulse an analog-to-digital conversion takes place. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIConvertActiveEdgeRemarksSpecifies on which edge of the clock pulse an analog-to-digital conversion takes place. Use this enumeration to get or set the value

### AIConvertActiveEdge Enumeration

Specifies on which edge of the clock pulse an analog-to-digital conversion takes place.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIConvertActiveEdge

#### Remarks

Specifies on which edge of the clock pulse an analog-to-digital conversion takes place. Use this enumeration to get or set the value of [AIConvertActiveEdge](nationalinstruments-daqmx-timing-aiconvertactiveedge.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 10280 | Rising edge(s). |
| Falling | 10171 | Falling edge(s). |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiconvertclockpulsepolarity.html language=enus -->
## TOPIC 00371: AIConvertClockPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiconvertclockpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiconvertclockpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the polarity of the exported AI Convert Clock. The polarity is fixed and independent of the active edge of the source of the AI Convert Clock. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIConvertClockPulsePolarityRemarksIndicates the polarity of the exported AI Convert Clock. Th

### AIConvertClockPulsePolarity Enumeration

Indicates the polarity of the exported AI Convert Clock. The polarity is fixed and independent of the active edge of the source of the AI Convert Clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIConvertClockPulsePolarity

#### Remarks

Indicates the polarity of the exported AI Convert Clock. The polarity is fixed and independent of the active edge of the source of the AI Convert Clock. Use this enumeration to get or set the value of [AIConvertClockPulsePolarity](nationalinstruments-daqmx-exportsignals-aiconvertclockpulsepolarity.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveHigh | 10095 | High state is the active state. |
| ActiveLow | 10096 | Low state is the active state. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiconverttimebasesource.html language=enus -->
## TOPIC 00372: AIConvertTimebaseSource Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiconverttimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiconverttimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the AI Convert Clock Timebase. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIConvertTimebaseSourceRemarksSpecifies the terminal of the signal to use as the AI Convert Clock Timebase. Use this enumeration to get or set the value of AIConvertTim

### AIConvertTimebaseSource Enumeration

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the AI Convert Clock Timebase.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIConvertTimebaseSource

#### Remarks

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the AI Convert Clock Timebase. Use this enumeration to get or set the value of [AIConvertTimebaseSource](nationalinstruments-daqmx-timing-aiconverttimebasesource.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| SameAsSampleTimebase | 10284 | Use the same source as Sample Clock timebase. |
| SameAsMasterTimebase | 10282 | Use the same source as the Master Timebase. |
| Timebase100MHz | 15857 | Use the onboard 100 MHz timebase. |
| Timebase80MHz | 14636 | Use the onboard 80 MHz timebase. |
| Timebase20MHz | 12537 | Use the onboard 20 MHz timebase. |
| Timebase8MHz | 16023 | Use the onboard 8 MHz timebase. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aicoupling.html language=enus -->
## TOPIC 00373: AICoupling Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aicoupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aicoupling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AICouplingRemarksSpecifies the coupling for the channel. Use this enumeration to get or set the value of Coupling.MembersNameValueDescriptionAC10045Remove the DC offset from the signal. DC10050Allow NI-DAQm

### AICoupling Enumeration

Specifies the coupling for the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AICoupling

#### Remarks

Specifies the coupling for the channel. Use this enumeration to get or set the value of [Coupling](nationalinstruments-daqmx-aichannel-coupling.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AC | 10045 | Remove the DC offset from the signal. |
| DC | 10050 | Allow NI-DAQmx to measure all of the signal. |
| Ground | 10066 | Remove the signal from the measurement and measure only ground. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aicurrentacrmsunits.html language=enus -->
## TOPIC 00374: AICurrentAcrmsUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aicurrentacrmsunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aicurrentacrmsunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return current RMS measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AICurrentAcrmsUnitsRemarksSpecifies the units to use to return current RMS measurements from the channel. Use this enumeration to get or set the value of CurrentAcrms

### AICurrentAcrmsUnits Enumeration

Specifies the units to use to return current RMS measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AICurrentAcrmsUnits

#### Remarks

Specifies the units to use to return current RMS measurements from the channel. Use this enumeration to get or set the value of [CurrentAcrmsUnits](nationalinstruments-daqmx-aichannel-currentacrmsunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Amps | 10342 | Amperes. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |
| FromTeds | 12516 | Units defined by TEDS information associated with the channel. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aicurrentshuntlocation.html language=enus -->
## TOPIC 00375: AICurrentShuntLocation Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aicurrentshuntlocation.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aicurrentshuntlocation.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shunt resistor location for current measurements. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AICurrentShuntLocationRemarksSpecifies the shunt resistor location for current measurements. Use this enumeration to get or set the value of CurrentShuntLocation.MembersNameValueDesc

### AICurrentShuntLocation Enumeration

Specifies the shunt resistor location for current measurements.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AICurrentShuntLocation

#### Remarks

Specifies the shunt resistor location for current measurements. Use this enumeration to get or set the value of [CurrentShuntLocation](nationalinstruments-daqmx-aichannel-currentshuntlocation.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Internal | 10200 | Use the built-in shunt resistor of the device. |
| External | 10167 | Use a shunt resistor external to the device. You must specify the value of the shunt resistor by using CurrentShuntResistance. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aicurrentunits.html language=enus -->
## TOPIC 00376: AICurrentUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aicurrentunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aicurrentunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return current measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AICurrentUnitsRemarksSpecifies the units to use to return current measurements from the channel. Use this enumeration to get or set the value of CurrentUnits.MembersNameV

### AICurrentUnits Enumeration

Specifies the units to use to return current measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AICurrentUnits

#### Remarks

Specifies the units to use to return current measurements from the channel. Use this enumeration to get or set the value of [CurrentUnits](nationalinstruments-daqmx-aichannel-currentunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Amps | 10342 | Amperes. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |
| FromTeds | 12516 | Units defined by TEDS information associated with the channel. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aidatatransfermechanism.html language=enus -->
## TOPIC 00377: AIDataTransferMechanism Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aidatatransfermechanism.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aidatatransfermechanism.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data transfer mode for the device. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIDataTransferMechanismRemarksSpecifies the data transfer mode for the device. Use this enumeration to get or set the value of DataTransferMechanism.MembersNameValueDescriptionDma10054Direct Memory

### AIDataTransferMechanism Enumeration

Specifies the data transfer mode for the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIDataTransferMechanism

#### Remarks

Specifies the data transfer mode for the device. Use this enumeration to get or set the value of [DataTransferMechanism](nationalinstruments-daqmx-aichannel-datatransfermechanism.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Dma | 10054 | Direct Memory Access. Data transfers take place independently from the application. |
| Interrupts | 10204 | Data transfers take place independently from the application. Using interrupts increases CPU usage because the CPU must service interrupt requests. Typically, you should use interrupts if the device is out of DMA channels. |
| ProgrammedIO | 10264 | Data transfers take place when you call reading from the task or writing to the task. |
| UsbBulk | 12590 | Data transfers take place independently from the application using a USB bulk pipe. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aidatatransferrequestcondition.html language=enus -->
## TOPIC 00378: AIDataTransferRequestCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aidatatransferrequestcondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aidatatransferrequestcondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies under what condition to transfer data from the onboard memory of the device to the buffer. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIDataTransferRequestConditionRemarksSpecifies under what condition to transfer data from the onboard memory of the device to the buffer. Use thi

### AIDataTransferRequestCondition Enumeration

Specifies under what condition to transfer data from the onboard memory of the device to the buffer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIDataTransferRequestCondition

#### Remarks

Specifies under what condition to transfer data from the onboard memory of the device to the buffer. Use this enumeration to get or set the value of [DataTransferRequestCondition](nationalinstruments-daqmx-aichannel-datatransferrequestcondition.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| OnBoardMemoryMoreThanHalfFull | 10237 | Transfer data from the device when more than half of the onboard memory of the device fills. |
| OnBoardMemoryNotEmpty | 10241 | Transfer data from the device when there is data in the onboard memory. |
| OnBoardMemoryCustomThreshold | 12577 | Transfer data from the device when the number of samples specified with DataTransferCustomThreshold are in the device FIFO. |
| WhenAcquisitionComplete | 12546 | Transfer data when the acquisition is complete. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aidigitalfiltertype.html language=enus -->
## TOPIC 00379: AIDigitalFilterType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aidigitalfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aidigitalfiltertype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the AI digital filter types supported by the device. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIDigitalFilterTypeRemarksIndicates the AI digital filter types supported by the device. Use this enumeration to get or set the value of DigitalFilterTypes.MembersNameValueDescription

### AIDigitalFilterType Enumeration

Indicates the AI digital filter types supported by the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIDigitalFilterType

#### Remarks

Indicates the AI digital filter types supported by the device. Use this enumeration to get or set the value of [DigitalFilterTypes](nationalinstruments-daqmx-device-digitalfiltertypes.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Lowpass | 16071 | Lowpass filter. |
| Highpass | 16072 | Highpass filter. |
| Bandpass | 16073 | Bandpass filter. |
| Notch | 16074 | Notch filter. |
| Custom | 10137 | Custom filter. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aieddycurrentproximityprobesensitivityunits.html language=enus -->
## TOPIC 00380: AIEddyCurrentProximityProbeSensitivityUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aieddycurrentproximityprobesensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aieddycurrentproximityprobesensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of EddyCurrentProximityProbeSensitivity. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIEddyCurrentProximityProbeSensitivityUnitsRemarksSpecifies the units of EddyCurrentProximityProbeSensitivity. Use this enumeration to get or set the value of EddyCurrentProximityProbeS

### AIEddyCurrentProximityProbeSensitivityUnits Enumeration

Specifies the units of [EddyCurrentProximityProbeSensitivity](nationalinstruments-daqmx-aichannel-eddycurrentproximityprobesensitivity.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIEddyCurrentProximityProbeSensitivityUnits

#### Remarks

Specifies the units of [EddyCurrentProximityProbeSensitivity](nationalinstruments-daqmx-aichannel-eddycurrentproximityprobesensitivity.html). Use this enumeration to get or set the value of [EddyCurrentProximityProbeSensitivityUnits](nationalinstruments-daqmx-aichannel-eddycurrentproximityprobesensitivityunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| MillivoltsPerMil | 14836 | mVolts/mil. |
| VoltsPerMil | 14837 | Volts/mil. |
| MillivoltsPerMillimeter | 14838 | mVolts/mMeter. |
| VoltsPerMillimeter | 14839 | Volts/mMeter. |
| MilliVoltsPerMicron | 14840 | mVolts/micron. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aieddycurrentproximityprobeunits.html language=enus -->
## TOPIC 00381: AIEddyCurrentProximityProbeUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aieddycurrentproximityprobeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aieddycurrentproximityprobeunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return proximity measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIEddyCurrentProximityProbeUnitsRemarksSpecifies the units to use to return proximity measurements from the channel. Use this enumeration to get or set the value of Edd

### AIEddyCurrentProximityProbeUnits Enumeration

Specifies the units to use to return proximity measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIEddyCurrentProximityProbeUnits

#### Remarks

Specifies the units to use to return proximity measurements from the channel. Use this enumeration to get or set the value of [EddyCurrentProximityProbeUnits](nationalinstruments-daqmx-aichannel-eddycurrentproximityprobeunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Meters | 10219 | Meters. |
| Inches | 10379 | Inches. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiexcitationdcorac.html language=enus -->
## TOPIC 00382: AIExcitationDCOrAC Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiexcitationdcorac.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiexcitationdcorac.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if the excitation supply is DC or AC. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIExcitationDCOrACRemarksSpecifies if the excitation supply is DC or AC. Use this enumeration to get or set the value of ExcitationDCOrAC.MembersNameValueDescriptionDC10050DC excitation. AC10045AC e

### AIExcitationDCOrAC Enumeration

Specifies if the excitation supply is DC or AC.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIExcitationDCOrAC

#### Remarks

Specifies if the excitation supply is DC or AC. Use this enumeration to get or set the value of [ExcitationDCOrAC](nationalinstruments-daqmx-aichannel-excitationdcorac.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| DC | 10050 | DC excitation. |
| AC | 10045 | AC excitation. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiexcitationsense.html language=enus -->
## TOPIC 00383: AIExcitationSense Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiexcitationsense.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiexcitationsense.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use local or remote sense to sense excitation. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIExcitationSenseRemarksSpecifies whether to use local or remote sense to sense excitation. Use this enumeration to get or set the value of ExcitationSense.MembersNameValueDescri

### AIExcitationSense Enumeration

Specifies whether to use local or remote sense to sense excitation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIExcitationSense

#### Remarks

Specifies whether to use local or remote sense to sense excitation. Use this enumeration to get or set the value of [ExcitationSense](nationalinstruments-daqmx-aichannel-excitationsense.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Local | 16095 | Local. |
| Remote | 16096 | Remote. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiexcitationsource.html language=enus -->
## TOPIC 00384: AIExcitationSource Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiexcitationsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiexcitationsource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of excitation. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIExcitationSourceRemarksSpecifies the source of excitation. Use this enumeration to get or set the value of ExcitationSource.MembersNameValueDescriptionInternal10200Use the built-in excitation source of the de

### AIExcitationSource Enumeration

Specifies the source of excitation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIExcitationSource

#### Remarks

Specifies the source of excitation. Use this enumeration to get or set the value of [ExcitationSource](nationalinstruments-daqmx-aichannel-excitationsource.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Internal | 10200 | Use the built-in excitation source of the device. If you select this value, you must specify the amount of excitation. |
| External | 10167 | Use an excitation source other than the built-in excitation source of the device. If you select this value, you must specify the amount of excitation. |
| None | 10230 | Supply no excitation to the channel. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiexcitationvoltageorcurrent.html language=enus -->
## TOPIC 00385: AIExcitationVoltageOrCurrent Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiexcitationvoltageorcurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiexcitationvoltageorcurrent.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if the channel uses current or voltage excitation. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIExcitationVoltageOrCurrentRemarksSpecifies if the channel uses current or voltage excitation. Use this enumeration to get or set the value of ExcitationVoltageOrCurrent.MembersNameVal

### AIExcitationVoltageOrCurrent Enumeration

Specifies if the channel uses current or voltage excitation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIExcitationVoltageOrCurrent

#### Remarks

Specifies if the channel uses current or voltage excitation. Use this enumeration to get or set the value of [ExcitationVoltageOrCurrent](nationalinstruments-daqmx-aichannel-excitationvoltageorcurrent.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Voltage | 10322 | Voltage excitation. |
| Current | 10134 | Current excitation. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aifilterdelayunits.html language=enus -->
## TOPIC 00386: AIFilterDelayUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aifilterdelayunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aifilterdelayunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of FilterDelay and FilterDelayAdjustment. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIFilterDelayUnitsRemarksSpecifies the units of FilterDelay and FilterDelayAdjustment. Use this enumeration to get or set the value of FilterDelayUnits.MembersNameValueDescriptionSecon

### AIFilterDelayUnits Enumeration

Specifies the units of [FilterDelay](nationalinstruments-daqmx-aichannel-filterdelay.html) and [FilterDelayAdjustment](nationalinstruments-daqmx-aichannel-filterdelayadjustment.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIFilterDelayUnits

#### Remarks

Specifies the units of [FilterDelay](nationalinstruments-daqmx-aichannel-filterdelay.html) and [FilterDelayAdjustment](nationalinstruments-daqmx-aichannel-filterdelayadjustment.html). Use this enumeration to get or set the value of [FilterDelayUnits](nationalinstruments-daqmx-aichannel-filterdelayunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Seconds | 10364 | Seconds. |
| SampleClockPeriods | 10286 | Sample Clock Periods. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aifilterresponse.html language=enus -->
## TOPIC 00387: AIFilterResponse Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aifilterresponse.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aifilterresponse.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the corresponding filter response and defines the shape of the filter response. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIFilterResponseRemarksSpecifies the corresponding filter response and defines the shape of the filter response. Use this enumeration to get or set the valu

### AIFilterResponse Enumeration

Specifies the corresponding filter response and defines the shape of the filter response.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIFilterResponse

#### Remarks

Specifies the corresponding filter response and defines the shape of the filter response. Use this enumeration to get or set the value of [FilterResponse](nationalinstruments-daqmx-aichannel-filterresponse.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Comb | 16152 | Comb filter response. |
| Bessel | 16153 | Bessel filter response. |
| Brickwall | 16155 | Brickwall filter response. |
| Butterworth | 16076 | Butterworth filter response. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiforceiepesensorsensitivityunits.html language=enus -->
## TOPIC 00388: AIForceIepeSensorSensitivityUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiforceiepesensorsensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiforceiepesensorsensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units for ForceIepeSensorSensitivity. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIForceIepeSensorSensitivityUnitsRemarksSpecifies the units for ForceIepeSensorSensitivity. Use this enumeration to get or set the value of ForceIepeSensorSensitivityUnits.MembersNameValueDescri

### AIForceIepeSensorSensitivityUnits Enumeration

Specifies the units for [ForceIepeSensorSensitivity](nationalinstruments-daqmx-aichannel-forceiepesensorsensitivity.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIForceIepeSensorSensitivityUnits

#### Remarks

Specifies the units for [ForceIepeSensorSensitivity](nationalinstruments-daqmx-aichannel-forceiepesensorsensitivity.html). Use this enumeration to get or set the value of [ForceIepeSensorSensitivityUnits](nationalinstruments-daqmx-aichannel-forceiepesensorsensitivityunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| MillivoltsPerNewton | 15891 | Millivolts per newton. |
| MillivoltsPerPound | 15892 | Millivolts per pound. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiforceunits.html language=enus -->
## TOPIC 00389: AIForceUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiforceunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiforceunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in which unit to return force or load measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIForceUnitsRemarksSpecifies in which unit to return force or load measurements from the channel. Use this enumeration to get or set the value of ForceUnits.MembersNam

### AIForceUnits Enumeration

Specifies in which unit to return force or load measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIForceUnits

#### Remarks

Specifies in which unit to return force or load measurements from the channel. Use this enumeration to get or set the value of [ForceUnits](nationalinstruments-daqmx-aichannel-forceunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Newtons | 15875 | Newtons. |
| Pounds | 15876 | Pounds. |
| KilogramForce | 15877 | Kilograms-force. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aifrequencyunits.html language=enus -->
## TOPIC 00390: AIFrequencyUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aifrequencyunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aifrequencyunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return frequency measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIFrequencyUnitsRemarksSpecifies the units to use to return frequency measurements from the channel. Use this enumeration to get or set the value of FrequencyUnits.Memb

### AIFrequencyUnits Enumeration

Specifies the units to use to return frequency measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIFrequencyUnits

#### Remarks

Specifies the units to use to return frequency measurements from the channel. Use this enumeration to get or set the value of [FrequencyUnits](nationalinstruments-daqmx-aichannel-frequencyunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Hertz | 10373 | Hertz. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiholdcompleteeventpulsepolarity.html language=enus -->
## TOPIC 00391: AIHoldCompleteEventPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiholdcompleteeventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiholdcompleteeventpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of an exported AI Hold Complete Event pulse. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIHoldCompleteEventPulsePolarityRemarksSpecifies the polarity of an exported AI Hold Complete Event pulse. Use this enumeration to get or set the value of AIHoldCompleteEventPuls

### AIHoldCompleteEventPulsePolarity Enumeration

Specifies the polarity of an exported AI Hold Complete Event pulse.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIHoldCompleteEventPulsePolarity

#### Remarks

Specifies the polarity of an exported AI Hold Complete Event pulse. Use this enumeration to get or set the value of [AIHoldCompleteEventPulsePolarity](nationalinstruments-daqmx-exportsignals-aiholdcompleteeventpulsepolarity.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveHigh | 10095 | High state is the active state. |
| ActiveLow | 10096 | Low state is the active state. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-ailowpassswitchedcapacitorclocksource.html language=enus -->
## TOPIC 00392: AILowpassSwitchedCapacitorClockSource Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-ailowpassswitchedcapacitorclocksource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-ailowpassswitchedcapacitorclocksource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the filter clock. If you need a higher resolution for the filter, you can supply an external clock to increase the resolution. Refer to the SCXI-1141/1142/1143 User Manual for more information. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AILowpassSwitchedCapacitorCl

### AILowpassSwitchedCapacitorClockSource Enumeration

Specifies the source of the filter clock. If you need a higher resolution for the filter, you can supply an external clock to increase the resolution. Refer to the SCXI-1141/1142/1143 User Manual for more information.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AILowpassSwitchedCapacitorClockSource

#### Remarks

Specifies the source of the filter clock. If you need a higher resolution for the filter, you can supply an external clock to increase the resolution. Refer to the SCXI-1141/1142/1143 User Manual for more information. Use this enumeration to get or set the value of [LowpassSwitchedCapacitorClockSource](nationalinstruments-daqmx-aichannel-lowpassswitchedcapacitorclocksource.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Internal | 10200 | Internal to the device. |
| External | 10167 | External to the device. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-ailvdtsensitivityunits.html language=enus -->
## TOPIC 00393: AILvdtSensitivityUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-ailvdtsensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-ailvdtsensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of LvdtSensitivity. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AILvdtSensitivityUnitsRemarksSpecifies the units of LvdtSensitivity. Use this enumeration to get or set the value of LvdtSensitivityUnits.MembersNameValueDescriptionMillivoltsPerVoltPerMillimeter12506mVolts

### AILvdtSensitivityUnits Enumeration

Specifies the units of [LvdtSensitivity](nationalinstruments-daqmx-aichannel-lvdtsensitivity.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AILvdtSensitivityUnits

#### Remarks

Specifies the units of [LvdtSensitivity](nationalinstruments-daqmx-aichannel-lvdtsensitivity.html). Use this enumeration to get or set the value of [LvdtSensitivityUnits](nationalinstruments-daqmx-aichannel-lvdtsensitivityunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| MillivoltsPerVoltPerMillimeter | 12506 | mVolts/Volt/mMeter. |
| MillivoltsPerVoltPerMilliinch | 12505 | mVolts/Volt/0.001 Inch. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-ailvdtunits.html language=enus -->
## TOPIC 00394: AILvdtUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-ailvdtunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-ailvdtunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return linear position measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AILvdtUnitsRemarksSpecifies the units to use to return linear position measurements from the channel. Use this enumeration to get or set the value of LvdtUnits.Me

### AILvdtUnits Enumeration

Specifies the units to use to return linear position measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AILvdtUnits

#### Remarks

Specifies the units to use to return linear position measurements from the channel. Use this enumeration to get or set the value of [LvdtUnits](nationalinstruments-daqmx-aichannel-lvdtunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Meters | 10219 | Meters. |
| Inches | 10379 | Inches. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aimeasurementtype.html language=enus -->
## TOPIC 00395: AIMeasurementType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aimeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aimeasurementtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the measurement to take with the analog input channel and in some cases, such as for temperature measurements, the sensor to use. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIMeasurementTypeRemarksIndicates the measurement to take with the analog input channel and in some cases,

### AIMeasurementType Enumeration

Indicates the measurement to take with the analog input channel and in some cases, such as for temperature measurements, the sensor to use.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIMeasurementType

#### Remarks

Indicates the measurement to take with the analog input channel and in some cases, such as for temperature measurements, the sensor to use. Use this enumeration to get or set the value of [MeasurementType](nationalinstruments-daqmx-aichannel-measurementtype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Voltage | 10322 | Voltage measurement. |
| VoltageRms | 10350 | Voltage RMS measurement. |
| Current | 10134 | Current measurement. |
| CurrentRms | 10351 | Current RMS measurement. |
| VoltageCustomWithExcitation | 10323 | Voltage measurement with an excitation source. You can use this measurement type for custom sensors that require excitation, but you must use a custom scale to scale the measured voltage. |
| Bridge | 15908 | Measure voltage ratios from a Wheatstone bridge. |
| Frequency | 10181 | Frequency measurement using a frequency to voltage converter. |
| Resistance | 10278 | Resistance measurement. |
| Thermocouple | 10303 | Temperature measurement using a thermocouple. |
| Thermistor | 10302 | Temperature measurement using a thermistor. |
| Rtd | 10301 | Temperature measurement using an RTD. |
| BuiltInTemperatureSensor | 10311 | Temperature measurement using a built-in sensor on a terminal block or device. On SCXI modules, for example, this could be the CJC sensor. |
| StrainGage | 10300 | Strain measurement. |
| RosetteStrainGage | 15980 | Strain measurement using a rosette strain gage. |
| Lvdt | 10352 | Position measurement using an LVDT. |
| Rvdt | 10353 | Position measurement using an RVDT. |
| EddyCurrentProximityProbe | 14835 | Position measurement using an eddy current proximity probe. |
| Accelerometer | 10356 | Acceleration measurement using an accelerometer. |
| AccelerationCharge | 16104 | Acceleration measurement using a charge-based sensor. |
| AccelerationFourWireDCVoltage | 16106 | Acceleration measurement using a 4 wire DC voltage based sensor. |
| VelocityIepeSensor | 15966 | Velocity measurement using an IEPE Sensor. |
| ForceBridge | 15899 | Force measurement using a bridge-based sensor. |
| ForceIepeSensor | 15895 | Force measurement using an IEPE Sensor. |
| PressureBridge | 15902 | Pressure measurement using a bridge-based sensor. |
| Microphone | 10354 | Sound pressure measurement using a microphone. |
| TorqueBridge | 15905 | Torque measurement using a bridge-based sensor. |
| TedsSensor | 12531 | Measurement type defined by TEDS. |
| Charge | 16105 | Charge measurement. |
| Power | 16201 | Power source and measurement. |
| CalculatedPower | 16204 | Calculated power measurement. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aipowermeasurement-aipowermeasurement__double-double.html language=enus -->
## TOPIC 00396: AIPowerMeasurement(double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aipowermeasurement-aipowermeasurement__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aipowermeasurement-aipowermeasurement__double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the AIPowerMeasurement object with the specified initial values. SyntaxNamespace: NationalInstruments.DAQmxpublic AIPowerMeasurement(double voltage, double current)ParametersNameTypeDescriptionvoltagedoubleThe voltage component of the power measurement.currentdoubleThe

### AIPowerMeasurement(double, double)

Initializes a new instance of the [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html) object with the specified initial values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AIPowerMeasurement(double voltage, double current)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| voltage | double | The voltage component of the power measurement. |
| current | double | The current component of the power measurement. |

Parent topic:

AIPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aipowermeasurement-current.html language=enus -->
## TOPIC 00397: Current

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aipowermeasurement-current.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aipowermeasurement-current.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the current component of the power measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic double Current { get; set; }RemarksThe current value in amperes.

### Current

Gets or sets the current component of the power measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Current { get; set; }

#### Remarks

The current value in amperes.

Parent topic:

AIPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aipowermeasurement-equals__aipowermeasurement-aipowermeasurement.html language=enus -->
## TOPIC 00398: Equals(AIPowerMeasurement, AIPowerMeasurement)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aipowermeasurement-equals__aipowermeasurement-aipowermeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aipowermeasurement-equals__aipowermeasurement-aipowermeasurement.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a value indicating if two specified instances of AIPowerMeasurement are equal. SyntaxNamespace: NationalInstruments.DAQmxpublic static bool Equals(AIPowerMeasurement obj1, AIPowerMeasurement obj2)ParametersNameTypeDescriptionobj1AIPowerMeasurementA AIPowerMeasurement object.obj2AIPowerMeasur

### Equals(AIPowerMeasurement, AIPowerMeasurement)

Returns a value indicating if two specified instances of [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public static bool Equals(AIPowerMeasurement obj1, AIPowerMeasurement obj2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj1 | AIPowerMeasurement | A AIPowerMeasurement object. |
| obj2 | AIPowerMeasurement | A AIPowerMeasurement object. |

#### Returns

true if *obj1*  and *obj2*  are equal.

Parent topic:

AIPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aipowermeasurement-equals__aipowermeasurement.html language=enus -->
## TOPIC 00399: Equals(AIPowerMeasurement)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aipowermeasurement-equals__aipowermeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aipowermeasurement-equals__aipowermeasurement.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a value indicating if this instance is equal to the specified AIPowerMeasurement object. SyntaxNamespace: NationalInstruments.DAQmxpublic bool Equals(AIPowerMeasurement obj)ParametersNameTypeDescriptionobjAIPowerMeasurementA AIPowerMeasurement object to compare with this instance.Returnstrue

### Equals(AIPowerMeasurement)

Returns a value indicating if this instance is equal to the specified [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html) object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool Equals(AIPowerMeasurement obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | AIPowerMeasurement | A AIPowerMeasurement object to compare with this instance. |

#### Returns

true if *obj*  has the same low ticks and high ticks as this instance.

Parent topic:

AIPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aipowermeasurement-equals__object.html language=enus -->
## TOPIC 00400: Equals(object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aipowermeasurement-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aipowermeasurement-equals__object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a value indicating if this instance is equal to the specified object. SyntaxNamespace: NationalInstruments.DAQmxpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectAn object to compare with this instance.Returnstrue if obj is a AIPowerMeasurement object that has the

### Equals(object)

Returns a value indicating if this instance is equal to the specified object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | An object to compare with this instance. |

#### Returns

true if *obj*  is a [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html) object that has the same low ticks and high ticks as this instance.

Parent topic:

AIPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aipowermeasurement-gethashcode.html language=enus -->
## TOPIC 00401: GetHashCode()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aipowermeasurement-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aipowermeasurement-gethashcode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a hash code for the AIPowerMeasurement object. SyntaxNamespace: NationalInstruments.DAQmxpublic override int GetHashCode()RemarksTwo AIPowerMeasurement objects might have the same hash code even though they represent different values. ReturnsA 32-bit signed integer hash code.

### GetHashCode()

Returns a hash code for the [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html) object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override int GetHashCode()

#### Remarks

Two [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html) objects might have the same hash code even though they represent different values.

#### Returns

A 32-bit signed integer hash code.

Parent topic:

AIPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aipowermeasurement-getobjectdata__serializationinfo-streamingcontext.html language=enus -->
## TOPIC 00402: GetObjectData(SerializationInfo, StreamingContext)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aipowermeasurement-getobjectdata__serializationinfo-streamingcontext.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aipowermeasurement-getobjectdata__serializationinfo-streamingcontext.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the SerializationInfo object with information about the exception. SyntaxNamespace: NationalInstruments.DAQmxpublic void GetObjectData(SerializationInfo info, StreamingContext context)ParametersNameTypeDescriptioninfoSerializationInfoObject that holds the serialized object data.contextStreaming

### GetObjectData(SerializationInfo, StreamingContext)

Sets the SerializationInfo object with information about the exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void GetObjectData(SerializationInfo info, StreamingContext context)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| info | SerializationInfo | Object that holds the serialized object data. |
| context | StreamingContext | Contextual information about the source or destination. |

Parent topic:

AIPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aipowermeasurement-operator_eq__aipowermeasurement-aipowermeasurement.html language=enus -->
## TOPIC 00403: operator==(AIPowerMeasurement, AIPowerMeasurement)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aipowermeasurement-operator_eq__aipowermeasurement-aipowermeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aipowermeasurement-operator_eq__aipowermeasurement-aipowermeasurement.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns true if two AIPowerMeasurement objects are equal. SyntaxNamespace: NationalInstruments.DAQmxpublic static bool operator==(AIPowerMeasurement obj1, AIPowerMeasurement obj2)ParametersNameTypeDescriptionobj1AIPowerMeasurementA AIPowerMeasurement object.obj2AIPowerMeasurementA AIPowerMeasurement

### operator==(AIPowerMeasurement, AIPowerMeasurement)

Returns true if two [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html) objects are equal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public static bool operator==(AIPowerMeasurement obj1, AIPowerMeasurement obj2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj1 | AIPowerMeasurement | A AIPowerMeasurement object. |
| obj2 | AIPowerMeasurement | A AIPowerMeasurement object. |

#### Returns

true if the values of *obj1*  and *obj2*  are equal.

Parent topic:

AIPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aipowermeasurement-operator_neq__aipowermeasurement-aipowermeasurement.html language=enus -->
## TOPIC 00404: operator!=(AIPowerMeasurement, AIPowerMeasurement)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aipowermeasurement-operator_neq__aipowermeasurement-aipowermeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aipowermeasurement-operator_neq__aipowermeasurement-aipowermeasurement.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns true if two AIPowerMeasurement objects are not equal. SyntaxNamespace: NationalInstruments.DAQmxpublic static bool operator!=(AIPowerMeasurement obj1, AIPowerMeasurement obj2)ParametersNameTypeDescriptionobj1AIPowerMeasurementA AIPowerMeasurement object.obj2AIPowerMeasurementA AIPowerMeasure

### operator!=(AIPowerMeasurement, AIPowerMeasurement)

Returns true if two [AIPowerMeasurement](nationalinstruments-daqmx-aipowermeasurement.html) objects are not equal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public static bool operator!=(AIPowerMeasurement obj1, AIPowerMeasurement obj2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj1 | AIPowerMeasurement | A AIPowerMeasurement object. |
| obj2 | AIPowerMeasurement | A AIPowerMeasurement object. |

#### Returns

true if the values of *obj1*  and *obj2*  are not equal.

Parent topic:

AIPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aipowermeasurement-voltage.html language=enus -->
## TOPIC 00405: Voltage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aipowermeasurement-voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aipowermeasurement-voltage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the voltage component of the power measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic double Voltage { get; set; }RemarksThe voltage value in volts.

### Voltage

Gets or sets the voltage component of the power measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Voltage { get; set; }

#### Remarks

The voltage value in volts.

Parent topic:

AIPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aipowermeasurement.html language=enus -->
## TOPIC 00406: AIPowerMeasurement Data Structure

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aipowermeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aipowermeasurement.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates a power measurement specified in terms of voltage and current. Derives fromISerializableSyntaxNamespace: NationalInstruments.DAQmxpublic struct AIPowerMeasurement : ISerializableThread SafetyAny members of this type are not guaranteed to be thread safe.ConstructorsNameDescriptionAIPower

### AIPowerMeasurement Data Structure

Encapsulates a power measurement specified in terms of voltage and current.

#### Derives from

- ISerializable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public struct AIPowerMeasurement : ISerializable

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| AIPowerMeasurement(double, double) | Initializes a new instance of the AIPowerMeasurement object with the specified initial values. |

#### Properties

| Name | Description |
| --- | --- |
| Current | Gets or sets the current component of the power measurement. |
| Voltage | Gets or sets the voltage component of the power measurement. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(object) | Returns a value indicating if this instance is equal to the specified object. |
| Equals(AIPowerMeasurement) | Returns a value indicating if this instance is equal to the specified AIPowerMeasurement object. |
| GetHashCode() | Returns a hash code for the AIPowerMeasurement object. |
| GetObjectData(SerializationInfo, StreamingContext) | Sets the SerializationInfo object with information about the exception. |
| Equals(AIPowerMeasurement, AIPowerMeasurement) | Returns a value indicating if two specified instances of AIPowerMeasurement are equal. |

#### Operators

| Name | Description |
| --- | --- |
| operator!=(AIPowerMeasurement, AIPowerMeasurement) | Returns true if two AIPowerMeasurement objects are not equal. |
| operator==(AIPowerMeasurement, AIPowerMeasurement) | Returns true if two AIPowerMeasurement objects are equal. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aipowerunits.html language=enus -->
## TOPIC 00407: AIPowerUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aipowerunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aipowerunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return power measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIPowerUnitsRemarksSpecifies the units to use to return power measurements from the channel. Use this enumeration to get or set the value of CalculatedPowerUnits.MembersNam

### AIPowerUnits Enumeration

Specifies the units to use to return power measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIPowerUnits

#### Remarks

Specifies the units to use to return power measurements from the channel. Use this enumeration to get or set the value of [CalculatedPowerUnits](nationalinstruments-daqmx-aichannel-calculatedpowerunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Watts | 16203 | Watts. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aipressureunits.html language=enus -->
## TOPIC 00408: AIPressureUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aipressureunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aipressureunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in which unit to return pressure measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIPressureUnitsRemarksSpecifies in which unit to return pressure measurements from the channel. Use this enumeration to get or set the value of PressureUnits.MembersNameVal

### AIPressureUnits Enumeration

Specifies in which unit to return pressure measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIPressureUnits

#### Remarks

Specifies in which unit to return pressure measurements from the channel. Use this enumeration to get or set the value of [PressureUnits](nationalinstruments-daqmx-aichannel-pressureunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Pascals | 10081 | Pascals. |
| PoundsPerSquareInch | 15879 | Pounds per square inch. |
| Bar | 15880 | Bar. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-airawdatacompressiontype.html language=enus -->
## TOPIC 00409: AIRawDataCompressionType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-airawdatacompressiontype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-airawdatacompressiontype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of compression to apply to raw samples returned from the device. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIRawDataCompressionTypeRemarksSpecifies the type of compression to apply to raw samples returned from the device. Use this enumeration to get or set the value of

### AIRawDataCompressionType Enumeration

Specifies the type of compression to apply to [raw samples](/csh?context=nidaqmx_mxcncpts_rawdata) returned from the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIRawDataCompressionType

#### Remarks

Specifies the type of compression to apply to [raw samples](/csh?context=nidaqmx_mxcncpts_rawdata) returned from the device. Use this enumeration to get or set the value of [RawDataCompressionType](nationalinstruments-daqmx-aichannel-rawdatacompressiontype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 10230 | Do not compress samples. |
| LosslessPacking | 12555 | Remove unused bits from samples. No resolution is lost. |
| LossyLsbRemoval | 12556 | Remove unused bits from samples. Then, if necessary, remove bits from samples until the samples are the size specified with LossyLsbRemovalCompressedSampleSize. This compression type limits resolution to the specified sample size. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-airawsamplejustification.html language=enus -->
## TOPIC 00410: AIRawSampleJustification Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-airawsamplejustification.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-airawsamplejustification.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the justification of a raw sample from the device. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIRawSampleJustificationRemarksIndicates the justification of a raw sample from the device. Use this enumeration to get or set the value of RawSampleJustification.MembersNameValueDescri

### AIRawSampleJustification Enumeration

Indicates the justification of a [raw sample](/csh?context=nidaqmx_mxcncpts_rawdata) from the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIRawSampleJustification

#### Remarks

Indicates the justification of a [raw sample](/csh?context=nidaqmx_mxcncpts_rawdata) from the device. Use this enumeration to get or set the value of [RawSampleJustification](nationalinstruments-daqmx-aichannel-rawsamplejustification.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| RightJustified | 10279 | Samples occupy the lower bits of the integer. |
| LeftJustified | 10209 | Samples occupy the higher bits of the integer. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-airesistanceconfiguration.html language=enus -->
## TOPIC 00411: AIResistanceConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-airesistanceconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-airesistanceconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resistance configuration for the channel. NI-DAQmx uses this value for any resistance-based measurements, including temperature measurement using a thermistor or RTD. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIResistanceConfigurationRemarksSpecifies the resistance configur

### AIResistanceConfiguration Enumeration

Specifies the resistance configuration for the channel. NI-DAQmx uses this value for any resistance-based measurements, including temperature measurement using a thermistor or RTD.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIResistanceConfiguration

#### Remarks

Specifies the resistance configuration for the channel. NI-DAQmx uses this value for any resistance-based measurements, including temperature measurement using a thermistor or RTD. Use this enumeration to get or set the value of [ResistanceConfiguration](nationalinstruments-daqmx-aichannel-resistanceconfiguration.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| TwoWire | 2 | 2-wire mode. |
| ThreeWire | 3 | 3-wire mode. |
| FourWire | 4 | 4-wire mode. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-airesistanceunits.html language=enus -->
## TOPIC 00412: AIResistanceUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-airesistanceunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-airesistanceunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return resistance measurements. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIResistanceUnitsRemarksSpecifies the units to use to return resistance measurements. Use this enumeration to get or set the value of ResistanceUnits.MembersNameValueDescriptionOhms103

### AIResistanceUnits Enumeration

Specifies the units to use to return resistance measurements.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIResistanceUnits

#### Remarks

Specifies the units to use to return resistance measurements. Use this enumeration to get or set the value of [ResistanceUnits](nationalinstruments-daqmx-aichannel-resistanceunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Ohms | 10384 | Ohms. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |
| FromTeds | 12516 | Units defined by TEDS information associated with the channel. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-airesolutionunits.html language=enus -->
## TOPIC 00413: AIResolutionUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-airesolutionunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-airesolutionunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the units of Resolution. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIResolutionUnitsRemarksIndicates the units of Resolution. Use this enumeration to get or set the value of ResolutionUnits.MembersNameValueDescriptionBits10109Bits.

### AIResolutionUnits Enumeration

Indicates the units of [Resolution](nationalinstruments-daqmx-aichannel-resolution.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIResolutionUnits

#### Remarks

Indicates the units of [Resolution](nationalinstruments-daqmx-aichannel-resolution.html). Use this enumeration to get or set the value of [ResolutionUnits](nationalinstruments-daqmx-aichannel-resolutionunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Bits | 10109 | Bits. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-airosettemeasurementtype.html language=enus -->
## TOPIC 00414: AIRosetteMeasurementType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-airosettemeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-airosettemeasurementtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of rosette measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIRosetteMeasurementTypeRemarksSpecifies the type of rosette measurement. Use this enumeration to get or set the value of RosetteMeasurementType.MembersNameValueDescriptionPrincipalStrain115971The maximu

### AIRosetteMeasurementType Enumeration

Specifies the type of rosette measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIRosetteMeasurementType

#### Remarks

Specifies the type of rosette measurement. Use this enumeration to get or set the value of [RosetteMeasurementType](nationalinstruments-daqmx-aichannel-rosettemeasurementtype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| PrincipalStrain1 | 15971 | The maximum tensile strain coplanar to the surface of the material under stress. |
| PrincipalStrain2 | 15972 | The minimum tensile strain coplanar to the surface of the material under stress. |
| PrincipalStrainAngle | 15973 | The angle at which the principal strains of the rosette occur. |
| CartesianStrainX | 15974 | The tensile strain coplanar to the surface of the material under stress in the X coordinate direction. |
| CartesianStrainY | 15975 | The tensile strain coplanar to the surface of the material under stress in the Y coordinate direction. |
| CartesianShearStrainXY | 15976 | The tensile strain coplanar to the surface of the material under stress in the XY coordinate direction. |
| MaximumShearStrain | 15977 | The maximum strain coplanar to the cross section of the material under stress. |
| MaximumShearStrainAngle | 15978 | The angle at which the maximum shear strain of the rosette occurs. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-airosettetype.html language=enus -->
## TOPIC 00415: AIRosetteType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-airosettetype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-airosettetype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the type of rosette gage. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIRosetteTypeRemarksIndicates the type of rosette gage. Use this enumeration to get or set the value of RosetteType.MembersNameValueDescriptionRectangular15968A rectangular rosette consists of three strain gage

### AIRosetteType Enumeration

Indicates the type of rosette gage.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIRosetteType

#### Remarks

Indicates the type of rosette gage. Use this enumeration to get or set the value of [RosetteType](nationalinstruments-daqmx-aichannel-rosettetype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rectangular | 15968 | A rectangular rosette consists of three strain gages, each separated by a 45 degree angle. |
| Delta | 15969 | A delta rosette consists of three strain gages, each separated by a 60 degree angle. |
| Tee | 15970 | A tee rosette consists of two gages oriented at 90 degrees with respect to each other. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-airtdtype.html language=enus -->
## TOPIC 00416: AIRtdType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-airtdtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-airtdtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of RTD connected to the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIRtdTypeRemarksSpecifies the type of RTD connected to the channel. Use this enumeration to get or set the value of RtdType.MembersNameValueDescriptionPt375012481Pt3750. Pt385110071Pt3851. Pt391

### AIRtdType Enumeration

Specifies the [type](/csh?context=nidaqmx_measfunds_rtd) of RTD connected to the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIRtdType

#### Remarks

Specifies the [type](/csh?context=nidaqmx_measfunds_rtd) of RTD connected to the channel. Use this enumeration to get or set the value of [RtdType](nationalinstruments-daqmx-aichannel-rtdtype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Pt3750 | 12481 | Pt3750. |
| Pt3851 | 10071 | Pt3851. |
| Pt3911 | 12482 | Pt3911. |
| Pt3916 | 10069 | Pt3916. |
| Pt3920 | 10053 | Pt3920. |
| Pt3928 | 12483 | Pt3928. |
| Custom | 10137 | You must use RtdA, RtdB, and RtdC to supply the coefficients for the Callendar-Van Dusen equation. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-airvdtsensitivityunits.html language=enus -->
## TOPIC 00417: AIRvdtSensitivityUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-airvdtsensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-airvdtsensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of RvdtSensitivity. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIRvdtSensitivityUnitsRemarksSpecifies the units of RvdtSensitivity. Use this enumeration to get or set the value of RvdtSensitivityUnits.MembersNameValueDescriptionMillivoltsPerVoltPerDegree12507mVolts/Vol

### AIRvdtSensitivityUnits Enumeration

Specifies the units of [RvdtSensitivity](nationalinstruments-daqmx-aichannel-rvdtsensitivity.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIRvdtSensitivityUnits

#### Remarks

Specifies the units of [RvdtSensitivity](nationalinstruments-daqmx-aichannel-rvdtsensitivity.html). Use this enumeration to get or set the value of [RvdtSensitivityUnits](nationalinstruments-daqmx-aichannel-rvdtsensitivityunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| MillivoltsPerVoltPerDegree | 12507 | mVolts/Volt/Degree. |
| MillivoltsPerVoltPerRadian | 12508 | mVolts/Volt/Radian. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-airvdtunits.html language=enus -->
## TOPIC 00418: AIRvdtUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-airvdtunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-airvdtunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return angular position measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIRvdtUnitsRemarksSpecifies the units to use to return angular position measurements from the channel. Use this enumeration to get or set the value of RvdtUnits.

### AIRvdtUnits Enumeration

Specifies the units to use to return angular position measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIRvdtUnits

#### Remarks

Specifies the units to use to return angular position measurements from the channel. Use this enumeration to get or set the value of [RvdtUnits](nationalinstruments-daqmx-aichannel-rvdtunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Degrees | 10146 | Degrees. |
| Radians | 10273 | Radians. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aisensorpowerconfiguration.html language=enus -->
## TOPIC 00419: AISensorPowerConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aisensorpowerconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aisensorpowerconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to turn on the sensor's power supply or to leave the configuration unchanged. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AISensorPowerConfigurationRemarksSpecifies whether to turn on the sensor's power supply or to leave the configuration unchanged. Use this enumeration

### AISensorPowerConfiguration Enumeration

Specifies whether to turn on the sensor's power supply or to leave the configuration unchanged.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AISensorPowerConfiguration

#### Remarks

Specifies whether to turn on the sensor's power supply or to leave the configuration unchanged. Use this enumeration to get or set the value of [SensorPowerConfiguration](nationalinstruments-daqmx-aichannel-sensorpowerconfiguration.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| NoChange | 10160 | Sensor power supply configuration is not changed. |
| Enabled | 16145 | Sensor power supply is turned on. |
| Disabled | 16146 | Sensor power supply is turned off. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aisensorpowertype.html language=enus -->
## TOPIC 00420: AISensorPowerType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aisensorpowertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aisensorpowertype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of power supplied to the sensor. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AISensorPowerTypeRemarksSpecifies the type of power supplied to the sensor. Use this enumeration to get or set the value of SensorPowerType.MembersNameValueDescriptionDC10050Sensor power supply

### AISensorPowerType Enumeration

Specifies the type of power supplied to the sensor.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AISensorPowerType

#### Remarks

Specifies the type of power supplied to the sensor. Use this enumeration to get or set the value of [SensorPowerType](nationalinstruments-daqmx-aichannel-sensorpowertype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| DC | 10050 | Sensor power supply generates a single DC voltage level. |
| AC | 10045 | Sensor power supply generates an AC voltage. |
| BipolarDC | 16147 | Sensor power supply generates a pair of DC voltage levels. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aisoundpressureunits.html language=enus -->
## TOPIC 00421: AISoundPressureUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aisoundpressureunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aisoundpressureunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return sound pressure measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AISoundPressureUnitsRemarksSpecifies the units to use to return sound pressure measurements from the channel. Use this enumeration to get or set the value of Sound

### AISoundPressureUnits Enumeration

Specifies the units to use to return sound pressure measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AISoundPressureUnits

#### Remarks

Specifies the units to use to return sound pressure measurements from the channel. Use this enumeration to get or set the value of [SoundPressureUnits](nationalinstruments-daqmx-aichannel-soundpressureunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Pascals | 10081 | Pascals. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aistraingageconfiguration.html language=enus -->
## TOPIC 00422: AIStrainGageConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aistraingageconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aistraingageconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bridge configuration of the strain gages. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIStrainGageConfigurationRemarksSpecifies the bridge configuration of the strain gages. Use this enumeration to get or set the value of StrainGageConfiguration.MembersNameValueDescriptionFul

### AIStrainGageConfiguration Enumeration

Specifies the [bridge configuration](/csh?context=nidaqmx_measfunds_bridgeconfig) of the strain gages.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIStrainGageConfiguration

#### Remarks

Specifies the [bridge configuration](/csh?context=nidaqmx_measfunds_bridgeconfig) of the strain gages. Use this enumeration to get or set the value of [StrainGageConfiguration](nationalinstruments-daqmx-aichannel-straingageconfiguration.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FullBridgeI | 10183 | Four active gages with two pairs subjected to equal and opposite strains. |
| FullBridgeII | 10184 | Four active gages with two aligned with maximum principal strain and two Poisson gages in adjacent arms. |
| FullBridgeIII | 10185 | Four active gages with two aligned with maximum principal strain and two Poisson gages in opposite arms. |
| HalfBridgeI | 10188 | Two active gages with one aligned with maximum principal strain and one Poisson gage. |
| HalfBridgeII | 10189 | Two active gages with equal and opposite strains. |
| QuarterBridgeI | 10271 | Single active gage. |
| QuarterBridgeII | 10272 | Single active gage and one dummy gage. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aistrainunits.html language=enus -->
## TOPIC 00423: AIStrainUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aistrainunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aistrainunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return strain measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIStrainUnitsRemarksSpecifies the units to use to return strain measurements from the channel. Use this enumeration to get or set the value of StrainUnits.MembersNameValue

### AIStrainUnits Enumeration

Specifies the units to use to return strain measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIStrainUnits

#### Remarks

Specifies the units to use to return strain measurements from the channel. Use this enumeration to get or set the value of [StrainUnits](nationalinstruments-daqmx-aichannel-strainunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Strain | 10299 | Strain. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aitemperatureunits.html language=enus -->
## TOPIC 00424: AITemperatureUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aitemperatureunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aitemperatureunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return temperature measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AITemperatureUnitsRemarksSpecifies the units to use to return temperature measurements from the channel. Use this enumeration to get or set the value of TemperatureUn

### AITemperatureUnits Enumeration

Specifies the units to use to return temperature measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AITemperatureUnits

#### Remarks

Specifies the units to use to return temperature measurements from the channel. Use this enumeration to get or set the value of [TemperatureUnits](nationalinstruments-daqmx-aichannel-temperatureunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| DegreesC | 10143 | Degrees Celsius. |
| DegreesF | 10144 | Degrees Fahrenheit. |
| Kelvins | 10325 | Kelvins. |
| DegreesR | 10145 | Degrees Rankine. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiterminalconfiguration.html language=enus -->
## TOPIC 00425: AITerminalConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiterminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal configuration for the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AITerminalConfigurationRemarksSpecifies the terminal configuration for the channel. Use this enumeration to get or set the value of TerminalConfiguration.MembersNameValueDescriptionRse10083Ref

### AITerminalConfiguration Enumeration

Specifies the terminal configuration for the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AITerminalConfiguration

#### Remarks

Specifies the terminal configuration for the channel. Use this enumeration to get or set the value of [TerminalConfiguration](nationalinstruments-daqmx-aichannel-terminalconfiguration.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rse | 10083 | Referenced Single-Ended. |
| Nrse | 10078 | Non-Referenced Single-Ended. |
| Differential | 10106 | Differential. |
| Pseudodifferential | 12529 | Pseudodifferential. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aithermocouplecjcsource.html language=enus -->
## TOPIC 00426: AIThermocoupleCjcSource Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aithermocouplecjcsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aithermocouplecjcsource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the source of cold-junction compensation. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIThermocoupleCjcSourceRemarksIndicates the source of cold-junction compensation. Use this enumeration to get or set the value of ThermocoupleCjcSource.MembersNameValueDescriptionBuiltIn10200Use

### AIThermocoupleCjcSource Enumeration

Indicates the source of [cold-junction compensation](/csh?context=nidaqmx_measfunds_sigcontherm).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIThermocoupleCjcSource

#### Remarks

Indicates the source of [cold-junction compensation](/csh?context=nidaqmx_measfunds_sigcontherm). Use this enumeration to get or set the value of [ThermocoupleCjcSource](nationalinstruments-daqmx-aichannel-thermocouplecjcsource.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| BuiltIn | 10200 | Use a cold-junction compensation channel built into the terminal block. |
| ConstantValue | 10116 | You must specify the cold-junction temperature. |
| Channel | 10113 | Use a channel for cold-junction compensation. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aithermocouplescaletype.html language=enus -->
## TOPIC 00427: AIThermocoupleScaleType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aithermocouplescaletype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aithermocouplescaletype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method or equation form that the thermocouple scale uses. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIThermocoupleScaleTypeRemarksSpecifies the method or equation form that the thermocouple scale uses. Use this enumeration to get or set the value of ThermocoupleScaleType.Me

### AIThermocoupleScaleType Enumeration

Specifies the method or equation form that the thermocouple scale uses.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIThermocoupleScaleType

#### Remarks

Specifies the method or equation form that the thermocouple scale uses. Use this enumeration to get or set the value of [ThermocoupleScaleType](nationalinstruments-daqmx-aichannel-thermocouplescaletype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Polynomial | 10449 | Scale values by using an Nth order polynomial equation. |
| Table | 10450 | Map an array of prescaled values to an array of corresponding scaled values, with all other values scaled proportionally. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aithermocoupletype.html language=enus -->
## TOPIC 00428: AIThermocoupleType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aithermocoupletype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aithermocoupletype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of thermocouple connected to the channel. Thermocouple types differ in composition and measurement range. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIThermocoupleTypeRemarksSpecifies the type of thermocouple connected to the channel. Thermocouple types differ in compos

### AIThermocoupleType Enumeration

Specifies the [type](/csh?context=nidaqmx_measfunds_thermocouples) of thermocouple connected to the channel. Thermocouple types differ in composition and measurement range.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIThermocoupleType

#### Remarks

Specifies the [type](/csh?context=nidaqmx_measfunds_thermocouples) of thermocouple connected to the channel. Thermocouple types differ in composition and measurement range. Use this enumeration to get or set the value of [ThermocoupleType](nationalinstruments-daqmx-aichannel-thermocoupletype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| J | 10072 | J-type thermocouple. |
| K | 10073 | K-type thermocouple. |
| N | 10077 | N-type thermocouple. |
| R | 10082 | R-type thermocouple. |
| S | 10085 | S-type thermocouple. |
| T | 10086 | T-type thermocouple. |
| B | 10047 | B-type thermocouple. |
| E | 10055 | E-type thermocouple. |
| A | 16208 | E-type thermocouple. |
| C | 16209 | E-type thermocouple. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aitorqueunits.html language=enus -->
## TOPIC 00429: AITorqueUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aitorqueunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aitorqueunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in which unit to return torque measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AITorqueUnitsRemarksSpecifies in which unit to return torque measurements from the channel. Use this enumeration to get or set the value of TorqueUnits.MembersNameValueDescri

### AITorqueUnits Enumeration

Specifies in which unit to return torque measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AITorqueUnits

#### Remarks

Specifies in which unit to return torque measurements from the channel. Use this enumeration to get or set the value of [TorqueUnits](nationalinstruments-daqmx-aichannel-torqueunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| NewtonMeters | 15881 | Newton meters. |
| InchOunces | 15882 | Ounce-inches. |
| InchPounds | 15883 | Pound-inches. |
| FootPounds | 15884 | Pound-feet. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiunscaledpowermeasurement-aiunscaledpowermeasurement__short-short.html language=enus -->
## TOPIC 00430: AIUnscaledPowerMeasurement(short, short)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiunscaledpowermeasurement-aiunscaledpowermeasurement__short-short.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiunscaledpowermeasurement-aiunscaledpowermeasurement__short-short.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the AIUnscaledPowerMeasurement object with the specified initial values. SyntaxNamespace: NationalInstruments.DAQmxpublic AIUnscaledPowerMeasurement(short voltage, short current)ParametersNameTypeDescriptionvoltageshortThe voltage component of the power measurement.curr

### AIUnscaledPowerMeasurement(short, short)

Initializes a new instance of the [AIUnscaledPowerMeasurement](nationalinstruments-daqmx-aiunscaledpowermeasurement.html) object with the specified initial values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AIUnscaledPowerMeasurement(short voltage, short current)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| voltage | short | The voltage component of the power measurement. |
| current | short | The current component of the power measurement. |

Parent topic:

AIUnscaledPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiunscaledpowermeasurement-current.html language=enus -->
## TOPIC 00431: Current

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiunscaledpowermeasurement-current.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiunscaledpowermeasurement-current.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the current component of the power measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic short Current { get; set; }RemarksThe current value in amperes.

### Current

Gets or sets the current component of the power measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public short Current { get; set; }

#### Remarks

The current value in amperes.

Parent topic:

AIUnscaledPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiunscaledpowermeasurement-equals__aiunscaledpowermeasurement-aiunscaledpowermeasurement.html language=enus -->
## TOPIC 00432: Equals(AIUnscaledPowerMeasurement, AIUnscaledPowerMeasurement)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiunscaledpowermeasurement-equals__aiunscaledpowermeasurement-aiunscaledpowermeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiunscaledpowermeasurement-equals__aiunscaledpowermeasurement-aiunscaledpowermeasurement.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a value indicating if two specified instances of AIUnscaledPowerMeasurement are equal. SyntaxNamespace: NationalInstruments.DAQmxpublic static bool Equals(AIUnscaledPowerMeasurement obj1, AIUnscaledPowerMeasurement obj2)ParametersNameTypeDescriptionobj1AIUnscaledPowerMeasurementA AIUnscaledP

### Equals(AIUnscaledPowerMeasurement, AIUnscaledPowerMeasurement)

Returns a value indicating if two specified instances of [AIUnscaledPowerMeasurement](nationalinstruments-daqmx-aiunscaledpowermeasurement.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public static bool Equals(AIUnscaledPowerMeasurement obj1, AIUnscaledPowerMeasurement obj2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj1 | AIUnscaledPowerMeasurement | A AIUnscaledPowerMeasurement object. |
| obj2 | AIUnscaledPowerMeasurement | A AIUnscaledPowerMeasurement object. |

#### Returns

true if *obj1*  and *obj2*  are equal.

Parent topic:

AIUnscaledPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiunscaledpowermeasurement-equals__aiunscaledpowermeasurement.html language=enus -->
## TOPIC 00433: Equals(AIUnscaledPowerMeasurement)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiunscaledpowermeasurement-equals__aiunscaledpowermeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiunscaledpowermeasurement-equals__aiunscaledpowermeasurement.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a value indicating if this instance is equal to the specified AIUnscaledPowerMeasurement object. SyntaxNamespace: NationalInstruments.DAQmxpublic bool Equals(AIUnscaledPowerMeasurement obj)ParametersNameTypeDescriptionobjAIUnscaledPowerMeasurementA AIUnscaledPowerMeasurement object to compar

### Equals(AIUnscaledPowerMeasurement)

Returns a value indicating if this instance is equal to the specified [AIUnscaledPowerMeasurement](nationalinstruments-daqmx-aiunscaledpowermeasurement.html) object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool Equals(AIUnscaledPowerMeasurement obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | AIUnscaledPowerMeasurement | A AIUnscaledPowerMeasurement object to compare with this instance. |

#### Returns

true if *obj*  has the same low ticks and high ticks as this instance.

Parent topic:

AIUnscaledPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiunscaledpowermeasurement-equals__object.html language=enus -->
## TOPIC 00434: Equals(object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiunscaledpowermeasurement-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiunscaledpowermeasurement-equals__object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a value indicating if this instance is equal to the specified object. SyntaxNamespace: NationalInstruments.DAQmxpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectAn object to compare with this instance.Returnstrue if obj is a AIUnscaledPowerMeasurement object that

### Equals(object)

Returns a value indicating if this instance is equal to the specified object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | An object to compare with this instance. |

#### Returns

true if *obj*  is a [AIUnscaledPowerMeasurement](nationalinstruments-daqmx-aiunscaledpowermeasurement.html) object that has the same low ticks and high ticks as this instance.

Parent topic:

AIUnscaledPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiunscaledpowermeasurement-gethashcode.html language=enus -->
## TOPIC 00435: GetHashCode()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiunscaledpowermeasurement-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiunscaledpowermeasurement-gethashcode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a hash code for the AIUnscaledPowerMeasurement object. SyntaxNamespace: NationalInstruments.DAQmxpublic override int GetHashCode()RemarksTwo AIUnscaledPowerMeasurement objects might have the same hash code even though they represent different values. ReturnsA 32-bit signed integer hash code.

### GetHashCode()

Returns a hash code for the [AIUnscaledPowerMeasurement](nationalinstruments-daqmx-aiunscaledpowermeasurement.html) object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override int GetHashCode()

#### Remarks

Two [AIUnscaledPowerMeasurement](nationalinstruments-daqmx-aiunscaledpowermeasurement.html) objects might have the same hash code even though they represent different values.

#### Returns

A 32-bit signed integer hash code.

Parent topic:

AIUnscaledPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiunscaledpowermeasurement-getobjectdata__serializationinfo-streamingcontext.html language=enus -->
## TOPIC 00436: GetObjectData(SerializationInfo, StreamingContext)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiunscaledpowermeasurement-getobjectdata__serializationinfo-streamingcontext.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiunscaledpowermeasurement-getobjectdata__serializationinfo-streamingcontext.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the SerializationInfo object with information about the exception. SyntaxNamespace: NationalInstruments.DAQmxpublic void GetObjectData(SerializationInfo info, StreamingContext context)ParametersNameTypeDescriptioninfoSerializationInfoObject that holds the serialized object data.contextStreaming

### GetObjectData(SerializationInfo, StreamingContext)

Sets the SerializationInfo object with information about the exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void GetObjectData(SerializationInfo info, StreamingContext context)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| info | SerializationInfo | Object that holds the serialized object data. |
| context | StreamingContext | Contextual information about the source or destination. |

Parent topic:

AIUnscaledPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiunscaledpowermeasurement-operator_eq__aiunscaledpowermeasurement-aiunscaledpowermeasurement.html language=enus -->
## TOPIC 00437: operator==(AIUnscaledPowerMeasurement, AIUnscaledPowerMeasurement)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiunscaledpowermeasurement-operator_eq__aiunscaledpowermeasurement-aiunscaledpowermeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiunscaledpowermeasurement-operator_eq__aiunscaledpowermeasurement-aiunscaledpowermeasurement.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns true if two AIUnscaledPowerMeasurement objects are equal. SyntaxNamespace: NationalInstruments.DAQmxpublic static bool operator==(AIUnscaledPowerMeasurement obj1, AIUnscaledPowerMeasurement obj2)ParametersNameTypeDescriptionobj1AIUnscaledPowerMeasurementA AIUnscaledPowerMeasurement object.ob

### operator==(AIUnscaledPowerMeasurement, AIUnscaledPowerMeasurement)

Returns true if two [AIUnscaledPowerMeasurement](nationalinstruments-daqmx-aiunscaledpowermeasurement.html) objects are equal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public static bool operator==(AIUnscaledPowerMeasurement obj1, AIUnscaledPowerMeasurement obj2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj1 | AIUnscaledPowerMeasurement | A AIUnscaledPowerMeasurement object. |
| obj2 | AIUnscaledPowerMeasurement | A AIUnscaledPowerMeasurement object. |

#### Returns

true if the values of *obj1*  and *obj2*  are equal.

Parent topic:

AIUnscaledPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiunscaledpowermeasurement-operator_neq__aiunscaledpowermeasurement-aiunscaledpowermeasurement.html language=enus -->
## TOPIC 00438: operator!=(AIUnscaledPowerMeasurement, AIUnscaledPowerMeasurement)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiunscaledpowermeasurement-operator_neq__aiunscaledpowermeasurement-aiunscaledpowermeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiunscaledpowermeasurement-operator_neq__aiunscaledpowermeasurement-aiunscaledpowermeasurement.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns true if two AIUnscaledPowerMeasurement objects are not equal. SyntaxNamespace: NationalInstruments.DAQmxpublic static bool operator!=(AIUnscaledPowerMeasurement obj1, AIUnscaledPowerMeasurement obj2)ParametersNameTypeDescriptionobj1AIUnscaledPowerMeasurementA AIUnscaledPowerMeasurement objec

### operator!=(AIUnscaledPowerMeasurement, AIUnscaledPowerMeasurement)

Returns true if two [AIUnscaledPowerMeasurement](nationalinstruments-daqmx-aiunscaledpowermeasurement.html) objects are not equal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public static bool operator!=(AIUnscaledPowerMeasurement obj1, AIUnscaledPowerMeasurement obj2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj1 | AIUnscaledPowerMeasurement | A AIUnscaledPowerMeasurement object. |
| obj2 | AIUnscaledPowerMeasurement | A AIUnscaledPowerMeasurement object. |

#### Returns

true if the values of *obj1*  and *obj2*  are not equal.

Parent topic:

AIUnscaledPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiunscaledpowermeasurement-voltage.html language=enus -->
## TOPIC 00439: Voltage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiunscaledpowermeasurement-voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiunscaledpowermeasurement-voltage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the voltage component of the power measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic short Voltage { get; set; }RemarksThe voltage value in volts.

### Voltage

Gets or sets the voltage component of the power measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public short Voltage { get; set; }

#### Remarks

The voltage value in volts.

Parent topic:

AIUnscaledPowerMeasurement Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiunscaledpowermeasurement.html language=enus -->
## TOPIC 00440: AIUnscaledPowerMeasurement Data Structure

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiunscaledpowermeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiunscaledpowermeasurement.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates a power measurement specified in terms of voltage and current. Derives fromISerializableSyntaxNamespace: NationalInstruments.DAQmxpublic struct AIUnscaledPowerMeasurement : ISerializableThread SafetyAny members of this type are not guaranteed to be thread safe.ConstructorsNameDescriptio

### AIUnscaledPowerMeasurement Data Structure

Encapsulates a power measurement specified in terms of voltage and current.

#### Derives from

- ISerializable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public struct AIUnscaledPowerMeasurement : ISerializable

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| AIUnscaledPowerMeasurement(short, short) | Initializes a new instance of the AIUnscaledPowerMeasurement object with the specified initial values. |

#### Properties

| Name | Description |
| --- | --- |
| Current | Gets or sets the current component of the power measurement. |
| Voltage | Gets or sets the voltage component of the power measurement. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(object) | Returns a value indicating if this instance is equal to the specified object. |
| Equals(AIUnscaledPowerMeasurement) | Returns a value indicating if this instance is equal to the specified AIUnscaledPowerMeasurement object. |
| GetHashCode() | Returns a hash code for the AIUnscaledPowerMeasurement object. |
| GetObjectData(SerializationInfo, StreamingContext) | Sets the SerializationInfo object with information about the exception. |
| Equals(AIUnscaledPowerMeasurement, AIUnscaledPowerMeasurement) | Returns a value indicating if two specified instances of AIUnscaledPowerMeasurement are equal. |

#### Operators

| Name | Description |
| --- | --- |
| operator!=(AIUnscaledPowerMeasurement, AIUnscaledPowerMeasurement) | Returns true if two AIUnscaledPowerMeasurement objects are not equal. |
| operator==(AIUnscaledPowerMeasurement, AIUnscaledPowerMeasurement) | Returns true if two AIUnscaledPowerMeasurement objects are equal. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aivelocityiepesensorsensitivityunits.html language=enus -->
## TOPIC 00441: AIVelocityIepeSensorSensitivityUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aivelocityiepesensorsensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aivelocityiepesensorsensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units for VelocityIepeSensorSensitivity. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIVelocityIepeSensorSensitivityUnitsRemarksSpecifies the units for VelocityIepeSensorSensitivity. Use this enumeration to get or set the value of VelocityIepeSensorSensitivityUnits.MembersNam

### AIVelocityIepeSensorSensitivityUnits Enumeration

Specifies the units for [VelocityIepeSensorSensitivity](nationalinstruments-daqmx-aichannel-velocityiepesensorsensitivity.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIVelocityIepeSensorSensitivityUnits

#### Remarks

Specifies the units for [VelocityIepeSensorSensitivity](nationalinstruments-daqmx-aichannel-velocityiepesensorsensitivity.html). Use this enumeration to get or set the value of [VelocityIepeSensorSensitivityUnits](nationalinstruments-daqmx-aichannel-velocityiepesensorsensitivityunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| MillivoltsPerMillimeterPerSecond | 15963 | Millivolts per millimeter per second. |
| MillivoltsPerInchPerSecond | 15964 | Millivolts per inch per second. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aivelocityunits.html language=enus -->
## TOPIC 00442: AIVelocityUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aivelocityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aivelocityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in which unit to return velocity measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIVelocityUnitsRemarksSpecifies in which unit to return velocity measurements from the channel. Use this enumeration to get or set the value of VelocityUnits.MembersNameVal

### AIVelocityUnits Enumeration

Specifies in which unit to return velocity measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIVelocityUnits

#### Remarks

Specifies in which unit to return velocity measurements from the channel. Use this enumeration to get or set the value of [VelocityUnits](nationalinstruments-daqmx-aichannel-velocityunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| MetersPerSecond | 15959 | Meters per second. |
| InchesPerSecond | 15960 | Inches per second. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aivoltageacrmsunits.html language=enus -->
## TOPIC 00443: AIVoltageAcrmsUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aivoltageacrmsunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aivoltageacrmsunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return voltage RMS measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIVoltageAcrmsUnitsRemarksSpecifies the units to use to return voltage RMS measurements from the channel. Use this enumeration to get or set the value of VoltageAcrms

### AIVoltageAcrmsUnits Enumeration

Specifies the units to use to return voltage RMS measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIVoltageAcrmsUnits

#### Remarks

Specifies the units to use to return voltage RMS measurements from the channel. Use this enumeration to get or set the value of [VoltageAcrmsUnits](nationalinstruments-daqmx-aichannel-voltageacrmsunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Volts | 10348 | Volts. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |
| FromTeds | 12516 | Units defined by TEDS information associated with the channel. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aivoltageunits.html language=enus -->
## TOPIC 00444: AIVoltageUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aivoltageunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aivoltageunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return voltage measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIVoltageUnitsRemarksSpecifies the units to use to return voltage measurements from the channel. Use this enumeration to get or set the value of VoltageUnits.MembersNameV

### AIVoltageUnits Enumeration

Specifies the units to use to return voltage measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIVoltageUnits

#### Remarks

Specifies the units to use to return voltage measurements from the channel. Use this enumeration to get or set the value of [VoltageUnits](nationalinstruments-daqmx-aichannel-voltageunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Volts | 10348 | Volts. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |
| FromTeds | 12516 | Units defined by TEDS information associated with the channel. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgepausetriggercoupling.html language=enus -->
## TOPIC 00445: AnalogEdgePauseTriggerCoupling Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgepausetriggercoupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgepausetriggercoupling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AnalogEdgePauseTriggerCouplingRemarksSpecifies the coupling for the source signal of the trigger if the source is a terminal ra

### AnalogEdgePauseTriggerCoupling Enumeration

Specifies the coupling for the source signal of the trigger if the source is a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AnalogEdgePauseTriggerCoupling

#### Remarks

Specifies the coupling for the source signal of the trigger if the source is a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans). Use this enumeration to get or set the value of [Coupling](nationalinstruments-daqmx-analoglevelpausetrigger-coupling.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AC | 10045 | Alternating Current. |
| DC | 10050 | Direct Current. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgereferencetrigger-coupling.html language=enus -->
## TOPIC 00446: Coupling

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgereferencetrigger-coupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgereferencetrigger-coupling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogEdgeReferenceTriggerCoupling Coupling { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx

### Coupling

Specifies the coupling for the source signal of the trigger if the source is a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogEdgeReferenceTriggerCoupling](nationalinstruments-daqmx-analogedgereferencetriggercoupling.html) Coupling { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgereferencetrigger-digitalfilterenable.html language=enus -->
## TOPIC 00447: DigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgereferencetrigger-digitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgereferencetrigger-digitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals

### DigitalFilterEnable

Specifies whether to apply a digital [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the hysteresis window rapidly.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgereferencetrigger-digitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00448: DigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgereferencetrigger-digitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgereferencetrigger-digitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width thefilter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the[filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgereferencetrigger-digitalfiltertimebaserate.html language=enus -->
## TOPIC 00449: DigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgereferencetrigger-digitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgereferencetrigger-digitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver r

### DigitalFilterTimebaseRate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgereferencetrigger-digitalfiltertimebasesource.html language=enus -->
## TOPIC 00450: DigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgereferencetrigger-digitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgereferencetrigger-digitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string DigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterTimebaseSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgereferencetrigger-digitalsynchronizationenable.html language=enus -->
## TOPIC 00451: DigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgereferencetrigger-digitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgereferencetrigger-digitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalSynchronizationEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returne

### DigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalSynchronizationEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgereferencetrigger-hysteresis.html language=enus -->
## TOPIC 00452: Hysteresis

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgereferencetrigger-hysteresis.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgereferencetrigger-hysteresis.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a hysteresis level in the units of the measurement. If Slope is Rising, the trigger does not deassert until the source signal passes below Level minus the hysteresis. If Slope is Falling, the trigger does not deassert until the source signal passes above Level plus the hysteresis. Hysteres

### Hysteresis

Specifies a [hysteresis level](/csh?context=nidaqmx_mxcncpts_analogtriggering) in the units of the measurement. If [Slope](nationalinstruments-daqmx-analogedgereferencetrigger-slope.html) is [Rising](nationalinstruments-daqmx-analogedgereferencetriggerslope.html), the trigger does not deassert until the source signal passes below [Level](nationalinstruments-daqmx-analogedgereferencetrigger-level.html) minus the hysteresis. If [Slope](nationalinstruments-daqmx-analogedgereferencetrigger-slope.html) is [Falling](nationalinstruments-daqmx-analogedgereferencetriggerslope.html), the trigger does not deassert until the source signal passes above [Level](nationalinstruments-daqmx-analogedgereferencetrigger-level.html) plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Hysteresis { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgereferencetrigger-level.html language=enus -->
## TOPIC 00453: Level

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgereferencetrigger-level.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgereferencetrigger-level.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in the units of the measurement the threshold at which the Reference Trigger occurs. Use Slope to specify on which slope to trigger at this threshold. SyntaxNamespace: NationalInstruments.DAQmxpublic double Level { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionT

### Level

Specifies in the units of the measurement the threshold at which the [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger) occurs. Use [Slope](nationalinstruments-daqmx-analogedgereferencetrigger-slope.html) to specify on which slope to trigger at this threshold.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Level { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgereferencetrigger-slope.html language=enus -->
## TOPIC 00454: Slope

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgereferencetrigger-slope.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgereferencetrigger-slope.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which slope of the source signal the Reference Trigger occurs. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogEdgeReferenceTriggerSlope Slope { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Slope

Specifies on which slope of the source signal the [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger) occurs.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogEdgeReferenceTriggerSlope](nationalinstruments-daqmx-analogedgereferencetriggerslope.html) Slope { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgereferencetrigger-source.html language=enus -->
## TOPIC 00455: Source

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgereferencetrigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgereferencetrigger-source.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Reference Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic string Source { get; set; }RemarksFor E Series devices, if you use a channel name, the channel must be the only channel

### Source

Specifies the name of a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans) or [terminal](/csh?context=nidaqmx_mxcncpts_terminal) where there is an analog signal to use as the source of the [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Source { get; set; }

#### Remarks

For E Series devices, if you use a channel name, the channel must be the only channel in the task. The only terminal you can use for E Series devices is PFI0.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgereferencetrigger-tostring.html language=enus -->
## TOPIC 00456: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgereferencetrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgereferencetrigger-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgereferencetrigger.html language=enus -->
## TOPIC 00457: AnalogEdgeReferenceTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgereferencetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgereferencetrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties to configure analog edge reference triggers. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class AnalogEdgeReferenceTrigger : MarshalByRefObject, IFilteredTypeDescriptorRemarksExample applications are located in the <Public

### AnalogEdgeReferenceTrigger Class

Contains properties to configure [analog edge](/csh?context=nidaqmx_mxcncpts_analogtriggering) [reference triggers](/csh?context=nidaqmx_mxcncpts_referencetrigger).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AnalogEdgeReferenceTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Coupling | Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. |
| DigitalFilterEnable | Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the hysteresis window rapidly. |
| DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width thefilter recognizes. |
| DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
| DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
| DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
| Hysteresis | Specifies a hysteresis level in the units of the measurement. If Slope is Rising, the trigger does not deassert until the source signal passes below Level minus the hysteresis. If Slope is Falling, the trigger does not deassert until the source signal passes above Level plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. |
| Level | Specifies in the units of the measurement the threshold at which the Reference Trigger occurs. Use Slope to specify on which slope to trigger at this threshold. |
| Slope | Specifies on which slope of the source signal the Reference Trigger occurs. |
| Source | Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Reference Trigger. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- ReferenceTrigger
- AnalogEdge

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgereferencetriggercoupling.html language=enus -->
## TOPIC 00458: AnalogEdgeReferenceTriggerCoupling Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgereferencetriggercoupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgereferencetriggercoupling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AnalogEdgeReferenceTriggerCouplingRemarksSpecifies the coupling for the source signal of the trigger if the source is a termina

### AnalogEdgeReferenceTriggerCoupling Enumeration

Specifies the coupling for the source signal of the trigger if the source is a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AnalogEdgeReferenceTriggerCoupling

#### Remarks

Specifies the coupling for the source signal of the trigger if the source is a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans). Use this enumeration to get or set the value of [Coupling](nationalinstruments-daqmx-analogedgereferencetrigger-coupling.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AC | 10045 | Alternating Current. |
| DC | 10050 | Direct Current. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgereferencetriggerslope.html language=enus -->
## TOPIC 00459: AnalogEdgeReferenceTriggerSlope Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgereferencetriggerslope.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgereferencetriggerslope.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which slope of the source signal the Reference Trigger occurs. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AnalogEdgeReferenceTriggerSlopeRemarksSpecifies on which slope of the source signal the Reference Trigger occurs. Use this enumeration to get or set the value of Slope.Me

### AnalogEdgeReferenceTriggerSlope Enumeration

Specifies on which slope of the source signal the [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger) occurs.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AnalogEdgeReferenceTriggerSlope

#### Remarks

Specifies on which slope of the source signal the [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger) occurs. Use this enumeration to get or set the value of [Slope](nationalinstruments-daqmx-analogedgereferencetrigger-slope.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 10280 | Trigger on the rising slope of the signal. |
| Falling | 10171 | Trigger on the falling slope of the signal. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgestarttrigger-coupling.html language=enus -->
## TOPIC 00460: Coupling

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgestarttrigger-coupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgestarttrigger-coupling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogEdgeStartTriggerCoupling Coupling { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx dri

### Coupling

Specifies the coupling for the source signal of the trigger if the source is a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogEdgeStartTriggerCoupling](nationalinstruments-daqmx-analogedgestarttriggercoupling.html) Coupling { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgestarttrigger-digitalfilterenable.html language=enus -->
## TOPIC 00461: DigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgestarttrigger-digitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgestarttrigger-digitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals

### DigitalFilterEnable

Specifies whether to apply a digital [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the hysteresis window rapidly.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgestarttrigger-digitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00462: DigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgestarttrigger-digitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgestarttrigger-digitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgestarttrigger-digitalfiltertimebaserate.html language=enus -->
## TOPIC 00463: DigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgestarttrigger-digitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgestarttrigger-digitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver r

### DigitalFilterTimebaseRate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgestarttrigger-digitalfiltertimebasesource.html language=enus -->
## TOPIC 00464: DigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgestarttrigger-digitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgestarttrigger-digitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string DigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterTimebaseSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgestarttrigger-digitalsynchronizationenable.html language=enus -->
## TOPIC 00465: DigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgestarttrigger-digitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgestarttrigger-digitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalSynchronizationEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returne

### DigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalSynchronizationEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgestarttrigger-hysteresis.html language=enus -->
## TOPIC 00466: Hysteresis

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgestarttrigger-hysteresis.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgestarttrigger-hysteresis.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a hysteresis level in the units of the measurement or generation. If Slope is Rising, the trigger does not deassert until the source signal passes below Level minus the hysteresis. If Slope is Falling, the trigger does not deassert until the source signal passes above Level plus the hyster

### Hysteresis

Specifies a [hysteresis level](/csh?context=nidaqmx_mxcncpts_analogtriggering) in the units of the measurement or generation. If [Slope](nationalinstruments-daqmx-analogedgestarttrigger-slope.html) is [Rising](nationalinstruments-daqmx-analogedgestarttriggerslope.html), the trigger does not deassert until the source signal passes below [Level](nationalinstruments-daqmx-analogedgestarttrigger-level.html) minus the hysteresis. If [Slope](nationalinstruments-daqmx-analogedgestarttrigger-slope.html) is [Falling](nationalinstruments-daqmx-analogedgestarttriggerslope.html), the trigger does not deassert until the source signal passes above [Level](nationalinstruments-daqmx-analogedgestarttrigger-level.html) plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Hysteresis { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgestarttrigger-level.html language=enus -->
## TOPIC 00467: Level

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgestarttrigger-level.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgestarttrigger-level.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies at what threshold in the units of the measurement or generation to start acquiring or generating samples. Use Slope to specify on which slope to trigger on this threshold. SyntaxNamespace: NationalInstruments.DAQmxpublic double Level { get; set; }ExceptionsTypeDescriptionNationalInstrument

### Level

Specifies at what threshold in the units of the measurement or generation to start acquiring or generating samples. Use [Slope](nationalinstruments-daqmx-analogedgestarttrigger-slope.html) to specify on which slope to trigger on this threshold.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Level { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgestarttrigger-slope.html language=enus -->
## TOPIC 00468: Slope

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgestarttrigger-slope.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgestarttrigger-slope.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which slope of the trigger signal to start acquiring or generating samples. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogEdgeStartTriggerSlope Slope { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Slope

Specifies on which slope of the trigger signal to start acquiring or generating samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogEdgeStartTriggerSlope](nationalinstruments-daqmx-analogedgestarttriggerslope.html) Slope { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgestarttrigger-source.html language=enus -->
## TOPIC 00469: Source

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgestarttrigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgestarttrigger-source.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Start Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic string Source { get; set; }RemarksFor E Series devices, if you use a channel name, the channel must be the first one in the

### Source

Specifies the name of a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans) or [terminal](/csh?context=nidaqmx_mxcncpts_terminal) where there is an analog signal to use as the [source](/csh?context=nidaqmx_mxdevconsid_analogtrig) of the Start Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Source { get; set; }

#### Remarks

For E Series devices, if you use a channel name, the channel must be the first one in the task. The only terminal you can use for E Series devices is PFI0.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgestarttrigger-tostring.html language=enus -->
## TOPIC 00470: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgestarttrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgestarttrigger-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgestarttrigger.html language=enus -->
## TOPIC 00471: AnalogEdgeStartTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgestarttrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgestarttrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties to configure analog edge start triggers. For more information, refer to StartTrigger. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class AnalogEdgeStartTrigger : MarshalByRefObject, IFilteredTypeDescriptorRemarksExample app

### AnalogEdgeStartTrigger Class

Contains properties to configure [analog edge](/csh?context=nidaqmx_mxcncpts_analogtriggering) [start triggers](/csh?context=nidaqmx_mxcncpts_starttrig). For more information, refer to [StartTrigger](nationalinstruments-daqmx-starttrigger.html).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AnalogEdgeStartTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Coupling | Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. |
| DigitalFilterEnable | Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the hysteresis window rapidly. |
| DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
| DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
| DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
| DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
| Hysteresis | Specifies a hysteresis level in the units of the measurement or generation. If Slope is Rising, the trigger does not deassert until the source signal passes below Level minus the hysteresis. If Slope is Falling, the trigger does not deassert until the source signal passes above Level plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. |
| Level | Specifies at what threshold in the units of the measurement or generation to start acquiring or generating samples. Use Slope to specify on which slope to trigger on this threshold. |
| Slope | Specifies on which slope of the trigger signal to start acquiring or generating samples. |
| Source | Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Start Trigger. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- StartTrigger
- AnalogEdge

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgestarttriggercoupling.html language=enus -->
## TOPIC 00472: AnalogEdgeStartTriggerCoupling Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgestarttriggercoupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgestarttriggercoupling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AnalogEdgeStartTriggerCouplingRemarksSpecifies the coupling for the source signal of the trigger if the source is a terminal ra

### AnalogEdgeStartTriggerCoupling Enumeration

Specifies the coupling for the source signal of the trigger if the source is a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AnalogEdgeStartTriggerCoupling

#### Remarks

Specifies the coupling for the source signal of the trigger if the source is a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans). Use this enumeration to get or set the value of [Coupling](nationalinstruments-daqmx-analogedgestarttrigger-coupling.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AC | 10045 | Alternating Current. |
| DC | 10050 | Direct Current. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogedgestarttriggerslope.html language=enus -->
## TOPIC 00473: AnalogEdgeStartTriggerSlope Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogedgestarttriggerslope.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogedgestarttriggerslope.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which slope of the trigger signal to start acquiring or generating samples. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AnalogEdgeStartTriggerSlopeRemarksSpecifies on which slope of the trigger signal to start acquiring or generating samples. Use this enumeration to get or set

### AnalogEdgeStartTriggerSlope Enumeration

Specifies on which slope of the trigger signal to start acquiring or generating samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AnalogEdgeStartTriggerSlope

#### Remarks

Specifies on which slope of the trigger signal to start acquiring or generating samples. Use this enumeration to get or set the value of [Slope](nationalinstruments-daqmx-analogedgestarttrigger-slope.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 10280 | Trigger on the rising slope of the signal. |
| Falling | 10171 | Trigger on the falling slope of the signal. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analoglevelpausetrigger-condition.html language=enus -->
## TOPIC 00474: Condition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analoglevelpausetrigger-condition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analoglevelpausetrigger-condition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the task pauses above or below the threshold you specify with Level. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogLevelPauseTriggerCondition Condition { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Condition

Specifies whether the task pauses above or below the threshold you specify with [Level](nationalinstruments-daqmx-analoglevelpausetrigger-level.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogLevelPauseTriggerCondition](nationalinstruments-daqmx-analoglevelpausetriggercondition.html) Condition { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analoglevelpausetrigger-coupling.html language=enus -->
## TOPIC 00475: Coupling

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analoglevelpausetrigger-coupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analoglevelpausetrigger-coupling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogEdgePauseTriggerCoupling Coupling { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx dri

### Coupling

Specifies the coupling for the source signal of the trigger if the source is a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) rather than a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogEdgePauseTriggerCoupling](nationalinstruments-daqmx-analogedgepausetriggercoupling.html) Coupling { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analoglevelpausetrigger-digitalfilterenable.html language=enus -->
## TOPIC 00476: DigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analoglevelpausetrigger-digitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analoglevelpausetrigger-digitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals

### DigitalFilterEnable

Specifies whether to apply a digital [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the hysteresis window rapidly.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analoglevelpausetrigger-digitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00477: DigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analoglevelpausetrigger-digitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analoglevelpausetrigger-digitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analoglevelpausetrigger-digitalfiltertimebaserate.html language=enus -->
## TOPIC 00478: DigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analoglevelpausetrigger-digitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analoglevelpausetrigger-digitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver r

### DigitalFilterTimebaseRate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analoglevelpausetrigger-digitalfiltertimebasesource.html language=enus -->
## TOPIC 00479: DigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analoglevelpausetrigger-digitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analoglevelpausetrigger-digitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string DigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterTimebaseSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analoglevelpausetrigger-digitalsynchronizationenable.html language=enus -->
## TOPIC 00480: DigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analoglevelpausetrigger-digitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analoglevelpausetrigger-digitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalSynchronizationEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returne

### DigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalSynchronizationEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analoglevelpausetrigger-hysteresis.html language=enus -->
## TOPIC 00481: Hysteresis

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analoglevelpausetrigger-hysteresis.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analoglevelpausetrigger-hysteresis.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a hysteresis level in the units of the measurement or generation. If Condition is AboveLevel, the trigger does not deassert until the source signal passes below Level minus the hysteresis. If Condition is BelowLevel, the trigger does not deassert until the source signal passes above Level

### Hysteresis

Specifies a [hysteresis level](/csh?context=nidaqmx_mxcncpts_analogtriggering) in the units of the measurement or generation. If [Condition](nationalinstruments-daqmx-analoglevelpausetrigger-condition.html) is [AboveLevel](nationalinstruments-daqmx-analoglevelpausetriggercondition.html), the trigger does not deassert until the source signal passes below [Level](nationalinstruments-daqmx-analoglevelpausetrigger-level.html) minus the hysteresis. If [Condition](nationalinstruments-daqmx-analoglevelpausetrigger-condition.html) is [BelowLevel](nationalinstruments-daqmx-analoglevelpausetriggercondition.html), the trigger does not deassert until the source signal passes above [Level](nationalinstruments-daqmx-analoglevelpausetrigger-level.html) plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Hysteresis { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analoglevelpausetrigger-level.html language=enus -->
## TOPIC 00482: Level

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analoglevelpausetrigger-level.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analoglevelpausetrigger-level.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the threshold at which to pause the task. Specify this value in the units of the measurement or generation. Use Condition to specify whether the task pauses above or below this threshold. SyntaxNamespace: NationalInstruments.DAQmxpublic double Level { get; set; }ExceptionsTypeDescriptionNa

### Level

Specifies the threshold at which to pause the task. Specify this value in the units of the measurement or generation. Use [Condition](nationalinstruments-daqmx-analoglevelpausetrigger-condition.html) to specify whether the task pauses above or below this threshold.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Level { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analoglevelpausetrigger-source.html language=enus -->
## TOPIC 00483: Source

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analoglevelpausetrigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analoglevelpausetrigger-source.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic string Source { get; set; }RemarksFor E Series devices, if you use a channel name, the channel must be the only channel in the tas

### Source

Specifies the name of a [virtual channel](/csh?context=nidaqmx_mxcncpts_chans) or [terminal](/csh?context=nidaqmx_mxcncpts_terminal) where there is an analog signal to use as the source of the trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Source { get; set; }

#### Remarks

For E Series devices, if you use a channel name, the channel must be the only channel in the task. The only terminal you can use for E Series devices is PFI0.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analoglevelpausetrigger-tostring.html language=enus -->
## TOPIC 00484: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analoglevelpausetrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analoglevelpausetrigger-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analoglevelpausetrigger.html language=enus -->
## TOPIC 00485: AnalogLevelPauseTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analoglevelpausetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analoglevelpausetrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties to configure analog level pause triggers. For more information, refer to PauseTrigger. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class AnalogLevelPauseTrigger : MarshalByRefObject, IFilteredTypeDescriptorRemarksExample a

### AnalogLevelPauseTrigger Class

Contains properties to configure [analog level](/csh?context=nidaqmx_mxcncpts_analogtriggering) [pause triggers](/csh?context=nidaqmx_mxcncpts_pausetrigger). For more information, refer to [PauseTrigger](nationalinstruments-daqmx-pausetrigger.html).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AnalogLevelPauseTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Condition | Specifies whether the task pauses above or below the threshold you specify with Level. |
| Coupling | Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. |
| DigitalFilterEnable | Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the hysteresis window rapidly. |
| DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
| DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
| DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
| DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
| Hysteresis | Specifies a hysteresis level in the units of the measurement or generation. If Condition is AboveLevel, the trigger does not deassert until the source signal passes below Level minus the hysteresis. If Condition is BelowLevel, the trigger does not deassert until the source signal passes above Level plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. |
| Level | Specifies the threshold at which to pause the task. Specify this value in the units of the measurement or generation. Use Condition to specify whether the task pauses above or below this threshold. |
| Source | Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- PauseTrigger
- AnalogLevel

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analoglevelpausetriggercondition.html language=enus -->
## TOPIC 00486: AnalogLevelPauseTriggerCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analoglevelpausetriggercondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analoglevelpausetriggercondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the task pauses above or below the threshold you specify with Level. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AnalogLevelPauseTriggerConditionRemarksSpecifies whether the task pauses above or below the threshold you specify with Level. Use this enumeration to get or se

### AnalogLevelPauseTriggerCondition Enumeration

Specifies whether the task pauses above or below the threshold you specify with [Level](nationalinstruments-daqmx-analoglevelpausetrigger-level.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AnalogLevelPauseTriggerCondition

#### Remarks

Specifies whether the task pauses above or below the threshold you specify with [Level](nationalinstruments-daqmx-analoglevelpausetrigger-level.html). Use this enumeration to get or set the value of [Condition](nationalinstruments-daqmx-analoglevelpausetrigger-condition.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AboveLevel | 10093 | Pause the measurement or generation while the signal is above the threshold. |
| BelowLevel | 10107 | Pause the measurement or generation while the signal is below the threshold. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-analogmultichannelreader__daqstream.html language=enus -->
## TOPIC 00487: AnalogMultiChannelReader(DaqStream)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-analogmultichannelreader__daqstream.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-analogmultichannelreader__daqstream.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of the AnalogMultiChannelReader class to read from the specified DaqStream. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogMultiChannelReader(DaqStream stream)RemarksEach Task object contains a Stream property that serves as the connection point for readers to access t

### AnalogMultiChannelReader(DaqStream)

Creates a new instance of the [AnalogMultiChannelReader](nationalinstruments-daqmx-analogmultichannelreader.html) class to read from the specified [DaqStream](nationalinstruments-daqmx-daqstream.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public AnalogMultiChannelReader(DaqStream stream)

#### Remarks

Each [Task](nationalinstruments-daqmx-task.html) object contains a [Stream](nationalinstruments-daqmx-task-stream.html) property that serves as the connection point for readers to access the samples generated by that task.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| stream | DaqStream | The DaqStream to read. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadmultisample__int-asynccallback-object-double_arr2-reallocationpolicy.html language=enus -->
## TOPIC 00488: BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadmultisample__int-asynccallback-object-double_arr2-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadmultisample__int-asynccallback-object-double_arr2-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more floating-point samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSample(int samplesPerChannel, AsyncCallback callback, object state, double[,] data, ReallocationP

### BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double, ReallocationPolicy)

Begins an asynchronous read of one or more floating-point samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSample(int samplesPerChannel, AsyncCallback callback, object state, double[,] data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSample(IAsyncResult, out int)](nationalinstruments-daqmx-analogmultichannelreader-endmemoryoptimizedreadmultisample__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specifynullif you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specifynullif you do not need to pass any additional information to the callback. |
| data | double | An initialized 2D array of floating-point samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadmultisample__int-asynccallback-object-double_arr2.html language=enus -->
## TOPIC 00489: BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadmultisample__int-asynccallback-object-double_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadmultisample__int-asynccallback-object-double_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more floating-point samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSample(int samplesPerChannel, AsyncCallback callback, object state, double[,] data)RemarksIf the

### BeginMemoryOptimizedReadMultiSample(int, AsyncCallback, object, double)

Begins an asynchronous read of one or more floating-point samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSample(int samplesPerChannel, AsyncCallback callback, object state, double[,] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSample(IAsyncResult, out int)](nationalinstruments-daqmx-analogmultichannelreader-endmemoryoptimizedreadmultisample__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStreamyou are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | double | An initialized 2D array of floating-point samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadmultisamplepower__int-asynccallback-object-aipowermeasurement_arr2-reallocationpolicy.html language=enus -->
## TOPIC 00490: BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadmultisamplepower__int-asynccallback-object-aipowermeasurement_arr2-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadmultisamplepower__int-asynccallback-object-aipowermeasurement_arr2-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more power samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePower(int samplesPerChannel, AsyncCallback callback, object state, AIPowerMeasurement[,] data, Reall

### BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement, ReallocationPolicy)

Begins an asynchronous read of one or more power samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePower(int samplesPerChannel, AsyncCallback callback, object state, AIPowerMeasurement[,] data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePower(IAsyncResult, out int)](nationalinstruments-daqmx-analogmultichannelreader-endmemoryoptimizedreadmultisamplepower__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specifynullif you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specifynullif you do not need to pass any additional information to the callback. |
| data | AIPowerMeasurement | An initialized 2D array of power samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadmultisamplepower__int-asynccallback-object-aipowermeasurement_arr2.html language=enus -->
## TOPIC 00491: BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadmultisamplepower__int-asynccallback-object-aipowermeasurement_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadmultisamplepower__int-asynccallback-object-aipowermeasurement_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more power samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePower(int samplesPerChannel, AsyncCallback callback, object state, AIPowerMeasurement[,] data)Remark

### BeginMemoryOptimizedReadMultiSamplePower(int, AsyncCallback, object, AIPowerMeasurement)

Begins an asynchronous read of one or more power samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePower(int samplesPerChannel, AsyncCallback callback, object state, AIPowerMeasurement[,] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePower(IAsyncResult, out int)](nationalinstruments-daqmx-analogmultichannelreader-endmemoryoptimizedreadmultisamplepower__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStreamyou are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | AIPowerMeasurement | An initialized 2D array of power samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadwaveform__int-asynccallback-object-analogwaveform_double__arr1-reallocationpolicy.html language=enus -->
## TOPIC 00492: BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform< double >[], ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadwaveform__int-asynccallback-object-analogwaveform_double__arr1-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadwaveform__int-asynccallback-object-analogwaveform_double__arr1-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more analog waveform samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadWaveform(int samplesPerChannel, AsyncCallback callback, object state, AnalogWaveform< double >[] data

### BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform< double >[], ReallocationPolicy)

Begins an asynchronous read of one or more analog waveform samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadWaveform(int samplesPerChannel, AsyncCallback callback, object state, AnalogWaveform< double >[] data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing AnalogWaveformTData objects and their corresponding memory to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with [BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform<double>[])](nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadwaveform__int-asynccallback-object-analogwaveform_double__arr1.html) , call [EndMemoryOptimizedReadWaveform(IAsyncResult)](nationalinstruments-daqmx-analogmultichannelreader-endmemoryoptimizedreadwaveform__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | AnalogWaveform< double >[] | An initialized 1D array of AnalogWaveformTData that contains the read data. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadwaveform__int-asynccallback-object-analogwaveform_double__arr1.html language=enus -->
## TOPIC 00493: BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform< double >[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadwaveform__int-asynccallback-object-analogwaveform_double__arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadwaveform__int-asynccallback-object-analogwaveform_double__arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more analog waveform samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadWaveform(int samplesPerChannel, AsyncCallback callback, object state, AnalogWaveform< double >[] data

### BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform< double >[])

Begins an asynchronous read of one or more analog waveform samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadWaveform(int samplesPerChannel, AsyncCallback callback, object state, AnalogWaveform< double >[] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing AnalogWaveformTData objects and their corresponding memory to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginMemoryOptimizedReadWaveform(int, AsyncCallback, object, AnalogWaveform<double>[]), call [EndMemoryOptimizedReadWaveform(IAsyncResult)](nationalinstruments-daqmx-analogmultichannelreader-endmemoryoptimizedreadwaveform__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | AnalogWaveform< double >[] | An initialized 1D array of AnalogWaveformTData that contains the read data. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadwaveform__timespan-asynccallback-object-analogwaveform_double__arr1-reallocationpolicy.html language=enus -->
## TOPIC 00494: BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, object, AnalogWaveform< double >[], ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadwaveform__timespan-asynccallback-object-analogwaveform_double__arr1-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadwaveform__timespan-asynccallback-object-analogwaveform_double__arr1-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous, memory-optimized read of one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration . SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadWaveform(TimeSpan duration, AsyncCallback callback, objec

### BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, object, AnalogWaveform< double >[], ReallocationPolicy)

Begins an asynchronous, memory-optimized read of one or more analog waveform samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task for a specified *duration* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadWaveform(TimeSpan duration, AsyncCallback callback, object state, AnalogWaveform< double >[] data, ReallocationPolicy policy)

#### Remarks

If the *data*  waveform is large enough to hold the number of samples requested, this overload attempts to reuse the existing AnalogWaveformTData object's memory to store acquired data. This results in more efficient memory allocation when performing subsequent reads with a continuous analog input task, if each subsequent read acquires the same or fewer number of samples.

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, object, AnalogWaveform<double>[], ReallocationPolicy), call [EndMemoryOptimizedReadWaveform(IAsyncResult)](nationalinstruments-daqmx-analogmultichannelreader-endmemoryoptimizedreadwaveform__iasyncresult.html), passing the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the [Stream](nationalinstruments-daqmx-task-stream.html) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| duration | TimeSpan | The duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | AnalogWaveform< double >[] | An initialized 1D array of AnalogWaveformTData that contains the read data. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadwaveform__timespan-asynccallback-object-analogwaveform_double__arr1.html language=enus -->
## TOPIC 00495: BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, object, AnalogWaveform< double >[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadwaveform__timespan-asynccallback-object-analogwaveform_double__arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-beginmemoryoptimizedreadwaveform__timespan-asynccallback-object-analogwaveform_double__arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous, memory-optimized read of one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration . SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadWaveform(TimeSpan duration, AsyncCallback callback, objec

### BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, object, AnalogWaveform< double >[])

Begins an asynchronous, memory-optimized read of one or more analog waveform samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task for a specified *duration* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadWaveform(TimeSpan duration, AsyncCallback callback, object state, AnalogWaveform< double >[] data)

#### Remarks

If the *data*  waveform is large enough to hold the number of samples requested, this overload attempts to reuse the existing AnalogWaveformTData object's memory to store acquired data. This results in more efficient memory allocation when performing subsequent reads with a continuous analog input task, if each subsequent read acquires the same or fewer number of samples.

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, object, AnalogWaveform<double>[]), call [EndMemoryOptimizedReadWaveform(IAsyncResult)](nationalinstruments-daqmx-analogmultichannelreader-endmemoryoptimizedreadwaveform__iasyncresult.html), passing the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the [Stream](nationalinstruments-daqmx-task-stream.html) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| duration | TimeSpan | The duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | AnalogWaveform< double >[] | An initialized 1D array of AnalogWaveformTData that contains the read data. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-beginreadmultisample__int-asynccallback-object.html language=enus -->
## TOPIC 00496: BeginReadMultiSample(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-beginreadmultisample__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-beginreadmultisample__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more floating-point samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSample(int samplesPerChannel, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions

### BeginReadMultiSample(int, AsyncCallback, object)

Begins an asynchronous read of one or more floating-point samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSample(int samplesPerChannel, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSample(int, AsyncCallback, object), call [EndReadMultiSample(IAsyncResult)](nationalinstruments-daqmx-analogmultichannelreader-endreadmultisample__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-beginreadmultisamplepower__int-asynccallback-object.html language=enus -->
## TOPIC 00497: BeginReadMultiSamplePower(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-beginreadmultisamplepower__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-beginreadmultisamplepower__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more power samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSamplePower(int samplesPerChannel, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions tha

### BeginReadMultiSamplePower(int, AsyncCallback, object)

Begins an asynchronous read of one or more power samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSamplePower(int samplesPerChannel, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePower(int, AsyncCallback, object), call [EndReadMultiSamplePower(IAsyncResult)](nationalinstruments-daqmx-analogmultichannelreader-endreadmultisamplepower__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-beginreadsinglesample__asynccallback-object.html language=enus -->
## TOPIC 00498: BeginReadSingleSample(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-beginreadsinglesample__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-beginreadsinglesample__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single floating-point sample from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSample(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an a

### BeginReadSingleSample(AsyncCallback, object)

Begins an asynchronous read of a single floating-point sample from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSample(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSample(AsyncCallback, object), call [EndReadSingleSample(IAsyncResult)](nationalinstruments-daqmx-analogmultichannelreader-endreadsinglesample__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-beginreadsinglesamplepower__asynccallback-object.html language=enus -->
## TOPIC 00499: BeginReadSingleSamplePower(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-beginreadsinglesamplepower__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-beginreadsinglesamplepower__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single power sample from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSamplePower(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an async

### BeginReadSingleSamplePower(AsyncCallback, object)

Begins an asynchronous read of a single power sample from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSamplePower(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePower(AsyncCallback, object), call [EndReadSingleSamplePower(IAsyncResult)](nationalinstruments-daqmx-analogmultichannelreader-endreadsinglesamplepower__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-analogmultichannelreader-beginreadwaveform__int-asynccallback-object.html language=enus -->
## TOPIC 00500: BeginReadWaveform(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-analogmultichannelreader-beginreadwaveform__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-analogmultichannelreader-beginreadwaveform__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more analog waveform samples from one or more AIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadWaveform(int samplesPerChannel, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions t

### BeginReadWaveform(int, AsyncCallback, object)

Begins an asynchronous read of one or more analog waveform samples from one or more [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadWaveform(int samplesPerChannel, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadWaveform(int, AsyncCallback, object), call [EndReadWaveform(IAsyncResult)](nationalinstruments-daqmx-analogmultichannelreader-endreadwaveform__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

AnalogMultiChannelReader Class
