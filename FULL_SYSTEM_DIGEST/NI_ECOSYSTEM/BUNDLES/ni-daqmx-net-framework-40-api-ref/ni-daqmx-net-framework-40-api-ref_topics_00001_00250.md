# NI DOCUMENT BUNDLE: ni-daqmx-net-framework-40-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-net-framework-40-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/events_t_nationalinstruments_daqmx_task.htm language=enus -->
## TOPIC 00001: Task Events

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/events_t_nationalinstruments_daqmx_task.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/events_t_nationalinstruments_daqmx_task.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task Events

### Task Events

The [Task](t_nationalinstruments_daqmx_task.htm) type exposes the following members.

##### Events

|  | Name | Description |
| --- | --- | --- |
|  | CounterOutput | Occurs when any of the counters used in the task reaches its terminal count. |
|  | DigitalChangeDetection | Occurs when a digital change is detected on any of the digital lines used in the task. |
|  | Done | Occurs when the task completes. |
|  | EveryNSamplesRead | Occurs when N number of samples per channel, as defined by EveryNSamplesReadEventInterval, is written from the device to the PC buffer. |
|  | EveryNSamplesWritten | Occurs when N number of samples per channel, as defined by EveryNSamplesWrittenEventInterval, have been written from the PC buffer to the device. |
|  | SampleClock | Occurs on each pulse of the task's sample clock. |
|  | SampleComplete | Occurs when each sample is acquired into the NI-DAQmx driver buffer and is ready for reading. |

Top

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannel_performstrainshuntcalibration.htm language=enus -->
## TOPIC 00002: AIChannelPerformStrainShuntCalibration Method (Double, ShuntElementLocation)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannel_performstrainshuntcalibration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannel_performstrainshuntcalibration.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.PerformStrainShuntCalibration Method (Double, ShuntElementLocation)

### AIChannelPerformStrainShuntCalibration Method (Double, ShuntElementLocation)

Performs shunt calibration for the virtual channels in the task using a strain gage sensor. An error will occur if not all virtual channels in the task support this operation.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void PerformStrainShuntCalibration(
	double shuntResistorValue,
	ShuntElementLocation shuntResistorLocation
)
```

```text
Public Sub PerformStrainShuntCalibration ( 
	shuntResistorValue As Double,
	shuntResistorLocation As ShuntElementLocation
)
```

###### Parameters

- **shuntResistorValue**
  - Type: SystemDoubleSpecifies the shunt resistance, in ohms.
- **shuntResistorLocation**
  - Type: NationalInstruments.DAQmxShuntElementLocationSpecifies the location of the shunt resistor.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

PerformStrainShuntCalibration Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannel_performthermocoupleleadoffsetnullingcalibration.htm language=enus -->
## TOPIC 00003: AIChannelPerformThermocoupleLeadOffsetNullingCalibration Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannel_performthermocoupleleadoffsetnullingcalibration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannel_performthermocoupleleadoffsetnullingcalibration.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.PerformThermocoupleLeadOffsetNullingCalibration Method

### AIChannelPerformThermocoupleLeadOffsetNullingCalibration Method

Performs thermocouple lead offset nulling calibration on the channels in the task to compensate for offsets introduced by open thermocouple detection. An error will occur if not all virtual channels in the task support this operation.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void PerformThermocoupleLeadOffsetNullingCalibration()
```

```text
Public Sub PerformThermocoupleLeadOffsetNullingCalibration
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Keep the measured temperature as constant as possible while performing this adjustment.

##### See Also

###### Reference

AIChannel Class

PerformThermocoupleLeadOffsetNullingCalibration Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannel_performthermocoupleleadoffsetnullingcalibration_1.htm language=enus -->
## TOPIC 00004: AIChannelPerformThermocoupleLeadOffsetNullingCalibration Method (Boolean)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannel_performthermocoupleleadoffsetnullingcalibration_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannel_performthermocoupleleadoffsetnullingcalibration_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.PerformThermocoupleLeadOffsetNullingCalibration Method (Boolean)

### AIChannelPerformThermocoupleLeadOffsetNullingCalibration Method (Boolean)

Performs thermocouple lead offset nulling calibration on the channels in the task to compensate for offsets introduced by open thermocouple detection. Use this method to specify whether or not to skip channels that do not support calibration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void PerformThermocoupleLeadOffsetNullingCalibration(
	bool skipUnsupportedChannels
)
```

```text
Public Sub PerformThermocoupleLeadOffsetNullingCalibration ( 
	skipUnsupportedChannels As Boolean
)
```

###### Parameters

- **skipUnsupportedChannels**
  - Type: SystemBooleanSpecifies whether or not to skip channels that do not support calibration. If skipUnsupportedChannels is , calibration will be performed only on supported virtual channels in the task. If , calibration will be performed on all virtual channels in the task, which may result in an error if not all channels support calibration.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Keep the measured temperature as constant as possible while performing this adjustment.

##### See Also

###### Reference

AIChannel Class

PerformThermocoupleLeadOffsetNullingCalibration Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createaccelerationchargechannel_1.htm language=enus -->
## TOPIC 00005: AIChannelCollectionCreateAccelerationChargeChannel Method (String, String, AITerminalConfiguration, Double, Double, String, Double, AIAccelerationChargeSensitivityUnits)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createaccelerationchargechannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createaccelerationchargechannel_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateAccelerationChargeChannel Method (String, String, AITerminalConfiguration, Double, Double, String, Double, AIAccelerationChargeSensitivityUnits)

### AIChannelCollectionCreateAccelerationChargeChannel Method (String, String, AITerminalConfiguration, Double, Double, String, Double, AIAccelerationChargeSensitivityUnits)

taskHandle

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateAccelerationChargeChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration terminalConfiguration,
	double minimumValue,
	double maximumValue,
	string customScaleName,
	double sensitivity,
	AIAccelerationChargeSensitivityUnits sensitivityUnits
)
```

```text
Public Function CreateAccelerationChargeChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	terminalConfiguration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	customScaleName As String,
	sensitivity As Double,
	sensitivityUnits As AIAccelerationChargeSensitivityUnits
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemString The names of the physical channels to use to create virtual channels. You can specify a list or range of physical channels.
- **nameToAssignChannel**
  - Type: SystemString The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignToChannel, you must use the names when you refer to these channels in other NI-DAQmx methods.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input TerminalConfigurationTypes for the channel.
- **minimumValue**
  - Type: SystemDouble The minimum value, in units, that you expect to measure.
- **maximumValue**
  - Type: SystemDouble The maximum value, in units, that you expect to measure.
- **customScaleName**
  - Type: SystemString The name of a custom scale to apply to the channel. To use this parameter, you must set units to FromCustomScale. If you do not set units to FromCustomScale, you must set customScaleName to .
- **sensitivity**
  - Type: SystemDouble The sensitivity of the sensor. This value is in the units you specify with the sensitivityUnits input. Refer to the sensor documentation to determine this value.
- **sensitivityUnits**
  - Type: NationalInstruments.DAQmxAIAccelerationChargeSensitivityUnits The units of sensitivity.

###### Return Value

AIChannel

##### See Also

###### Reference

AIChannelCollection Class

CreateAccelerationChargeChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createaccelerometerchannel.htm language=enus -->
## TOPIC 00006: AIChannelCollectionCreateAccelerometerChannel Method (String, String, AITerminalConfiguration, Double, Double, Double, AIAccelerometerSensitivityUnits, AIExcitationSource, Double, AIAccelerationUnits)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createaccelerometerchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createaccelerometerchannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateAccelerometerChannel Method (String, String, AITerminalConfiguration, Double, Double, Double, AIAccelerometerSensitivityUnits, AIExcitationSource, Double, AIAccelerationUnits)

### AIChannelCollectionCreateAccelerometerChannel Method (String, String, AITerminalConfiguration, Double, Double, Double, AIAccelerometerSensitivityUnits, AIExcitationSource, Double, AIAccelerationUnits)

AIChannel

accelerometer

measure acceleration

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateAccelerometerChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration configuration,
	double minimumValue,
	double maximumValue,
	double sensitivity,
	AIAccelerometerSensitivityUnits sensitivityUnits,
	AIExcitationSource currentExcitationSource,
	double currentExcitationValue,
	AIAccelerationUnits units
)
```

```text
Public Function CreateAccelerometerChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	configuration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	sensitivity As Double,
	sensitivityUnits As AIAccelerometerSensitivityUnits,
	currentExcitationSource As AIExcitationSource,
	currentExcitationValue As Double,
	units As AIAccelerationUnits
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemStringOne or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **configuration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **sensitivity**
  - Type: SystemDoubleThe sensitivity of the sensor. This value is in the units you specify with sensitivityUnits. Refer to sensor documentation to determine this value.
- **sensitivityUnits**
  - Type: NationalInstruments.DAQmxAIAccelerometerSensitivityUnitsThe units of sensitivity.
- **currentExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSourceThe source of excitation.
- **currentExcitationValue**
  - Type: SystemDoubleThe amount of excitation in amps that the sensor requires.
- **units**
  - Type: NationalInstruments.DAQmxAIAccelerationUnitsThe units to use to return the measurement.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for nameToAssignChannel. If you provide fewer local virtual channel names in nameToAssignChannel than you create, NI-DAQmx [automatically assigns names](/csh?topicname=mxcncpts/;) to the local virtual channels.

If you do not provide a value for nameToAssignChannel, NI-DAQmx uses the physicalChannelName as the local virtual channel name. If you use nameToAssignChannel to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateAccelerometerChannel(String, String, AITerminalConfiguration, Double, Double, Double, AIAccelerometerSensitivityUnits, AIExcitationSource, Double, AIAccelerationUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateAccelerometerChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel.htm language=enus -->
## TOPIC 00007: AIChannelCollectionCreateCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, AICurrentUnits)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, AICurrentUnits)

### AIChannelCollectionCreateCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, AICurrentUnits)

AIChannel

measure current

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateCurrentChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration terminalConfiguration,
	double minimumValue,
	double maximumValue,
	AICurrentUnits units
)
```

```text
Public Function CreateCurrentChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	terminalConfiguration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	units As AICurrentUnits
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **units**
  - Type: NationalInstruments.DAQmxAICurrentUnitsThe units to use to return the measurement.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for nameToAssignChannel. If you provide fewer local virtual channel names in nameToAssignChannel than you create, NI-DAQmx [automatically assigns names](/csh?topicname=mxcncpts/;) to the local virtual channels.

If you do not provide a value for nameToAssignChannel, NI-DAQmx uses the physicalChannelName as the local virtual channel name. If you use nameToAssignChannel to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method with devices that have a built-in shunt resistor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateCurrentChannel(String, String, AITerminalConfiguration, Double, Double, AICurrentUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateCurrentChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_2.htm language=enus -->
## TOPIC 00008: AIChannelCollectionCreateCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, Double, AICurrentUnits)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_2.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, Double, AICurrentUnits)

### AIChannelCollectionCreateCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, Double, AICurrentUnits)

AIChannel

measure current

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateCurrentChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration terminalConfiguration,
	double minimumValue,
	double maximumValue,
	double externalShuntResistorValue,
	AICurrentUnits units
)
```

```text
Public Function CreateCurrentChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	terminalConfiguration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	externalShuntResistorValue As Double,
	units As AICurrentUnits
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **externalShuntResistorValue**
  - Type: SystemDoubleThe value in ohms of an external shunt resistor.
- **units**
  - Type: NationalInstruments.DAQmxAICurrentUnitsThe units to use to return the measurement.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for nameToAssignChannel. If you provide fewer local virtual channel names in nameToAssignChannel than you create, NI-DAQmx [automatically assigns names](/csh?topicname=mxcncpts/;) to the local virtual channels.

If you do not provide a value for nameToAssignChannel, NI-DAQmx uses the physicalChannelName as the local virtual channel name. If you use nameToAssignChannel to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method with devices that do not have a built-in shunt resistor. You must attach an external shunt resistor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateCurrentChannel(String, String, AITerminalConfiguration, Double, Double, Double, AICurrentUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateCurrentChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_3.htm language=enus -->
## TOPIC 00009: AIChannelCollectionCreateCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, Double, String)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_3.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, Double, String)

### AIChannelCollectionCreateCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, Double, String)

AIChannel

measure current

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateCurrentChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration terminalConfiguration,
	double minimumValue,
	double maximumValue,
	double externalShuntResistorValue,
	string customScaleName
)
```

```text
Public Function CreateCurrentChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	terminalConfiguration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	externalShuntResistorValue As Double,
	customScaleName As String
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **externalShuntResistorValue**
  - Type: SystemDoubleThe value in ohms of an external shunt resistor.
- **customScaleName**
  - Type: SystemStringThe name of the custom scale to apply to the local virtual channel.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for nameToAssignChannel. If you provide fewer local virtual channel names in nameToAssignChannel than you create, NI-DAQmx [automatically assigns names](/csh?topicname=mxcncpts/;) to the local virtual channels.

If you do not provide a value for nameToAssignChannel, NI-DAQmx uses the physicalChannelName as the local virtual channel name. If you use nameToAssignChannel to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method with devices that do not have a built-in shunt resistor. You must attach an external shunt resistor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateCurrentChannel(String, String, AITerminalConfiguration, Double, Double, Double, String) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateCurrentChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_4.htm language=enus -->
## TOPIC 00010: AIChannelCollectionCreateCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, String)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_4.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_4.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, String)

### AIChannelCollectionCreateCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, String)

AIChannel

measure current

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateCurrentChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration terminalConfiguration,
	double minimumValue,
	double maximumValue,
	string customScaleName
)
```

```text
Public Function CreateCurrentChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	terminalConfiguration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	customScaleName As String
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **customScaleName**
  - Type: SystemStringThe name of the custom scale to apply to the local virtual channel.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for nameToAssignChannel. If you provide fewer local virtual channel names in nameToAssignChannel than you create, NI-DAQmx [automatically assigns names](/csh?topicname=mxcncpts/;) to the local virtual channels.

If you do not provide a value for nameToAssignChannel, NI-DAQmx uses the physicalChannelName as the local virtual channel name. If you use nameToAssignChannel to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method with devices that have a built-in shunt resistor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateCurrentChannel(String, String, AITerminalConfiguration, Double, Double, String) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateCurrentChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentrmschannel_1.htm language=enus -->
## TOPIC 00011: AIChannelCollectionCreateCurrentRmsChannel Method (String, String, AITerminalConfiguration, Double, Double, Double, AICurrentAcrmsUnits)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentrmschannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentrmschannel_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateCurrentRmsChannel Method (String, String, AITerminalConfiguration, Double, Double, Double, AICurrentAcrmsUnits)

### AIChannelCollectionCreateCurrentRmsChannel Method (String, String, AITerminalConfiguration, Double, Double, Double, AICurrentAcrmsUnits)

AIChannel

measure AC current

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateCurrentRmsChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration terminalConfiguration,
	double minimumValue,
	double maximumValue,
	double externalShuntResistorValue,
	AICurrentAcrmsUnits units
)
```

```text
Public Function CreateCurrentRmsChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	terminalConfiguration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	externalShuntResistorValue As Double,
	units As AICurrentAcrmsUnits
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **minimumValue**
  - Type: SystemDoubleThe minimum value you expect to measure, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value you expect to measure, in units.
- **externalShuntResistorValue**
  - Type: SystemDoubleThe value in ohms of an external shunt resistor.
- **units**
  - Type: NationalInstruments.DAQmxAICurrentAcrmsUnitsThe units to use to return the measurement.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for nameToAssignChannel. If you provide fewer local virtual channel names in nameToAssignChannel than you create, NI-DAQmx [automatically assigns names](/csh?topicname=mxcncpts/;) to the local virtual channels.

If you do not provide a value for nameToAssignChannel, NI-DAQmx uses the physicalChannelName as the local virtual channel name. If you use nameToAssignChannel to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method with devices that do not have a built-in shunt resistor. You must attach an external shunt resistor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. [CreateCurrentChannel(String, String, AITerminalConfiguration, Double, Double, Double, AICurrentUnits)](m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_2.htm) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateCurrentRmsChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentrmschannel_2.htm language=enus -->
## TOPIC 00012: AIChannelCollectionCreateCurrentRmsChannel Method (String, String, AITerminalConfiguration, Double, Double, Double, String)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentrmschannel_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentrmschannel_2.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateCurrentRmsChannel Method (String, String, AITerminalConfiguration, Double, Double, Double, String)

### AIChannelCollectionCreateCurrentRmsChannel Method (String, String, AITerminalConfiguration, Double, Double, Double, String)

AIChannel

measure AC current

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateCurrentRmsChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration terminalConfiguration,
	double minimumValue,
	double maximumValue,
	double externalShuntResistorValue,
	string customScaleName
)
```

```text
Public Function CreateCurrentRmsChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	terminalConfiguration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	externalShuntResistorValue As Double,
	customScaleName As String
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **minimumValue**
  - Type: SystemDoubleThe minimum value you expect to measure, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value you expect to measure, in units.
- **externalShuntResistorValue**
  - Type: SystemDoubleThe value in ohms of an external shunt resistor.
- **customScaleName**
  - Type: SystemStringThe name of the custom scale to apply to the local virtual channel.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for nameToAssignChannel. If you provide fewer local virtual channel names in nameToAssignChannel than you create, NI-DAQmx [automatically assigns names](/csh?topicname=mxcncpts/;) to the local virtual channels.

If you do not provide a value for nameToAssignChannel, NI-DAQmx uses the physicalChannelName as the local virtual channel name. If you use nameToAssignChannel to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method with devices that do not have a built-in shunt resistor. You must attach an external shunt resistor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. [CreateCurrentChannel(String, String, AITerminalConfiguration, Double, Double, Double, String)](m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_3.htm) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateCurrentRmsChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentrmschannel_3.htm language=enus -->
## TOPIC 00013: AIChannelCollectionCreateCurrentRmsChannel Method (String, String, AITerminalConfiguration, Double, Double, String)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentrmschannel_3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentrmschannel_3.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateCurrentRmsChannel Method (String, String, AITerminalConfiguration, Double, Double, String)

### AIChannelCollectionCreateCurrentRmsChannel Method (String, String, AITerminalConfiguration, Double, Double, String)

AIChannel

measure AC current

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateCurrentRmsChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration terminalConfiguration,
	double minimumValue,
	double maximumValue,
	string customScaleName
)
```

```text
Public Function CreateCurrentRmsChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	terminalConfiguration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	customScaleName As String
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **minimumValue**
  - Type: SystemDoubleThe minimum value you expect to measure, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value you expect to measure, in units.
- **customScaleName**
  - Type: SystemStringThe name of the custom scale to apply to the local virtual channel.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for nameToAssignChannel. If you provide fewer local virtual channel names in nameToAssignChannel than you create, NI-DAQmx [automatically assigns names](/csh?topicname=mxcncpts/;) to the local virtual channels.

If you do not provide a value for nameToAssignChannel, NI-DAQmx uses the physicalChannelName as the local virtual channel name. If you use nameToAssignChannel to create a name for the local virtual channel, you must use this name in other properties and methods.

Use this method with devices that have a built-in shunt resistor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. [CreateCurrentChannel(String, String, AITerminalConfiguration, Double, Double, String)](m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_4.htm) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateCurrentRmsChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createlvdtchannel_1.htm language=enus -->
## TOPIC 00014: AIChannelCollectionCreateLvdtChannel Method (String, String, Double, Double, Double, AILvdtSensitivityUnits, AIExcitationSource, Double, Double, AIACExcitationWireMode, String)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createlvdtchannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createlvdtchannel_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateLvdtChannel Method (String, String, Double, Double, Double, AILvdtSensitivityUnits, AIExcitationSource, Double, Double, AIACExcitationWireMode, String)

### AIChannelCollectionCreateLvdtChannel Method (String, String, Double, Double, Double, AILvdtSensitivityUnits, AIExcitationSource, Double, Double, AIACExcitationWireMode, String)

AIChannel

LVDT

measure linear position

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateLvdtChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	double sensitivity,
	AILvdtSensitivityUnits sensitivityUnits,
	AIExcitationSource voltageExcitationSource,
	double voltageExcitationValue,
	double voltageExcitationFrequency,
	AIACExcitationWireMode voltageExcitationWireMode,
	string customScaleName
)
```

```text
Public Function CreateLvdtChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	sensitivity As Double,
	sensitivityUnits As AILvdtSensitivityUnits,
	voltageExcitationSource As AIExcitationSource,
	voltageExcitationValue As Double,
	voltageExcitationFrequency As Double,
	voltageExcitationWireMode As AIACExcitationWireMode,
	customScaleName As String
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemStringOne or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **sensitivity**
  - Type: SystemDoubleThe sensitivity of the sensor. This value is in the units you specify with sensitivityUnits. Refer to the sensor documentation to determine this value.
- **sensitivityUnits**
  - Type: NationalInstruments.DAQmxAILvdtSensitivityUnitsThe units of sensitivity.
- **voltageExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSourceThe source of excitation.
- **voltageExcitationValue**
  - Type: SystemDoubleThe amount of excitation in volts that the sensor requires.
- **voltageExcitationFrequency**
  - Type: SystemDoubleThe excitation frequency that the sensor requires, in hertz. Refer to the sensor documentation to determine this value.
- **voltageExcitationWireMode**
  - Type: NationalInstruments.DAQmxAIACExcitationWireModeThe number of leads on the sensor. Some sensors might require you to tie leads together to create a four- or five-wire sensor. Refer to the documentation for your sensor for more information.
- **customScaleName**
  - Type: SystemStringThe name of the custom scale to apply to the local virtual channel.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for nameToAssignChannel. If you provide fewer local virtual channel names in nameToAssignChannel than you create, NI-DAQmx [automatically assigns names](/csh?topicname=mxcncpts/;) to the local virtual channels.

If you do not provide a value for nameToAssignChannel, NI-DAQmx uses the physicalChannelName as the local virtual channel name. If you use nameToAssignChannel to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateLvdtChannel(String, String, Double, Double, Double, AILvdtSensitivityUnits, AIExcitationSource, Double, Double, AIACExcitationWireMode, String) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateLvdtChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedscurrentchannel.htm language=enus -->
## TOPIC 00015: AIChannelCollectionCreateTedsCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, AICurrentUnits)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedscurrentchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedscurrentchannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, AICurrentUnits)

### AIChannelCollectionCreateTedsCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, AICurrentUnits)

AIChannel

measure current

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateTedsCurrentChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration terminalConfiguration,
	double minimumValue,
	double maximumValue,
	AICurrentUnits units
)
```

```text
Public Function CreateTedsCurrentChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	terminalConfiguration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	units As AICurrentUnits
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **units**
  - Type: NationalInstruments.DAQmxAICurrentUnitsThe units to use to return the current measurement.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateTedsCurrentChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedscurrentchannel_3.htm language=enus -->
## TOPIC 00016: AIChannelCollectionCreateTedsCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, String)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedscurrentchannel_3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedscurrentchannel_3.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, String)

### AIChannelCollectionCreateTedsCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, String)

AIChannel

measure current

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateTedsCurrentChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration terminalConfiguration,
	double minimumValue,
	double maximumValue,
	string customScaleName
)
```

```text
Public Function CreateTedsCurrentChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	terminalConfiguration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	customScaleName As String
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **customScaleName**
  - Type: SystemStringThe name of the custom scale to apply to the local virtual channel.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateTedsCurrentChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsforcebridgechannel_1.htm language=enus -->
## TOPIC 00017: AIChannelCollectionCreateTedsForceBridgeChannel Method (String, String, Double, Double, String, AIExcitationSource, Double)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsforcebridgechannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsforcebridgechannel_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsForceBridgeChannel Method (String, String, Double, Double, String, AIExcitationSource, Double)

### AIChannelCollectionCreateTedsForceBridgeChannel Method (String, String, Double, Double, String, AIExcitationSource, Double)

AIChannel

Wheatstone bridge

measure force or load

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateTedsForceBridgeChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	string customScaleName,
	AIExcitationSource voltageExcitationSource,
	double voltageExcitationValue
)
```

```text
Public Function CreateTedsForceBridgeChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	customScaleName As String,
	voltageExcitationSource As AIExcitationSource,
	voltageExcitationValue As Double
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemString The names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **minimumValue**
  - Type: SystemDouble The minimum value you expect to measure, in units.
- **maximumValue**
  - Type: SystemDouble The maximum value you expect to measure, in units.
- **customScaleName**
  - Type: SystemString The name of the custom scale to apply to the local virtual channel.
- **voltageExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSourceThe source of excitation.
- **voltageExcitationValue**
  - Type: SystemDoubleThe amount of excitation in volts that the sensor requires.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a
 [Task](t_nationalinstruments_daqmx_task.htm)
 are valid, you must verify the task by starting the task, either with
 [Start](m_nationalinstruments_daqmx_task_start.htm)
 or by reading from or writing to the task, or by calling
 [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm)
 with
 [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateTedsForceBridgeChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsmicrophonechannel.htm language=enus -->
## TOPIC 00018: AIChannelCollectionCreateTedsMicrophoneChannel Method (String, String, Double, AITerminalConfiguration, AIExcitationSource, Double, AISoundPressureUnits)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsmicrophonechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsmicrophonechannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsMicrophoneChannel Method (String, String, Double, AITerminalConfiguration, AIExcitationSource, Double, AISoundPressureUnits)

### AIChannelCollectionCreateTedsMicrophoneChannel Method (String, String, Double, AITerminalConfiguration, AIExcitationSource, Double, AISoundPressureUnits)

AIChannel

measure sound pressure

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateTedsMicrophoneChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double maximumSoundPressureLevel,
	AITerminalConfiguration terminalConfiguration,
	AIExcitationSource currentExcitationSource,
	double currentExcitationValue,
	AISoundPressureUnits units
)
```

```text
Public Function CreateTedsMicrophoneChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	maximumSoundPressureLevel As Double,
	terminalConfiguration As AITerminalConfiguration,
	currentExcitationSource As AIExcitationSource,
	currentExcitationValue As Double,
	units As AISoundPressureUnits
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **maximumSoundPressureLevel**
  - Type: SystemDoubleThe maximum instantaneous sound pressure level you expect to measure. This value is in decibels, referenced to 20 micropascals.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **currentExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSourceThe source of excitation.
- **currentExcitationValue**
  - Type: SystemDoubleThe amount of excitation in amperes that the sensor requires. Refer to the sensor documentation to determine this value.
- **units**
  - Type: NationalInstruments.DAQmxAISoundPressureUnitsThe units to use to return the sound pressure measurement.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateTedsMicrophoneChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsmicrophonechannel_1.htm language=enus -->
## TOPIC 00019: AIChannelCollectionCreateTedsMicrophoneChannel Method (String, String, Double, AITerminalConfiguration, AIExcitationSource, Double, String)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsmicrophonechannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsmicrophonechannel_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsMicrophoneChannel Method (String, String, Double, AITerminalConfiguration, AIExcitationSource, Double, String)

### AIChannelCollectionCreateTedsMicrophoneChannel Method (String, String, Double, AITerminalConfiguration, AIExcitationSource, Double, String)

AIChannel

measure sound pressure

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateTedsMicrophoneChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double maximumSoundPressureLevel,
	AITerminalConfiguration terminalConfiguration,
	AIExcitationSource currentExcitationSource,
	double currentExcitationValue,
	string customScaleName
)
```

```text
Public Function CreateTedsMicrophoneChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	maximumSoundPressureLevel As Double,
	terminalConfiguration As AITerminalConfiguration,
	currentExcitationSource As AIExcitationSource,
	currentExcitationValue As Double,
	customScaleName As String
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **maximumSoundPressureLevel**
  - Type: SystemDoubleThe maximum instantaneous sound pressure level you expect to measure. This value is in decibels, referenced to 20 micropascals.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **currentExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSourceThe source of excitation.
- **currentExcitationValue**
  - Type: SystemDoubleThe amount of excitation in amperes that the sensor requires. Refer to the sensor documentation to determine this value.
- **customScaleName**
  - Type: SystemStringThe name of the custom scale to apply to the local virtual channel.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateTedsMicrophoneChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsresistancechannel.htm language=enus -->
## TOPIC 00020: AIChannelCollectionCreateTedsResistanceChannel Method (String, String, Double, Double, AIResistanceConfiguration, AIExcitationSource, Double, AIResistanceUnits)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsresistancechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsresistancechannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsResistanceChannel Method (String, String, Double, Double, AIResistanceConfiguration, AIExcitationSource, Double, AIResistanceUnits)

### AIChannelCollectionCreateTedsResistanceChannel Method (String, String, Double, Double, AIResistanceConfiguration, AIExcitationSource, Double, AIResistanceUnits)

AIChannel

measure resistance

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateTedsResistanceChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	AIResistanceConfiguration resistanceConfiguration,
	AIExcitationSource currentExcitationSource,
	double currentExcitationValue,
	AIResistanceUnits units
)
```

```text
Public Function CreateTedsResistanceChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	resistanceConfiguration As AIResistanceConfiguration,
	currentExcitationSource As AIExcitationSource,
	currentExcitationValue As Double,
	units As AIResistanceUnits
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **resistanceConfiguration**
  - Type: NationalInstruments.DAQmxAIResistanceConfigurationThe number of wires to use for resistive measurements.
- **currentExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSourceThe source of excitation.
- **currentExcitationValue**
  - Type: SystemDoubleThe amount of excitation in amperes that the sensor requires. Refer to the sensor documentation to determine this value.
- **units**
  - Type: NationalInstruments.DAQmxAIResistanceUnitsThe units to use to return the resistance measurement.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateTedsResistanceChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsstraingagechannel.htm language=enus -->
## TOPIC 00021: AIChannelCollectionCreateTedsStrainGageChannel Method (String, String, Double, Double, AIExcitationSource, Double, Double, Double, AIStrainUnits)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsstraingagechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsstraingagechannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsStrainGageChannel Method (String, String, Double, Double, AIExcitationSource, Double, Double, Double, AIStrainUnits)

### AIChannelCollectionCreateTedsStrainGageChannel Method (String, String, Double, Double, AIExcitationSource, Double, Double, Double, AIStrainUnits)

AIChannel

measure strain

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateTedsStrainGageChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	AIExcitationSource voltageExcitationSource,
	double voltageExcitationValue,
	double initialBridgeVoltage,
	double leadWireResistance,
	AIStrainUnits units
)
```

```text
Public Function CreateTedsStrainGageChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	voltageExcitationSource As AIExcitationSource,
	voltageExcitationValue As Double,
	initialBridgeVoltage As Double,
	leadWireResistance As Double,
	units As AIStrainUnits
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **voltageExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSourceThe source of excitation.
- **voltageExcitationValue**
  - Type: SystemDoubleThe amount of excitation in volts that the sensor requires. Refer to the sensor documentation to determine this value.
- **initialBridgeVoltage**
  - Type: SystemDoubleThe output voltage of the bridge in the unloaded condition. NI-DAQmx subtracts this value from any measurements before applying scaling equations. Perform a voltage measurement on the bridge with no strain applied to determine this value.
- **leadWireResistance**
  - Type: SystemDoubleThe amount of resistance in ohms in the lead wires. Ideally, this value is the same for all leads.
- **units**
  - Type: NationalInstruments.DAQmxAIStrainUnitsThe units to use to return the strain measurement.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateTedsStrainGageChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsthermocouplechannel_2.htm language=enus -->
## TOPIC 00022: AIChannelCollectionCreateTedsThermocoupleChannel Method (String, String, Double, Double, AITemperatureUnits, String)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsthermocouplechannel_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsthermocouplechannel_2.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsThermocoupleChannel Method (String, String, Double, Double, AITemperatureUnits, String)

### AIChannelCollectionCreateTedsThermocoupleChannel Method (String, String, Double, Double, AITemperatureUnits, String)

AIChannel

thermocouple

measure temperature

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateTedsThermocoupleChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	AITemperatureUnits units,
	string cjcChannel
)
```

```text
Public Function CreateTedsThermocoupleChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	units As AITemperatureUnits,
	cjcChannel As String
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **units**
  - Type: NationalInstruments.DAQmxAITemperatureUnitsThe units to use to return the temperature measurement.
- **cjcChannel**
  - Type: SystemStringThe channel that acquires the temperature of the thermocouple cold-junction if you set AIThermocoupleCjcSource to Channel. You can use a global channel or another virtual channel already in the task. If the channel is a temperature channel, NI-DAQmx acquires the temperature in the correct units. Other channel types, such as a resistance channel with a custom sensor, must use a custom scale to scale values to degrees Celsius.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateTedsThermocoupleChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedstorquebridgechannel.htm language=enus -->
## TOPIC 00023: AIChannelCollectionCreateTedsTorqueBridgeChannel Method (String, String, Double, Double, AITorqueUnits, AIExcitationSource, Double)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedstorquebridgechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedstorquebridgechannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsTorqueBridgeChannel Method (String, String, Double, Double, AITorqueUnits, AIExcitationSource, Double)

### AIChannelCollectionCreateTedsTorqueBridgeChannel Method (String, String, Double, Double, AITorqueUnits, AIExcitationSource, Double)

AIChannel

Wheatstone bridge

measure torque

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateTedsTorqueBridgeChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	AITorqueUnits units,
	AIExcitationSource voltageExcitationSource,
	double voltageExcitationValue
)
```

```text
Public Function CreateTedsTorqueBridgeChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	units As AITorqueUnits,
	voltageExcitationSource As AIExcitationSource,
	voltageExcitationValue As Double
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemString The names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **minimumValue**
  - Type: SystemDouble The minimum value you expect to measure, in units.
- **maximumValue**
  - Type: SystemDouble The maximum value you expect to measure, in units.
- **units**
  - Type: NationalInstruments.DAQmxAITorqueUnitsThe units to use to return the measurement.
- **voltageExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSourceThe source of excitation.
- **voltageExcitationValue**
  - Type: SystemDoubleThe amount of excitation, in volts, that the sensor requires.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for
 nameToAssignChannel. If you provide fewer local virtual channel names in
 nameToAssignChannel
 than you create, NI-DAQmx
 [automatically assigns names](/csh?topicname=mxcncpts/;)
 to the local virtual channels.

If you do not provide a value for
 nameToAssignChannel, NI-DAQmx uses the
 physicalChannelName
 as the local virtual channel name. If you use
 nameToAssignChannel
 to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a
 [Task](t_nationalinstruments_daqmx_task.htm)
 are valid, you must verify the task by starting the task, either with
 [Start](m_nationalinstruments_daqmx_task_start.htm)
 or by reading from or writing to the task, or by calling
 [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm)
 with
 [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateTedsTorqueBridgeChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedstorquebridgechannel_1.htm language=enus -->
## TOPIC 00024: AIChannelCollectionCreateTedsTorqueBridgeChannel Method (String, String, Double, Double, String, AIExcitationSource, Double)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedstorquebridgechannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedstorquebridgechannel_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsTorqueBridgeChannel Method (String, String, Double, Double, String, AIExcitationSource, Double)

### AIChannelCollectionCreateTedsTorqueBridgeChannel Method (String, String, Double, Double, String, AIExcitationSource, Double)

AIChannel

Wheatstone bridge

measure torque

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateTedsTorqueBridgeChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	string customScaleName,
	AIExcitationSource voltageExcitationSource,
	double voltageExcitationValue
)
```

```text
Public Function CreateTedsTorqueBridgeChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	customScaleName As String,
	voltageExcitationSource As AIExcitationSource,
	voltageExcitationValue As Double
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemString The names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **minimumValue**
  - Type: SystemDouble The minimum value you expect to measure, in custom scaled units.
- **maximumValue**
  - Type: SystemDouble The maximum value you expect to measure, in custom scaled units.
- **customScaleName**
  - Type: SystemString The name of the custom scale to apply to the local virtual channel.
- **voltageExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSourceThe source of excitation.
- **voltageExcitationValue**
  - Type: SystemDoubleThe amount of excitation, in volts, that the sensor requires.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for
 nameToAssignChannel. If you provide fewer local virtual channel names in
 nameToAssignChannel
 than you create, NI-DAQmx
 [automatically assigns names](/csh?topicname=mxcncpts/;)
 to the local virtual channels.

If you do not provide a value for
 nameToAssignChannel, NI-DAQmx uses the
 physicalChannelName
 as the local virtual channel name. If you use
 nameToAssignChannel
 to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a
 [Task](t_nationalinstruments_daqmx_task.htm)
 are valid, you must verify the task by starting the task, either with
 [Start](m_nationalinstruments_daqmx_task_start.htm)
 or by reading from or writing to the task, or by calling
 [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm)
 with
 [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateTedsTorqueBridgeChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsvoltagechannel.htm language=enus -->
## TOPIC 00025: AIChannelCollectionCreateTedsVoltageChannel Method (String, String, AITerminalConfiguration, Double, Double, AIVoltageUnits)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsvoltagechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsvoltagechannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsVoltageChannel Method (String, String, AITerminalConfiguration, Double, Double, AIVoltageUnits)

### AIChannelCollectionCreateTedsVoltageChannel Method (String, String, AITerminalConfiguration, Double, Double, AIVoltageUnits)

AIChannel

measure voltage

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateTedsVoltageChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration terminalConfiguration,
	double minimumValue,
	double maximumValue,
	AIVoltageUnits units
)
```

```text
Public Function CreateTedsVoltageChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	terminalConfiguration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	units As AIVoltageUnits
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **units**
  - Type: NationalInstruments.DAQmxAIVoltageUnitsThe units to use to return the voltage measurement.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

| Note |
| --- |
| If the measurement requires the use of internal excitation or you need the voltage to be scaled by the excitation, use CreateTedsVoltageChannelWithExcitation(String, String, AITerminalConfiguration, Double, Double, AIExcitationSource, Double, String) instead. |

##### See Also

###### Reference

AIChannelCollection Class

CreateTedsVoltageChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsvoltagechannel_1.htm language=enus -->
## TOPIC 00026: AIChannelCollectionCreateTedsVoltageChannel Method (String, String, AITerminalConfiguration, Double, Double, String)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsvoltagechannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsvoltagechannel_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsVoltageChannel Method (String, String, AITerminalConfiguration, Double, Double, String)

### AIChannelCollectionCreateTedsVoltageChannel Method (String, String, AITerminalConfiguration, Double, Double, String)

AIChannel

measure voltage

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateTedsVoltageChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration terminalConfiguration,
	double minimumValue,
	double maximumValue,
	string customScaleName
)
```

```text
Public Function CreateTedsVoltageChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	terminalConfiguration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	customScaleName As String
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **customScaleName**
  - Type: SystemStringThe name of the custom scale to apply to the local virtual channel.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

| Note |
| --- |
| If the measurement requires the use of internal excitation or you need the voltage to be scaled by the excitation, use CreateTedsVoltageChannelWithExcitation(String, String, AITerminalConfiguration, Double, Double, AIExcitationSource, Double, String) instead. |

##### See Also

###### Reference

AIChannelCollection Class

CreateTedsVoltageChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsvoltagechannelwithexcitation_1.htm language=enus -->
## TOPIC 00027: AIChannelCollectionCreateTedsVoltageChannelWithExcitation Method (String, String, AITerminalConfiguration, Double, Double, AIExcitationSource, Double, String)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsvoltagechannelwithexcitation_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtedsvoltagechannelwithexcitation_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsVoltageChannelWithExcitation Method (String, String, AITerminalConfiguration, Double, Double, AIExcitationSource, Double, String)

### AIChannelCollectionCreateTedsVoltageChannelWithExcitation Method (String, String, AITerminalConfiguration, Double, Double, AIExcitationSource, Double, String)

AIChannel

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateTedsVoltageChannelWithExcitation(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration configuration,
	double minimumValue,
	double maximumValue,
	AIExcitationSource voltageExcitationSource,
	double voltageExcitationValue,
	string customScaleName
)
```

```text
Public Function CreateTedsVoltageChannelWithExcitation ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	configuration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	voltageExcitationSource As AIExcitationSource,
	voltageExcitationValue As Double,
	customScaleName As String
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **configuration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **voltageExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSourceThe source of excitation.
- **voltageExcitationValue**
  - Type: SystemDoubleThe amount of excitation in volts that the sensor requires. Refer to the sensor documentation to determine this value.
- **customScaleName**
  - Type: SystemStringThe name of the custom scale to apply to the local virtual channel.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

You must configure the physical channel(s) with TEDS information to use this method.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateTedsVoltageChannelWithExcitation Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createthermistorvexchannel.htm language=enus -->
## TOPIC 00028: AIChannelCollectionCreateThermistorVExChannel Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createthermistorvexchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createthermistorvexchannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateThermistorVExChannel Method

### AIChannelCollectionCreateThermistorVExChannel Method

AIChannel

thermistor

measure temperature

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateThermistorVExChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	AITemperatureUnits units,
	AIResistanceConfiguration resistanceConfiguration,
	AIExcitationSource voltageExcitationSource,
	double voltageExcitationValue,
	double a,
	double b,
	double c,
	double r1
)
```

```text
Public Function CreateThermistorVExChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	units As AITemperatureUnits,
	resistanceConfiguration As AIResistanceConfiguration,
	voltageExcitationSource As AIExcitationSource,
	voltageExcitationValue As Double,
	a As Double,
	b As Double,
	c As Double,
	r1 As Double
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **units**
  - Type: NationalInstruments.DAQmxAITemperatureUnitsThe units to use to return the measurement.
- **resistanceConfiguration**
  - Type: NationalInstruments.DAQmxAIResistanceConfigurationThe number of wires to use for resistive measurements.
- **voltageExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSourceThe source of excitation.
- **voltageExcitationValue**
  - Type: SystemDoubleThe amount of excitation in volts that the sensor requires. Refer to the sensor documentation to determine this value.
- **a**
  - Type: SystemDoubleThe A constant for the Steinhart-Hart thermistor equation. Consult the sensor documentation to determine the value for this constant.
- **b**
  - Type: SystemDoubleThe B constant for the Steinhart-Hart thermistor equation. Consult the sensor documentation to determine the value for this constant.
- **c**
  - Type: SystemDoubleThe C constant for the Steinhart-Hart thermistor equation. Consult the sensor documentation to determine the value for this constant.
- **r1**
  - Type: SystemDoubleThe value of the dropping resistor, in ohms.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for nameToAssignChannel. If you provide fewer local virtual channel names in nameToAssignChannel than you create, NI-DAQmx [automatically assigns names](/csh?topicname=mxcncpts/;) to the local virtual channels.

If you do not provide a value for nameToAssignChannel, NI-DAQmx uses the physicalChannelName as the local virtual channel name. If you use nameToAssignChannel to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateThermistorVExChannel(String, String, Double, Double, AITemperatureUnits, AIResistanceConfiguration, AIExcitationSource, Double, Double, Double, Double, Double) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createthermocouplechannel_1.htm language=enus -->
## TOPIC 00029: AIChannelCollectionCreateThermocoupleChannel Method (String, String, Double, Double, AIThermocoupleType, AITemperatureUnits, Double)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createthermocouplechannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createthermocouplechannel_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateThermocoupleChannel Method (String, String, Double, Double, AIThermocoupleType, AITemperatureUnits, Double)

### AIChannelCollectionCreateThermocoupleChannel Method (String, String, Double, Double, AIThermocoupleType, AITemperatureUnits, Double)

AIChannel

thermocouple

measure temperature

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateThermocoupleChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	AIThermocoupleType thermocoupleType,
	AITemperatureUnits units,
	double cjcValue
)
```

```text
Public Function CreateThermocoupleChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	thermocoupleType As AIThermocoupleType,
	units As AITemperatureUnits,
	cjcValue As Double
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **thermocoupleType**
  - Type: NationalInstruments.DAQmxAIThermocoupleTypeThe type of thermocouple connected to the channel. Thermocouple types differ in composition and measurement range.
- **units**
  - Type: NationalInstruments.DAQmxAITemperatureUnitsThe units to use to return the temperature measurement.
- **cjcValue**
  - Type: SystemDoubleThe temperature in units of the cold-junction.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for nameToAssignChannel. If you provide fewer local virtual channel names in nameToAssignChannel than you create, NI-DAQmx [automatically assigns names](/csh?topicname=mxcncpts/;) to the local virtual channels.

If you do not provide a value for nameToAssignChannel, NI-DAQmx uses the physicalChannelName as the local virtual channel name. If you use nameToAssignChannel to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateThermocoupleChannel(String, String, Double, Double, AIThermocoupleType, AITemperatureUnits, Double) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateThermocoupleChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtorquebridgepolynomialchannel.htm language=enus -->
## TOPIC 00030: AIChannelCollectionCreateTorqueBridgePolynomialChannel Method (String, String, Double, Double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtorquebridgepolynomialchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtorquebridgepolynomialchannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTorqueBridgePolynomialChannel Method (String, String, Double, Double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double[], Double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits)

### AIChannelCollectionCreateTorqueBridgePolynomialChannel Method (String, String, Double, Double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits)

AIChannel

Wheatstone bridge

measure torque

PolynomialScale

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateTorqueBridgePolynomialChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	AITorqueUnits units,
	AIBridgeConfiguration bridgeConfiguration,
	AIExcitationSource voltageExcitationSource,
	double voltageExcitationValue,
	double nominalBridgeResistance,
	double[] forwardCoefficients,
	double[] reverseCoefficients,
	AIBridgeElectricalUnits electricalUnits,
	AIBridgePhysicalUnits physicalUnits
)
```

```text
Public Function CreateTorqueBridgePolynomialChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	units As AITorqueUnits,
	bridgeConfiguration As AIBridgeConfiguration,
	voltageExcitationSource As AIExcitationSource,
	voltageExcitationValue As Double,
	nominalBridgeResistance As Double,
	forwardCoefficients As Double(),
	reverseCoefficients As Double(),
	electricalUnits As AIBridgeElectricalUnits,
	physicalUnits As AIBridgePhysicalUnits
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemString The names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **minimumValue**
  - Type: SystemDouble The minimum value you expect to measure, in units.
- **maximumValue**
  - Type: SystemDouble The maximum value you expect to measure, in units.
- **units**
  - Type: NationalInstruments.DAQmxAITorqueUnitsThe units to use to return the measurement.
- **bridgeConfiguration**
  - Type: NationalInstruments.DAQmxAIBridgeConfigurationThe type of Wheatstone bridge configuration connected to the channel.
- **voltageExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSourceThe source of excitation.
- **voltageExcitationValue**
  - Type: SystemDoubleThe amount of excitation, in volts, that the sensor requires.
- **nominalBridgeResistance**
  - Type: SystemDoubleThe resistance, in ohms, of the bridge while not under load.
- **forwardCoefficients**
  - Type: SystemDouble The array of the forward coefficients of the polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x3.
- **reverseCoefficients**
  - Type: SystemDouble The array of the reverse coefficients of the polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9y3.
- **electricalUnits**
  - Type: NationalInstruments.DAQmxAIBridgeElectricalUnitsSpecifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate.
- **physicalUnits**
  - Type: NationalInstruments.DAQmxAIBridgePhysicalUnitsSpecifies to which physical units to scale electrical data.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Specify different values for physical units if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for
 nameToAssignChannel. If you provide fewer local virtual channel names in
 nameToAssignChannel
 than you create, NI-DAQmx
 [automatically assigns names](/csh?topicname=mxcncpts/;)
 to the local virtual channels.

If you do not provide a value for
 nameToAssignChannel, NI-DAQmx uses the
 physicalChannelName
 as the local virtual channel name. If you use
 nameToAssignChannel
 to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a
 [Task](t_nationalinstruments_daqmx_task.htm)
 are valid, you must verify the task by starting the task, either with
 [Start](m_nationalinstruments_daqmx_task_start.htm)
 or by reading from or writing to the task, or by calling
 [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm)
 with
 [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateTorqueBridgePolynomialChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtorquebridgetwopointlinearchannel.htm language=enus -->
## TOPIC 00031: AIChannelCollectionCreateTorqueBridgeTwoPointLinearChannel Method (String, String, Double, Double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtorquebridgetwopointlinearchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtorquebridgetwopointlinearchannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTorqueBridgeTwoPointLinearChannel Method (String, String, Double, Double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits)

### AIChannelCollectionCreateTorqueBridgeTwoPointLinearChannel Method (String, String, Double, Double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits)

AIChannel

Wheatstone bridge

measure torque

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateTorqueBridgeTwoPointLinearChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	AITorqueUnits units,
	AIBridgeConfiguration bridgeConfiguration,
	AIExcitationSource voltageExcitationSource,
	double voltageExcitationValue,
	double nominalBridgeResistance,
	double firstElectricalValue,
	double secondElectricalValue,
	AIBridgeElectricalUnits electricalUnits,
	double firstPhysicalValue,
	double secondPhysicalValue,
	AIBridgePhysicalUnits physicalUnits
)
```

```text
Public Function CreateTorqueBridgeTwoPointLinearChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	units As AITorqueUnits,
	bridgeConfiguration As AIBridgeConfiguration,
	voltageExcitationSource As AIExcitationSource,
	voltageExcitationValue As Double,
	nominalBridgeResistance As Double,
	firstElectricalValue As Double,
	secondElectricalValue As Double,
	electricalUnits As AIBridgeElectricalUnits,
	firstPhysicalValue As Double,
	secondPhysicalValue As Double,
	physicalUnits As AIBridgePhysicalUnits
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemString The names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **minimumValue**
  - Type: SystemDouble The minimum value you expect to measure, in units.
- **maximumValue**
  - Type: SystemDouble The maximum value you expect to measure, in units.
- **units**
  - Type: NationalInstruments.DAQmxAITorqueUnitsThe units to use to return the measurement.
- **bridgeConfiguration**
  - Type: NationalInstruments.DAQmxAIBridgeConfigurationThe type of Wheatstone bridge configuration connected to the channel.
- **voltageExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSourceThe source of excitation.
- **voltageExcitationValue**
  - Type: SystemDoubleThe amount of excitation, in volts, that the sensor requires.
- **nominalBridgeResistance**
  - Type: SystemDoubleThe resistance, in ohms, of the bridge while not under load.
- **firstElectricalValue**
  - Type: SystemDouble The first electrical value, corresponding to firstPhysicalValue. Specify this value in the units specified with electricalUnits.
- **secondElectricalValue**
  - Type: SystemDouble The second electrical value, corresponding to secondPhysicalValue. Specify this value in the units specified with electricalUnits.
- **electricalUnits**
  - Type: NationalInstruments.DAQmxAIBridgeElectricalUnitsSpecifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate.
- **firstPhysicalValue**
  - Type: SystemDouble The first physical value, corresponding to firstElectricalValue. Specify this value in the units specified with physicalUnits.
- **secondPhysicalValue**
  - Type: SystemDouble The second physical value, corresponding to secondElectricalValue. Specify this value in the units specified with physicalUnits.
- **physicalUnits**
  - Type: NationalInstruments.DAQmxAIBridgePhysicalUnitsSpecifies to which physical units to scale electrical data.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Specify different values for physical units if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for
 nameToAssignChannel. If you provide fewer local virtual channel names in
 nameToAssignChannel
 than you create, NI-DAQmx
 [automatically assigns names](/csh?topicname=mxcncpts/;)
 to the local virtual channels.

If you do not provide a value for
 nameToAssignChannel, NI-DAQmx uses the
 physicalChannelName
 as the local virtual channel name. If you use
 nameToAssignChannel
 to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a
 [Task](t_nationalinstruments_daqmx_task.htm)
 are valid, you must verify the task by starting the task, either with
 [Start](m_nationalinstruments_daqmx_task_start.htm)
 or by reading from or writing to the task, or by calling
 [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm)
 with
 [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateTorqueBridgeTwoPointLinearChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtorquebridgetwopointlinearchannel_1.htm language=enus -->
## TOPIC 00032: AIChannelCollectionCreateTorqueBridgeTwoPointLinearChannel Method (String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtorquebridgetwopointlinearchannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtorquebridgetwopointlinearchannel_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTorqueBridgeTwoPointLinearChannel Method (String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits)

### AIChannelCollectionCreateTorqueBridgeTwoPointLinearChannel Method (String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits)

AIChannel

Wheatstone bridge

measure torque

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateTorqueBridgeTwoPointLinearChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	string customScaleName,
	AIBridgeConfiguration bridgeConfiguration,
	AIExcitationSource voltageExcitationSource,
	double voltageExcitationValue,
	double nominalBridgeResistance,
	double firstElectricalValue,
	double secondElectricalValue,
	AIBridgeElectricalUnits electricalUnits,
	double firstPhysicalValue,
	double secondPhysicalValue,
	AIBridgePhysicalUnits physicalUnits
)
```

```text
Public Function CreateTorqueBridgeTwoPointLinearChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	customScaleName As String,
	bridgeConfiguration As AIBridgeConfiguration,
	voltageExcitationSource As AIExcitationSource,
	voltageExcitationValue As Double,
	nominalBridgeResistance As Double,
	firstElectricalValue As Double,
	secondElectricalValue As Double,
	electricalUnits As AIBridgeElectricalUnits,
	firstPhysicalValue As Double,
	secondPhysicalValue As Double,
	physicalUnits As AIBridgePhysicalUnits
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemString The names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **minimumValue**
  - Type: SystemDouble The minimum value you expect to measure, in custom scaled units.
- **maximumValue**
  - Type: SystemDouble The maximum value you expect to measure, in custom scaled units.
- **customScaleName**
  - Type: SystemString The name of the custom scale to apply to the local virtual channel.
- **bridgeConfiguration**
  - Type: NationalInstruments.DAQmxAIBridgeConfigurationThe type of Wheatstone bridge configuration connected to the channel.
- **voltageExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSourceThe source of excitation.
- **voltageExcitationValue**
  - Type: SystemDoubleThe amount of excitation, in volts, that the sensor requires.
- **nominalBridgeResistance**
  - Type: SystemDoubleThe resistance, in ohms, of the bridge while not under load.
- **firstElectricalValue**
  - Type: SystemDouble The first electrical value, corresponding to firstPhysicalValue. Specify this value in the units specified with electricalUnits.
- **secondElectricalValue**
  - Type: SystemDouble The second electrical value, corresponding to secondPhysicalValue. Specify this value in the units specified with electricalUnits.
- **electricalUnits**
  - Type: NationalInstruments.DAQmxAIBridgeElectricalUnitsSpecifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate.
- **firstPhysicalValue**
  - Type: SystemDouble The first physical value, corresponding to firstElectricalValue. Specify this value in the units specified with physicalUnits.
- **secondPhysicalValue**
  - Type: SystemDouble The second physical value, corresponding to secondElectricalValue. Specify this value in the units specified with physicalUnits.
- **physicalUnits**
  - Type: NationalInstruments.DAQmxAIBridgePhysicalUnitsSpecifies to which physical units to scale electrical data.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Specify different values for physical units if the sensor specifications provide physical values in one unit, but you want NI-DAQmx to scale data to a different unit.

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for
 nameToAssignChannel. If you provide fewer local virtual channel names in
 nameToAssignChannel
 than you create, NI-DAQmx
 [automatically assigns names](/csh?topicname=mxcncpts/;)
 to the local virtual channels.

If you do not provide a value for
 nameToAssignChannel, NI-DAQmx uses the
 physicalChannelName
 as the local virtual channel name. If you use
 nameToAssignChannel
 to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a
 [Task](t_nationalinstruments_daqmx_task.htm)
 are valid, you must verify the task by starting the task, either with
 [Start](m_nationalinstruments_daqmx_task_start.htm)
 or by reading from or writing to the task, or by calling
 [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm)
 with
 [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateTorqueBridgeTwoPointLinearChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createvelocityiepechannel.htm language=enus -->
## TOPIC 00033: AIChannelCollectionCreateVelocityIepeChannel Method (String, String, AITerminalConfiguration, Double, Double, AIVelocityUnits, Double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, Double)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createvelocityiepechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createvelocityiepechannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateVelocityIepeChannel Method (String, String, AITerminalConfiguration, Double, Double, AIVelocityUnits, Double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, Double)

### AIChannelCollectionCreateVelocityIepeChannel Method (String, String, AITerminalConfiguration, Double, Double, AIVelocityUnits, Double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, Double)

AIChannel

IEPE velocity sensor

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateVelocityIepeChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration terminalConfiguration,
	double minimumValue,
	double maximumValue,
	AIVelocityUnits units,
	double sensitivity,
	AIVelocityIepeSensorSensitivityUnits sensitivityUnits,
	AIExcitationSource currentExcitationSource,
	double currentExcitationValue
)
```

```text
Public Function CreateVelocityIepeChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	terminalConfiguration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	units As AIVelocityUnits,
	sensitivity As Double,
	sensitivityUnits As AIVelocityIepeSensorSensitivityUnits,
	currentExcitationSource As AIExcitationSource,
	currentExcitationValue As Double
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemStringOne or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **units**
  - Type: NationalInstruments.DAQmxAIVelocityUnitsThe units to use to return the measurement.
- **sensitivity**
  - Type: SystemDoubleThe sensitivity of the sensor. This value is in the units you specify with sensitivityUnits. Refer to the sensor documentation to determine this value.
- **sensitivityUnits**
  - Type: NationalInstruments.DAQmxAIVelocityIepeSensorSensitivityUnitsThe units of sensitivity.
- **currentExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSource The source of excitation.
- **currentExcitationValue**
  - Type: SystemDouble The amount of excitation in amperes that the sensor requires.

###### Return Value

AIChannel

AIChannel

##### See Also

###### Reference

AIChannelCollection Class

CreateVelocityIepeChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createvelocityiepechannel_1.htm language=enus -->
## TOPIC 00034: AIChannelCollectionCreateVelocityIepeChannel Method (String, String, AITerminalConfiguration, Double, Double, String, Double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, Double)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createvelocityiepechannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createvelocityiepechannel_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateVelocityIepeChannel Method (String, String, AITerminalConfiguration, Double, Double, String, Double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, Double)

### AIChannelCollectionCreateVelocityIepeChannel Method (String, String, AITerminalConfiguration, Double, Double, String, Double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, Double)

AIChannel

IEPE velocity sensor

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateVelocityIepeChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration terminalConfiguration,
	double minimumValue,
	double maximumValue,
	string customScaleName,
	double sensitivity,
	AIVelocityIepeSensorSensitivityUnits sensitivityUnits,
	AIExcitationSource currentExcitationSource,
	double currentExcitationValue
)
```

```text
Public Function CreateVelocityIepeChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	terminalConfiguration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	customScaleName As String,
	sensitivity As Double,
	sensitivityUnits As AIVelocityIepeSensorSensitivityUnits,
	currentExcitationSource As AIExcitationSource,
	currentExcitationValue As Double
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemStringOne or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **customScaleName**
  - Type: SystemStringThe name of the custom scale to apply to the local virtual channel.
- **sensitivity**
  - Type: SystemDoubleThe sensitivity of the sensor. This value is in the units you specify with sensitivityUnits. Refer to the sensor documentation to determine this value.
- **sensitivityUnits**
  - Type: NationalInstruments.DAQmxAIVelocityIepeSensorSensitivityUnitsThe units of sensitivity.
- **currentExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSource The source of excitation.
- **currentExcitationValue**
  - Type: SystemDouble The amount of excitation in amperes that the sensor requires.

###### Return Value

AIChannel

AIChannel

##### See Also

###### Reference

AIChannelCollection Class

CreateVelocityIepeChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createvoltagechannel_1.htm language=enus -->
## TOPIC 00035: AIChannelCollectionCreateVoltageChannel Method (String, String, AITerminalConfiguration, Double, Double, String)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createvoltagechannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_aichannelcollection_createvoltagechannel_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateVoltageChannel Method (String, String, AITerminalConfiguration, Double, Double, String)

### AIChannelCollectionCreateVoltageChannel Method (String, String, AITerminalConfiguration, Double, Double, String)

AIChannel

measure voltage

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateVoltageChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration terminalConfiguration,
	double minimumValue,
	double maximumValue,
	string customScaleName
)
```

```text
Public Function CreateVoltageChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	terminalConfiguration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	customScaleName As String
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemStringOne or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of -1 casted to an AITerminalConfiguration.
- **minimumValue**
  - Type: SystemDoubleThe minimum value expected from the measurement, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value expected from the measurement, in units.
- **customScaleName**
  - Type: SystemStringThe name of the custom scale to apply to the local virtual channel.

###### Return Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for nameToAssignChannel. If you provide fewer local virtual channel names in nameToAssignChannel than you create, NI-DAQmx [automatically assigns names](/csh?topicname=mxcncpts/;) to the local virtual channels.

If you do not provide a value for nameToAssignChannel, NI-DAQmx uses the physicalChannelName as the local virtual channel name. If you use nameToAssignChannel to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateVoltageChannel(String, String, AITerminalConfiguration, Double, Double, String) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

| Note |
| --- |
| If the measurement requires the use of internal excitation or you need the voltage scaled by the excitation, use CreateVoltageChannelWithExcitation(String, String, AITerminalConfiguration, Double, Double, AIBridgeConfiguration, AIExcitationSource, Double, Boolean, String) instead. |

##### See Also

###### Reference

AIChannelCollection Class

CreateVoltageChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader__ctor.htm language=enus -->
## TOPIC 00036: AnalogMultiChannelReader Constructor

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader__ctor.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader Constructor

### AnalogMultiChannelReader Constructor

AnalogMultiChannelReader

DaqStream

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogMultiChannelReader(
	DaqStream stream
)
```

```text
Public Sub New ( 
	stream As DaqStream
)
```

###### Parameters

- **stream**
  - Type: NationalInstruments.DAQmxDaqStreamThe DaqStream to read.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Task

Stream

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

AnalogMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginmemoryoptimizedreadwaveform.htm language=enus -->
## TOPIC 00037: AnalogMultiChannelReaderBeginMemoryOptimizedReadWaveform Method (Int32, AsyncCallback, Object, AnalogWaveformDouble)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginmemoryoptimizedreadwaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginmemoryoptimizedreadwaveform.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.BeginMemoryOptimizedReadWaveform Method (Int32, AsyncCallback, Object, AnalogWaveform(Double)[])

### AnalogMultiChannelReaderBeginMemoryOptimizedReadWaveform Method (Int32, AsyncCallback, Object, AnalogWaveformDouble)

AIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadWaveform(
	int samplesPerChannel,
	AsyncCallback callback,
	Object state,
	AnalogWaveform<double>[] data
)
```

```text
Public Function BeginMemoryOptimizedReadWaveform ( 
	samplesPerChannel As Integer,
	callback As AsyncCallback,
	state As Object,
	data As AnalogWaveform(Of Double)()
) As IAsyncResult
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: NationalInstrumentsAnalogWaveformDouble An initialized 1D array of AnalogWaveformTData that contains the read data. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing AnalogWaveformTData objects and their corresponding memory to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginMemoryOptimizedReadWaveform(Int32, AsyncCallback, Object, AnalogWaveformDouble), call [EndMemoryOptimizedReadWaveform(IAsyncResult)](m_nationalinstruments_daqmx_analogmultichannelreader_endmemoryoptimizedreadwaveform.htm) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogMultiChannelReader Class

BeginMemoryOptimizedReadWaveform Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginmemoryoptimizedreadwaveform_2.htm language=enus -->
## TOPIC 00038: AnalogMultiChannelReaderBeginMemoryOptimizedReadWaveform Method (TimeSpan, AsyncCallback, Object, AnalogWaveformDouble)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginmemoryoptimizedreadwaveform_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginmemoryoptimizedreadwaveform_2.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.BeginMemoryOptimizedReadWaveform Method (TimeSpan, AsyncCallback, Object, AnalogWaveform(Double)[])

### AnalogMultiChannelReaderBeginMemoryOptimizedReadWaveform Method (TimeSpan, AsyncCallback, Object, AnalogWaveformDouble)

AIChannel

duration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadWaveform(
	TimeSpan duration,
	AsyncCallback callback,
	Object state,
	AnalogWaveform<double>[] data
)
```

```text
Public Function BeginMemoryOptimizedReadWaveform ( 
	duration As TimeSpan,
	callback As AsyncCallback,
	state As Object,
	data As AnalogWaveform(Of Double)()
) As IAsyncResult
```

###### Parameters

- **duration**
  - Type: SystemTimeSpanThe duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: NationalInstrumentsAnalogWaveformDoubleAn initialized 1D array of AnalogWaveformTData that contains the read data. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

data

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, Object, AnalogWaveformDouble), call [EndMemoryOptimizedReadWaveform(IAsyncResult)](m_nationalinstruments_daqmx_analogmultichannelreader_endmemoryoptimizedreadwaveform.htm), passing the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the [Stream](p_nationalinstruments_daqmx_task_stream.htm) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogMultiChannelReader Class

BeginMemoryOptimizedReadWaveform Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginmemoryoptimizedreadwaveform_3.htm language=enus -->
## TOPIC 00039: AnalogMultiChannelReaderBeginMemoryOptimizedReadWaveform Method (TimeSpan, AsyncCallback, Object, AnalogWaveformDouble, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginmemoryoptimizedreadwaveform_3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginmemoryoptimizedreadwaveform_3.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.BeginMemoryOptimizedReadWaveform Method (TimeSpan, AsyncCallback, Object, AnalogWaveform(Double)[], ReallocationPolicy)

### AnalogMultiChannelReaderBeginMemoryOptimizedReadWaveform Method (TimeSpan, AsyncCallback, Object, AnalogWaveformDouble, ReallocationPolicy)

AIChannel

duration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadWaveform(
	TimeSpan duration,
	AsyncCallback callback,
	Object state,
	AnalogWaveform<double>[] data,
	ReallocationPolicy policy
)
```

```text
Public Function BeginMemoryOptimizedReadWaveform ( 
	duration As TimeSpan,
	callback As AsyncCallback,
	state As Object,
	data As AnalogWaveform(Of Double)(),
	policy As ReallocationPolicy
) As IAsyncResult
```

###### Parameters

- **duration**
  - Type: SystemTimeSpanThe duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: NationalInstrumentsAnalogWaveformDoubleAn initialized 1D array of AnalogWaveformTData that contains the read data. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicyDictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

data

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, Object, AnalogWaveformDouble, ReallocationPolicy), call [EndMemoryOptimizedReadWaveform(IAsyncResult)](m_nationalinstruments_daqmx_analogmultichannelreader_endmemoryoptimizedreadwaveform.htm), passing the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the [Stream](p_nationalinstruments_daqmx_task_stream.htm) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogMultiChannelReader Class

BeginMemoryOptimizedReadWaveform Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginreadsinglesample.htm language=enus -->
## TOPIC 00040: AnalogMultiChannelReaderBeginReadSingleSample Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginreadsinglesample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginreadsinglesample.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.BeginReadSingleSample Method

### AnalogMultiChannelReaderBeginReadSingleSample Method

AIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadSingleSample(
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadSingleSample ( 
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSample(AsyncCallback, Object), call [EndReadSingleSample(IAsyncResult)](m_nationalinstruments_daqmx_analogmultichannelreader_endreadsinglesample.htm) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginreadwaveform_1.htm language=enus -->
## TOPIC 00041: AnalogMultiChannelReaderBeginReadWaveform Method (TimeSpan, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginreadwaveform_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginreadwaveform_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.BeginReadWaveform Method (TimeSpan, AsyncCallback, Object)

### AnalogMultiChannelReaderBeginReadWaveform Method (TimeSpan, AsyncCallback, Object)

AIChannel

duration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadWaveform(
	TimeSpan duration,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadWaveform ( 
	duration As TimeSpan,
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **duration**
  - Type: SystemTimeSpanThe duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

BeginReadWaveform(TimeSpan, AsyncCallback, Object)

EndReadWaveform(IAsyncResult)

IAsyncResult

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the [Stream](p_nationalinstruments_daqmx_task_stream.htm) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogMultiChannelReader Class

BeginReadWaveform Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_endmemoryoptimizedreadmultisample.htm language=enus -->
## TOPIC 00042: AnalogMultiChannelReaderEndMemoryOptimizedReadMultiSample Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_endmemoryoptimizedreadmultisample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_endmemoryoptimizedreadmultisample.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.EndMemoryOptimizedReadMultiSample Method

### AnalogMultiChannelReaderEndMemoryOptimizedReadMultiSample Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[,] EndMemoryOptimizedReadMultiSample(
	IAsyncResult asyncResult,
	out int actualNumberOfSamplesPerChannelRead
)
```

```text
Public Function EndMemoryOptimizedReadMultiSample ( 
	asyncResult As IAsyncResult,
	<OutAttribute> ByRef actualNumberOfSamplesPerChannelRead As Integer
) As Double(,)
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResult An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSample(Int32, AsyncCallback, Object, Double).
- **actualNumberOfSamplesPerChannelRead**
  - Type: SystemInt32The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

Double

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; orFor asynchronous reads, if asyncResult is or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSample(Int32, AsyncCallback, Object, Double). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call
 this method 
 before the asynchronous read
 IAsyncResult
 is complete,
 it 
 waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
 [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
 [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
 property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_endmemoryoptimizedreadwaveform.htm language=enus -->
## TOPIC 00043: AnalogMultiChannelReaderEndMemoryOptimizedReadWaveform Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_endmemoryoptimizedreadwaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_endmemoryoptimizedreadwaveform.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.EndMemoryOptimizedReadWaveform Method

### AnalogMultiChannelReaderEndMemoryOptimizedReadWaveform Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogWaveform<double>[] EndMemoryOptimizedReadWaveform(
	IAsyncResult asyncResult
)
```

```text
Public Function EndMemoryOptimizedReadWaveform ( 
	asyncResult As IAsyncResult
) As AnalogWaveform(Of Double)()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadWaveform(Int32, AsyncCallback, Object, AnalogWaveformDouble)

###### Return Value

AnalogWaveform

Double

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If the first dimension of data does not match the number of channels. If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples.For asynchronous reads, if asyncResult is or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadWaveform(Int32, AsyncCallback, Object, AnalogWaveformDouble).For reads that take a TimeSpan duration, if the duration provided was less than Zero. |
| DaqException | If data is or is uninitialized.If one of the elements of data is .The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndMemoryOptimizedReadWaveform(IAsyncResult) before the asynchronous read IAsyncResult
 is complete,
 EndMemoryOptimizedReadWaveform(IAsyncResult)
 waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
 [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
 [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
 property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_endreadmultisample.htm language=enus -->
## TOPIC 00044: AnalogMultiChannelReaderEndReadMultiSample Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_endreadmultisample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_endreadmultisample.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.EndReadMultiSample Method

### AnalogMultiChannelReaderEndReadMultiSample Method

BeginReadMultiSample(Int32, AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[,] EndReadMultiSample(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadMultiSample ( 
	asyncResult As IAsyncResult
) As Double(,)
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSample(Int32, AsyncCallback, Object) .

###### Return Value

Double

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSample(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadMultiSample(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSample(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_endreadsinglesample.htm language=enus -->
## TOPIC 00045: AnalogMultiChannelReaderEndReadSingleSample Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_endreadsinglesample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_endreadsinglesample.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.EndReadSingleSample Method

### AnalogMultiChannelReaderEndReadSingleSample Method

BeginReadSingleSample(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] EndReadSingleSample(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadSingleSample ( 
	asyncResult As IAsyncResult
) As Double()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSample(AsyncCallback, Object).

###### Return Value

Double

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadSingleSample(AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSample(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSample(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_endreadwaveform.htm language=enus -->
## TOPIC 00046: AnalogMultiChannelReaderEndReadWaveform Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_endreadwaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_endreadwaveform.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.EndReadWaveform Method

### AnalogMultiChannelReaderEndReadWaveform Method

BeginReadWaveform(Int32, AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogWaveform<double>[] EndReadWaveform(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadWaveform ( 
	asyncResult As IAsyncResult
) As AnalogWaveform(Of Double)()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadWaveform(Int32, AsyncCallback, Object).

###### Return Value

AnalogWaveform

Double

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadWaveform(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadWaveform(IAsyncResult) before the asynchronous read IAsyncResult is complete, [EndReadWaveform(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelreader_endreadwaveform.htm) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadmultisample.htm language=enus -->
## TOPIC 00047: AnalogMultiChannelReaderMemoryOptimizedReadMultiSample Method (Int32, Double, ReallocationPolicy, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadmultisample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadmultisample.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.MemoryOptimizedReadMultiSample Method (Int32, Double[,], ReallocationPolicy, Int32)

### AnalogMultiChannelReaderMemoryOptimizedReadMultiSample Method (Int32, Double, ReallocationPolicy, Int32)

AIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[,] MemoryOptimizedReadMultiSample(
	int samplesPerChannel,
	ref double[,] data,
	ReallocationPolicy policy,
	out int actualNumberOfSamplesPerChannelRead
)
```

```text
Public Function MemoryOptimizedReadMultiSample ( 
	samplesPerChannel As Integer,
	ByRef data As Double(,),
	policy As ReallocationPolicy,
	<OutAttribute> ByRef actualNumberOfSamplesPerChannelRead As Integer
) As Double(,)
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: SystemDoubleAn initialized 2D array of floating-point samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicyDictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.
- **actualNumberOfSamplesPerChannelRead**
  - Type: SystemInt32The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

Double

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

AnalogMultiChannelReader Class

MemoryOptimizedReadMultiSample Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadmultisample_1.htm language=enus -->
## TOPIC 00048: AnalogMultiChannelReaderMemoryOptimizedReadMultiSample Method (Int32, Double, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadmultisample_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadmultisample_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.MemoryOptimizedReadMultiSample Method (Int32, Double[,], Int32)

### AnalogMultiChannelReaderMemoryOptimizedReadMultiSample Method (Int32, Double, Int32)

AIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[,] MemoryOptimizedReadMultiSample(
	int samplesPerChannel,
	ref double[,] data,
	out int actualNumberOfSamplesPerChannelRead
)
```

```text
Public Function MemoryOptimizedReadMultiSample ( 
	samplesPerChannel As Integer,
	ByRef data As Double(,),
	<OutAttribute> ByRef actualNumberOfSamplesPerChannelRead As Integer
) As Double(,)
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: SystemDoubleAn initialized 2D array of floating-point samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.
- **actualNumberOfSamplesPerChannelRead**
  - Type: SystemInt32The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

Double

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html)
.

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

AnalogMultiChannelReader Class

MemoryOptimizedReadMultiSample Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadwaveform.htm language=enus -->
## TOPIC 00049: AnalogMultiChannelReaderMemoryOptimizedReadWaveform Method (Int32, AnalogWaveformDouble)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadwaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadwaveform.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.MemoryOptimizedReadWaveform Method (Int32, AnalogWaveform(Double)[])

### AnalogMultiChannelReaderMemoryOptimizedReadWaveform Method (Int32, AnalogWaveformDouble)

AIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogWaveform<double>[] MemoryOptimizedReadWaveform(
	int samplesPerChannel,
	AnalogWaveform<double>[] data
)
```

```text
Public Function MemoryOptimizedReadWaveform ( 
	samplesPerChannel As Integer,
	data As AnalogWaveform(Of Double)()
) As AnalogWaveform(Of Double)()
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: NationalInstrumentsAnalogWaveformDouble An initialized 1D array of AnalogWaveformTData that contains the read data. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.

###### Return Value

AnalogWaveform

Double

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing AnalogWaveformTData objects and their corresponding memory to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

AnalogMultiChannelReader Class

MemoryOptimizedReadWaveform Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadwaveform_1.htm language=enus -->
## TOPIC 00050: AnalogMultiChannelReaderMemoryOptimizedReadWaveform Method (Int32, AnalogWaveformDouble, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadwaveform_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadwaveform_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.MemoryOptimizedReadWaveform Method (Int32, AnalogWaveform(Double)[], ReallocationPolicy)

### AnalogMultiChannelReaderMemoryOptimizedReadWaveform Method (Int32, AnalogWaveformDouble, ReallocationPolicy)

AIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogWaveform<double>[] MemoryOptimizedReadWaveform(
	int samplesPerChannel,
	AnalogWaveform<double>[] data,
	ReallocationPolicy policy
)
```

```text
Public Function MemoryOptimizedReadWaveform ( 
	samplesPerChannel As Integer,
	data As AnalogWaveform(Of Double)(),
	policy As ReallocationPolicy
) As AnalogWaveform(Of Double)()
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: NationalInstrumentsAnalogWaveformDouble An initialized 1D array of AnalogWaveformTData that contains the read data. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicyDictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.

###### Return Value

AnalogWaveform

Double

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing
 AnalogWaveformTData
 objects and their corresponding memory to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
 [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

The data returned from analog waveform reads is affected by the
 [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm)
 property of the
 [DaqStream](t_nationalinstruments_daqmx_daqstream.htm)
 you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the
 [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
 property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

AnalogMultiChannelReader Class

MemoryOptimizedReadWaveform Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadwaveform_2.htm language=enus -->
## TOPIC 00051: AnalogMultiChannelReaderMemoryOptimizedReadWaveform Method (TimeSpan, AnalogWaveformDouble)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadwaveform_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadwaveform_2.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.MemoryOptimizedReadWaveform Method (TimeSpan, AnalogWaveform(Double)[])

### AnalogMultiChannelReaderMemoryOptimizedReadWaveform Method (TimeSpan, AnalogWaveformDouble)

AIChannel

duration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogWaveform<double>[] MemoryOptimizedReadWaveform(
	TimeSpan duration,
	AnalogWaveform<double>[] data
)
```

```text
Public Function MemoryOptimizedReadWaveform ( 
	duration As TimeSpan,
	data As AnalogWaveform(Of Double)()
) As AnalogWaveform(Of Double)()
```

###### Parameters

- **duration**
  - Type: SystemTimeSpanThe duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate.
- **data**
  - Type: NationalInstrumentsAnalogWaveformDoubleAn initialized 1D array of AnalogWaveformTData that contains the read data. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.

###### Return Value

AnalogWaveform

Double

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If the first dimension of data does not match the number of channels. If the duration provided was less than Zero. |
| DaqException | If data is or is uninitialized.If one of the elements of data is .The NI-DAQmx driver returned an error. |

##### Remarks

data

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the [Stream](p_nationalinstruments_daqmx_task_stream.htm) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

AnalogMultiChannelReader Class

MemoryOptimizedReadWaveform Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadwaveform_3.htm language=enus -->
## TOPIC 00052: AnalogMultiChannelReaderMemoryOptimizedReadWaveform Method (TimeSpan, AnalogWaveformDouble, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadwaveform_3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_memoryoptimizedreadwaveform_3.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.MemoryOptimizedReadWaveform Method (TimeSpan, AnalogWaveform(Double)[], ReallocationPolicy)

### AnalogMultiChannelReaderMemoryOptimizedReadWaveform Method (TimeSpan, AnalogWaveformDouble, ReallocationPolicy)

AIChannel

duration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogWaveform<double>[] MemoryOptimizedReadWaveform(
	TimeSpan duration,
	AnalogWaveform<double>[] data,
	ReallocationPolicy policy
)
```

```text
Public Function MemoryOptimizedReadWaveform ( 
	duration As TimeSpan,
	data As AnalogWaveform(Of Double)(),
	policy As ReallocationPolicy
) As AnalogWaveform(Of Double)()
```

###### Parameters

- **duration**
  - Type: SystemTimeSpanThe duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate.
- **data**
  - Type: NationalInstrumentsAnalogWaveformDoubleAn initialized 1D array of AnalogWaveformTData that contains the read data. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicyDictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.

###### Return Value

AnalogWaveform

Double

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If the first dimension of data does not match the number of channels. If the duration provided was less than Zero. If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| DaqException | If data is or is uninitialized.If one of the elements of data is .The NI-DAQmx driver returned an error. |

##### Remarks

data

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the [Stream](p_nationalinstruments_daqmx_task_stream.htm) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

AnalogMultiChannelReader Class

MemoryOptimizedReadWaveform Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_readmultisample.htm language=enus -->
## TOPIC 00053: AnalogMultiChannelReaderReadMultiSample Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_readmultisample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_readmultisample.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.ReadMultiSample Method

### AnalogMultiChannelReaderReadMultiSample Method

AIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[,] ReadMultiSample(
	int samplesPerChannel
)
```

```text
Public Function ReadMultiSample ( 
	samplesPerChannel As Integer
) As Double(,)
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.

###### Return Value

Double

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

AnalogMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_readsinglesample.htm language=enus -->
## TOPIC 00054: AnalogMultiChannelReaderReadSingleSample Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_readsinglesample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_readsinglesample.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.ReadSingleSample Method

### AnalogMultiChannelReaderReadSingleSample Method

AIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] ReadSingleSample()
```

```text
Public Function ReadSingleSample As Double()
```

###### Return Value

Double

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

DAQ Assistant

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

AnalogMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_readwaveform.htm language=enus -->
## TOPIC 00055: AnalogMultiChannelReaderReadWaveform Method (Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_readwaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_readwaveform.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.ReadWaveform Method (Int32)

### AnalogMultiChannelReaderReadWaveform Method (Int32)

AIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogWaveform<double>[] ReadWaveform(
	int samplesPerChannel
)
```

```text
Public Function ReadWaveform ( 
	samplesPerChannel As Integer
) As AnalogWaveform(Of Double)()
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.

###### Return Value

AnalogWaveform

Double

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

AnalogMultiChannelReader Class

ReadWaveform Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_readwaveform_1.htm language=enus -->
## TOPIC 00056: AnalogMultiChannelReaderReadWaveform Method (TimeSpan)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_readwaveform_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_readwaveform_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.ReadWaveform Method (TimeSpan)

### AnalogMultiChannelReaderReadWaveform Method (TimeSpan)

AIChannel

duration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogWaveform<double>[] ReadWaveform(
	TimeSpan duration
)
```

```text
Public Function ReadWaveform ( 
	duration As TimeSpan
) As AnalogWaveform(Of Double)()
```

###### Parameters

- **duration**
  - Type: SystemTimeSpanThe duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate.

###### Return Value

AnalogWaveform

Double

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If the duration provided was less than Zero. |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

DAQ Assistant

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the [Stream](p_nationalinstruments_daqmx_task_stream.htm) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

AnalogMultiChannelReader Class

ReadWaveform Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_tostring.htm language=enus -->
## TOPIC 00057: AnalogMultiChannelReaderToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.ToString Method

### AnalogMultiChannelReaderToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

AnalogMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_endwrite.htm language=enus -->
## TOPIC 00058: AnalogMultiChannelWriterEndWrite Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_endwrite.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_endwrite.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelWriter.EndWrite Method

### AnalogMultiChannelWriterEndWrite Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void EndWrite(
	IAsyncResult asyncResult
)
```

```text
Public Sub EndWrite ( 
	asyncResult As IAsyncResult
)
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginWriteMultiSample(Boolean, Double, AsyncCallback, Object) or BeginWriteSingleSample(Boolean, Double, AsyncCallback, Object).

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginWriteMultiSample(Boolean, Double, AsyncCallback, Object) or BeginWriteSingleSample(Boolean, Double, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| IndexOutOfRangeException | The data provided to BeginWriteMultiSample(Boolean, Double, AsyncCallback, Object) or BeginWriteSingleSample(Boolean, Double, AsyncCallback, Object) has a non-zero lower bound. |

##### Remarks

If you call EndWrite(IAsyncResult) before the asynchronous write represented by the provided IAsyncResult is complete, EndWrite(IAsyncResult) waits for the write to complete before returning. For a write to a buffered task, the write is considered complete when all of the written samples have been transferred to the task buffer. Use [IsDone](p_nationalinstruments_daqmx_task_isdone.htm) or [WaitUntilDone(TimeSpan)](m_nationalinstruments_daqmx_task_waituntildone_2.htm) on the [Task](t_nationalinstruments_daqmx_task.htm) object to determine if a task has generated all of the data it was configured to generate.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_writewaveform__1.htm language=enus -->
## TOPIC 00059: AnalogMultiChannelWriterWriteWaveformTData Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_writewaveform__1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_writewaveform__1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelWriter.WriteWaveform(TData) Method

### AnalogMultiChannelWriterWriteWaveformTData Method

AOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteWaveform<TData>(
	bool autoStart,
	AnalogWaveform<TData>[] data
)
```

```text
Public Sub WriteWaveform(Of TData) ( 
	autoStart As Boolean,
	data As AnalogWaveform(Of TData)()
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If you set autoStart to , WriteWaveform automatically calls Start if you do not explicitly call Start. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: NationalInstrumentsAnalogWaveformTDataA 1D array of AnalogWaveformTData objects to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. The order of the lines in the analog waveform corresponds to the order in which you add the lines to the channel.

###### Type Parameters

- **TData**
  - The type of the analog waveform samples.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

##### Remarks

WriteWaveform

WriteWaveform

Analog waveform writes are not affected by the SampleInterval or StartTime properties on AnalogWaveformTData. To configure timing for analog waveform writes, use the [ConfigureSampleClock(String, Double, SampleClockActiveEdge, SampleQuantityMode, Int32)](m_nationalinstruments_daqmx_timing_configuresampleclock_1.htm) method.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

AnalogMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultiedgereferencetrigger_tostring.htm language=enus -->
## TOPIC 00060: AnalogMultiEdgeReferenceTriggerToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultiedgereferencetrigger_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultiedgereferencetrigger_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiEdgeReferenceTrigger.ToString Method

### AnalogMultiEdgeReferenceTriggerToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### See Also

###### Reference

AnalogMultiEdgeReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultiedgestarttrigger_tostring.htm language=enus -->
## TOPIC 00061: AnalogMultiEdgeStartTriggerToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultiedgestarttrigger_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogmultiedgestarttrigger_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiEdgeStartTrigger.ToString Method

### AnalogMultiEdgeStartTriggerToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### See Also

###### Reference

AnalogMultiEdgeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader__ctor.htm language=enus -->
## TOPIC 00062: AnalogSingleChannelReader Constructor

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader__ctor.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelReader Constructor

### AnalogSingleChannelReader Constructor

AnalogSingleChannelReader

DaqStream

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogSingleChannelReader(
	DaqStream stream
)
```

```text
Public Sub New ( 
	stream As DaqStream
)
```

###### Parameters

- **stream**
  - Type: NationalInstruments.DAQmxDaqStreamThe DaqStream to read.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Task

Stream

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

AnalogSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_beginmemoryoptimizedreadmultisample.htm language=enus -->
## TOPIC 00063: AnalogSingleChannelReaderBeginMemoryOptimizedReadMultiSample Method (Int32, AsyncCallback, Object, Double)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_beginmemoryoptimizedreadmultisample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_beginmemoryoptimizedreadmultisample.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelReader.BeginMemoryOptimizedReadMultiSample Method (Int32, AsyncCallback, Object, Double[])

### AnalogSingleChannelReaderBeginMemoryOptimizedReadMultiSample Method (Int32, AsyncCallback, Object, Double)

AIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual IAsyncResult BeginMemoryOptimizedReadMultiSample(
	int numberOfSamples,
	AsyncCallback callback,
	Object state,
	double[] data
)
```

```text
Public Overridable Function BeginMemoryOptimizedReadMultiSample ( 
	numberOfSamples As Integer,
	callback As AsyncCallback,
	state As Object,
	data As Double()
) As IAsyncResult
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32The number of samples to read. If you set numberOfSamples to 1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to 1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. Setting numberOfSamples to 1 returns all available samples or 2 31 1 samples, whichever is smaller.
- **callback**
  - Type: SystemAsyncCallback An optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObject A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemDoubleAn initialized 1D array of floating-point samples that contains the read data. Each element in the array corresponds to a sample from the channel.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
 this method, call [EndMemoryOptimizedReadMultiSample(IAsyncResult, Int32)](m_nationalinstruments_daqmx_analogsinglechannelreader_endmemoryoptimizedreadmultisample.htm)
 with the returned
 IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

AnalogSingleChannelReader Class

BeginMemoryOptimizedReadMultiSample Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_beginmemoryoptimizedreadmultisample_1.htm language=enus -->
## TOPIC 00064: AnalogSingleChannelReaderBeginMemoryOptimizedReadMultiSample Method (Int32, AsyncCallback, Object, Double, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_beginmemoryoptimizedreadmultisample_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_beginmemoryoptimizedreadmultisample_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelReader.BeginMemoryOptimizedReadMultiSample Method (Int32, AsyncCallback, Object, Double[], ReallocationPolicy)

### AnalogSingleChannelReaderBeginMemoryOptimizedReadMultiSample Method (Int32, AsyncCallback, Object, Double, ReallocationPolicy)

AIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual IAsyncResult BeginMemoryOptimizedReadMultiSample(
	int numberOfSamples,
	AsyncCallback callback,
	Object state,
	double[] data,
	ReallocationPolicy policy
)
```

```text
Public Overridable Function BeginMemoryOptimizedReadMultiSample ( 
	numberOfSamples As Integer,
	callback As AsyncCallback,
	state As Object,
	data As Double(),
	policy As ReallocationPolicy
) As IAsyncResult
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallback An optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObject A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemDoubleAn initialized 1D array of floating-point samples that contains the read data. Each element in the array corresponds to a sample from the channel.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicyDictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
 this method, call [EndMemoryOptimizedReadMultiSample(IAsyncResult, Int32)](m_nationalinstruments_daqmx_analogsinglechannelreader_endmemoryoptimizedreadmultisample.htm)
 with the returned
 IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

AnalogSingleChannelReader Class

BeginMemoryOptimizedReadMultiSample Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_endmemoryoptimizedreadmultisample.htm language=enus -->
## TOPIC 00065: AnalogSingleChannelReaderEndMemoryOptimizedReadMultiSample Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_endmemoryoptimizedreadmultisample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_endmemoryoptimizedreadmultisample.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelReader.EndMemoryOptimizedReadMultiSample Method

### AnalogSingleChannelReaderEndMemoryOptimizedReadMultiSample Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual double[] EndMemoryOptimizedReadMultiSample(
	IAsyncResult asyncResult,
	out int actualNumberOfSamplesRead
)
```

```text
Public Overridable Function EndMemoryOptimizedReadMultiSample ( 
	asyncResult As IAsyncResult,
	<OutAttribute> ByRef actualNumberOfSamplesRead As Integer
) As Double()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResult An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSample(Int32, AsyncCallback, Object, Double).
- **actualNumberOfSamplesRead**
  - Type: SystemInt32The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; orFor asynchronous reads, if asyncResult is or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSample(Int32, AsyncCallback, Object, Double). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call
 this method
 before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
 [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
 [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
 property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_endmemoryoptimizedreadwaveform.htm language=enus -->
## TOPIC 00066: AnalogSingleChannelReaderEndMemoryOptimizedReadWaveform Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_endmemoryoptimizedreadwaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_endmemoryoptimizedreadwaveform.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelReader.EndMemoryOptimizedReadWaveform Method

### AnalogSingleChannelReaderEndMemoryOptimizedReadWaveform Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual AnalogWaveform<double> EndMemoryOptimizedReadWaveform(
	IAsyncResult asyncResult
)
```

```text
Public Overridable Function EndMemoryOptimizedReadWaveform ( 
	asyncResult As IAsyncResult
) As AnalogWaveform(Of Double)
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResult An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadWaveform(Int32, AsyncCallback, Object, AnalogWaveformDouble).

###### Return Value

AnalogWaveform

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples.For asynchronous reads, if asyncResult is or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadWaveform(Int32, AsyncCallback, Object, AnalogWaveformDouble).For reads that take a TimeSpan duration, if the duration provided was less than Zero. |
| DaqException | If data is or is uninitialized.The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call
 EndMemoryOptimizedReadWaveform(IAsyncResult)
 before the asynchronous read is complete,
 EndMemoryOptimizedReadWaveform(IAsyncResult)
 waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
 [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
 [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
 property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_endreadmultisample.htm language=enus -->
## TOPIC 00067: AnalogSingleChannelReaderEndReadMultiSample Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_endreadmultisample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_endreadmultisample.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelReader.EndReadMultiSample Method

### AnalogSingleChannelReaderEndReadMultiSample Method

BeginReadMultiSample(Int32, AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual double[] EndReadMultiSample(
	IAsyncResult asyncResult
)
```

```text
Public Overridable Function EndReadMultiSample ( 
	asyncResult As IAsyncResult
) As Double()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSample(Int32, AsyncCallback, Object).

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSample(Int32, AsyncCallback, Object) . |
| OutOfMemoryException | There is not enough memory to carry out this operation. |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |

##### Remarks

If you call EndReadMultiSample(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSample(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_endreadsinglesample.htm language=enus -->
## TOPIC 00068: AnalogSingleChannelReaderEndReadSingleSample Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_endreadsinglesample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_endreadsinglesample.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelReader.EndReadSingleSample Method

### AnalogSingleChannelReaderEndReadSingleSample Method

BeginReadSingleSample(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual double EndReadSingleSample(
	IAsyncResult asyncResult
)
```

```text
Public Overridable Function EndReadSingleSample ( 
	asyncResult As IAsyncResult
) As Double
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSample(AsyncCallback, Object).

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadSingleSample(AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSample(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSample(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_memoryoptimizedreadmultisample.htm language=enus -->
## TOPIC 00069: AnalogSingleChannelReaderMemoryOptimizedReadMultiSample Method (Int32, Double, ReallocationPolicy, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_memoryoptimizedreadmultisample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_memoryoptimizedreadmultisample.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelReader.MemoryOptimizedReadMultiSample Method (Int32, Double[], ReallocationPolicy, Int32)

### AnalogSingleChannelReaderMemoryOptimizedReadMultiSample Method (Int32, Double, ReallocationPolicy, Int32)

AIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual double[] MemoryOptimizedReadMultiSample(
	int numberOfSamples,
	ref double[] data,
	ReallocationPolicy policy,
	out int actualNumberOfSamplesRead
)
```

```text
Public Overridable Function MemoryOptimizedReadMultiSample ( 
	numberOfSamples As Integer,
	ByRef data As Double(),
	policy As ReallocationPolicy,
	<OutAttribute> ByRef actualNumberOfSamplesRead As Integer
) As Double()
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: SystemDoubleAn initialized 1D array of floating-point samples that contains the read data. Each element in the array corresponds to a sample from the channel.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicyDictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.
- **actualNumberOfSamplesRead**
  - Type: SystemInt32The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

Double

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

AnalogSingleChannelReader Class

MemoryOptimizedReadMultiSample Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelwriter_beginwritemultisample.htm language=enus -->
## TOPIC 00070: AnalogSingleChannelWriterBeginWriteMultiSample Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelwriter_beginwritemultisample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_analogsinglechannelwriter_beginwritemultisample.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelWriter.BeginWriteMultiSample Method

### AnalogSingleChannelWriterBeginWriteMultiSample Method

AOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteMultiSample(
	bool autoStart,
	double[] data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteMultiSample ( 
	autoStart As Boolean,
	data As Double(),
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemDoubleA 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_analogsinglechannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogSingleChannelWriter Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_cidatafrequency_equals.htm language=enus -->
## TOPIC 00071: CIDataFrequencyEquals Method (CIDataFrequency)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_cidatafrequency_equals.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_cidatafrequency_equals.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataFrequency.Equals Method (CIDataFrequency)

### CIDataFrequencyEquals Method (CIDataFrequency)

CIDataFrequency

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool Equals(
	CIDataFrequency c
)
```

```text
Public Function Equals ( 
	c As CIDataFrequency
) As Boolean
```

###### Parameters

- **c**
  - Type: NationalInstruments.DAQmxCIDataFrequencyA CIDataFrequency to compare with this instance.

###### Return Value

Boolean

c

##### See Also

###### Reference

CIDataFrequency Structure

Equals Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_cidataticks__ctor_1.htm language=enus -->
## TOPIC 00072: CIDataTicks Constructor (UInt32, UInt32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_cidataticks__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_cidataticks__ctor_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataTicks Constructor (UInt32, UInt32)

### CIDataTicks Constructor (UInt32, UInt32)

CIDataTicks

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIDataTicks(
	uint lowTicks,
	uint highTicks
)
```

```text
Public Sub New ( 
	lowTicks As UInteger,
	highTicks As UInteger
)
```

###### Parameters

- **lowTicks**
  - Type: SystemUInt32The number of timebase ticks the pulse is low.
- **highTicks**
  - Type: SystemUInt32The number of timebase ticks the pulse is high.

##### See Also

###### Reference

CIDataTicks Structure

CIDataTicks Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_cidataticks_gethashcode.htm language=enus -->
## TOPIC 00073: CIDataTicksGetHashCode Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_cidataticks_gethashcode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_cidataticks_gethashcode.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataTicks.GetHashCode Method

### CIDataTicksGetHashCode Method

CIDataTicks

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override sealed int GetHashCode()
```

```text
Public Overrides NotOverridable Function GetHashCode As Integer
```

###### Return Value

Int32

##### Remarks

CIDataTicks

##### See Also

###### Reference

CIDataTicks Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_cidataticks_getobjectdata.htm language=enus -->
## TOPIC 00074: CIDataTicksGetObjectData Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_cidataticks_getobjectdata.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_cidataticks_getobjectdata.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataTicks.GetObjectData Method

### CIDataTicksGetObjectData Method

SerializationInfo

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void GetObjectData(
	SerializationInfo info,
	StreamingContext context
)
```

```text
Public Sub GetObjectData ( 
	info As SerializationInfo,
	context As StreamingContext
)
```

###### Parameters

- **info**
  - Type: System.Runtime.SerializationSerializationInfo Object that holds the serialized object data.
- **context**
  - Type: System.Runtime.SerializationStreamingContext Contextual information about the source or destination.

###### Implements

##### See Also

###### Reference

CIDataTicks Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginmemoryoptimizedreadmultisampledouble.htm language=enus -->
## TOPIC 00075: CounterSingleChannelReaderBeginMemoryOptimizedReadMultiSampleDouble Method (Int32, AsyncCallback, Object, Double)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginmemoryoptimizedreadmultisampledouble.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginmemoryoptimizedreadmultisampledouble.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.BeginMemoryOptimizedReadMultiSampleDouble Method (Int32, AsyncCallback, Object, Double[])

### CounterSingleChannelReaderBeginMemoryOptimizedReadMultiSampleDouble Method (Int32, AsyncCallback, Object, Double)

Double

CIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadMultiSampleDouble(
	int numberOfSamples,
	AsyncCallback callback,
	Object state,
	double[] data
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSampleDouble ( 
	numberOfSamples As Integer,
	callback As AsyncCallback,
	state As Object,
	data As Double()
) As IAsyncResult
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemDoubleAn initialized 1D array of Double samples that contains the read data. Each element in the array corresponds to a sample from the channel.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. The memory allocation for the buffer is available to a maximum of 2 GB.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSampleDouble(IAsyncResult, Int32)](m_nationalinstruments_daqmx_countersinglechannelreader_endmemoryoptimizedreadmultisampledouble.htm) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

CounterSingleChannelReader Class

BeginMemoryOptimizedReadMultiSampleDouble Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginmemoryoptimizedreadmultisampleint32.htm language=enus -->
## TOPIC 00076: CounterSingleChannelReaderBeginMemoryOptimizedReadMultiSampleInt32 Method (Int32, AsyncCallback, Object, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginmemoryoptimizedreadmultisampleint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginmemoryoptimizedreadmultisampleint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.BeginMemoryOptimizedReadMultiSampleInt32 Method (Int32, AsyncCallback, Object, Int32[])

### CounterSingleChannelReaderBeginMemoryOptimizedReadMultiSampleInt32 Method (Int32, AsyncCallback, Object, Int32)

Int32

CIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadMultiSampleInt32(
	int numberOfSamples,
	AsyncCallback callback,
	Object state,
	int[] data
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSampleInt32 ( 
	numberOfSamples As Integer,
	callback As AsyncCallback,
	state As Object,
	data As Integer()
) As IAsyncResult
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemInt32An initialized 1D array of Int32 samples that contains the read data. Each element in the array corresponds to a sample from the channel.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. The memory allocation for the buffer is available to a maximum of 2 GB.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult, Int32)](m_nationalinstruments_daqmx_countersinglechannelreader_endmemoryoptimizedreadmultisampleint32.htm) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

CounterSingleChannelReader Class

BeginMemoryOptimizedReadMultiSampleInt32 Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginmemoryoptimizedreadmultisampleint32_1.htm language=enus -->
## TOPIC 00077: CounterSingleChannelReaderBeginMemoryOptimizedReadMultiSampleInt32 Method (Int32, AsyncCallback, Object, Int32, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginmemoryoptimizedreadmultisampleint32_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginmemoryoptimizedreadmultisampleint32_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.BeginMemoryOptimizedReadMultiSampleInt32 Method (Int32, AsyncCallback, Object, Int32[], ReallocationPolicy)

### CounterSingleChannelReaderBeginMemoryOptimizedReadMultiSampleInt32 Method (Int32, AsyncCallback, Object, Int32, ReallocationPolicy)

Int32

CIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadMultiSampleInt32(
	int numberOfSamples,
	AsyncCallback callback,
	Object state,
	int[] data,
	ReallocationPolicy policy
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSampleInt32 ( 
	numberOfSamples As Integer,
	callback As AsyncCallback,
	state As Object,
	data As Integer(),
	policy As ReallocationPolicy
) As IAsyncResult
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemInt32An initialized 1D array of Int32 samples that contains the read data. Each element in the array corresponds to a sample from the channel.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicyDictates the reallocation behavior of the data. Refer to ReallocationPolicy for more information.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

When performing an asynchronous memory-optimized read, the size of the data buffer dynamically increases if the number of samples read exceeds the existing buffer and [ReallocationPolicy](t_nationalinstruments_daqmx_reallocationpolicy.htm) is [ToGrow](t_nationalinstruments_daqmx_reallocationpolicy.htm). 
This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. 
An ArgumentException is thrown if the buffer is not capable of holding the data and [ReallocationPolicy](t_nationalinstruments_daqmx_reallocationpolicy.htm) is [DoNotReallocate](t_nationalinstruments_daqmx_reallocationpolicy.htm).

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult, Int32)](m_nationalinstruments_daqmx_countersinglechannelreader_endmemoryoptimizedreadmultisampleint32.htm) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

CounterSingleChannelReader Class

BeginMemoryOptimizedReadMultiSampleInt32 Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginreadsinglesampleint32.htm language=enus -->
## TOPIC 00078: CounterSingleChannelReaderBeginReadSingleSampleInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginreadsinglesampleint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginreadsinglesampleint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.BeginReadSingleSampleInt32 Method

### CounterSingleChannelReaderBeginReadSingleSampleInt32 Method

Begins an asynchronous read of a 32-bit integer sample from a counter task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadSingleSampleInt32(
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadSingleSampleInt32 ( 
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSampleInt32(AsyncCallback, Object), call [EndReadSingleSampleInt32(IAsyncResult)](m_nationalinstruments_daqmx_countersinglechannelreader_endreadsinglesampleint32.htm) with the returned IAsyncResult.

Use this method when counter samples are returned unscaled, such as for event counting.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginreadsinglesamplepulsefrequency.htm language=enus -->
## TOPIC 00079: CounterSingleChannelReaderBeginReadSingleSamplePulseFrequency Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginreadsinglesamplepulsefrequency.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginreadsinglesamplepulsefrequency.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.BeginReadSingleSamplePulseFrequency Method

### CounterSingleChannelReaderBeginReadSingleSamplePulseFrequency Method

Begins an asynchronous read of a single pulse sample in terms of frequency from a counter task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadSingleSamplePulseFrequency(
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadSingleSamplePulseFrequency ( 
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePulseFrequency(AsyncCallback, Object), call [EndReadSingleSamplePulseFrequency(IAsyncResult)](m_nationalinstruments_daqmx_countersinglechannelreader_endreadsinglesamplepulsefrequency.htm) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginreadsinglesamplepulseticks.htm language=enus -->
## TOPIC 00080: CounterSingleChannelReaderBeginReadSingleSamplePulseTicks Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginreadsinglesamplepulseticks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginreadsinglesamplepulseticks.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.BeginReadSingleSamplePulseTicks Method

### CounterSingleChannelReaderBeginReadSingleSamplePulseTicks Method

Begins an asynchronous read of a single pulse sample in terms of ticks from a counter task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadSingleSamplePulseTicks(
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadSingleSamplePulseTicks ( 
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePulseTicks(AsyncCallback, Object), call [EndReadSingleSamplePulseTicks(IAsyncResult)](m_nationalinstruments_daqmx_countersinglechannelreader_endreadsinglesamplepulseticks.htm) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginreadsinglesamplepulsetime.htm language=enus -->
## TOPIC 00081: CounterSingleChannelReaderBeginReadSingleSamplePulseTime Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginreadsinglesamplepulsetime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginreadsinglesamplepulsetime.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.BeginReadSingleSamplePulseTime Method

### CounterSingleChannelReaderBeginReadSingleSamplePulseTime Method

Begins an asynchronous read of a single pulse sample in terms of time from a counter task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadSingleSamplePulseTime(
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadSingleSamplePulseTime ( 
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePulseTime(AsyncCallback, Object), call [EndReadSingleSamplePulseTime(IAsyncResult)](m_nationalinstruments_daqmx_countersinglechannelreader_endreadsinglesamplepulsetime.htm) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadmultisamplepulseticks.htm language=enus -->
## TOPIC 00082: CounterSingleChannelReaderEndReadMultiSamplePulseTicks Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadmultisamplepulseticks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadmultisamplepulseticks.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.EndReadMultiSamplePulseTicks Method

### CounterSingleChannelReaderEndReadMultiSamplePulseTicks Method

BeginReadMultiSamplePulseTicks(Int32, AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIDataTicks[] EndReadMultiSamplePulseTicks(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadMultiSamplePulseTicks ( 
	asyncResult As IAsyncResult
) As CIDataTicks()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePulseTicks(Int32, AsyncCallback, Object).

###### Return Value

CIDataTicks

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePulseTicks(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadMultiSamplePulseTicks(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePulseTicks(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadmultisamplepulsetime.htm language=enus -->
## TOPIC 00083: CounterSingleChannelReaderEndReadMultiSamplePulseTime Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadmultisamplepulsetime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadmultisamplepulsetime.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.EndReadMultiSamplePulseTime Method

### CounterSingleChannelReaderEndReadMultiSamplePulseTime Method

BeginReadMultiSamplePulseTime(Int32, AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIDataTime[] EndReadMultiSamplePulseTime(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadMultiSamplePulseTime ( 
	asyncResult As IAsyncResult
) As CIDataTime()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePulseTime(Int32, AsyncCallback, Object).

###### Return Value

CIDataTime

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePulseTime(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadMultiSamplePulseTime(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePulseTime(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadmultisampleuint32.htm language=enus -->
## TOPIC 00084: CounterSingleChannelReaderEndReadMultiSampleUInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadmultisampleuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadmultisampleuint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.EndReadMultiSampleUInt32 Method

### CounterSingleChannelReaderEndReadMultiSampleUInt32 Method

BeginReadMultiSampleUInt32(Int32, AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public uint[] EndReadMultiSampleUInt32(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadMultiSampleUInt32 ( 
	asyncResult As IAsyncResult
) As UInteger()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSampleUInt32(Int32, AsyncCallback, Object).

###### Return Value

UInt32

UInt32

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSampleUInt32(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadMultiSampleUInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSampleUInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadsinglesampledouble.htm language=enus -->
## TOPIC 00085: CounterSingleChannelReaderEndReadSingleSampleDouble Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadsinglesampledouble.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadsinglesampledouble.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.EndReadSingleSampleDouble Method

### CounterSingleChannelReaderEndReadSingleSampleDouble Method

BeginReadSingleSampleDouble(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double EndReadSingleSampleDouble(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadSingleSampleDouble ( 
	asyncResult As IAsyncResult
) As Double
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSampleDouble(AsyncCallback, Object).

###### Return Value

Double

Double

DAQ Assistant

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSample(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSampleDouble(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSampleDouble(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadsinglesampleint32.htm language=enus -->
## TOPIC 00086: CounterSingleChannelReaderEndReadSingleSampleInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadsinglesampleint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadsinglesampleint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.EndReadSingleSampleInt32 Method

### CounterSingleChannelReaderEndReadSingleSampleInt32 Method

BeginReadSingleSampleInt32(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public int EndReadSingleSampleInt32(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadSingleSampleInt32 ( 
	asyncResult As IAsyncResult
) As Integer
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSampleInt32(AsyncCallback, Object).

###### Return Value

Int32

Int32

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSample(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSampleInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSampleInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadsinglesamplepulsefrequency.htm language=enus -->
## TOPIC 00087: CounterSingleChannelReaderEndReadSingleSamplePulseFrequency Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadsinglesamplepulsefrequency.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadsinglesamplepulsefrequency.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.EndReadSingleSamplePulseFrequency Method

### CounterSingleChannelReaderEndReadSingleSamplePulseFrequency Method

BeginReadSingleSamplePulseFrequency(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIDataFrequency EndReadSingleSamplePulseFrequency(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadSingleSamplePulseFrequency ( 
	asyncResult As IAsyncResult
) As CIDataFrequency
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePulseFrequency(AsyncCallback, Object).

###### Return Value

CIDataFrequency

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSample(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSamplePulseFrequency(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePulseFrequency(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadsinglesamplepulseticks.htm language=enus -->
## TOPIC 00088: CounterSingleChannelReaderEndReadSingleSamplePulseTicks Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadsinglesamplepulseticks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_endreadsinglesamplepulseticks.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.EndReadSingleSamplePulseTicks Method

### CounterSingleChannelReaderEndReadSingleSamplePulseTicks Method

BeginReadSingleSamplePulseTicks(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIDataTicks EndReadSingleSamplePulseTicks(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadSingleSamplePulseTicks ( 
	asyncResult As IAsyncResult
) As CIDataTicks
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePulseTicks(AsyncCallback, Object).

###### Return Value

CIDataTicks

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSample(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSamplePulseTicks(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePulseTicks(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampledouble.htm language=enus -->
## TOPIC 00089: CounterSingleChannelReaderMemoryOptimizedReadMultiSampleDouble Method (Int32, Double, ReallocationPolicy, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampledouble.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampledouble.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.MemoryOptimizedReadMultiSampleDouble Method (Int32, Double[], ReallocationPolicy, Int32)

### CounterSingleChannelReaderMemoryOptimizedReadMultiSampleDouble Method (Int32, Double, ReallocationPolicy, Int32)

Double

CIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] MemoryOptimizedReadMultiSampleDouble(
	int numberOfSamples,
	ref double[] data,
	ReallocationPolicy policy,
	out int actualNumberOfSamplesRead
)
```

```text
Public Function MemoryOptimizedReadMultiSampleDouble ( 
	numberOfSamples As Integer,
	ByRef data As Double(),
	policy As ReallocationPolicy,
	<OutAttribute> ByRef actualNumberOfSamplesRead As Integer
) As Double()
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: SystemDoubleAn initialized 1D array of Double samples that contains the read data. Each element in the array corresponds to a sample from the channel.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicyDictates the reallocation behavior of data. Refer to ReallocationPolicy for more information.
- **actualNumberOfSamplesRead**
  - Type: SystemInt32The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data.

###### Return Value

Double

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

When performing an asynchronous memory-optimized read, the size of the data buffer dynamically increases if the number of samples read exceeds the existing buffer and [ReallocationPolicy](t_nationalinstruments_daqmx_reallocationpolicy.htm) is [ToGrow](t_nationalinstruments_daqmx_reallocationpolicy.htm). 
This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. 
An ArgumentException is thrown if the buffer is not capable of holding the data and [ReallocationPolicy](t_nationalinstruments_daqmx_reallocationpolicy.htm) is [DoNotReallocate](t_nationalinstruments_daqmx_reallocationpolicy.htm).

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

CounterSingleChannelReader Class

MemoryOptimizedReadMultiSampleDouble Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampledouble_1.htm language=enus -->
## TOPIC 00090: CounterSingleChannelReaderMemoryOptimizedReadMultiSampleDouble Method (Int32, Double, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampledouble_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampledouble_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.MemoryOptimizedReadMultiSampleDouble Method (Int32, Double[], Int32)

### CounterSingleChannelReaderMemoryOptimizedReadMultiSampleDouble Method (Int32, Double, Int32)

Double

CIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] MemoryOptimizedReadMultiSampleDouble(
	int numberOfSamples,
	ref double[] data,
	out int actualNumberOfSamplesRead
)
```

```text
Public Function MemoryOptimizedReadMultiSampleDouble ( 
	numberOfSamples As Integer,
	ByRef data As Double(),
	<OutAttribute> ByRef actualNumberOfSamplesRead As Integer
) As Double()
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: SystemDoubleAn initialized 1D array of Double samples that contains the read data. Each element in the array corresponds to a sample from the channel.
- **actualNumberOfSamplesRead**
  - Type: SystemInt32The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data.

###### Return Value

Double

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. The memory allocation for the buffer is available to a maximum of 2 GB.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

CounterSingleChannelReader Class

MemoryOptimizedReadMultiSampleDouble Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampleuint32.htm language=enus -->
## TOPIC 00091: CounterSingleChannelReaderMemoryOptimizedReadMultiSampleUInt32 Method (Int32, UInt32, ReallocationPolicy, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampleuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampleuint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.MemoryOptimizedReadMultiSampleUInt32 Method (Int32, UInt32[], ReallocationPolicy, Int32)

### CounterSingleChannelReaderMemoryOptimizedReadMultiSampleUInt32 Method (Int32, UInt32, ReallocationPolicy, Int32)

UInt32

CIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public uint[] MemoryOptimizedReadMultiSampleUInt32(
	int numberOfSamples,
	ref uint[] data,
	ReallocationPolicy policy,
	out int actualNumberOfSamplesRead
)
```

```text
Public Function MemoryOptimizedReadMultiSampleUInt32 ( 
	numberOfSamples As Integer,
	ByRef data As UInteger(),
	policy As ReallocationPolicy,
	<OutAttribute> ByRef actualNumberOfSamplesRead As Integer
) As UInteger()
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: SystemUInt32An initialized 1D array of UInt32 samples that contains the read data. Each element in the array corresponds to a sample from the channel.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicyDictates the reallocation behavior of data. Refer to ReallocationPolicy for more information.
- **actualNumberOfSamplesRead**
  - Type: SystemInt32The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data.

###### Return Value

UInt32

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

When performing an asynchronous memory-optimized read, the size of the data buffer dynamically increases if the number of samples read exceeds the existing buffer and [ReallocationPolicy](t_nationalinstruments_daqmx_reallocationpolicy.htm) is [ToGrow](t_nationalinstruments_daqmx_reallocationpolicy.htm). 
This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. 
An ArgumentException is thrown if the buffer is not capable of holding the data and [ReallocationPolicy](t_nationalinstruments_daqmx_reallocationpolicy.htm) is [DoNotReallocate](t_nationalinstruments_daqmx_reallocationpolicy.htm).

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

CounterSingleChannelReader Class

MemoryOptimizedReadMultiSampleUInt32 Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampleuint32_1.htm language=enus -->
## TOPIC 00092: CounterSingleChannelReaderMemoryOptimizedReadMultiSampleUInt32 Method (Int32, UInt32, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampleuint32_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampleuint32_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.MemoryOptimizedReadMultiSampleUInt32 Method (Int32, UInt32[], Int32)

### CounterSingleChannelReaderMemoryOptimizedReadMultiSampleUInt32 Method (Int32, UInt32, Int32)

UInt32

CIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public uint[] MemoryOptimizedReadMultiSampleUInt32(
	int numberOfSamples,
	ref uint[] data,
	out int actualNumberOfSamplesRead
)
```

```text
Public Function MemoryOptimizedReadMultiSampleUInt32 ( 
	numberOfSamples As Integer,
	ByRef data As UInteger(),
	<OutAttribute> ByRef actualNumberOfSamplesRead As Integer
) As UInteger()
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: SystemUInt32An initialized 1D array of UInt32 samples that contains the read data. Each element in the array corresponds to a sample from the channel.
- **actualNumberOfSamplesRead**
  - Type: SystemInt32The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data.

###### Return Value

UInt32

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. The memory allocation for the buffer is available to a maximum of 2 GB.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

CounterSingleChannelReader Class

MemoryOptimizedReadMultiSampleUInt32 Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_readmultisamplepulsefrequency.htm language=enus -->
## TOPIC 00093: CounterSingleChannelReaderReadMultiSamplePulseFrequency Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_readmultisamplepulsefrequency.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_readmultisamplepulsefrequency.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.ReadMultiSamplePulseFrequency Method

### CounterSingleChannelReaderReadMultiSamplePulseFrequency Method

Reads one or more pulse samples in terms of frequency from a counter task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIDataFrequency[] ReadMultiSamplePulseFrequency(
	int numberOfSamples
)
```

```text
Public Function ReadMultiSamplePulseFrequency ( 
	numberOfSamples As Integer
) As CIDataFrequency()
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.

###### Return Value

CIDataFrequency

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_readmultisamplepulseticks.htm language=enus -->
## TOPIC 00094: CounterSingleChannelReaderReadMultiSamplePulseTicks Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_readmultisamplepulseticks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_readmultisamplepulseticks.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.ReadMultiSamplePulseTicks Method

### CounterSingleChannelReaderReadMultiSamplePulseTicks Method

Reads one or more pulse samples in terms of ticks from a counter task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIDataTicks[] ReadMultiSamplePulseTicks(
	int numberOfSamples
)
```

```text
Public Function ReadMultiSamplePulseTicks ( 
	numberOfSamples As Integer
) As CIDataTicks()
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.

###### Return Value

CIDataTicks

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_readsinglesamplepulseticks.htm language=enus -->
## TOPIC 00095: CounterSingleChannelReaderReadSingleSamplePulseTicks Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_readsinglesamplepulseticks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_readsinglesamplepulseticks.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.ReadSingleSamplePulseTicks Method

### CounterSingleChannelReaderReadSingleSamplePulseTicks Method

Reads a pulse sample in terms of ticks from a counter task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIDataTicks ReadSingleSamplePulseTicks()
```

```text
Public Function ReadSingleSamplePulseTicks As CIDataTicks
```

###### Return Value

CIDataTicks

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_readsinglesampleuint32.htm language=enus -->
## TOPIC 00096: CounterSingleChannelReaderReadSingleSampleUInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_readsinglesampleuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_readsinglesampleuint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.ReadSingleSampleUInt32 Method

### CounterSingleChannelReaderReadSingleSampleUInt32 Method

UInt32

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public uint ReadSingleSampleUInt32()
```

```text
Public Function ReadSingleSampleUInt32 As UInteger
```

###### Return Value

UInt32

UInt32

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_tostring.htm language=enus -->
## TOPIC 00097: CounterSingleChannelReaderToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.ToString Method

### CounterSingleChannelReaderToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelwriter_writemultisample_1.htm language=enus -->
## TOPIC 00098: CounterSingleChannelWriterWriteMultiSample Method (Boolean, CODataTicks)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelwriter_writemultisample_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelwriter_writemultisample_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelWriter.WriteMultiSample Method (Boolean, CODataTicks[])

### CounterSingleChannelWriterWriteMultiSample Method (Boolean, CODataTicks)

COChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteMultiSample(
	bool autoStart,
	CODataTicks[] data
)
```

```text
Public Sub WriteMultiSample ( 
	autoStart As Boolean,
	data As CODataTicks()
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: NationalInstruments.DAQmxCODataTicksA 1D array of samples to write to the task. Each element of the array corresponds to a sample to write to the channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

DAQ Assistant

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

CounterSingleChannelWriter Class

WriteMultiSample Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelwriter_writemultisample_2.htm language=enus -->
## TOPIC 00099: CounterSingleChannelWriterWriteMultiSample Method (Boolean, CODataTime)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelwriter_writemultisample_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelwriter_writemultisample_2.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelWriter.WriteMultiSample Method (Boolean, CODataTime[])

### CounterSingleChannelWriterWriteMultiSample Method (Boolean, CODataTime)

COChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteMultiSample(
	bool autoStart,
	CODataTime[] data
)
```

```text
Public Sub WriteMultiSample ( 
	autoStart As Boolean,
	data As CODataTime()
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: NationalInstruments.DAQmxCODataTimeA 1D array of samples to write to the task. Each element of the array corresponds to a sample to write to the channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

DAQ Assistant

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

CounterSingleChannelWriter Class

WriteMultiSample Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelwriter_writesinglesample_1.htm language=enus -->
## TOPIC 00100: CounterSingleChannelWriterWriteSingleSample Method (Boolean, CODataTicks)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelwriter_writesinglesample_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelwriter_writesinglesample_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelWriter.WriteSingleSample Method (Boolean, CODataTicks)

### CounterSingleChannelWriterWriteSingleSample Method (Boolean, CODataTicks)

COChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteSingleSample(
	bool autoStart,
	CODataTicks data
)
```

```text
Public Sub WriteSingleSample ( 
	autoStart As Boolean,
	data As CODataTicks
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: NationalInstruments.DAQmxCODataTicksA sample to write to the task.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

DAQ Assistant

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

CounterSingleChannelWriter Class

WriteSingleSample Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelwriter_writesinglesample_2.htm language=enus -->
## TOPIC 00101: CounterSingleChannelWriterWriteSingleSample Method (Boolean, CODataTime)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelwriter_writesinglesample_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_countersinglechannelwriter_writesinglesample_2.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelWriter.WriteSingleSample Method (Boolean, CODataTime)

### CounterSingleChannelWriterWriteSingleSample Method (Boolean, CODataTime)

COChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteSingleSample(
	bool autoStart,
	CODataTime data
)
```

```text
Public Sub WriteSingleSample ( 
	autoStart As Boolean,
	data As CODataTime
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: NationalInstruments.DAQmxCODataTimeA sample to write to the task.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

DAQ Assistant

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

CounterSingleChannelWriter Class

WriteSingleSample Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqexception__ctor_1.htm language=enus -->
## TOPIC 00102: DaqException Constructor (SerializationInfo, StreamingContext)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqexception__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqexception__ctor_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqException Constructor (SerializationInfo, StreamingContext)

### DaqException Constructor (SerializationInfo, StreamingContext)

DaqException

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected DaqException(
	SerializationInfo info,
	StreamingContext context
)
```

```text
Protected Sub New ( 
	info As SerializationInfo,
	context As StreamingContext
)
```

###### Parameters

- **info**
  - Type: System.Runtime.SerializationSerializationInfoThe object that holds the serialized object data.
- **context**
  - Type: System.Runtime.SerializationStreamingContextThe contextual information about the source or destination.

##### Remarks

This constructor is called during deserialization to reconstitute the exception object transmitted over a stream. For more information, refer to XML and SOAP Serialization in the Microsoft .NET Framework documentation.

##### See Also

###### Reference

DaqException Class

DaqException Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqexception__ctor_2.htm language=enus -->
## TOPIC 00103: DaqException Constructor (String)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqexception__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqexception__ctor_2.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqException Constructor (String)

### DaqException Constructor (String)

DaqException

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DaqException(
	string message
)
```

```text
Public Sub New ( 
	message As String
)
```

###### Parameters

- **message**
  - Type: SystemString The error message that explains the cause of the exception.

##### See Also

###### Reference

DaqException Class

DaqException Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

NI-DAQmx Driver Error Codes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_addnetworkdevice.htm language=enus -->
## TOPIC 00104: DaqSystemAddNetworkDevice Method (String, String, Boolean, Double)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_addnetworkdevice.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_addnetworkdevice.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.AddNetworkDevice Method (String, String, Boolean, Double)

### DaqSystemAddNetworkDevice Method (String, String, Boolean, Double)

Adds a Network cDAQ device to the system and, if specified, attempts to reserve it.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public Device AddNetworkDevice(
	string ipAddress,
	string deviceName,
	bool attemptReservation,
	double timeout
)
```

```text
Public Function AddNetworkDevice ( 
	ipAddress As String,
	deviceName As String,
	attemptReservation As Boolean,
	timeout As Double
) As Device
```

###### Parameters

- **ipAddress**
  - Type: SystemStringSpecifies the string containing the IP address (in dotted decimal notation) of the device to add to the system.
- **deviceName**
  - Type: SystemStringThe name to assign to the device. If unspecified, NI-DAQmx chooses the device name.
- **attemptReservation**
  - Type: SystemBooleanSpecifies whether a reservation should be attempted after the device is successfully added.
- **timeout**
  - Type: SystemDoubleSpecifies the time in seconds to wait for the device to respond before timing out.

###### Return Value

Device

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

attemptReservation

##### See Also

###### Reference

DaqSystem Class

AddNetworkDevice Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_addnetworkdevice_1.htm language=enus -->
## TOPIC 00105: DaqSystemAddNetworkDevice Method (String, String, Double)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_addnetworkdevice_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_addnetworkdevice_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.AddNetworkDevice Method (String, String, Double)

### DaqSystemAddNetworkDevice Method (String, String, Double)

Adds a Network cDAQ device to the system. This method does not attempt to reserve the device after the device is successfully added.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public Device AddNetworkDevice(
	string ipAddress,
	string deviceName,
	double timeout
)
```

```text
Public Function AddNetworkDevice ( 
	ipAddress As String,
	deviceName As String,
	timeout As Double
) As Device
```

###### Parameters

- **ipAddress**
  - Type: SystemStringSpecifies the string containing the IP address (in dotted decimal notation) of the device to add to the system.
- **deviceName**
  - Type: SystemStringThe name to assign to the device. If unspecified, NI-DAQmx chooses the device name.
- **timeout**
  - Type: SystemDoubleSpecifies the time in seconds to wait for the device to respond before timing out.

###### Return Value

Device

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

MAX automatically attempts to reserve a device when the device is added, but this method does not.

##### See Also

###### Reference

DaqSystem Class

AddNetworkDevice Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_connectswitchchannels.htm language=enus -->
## TOPIC 00106: DaqSystemConnectSwitchChannels Method (String, Boolean)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_connectswitchchannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_connectswitchchannels.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.ConnectSwitchChannels Method (String, Boolean)

### DaqSystemConnectSwitchChannels Method (String, Boolean)

**Note: This API is now obsolete.**

Makes one or more connections between switch channels as specified by the connection list.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This method is obsolete.")]
public void ConnectSwitchChannels(
	string connectionList,
	bool waitForSettling
)
```

```text
<ObsoleteAttribute("This method is obsolete.")>
Public Sub ConnectSwitchChannels ( 
	connectionList As String,
	waitForSettling As Boolean
)
```

###### Parameters

- **connectionList**
  - Type: SystemStringA list of connections to make between switch channels. This list uses a special syntax.
- **waitForSettling**
  - Type: SystemBooleanIf , this method waits for the switches to settle before returning. If , the method returns immediately after the operation. This settling time is controlled through the SettlingTime property.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

You can specify only the two endpoints, or you can specify the explicit path between two endpoints. This method can make connections on multiple devices, but each individual connection must reside on a single device. In the event of an error, connecting stops at the point in the list where the error occurred.

##### See Also

###### Reference

DaqSystem Class

ConnectSwitchChannels Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_connectterminals.htm language=enus -->
## TOPIC 00107: DaqSystemConnectTerminals Method (String, String)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_connectterminals.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_connectterminals.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.ConnectTerminals Method (String, String)

### DaqSystemConnectTerminals Method (String, String)

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConnectTerminals(
	string sourceTerminal,
	string destinationTerminal
)
```

```text
Public Sub ConnectTerminals ( 
	sourceTerminal As String,
	destinationTerminal As String
)
```

###### Parameters

- **sourceTerminal**
  - Type: SystemStringThe originating terminal of the route.
- **destinationTerminal**
  - Type: SystemStringThe receiving terminal of the route.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

immediate routing

##### See Also

###### Reference

DaqSystem Class

ConnectTerminals Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_connectterminals_1.htm language=enus -->
## TOPIC 00108: DaqSystemConnectTerminals Method (String, String, SignalRoutingModifiers)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_connectterminals_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_connectterminals_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.ConnectTerminals Method (String, String, SignalRoutingModifiers)

### DaqSystemConnectTerminals Method (String, String, SignalRoutingModifiers)

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConnectTerminals(
	string sourceTerminal,
	string destinationTerminal,
	SignalRoutingModifiers signalModifiers
)
```

```text
Public Sub ConnectTerminals ( 
	sourceTerminal As String,
	destinationTerminal As String,
	signalModifiers As SignalRoutingModifiers
)
```

###### Parameters

- **sourceTerminal**
  - Type: SystemStringThe originating terminal of the route.
- **destinationTerminal**
  - Type: SystemStringThe receiving terminal of the route.
- **signalModifiers**
  - Type: NationalInstruments.DAQmxSignalRoutingModifiersSpecifies if the signal routed from the source terminal to the destination terminal is inverted. If the device is not capable of signal inversion or if a previous route reserved the inversion circuitry in an incompatible configuration, attempting to invert the signal causes an error.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

immediate routing

##### See Also

###### Reference

DaqSystem Class

ConnectTerminals Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_createwatchdogtimertask.htm language=enus -->
## TOPIC 00109: DaqSystemCreateWatchdogTimerTask Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_createwatchdogtimertask.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_createwatchdogtimertask.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.CreateWatchdogTimerTask Method

### DaqSystemCreateWatchdogTimerTask Method

watchdog timer

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public Task CreateWatchdogTimerTask(
	string taskName,
	string device,
	double timeout,
	string[] physicalChannels,
	WatchdogDOExpirationState[] expirationStates
)
```

```text
Public Function CreateWatchdogTimerTask ( 
	taskName As String,
	device As String,
	timeout As Double,
	physicalChannels As String(),
	expirationStates As WatchdogDOExpirationState()
) As Task
```

###### Parameters

- **taskName**
  - Type: SystemStringThe name of the task to create. If you specify Empty or , the NI-DAQmx driver assigns a unique name to the new task.
- **device**
  - Type: SystemStringThe name of the device for which to create a watchdog timer task.
- **timeout**
  - Type: SystemDoubleThe amount of time in seconds until the watchdog timer expires. A value of -1 means the internal timer never expires. Set timeout to -1 if you use an Expiration Trigger to expire the watchdog task.
- **physicalChannels**
  - Type: SystemStringThe physical channel names for which to define watchdog expiration states. Each value in this vector specifies a physical channel string that is assigned the expiration state at the corresponding position in the expirationStates parameter. You cannot modify the expiration state of dedicated digital input physical channels.
- **expirationStates**
  - Type: NationalInstruments.DAQmxWatchdogDOExpirationStateThe state to which to set the digital physical channel when the watchdog timer expires.

###### Return Value

Task

Task

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Task

Watchdog

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_deleteglobalchannel.htm language=enus -->
## TOPIC 00110: DaqSystemDeleteGlobalChannel Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_deleteglobalchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_deleteglobalchannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.DeleteGlobalChannel Method

### DaqSystemDeleteGlobalChannel Method

global channel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void DeleteGlobalChannel(
	string persistedName
)
```

```text
Public Sub DeleteGlobalChannel ( 
	persistedName As String
)
```

###### Parameters

- **persistedName**
  - Type: SystemStringThe name of the global channel to delete.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

tasks

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_deletescale.htm language=enus -->
## TOPIC 00111: DaqSystemDeleteScale Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_deletescale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_deletescale.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.DeleteScale Method

### DaqSystemDeleteScale Method

custom scale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void DeleteScale(
	string persistedName
)
```

```text
Public Sub DeleteScale ( 
	persistedName As String
)
```

###### Parameters

- **persistedName**
  - Type: SystemStringThe name of the scale to delete.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

virtual channels

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_deletetask.htm language=enus -->
## TOPIC 00112: DaqSystemDeleteTask Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_deletetask.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_deletetask.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.DeleteTask Method

### DaqSystemDeleteTask Method

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void DeleteTask(
	string persistedName
)
```

```text
Public Sub DeleteTask ( 
	persistedName As String
)
```

###### Parameters

- **persistedName**
  - Type: SystemStringThe name of the task to delete.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method does not clear the copy of the task stored in memory.

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_disconnectswitchchannels.htm language=enus -->
## TOPIC 00113: DaqSystemDisconnectSwitchChannels Method (String, Boolean)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_disconnectswitchchannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_disconnectswitchchannels.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.DisconnectSwitchChannels Method (String, Boolean)

### DaqSystemDisconnectSwitchChannels Method (String, Boolean)

**Note: This API is now obsolete.**

Terminates one or more connections between switch channels as specified by the disconnection list.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This method is obsolete.")]
public void DisconnectSwitchChannels(
	string disconnectionList,
	bool waitForSettling
)
```

```text
<ObsoleteAttribute("This method is obsolete.")>
Public Sub DisconnectSwitchChannels ( 
	disconnectionList As String,
	waitForSettling As Boolean
)
```

###### Parameters

- **disconnectionList**
  - Type: SystemStringA list of switch connections to terminate. This list uses a special syntax.
- **waitForSettling**
  - Type: SystemBooleanIf , this method waits for the switches to settle before returning. If , the method returns immediately after the operation. This settling time is controlled through the SettlingTime property.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqSystem Class

DisconnectSwitchChannels Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_disconnectswitchchannels_1.htm language=enus -->
## TOPIC 00114: DaqSystemDisconnectSwitchChannels Method (String, String, Boolean)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_disconnectswitchchannels_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_disconnectswitchchannels_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.DisconnectSwitchChannels Method (String, String, Boolean)

### DaqSystemDisconnectSwitchChannels Method (String, String, Boolean)

**Note: This API is now obsolete.**

Terminates a connection between two channels.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This method is obsolete.")]
public void DisconnectSwitchChannels(
	string switchChannel1,
	string switchChannel2,
	bool waitForSettling
)
```

```text
<ObsoleteAttribute("This method is obsolete.")>
Public Sub DisconnectSwitchChannels ( 
	switchChannel1 As String,
	switchChannel2 As String,
	waitForSettling As Boolean
)
```

###### Parameters

- **switchChannel1**
  - Type: SystemStringThe first channel in the connection.
- **switchChannel2**
  - Type: SystemStringThe second channel in the connection.
- **waitForSettling**
  - Type: SystemBooleanIf , this method waits for the switches to settle before returning. If , the method returns immediately after the operation. This settling time is controlled through the SettlingTime property.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqSystem Class

DisconnectSwitchChannels Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_disconnectterminals.htm language=enus -->
## TOPIC 00115: DaqSystemDisconnectTerminals Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_disconnectterminals.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_disconnectterminals.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.DisconnectTerminals Method

### DaqSystemDisconnectTerminals Method

ConnectTerminals(String, String, SignalRoutingModifiers)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void DisconnectTerminals(
	string sourceTerminal,
	string destinationTerminal
)
```

```text
Public Sub DisconnectTerminals ( 
	sourceTerminal As String,
	destinationTerminal As String
)
```

###### Parameters

- **sourceTerminal**
  - Type: SystemStringThe originating terminal of the route.
- **destinationTerminal**
  - Type: SystemStringThe receiving terminal of the route.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

immediate routing

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_getterminals.htm language=enus -->
## TOPIC 00116: DaqSystemGetTerminals Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_getterminals.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_getterminals.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.GetTerminals Method

### DaqSystemGetTerminals Method

terminal names

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] GetTerminals(
	TerminalTypes terminalTypes
)
```

```text
Public Function GetTerminals ( 
	terminalTypes As TerminalTypes
) As String()
```

###### Parameters

- **terminalTypes**
  - Type: NationalInstruments.DAQmxTerminalTypesThe types of terminals to include.

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_loaddevice.htm language=enus -->
## TOPIC 00117: DaqSystemLoadDevice Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_loaddevice.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_loaddevice.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.LoadDevice Method

### DaqSystemLoadDevice Method

Device

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public Device LoadDevice(
	string deviceName
)
```

```text
Public Function LoadDevice ( 
	deviceName As String
) As Device
```

###### Parameters

- **deviceName**
  - Type: SystemStringThe name of the device.

###### Return Value

Device

Device

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Devices

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_loadphysicalchannel.htm language=enus -->
## TOPIC 00118: DaqSystemLoadPhysicalChannel Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_loadphysicalchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_loadphysicalchannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.LoadPhysicalChannel Method

### DaqSystemLoadPhysicalChannel Method

PhysicalChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public PhysicalChannel LoadPhysicalChannel(
	string physicalChannelName
)
```

```text
Public Function LoadPhysicalChannel ( 
	physicalChannelName As String
) As PhysicalChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe name of the physical channel.

###### Return Value

PhysicalChannel

PhysicalChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_openswitchrelays.htm language=enus -->
## TOPIC 00119: DaqSystemOpenSwitchRelays Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_openswitchrelays.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_openswitchrelays.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.OpenSwitchRelays Method

### DaqSystemOpenSwitchRelays Method

**Note: This API is now obsolete.**

Opens the specified relays.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This method is obsolete.")]
public void OpenSwitchRelays(
	string relays,
	bool waitForSettling
)
```

```text
<ObsoleteAttribute("This method is obsolete.")>
Public Sub OpenSwitchRelays ( 
	relays As String,
	waitForSettling As Boolean
)
```

###### Parameters

- **relays**
  - Type: SystemStringA set of relays to open. You can specify a string that contains a comma-delimited list of relays.
- **waitForSettling**
  - Type: SystemBooleanIf , this method waits for the switches to settle before returning. If , the method returns immediately after the operation. This settling time is controlled through the SettlingTime property.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

usage types

ConnectSwitchChannels(String, Boolean)

DisconnectSwitchChannels(String, Boolean)

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_removecdaqsynchronizationconnection.htm language=enus -->
## TOPIC 00120: DaqSystemRemoveCDaqSynchronizationConnection Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_removecdaqsynchronizationconnection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_removecdaqsynchronizationconnection.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.RemoveCDaqSynchronizationConnection Method

### DaqSystemRemoveCDaqSynchronizationConnection Method

Removes a cDAQ Sync connection between devices. The connection is not verified.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void RemoveCDaqSynchronizationConnection(
	string portList
)
```

```text
Public Sub RemoveCDaqSynchronizationConnection ( 
	portList As String
)
```

###### Parameters

- **portList**
  - Type: SystemStringSpecifies the cDAQ Sync ports to disconnect.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_saveglobalchannel_1.htm language=enus -->
## TOPIC 00121: DaqSystemSaveGlobalChannel Method (Channel, String, SaveOptions)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_saveglobalchannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_saveglobalchannel_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.SaveGlobalChannel Method (Channel, String, SaveOptions)

### DaqSystemSaveGlobalChannel Method (Channel, String, SaveOptions)

local or global channel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void SaveGlobalChannel(
	Channel channel,
	string author,
	SaveOptions options
)
```

```text
Public Sub SaveGlobalChannel ( 
	channel As Channel,
	author As String,
	options As SaveOptions
)
```

###### Parameters

- **channel**
  - Type: NationalInstruments.DAQmxChannelThe channel instance to save.
- **author**
  - Type: SystemStringA user-specified string that represents the name to store with the channel. For example, channels created with the DAQ Assistant have the string "DAQ Assistant" as their author. You may pass Empty.
- **options**
  - Type: NationalInstruments.DAQmxSaveOptionsOne or more flags indicating various save options.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

SaveGlobalChannelAs(Channel, String)

You cannot view programmatically saved global channels in the DAQ Assistant for versions of NI-DAQ earlier than 7.4. To view a programmatically saved global channel in an earlier version of NI-DAQ, first use the DAQ Assistant in NI-DAQ 7.4 or later to save the global channel.

Visit the DAQmx Professional Developer Tools Web site for more information and examples of programmatically saving global channels.

##### See Also

###### Reference

DaqSystem Class

SaveGlobalChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_saveglobalchannelas.htm language=enus -->
## TOPIC 00122: DaqSystemSaveGlobalChannelAs Method (Channel, String)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_saveglobalchannelas.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_saveglobalchannelas.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.SaveGlobalChannelAs Method (Channel, String)

### DaqSystemSaveGlobalChannelAs Method (Channel, String)

local or global channel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void SaveGlobalChannelAs(
	Channel channel,
	string persistedName
)
```

```text
Public Sub SaveGlobalChannelAs ( 
	channel As Channel,
	persistedName As String
)
```

###### Parameters

- **channel**
  - Type: NationalInstruments.DAQmxChannelThe channel instance to save.
- **persistedName**
  - Type: SystemStringThe name to use for the saved channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Default

Author

SaveGlobalChannelAs(Channel, String, String, SaveOptions)

If you do not assign a value to the saved channel, NI-DAQmx uses the name currently assigned to the channel.

You cannot view programmatically saved global channels in the DAQ Assistant for versions of NI-DAQ earlier than 7.4. To view a programmatically saved global channel in an earlier version of NI-DAQ, first use the DAQ Assistant in NI-DAQ 7.4 or later to save the global channel.

Visit the DAQmx Professional Developer Tools Web site for more information and examples of programmatically saving global channels.

##### See Also

###### Reference

DaqSystem Class

SaveGlobalChannelAs Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_saveglobalchannelas_1.htm language=enus -->
## TOPIC 00123: DaqSystemSaveGlobalChannelAs Method (Channel, String, String, SaveOptions)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_saveglobalchannelas_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_saveglobalchannelas_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.SaveGlobalChannelAs Method (Channel, String, String, SaveOptions)

### DaqSystemSaveGlobalChannelAs Method (Channel, String, String, SaveOptions)

local or global channel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void SaveGlobalChannelAs(
	Channel channel,
	string persistedName,
	string author,
	SaveOptions options
)
```

```text
Public Sub SaveGlobalChannelAs ( 
	channel As Channel,
	persistedName As String,
	author As String,
	options As SaveOptions
)
```

###### Parameters

- **channel**
  - Type: NationalInstruments.DAQmxChannelThe channel instance to save.
- **persistedName**
  - Type: SystemStringThe name to use for the saved channel.
- **author**
  - Type: SystemStringA user-specified string that represents the name to store with the channel. For example, channels created with the DAQ Assistant have the string "DAQ Assistant" as their author. You may pass Empty.
- **options**
  - Type: NationalInstruments.DAQmxSaveOptionsOne or more flags indicating various save options.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

You cannot view programmatically saved global channels in the DAQ Assistant for versions of NI-DAQ earlier than 7.4. To view a programmatically saved global channel in an earlier version of NI-DAQ, first use the DAQ Assistant in NI-DAQ 7.4 or later to save the global channel.

Visit the DAQmx Professional Developer Tools Web site for more information and examples of programmatically saving global channels.

##### See Also

###### Reference

DaqSystem Class

SaveGlobalChannelAs Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_savescale.htm language=enus -->
## TOPIC 00124: DaqSystemSaveScale Method (Scale)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_savescale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_savescale.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.SaveScale Method (Scale)

### DaqSystemSaveScale Method (Scale)

custom scale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void SaveScale(
	Scale scale
)
```

```text
Public Sub SaveScale ( 
	scale As Scale
)
```

###### Parameters

- **scale**
  - Type: NationalInstruments.DAQmxScaleThe scale instance to save.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

SaveScaleAs(Scale, String)

This method sets the [Default](t_nationalinstruments_daqmx_saveoptions.htm) option for the saved scale and uses an empty string for the scale [Author](p_nationalinstruments_daqmx_savedscaleinfo_author.htm). You can specify your own options and author value by using the [SaveScale(Scale, String, SaveOptions)](m_nationalinstruments_daqmx_daqsystem_savescale_1.htm) overload.

Visit the DAQmx Professional Developer Tools Web site for more information and examples of programmatically saving custom scales.

##### See Also

###### Reference

DaqSystem Class

SaveScale Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_savetask_1.htm language=enus -->
## TOPIC 00125: DaqSystemSaveTask Method (Task, String, SaveOptions)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_savetask_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_savetask_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.SaveTask Method (Task, String, SaveOptions)

### DaqSystemSaveTask Method (Task, String, SaveOptions)

task

local channels

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void SaveTask(
	Task task,
	string author,
	SaveOptions options
)
```

```text
Public Sub SaveTask ( 
	task As Task,
	author As String,
	options As SaveOptions
)
```

###### Parameters

- **task**
  - Type: NationalInstruments.DAQmxTaskThe task instance to save.
- **author**
  - Type: SystemStringA user-specified string that represents the name to store with the task. For example, tasks created with the DAQ Assistant have the string "DAQ Assistant" as their author. You may pass Empty.
- **options**
  - Type: NationalInstruments.DAQmxSaveOptionsOne or more flags indicating various save options.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

SaveTaskAs(Task, String)

You cannot view programmatically saved tasks in the DAQ Assistant for versions of NI-DAQ earlier than 7.4. To view a programmatically saved task in an earlier version of NI-DAQ, first use the DAQ Assistant in NI-DAQ 7.4 or later to save the task.

Visit the DAQmx Professional Developer Tools Web site for more information and examples of programmatically saving tasks.

##### See Also

###### Reference

DaqSystem Class

SaveTask Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_savetaskas_1.htm language=enus -->
## TOPIC 00126: DaqSystemSaveTaskAs Method (Task, String, String, SaveOptions)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_savetaskas_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_savetaskas_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.SaveTaskAs Method (Task, String, String, SaveOptions)

### DaqSystemSaveTaskAs Method (Task, String, String, SaveOptions)

task

local channels

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void SaveTaskAs(
	Task task,
	string persistedName,
	string author,
	SaveOptions options
)
```

```text
Public Sub SaveTaskAs ( 
	task As Task,
	persistedName As String,
	author As String,
	options As SaveOptions
)
```

###### Parameters

- **task**
  - Type: NationalInstruments.DAQmxTaskThe task instance to save.
- **persistedName**
  - Type: SystemStringThe name to use for the saved task.
- **author**
  - Type: SystemStringA user-specified string that represents the name to store with the task. For example, tasks created with the DAQ Assistant have the string "DAQ Assistant" as their author. You may pass Empty.
- **options**
  - Type: NationalInstruments.DAQmxSaveOptionsOne or more flags indicating various save options.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

You cannot view programmatically saved tasks in the DAQ Assistant for versions of NI-DAQ earlier than 7.4. To view a programmatically saved task in an earlier version of NI-DAQ, first use the DAQ Assistant in NI-DAQ 7.4 or later to save the task.

Visit the DAQmx Professional Developer Tools Web site for more information and examples of programmatically saving tasks.

##### See Also

###### Reference

DaqSystem Class

SaveTaskAs Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_setdevicepowerupstate_1.htm language=enus -->
## TOPIC 00127: DaqSystemSetDevicePowerUpState Method (String, String, DigitalPullUpPullDownResistorState)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_setdevicepowerupstate_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_setdevicepowerupstate_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.SetDevicePowerUpState Method (String, String[], DigitalPullUpPullDownResistorState[])

### DaqSystemSetDevicePowerUpState Method (String, String, DigitalPullUpPullDownResistorState)

Sets the resistor level for lines when they are in tristate logic.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void SetDevicePowerUpState(
	string deviceName,
	string[] channels,
	DigitalPullUpPullDownResistorState[] states
)
```

```text
Public Sub SetDevicePowerUpState ( 
	deviceName As String,
	channels As String(),
	states As DigitalPullUpPullDownResistorState()
)
```

###### Parameters

- **deviceName**
  - Type: SystemStringThe name, as configured in Measurement Automation Explorer (MAX), of the device to which this operation applies.
- **channels**
  - Type: SystemStringThe digital line or port to modify. You cannot modify dedicated digital input lines.
- **states**
  - Type: NationalInstruments.DAQmxDigitalPullUpPullDownResistorStateThe pull up pull down level set for the physical channel specified with DigitalPullUpPullDownResistorState.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqSystem Class

SetDevicePowerUpState Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_setdevicepowerupstate_2.htm language=enus -->
## TOPIC 00128: DaqSystemSetDevicePowerUpState Method (String, String, Double, String, Double)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_setdevicepowerupstate_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_daqsystem_setdevicepowerupstate_2.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.SetDevicePowerUpState Method (String, String[], Double[], String[], Double[])

### DaqSystemSetDevicePowerUpState Method (String, String, Double, String, Double)

power up states

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void SetDevicePowerUpState(
	string deviceName,
	string[] voltageChannels,
	double[] voltageValues,
	string[] currentChannels,
	double[] currentValues
)
```

```text
Public Sub SetDevicePowerUpState ( 
	deviceName As String,
	voltageChannels As String(),
	voltageValues As Double(),
	currentChannels As String(),
	currentValues As Double()
)
```

###### Parameters

- **deviceName**
  - Type: SystemStringThe name, as configured in Measurement Automation Explorer (MAX), of the device to which this operation applies.
- **voltageChannels**
  - Type: SystemStringThe voltage channels for which to set new power up values. Each value in this array specifies a virtual channel string that is assigned the voltage at the corresponding position in the voltageValues parameter. You can set voltage power up states only for physical channels that support voltage output.
- **voltageValues**
  - Type: SystemDoubleThe voltages to set. Each value in this array applies to the virtual channel name at the corresponding position of the voltageChannels parameter. You can set voltage power up states only for physical channels that support voltage output.
- **currentChannels**
  - Type: SystemStringThe current channels for which to set new power up values. Each value in this array specifies a virtual channel string that is assigned the current at the corresponding position in the currentValues parameter. You can set current power up states only for physical channels that support current output.
- **currentValues**
  - Type: SystemDoubleThe currents to set. Each value in this array applies to the virtual channel name at the corresponding position of the currentChannels parameter. You can set current power up states only for physical channels that support current output.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Power up states are stored in EEPROMs that you can write to only a limited number of times. Therefore, you should use this method as infrequently as possible. This method writes to the EEPROM only if a setting you request is different from the one currently stored on the EEPROM. This method writes power up states in the sequential order of the power up states array. Therefore, any physical channels with multiple entries in that array use the highest array index.

When you call this method, you can choose to not set either voltages or currents by passing in for the voltage or current parameters, but not both.

##### See Also

###### Reference

DaqSystem Class

SetDevicePowerUpState Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_deletenetworkdevice.htm language=enus -->
## TOPIC 00129: DeviceDeleteNetworkDevice Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_deletenetworkdevice.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_deletenetworkdevice.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.DeleteNetworkDevice Method

### DeviceDeleteNetworkDevice Method

Deletes a Network DAQ device previously added to the host.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void DeleteNetworkDevice()
```

```text
Public Sub DeleteNetworkDevice
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

If the device is reserved, the device is unreserved before it is removed.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_dispose_1.htm language=enus -->
## TOPIC 00130: DeviceDispose Method (Boolean)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_dispose_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_dispose_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.Dispose Method (Boolean)

### DeviceDispose Method (Boolean)

Device

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void Dispose(
	bool A_0
)
```

```text
Protected Overridable Sub Dispose ( 
	A_0 As Boolean
)
```

###### Parameters

- **A_0**
  - Type: SystemBoolean

##### Remarks

Cleaning Up Unmanaged Resources

IDisposable

##### See Also

###### Reference

Device Class

Dispose Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_getphysicalchannels.htm language=enus -->
## TOPIC 00131: DeviceGetPhysicalChannels Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_getphysicalchannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_getphysicalchannels.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.GetPhysicalChannels Method

### DeviceGetPhysicalChannels Method

physical channels

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] GetPhysicalChannels(
	PhysicalChannelTypes physicalChannelTypes,
	PhysicalChannelAccess physicalChannelAccess
)
```

```text
Public Function GetPhysicalChannels ( 
	physicalChannelTypes As PhysicalChannelTypes,
	physicalChannelAccess As PhysicalChannelAccess
) As String()
```

###### Parameters

- **physicalChannelTypes**
  - Type: NationalInstruments.DAQmxPhysicalChannelTypesThe types of physical channels to include.
- **physicalChannelAccess**
  - Type: NationalInstruments.DAQmxPhysicalChannelAccessThe access types of physical channels to include.

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_reservenetworkdevice_1.htm language=enus -->
## TOPIC 00132: DeviceReserveNetworkDevice Method (Boolean)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_reservenetworkdevice_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_reservenetworkdevice_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.ReserveNetworkDevice Method (Boolean)

### DeviceReserveNetworkDevice Method (Boolean)

Reserves the Network DAQ device for the current host. Reservation is required to run NI-DAQmx tasks, and the device must be added in MAX before it can be reserved. Use this method to specify whether to override an existing reservation.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ReserveNetworkDevice(
	bool overrideReservation
)
```

```text
Public Sub ReserveNetworkDevice ( 
	overrideReservation As Boolean
)
```

###### Parameters

- **overrideReservation**
  - Type: SystemBooleanSpecifies whether an existing reservation on the device should be overridden by this reservation.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

ReserveNetworkDevice Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_restorelastexternalcalibration.htm language=enus -->
## TOPIC 00133: DeviceRestoreLastExternalCalibration Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_restorelastexternalcalibration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_restorelastexternalcalibration.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.RestoreLastExternalCalibration Method

### DeviceRestoreLastExternalCalibration Method

Sets the self-calibration constants of the device to the current external calibration constants.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void RestoreLastExternalCalibration()
```

```text
Public Sub RestoreLastExternalCalibration
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

National Instruments sets the external calibration constants at the factory, and those constants remain in effect until you perform a new external calibration on the device.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_startexternalcalibration.htm language=enus -->
## TOPIC 00134: DeviceStartExternalCalibration Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_startexternalcalibration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_startexternalcalibration.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.StartExternalCalibration Method

### DeviceStartExternalCalibration Method

Starts an external calibration session on a device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public ExternalCalibrationSession StartExternalCalibration(
	string password
)
```

```text
Public Function StartExternalCalibration ( 
	password As String
) As ExternalCalibrationSession
```

###### Parameters

- **password**
  - Type: SystemStringThe current calibration password for the device. The default password for all NI products is NI.

###### Return Value

ExternalCalibrationSession

ExternalCalibrationSession

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_tostring.htm language=enus -->
## TOPIC 00135: DeviceToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.ToString Method

### DeviceToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_unreservenetworkdevice.htm language=enus -->
## TOPIC 00136: DeviceUnreserveNetworkDevice Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_unreservenetworkdevice.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_device_unreservenetworkdevice.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device.UnreserveNetworkDevice Method

### DeviceUnreserveNetworkDevice Method

Unreserves or releases a Network DAQ device previously reserved by the host.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void UnreserveNetworkDevice()
```

```text
Public Sub UnreserveNetworkDevice
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_dichannelcollection_createchannel.htm language=enus -->
## TOPIC 00137: DIChannelCollectionCreateChannel Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_dichannelcollection_createchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_dichannelcollection_createchannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DIChannelCollection.CreateChannel Method

### DIChannelCollectionCreateChannel Method

DIChannel

measure digital signals

DIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DIChannel CreateChannel(
	string lines,
	string nameToAssign,
	ChannelLineGrouping grouping
)
```

```text
Public Function CreateChannel ( 
	lines As String,
	nameToAssign As String,
	grouping As ChannelLineGrouping
) As DIChannel
```

###### Parameters

- **lines**
  - Type: SystemStringThe names of the digital lines or ports to use to create the virtual channel.
- **nameToAssign**
  - Type: SystemStringThe name of the virtual channel this method creates.
- **grouping**
  - Type: NationalInstruments.DAQmxChannelLineGroupingThe grouping of digital lines into one or more DIChannel objects. If you specify one or more entire ports with lines, you must set grouping to OneChannelForAllLines.

###### Return Value

DIChannel

DIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

DIChannel

DIChannel

lines

If you do not specify a value for nameToAssign, NI-DAQmx uses the physical channel name for the virtual channel name. If you use nameToAssign to create a name for the local virtual channel, you must use that name when you refer to this channel in other NI-DAQmx properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateChannel(String, String, ChannelLineGrouping) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

DIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_dichannelcollection_getenumerator.htm language=enus -->
## TOPIC 00138: DIChannelCollectionGetEnumerator Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_dichannelcollection_getenumerator.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_dichannelcollection_getenumerator.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DIChannelCollection.GetEnumerator Method

### DIChannelCollectionGetEnumerator Method

Returns an enumerator that you can use to iterate through the collection.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual IEnumerator GetEnumerator()
```

```text
Public Overridable Function GetEnumerator As IEnumerator
```

###### Return Value

IEnumerator

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

DIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_dichannelcollection_tostring.htm language=enus -->
## TOPIC 00139: DIChannelCollectionToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_dichannelcollection_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_dichannelcollection_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DIChannelCollection.ToString Method

### DIChannelCollectionToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

DIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader__ctor.htm language=enus -->
## TOPIC 00140: DigitalMultiChannelReader Constructor

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader__ctor.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader Constructor

### DigitalMultiChannelReader Constructor

DigitalMultiChannelReader

DaqStream

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DigitalMultiChannelReader(
	DaqStream stream
)
```

```text
Public Sub New ( 
	stream As DaqStream
)
```

###### Parameters

- **stream**
  - Type: NationalInstruments.DAQmxDaqStreamThe DaqStream to read.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Task

Stream

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginmemoryoptimizedreadmultisampleportuint32.htm language=enus -->
## TOPIC 00141: DigitalMultiChannelReaderBeginMemoryOptimizedReadMultiSamplePortUInt32 Method (Int32, AsyncCallback, Object, UInt32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginmemoryoptimizedreadmultisampleportuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginmemoryoptimizedreadmultisampleportuint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.BeginMemoryOptimizedReadMultiSamplePortUInt32 Method (Int32, AsyncCallback, Object, UInt32[,])

### DigitalMultiChannelReaderBeginMemoryOptimizedReadMultiSamplePortUInt32 Method (Int32, AsyncCallback, Object, UInt32)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt32(
	int samplesPerChannel,
	AsyncCallback callback,
	Object state,
	uint[,] data
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSamplePortUInt32 ( 
	samplesPerChannel As Integer,
	callback As AsyncCallback,
	state As Object,
	data As UInteger(,)
) As IAsyncResult
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallback An optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObject A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemUInt32 An initialized 2D array of 32-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
this method, call [EndMemoryOptimizedReadMultiSamplePortUInt32(IAsyncResult, Int32)](m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadmultisampleportuint32.htm)
with the returned
IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

BeginMemoryOptimizedReadMultiSamplePortUInt32 Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginreadsinglesamplemultiline.htm language=enus -->
## TOPIC 00142: DigitalMultiChannelReaderBeginReadSingleSampleMultiLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginreadsinglesamplemultiline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginreadsinglesamplemultiline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.BeginReadSingleSampleMultiLine Method

### DigitalMultiChannelReaderBeginReadSingleSampleMultiLine Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadSingleSampleMultiLine(
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadSingleSampleMultiLine ( 
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSampleMultiLine(AsyncCallback, Object), call [EndReadSingleSampleMultiLine(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesamplemultiline.htm) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginreadsinglesampleportuint16.htm language=enus -->
## TOPIC 00143: DigitalMultiChannelReaderBeginReadSingleSamplePortUInt16 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginreadsinglesampleportuint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginreadsinglesampleportuint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.BeginReadSingleSamplePortUInt16 Method

### DigitalMultiChannelReaderBeginReadSingleSamplePortUInt16 Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadSingleSamplePortUInt16(
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadSingleSamplePortUInt16 ( 
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePortUInt16(AsyncCallback, Object), call [EndReadSingleSamplePortUInt16(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesampleportuint16.htm) with the returned IAsyncResult.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginreadwaveform.htm language=enus -->
## TOPIC 00144: DigitalMultiChannelReaderBeginReadWaveform Method (Int32, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginreadwaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginreadwaveform.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.BeginReadWaveform Method (Int32, AsyncCallback, Object)

### DigitalMultiChannelReaderBeginReadWaveform Method (Int32, AsyncCallback, Object)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadWaveform(
	int samplesPerChannel,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadWaveform ( 
	samplesPerChannel As Integer,
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadWaveform(Int32, AsyncCallback, Object), call [EndReadWaveform(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelreader_endreadwaveform.htm) with the returned IAsyncResult.

The data returned from digital waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

BeginReadWaveform Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginreadwaveform_1.htm language=enus -->
## TOPIC 00145: DigitalMultiChannelReaderBeginReadWaveform Method (TimeSpan, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginreadwaveform_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginreadwaveform_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.BeginReadWaveform Method (TimeSpan, AsyncCallback, Object)

### DigitalMultiChannelReaderBeginReadWaveform Method (TimeSpan, AsyncCallback, Object)

DIChannel

duration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadWaveform(
	TimeSpan duration,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadWaveform ( 
	duration As TimeSpan,
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **duration**
  - Type: SystemTimeSpanThe duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

BeginReadWaveform(TimeSpan, AsyncCallback, Object)

EndReadWaveform(IAsyncResult)

IAsyncResult

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the [Stream](p_nationalinstruments_daqmx_task_stream.htm) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

BeginReadWaveform Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadmultisampleportbyte.htm language=enus -->
## TOPIC 00146: DigitalMultiChannelReaderEndMemoryOptimizedReadMultiSamplePortByte Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadmultisampleportbyte.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadmultisampleportbyte.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndMemoryOptimizedReadMultiSamplePortByte Method

### DigitalMultiChannelReaderEndMemoryOptimizedReadMultiSamplePortByte Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public byte[,] EndMemoryOptimizedReadMultiSamplePortByte(
	IAsyncResult asyncResult,
	out int actualNumberOfSamplesPerChannelRead
)
```

```text
Public Function EndMemoryOptimizedReadMultiSamplePortByte ( 
	asyncResult As IAsyncResult,
	<OutAttribute> ByRef actualNumberOfSamplesPerChannelRead As Integer
) As Byte(,)
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResult An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePortByte(Int32, AsyncCallback, Object, Byte).
- **actualNumberOfSamplesPerChannelRead**
  - Type: SystemInt32 The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

Byte

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePortByte(Int32, AsyncCallback, Object, Byte). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call
this method
before the asynchronous read
IAsyncResult
is complete,
it
waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadmultisampleportint32.htm language=enus -->
## TOPIC 00147: DigitalMultiChannelReaderEndMemoryOptimizedReadMultiSamplePortInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadmultisampleportint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadmultisampleportint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndMemoryOptimizedReadMultiSamplePortInt32 Method

### DigitalMultiChannelReaderEndMemoryOptimizedReadMultiSamplePortInt32 Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public int[,] EndMemoryOptimizedReadMultiSamplePortInt32(
	IAsyncResult asyncResult,
	out int actualNumberOfSamplesPerChannelRead
)
```

```text
Public Function EndMemoryOptimizedReadMultiSamplePortInt32 ( 
	asyncResult As IAsyncResult,
	<OutAttribute> ByRef actualNumberOfSamplesPerChannelRead As Integer
) As Integer(,)
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResult An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePortInt32(Int32, AsyncCallback, Object, Int32).
- **actualNumberOfSamplesPerChannelRead**
  - Type: SystemInt32 The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

Int32

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePortInt32(Int32, AsyncCallback, Object, Int32). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call
this method
before the asynchronous read
IAsyncResult
is complete,
it
waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadmultisampleportuint16.htm language=enus -->
## TOPIC 00148: DigitalMultiChannelReaderEndMemoryOptimizedReadMultiSamplePortUInt16 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadmultisampleportuint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadmultisampleportuint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndMemoryOptimizedReadMultiSamplePortUInt16 Method

### DigitalMultiChannelReaderEndMemoryOptimizedReadMultiSamplePortUInt16 Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public ushort[,] EndMemoryOptimizedReadMultiSamplePortUInt16(
	IAsyncResult asyncResult,
	out int actualNumberOfSamplesPerChannelRead
)
```

```text
Public Function EndMemoryOptimizedReadMultiSamplePortUInt16 ( 
	asyncResult As IAsyncResult,
	<OutAttribute> ByRef actualNumberOfSamplesPerChannelRead As Integer
) As UShort(,)
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResult An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePortUInt16(Int32, AsyncCallback, Object, UInt16).
- **actualNumberOfSamplesPerChannelRead**
  - Type: SystemInt32 The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

UInt16

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePortUInt16(Int32, AsyncCallback, Object, UInt16). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call
this method
before the asynchronous read
IAsyncResult
is complete,
it
waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadmultisampleportuint32.htm language=enus -->
## TOPIC 00149: DigitalMultiChannelReaderEndMemoryOptimizedReadMultiSamplePortUInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadmultisampleportuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadmultisampleportuint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndMemoryOptimizedReadMultiSamplePortUInt32 Method

### DigitalMultiChannelReaderEndMemoryOptimizedReadMultiSamplePortUInt32 Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public uint[,] EndMemoryOptimizedReadMultiSamplePortUInt32(
	IAsyncResult asyncResult,
	out int actualNumberOfSamplesPerChannelRead
)
```

```text
Public Function EndMemoryOptimizedReadMultiSamplePortUInt32 ( 
	asyncResult As IAsyncResult,
	<OutAttribute> ByRef actualNumberOfSamplesPerChannelRead As Integer
) As UInteger(,)
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResult An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePortUInt32(Int32, AsyncCallback, Object, UInt32).
- **actualNumberOfSamplesPerChannelRead**
  - Type: SystemInt32 The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

UInt32

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePortUInt32(Int32, AsyncCallback, Object, UInt32). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call
this method
before the asynchronous read
IAsyncResult
is complete,
it
waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadsinglesamplemultiline.htm language=enus -->
## TOPIC 00150: DigitalMultiChannelReaderEndMemoryOptimizedReadSingleSampleMultiLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadsinglesamplemultiline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadsinglesamplemultiline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndMemoryOptimizedReadSingleSampleMultiLine Method

### DigitalMultiChannelReaderEndMemoryOptimizedReadSingleSampleMultiLine Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool[,] EndMemoryOptimizedReadSingleSampleMultiLine(
	IAsyncResult asyncResult
)
```

```text
Public Function EndMemoryOptimizedReadSingleSampleMultiLine ( 
	asyncResult As IAsyncResult
) As Boolean(,)
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, Object, Boolean).

###### Return Value

Boolean

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; or asyncResult is or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, Object, Boolean). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call
this method
before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadmultisampleportbyte.htm language=enus -->
## TOPIC 00151: DigitalMultiChannelReaderEndReadMultiSamplePortByte Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadmultisampleportbyte.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadmultisampleportbyte.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndReadMultiSamplePortByte Method

### DigitalMultiChannelReaderEndReadMultiSamplePortByte Method

BeginReadMultiSamplePortByte(Int32, AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public byte[,] EndReadMultiSamplePortByte(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadMultiSamplePortByte ( 
	asyncResult As IAsyncResult
) As Byte(,)
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePortByte(Int32, AsyncCallback, Object).

###### Return Value

Byte

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePortByte(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadMultiSamplePortByte(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePortByte(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadmultisampleportint16.htm language=enus -->
## TOPIC 00152: DigitalMultiChannelReaderEndReadMultiSamplePortInt16 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadmultisampleportint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadmultisampleportint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndReadMultiSamplePortInt16 Method

### DigitalMultiChannelReaderEndReadMultiSamplePortInt16 Method

BeginReadMultiSamplePortInt16(Int32, AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public short[,] EndReadMultiSamplePortInt16(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadMultiSamplePortInt16 ( 
	asyncResult As IAsyncResult
) As Short(,)
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePortInt16(Int32, AsyncCallback, Object).

###### Return Value

Int16

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePortInt16(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadMultiSamplePortInt16(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePortInt16(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadmultisampleportint32.htm language=enus -->
## TOPIC 00153: DigitalMultiChannelReaderEndReadMultiSamplePortInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadmultisampleportint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadmultisampleportint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndReadMultiSamplePortInt32 Method

### DigitalMultiChannelReaderEndReadMultiSamplePortInt32 Method

BeginReadMultiSamplePortInt32(Int32, AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public int[,] EndReadMultiSamplePortInt32(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadMultiSamplePortInt32 ( 
	asyncResult As IAsyncResult
) As Integer(,)
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePortInt32(Int32, AsyncCallback, Object).

###### Return Value

Int32

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePortInt32(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadMultiSamplePortInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePortInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadmultisampleportuint16.htm language=enus -->
## TOPIC 00154: DigitalMultiChannelReaderEndReadMultiSamplePortUInt16 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadmultisampleportuint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadmultisampleportuint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndReadMultiSamplePortUInt16 Method

### DigitalMultiChannelReaderEndReadMultiSamplePortUInt16 Method

BeginReadMultiSamplePortUInt16(Int32, AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public ushort[,] EndReadMultiSamplePortUInt16(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadMultiSamplePortUInt16 ( 
	asyncResult As IAsyncResult
) As UShort(,)
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePortUInt16(Int32, AsyncCallback, Object).

###### Return Value

UInt16

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePortUInt16(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadMultiSamplePortUInt16(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePortUInt16(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadmultisampleportuint32.htm language=enus -->
## TOPIC 00155: DigitalMultiChannelReaderEndReadMultiSamplePortUInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadmultisampleportuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadmultisampleportuint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndReadMultiSamplePortUInt32 Method

### DigitalMultiChannelReaderEndReadMultiSamplePortUInt32 Method

BeginReadMultiSamplePortUInt32(Int32, AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public uint[,] EndReadMultiSamplePortUInt32(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadMultiSamplePortUInt32 ( 
	asyncResult As IAsyncResult
) As UInteger(,)
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePortUInt32(Int32, AsyncCallback, Object).

###### Return Value

UInt32

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePortUInt32(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadMultiSamplePortUInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePortUInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesamplemultiline.htm language=enus -->
## TOPIC 00156: DigitalMultiChannelReaderEndReadSingleSampleMultiLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesamplemultiline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesamplemultiline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndReadSingleSampleMultiLine Method

### DigitalMultiChannelReaderEndReadSingleSampleMultiLine Method

BeginReadSingleSampleMultiLine(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool[,] EndReadSingleSampleMultiLine(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadSingleSampleMultiLine ( 
	asyncResult As IAsyncResult
) As Boolean(,)
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSampleMultiLine(AsyncCallback, Object).

###### Return Value

Boolean

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; or asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadSingleSampleMultiLine(AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSampleMultiLine(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSampleMultiLine(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesampleportbyte.htm language=enus -->
## TOPIC 00157: DigitalMultiChannelReaderEndReadSingleSamplePortByte Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesampleportbyte.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesampleportbyte.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndReadSingleSamplePortByte Method

### DigitalMultiChannelReaderEndReadSingleSamplePortByte Method

BeginReadSingleSamplePortByte(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public byte[] EndReadSingleSamplePortByte(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadSingleSamplePortByte ( 
	asyncResult As IAsyncResult
) As Byte()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortByte(AsyncCallback, Object).

###### Return Value

Byte

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePortByte(AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSamplePortByte(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortByte(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesampleportint16.htm language=enus -->
## TOPIC 00158: DigitalMultiChannelReaderEndReadSingleSamplePortInt16 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesampleportint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesampleportint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndReadSingleSamplePortInt16 Method

### DigitalMultiChannelReaderEndReadSingleSamplePortInt16 Method

BeginReadSingleSamplePortInt16(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public short[] EndReadSingleSamplePortInt16(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadSingleSamplePortInt16 ( 
	asyncResult As IAsyncResult
) As Short()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortInt16(AsyncCallback, Object).

###### Return Value

Int16

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePortInt16(AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSamplePortInt16(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortInt16(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesampleportint32.htm language=enus -->
## TOPIC 00159: DigitalMultiChannelReaderEndReadSingleSamplePortInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesampleportint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesampleportint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndReadSingleSamplePortInt32 Method

### DigitalMultiChannelReaderEndReadSingleSamplePortInt32 Method

BeginReadSingleSamplePortInt32(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public int[] EndReadSingleSamplePortInt32(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadSingleSamplePortInt32 ( 
	asyncResult As IAsyncResult
) As Integer()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortInt32(AsyncCallback, Object).

###### Return Value

Int32

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePortInt32(AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSamplePortInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesampleportuint16.htm language=enus -->
## TOPIC 00160: DigitalMultiChannelReaderEndReadSingleSamplePortUInt16 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesampleportuint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesampleportuint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndReadSingleSamplePortUInt16 Method

### DigitalMultiChannelReaderEndReadSingleSamplePortUInt16 Method

BeginReadSingleSamplePortUInt16(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public ushort[] EndReadSingleSamplePortUInt16(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadSingleSamplePortUInt16 ( 
	asyncResult As IAsyncResult
) As UShort()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortUInt16(AsyncCallback, Object).

###### Return Value

UInt16

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePortUInt16(AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSamplePortUInt16(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortUInt16(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesampleportuint32.htm language=enus -->
## TOPIC 00161: DigitalMultiChannelReaderEndReadSingleSamplePortUInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesampleportuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesampleportuint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndReadSingleSamplePortUInt32 Method

### DigitalMultiChannelReaderEndReadSingleSamplePortUInt32 Method

BeginReadSingleSamplePortUInt32(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public uint[] EndReadSingleSamplePortUInt32(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadSingleSamplePortUInt32 ( 
	asyncResult As IAsyncResult
) As UInteger()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortUInt32(AsyncCallback, Object).

###### Return Value

UInt32

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePortUInt32(AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSamplePortUInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortUInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesamplesingleline.htm language=enus -->
## TOPIC 00162: DigitalMultiChannelReaderEndReadSingleSampleSingleLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesamplesingleline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadsinglesamplesingleline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndReadSingleSampleSingleLine Method

### DigitalMultiChannelReaderEndReadSingleSampleSingleLine Method

BeginReadSingleSampleSingleLine(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool[] EndReadSingleSampleSingleLine(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadSingleSampleSingleLine ( 
	asyncResult As IAsyncResult
) As Boolean()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSampleSingleLine(AsyncCallback, Object).

###### Return Value

Boolean

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadSingleSampleSingleLine(AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSampleSingleLine(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSampleSingleLine(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadwaveform.htm language=enus -->
## TOPIC 00163: DigitalMultiChannelReaderEndReadWaveform Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadwaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_endreadwaveform.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.EndReadWaveform Method

### DigitalMultiChannelReaderEndReadWaveform Method

BeginReadWaveform(Int32, AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DigitalWaveform[] EndReadWaveform(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadWaveform ( 
	asyncResult As IAsyncResult
) As DigitalWaveform()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadWaveform(Int32, AsyncCallback, Object).

###### Return Value

DigitalWaveform

DigitalWaveform

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadWaveform(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadWaveform(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadWaveform(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportbyte.htm language=enus -->
## TOPIC 00164: DigitalMultiChannelReaderMemoryOptimizedReadMultiSamplePortByte Method (Int32, Byte, ReallocationPolicy, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportbyte.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportbyte.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.MemoryOptimizedReadMultiSamplePortByte Method (Int32, Byte[,], ReallocationPolicy, Int32)

### DigitalMultiChannelReaderMemoryOptimizedReadMultiSamplePortByte Method (Int32, Byte, ReallocationPolicy, Int32)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public byte[,] MemoryOptimizedReadMultiSamplePortByte(
	int samplesPerChannel,
	ref byte[,] data,
	ReallocationPolicy policy,
	out int actualNumberOfSamplesPerChannelRead
)
```

```text
Public Function MemoryOptimizedReadMultiSamplePortByte ( 
	samplesPerChannel As Integer,
	ByRef data As Byte(,),
	policy As ReallocationPolicy,
	<OutAttribute> ByRef actualNumberOfSamplesPerChannelRead As Integer
) As Byte(,)
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: SystemByte An initialized 2D array of 8-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicy Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.
- **actualNumberOfSamplesPerChannelRead**
  - Type: SystemInt32 The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

Byte

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalMultiChannelReader Class

MemoryOptimizedReadMultiSamplePortByte Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportbyte_1.htm language=enus -->
## TOPIC 00165: DigitalMultiChannelReaderMemoryOptimizedReadMultiSamplePortByte Method (Int32, Byte, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportbyte_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportbyte_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.MemoryOptimizedReadMultiSamplePortByte Method (Int32, Byte[,], Int32)

### DigitalMultiChannelReaderMemoryOptimizedReadMultiSamplePortByte Method (Int32, Byte, Int32)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public byte[,] MemoryOptimizedReadMultiSamplePortByte(
	int samplesPerChannel,
	ref byte[,] data,
	out int actualNumberOfSamplesPerChannelRead
)
```

```text
Public Function MemoryOptimizedReadMultiSamplePortByte ( 
	samplesPerChannel As Integer,
	ByRef data As Byte(,),
	<OutAttribute> ByRef actualNumberOfSamplesPerChannelRead As Integer
) As Byte(,)
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: SystemByte An initialized 2D array of 8-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.
- **actualNumberOfSamplesPerChannelRead**
  - Type: SystemInt32 The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

Byte

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; or If the first dimension of data does not match the number of channels. |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalMultiChannelReader Class

MemoryOptimizedReadMultiSamplePortByte Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportint32.htm language=enus -->
## TOPIC 00166: DigitalMultiChannelReaderMemoryOptimizedReadMultiSamplePortInt32 Method (Int32, Int32, ReallocationPolicy, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.MemoryOptimizedReadMultiSamplePortInt32 Method (Int32, Int32[,], ReallocationPolicy, Int32)

### DigitalMultiChannelReaderMemoryOptimizedReadMultiSamplePortInt32 Method (Int32, Int32, ReallocationPolicy, Int32)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public int[,] MemoryOptimizedReadMultiSamplePortInt32(
	int samplesPerChannel,
	ref int[,] data,
	ReallocationPolicy policy,
	out int actualNumberOfSamplesPerChannelRead
)
```

```text
Public Function MemoryOptimizedReadMultiSamplePortInt32 ( 
	samplesPerChannel As Integer,
	ByRef data As Integer(,),
	policy As ReallocationPolicy,
	<OutAttribute> ByRef actualNumberOfSamplesPerChannelRead As Integer
) As Integer(,)
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: SystemInt32 An initialized 2D array of 32-bit integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicy Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.
- **actualNumberOfSamplesPerChannelRead**
  - Type: SystemInt32 The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

Int32

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalMultiChannelReader Class

MemoryOptimizedReadMultiSamplePortInt32 Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportint32_1.htm language=enus -->
## TOPIC 00167: DigitalMultiChannelReaderMemoryOptimizedReadMultiSamplePortInt32 Method (Int32, Int32, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportint32_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportint32_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.MemoryOptimizedReadMultiSamplePortInt32 Method (Int32, Int32[,], Int32)

### DigitalMultiChannelReaderMemoryOptimizedReadMultiSamplePortInt32 Method (Int32, Int32, Int32)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public int[,] MemoryOptimizedReadMultiSamplePortInt32(
	int samplesPerChannel,
	ref int[,] data,
	out int actualNumberOfSamplesPerChannelRead
)
```

```text
Public Function MemoryOptimizedReadMultiSamplePortInt32 ( 
	samplesPerChannel As Integer,
	ByRef data As Integer(,),
	<OutAttribute> ByRef actualNumberOfSamplesPerChannelRead As Integer
) As Integer(,)
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: SystemInt32 An initialized 2D array of 32-bit integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.
- **actualNumberOfSamplesPerChannelRead**
  - Type: SystemInt32 The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

Int32

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; or If the first dimension of data does not match the number of channels. |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalMultiChannelReader Class

MemoryOptimizedReadMultiSamplePortInt32 Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportuint16.htm language=enus -->
## TOPIC 00168: DigitalMultiChannelReaderMemoryOptimizedReadMultiSamplePortUInt16 Method (Int32, UInt16, ReallocationPolicy, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportuint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportuint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.MemoryOptimizedReadMultiSamplePortUInt16 Method (Int32, UInt16[,], ReallocationPolicy, Int32)

### DigitalMultiChannelReaderMemoryOptimizedReadMultiSamplePortUInt16 Method (Int32, UInt16, ReallocationPolicy, Int32)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public ushort[,] MemoryOptimizedReadMultiSamplePortUInt16(
	int samplesPerChannel,
	ref ushort[,] data,
	ReallocationPolicy policy,
	out int actualNumberOfSamplesPerChannelRead
)
```

```text
Public Function MemoryOptimizedReadMultiSamplePortUInt16 ( 
	samplesPerChannel As Integer,
	ByRef data As UShort(,),
	policy As ReallocationPolicy,
	<OutAttribute> ByRef actualNumberOfSamplesPerChannelRead As Integer
) As UShort(,)
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: SystemUInt16 An initialized 2D array of 16-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicy Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.
- **actualNumberOfSamplesPerChannelRead**
  - Type: SystemInt32 The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

UInt16

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalMultiChannelReader Class

MemoryOptimizedReadMultiSamplePortUInt16 Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportuint16_1.htm language=enus -->
## TOPIC 00169: DigitalMultiChannelReaderMemoryOptimizedReadMultiSamplePortUInt16 Method (Int32, UInt16, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportuint16_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportuint16_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.MemoryOptimizedReadMultiSamplePortUInt16 Method (Int32, UInt16[,], Int32)

### DigitalMultiChannelReaderMemoryOptimizedReadMultiSamplePortUInt16 Method (Int32, UInt16, Int32)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public ushort[,] MemoryOptimizedReadMultiSamplePortUInt16(
	int samplesPerChannel,
	ref ushort[,] data,
	out int actualNumberOfSamplesPerChannelRead
)
```

```text
Public Function MemoryOptimizedReadMultiSamplePortUInt16 ( 
	samplesPerChannel As Integer,
	ByRef data As UShort(,),
	<OutAttribute> ByRef actualNumberOfSamplesPerChannelRead As Integer
) As UShort(,)
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: SystemUInt16 An initialized 2D array of 16-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.
- **actualNumberOfSamplesPerChannelRead**
  - Type: SystemInt32 The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

UInt16

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; or If the first dimension of data does not match the number of channels. |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalMultiChannelReader Class

MemoryOptimizedReadMultiSamplePortUInt16 Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportuint32.htm language=enus -->
## TOPIC 00170: DigitalMultiChannelReaderMemoryOptimizedReadMultiSamplePortUInt32 Method (Int32, UInt32, ReallocationPolicy, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportuint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.MemoryOptimizedReadMultiSamplePortUInt32 Method (Int32, UInt32[,], ReallocationPolicy, Int32)

### DigitalMultiChannelReaderMemoryOptimizedReadMultiSamplePortUInt32 Method (Int32, UInt32, ReallocationPolicy, Int32)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public uint[,] MemoryOptimizedReadMultiSamplePortUInt32(
	int samplesPerChannel,
	ref uint[,] data,
	ReallocationPolicy policy,
	out int actualNumberOfSamplesPerChannelRead
)
```

```text
Public Function MemoryOptimizedReadMultiSamplePortUInt32 ( 
	samplesPerChannel As Integer,
	ByRef data As UInteger(,),
	policy As ReallocationPolicy,
	<OutAttribute> ByRef actualNumberOfSamplesPerChannelRead As Integer
) As UInteger(,)
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: SystemUInt32 An initialized 2D array of 32-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicy Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.
- **actualNumberOfSamplesPerChannelRead**
  - Type: SystemInt32 The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

UInt32

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalMultiChannelReader Class

MemoryOptimizedReadMultiSamplePortUInt32 Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportuint32_1.htm language=enus -->
## TOPIC 00171: DigitalMultiChannelReaderMemoryOptimizedReadMultiSamplePortUInt32 Method (Int32, UInt32, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportuint32_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadmultisampleportuint32_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.MemoryOptimizedReadMultiSamplePortUInt32 Method (Int32, UInt32[,], Int32)

### DigitalMultiChannelReaderMemoryOptimizedReadMultiSamplePortUInt32 Method (Int32, UInt32, Int32)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public uint[,] MemoryOptimizedReadMultiSamplePortUInt32(
	int samplesPerChannel,
	ref uint[,] data,
	out int actualNumberOfSamplesPerChannelRead
)
```

```text
Public Function MemoryOptimizedReadMultiSamplePortUInt32 ( 
	samplesPerChannel As Integer,
	ByRef data As UInteger(,),
	<OutAttribute> ByRef actualNumberOfSamplesPerChannelRead As Integer
) As UInteger(,)
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: SystemUInt32 An initialized 2D array of 32-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.
- **actualNumberOfSamplesPerChannelRead**
  - Type: SystemInt32 The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

UInt32

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; or If the first dimension of data does not match the number of channels. |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalMultiChannelReader Class

MemoryOptimizedReadMultiSamplePortUInt32 Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadsinglesamplemultiline.htm language=enus -->
## TOPIC 00172: DigitalMultiChannelReaderMemoryOptimizedReadSingleSampleMultiLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadsinglesamplemultiline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_memoryoptimizedreadsinglesamplemultiline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.MemoryOptimizedReadSingleSampleMultiLine Method

### DigitalMultiChannelReaderMemoryOptimizedReadSingleSampleMultiLine Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool[,] MemoryOptimizedReadSingleSampleMultiLine(
	bool[,] data
)
```

```text
Public Function MemoryOptimizedReadSingleSampleMultiLine ( 
	data As Boolean(,)
) As Boolean(,)
```

###### Parameters

- **data**
  - Type: SystemBooleanAn initialized 2D array of boolean samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a line in that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead

###### Return Value

Boolean

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; or If the first dimension of data does not match the number of channels. |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readmultisampleportbyte.htm language=enus -->
## TOPIC 00173: DigitalMultiChannelReaderReadMultiSamplePortByte Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readmultisampleportbyte.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readmultisampleportbyte.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.ReadMultiSamplePortByte Method

### DigitalMultiChannelReaderReadMultiSamplePortByte Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public byte[,] ReadMultiSamplePortByte(
	int samplesPerChannel
)
```

```text
Public Function ReadMultiSamplePortByte ( 
	samplesPerChannel As Integer
) As Byte(,)
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.

###### Return Value

Byte

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

Use this method for devices with up to eight lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readmultisampleportint16.htm language=enus -->
## TOPIC 00174: DigitalMultiChannelReaderReadMultiSamplePortInt16 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readmultisampleportint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readmultisampleportint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.ReadMultiSamplePortInt16 Method

### DigitalMultiChannelReaderReadMultiSamplePortInt16 Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public short[,] ReadMultiSamplePortInt16(
	int samplesPerChannel
)
```

```text
Public Function ReadMultiSamplePortInt16 ( 
	samplesPerChannel As Integer
) As Short(,)
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.

###### Return Value

Int16

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readmultisampleportint32.htm language=enus -->
## TOPIC 00175: DigitalMultiChannelReaderReadMultiSamplePortInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readmultisampleportint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readmultisampleportint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.ReadMultiSamplePortInt32 Method

### DigitalMultiChannelReaderReadMultiSamplePortInt32 Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public int[,] ReadMultiSamplePortInt32(
	int samplesPerChannel
)
```

```text
Public Function ReadMultiSamplePortInt32 ( 
	samplesPerChannel As Integer
) As Integer(,)
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.

###### Return Value

Int32

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readmultisampleportuint16.htm language=enus -->
## TOPIC 00176: DigitalMultiChannelReaderReadMultiSamplePortUInt16 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readmultisampleportuint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readmultisampleportuint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.ReadMultiSamplePortUInt16 Method

### DigitalMultiChannelReaderReadMultiSamplePortUInt16 Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public ushort[,] ReadMultiSamplePortUInt16(
	int samplesPerChannel
)
```

```text
Public Function ReadMultiSamplePortUInt16 ( 
	samplesPerChannel As Integer
) As UShort(,)
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.

###### Return Value

UInt16

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readmultisampleportuint32.htm language=enus -->
## TOPIC 00177: DigitalMultiChannelReaderReadMultiSamplePortUInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readmultisampleportuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readmultisampleportuint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.ReadMultiSamplePortUInt32 Method

### DigitalMultiChannelReaderReadMultiSamplePortUInt32 Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public uint[,] ReadMultiSamplePortUInt32(
	int samplesPerChannel
)
```

```text
Public Function ReadMultiSamplePortUInt32 ( 
	samplesPerChannel As Integer
) As UInteger(,)
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.

###### Return Value

UInt32

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesamplemultiline.htm language=enus -->
## TOPIC 00178: DigitalMultiChannelReaderReadSingleSampleMultiLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesamplemultiline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesamplemultiline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.ReadSingleSampleMultiLine Method

### DigitalMultiChannelReaderReadSingleSampleMultiLine Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool[,] ReadSingleSampleMultiLine()
```

```text
Public Function ReadSingleSampleMultiLine As Boolean(,)
```

###### Return Value

Boolean

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportbyte.htm language=enus -->
## TOPIC 00179: DigitalMultiChannelReaderReadSingleSamplePortByte Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportbyte.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportbyte.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.ReadSingleSamplePortByte Method

### DigitalMultiChannelReaderReadSingleSamplePortByte Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public byte[] ReadSingleSamplePortByte()
```

```text
Public Function ReadSingleSamplePortByte As Byte()
```

###### Return Value

Byte

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

Use this method for devices with up to eight lines per port.

##### Remarks

Timeout

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportint16.htm language=enus -->
## TOPIC 00180: DigitalMultiChannelReaderReadSingleSamplePortInt16 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.ReadSingleSamplePortInt16 Method

### DigitalMultiChannelReaderReadSingleSamplePortInt16 Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public short[] ReadSingleSamplePortInt16()
```

```text
Public Function ReadSingleSamplePortInt16 As Short()
```

###### Return Value

Int16

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

Use this method for devices with up to 16 lines per port.

##### Remarks

Timeout

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportint32.htm language=enus -->
## TOPIC 00181: DigitalMultiChannelReaderReadSingleSamplePortInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.ReadSingleSamplePortInt32 Method

### DigitalMultiChannelReaderReadSingleSamplePortInt32 Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public int[] ReadSingleSamplePortInt32()
```

```text
Public Function ReadSingleSamplePortInt32 As Integer()
```

###### Return Value

Int32

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

Use this method for devices with up to 32 lines per port.

##### Remarks

Timeout

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportuint16.htm language=enus -->
## TOPIC 00182: DigitalMultiChannelReaderReadSingleSamplePortUInt16 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportuint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportuint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.ReadSingleSamplePortUInt16 Method

### DigitalMultiChannelReaderReadSingleSamplePortUInt16 Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public ushort[] ReadSingleSamplePortUInt16()
```

```text
Public Function ReadSingleSamplePortUInt16 As UShort()
```

###### Return Value

UInt16

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportuint32.htm language=enus -->
## TOPIC 00183: DigitalMultiChannelReaderReadSingleSamplePortUInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportuint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.ReadSingleSamplePortUInt32 Method

### DigitalMultiChannelReaderReadSingleSamplePortUInt32 Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public uint[] ReadSingleSamplePortUInt32()
```

```text
Public Function ReadSingleSamplePortUInt32 As UInteger()
```

###### Return Value

UInt32

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesamplesingleline.htm language=enus -->
## TOPIC 00184: DigitalMultiChannelReaderReadSingleSampleSingleLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesamplesingleline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesamplesingleline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.ReadSingleSampleSingleLine Method

### DigitalMultiChannelReaderReadSingleSampleSingleLine Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool[] ReadSingleSampleSingleLine()
```

```text
Public Function ReadSingleSampleSingleLine As Boolean()
```

###### Return Value

Boolean

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

Timeout

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readwaveform.htm language=enus -->
## TOPIC 00185: DigitalMultiChannelReaderReadWaveform Method (Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readwaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readwaveform.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.ReadWaveform Method (Int32)

### DigitalMultiChannelReaderReadWaveform Method (Int32)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DigitalWaveform[] ReadWaveform(
	int samplesPerChannel
)
```

```text
Public Function ReadWaveform ( 
	samplesPerChannel As Integer
) As DigitalWaveform()
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32 The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.

###### Return Value

DigitalWaveform

DigitalWaveform

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

The data returned from digital waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalMultiChannelReader Class

ReadWaveform Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readwaveform_1.htm language=enus -->
## TOPIC 00186: DigitalMultiChannelReaderReadWaveform Method (TimeSpan)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readwaveform_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readwaveform_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.ReadWaveform Method (TimeSpan)

### DigitalMultiChannelReaderReadWaveform Method (TimeSpan)

DIChannel

duration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DigitalWaveform[] ReadWaveform(
	TimeSpan duration
)
```

```text
Public Function ReadWaveform ( 
	duration As TimeSpan
) As DigitalWaveform()
```

###### Parameters

- **duration**
  - Type: SystemTimeSpanThe duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate.

###### Return Value

DigitalWaveform

DigitalWaveform

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If the duration provided was less than Zero. |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

DAQ Assistant

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the [Stream](p_nationalinstruments_daqmx_task_stream.htm) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalMultiChannelReader Class

ReadWaveform Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_tostring.htm language=enus -->
## TOPIC 00187: DigitalMultiChannelReaderToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.ToString Method

### DigitalMultiChannelReaderToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter__ctor.htm language=enus -->
## TOPIC 00188: DigitalMultiChannelWriter Constructor

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter__ctor.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter Constructor

### DigitalMultiChannelWriter Constructor

DigitalMultiChannelWriter

DaqStream

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DigitalMultiChannelWriter(
	DaqStream stream
)
```

```text
Public Sub New ( 
	stream As DaqStream
)
```

###### Parameters

- **stream**
  - Type: NationalInstruments.DAQmxDaqStreamThe DaqStream to write to.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Task

Stream

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

DigitalMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport.htm language=enus -->
## TOPIC 00189: DigitalMultiChannelWriterBeginWriteMultiSamplePort Method (Boolean, Byte, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.BeginWriteMultiSamplePort Method (Boolean, Byte[,], AsyncCallback, Object)

### DigitalMultiChannelWriterBeginWriteMultiSamplePort Method (Boolean, Byte, AsyncCallback, Object)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteMultiSamplePort(
	bool autoStart,
	byte[,] data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteMultiSamplePort ( 
	autoStart As Boolean,
	data As Byte(,),
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemByteA 2D array of 8-bit integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 8 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelWriter Class

BeginWriteMultiSamplePort Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_1.htm language=enus -->
## TOPIC 00190: DigitalMultiChannelWriterBeginWriteMultiSamplePort Method (Boolean, Int16, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.BeginWriteMultiSamplePort Method (Boolean, Int16[,], AsyncCallback, Object)

### DigitalMultiChannelWriterBeginWriteMultiSamplePort Method (Boolean, Int16, AsyncCallback, Object)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteMultiSamplePort(
	bool autoStart,
	short[,] data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteMultiSamplePort ( 
	autoStart As Boolean,
	data As Short(,),
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemInt16A 2D array of 16-bit integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method 
for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelWriter Class

BeginWriteMultiSamplePort Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_2.htm language=enus -->
## TOPIC 00191: DigitalMultiChannelWriterBeginWriteMultiSamplePort Method (Boolean, Int32, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_2.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.BeginWriteMultiSamplePort Method (Boolean, Int32[,], AsyncCallback, Object)

### DigitalMultiChannelWriterBeginWriteMultiSamplePort Method (Boolean, Int32, AsyncCallback, Object)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteMultiSamplePort(
	bool autoStart,
	int[,] data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteMultiSamplePort ( 
	autoStart As Boolean,
	data As Integer(,),
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemInt32A 2D array of 32-bit integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method 
for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelWriter Class

BeginWriteMultiSamplePort Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_3.htm language=enus -->
## TOPIC 00192: DigitalMultiChannelWriterBeginWriteMultiSamplePort Method (Boolean, UInt16, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_3.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.BeginWriteMultiSamplePort Method (Boolean, UInt16[,], AsyncCallback, Object)

### DigitalMultiChannelWriterBeginWriteMultiSamplePort Method (Boolean, UInt16, AsyncCallback, Object)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteMultiSamplePort(
	bool autoStart,
	ushort[,] data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteMultiSamplePort ( 
	autoStart As Boolean,
	data As UShort(,),
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemUInt16A 2D array of 16-bit unsigned integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelWriter Class

BeginWriteMultiSamplePort Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_4.htm language=enus -->
## TOPIC 00193: DigitalMultiChannelWriterBeginWriteMultiSamplePort Method (Boolean, UInt32, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_4.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_4.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.BeginWriteMultiSamplePort Method (Boolean, UInt32[,], AsyncCallback, Object)

### DigitalMultiChannelWriterBeginWriteMultiSamplePort Method (Boolean, UInt32, AsyncCallback, Object)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteMultiSamplePort(
	bool autoStart,
	uint[,] data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteMultiSamplePort ( 
	autoStart As Boolean,
	data As UInteger(,),
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemUInt32A 2D array of 32-bit unsigned integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelWriter Class

BeginWriteMultiSamplePort Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesamplemultiline.htm language=enus -->
## TOPIC 00194: DigitalMultiChannelWriterBeginWriteSingleSampleMultiLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesamplemultiline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesamplemultiline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.BeginWriteSingleSampleMultiLine Method

### DigitalMultiChannelWriterBeginWriteSingleSampleMultiLine Method

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteSingleSampleMultiLine(
	bool autoStart,
	bool[,] data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteSingleSampleMultiLine ( 
	autoStart As Boolean,
	data As Boolean(,),
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemBooleanA 2D array of Boolean samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a line in that channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesampleport.htm language=enus -->
## TOPIC 00195: DigitalMultiChannelWriterBeginWriteSingleSamplePort Method (Boolean, Byte, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesampleport.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesampleport.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.BeginWriteSingleSamplePort Method (Boolean, Byte[], AsyncCallback, Object)

### DigitalMultiChannelWriterBeginWriteSingleSamplePort Method (Boolean, Byte, AsyncCallback, Object)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteSingleSamplePort(
	bool autoStart,
	byte[] data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteSingleSamplePort ( 
	autoStart As Boolean,
	data As Byte(),
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemByteA 1D array of 8-bit unsigned integer samples to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to eight lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelWriter Class

BeginWriteSingleSamplePort Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesampleport_1.htm language=enus -->
## TOPIC 00196: DigitalMultiChannelWriterBeginWriteSingleSamplePort Method (Boolean, Int16, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesampleport_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesampleport_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.BeginWriteSingleSamplePort Method (Boolean, Int16[], AsyncCallback, Object)

### DigitalMultiChannelWriterBeginWriteSingleSamplePort Method (Boolean, Int16, AsyncCallback, Object)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteSingleSamplePort(
	bool autoStart,
	short[] data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteSingleSamplePort ( 
	autoStart As Boolean,
	data As Short(),
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemInt16A 2D array of 16-bit integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelWriter Class

BeginWriteSingleSamplePort Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesampleport_2.htm language=enus -->
## TOPIC 00197: DigitalMultiChannelWriterBeginWriteSingleSamplePort Method (Boolean, Int32, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesampleport_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesampleport_2.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.BeginWriteSingleSamplePort Method (Boolean, Int32[], AsyncCallback, Object)

### DigitalMultiChannelWriterBeginWriteSingleSamplePort Method (Boolean, Int32, AsyncCallback, Object)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteSingleSamplePort(
	bool autoStart,
	int[] data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteSingleSamplePort ( 
	autoStart As Boolean,
	data As Integer(),
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemInt32A 2D array of 32-bit integer samples to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelWriter Class

BeginWriteSingleSamplePort Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesampleport_3.htm language=enus -->
## TOPIC 00198: DigitalMultiChannelWriterBeginWriteSingleSamplePort Method (Boolean, UInt16, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesampleport_3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesampleport_3.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.BeginWriteSingleSamplePort Method (Boolean, UInt16[], AsyncCallback, Object)

### DigitalMultiChannelWriterBeginWriteSingleSamplePort Method (Boolean, UInt16, AsyncCallback, Object)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteSingleSamplePort(
	bool autoStart,
	ushort[] data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteSingleSamplePort ( 
	autoStart As Boolean,
	data As UShort(),
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemUInt16A 2D array of 16-bit unsigned integer samples to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelWriter Class

BeginWriteSingleSamplePort Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesampleport_4.htm language=enus -->
## TOPIC 00199: DigitalMultiChannelWriterBeginWriteSingleSamplePort Method (Boolean, UInt32, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesampleport_4.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesampleport_4.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.BeginWriteSingleSamplePort Method (Boolean, UInt32[], AsyncCallback, Object)

### DigitalMultiChannelWriterBeginWriteSingleSamplePort Method (Boolean, UInt32, AsyncCallback, Object)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteSingleSamplePort(
	bool autoStart,
	uint[] data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteSingleSamplePort ( 
	autoStart As Boolean,
	data As UInteger(),
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemUInt32A 2D array of 32-bit unsigned integer samples to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelWriter Class

BeginWriteSingleSamplePort Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesamplesingleline.htm language=enus -->
## TOPIC 00200: DigitalMultiChannelWriterBeginWriteSingleSampleSingleLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesamplesingleline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesamplesingleline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.BeginWriteSingleSampleSingleLine Method

### DigitalMultiChannelWriterBeginWriteSingleSampleSingleLine Method

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteSingleSampleSingleLine(
	bool autoStart,
	bool[] data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteSingleSampleSingleLine ( 
	autoStart As Boolean,
	data As Boolean(),
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemBooleanA 1D array of Boolean samples to write to the task. Each element of the array corresponds to a channel within the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

This method fails if the channels in the task contain more than one digital line.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritewaveform.htm language=enus -->
## TOPIC 00201: DigitalMultiChannelWriterBeginWriteWaveform Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritewaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritewaveform.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.BeginWriteWaveform Method

### DigitalMultiChannelWriterBeginWriteWaveform Method

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginWriteWaveform(
	bool autoStart,
	DigitalWaveform[] data,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginWriteWaveform ( 
	autoStart As Boolean,
	data As DigitalWaveform(),
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: NationalInstrumentsDigitalWaveformA 1D array of DigitalWaveform objects to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. The order of the lines in the digital waveform corresponds to the order in which you add the lines to the channel.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the write is complete. Specify if you do not want a callback when the write is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelwriter_endwrite.htm) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Digital waveform writes are not affected by the SampleInterval or StartTime properties on the DigitalWaveform. To configure timing for digital waveform writes, use the [ConfigureSampleClock](overload_nationalinstruments_daqmx_timing_configuresampleclock.htm) method.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_endwrite.htm language=enus -->
## TOPIC 00202: DigitalMultiChannelWriterEndWrite Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_endwrite.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_endwrite.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.EndWrite Method

### DigitalMultiChannelWriterEndWrite Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void EndWrite(
	IAsyncResult asyncResult
)
```

```text
Public Sub EndWrite ( 
	asyncResult As IAsyncResult
)
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginWriteMultiSamplePort(Boolean, UInt32, AsyncCallback, Object), BeginWriteSingleSamplePort(Boolean, UInt32, AsyncCallback, Object), BeginWriteSingleSampleMultiLine(Boolean, Boolean, AsyncCallback, Object), BeginWriteSingleSampleSingleLine(Boolean, Boolean, AsyncCallback, Object), or BeginWriteWaveform(Boolean, DigitalWaveform, AsyncCallback, Object).

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginWriteMultiSamplePort(Boolean, UInt32, AsyncCallback, Object), BeginWriteSingleSamplePort(Boolean, UInt32, AsyncCallback, Object), BeginWriteSingleSampleMultiLine(Boolean, Boolean, AsyncCallback, Object), BeginWriteSingleSampleSingleLine(Boolean, Boolean, AsyncCallback, Object), or BeginWriteWaveform(Boolean, DigitalWaveform, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| IndexOutOfRangeException | The data passed to BeginWriteMultiSamplePort(Boolean, UInt32, AsyncCallback, Object), BeginWriteSingleSamplePort(Boolean, UInt32, AsyncCallback, Object), BeginWriteSingleSampleMultiLine(Boolean, Boolean, AsyncCallback, Object), BeginWriteSingleSampleSingleLine(Boolean, Boolean, AsyncCallback, Object), or BeginWriteWaveform(Boolean, DigitalWaveform, AsyncCallback, Object) has a non-zero lower bound. |

##### Remarks

If you call EndWrite(IAsyncResult) before the asynchronous write represented by the provided IAsyncResult is complete, EndWrite(IAsyncResult) waits for the write to complete before returning. For a write to a buffered task, the write is considered complete when all of the written samples have been transferred to the task buffer. Use [IsDone](p_nationalinstruments_daqmx_task_isdone.htm) or [WaitUntilDone(Int32)](m_nationalinstruments_daqmx_task_waituntildone_1.htm) on the [Task](t_nationalinstruments_daqmx_task.htm) object to determine if a task has generated all of the data it was configured to generate.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_tostring.htm language=enus -->
## TOPIC 00203: DigitalMultiChannelWriterToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.ToString Method

### DigitalMultiChannelWriterToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

DigitalMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport.htm language=enus -->
## TOPIC 00204: DigitalMultiChannelWriterWriteMultiSamplePort Method (Boolean, Byte)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.WriteMultiSamplePort Method (Boolean, Byte[,])

### DigitalMultiChannelWriterWriteMultiSamplePort Method (Boolean, Byte)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteMultiSamplePort(
	bool autoStart,
	byte[,] data
)
```

```text
Public Sub WriteMultiSamplePort ( 
	autoStart As Boolean,
	data As Byte(,)
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemByteA 2D array of 8-bit unsigned integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

##### See Also

###### Reference

DigitalMultiChannelWriter Class

WriteMultiSamplePort Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport_1.htm language=enus -->
## TOPIC 00205: DigitalMultiChannelWriterWriteMultiSamplePort Method (Boolean, Int16)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.WriteMultiSamplePort Method (Boolean, Int16[,])

### DigitalMultiChannelWriterWriteMultiSamplePort Method (Boolean, Int16)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteMultiSamplePort(
	bool autoStart,
	short[,] data
)
```

```text
Public Sub WriteMultiSamplePort ( 
	autoStart As Boolean,
	data As Short(,)
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemInt16A 2D array of 16-bit unsigned integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

##### See Also

###### Reference

DigitalMultiChannelWriter Class

WriteMultiSamplePort Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport_2.htm language=enus -->
## TOPIC 00206: DigitalMultiChannelWriterWriteMultiSamplePort Method (Boolean, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport_2.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.WriteMultiSamplePort Method (Boolean, Int32[,])

### DigitalMultiChannelWriterWriteMultiSamplePort Method (Boolean, Int32)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteMultiSamplePort(
	bool autoStart,
	int[,] data
)
```

```text
Public Sub WriteMultiSamplePort ( 
	autoStart As Boolean,
	data As Integer(,)
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemInt32A 2D array of 32-bit unsigned integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

##### See Also

###### Reference

DigitalMultiChannelWriter Class

WriteMultiSamplePort Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport_3.htm language=enus -->
## TOPIC 00207: DigitalMultiChannelWriterWriteMultiSamplePort Method (Boolean, UInt16)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport_3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport_3.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.WriteMultiSamplePort Method (Boolean, UInt16[,])

### DigitalMultiChannelWriterWriteMultiSamplePort Method (Boolean, UInt16)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteMultiSamplePort(
	bool autoStart,
	ushort[,] data
)
```

```text
Public Sub WriteMultiSamplePort ( 
	autoStart As Boolean,
	data As UShort(,)
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemUInt16A 2D array of 16-bit unsigned integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

##### See Also

###### Reference

DigitalMultiChannelWriter Class

WriteMultiSamplePort Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport_4.htm language=enus -->
## TOPIC 00208: DigitalMultiChannelWriterWriteMultiSamplePort Method (Boolean, UInt32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport_4.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport_4.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.WriteMultiSamplePort Method (Boolean, UInt32[,])

### DigitalMultiChannelWriterWriteMultiSamplePort Method (Boolean, UInt32)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteMultiSamplePort(
	bool autoStart,
	uint[,] data
)
```

```text
Public Sub WriteMultiSamplePort ( 
	autoStart As Boolean,
	data As UInteger(,)
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemUInt32A 2D array of 32-bit unsigned integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

##### See Also

###### Reference

DigitalMultiChannelWriter Class

WriteMultiSamplePort Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesamplemultiline.htm language=enus -->
## TOPIC 00209: DigitalMultiChannelWriterWriteSingleSampleMultiLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesamplemultiline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesamplemultiline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.WriteSingleSampleMultiLine Method

### DigitalMultiChannelWriterWriteSingleSampleMultiLine Method

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteSingleSampleMultiLine(
	bool autoStart,
	bool[,] data
)
```

```text
Public Sub WriteSingleSampleMultiLine ( 
	autoStart As Boolean,
	data As Boolean(,)
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemBooleanA 2D array of Boolean samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a line in that channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

##### Remarks

Timeout

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

##### See Also

###### Reference

DigitalMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport.htm language=enus -->
## TOPIC 00210: DigitalMultiChannelWriterWriteSingleSamplePort Method (Boolean, Byte)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.WriteSingleSamplePort Method (Boolean, Byte[])

### DigitalMultiChannelWriterWriteSingleSamplePort Method (Boolean, Byte)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteSingleSamplePort(
	bool autoStart,
	byte[] data
)
```

```text
Public Sub WriteSingleSamplePort ( 
	autoStart As Boolean,
	data As Byte()
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemByteA 1D array of 8-bit unsigned integer samples to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

##### See Also

###### Reference

DigitalMultiChannelWriter Class

WriteSingleSamplePort Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport_1.htm language=enus -->
## TOPIC 00211: DigitalMultiChannelWriterWriteSingleSamplePort Method (Boolean, Int16)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.WriteSingleSamplePort Method (Boolean, Int16[])

### DigitalMultiChannelWriterWriteSingleSamplePort Method (Boolean, Int16)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteSingleSamplePort(
	bool autoStart,
	short[] data
)
```

```text
Public Sub WriteSingleSamplePort ( 
	autoStart As Boolean,
	data As Short()
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemInt16A 2D array of 16-bit integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

##### See Also

###### Reference

DigitalMultiChannelWriter Class

WriteSingleSamplePort Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport_2.htm language=enus -->
## TOPIC 00212: DigitalMultiChannelWriterWriteSingleSamplePort Method (Boolean, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport_2.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.WriteSingleSamplePort Method (Boolean, Int32[])

### DigitalMultiChannelWriterWriteSingleSamplePort Method (Boolean, Int32)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteSingleSamplePort(
	bool autoStart,
	int[] data
)
```

```text
Public Sub WriteSingleSamplePort ( 
	autoStart As Boolean,
	data As Integer()
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemInt32A 2D array of 32-bit integer samples to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

##### Remarks

Use this method for devices with up to 32 lines per port.

##### Remarks

Timeout

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

##### See Also

###### Reference

DigitalMultiChannelWriter Class

WriteSingleSamplePort Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport_3.htm language=enus -->
## TOPIC 00213: DigitalMultiChannelWriterWriteSingleSamplePort Method (Boolean, UInt16)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport_3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport_3.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.WriteSingleSamplePort Method (Boolean, UInt16[])

### DigitalMultiChannelWriterWriteSingleSamplePort Method (Boolean, UInt16)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteSingleSamplePort(
	bool autoStart,
	ushort[] data
)
```

```text
Public Sub WriteSingleSamplePort ( 
	autoStart As Boolean,
	data As UShort()
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemUInt16A 2D array of 16-bit unsigned integer samples to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

##### See Also

###### Reference

DigitalMultiChannelWriter Class

WriteSingleSamplePort Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport_4.htm language=enus -->
## TOPIC 00214: DigitalMultiChannelWriterWriteSingleSamplePort Method (Boolean, UInt32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport_4.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport_4.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.WriteSingleSamplePort Method (Boolean, UInt32[])

### DigitalMultiChannelWriterWriteSingleSamplePort Method (Boolean, UInt32)

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteSingleSamplePort(
	bool autoStart,
	uint[] data
)
```

```text
Public Sub WriteSingleSamplePort ( 
	autoStart As Boolean,
	data As UInteger()
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemUInt32A 2D array of 32-bit unsigned integer samples to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

##### Remarks

Use this method for devices with up to 32 lines per port.

##### Remarks

Timeout

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

##### See Also

###### Reference

DigitalMultiChannelWriter Class

WriteSingleSamplePort Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesamplesingleline.htm language=enus -->
## TOPIC 00215: DigitalMultiChannelWriterWriteSingleSampleSingleLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesamplesingleline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesamplesingleline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.WriteSingleSampleSingleLine Method

### DigitalMultiChannelWriterWriteSingleSampleSingleLine Method

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteSingleSampleSingleLine(
	bool autoStart,
	bool[] data
)
```

```text
Public Sub WriteSingleSampleSingleLine ( 
	autoStart As Boolean,
	data As Boolean()
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemBooleanA 1D array of Boolean samples to write to the task. Each element of the array corresponds to a channel within the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

##### See Also

###### Reference

DigitalMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writewaveform.htm language=enus -->
## TOPIC 00216: DigitalMultiChannelWriterWriteWaveform Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writewaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writewaveform.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter.WriteWaveform Method

### DigitalMultiChannelWriterWriteWaveform Method

DOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteWaveform(
	bool autoStart,
	DigitalWaveform[] data
)
```

```text
Public Sub WriteWaveform ( 
	autoStart As Boolean,
	data As DigitalWaveform()
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: NationalInstrumentsDigitalWaveformA 1D array of DigitalWaveform objects to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. The order of the lines in the digital waveform corresponds to the order in which you add the lines to the channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

##### Remarks

Digital waveform writes are not affected by the SampleInterval or StartTime properties on the DigitalWaveform. To configure timing for digital waveform writes, use the [ConfigureSampleClock](overload_nationalinstruments_daqmx_timing_configuresampleclock.htm) method.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

##### See Also

###### Reference

DigitalMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalpatternpausetrigger_tostring.htm language=enus -->
## TOPIC 00217: DigitalPatternPauseTriggerToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalpatternpausetrigger_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalpatternpausetrigger_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternPauseTrigger.ToString Method

### DigitalPatternPauseTriggerToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

DigitalPatternPauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalpatternreferencetrigger_tostring.htm language=enus -->
## TOPIC 00218: DigitalPatternReferenceTriggerToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalpatternreferencetrigger_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalpatternreferencetrigger_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternReferenceTrigger.ToString Method

### DigitalPatternReferenceTriggerToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

DigitalPatternReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalpatternstarttrigger_tostring.htm language=enus -->
## TOPIC 00219: DigitalPatternStartTriggerToString Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalpatternstarttrigger_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalpatternstarttrigger_tostring.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternStartTrigger.ToString Method

### DigitalPatternStartTriggerToString Method

Returns a string representation of the object.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

DigitalPatternStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader__ctor.htm language=enus -->
## TOPIC 00220: DigitalSingleChannelReader Constructor

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader__ctor.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader Constructor

### DigitalSingleChannelReader Constructor

DigitalSingleChannelReader

DaqStream

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DigitalSingleChannelReader(
	DaqStream stream
)
```

```text
Public Sub New ( 
	stream As DaqStream
)
```

###### Parameters

- **stream**
  - Type: NationalInstruments.DAQmxDaqStreamThe DaqStream to read.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Task

Stream

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportbyte.htm language=enus -->
## TOPIC 00221: DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortByte Method (Int32, AsyncCallback, Object, Byte)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportbyte.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportbyte.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.BeginMemoryOptimizedReadMultiSamplePortByte Method (Int32, AsyncCallback, Object, Byte[])

### DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortByte Method (Int32, AsyncCallback, Object, Byte)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortByte(
	int numberOfSamples,
	AsyncCallback callback,
	Object state,
	byte[] data
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSamplePortByte ( 
	numberOfSamples As Integer,
	callback As AsyncCallback,
	state As Object,
	data As Byte()
) As IAsyncResult
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallback An optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObject A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemByteAn initialized 1D array of 8-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
this method, call [EndMemoryOptimizedReadMultiSamplePortByte(IAsyncResult, Int32)](m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportbyte.htm)
with the returned
IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

BeginMemoryOptimizedReadMultiSamplePortByte Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportbyte_1.htm language=enus -->
## TOPIC 00222: DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortByte Method (Int32, AsyncCallback, Object, Byte, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportbyte_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportbyte_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.BeginMemoryOptimizedReadMultiSamplePortByte Method (Int32, AsyncCallback, Object, Byte[], ReallocationPolicy)

### DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortByte Method (Int32, AsyncCallback, Object, Byte, ReallocationPolicy)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortByte(
	int numberOfSamples,
	AsyncCallback callback,
	Object state,
	byte[] data,
	ReallocationPolicy policy
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSamplePortByte ( 
	numberOfSamples As Integer,
	callback As AsyncCallback,
	state As Object,
	data As Byte(),
	policy As ReallocationPolicy
) As IAsyncResult
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallback An optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObject A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemByteAn initialized 1D array of 8-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicy Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
this method, call [EndMemoryOptimizedReadMultiSamplePortByte(IAsyncResult, Int32)](m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportbyte.htm)
with the returned
IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

BeginMemoryOptimizedReadMultiSamplePortByte Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportint32.htm language=enus -->
## TOPIC 00223: DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortInt32 Method (Int32, AsyncCallback, Object, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.BeginMemoryOptimizedReadMultiSamplePortInt32 Method (Int32, AsyncCallback, Object, Int32[])

### DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortInt32 Method (Int32, AsyncCallback, Object, Int32)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortInt32(
	int numberOfSamples,
	AsyncCallback callback,
	Object state,
	int[] data
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSamplePortInt32 ( 
	numberOfSamples As Integer,
	callback As AsyncCallback,
	state As Object,
	data As Integer()
) As IAsyncResult
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallback An optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObject A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemInt32An initialized 1D array of 32-bit integer samples that contains the read data. Each element in the array corresponds to a sample from the channel.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
this method, call [EndMemoryOptimizedReadMultiSamplePortInt32(IAsyncResult, Int32)](m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportint32.htm)
with the returned
IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

BeginMemoryOptimizedReadMultiSamplePortInt32 Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportint32_1.htm language=enus -->
## TOPIC 00224: DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortInt32 Method (Int32, AsyncCallback, Object, Int32, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportint32_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportint32_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.BeginMemoryOptimizedReadMultiSamplePortInt32 Method (Int32, AsyncCallback, Object, Int32[], ReallocationPolicy)

### DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortInt32 Method (Int32, AsyncCallback, Object, Int32, ReallocationPolicy)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortInt32(
	int numberOfSamples,
	AsyncCallback callback,
	Object state,
	int[] data,
	ReallocationPolicy policy
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSamplePortInt32 ( 
	numberOfSamples As Integer,
	callback As AsyncCallback,
	state As Object,
	data As Integer(),
	policy As ReallocationPolicy
) As IAsyncResult
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallback An optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObject A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemInt32An initialized 1D array of 32-bit integer samples that contains the read data. Each element in the array corresponds to a sample from the channel.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicy Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
this method, call [EndMemoryOptimizedReadMultiSamplePortInt32(IAsyncResult, Int32)](m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportint32.htm)
with the returned
IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

BeginMemoryOptimizedReadMultiSamplePortInt32 Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportuint16.htm language=enus -->
## TOPIC 00225: DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortUInt16 Method (Int32, AsyncCallback, Object, UInt16)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportuint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportuint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.BeginMemoryOptimizedReadMultiSamplePortUInt16 Method (Int32, AsyncCallback, Object, UInt16[])

### DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortUInt16 Method (Int32, AsyncCallback, Object, UInt16)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt16(
	int numberOfSamples,
	AsyncCallback callback,
	Object state,
	ushort[] data
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSamplePortUInt16 ( 
	numberOfSamples As Integer,
	callback As AsyncCallback,
	state As Object,
	data As UShort()
) As IAsyncResult
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallback An optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObject A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemUInt16An initialized 1D array of 16-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
this method, call [EndMemoryOptimizedReadMultiSamplePortUInt16(IAsyncResult, Int32)](m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportuint16.htm)
with the returned
IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

BeginMemoryOptimizedReadMultiSamplePortUInt16 Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportuint16_1.htm language=enus -->
## TOPIC 00226: DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortUInt16 Method (Int32, AsyncCallback, Object, UInt16, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportuint16_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportuint16_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.BeginMemoryOptimizedReadMultiSamplePortUInt16 Method (Int32, AsyncCallback, Object, UInt16[], ReallocationPolicy)

### DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortUInt16 Method (Int32, AsyncCallback, Object, UInt16, ReallocationPolicy)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt16(
	int numberOfSamples,
	AsyncCallback callback,
	Object state,
	ushort[] data,
	ReallocationPolicy policy
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSamplePortUInt16 ( 
	numberOfSamples As Integer,
	callback As AsyncCallback,
	state As Object,
	data As UShort(),
	policy As ReallocationPolicy
) As IAsyncResult
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallback An optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObject A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemUInt16An initialized 1D array of 16-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicy Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
this method, call [EndMemoryOptimizedReadMultiSamplePortUInt16(IAsyncResult, Int32)](m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportuint16.htm)
with the returned
IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

BeginMemoryOptimizedReadMultiSamplePortUInt16 Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportuint32.htm language=enus -->
## TOPIC 00227: DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortUInt32 Method (Int32, AsyncCallback, Object, UInt32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportuint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.BeginMemoryOptimizedReadMultiSamplePortUInt32 Method (Int32, AsyncCallback, Object, UInt32[])

### DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortUInt32 Method (Int32, AsyncCallback, Object, UInt32)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt32(
	int numberOfSamples,
	AsyncCallback callback,
	Object state,
	uint[] data
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSamplePortUInt32 ( 
	numberOfSamples As Integer,
	callback As AsyncCallback,
	state As Object,
	data As UInteger()
) As IAsyncResult
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallback An optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObject A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemUInt32An initialized 1D array of 32-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
this method, call [EndMemoryOptimizedReadMultiSamplePortUInt32(IAsyncResult, Int32)](m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportuint32.htm)
with the returned
IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

BeginMemoryOptimizedReadMultiSamplePortUInt32 Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportuint32_1.htm language=enus -->
## TOPIC 00228: DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortUInt32 Method (Int32, AsyncCallback, Object, UInt32, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportuint32_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportuint32_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.BeginMemoryOptimizedReadMultiSamplePortUInt32 Method (Int32, AsyncCallback, Object, UInt32[], ReallocationPolicy)

### DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortUInt32 Method (Int32, AsyncCallback, Object, UInt32, ReallocationPolicy)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt32(
	int numberOfSamples,
	AsyncCallback callback,
	Object state,
	uint[] data,
	ReallocationPolicy policy
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSamplePortUInt32 ( 
	numberOfSamples As Integer,
	callback As AsyncCallback,
	state As Object,
	data As UInteger(),
	policy As ReallocationPolicy
) As IAsyncResult
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallback An optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObject A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemUInt32An initialized 1D array of 32-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicy Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
this method, call [EndMemoryOptimizedReadMultiSamplePortUInt32(IAsyncResult, Int32)](m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportuint32.htm)
with the returned
IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

BeginMemoryOptimizedReadMultiSamplePortUInt32 Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadsinglesamplemultiline.htm language=enus -->
## TOPIC 00229: DigitalSingleChannelReaderBeginMemoryOptimizedReadSingleSampleMultiLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadsinglesamplemultiline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadsinglesamplemultiline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.BeginMemoryOptimizedReadSingleSampleMultiLine Method

### DigitalSingleChannelReaderBeginMemoryOptimizedReadSingleSampleMultiLine Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadSingleSampleMultiLine(
	AsyncCallback callback,
	Object state,
	bool[] data
)
```

```text
Public Function BeginMemoryOptimizedReadSingleSampleMultiLine ( 
	callback As AsyncCallback,
	state As Object,
	data As Boolean()
) As IAsyncResult
```

###### Parameters

- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemBooleanAn initialized 1D array of Boolean samples that contains the read data. Each element in the array corresponds to a digital line in the channel.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
this method, call [EndReadSingleSampleMultiLine(IAsyncResult)](m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadsinglesamplemultiline.htm)
with the returned
IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginreadmultisampleportuint16.htm language=enus -->
## TOPIC 00230: DigitalSingleChannelReaderBeginReadMultiSamplePortUInt16 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginreadmultisampleportuint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginreadmultisampleportuint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.BeginReadMultiSamplePortUInt16 Method

### DigitalSingleChannelReaderBeginReadMultiSamplePortUInt16 Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadMultiSamplePortUInt16(
	int numberOfSamples,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadMultiSamplePortUInt16 ( 
	numberOfSamples As Integer,
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePortUInt16(Int32, AsyncCallback, Object), call [EndReadMultiSamplePortUInt16(IAsyncResult)](m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadmultisampleportuint16.htm) with the returned IAsyncResult.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginreadmultisampleportuint32.htm language=enus -->
## TOPIC 00231: DigitalSingleChannelReaderBeginReadMultiSamplePortUInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginreadmultisampleportuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginreadmultisampleportuint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.BeginReadMultiSamplePortUInt32 Method

### DigitalSingleChannelReaderBeginReadMultiSamplePortUInt32 Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadMultiSamplePortUInt32(
	int numberOfSamples,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadMultiSamplePortUInt32 ( 
	numberOfSamples As Integer,
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePortUInt32(Int32, AsyncCallback, Object), call [EndReadMultiSamplePortUInt32(IAsyncResult)](m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadmultisampleportuint32.htm) with the returned IAsyncResult.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginreadsinglesamplemultiline.htm language=enus -->
## TOPIC 00232: DigitalSingleChannelReaderBeginReadSingleSampleMultiLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginreadsinglesamplemultiline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginreadsinglesamplemultiline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.BeginReadSingleSampleMultiLine Method

### DigitalSingleChannelReaderBeginReadSingleSampleMultiLine Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadSingleSampleMultiLine(
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadSingleSampleMultiLine ( 
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSampleMultiLine(AsyncCallback, Object), call [EndReadSingleSampleMultiLine(IAsyncResult)](m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadsinglesamplemultiline.htm) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginreadwaveform.htm language=enus -->
## TOPIC 00233: DigitalSingleChannelReaderBeginReadWaveform Method (Int32, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginreadwaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginreadwaveform.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.BeginReadWaveform Method (Int32, AsyncCallback, Object)

### DigitalSingleChannelReaderBeginReadWaveform Method (Int32, AsyncCallback, Object)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadWaveform(
	int numberOfSamples,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadWaveform ( 
	numberOfSamples As Integer,
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadWaveform(Int32, AsyncCallback, Object), call [EndReadWaveform(IAsyncResult)](m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadwaveform.htm) with the returned IAsyncResult.

The data returned from digital waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

BeginReadWaveform Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginreadwaveform_1.htm language=enus -->
## TOPIC 00234: DigitalSingleChannelReaderBeginReadWaveform Method (TimeSpan, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginreadwaveform_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_beginreadwaveform_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.BeginReadWaveform Method (TimeSpan, AsyncCallback, Object)

### DigitalSingleChannelReaderBeginReadWaveform Method (TimeSpan, AsyncCallback, Object)

DIChannel

duration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadWaveform(
	TimeSpan duration,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadWaveform ( 
	duration As TimeSpan,
	callback As AsyncCallback,
	state As Object
) As IAsyncResult
```

###### Parameters

- **duration**
  - Type: SystemTimeSpanThe duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

BeginReadWaveform(TimeSpan, AsyncCallback, Object)

EndReadWaveform(IAsyncResult)

IAsyncResult

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the [Stream](p_nationalinstruments_daqmx_task_stream.htm) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

BeginReadWaveform Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportbyte.htm language=enus -->
## TOPIC 00235: DigitalSingleChannelReaderEndMemoryOptimizedReadMultiSamplePortByte Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportbyte.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportbyte.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.EndMemoryOptimizedReadMultiSamplePortByte Method

### DigitalSingleChannelReaderEndMemoryOptimizedReadMultiSamplePortByte Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public byte[] EndMemoryOptimizedReadMultiSamplePortByte(
	IAsyncResult asyncResult,
	out int actualNumberOfSamplesRead
)
```

```text
Public Function EndMemoryOptimizedReadMultiSamplePortByte ( 
	asyncResult As IAsyncResult,
	<OutAttribute> ByRef actualNumberOfSamplesRead As Integer
) As Byte()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResult An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePortByte(Int32, AsyncCallback, Object, Byte).
- **actualNumberOfSamplesRead**
  - Type: SystemInt32 The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

Byte

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePortByte(Int32, AsyncCallback, Object, Byte). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call
this method
before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportint32.htm language=enus -->
## TOPIC 00236: DigitalSingleChannelReaderEndMemoryOptimizedReadMultiSamplePortInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.EndMemoryOptimizedReadMultiSamplePortInt32 Method

### DigitalSingleChannelReaderEndMemoryOptimizedReadMultiSamplePortInt32 Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public int[] EndMemoryOptimizedReadMultiSamplePortInt32(
	IAsyncResult asyncResult,
	out int actualNumberOfSamplesRead
)
```

```text
Public Function EndMemoryOptimizedReadMultiSamplePortInt32 ( 
	asyncResult As IAsyncResult,
	<OutAttribute> ByRef actualNumberOfSamplesRead As Integer
) As Integer()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResult An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePortInt32(Int32, AsyncCallback, Object, Int32).
- **actualNumberOfSamplesRead**
  - Type: SystemInt32

###### Return Value

Int32

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePortInt32(Int32, AsyncCallback, Object, Int32). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call
this method
before the asynchronous read
IAsyncResult
is complete,
it
waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportuint16.htm language=enus -->
## TOPIC 00237: DigitalSingleChannelReaderEndMemoryOptimizedReadMultiSamplePortUInt16 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportuint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportuint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.EndMemoryOptimizedReadMultiSamplePortUInt16 Method

### DigitalSingleChannelReaderEndMemoryOptimizedReadMultiSamplePortUInt16 Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public ushort[] EndMemoryOptimizedReadMultiSamplePortUInt16(
	IAsyncResult asyncResult,
	out int actualNumberOfSamplesRead
)
```

```text
Public Function EndMemoryOptimizedReadMultiSamplePortUInt16 ( 
	asyncResult As IAsyncResult,
	<OutAttribute> ByRef actualNumberOfSamplesRead As Integer
) As UShort()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResult An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePortUInt16(Int32, AsyncCallback, Object, UInt16).
- **actualNumberOfSamplesRead**
  - Type: SystemInt32 The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

UInt16

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePortUInt16(Int32, AsyncCallback, Object, UInt16). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call
this method
before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportuint32.htm language=enus -->
## TOPIC 00238: DigitalSingleChannelReaderEndMemoryOptimizedReadMultiSamplePortUInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadmultisampleportuint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.EndMemoryOptimizedReadMultiSamplePortUInt32 Method

### DigitalSingleChannelReaderEndMemoryOptimizedReadMultiSamplePortUInt32 Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public uint[] EndMemoryOptimizedReadMultiSamplePortUInt32(
	IAsyncResult asyncResult,
	out int actualNumberOfSamplesRead
)
```

```text
Public Function EndMemoryOptimizedReadMultiSamplePortUInt32 ( 
	asyncResult As IAsyncResult,
	<OutAttribute> ByRef actualNumberOfSamplesRead As Integer
) As UInteger()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResult An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePortUInt32(Int32, AsyncCallback, Object, UInt32).
- **actualNumberOfSamplesRead**
  - Type: SystemInt32 The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

UInt32

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePortUInt32(Int32, AsyncCallback, Object, UInt32). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call
this method
before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadsinglesamplemultiline.htm language=enus -->
## TOPIC 00239: DigitalSingleChannelReaderEndMemoryOptimizedReadSingleSampleMultiLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadsinglesamplemultiline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endmemoryoptimizedreadsinglesamplemultiline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.EndMemoryOptimizedReadSingleSampleMultiLine Method

### DigitalSingleChannelReaderEndMemoryOptimizedReadSingleSampleMultiLine Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool[] EndMemoryOptimizedReadSingleSampleMultiLine(
	IAsyncResult asyncResult
)
```

```text
Public Function EndMemoryOptimizedReadSingleSampleMultiLine ( 
	asyncResult As IAsyncResult
) As Boolean()
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, Object, Boolean).

###### Return Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; asyncResult is or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, Object, Boolean). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call
this method
before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadsinglesampleportint16.htm language=enus -->
## TOPIC 00240: DigitalSingleChannelReaderEndReadSingleSamplePortInt16 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadsinglesampleportint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadsinglesampleportint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.EndReadSingleSamplePortInt16 Method

### DigitalSingleChannelReaderEndReadSingleSamplePortInt16 Method

BeginReadSingleSamplePortInt16(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public short EndReadSingleSamplePortInt16(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadSingleSamplePortInt16 ( 
	asyncResult As IAsyncResult
) As Short
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortInt16(AsyncCallback, Object).

###### Return Value

Int16

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSample(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSamplePortInt16(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortInt16(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadsinglesampleportint32.htm language=enus -->
## TOPIC 00241: DigitalSingleChannelReaderEndReadSingleSamplePortInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadsinglesampleportint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadsinglesampleportint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.EndReadSingleSamplePortInt32 Method

### DigitalSingleChannelReaderEndReadSingleSamplePortInt32 Method

BeginReadSingleSamplePortInt32(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public int EndReadSingleSamplePortInt32(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadSingleSamplePortInt32 ( 
	asyncResult As IAsyncResult
) As Integer
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortInt32(AsyncCallback, Object).

###### Return Value

Int32

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSample(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSamplePortInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadsinglesampleportuint16.htm language=enus -->
## TOPIC 00242: DigitalSingleChannelReaderEndReadSingleSamplePortUInt16 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadsinglesampleportuint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadsinglesampleportuint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.EndReadSingleSamplePortUInt16 Method

### DigitalSingleChannelReaderEndReadSingleSamplePortUInt16 Method

BeginReadSingleSamplePortUInt16(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public ushort EndReadSingleSamplePortUInt16(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadSingleSamplePortUInt16 ( 
	asyncResult As IAsyncResult
) As UShort
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortUInt16(AsyncCallback, Object).

###### Return Value

UInt16

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSample(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSamplePortUInt16(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortUInt16(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadsinglesampleportuint32.htm language=enus -->
## TOPIC 00243: DigitalSingleChannelReaderEndReadSingleSamplePortUInt32 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadsinglesampleportuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadsinglesampleportuint32.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.EndReadSingleSamplePortUInt32 Method

### DigitalSingleChannelReaderEndReadSingleSamplePortUInt32 Method

BeginReadSingleSamplePortUInt32(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public uint EndReadSingleSamplePortUInt32(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadSingleSamplePortUInt32 ( 
	asyncResult As IAsyncResult
) As UInteger
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortUInt32(AsyncCallback, Object).

###### Return Value

UInt32

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSample(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSamplePortUInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortUInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadsinglesamplesingleline.htm language=enus -->
## TOPIC 00244: DigitalSingleChannelReaderEndReadSingleSampleSingleLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadsinglesamplesingleline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadsinglesamplesingleline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.EndReadSingleSampleSingleLine Method

### DigitalSingleChannelReaderEndReadSingleSampleSingleLine Method

BeginReadSingleSampleSingleLine(AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool EndReadSingleSampleSingleLine(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadSingleSampleSingleLine ( 
	asyncResult As IAsyncResult
) As Boolean
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSampleSingleLine(AsyncCallback, Object).

###### Return Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadMultiSample(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadSingleSampleSingleLine(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSampleSingleLine(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadwaveform.htm language=enus -->
## TOPIC 00245: DigitalSingleChannelReaderEndReadWaveform Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadwaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_endreadwaveform.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.EndReadWaveform Method

### DigitalSingleChannelReaderEndReadWaveform Method

BeginReadWaveform(Int32, AsyncCallback, Object)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DigitalWaveform EndReadWaveform(
	IAsyncResult asyncResult
)
```

```text
Public Function EndReadWaveform ( 
	asyncResult As IAsyncResult
) As DigitalWaveform
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResultAn IAsyncResult that represents an asynchronous call started by calling BeginReadWaveform(Int32, AsyncCallback, Object).

###### Return Value

DigitalWaveform

DigitalWaveform

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | asyncResult is or is not an instance of IAsyncResult returned from a call to BeginReadWaveform(Int32, AsyncCallback, Object). |
| DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If you call EndReadWaveform(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadWaveform(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_memoryoptimizedreadmultisampleportbyte.htm language=enus -->
## TOPIC 00246: DigitalSingleChannelReaderMemoryOptimizedReadMultiSamplePortByte Method (Int32, Byte, ReallocationPolicy, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_memoryoptimizedreadmultisampleportbyte.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_memoryoptimizedreadmultisampleportbyte.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.MemoryOptimizedReadMultiSamplePortByte Method (Int32, Byte[], ReallocationPolicy, Int32)

### DigitalSingleChannelReaderMemoryOptimizedReadMultiSamplePortByte Method (Int32, Byte, ReallocationPolicy, Int32)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public byte[] MemoryOptimizedReadMultiSamplePortByte(
	int numberOfSamples,
	ref byte[] data,
	ReallocationPolicy policy,
	out int actualNumberOfSamplesRead
)
```

```text
Public Function MemoryOptimizedReadMultiSamplePortByte ( 
	numberOfSamples As Integer,
	ByRef data As Byte(),
	policy As ReallocationPolicy,
	<OutAttribute> ByRef actualNumberOfSamplesRead As Integer
) As Byte()
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: SystemByteAn initialized 1D array of 8-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicy Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.
- **actualNumberOfSamplesRead**
  - Type: SystemInt32 The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

Byte

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalSingleChannelReader Class

MemoryOptimizedReadMultiSamplePortByte Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_memoryoptimizedreadmultisampleportint32_1.htm language=enus -->
## TOPIC 00247: DigitalSingleChannelReaderMemoryOptimizedReadMultiSamplePortInt32 Method (Int32, Int32, Int32)

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_memoryoptimizedreadmultisampleportint32_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_memoryoptimizedreadmultisampleportint32_1.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.MemoryOptimizedReadMultiSamplePortInt32 Method (Int32, Int32[], Int32)

### DigitalSingleChannelReaderMemoryOptimizedReadMultiSamplePortInt32 Method (Int32, Int32, Int32)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public int[] MemoryOptimizedReadMultiSamplePortInt32(
	int numberOfSamples,
	ref int[] data,
	out int actualNumberOfSamplesRead
)
```

```text
Public Function MemoryOptimizedReadMultiSamplePortInt32 ( 
	numberOfSamples As Integer,
	ByRef data As Integer(),
	<OutAttribute> ByRef actualNumberOfSamplesRead As Integer
) As Integer()
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **data**
  - Type: SystemInt32An initialized 1D array of 32-bit integer samples that contains the read data. Each element in the array corresponds to a sample from the channel.
- **actualNumberOfSamplesRead**
  - Type: SystemInt32 The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

Int32

data

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized. |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalSingleChannelReader Class

MemoryOptimizedReadMultiSamplePortInt32 Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_memoryoptimizedreadsinglesamplemultiline.htm language=enus -->
## TOPIC 00248: DigitalSingleChannelReaderMemoryOptimizedReadSingleSampleMultiLine Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_memoryoptimizedreadsinglesamplemultiline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_memoryoptimizedreadsinglesamplemultiline.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.MemoryOptimizedReadSingleSampleMultiLine Method

### DigitalSingleChannelReaderMemoryOptimizedReadSingleSampleMultiLine Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool[] MemoryOptimizedReadSingleSampleMultiLine(
	bool[] data
)
```

```text
Public Function MemoryOptimizedReadSingleSampleMultiLine ( 
	data As Boolean()
) As Boolean()
```

###### Parameters

- **data**
  - Type: SystemBooleanAn initialized 1D array of Boolean samples that contains the read data. Each element in the array corresponds to a digital line in the channel.

###### Return Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized. |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the
[Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm)
property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readmultisampleportbyte.htm language=enus -->
## TOPIC 00249: DigitalSingleChannelReaderReadMultiSamplePortByte Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readmultisampleportbyte.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readmultisampleportbyte.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.ReadMultiSamplePortByte Method

### DigitalSingleChannelReaderReadMultiSamplePortByte Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public byte[] ReadMultiSamplePortByte(
	int numberOfSamples
)
```

```text
Public Function ReadMultiSamplePortByte ( 
	numberOfSamples As Integer
) As Byte()
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.

###### Return Value

Byte

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

Use this method for devices with up to eight lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readmultisampleportint16.htm language=enus -->
## TOPIC 00250: DigitalSingleChannelReaderReadMultiSamplePortInt16 Method

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readmultisampleportint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/m_nationalinstruments_daqmx_digitalsinglechannelreader_readmultisampleportint16.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.ReadMultiSamplePortInt16 Method

### DigitalSingleChannelReaderReadMultiSamplePortInt16 Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public short[] ReadMultiSamplePortInt16(
	int numberOfSamples
)
```

```text
Public Function ReadMultiSamplePortInt16 ( 
	numberOfSamples As Integer
) As Short()
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.

###### Return Value

Int16

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

##### Remarks

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
