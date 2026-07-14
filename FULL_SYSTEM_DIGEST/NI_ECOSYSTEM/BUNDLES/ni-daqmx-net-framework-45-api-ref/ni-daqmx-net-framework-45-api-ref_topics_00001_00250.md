# NI DOCUMENT BUNDLE: ni-daqmx-net-framework-45-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-net-framework-45-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/e_nationalinstruments_daqmx_task_everynsamplesread.htm language=enus -->
## TOPIC 00001: TaskEveryNSamplesRead Event

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/e_nationalinstruments_daqmx_task_everynsamplesread.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/e_nationalinstruments_daqmx_task_everynsamplesread.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Task.EveryNSamplesRead Event

### TaskEveryNSamplesRead Event

EveryNSamplesReadEventInterval

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public event EveryNSamplesReadEventHandler EveryNSamplesRead
```

```text
Public Event EveryNSamplesRead As EveryNSamplesReadEventHandler
```

###### Value

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

EveryNSamplesReadEventInterval

| Note |
| --- |
| For more information about events in NI-DAQmx, refer to Events. |

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Events

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/e_nationalinstruments_daqmx_task_everynsampleswritten.htm language=enus -->
## TOPIC 00002: TaskEveryNSamplesWritten Event

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/e_nationalinstruments_daqmx_task_everynsampleswritten.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/e_nationalinstruments_daqmx_task_everynsampleswritten.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Task.EveryNSamplesWritten Event

### TaskEveryNSamplesWritten Event

EveryNSamplesWrittenEventInterval

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public event EveryNSamplesWrittenEventHandler EveryNSamplesWritten
```

```text
Public Event EveryNSamplesWritten As EveryNSamplesWrittenEventHandler
```

###### Value

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

EveryNSamplesWrittenEventInterval

| Note |
| --- |
| For more information about events in NI-DAQmx, refer to Events. |

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Events

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/e_nationalinstruments_daqmx_task_sampleclock.htm language=enus -->
## TOPIC 00003: TaskSampleClock Event

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/e_nationalinstruments_daqmx_task_sampleclock.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/e_nationalinstruments_daqmx_task_sampleclock.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Task.SampleClock Event

### TaskSampleClock Event

Occurs on each pulse of the task's sample clock.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public event SampleClockEventHandler SampleClock
```

```text
Public Event SampleClock As SampleClockEventHandler
```

###### Value

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Events

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Events

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_advancetrigger_configuredigitaledgetrigger.htm language=enus -->
## TOPIC 00004: AdvanceTriggerConfigureDigitalEdgeTrigger Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_advancetrigger_configuredigitaledgetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_advancetrigger_configuredigitaledgetrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AdvanceTrigger.ConfigureDigitalEdgeTrigger Method

### AdvanceTriggerConfigureDigitalEdgeTrigger Method

rising or falling edge of a digital signal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureDigitalEdgeTrigger(
	string source,
	DigitalEdgeAdvanceTriggerEdge edge
)
```

```text
Public Sub ConfigureDigitalEdgeTrigger ( 
	source As String,
	edge As DigitalEdgeAdvanceTriggerEdge
)
```

###### Parameters

- **source**
  - Type: SystemStringThe terminal of the trigger signal.
- **edge**
  - Type: NationalInstruments.DAQmxDigitalEdgeAdvanceTriggerEdgeThe edge of the trigger signal that causes an advance trigger to occur.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

ConfigureDigitalEdgeTrigger(String, DigitalEdgeAdvanceTriggerEdge)

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

AdvanceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_advancetrigger_configuresoftwaretrigger.htm language=enus -->
## TOPIC 00005: AdvanceTriggerConfigureSoftwareTrigger Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_advancetrigger_configuresoftwaretrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_advancetrigger_configuresoftwaretrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AdvanceTrigger.ConfigureSoftwareTrigger Method

### AdvanceTriggerConfigureSoftwareTrigger Method

Configures a task to advance to the next entry in a scan list upon a software trigger.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureSoftwareTrigger()
```

```text
Public Sub ConfigureSoftwareTrigger
```

##### Remarks

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

AdvanceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_advancetrigger_tostring.htm language=enus -->
## TOPIC 00006: AdvanceTriggerToString Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_advancetrigger_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_advancetrigger_tostring.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AdvanceTrigger.ToString Method

### AdvanceTriggerToString Method

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

AdvanceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannel_performbridgeoffsetnullingcalibration.htm language=enus -->
## TOPIC 00007: AIChannelPerformBridgeOffsetNullingCalibration Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannel_performbridgeoffsetnullingcalibration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannel_performbridgeoffsetnullingcalibration.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.PerformBridgeOffsetNullingCalibration Method

### AIChannelPerformBridgeOffsetNullingCalibration Method

Performs a bridge offset nulling calibration on the virtual channels in the task. An error will occur if not all virtual channels in the task support this operation.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void PerformBridgeOffsetNullingCalibration()
```

```text
Public Sub PerformBridgeOffsetNullingCalibration
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method adjusts the [BridgeBalanceCoarsePot](p_nationalinstruments_daqmx_aichannel_bridgebalancecoarsepot.htm), [BridgeBalanceFinePot](p_nationalinstruments_daqmx_aichannel_bridgebalancefinepot.htm), and [BridgeInitialVoltage](p_nationalinstruments_daqmx_aichannel_bridgeinitialvoltage.htm) properties to eliminate voltage offset in the virtual channel. If the acquisition device does not have a built-in potentiometer, only the initial bridge voltage attribute is adjusted.

The task must not be reserved, committed, or started. All virtual channel configurations must be complete prior to calling this method. The physical channel must remain in the state at which you expect to read 0 V from the bridge while the method executes.

##### See Also

###### Reference

AIChannel Class

PerformBridgeOffsetNullingCalibration Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannel_performbridgeoffsetnullingcalibration_1.htm language=enus -->
## TOPIC 00008: AIChannelPerformBridgeOffsetNullingCalibration Method (Boolean)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannel_performbridgeoffsetnullingcalibration_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannel_performbridgeoffsetnullingcalibration_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.PerformBridgeOffsetNullingCalibration Method (Boolean)

### AIChannelPerformBridgeOffsetNullingCalibration Method (Boolean)

Performs a bridge offset nulling calibration on the virtual channels in the task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void PerformBridgeOffsetNullingCalibration(
	bool skipUnsupportedChannels
)
```

```text
Public Sub PerformBridgeOffsetNullingCalibration ( 
	skipUnsupportedChannels As Boolean
)
```

###### Parameters

- **skipUnsupportedChannels**
  - Type: SystemBooleanSpecifies whether or not to skip channels that do not support shunt calibration. If skipUnsupportedChannels is , shunt calibration will be performed only on supported virtual channels in the task. If , shunt calibration will be performed on all virtual channels in the task, which may result in an error if not all channels support shunt calibration.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method adjusts the [BridgeBalanceCoarsePot](p_nationalinstruments_daqmx_aichannel_bridgebalancecoarsepot.htm), [BridgeBalanceFinePot](p_nationalinstruments_daqmx_aichannel_bridgebalancefinepot.htm), and [BridgeInitialVoltage](p_nationalinstruments_daqmx_aichannel_bridgeinitialvoltage.htm) properties to eliminate voltage offset in the virtual channel. If the acquisition device does not have a built-in potentiometer, only the initial bridge voltage attribute is adjusted.

The task must not be reserved, committed, or started. All virtual channel configurations must be complete prior to calling this method. The physical channel must remain in the state at which you expect to read 0 V from the bridge while the method executes.

##### See Also

###### Reference

AIChannel Class

PerformBridgeOffsetNullingCalibration Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannel_performbridgeshuntcalibration_1.htm language=enus -->
## TOPIC 00009: AIChannelPerformBridgeShuntCalibration Method (Double, ShuntElementLocation, Double, ShuntCalibrationSelect, ShuntResistorSource)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannel_performbridgeshuntcalibration_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannel_performbridgeshuntcalibration_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.PerformBridgeShuntCalibration Method (Double, ShuntElementLocation, Double, ShuntCalibrationSelect, ShuntResistorSource)

### AIChannelPerformBridgeShuntCalibration Method (Double, ShuntElementLocation, Double, ShuntCalibrationSelect, ShuntResistorSource)

Performs shunt calibration for the specified channels using a bridge sensor.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void PerformBridgeShuntCalibration(
	double shuntResistorValue,
	ShuntElementLocation shuntResistorLocation,
	double bridgeResistance,
	ShuntCalibrationSelect shuntResistorSelect,
	ShuntResistorSource shuntResistorSource
)
```

```text
Public Sub PerformBridgeShuntCalibration ( 
	shuntResistorValue As Double,
	shuntResistorLocation As ShuntElementLocation,
	bridgeResistance As Double,
	shuntResistorSelect As ShuntCalibrationSelect,
	shuntResistorSource As ShuntResistorSource
)
```

###### Parameters

- **shuntResistorValue**
  - Type: SystemDouble The resistance, in ohms, of the shunt resistor.
- **shuntResistorLocation**
  - Type: NationalInstruments.DAQmxShuntElementLocation The location of the shunt resistor.
- **bridgeResistance**
  - Type: SystemDouble The resistance, in ohms, of the bridge sensor.
- **shuntResistorSelect**
  - Type: NationalInstruments.DAQmxShuntCalibrationSelect The shunt calibration switch to use.
- **shuntResistorSource**
  - Type: NationalInstruments.DAQmxShuntResistorSource The shunt resistor to use.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

PerformBridgeShuntCalibration Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannel_performthermocoupleleadoffsetnullingcalibration_1.htm language=enus -->
## TOPIC 00010: AIChannelPerformThermocoupleLeadOffsetNullingCalibration Method (Boolean)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannel_performthermocoupleleadoffsetnullingcalibration_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannel_performthermocoupleleadoffsetnullingcalibration_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createaccelerationchargechannel_1.htm language=enus -->
## TOPIC 00011: AIChannelCollectionCreateAccelerationChargeChannel Method (String, String, AITerminalConfiguration, Double, Double, String, Double, AIAccelerationChargeSensitivityUnits)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createaccelerationchargechannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createaccelerationchargechannel_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel.htm language=enus -->
## TOPIC 00012: AIChannelCollectionCreateCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, AICurrentUnits)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_2.htm language=enus -->
## TOPIC 00013: AIChannelCollectionCreateCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, Double, AICurrentUnits)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_2.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_3.htm language=enus -->
## TOPIC 00014: AIChannelCollectionCreateCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, Double, String)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_3.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_4.htm language=enus -->
## TOPIC 00015: AIChannelCollectionCreateCurrentChannel Method (String, String, AITerminalConfiguration, Double, Double, String)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_4.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createcurrentchannel_4.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createdevicetemperaturechannel.htm language=enus -->
## TOPIC 00016: AIChannelCollectionCreateDeviceTemperatureChannel Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createdevicetemperaturechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createdevicetemperaturechannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateDeviceTemperatureChannel Method

### AIChannelCollectionCreateDeviceTemperatureChannel Method

**Note: This API is now obsolete.**

AIChannel

AIChannelCollection

CreateDeviceTemperatureChannel(String, String, AITemperatureUnits)

CreateBuiltInSensorTemperatureChannel(String, String, AITemperatureUnits)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("The CreateDeviceTemperatureChannel method is deprecated.  Please use the CreateBuiltInSensorTemperatureChannel method instead.")]
public AIChannel CreateDeviceTemperatureChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITemperatureUnits units
)
```

```text
<ObsoleteAttribute("The CreateDeviceTemperatureChannel method is deprecated.  Please use the CreateBuiltInSensorTemperatureChannel method instead.")>
Public Function CreateDeviceTemperatureChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	units As AITemperatureUnits
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **units**
  - Type: NationalInstruments.DAQmxAITemperatureUnitsThe units to use to return the measurement.

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

On SCXI modules, the built-in sensor might be the CJC sensor.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateDeviceTemperatureChannel(String, String, AITemperatureUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createeddycurrentproximityprobechannel_1.htm language=enus -->
## TOPIC 00017: AIChannelCollectionCreateEddyCurrentProximityProbeChannel Method (String, String, Double, Double, Double, AIEddyCurrentProximityProbeSensitivityUnits, String)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createeddycurrentproximityprobechannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createeddycurrentproximityprobechannel_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateEddyCurrentProximityProbeChannel Method (String, String, Double, Double, Double, AIEddyCurrentProximityProbeSensitivityUnits, String)

### AIChannelCollectionCreateEddyCurrentProximityProbeChannel Method (String, String, Double, Double, Double, AIEddyCurrentProximityProbeSensitivityUnits, String)

AIChannel

Eddy Current Proximity Probe

measure position

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateEddyCurrentProximityProbeChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	double sensitivity,
	AIEddyCurrentProximityProbeSensitivityUnits sensitivityUnits,
	string customScaleName
)
```

```text
Public Function CreateEddyCurrentProximityProbeChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	sensitivity As Double,
	sensitivityUnits As AIEddyCurrentProximityProbeSensitivityUnits,
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
  - Type: NationalInstruments.DAQmxAIEddyCurrentProximityProbeSensitivityUnitsThe units of sensitivity.
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

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateEddyCurrentProximityProbeChannel(String, String, Double, Double, Double, AIEddyCurrentProximityProbeSensitivityUnits, String) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateEddyCurrentProximityProbeChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createforcebridgetwopointlinearchannel.htm language=enus -->
## TOPIC 00018: AIChannelCollectionCreateForceBridgeTwoPointLinearChannel Method (String, String, Double, Double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createforcebridgetwopointlinearchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createforcebridgetwopointlinearchannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateForceBridgeTwoPointLinearChannel Method (String, String, Double, Double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits)

### AIChannelCollectionCreateForceBridgeTwoPointLinearChannel Method (String, String, Double, Double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits)

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
public AIChannel CreateForceBridgeTwoPointLinearChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	AIForceUnits units,
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
Public Function CreateForceBridgeTwoPointLinearChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	units As AIForceUnits,
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
  - Type: NationalInstruments.DAQmxAIForceUnitsThe units to use to return the measurement.
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

CreateForceBridgeTwoPointLinearChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createforceiepechannel_1.htm language=enus -->
## TOPIC 00019: AIChannelCollectionCreateForceIepeChannel Method (String, String, AITerminalConfiguration, Double, Double, String, Double, AIForceIepeSensorSensitivityUnits, AIExcitationSource, Double)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createforceiepechannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createforceiepechannel_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateForceIepeChannel Method (String, String, AITerminalConfiguration, Double, Double, String, Double, AIForceIepeSensorSensitivityUnits, AIExcitationSource, Double)

### AIChannelCollectionCreateForceIepeChannel Method (String, String, AITerminalConfiguration, Double, Double, String, Double, AIForceIepeSensorSensitivityUnits, AIExcitationSource, Double)

AIChannel

IEPE force sensor

measure force or load

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateForceIepeChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration terminalConfiguration,
	double minimumValue,
	double maximumValue,
	string customScaleName,
	double sensitivity,
	AIForceIepeSensorSensitivityUnits sensitivityUnits,
	AIExcitationSource currentExcitationSource,
	double currentExcitationValue
)
```

```text
Public Function CreateForceIepeChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	terminalConfiguration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	customScaleName As String,
	sensitivity As Double,
	sensitivityUnits As AIForceIepeSensorSensitivityUnits,
	currentExcitationSource As AIExcitationSource,
	currentExcitationValue As Double
) As AIChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemString The names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **terminalConfiguration**
  - Type: NationalInstruments.DAQmxAITerminalConfiguration The input terminal configuration. To use the default terminal configuration for the physical channel(s) being used, pass a value of 1 casted to an AITerminalConfiguration.
- **minimumValue**
  - Type: SystemDouble The minimum value you expect to measure, in units.
- **maximumValue**
  - Type: SystemDouble The maximum value you expect to measure, in units.
- **customScaleName**
  - Type: SystemString The name of the custom scale to apply to the local virtual channel.
- **sensitivity**
  - Type: SystemDouble The sensitivity of the sensor. This value is in the units you specify with sensitivityUnits. Refer to the sensor documentation to determine this value.
- **sensitivityUnits**
  - Type: NationalInstruments.DAQmxAIForceIepeSensorSensitivityUnits The units of sensitivity.
- **currentExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSourceThe source of excitation.
- **currentExcitationValue**
  - Type: SystemDoubleThe amount of excitation, in amperes, that the sensor requires.

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

CreateForceIepeChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createfrequencyvoltagechannel_1.htm language=enus -->
## TOPIC 00020: AIChannelCollectionCreateFrequencyVoltageChannel Method (String, String, Double, Double, Double, Double, String)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createfrequencyvoltagechannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createfrequencyvoltagechannel_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateFrequencyVoltageChannel Method (String, String, Double, Double, Double, Double, String)

### AIChannelCollectionCreateFrequencyVoltageChannel Method (String, String, Double, Double, Double, Double, String)

AIChannel

measure frequency

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateFrequencyVoltageChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	double thresholdVoltage,
	double hysteresis,
	string customScaleName
)
```

```text
Public Function CreateFrequencyVoltageChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	thresholdVoltage As Double,
	hysteresis As Double,
	customScaleName As String
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
- **thresholdVoltage**
  - Type: SystemDoubleThe voltage level at which to recognize waveform repetitions. You should select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls.
- **hysteresis**
  - Type: SystemDoubleA window, in volts, below thresholdVoltage. The input voltage must pass below thresholdVoltage minus hysteresis before NI-DAQmx recognizes a waveform repetition. Hysteresis can improve the measurement accuracy when the signal contains noise or jitter.
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

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateFrequencyVoltageChannel(String, String, Double, Double, Double, Double, String) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateFrequencyVoltageChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createthermocouplechannel.htm language=enus -->
## TOPIC 00021: AIChannelCollectionCreateThermocoupleChannel Method (String, String, Double, Double, AIThermocoupleType, AITemperatureUnits)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createthermocouplechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createthermocouplechannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateThermocoupleChannel Method (String, String, Double, Double, AIThermocoupleType, AITemperatureUnits)

### AIChannelCollectionCreateThermocoupleChannel Method (String, String, Double, Double, AIThermocoupleType, AITemperatureUnits)

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
	AITemperatureUnits units
)
```

```text
Public Function CreateThermocoupleChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	thermocoupleType As AIThermocoupleType,
	units As AITemperatureUnits
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
  - Type: NationalInstruments.DAQmxAITemperatureUnitsThe units to use to return the measurement.

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

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateThermocoupleChannel(String, String, Double, Double, AIThermocoupleType, AITemperatureUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateThermocoupleChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtorquebridgepolynomialchannel_1.htm language=enus -->
## TOPIC 00022: AIChannelCollectionCreateTorqueBridgePolynomialChannel Method (String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtorquebridgepolynomialchannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtorquebridgepolynomialchannel_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTorqueBridgePolynomialChannel Method (String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double[], Double[], AIBridgeElectricalUnits, AIBridgePhysicalUnits)

### AIChannelCollectionCreateTorqueBridgePolynomialChannel Method (String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits)

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
	string customScaleName,
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
	customScaleName As String,
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtorquebridgetablechannel_1.htm language=enus -->
## TOPIC 00023: AIChannelCollectionCreateTorqueBridgeTableChannel Method (String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, AIBridgeElectricalUnits, Double, AIBridgePhysicalUnits)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtorquebridgetablechannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createtorquebridgetablechannel_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTorqueBridgeTableChannel Method (String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double[], AIBridgeElectricalUnits, Double[], AIBridgePhysicalUnits)

### AIChannelCollectionCreateTorqueBridgeTableChannel Method (String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, AIBridgeElectricalUnits, Double, AIBridgePhysicalUnits)

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
public AIChannel CreateTorqueBridgeTableChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	string customScaleName,
	AIBridgeConfiguration bridgeConfiguration,
	AIExcitationSource voltageExcitationSource,
	double voltageExcitationValue,
	double nominalBridgeResistance,
	double[] electricalValues,
	AIBridgeElectricalUnits electricalUnits,
	double[] physicalValues,
	AIBridgePhysicalUnits physicalUnits
)
```

```text
Public Function CreateTorqueBridgeTableChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	customScaleName As String,
	bridgeConfiguration As AIBridgeConfiguration,
	voltageExcitationSource As AIExcitationSource,
	voltageExcitationValue As Double,
	nominalBridgeResistance As Double,
	electricalValues As Double(),
	electricalUnits As AIBridgeElectricalUnits,
	physicalValues As Double(),
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
- **electricalValues**
  - Type: SystemDouble The array of electrical values that map to the values in physicalValues. Specify this value in the units specified with electricalUnits.
- **electricalUnits**
  - Type: NationalInstruments.DAQmxAIBridgeElectricalUnitsSpecifies from which electrical units to scale data. Use the units that correspond to the units used for electrical values provided by the sensor data sheet or calibration certificate.
- **physicalValues**
  - Type: SystemDoubleThe array of physical values that map to the values in electricalValues. Specify this value in the units specified with physicalUnits.
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

CreateTorqueBridgeTableChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createvoltagechannelwithexcitation.htm language=enus -->
## TOPIC 00024: AIChannelCollectionCreateVoltageChannelWithExcitation Method (String, String, AITerminalConfiguration, Double, Double, AIBridgeConfiguration, AIExcitationSource, Double, Boolean, AIVoltageUnits)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createvoltagechannelwithexcitation.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aichannelcollection_createvoltagechannelwithexcitation.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateVoltageChannelWithExcitation Method (String, String, AITerminalConfiguration, Double, Double, AIBridgeConfiguration, AIExcitationSource, Double, Boolean, AIVoltageUnits)

### AIChannelCollectionCreateVoltageChannelWithExcitation Method (String, String, AITerminalConfiguration, Double, Double, AIBridgeConfiguration, AIExcitationSource, Double, Boolean, AIVoltageUnits)

AIChannel

AIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChannel CreateVoltageChannelWithExcitation(
	string physicalChannelName,
	string nameToAssignChannel,
	AITerminalConfiguration configuration,
	double minimumValue,
	double maximumValue,
	AIBridgeConfiguration bridgeConfiguration,
	AIExcitationSource voltageExcitationSource,
	double voltageExcitationValue,
	bool useExcitationForScaling,
	AIVoltageUnits units
)
```

```text
Public Function CreateVoltageChannelWithExcitation ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	configuration As AITerminalConfiguration,
	minimumValue As Double,
	maximumValue As Double,
	bridgeConfiguration As AIBridgeConfiguration,
	voltageExcitationSource As AIExcitationSource,
	voltageExcitationValue As Double,
	useExcitationForScaling As Boolean,
	units As AIVoltageUnits
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
- **bridgeConfiguration**
  - Type: NationalInstruments.DAQmxAIBridgeConfigurationThe bridge configuration. If you set bridgeConfiguration to NoBridge, useExcitationForScaling has no effect.
- **voltageExcitationSource**
  - Type: NationalInstruments.DAQmxAIExcitationSourceThe source of excitation.
- **voltageExcitationValue**
  - Type: SystemDoubleThe amount of excitation in volts that the sensor requires.
- **useExcitationForScaling**
  - Type: SystemBoolean if NI-DAQmx divides the measurement by the excitation. Typically, you set useExcitationForScaling to for ratiometric tranducers. If you set useExcitationForScaling to , set maximumValue and minimumValue to reflect the scaling. For example, if you expect to acquire a voltage between 5 and 5, and you use an excitation of .10 volts to scale the measurement, set minimumValue to 50 and set maximumValue to 50.
- **units**
  - Type: NationalInstruments.DAQmxAIVoltageUnitsThe units to use to return the measurement.

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

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateVoltageChannelWithExcitation(String, String, AITerminalConfiguration, Double, Double, AIBridgeConfiguration, AIExcitationSource, Double, Boolean, AIVoltageUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AIChannelCollection Class

CreateVoltageChannelWithExcitation Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginmemoryoptimizedreadwaveform_1.htm language=enus -->
## TOPIC 00025: AnalogMultiChannelReaderBeginMemoryOptimizedReadWaveform Method (Int32, AsyncCallback, Object, AnalogWaveformDouble, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginmemoryoptimizedreadwaveform_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultichannelreader_beginmemoryoptimizedreadwaveform_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader.BeginMemoryOptimizedReadWaveform Method (Int32, AsyncCallback, Object, AnalogWaveform(Double)[], ReallocationPolicy)

### AnalogMultiChannelReaderBeginMemoryOptimizedReadWaveform Method (Int32, AsyncCallback, Object, AnalogWaveformDouble, ReallocationPolicy)

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
	AnalogWaveform<double>[] data,
	ReallocationPolicy policy
)
```

```text
Public Function BeginMemoryOptimizedReadWaveform ( 
	samplesPerChannel As Integer,
	callback As AsyncCallback,
	state As Object,
	data As AnalogWaveform(Of Double)(),
	policy As ReallocationPolicy
) As IAsyncResult
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallback An optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObject A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: NationalInstrumentsAnalogWaveformDouble An initialized 1D array of AnalogWaveformTData that contains the read data. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicyDictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing
 AnalogWaveformTData
 objects and their corresponding memory to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
 [BeginMemoryOptimizedReadWaveform(Int32, AsyncCallback, Object, AnalogWaveformDouble)](m_nationalinstruments_daqmx_analogmultichannelreader_beginmemoryoptimizedreadwaveform.htm)
 , call
 [EndMemoryOptimizedReadWaveform(IAsyncResult)](m_nationalinstruments_daqmx_analogmultichannelreader_endmemoryoptimizedreadwaveform.htm)
 with the returned
 IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_tostring.htm language=enus -->
## TOPIC 00026: AnalogMultiChannelWriterToString Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_tostring.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelWriter.ToString Method

### AnalogMultiChannelWriterToString Method

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

AnalogMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_writemultisample.htm language=enus -->
## TOPIC 00027: AnalogMultiChannelWriterWriteMultiSample Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_writemultisample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_writemultisample.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelWriter.WriteMultiSample Method

### AnalogMultiChannelWriterWriteMultiSample Method

AOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteMultiSample(
	bool autoStart,
	double[,] data
)
```

```text
Public Sub WriteMultiSample ( 
	autoStart As Boolean,
	data As Double(,)
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemDoubleA 2D array of samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

##### Remarks

DAQ Assistant

If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](m_nationalinstruments_daqmx_task_waituntildone.htm) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

AnalogMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_writesinglesample.htm language=enus -->
## TOPIC 00028: AnalogMultiChannelWriterWriteSingleSample Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_writesinglesample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_writesinglesample.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelWriter.WriteSingleSample Method

### AnalogMultiChannelWriterWriteSingleSample Method

AOChannel

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WriteSingleSample(
	bool autoStart,
	double[] data
)
```

```text
Public Sub WriteSingleSample ( 
	autoStart As Boolean,
	data As Double()
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemDoubleA 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

##### Remarks

DAQ Assistant

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

##### See Also

###### Reference

AnalogMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_writewaveform__1.htm language=enus -->
## TOPIC 00029: AnalogMultiChannelWriterWriteWaveformTData Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_writewaveform__1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultichannelwriter_writewaveform__1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultiedgereferencetrigger_tostring.htm language=enus -->
## TOPIC 00030: AnalogMultiEdgeReferenceTriggerToString Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultiedgereferencetrigger_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultiedgereferencetrigger_tostring.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultiedgestarttrigger_tostring.htm language=enus -->
## TOPIC 00031: AnalogMultiEdgeStartTriggerToString Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultiedgestarttrigger_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogmultiedgestarttrigger_tostring.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_beginreadwaveform.htm language=enus -->
## TOPIC 00032: AnalogSingleChannelReaderBeginReadWaveform Method (Int32, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_beginreadwaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_beginreadwaveform.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelReader.BeginReadWaveform Method (Int32, AsyncCallback, Object)

### AnalogSingleChannelReaderBeginReadWaveform Method (Int32, AsyncCallback, Object)

AIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual IAsyncResult BeginReadWaveform(
	int numberOfSamples,
	AsyncCallback callback,
	Object state
)
```

```text
Public Overridable Function BeginReadWaveform ( 
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

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadWaveform(Int32, AsyncCallback, Object), call [EndReadWaveform(IAsyncResult)](m_nationalinstruments_daqmx_analogsinglechannelreader_endreadwaveform.htm) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](p_nationalinstruments_daqmx_daqstream_waveformattributemode.htm) property of the [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogSingleChannelReader Class

BeginReadWaveform Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_memoryoptimizedreadmultisample.htm language=enus -->
## TOPIC 00033: AnalogSingleChannelReaderMemoryOptimizedReadMultiSample Method (Int32, Double, ReallocationPolicy, Int32)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_memoryoptimizedreadmultisample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_memoryoptimizedreadmultisample.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_readwaveform.htm language=enus -->
## TOPIC 00034: AnalogSingleChannelReaderReadWaveform Method (Int32)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_readwaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_readwaveform.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelReader.ReadWaveform Method (Int32)

### AnalogSingleChannelReaderReadWaveform Method (Int32)

AIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual AnalogWaveform<double> ReadWaveform(
	int numberOfSamples
)
```

```text
Public Overridable Function ReadWaveform ( 
	numberOfSamples As Integer
) As AnalogWaveform(Of Double)
```

###### Parameters

- **numberOfSamples**
  - Type: SystemInt32 The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.

###### Return Value

AnalogWaveform

Double

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

AnalogSingleChannelReader Class

ReadWaveform Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_tostring.htm language=enus -->
## TOPIC 00035: AnalogSingleChannelReaderToString Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelreader_tostring.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelReader.ToString Method

### AnalogSingleChannelReaderToString Method

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

AnalogSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelwriter_beginwritemultisample.htm language=enus -->
## TOPIC 00036: AnalogSingleChannelWriterBeginWriteMultiSample Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelwriter_beginwritemultisample.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelwriter_beginwritemultisample.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelwriter_endwrite.htm language=enus -->
## TOPIC 00037: AnalogSingleChannelWriterEndWrite Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelwriter_endwrite.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogsinglechannelwriter_endwrite.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelWriter.EndWrite Method

### AnalogSingleChannelWriterEndWrite Method

BeginWriteSingleSample(Boolean, Double, AsyncCallback, Object)

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
| IndexOutOfRangeException | The data provided to BeginWriteMultiSample(Boolean, Double, AsyncCallback, Object) has a non-zero lower bound. |

##### Remarks

If you call EndWrite(IAsyncResult) before the asynchronous write represented by the provided IAsyncResult is complete, EndWrite(IAsyncResult) waits for the write to complete before returning. For a write to a buffered task, the write is considered complete when all of the written samples have been transferred to the task buffer. Use [IsDone](p_nationalinstruments_daqmx_task_isdone.htm) or [WaitUntilDone(Int32)](m_nationalinstruments_daqmx_task_waituntildone_1.htm) on the [Task](t_nationalinstruments_daqmx_task.htm) object to determine if a task has generated all of the data it was configured to generate.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogunscaledreader_beginreadint16.htm language=enus -->
## TOPIC 00038: AnalogUnscaledReaderBeginReadInt16 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogunscaledreader_beginreadint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_analogunscaledreader_beginreadint16.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogUnscaledReader.BeginReadInt16 Method

### AnalogUnscaledReaderBeginReadInt16 Method

unscaled

AIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadInt16(
	int samplesPerChannel,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadInt16 ( 
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

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadInt16(Int32, AsyncCallback, Object), call [EndReadInt16(IAsyncResult)](m_nationalinstruments_daqmx_analogunscaledreader_endreadint16.htm) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

AnalogUnscaledReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aochannelcollection_createvoltagechannel.htm language=enus -->
## TOPIC 00039: AOChannelCollectionCreateVoltageChannel Method (String, String, Double, Double, AOVoltageUnits)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aochannelcollection_createvoltagechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aochannelcollection_createvoltagechannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AOChannelCollection.CreateVoltageChannel Method (String, String, Double, Double, AOVoltageUnits)

### AOChannelCollectionCreateVoltageChannel Method (String, String, Double, Double, AOVoltageUnits)

AOChannel

generate voltage

AOChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AOChannel CreateVoltageChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	AOVoltageUnits units
)
```

```text
Public Function CreateVoltageChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	units As AOVoltageUnits
) As AOChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **minimumValue**
  - Type: SystemDoubleThe minimum value to generate, in units.
- **maximumValue**
  - Type: SystemDoubleThe maximum value to generate, in units.
- **units**
  - Type: NationalInstruments.DAQmxAOVoltageUnitsThe units to use to generate voltage.

###### Return Value

AOChannel

AOChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for nameToAssignChannel. If you provide fewer local virtual channel names in nameToAssignChannel than you create, NI-DAQmx [automatically assigns names](/csh?topicname=mxcncpts/;) to the local virtual channels.

If you do not provide a value for nameToAssignChannel, NI-DAQmx uses the physicalChannelName as the local virtual channel name. If you use nameToAssignChannel to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateVoltageChannel(String, String, Double, Double, AOVoltageUnits) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AOChannelCollection Class

CreateVoltageChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aochannelcollection_createvoltagechannel_1.htm language=enus -->
## TOPIC 00040: AOChannelCollectionCreateVoltageChannel Method (String, String, Double, Double, String)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aochannelcollection_createvoltagechannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_aochannelcollection_createvoltagechannel_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AOChannelCollection.CreateVoltageChannel Method (String, String, Double, Double, String)

### AOChannelCollectionCreateVoltageChannel Method (String, String, Double, Double, String)

AOChannel

generate voltage

AOChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AOChannel CreateVoltageChannel(
	string physicalChannelName,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	string customScaleName
)
```

```text
Public Function CreateVoltageChannel ( 
	physicalChannelName As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	customScaleName As String
) As AOChannel
```

###### Parameters

- **physicalChannelName**
  - Type: SystemStringThe names of one or more physical channels to use to create one or more local virtual channels.
- **nameToAssignChannel**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **minimumValue**
  - Type: SystemDoubleThe minimum value to generate.
- **maximumValue**
  - Type: SystemDoubleThe maximum value to generate.
- **customScaleName**
  - Type: SystemStringThe name of the custom scale to apply to the local virtual channel.

###### Return Value

AOChannel

AOChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method creates a local virtual channel for every physical channel name you specify. If you create multiple local virtual channels with one call to this method, you can specify a comma-delimited list of names for nameToAssignChannel. If you provide fewer local virtual channel names in nameToAssignChannel than you create, NI-DAQmx [automatically assigns names](/csh?topicname=mxcncpts/;) to the local virtual channels.

If you do not provide a value for nameToAssignChannel, NI-DAQmx uses the physicalChannelName as the local virtual channel name. If you use nameToAssignChannel to create a name for the local virtual channel, you must use this name in other properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateVoltageChannel(String, String, Double, Double, String) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

AOChannelCollection Class

CreateVoltageChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_cichannelcollection_createangularencoderchannel.htm language=enus -->
## TOPIC 00041: CIChannelCollectionCreateAngularEncoderChannel Method (String, String, CIEncoderDecodingType, Boolean, Double, CIEncoderZIndexPhase, Int32, Double, CIAngularEncoderUnits)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_cichannelcollection_createangularencoderchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_cichannelcollection_createangularencoderchannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannelCollection.CreateAngularEncoderChannel Method (String, String, CIEncoderDecodingType, Boolean, Double, CIEncoderZIndexPhase, Int32, Double, CIAngularEncoderUnits)

### CIChannelCollectionCreateAngularEncoderChannel Method (String, String, CIEncoderDecodingType, Boolean, Double, CIEncoderZIndexPhase, Int32, Double, CIAngularEncoderUnits)

CIChannel

angular encoder

measure angular position

CIChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIChannel CreateAngularEncoderChannel(
	string counter,
	string nameToAssignChannel,
	CIEncoderDecodingType encoderDecodingType,
	bool zIndexEnable,
	double zIndexValue,
	CIEncoderZIndexPhase zIndexPhase,
	int pulsesPerRevolution,
	double initialAngle,
	CIAngularEncoderUnits units
)
```

```text
Public Function CreateAngularEncoderChannel ( 
	counter As String,
	nameToAssignChannel As String,
	encoderDecodingType As CIEncoderDecodingType,
	zIndexEnable As Boolean,
	zIndexValue As Double,
	zIndexPhase As CIEncoderZIndexPhase,
	pulsesPerRevolution As Integer,
	initialAngle As Double,
	units As CIAngularEncoderUnits
) As CIChannel
```

###### Parameters

- **counter**
  - Type: SystemStringThe names of the counters to use to create the virtual channels. You can pass a string that contains a list or range of counters to this input.
- **nameToAssignChannel**
  - Type: SystemStringThe name to assign to the created channel. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **encoderDecodingType**
  - Type: NationalInstruments.DAQmxCIEncoderDecodingTypeThe count and interpretation of the pulses that the encoder generates on signal A and signal B. X1, X2, and X4 are valid for quadrature encoders only. TwoPulseCounting is valid only for two-pulse encoders.
- **zIndexEnable**
  - Type: SystemBooleanWhether to use z indexing for the channel.
- **zIndexValue**
  - Type: SystemDoubleThe value, in units, to which to reset the measurement when signal Z is high, and signal A and signal B are at the states you specify with zIndexPhase.
- **zIndexPhase**
  - Type: NationalInstruments.DAQmxCIEncoderZIndexPhaseThe states that signal A and signal B must be at while signal Z is high for NI-DAQmx to reset the measurement. If the signal Z is never high while the signal A and signal B are high, for example, you must choose a phase other than AHighBHigh.
- **pulsesPerRevolution**
  - Type: SystemInt32The number of pulses that the encoder generates per revolution. This value is the number of pulses on one of either the A signal or the B signal, not the total number of pulses on both the A and B signals.
- **initialAngle**
  - Type: SystemDoubleThe starting angle of the encoder. This value is in the units that you specify in the units parameter.
- **units**
  - Type: NationalInstruments.DAQmxCIAngularEncoderUnitsThe units to use to return angular position measurements from the channel.

###### Return Value

CIChannel

CIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

With the exception of [devices that support multi-counter tasks](/csh?topicname=mxdevconsid/multicounterdevices.html), you can create only one [CIChannel](t_nationalinstruments_daqmx_cichannel.htm) at a time with this function because a task can contain only one [CIChannel](t_nationalinstruments_daqmx_cichannel.htm). To read from multiple counters simultaneously, use a separate task for each counter.

This method creates a virtual channel for the physical channel name you specify.

If you do not provide a value for nameToAssignChannel, NI-DAQmx uses the counter as the local virtual channel name. If you use nameToAssignChannel to create a name for the local virtual channel, you must use this name in other properties and methods.

[X2](t_nationalinstruments_daqmx_ciencoderdecodingtype.htm) and [X4](t_nationalinstruments_daqmx_ciencoderdecodingtype.htm) decoding are more sensitive to smaller changes in position than [X1](t_nationalinstruments_daqmx_ciencoderdecodingtype.htm) encoding, with [X4](t_nationalinstruments_daqmx_ciencoderdecodingtype.htm) being the most sensitive. However, more sensitive decoding is more likely to produce erroneous measurements if vibration exists in the encoder or other noise exists in the signals.

When signal Z goes high and how long it stays high varies from encoder to encoder. Refer to the documentation for the encoder to determine the timing of signal Z with respect to signal A and signal B.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

CIChannelCollection Class

CreateAngularEncoderChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_cichannelcollection_createangularvelocitychannel_1.htm language=enus -->
## TOPIC 00042: CIChannelCollectionCreateAngularVelocityChannel Method (String, String, Double, Double, Int64, CIVelocityEncoderType, String)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_cichannelcollection_createangularvelocitychannel_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_cichannelcollection_createangularvelocitychannel_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannelCollection.CreateAngularVelocityChannel Method (String, String, Double, Double, Int64, CIVelocityEncoderType, String)

### CIChannelCollectionCreateAngularVelocityChannel Method (String, String, Double, Double, Int64, CIVelocityEncoderType, String)

Creates a channel to measure angular velocity.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIChannel CreateAngularVelocityChannel(
	string counter,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	long pulsesPerRevolution,
	CIVelocityEncoderType decodingType,
	string customScaleName
)
```

```text
Public Function CreateAngularVelocityChannel ( 
	counter As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	pulsesPerRevolution As Long,
	decodingType As CIVelocityEncoderType,
	customScaleName As String
) As CIChannel
```

###### Parameters

- **counter**
  - Type: SystemString The name of the counter to use to create virtual channels.
- **nameToAssignChannel**
  - Type: SystemString The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignChannel, use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels.
- **minimumValue**
  - Type: SystemDouble The minimum value, in units, that you expect to measure.
- **maximumValue**
  - Type: SystemDouble The maximum value, in units, that you expect to measure.
- **pulsesPerRevolution**
  - Type: SystemInt64 The number of pulses the encoder generates per revolution. This value is the number of pulses on either signal A or signal B, not the total number of pulses on both signal A and signal B.
- **decodingType**
  - Type: NationalInstruments.DAQmxCIVelocityEncoderType Specifies how to count and interpret the pulses that the encoder generates on signal A and signal B.
- **customScaleName**
  - Type: SystemString The name of a custom scale to apply to the channel.

###### Return Value

CIChannel

##### See Also

###### Reference

CIChannelCollection Class

CreateAngularVelocityChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_cichannelcollection_createangularvelocitychannel_2.htm language=enus -->
## TOPIC 00043: CIChannelCollectionCreateAngularVelocityChannel Method (String, String, Double, Double, UInt32, CIVelocityEncoderType, CIVelocityAngularEncoderUnits)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_cichannelcollection_createangularvelocitychannel_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_cichannelcollection_createangularvelocitychannel_2.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannelCollection.CreateAngularVelocityChannel Method (String, String, Double, Double, UInt32, CIVelocityEncoderType, CIVelocityAngularEncoderUnits)

### CIChannelCollectionCreateAngularVelocityChannel Method (String, String, Double, Double, UInt32, CIVelocityEncoderType, CIVelocityAngularEncoderUnits)

Creates a channel to measure angular velocity.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIChannel CreateAngularVelocityChannel(
	string counter,
	string nameToAssignChannel,
	double minimumValue,
	double maximumValue,
	uint pulsesPerRevolution,
	CIVelocityEncoderType decodingType,
	CIVelocityAngularEncoderUnits units
)
```

```text
Public Function CreateAngularVelocityChannel ( 
	counter As String,
	nameToAssignChannel As String,
	minimumValue As Double,
	maximumValue As Double,
	pulsesPerRevolution As UInteger,
	decodingType As CIVelocityEncoderType,
	units As CIVelocityAngularEncoderUnits
) As CIChannel
```

###### Parameters

- **counter**
  - Type: SystemString The name of the counter to use to create virtual channels.
- **nameToAssignChannel**
  - Type: SystemString The name(s) to assign to the created virtual channel(s). If you do not specify a name, NI-DAQmx uses the physical channel name as the virtual channel name. If you specify your own names for nameToAssignChannel, use the names when you refer to these channels in other NI-DAQmx functions. If you create multiple virtual channels with one call to this function, specify a list of names separated by commas. If you provide fewer names than the number of virtual channels you create, NI-DAQmx automatically assigns names to the virtual channels.
- **minimumValue**
  - Type: SystemDouble The minimum value, in units, that you expect to measure.
- **maximumValue**
  - Type: SystemDouble The maximum value, in units, that you expect to measure.
- **pulsesPerRevolution**
  - Type: SystemUInt32 The number of pulses the encoder generates per revolution. This value is the number of pulses on either signal A or signal B, not the total number of pulses on both signal A and signal B.
- **decodingType**
  - Type: NationalInstruments.DAQmxCIVelocityEncoderType Specifies how to count and interpret the pulses that the encoder generates on signal A and signal B.
- **units**
  - Type: NationalInstruments.DAQmxCIVelocityAngularEncoderUnits Specifies in which unit to return velocity measurements from the channel.

###### Return Value

CIChannel

##### Remarks

multi-counter tasks

default input terminal

##### See Also

###### Reference

CIChannelCollection Class

CreateAngularVelocityChannel Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_cidatatime_op_inequality.htm language=enus -->
## TOPIC 00044: CIDataTimeInequality Operator

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_cidatatime_op_inequality.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_cidatatime_op_inequality.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataTime.Inequality Operator

### CIDataTimeInequality Operator

CIDataTime

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public static bool operator !=(
	CIDataTime c1,
	CIDataTime c2
)
```

```text
Public Shared Operator <> ( 
	c1 As CIDataTime,
	c2 As CIDataTime
) As Boolean
```

###### Parameters

- **c1**
  - Type: NationalInstruments.DAQmxCIDataTime A CIDataTime object.
- **c2**
  - Type: NationalInstruments.DAQmxCIDataTime A CIDataTime object.

###### Return Value

Boolean

c1

c2

##### See Also

###### Reference

CIDataTime Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_codatafrequency_equals.htm language=enus -->
## TOPIC 00045: CODataFrequencyEquals Method (CODataFrequency)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_codatafrequency_equals.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_codatafrequency_equals.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CODataFrequency.Equals Method (CODataFrequency)

### CODataFrequencyEquals Method (CODataFrequency)

CODataFrequency

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool Equals(
	CODataFrequency c
)
```

```text
Public Function Equals ( 
	c As CODataFrequency
) As Boolean
```

###### Parameters

- **c**
  - Type: NationalInstruments.DAQmxCODataFrequencyA CODataFrequency to compare with this instance.

###### Return Value

Boolean

c

##### See Also

###### Reference

CODataFrequency Structure

Equals Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_codataticks_equals.htm language=enus -->
## TOPIC 00046: CODataTicksEquals Method (CODataTicks)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_codataticks_equals.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_codataticks_equals.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CODataTicks.Equals Method (CODataTicks)

### CODataTicksEquals Method (CODataTicks)

CODataTicks

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool Equals(
	CODataTicks c
)
```

```text
Public Function Equals ( 
	c As CODataTicks
) As Boolean
```

###### Parameters

- **c**
  - Type: NationalInstruments.DAQmxCODataTicksA CODataTicks object to compare with this instance.

###### Return Value

Boolean

c

##### See Also

###### Reference

CODataTicks Structure

Equals Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_codataticks_equals_1.htm language=enus -->
## TOPIC 00047: CODataTicksEquals Method (CODataTicks, CODataTicks)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_codataticks_equals_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_codataticks_equals_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CODataTicks.Equals Method (CODataTicks, CODataTicks)

### CODataTicksEquals Method (CODataTicks, CODataTicks)

CODataTicks

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public static bool Equals(
	CODataTicks c1,
	CODataTicks c2
)
```

```text
Public Shared Function Equals ( 
	c1 As CODataTicks,
	c2 As CODataTicks
) As Boolean
```

###### Parameters

- **c1**
  - Type: NationalInstruments.DAQmxCODataTicksA CODataTicks object.
- **c2**
  - Type: NationalInstruments.DAQmxCODataTicksA CODataTicks object.

###### Return Value

Boolean

c1

c2

##### See Also

###### Reference

CODataTicks Structure

Equals Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader__ctor.htm language=enus -->
## TOPIC 00048: CounterMultiChannelReader Constructor

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader__ctor.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader Constructor

### CounterMultiChannelReader Constructor

CounterMultiChannelReader

DaqStream

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CounterMultiChannelReader(
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

CounterMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginmemoryoptimizedreadmultisampleint32.htm language=enus -->
## TOPIC 00049: CounterMultiChannelReaderBeginMemoryOptimizedReadMultiSampleInt32 Method (Int32, AsyncCallback, Object, Int32)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginmemoryoptimizedreadmultisampleint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginmemoryoptimizedreadmultisampleint32.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader.BeginMemoryOptimizedReadMultiSampleInt32 Method (Int32, AsyncCallback, Object, Int32[,])

### CounterMultiChannelReaderBeginMemoryOptimizedReadMultiSampleInt32 Method (Int32, AsyncCallback, Object, Int32)

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
	int samplesPerChannel,
	AsyncCallback callback,
	Object state,
	int[,] data
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSampleInt32 ( 
	samplesPerChannel As Integer,
	callback As AsyncCallback,
	state As Object,
	data As Integer(,)
) As IAsyncResult
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallback An optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObject A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemInt32An initialized 2D array of Int32 samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
 this method, call 


[EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult, Int32)](m_nationalinstruments_daqmx_countermultichannelreader_endmemoryoptimizedreadmultisampleint32.htm)
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

CounterMultiChannelReader Class

BeginMemoryOptimizedReadMultiSampleInt32 Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginmemoryoptimizedreadmultisampleint32_1.htm language=enus -->
## TOPIC 00050: CounterMultiChannelReaderBeginMemoryOptimizedReadMultiSampleInt32 Method (Int32, AsyncCallback, Object, Int32, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginmemoryoptimizedreadmultisampleint32_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginmemoryoptimizedreadmultisampleint32_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader.BeginMemoryOptimizedReadMultiSampleInt32 Method (Int32, AsyncCallback, Object, Int32[,], ReallocationPolicy)

### CounterMultiChannelReaderBeginMemoryOptimizedReadMultiSampleInt32 Method (Int32, AsyncCallback, Object, Int32, ReallocationPolicy)

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
	int samplesPerChannel,
	AsyncCallback callback,
	Object state,
	int[,] data,
	ReallocationPolicy policy
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSampleInt32 ( 
	samplesPerChannel As Integer,
	callback As AsyncCallback,
	state As Object,
	data As Integer(,),
	policy As ReallocationPolicy
) As IAsyncResult
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specifyif you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specifyif you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemInt32An initialized 2D array of Int32 samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicyDictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
 this method, call 

[EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult, Int32)](m_nationalinstruments_daqmx_countermultichannelreader_endmemoryoptimizedreadmultisampleint32.htm)
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

CounterMultiChannelReader Class

BeginMemoryOptimizedReadMultiSampleInt32 Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginmemoryoptimizedreadmultisampleuint32.htm language=enus -->
## TOPIC 00051: CounterMultiChannelReaderBeginMemoryOptimizedReadMultiSampleUInt32 Method (Int32, AsyncCallback, Object, UInt32)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginmemoryoptimizedreadmultisampleuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginmemoryoptimizedreadmultisampleuint32.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader.BeginMemoryOptimizedReadMultiSampleUInt32 Method (Int32, AsyncCallback, Object, UInt32[,])

### CounterMultiChannelReaderBeginMemoryOptimizedReadMultiSampleUInt32 Method (Int32, AsyncCallback, Object, UInt32)

UInt32

CIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadMultiSampleUInt32(
	int samplesPerChannel,
	AsyncCallback callback,
	Object state,
	uint[,] data
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSampleUInt32 ( 
	samplesPerChannel As Integer,
	callback As AsyncCallback,
	state As Object,
	data As UInteger(,)
) As IAsyncResult
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallback An optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObject A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemUInt32An initialized 2D array of UInt32 samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
 this method, call [EndMemoryOptimizedReadMultiSampleUInt32(IAsyncResult, Int32)](m_nationalinstruments_daqmx_countermultichannelreader_endmemoryoptimizedreadmultisampleuint32.htm)
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

CounterMultiChannelReader Class

BeginMemoryOptimizedReadMultiSampleUInt32 Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginmemoryoptimizedreadmultisampleuint32_1.htm language=enus -->
## TOPIC 00052: CounterMultiChannelReaderBeginMemoryOptimizedReadMultiSampleUInt32 Method (Int32, AsyncCallback, Object, UInt32, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginmemoryoptimizedreadmultisampleuint32_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginmemoryoptimizedreadmultisampleuint32_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader.BeginMemoryOptimizedReadMultiSampleUInt32 Method (Int32, AsyncCallback, Object, UInt32[,], ReallocationPolicy)

### CounterMultiChannelReaderBeginMemoryOptimizedReadMultiSampleUInt32 Method (Int32, AsyncCallback, Object, UInt32, ReallocationPolicy)

UInt32

CIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadMultiSampleUInt32(
	int samplesPerChannel,
	AsyncCallback callback,
	Object state,
	uint[,] data,
	ReallocationPolicy policy
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSampleUInt32 ( 
	samplesPerChannel As Integer,
	callback As AsyncCallback,
	state As Object,
	data As UInteger(,),
	policy As ReallocationPolicy
) As IAsyncResult
```

###### Parameters

- **samplesPerChannel**
  - Type: SystemInt32The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from.
- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specifyif you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemUInt32An initialized 2D array of UInt32 samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicyDictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
 this method, call [EndMemoryOptimizedReadMultiSampleUInt32(IAsyncResult, Int32)](m_nationalinstruments_daqmx_countermultichannelreader_endmemoryoptimizedreadmultisampleuint32.htm)
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

CounterMultiChannelReader Class

BeginMemoryOptimizedReadMultiSampleUInt32 Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadmultisampledouble.htm language=enus -->
## TOPIC 00053: CounterMultiChannelReaderBeginReadMultiSampleDouble Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadmultisampledouble.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadmultisampledouble.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader.BeginReadMultiSampleDouble Method

### CounterMultiChannelReaderBeginReadMultiSampleDouble Method

Double

CIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadMultiSampleDouble(
	int samplesPerChannel,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadMultiSampleDouble ( 
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

To get the read data or any exceptions that occurred during an asynchronous read initiated with 

BeginReadMultiSampleDouble(Int32, AsyncCallback, Object), call 

[EndReadMultiSampleDouble(IAsyncResult)](m_nationalinstruments_daqmx_countermultichannelreader_endreadmultisampledouble.htm) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

CounterMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadmultisampleint32.htm language=enus -->
## TOPIC 00054: CounterMultiChannelReaderBeginReadMultiSampleInt32 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadmultisampleint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadmultisampleint32.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader.BeginReadMultiSampleInt32 Method

### CounterMultiChannelReaderBeginReadMultiSampleInt32 Method

Int32

CIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadMultiSampleInt32(
	int samplesPerChannel,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadMultiSampleInt32 ( 
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

To get the read data or any exceptions that occurred during an asynchronous read initiated with 


BeginReadMultiSampleInt32(Int32, AsyncCallback, Object), call [EndReadMultiSampleInt32(IAsyncResult)](m_nationalinstruments_daqmx_countermultichannelreader_endreadmultisampleint32.htm) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

CounterMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadmultisampleuint32.htm language=enus -->
## TOPIC 00055: CounterMultiChannelReaderBeginReadMultiSampleUInt32 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadmultisampleuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadmultisampleuint32.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader.BeginReadMultiSampleUInt32 Method

### CounterMultiChannelReaderBeginReadMultiSampleUInt32 Method

UInt32

CIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadMultiSampleUInt32(
	int samplesPerChannel,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadMultiSampleUInt32 ( 
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

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSampleUInt32(Int32, AsyncCallback, Object), call [EndReadMultiSampleUInt32(IAsyncResult)](m_nationalinstruments_daqmx_countermultichannelreader_endreadmultisampleuint32.htm) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

CounterMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadsinglesampledouble.htm language=enus -->
## TOPIC 00056: CounterMultiChannelReaderBeginReadSingleSampleDouble Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadsinglesampledouble.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadsinglesampledouble.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader.BeginReadSingleSampleDouble Method

### CounterMultiChannelReaderBeginReadSingleSampleDouble Method

Double

CIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadSingleSampleDouble(
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadSingleSampleDouble ( 
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

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSampleDouble(AsyncCallback, Object), call [EndReadSingleSampleDouble(IAsyncResult)](m_nationalinstruments_daqmx_countermultichannelreader_endreadsinglesampledouble.htm) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

CounterMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadsinglesampleint32.htm language=enus -->
## TOPIC 00057: CounterMultiChannelReaderBeginReadSingleSampleInt32 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadsinglesampleint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadsinglesampleint32.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader.BeginReadSingleSampleInt32 Method

### CounterMultiChannelReaderBeginReadSingleSampleInt32 Method

Int32

CIChannel

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

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSampleInt32(AsyncCallback, Object), call [EndReadSingleSampleInt32(IAsyncResult)](m_nationalinstruments_daqmx_countermultichannelreader_endreadsinglesampleint32.htm) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

CounterMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadsinglesampleuint32.htm language=enus -->
## TOPIC 00058: CounterMultiChannelReaderBeginReadSingleSampleUInt32 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadsinglesampleuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_beginreadsinglesampleuint32.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader.BeginReadSingleSampleUInt32 Method

### CounterMultiChannelReaderBeginReadSingleSampleUInt32 Method

UInt32

CIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadSingleSampleUInt32(
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadSingleSampleUInt32 ( 
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

To get the read data or any exceptions that occurred during an asynchronous read initiated with 

BeginReadSingleSampleUInt32(AsyncCallback, Object), call [EndReadSingleSampleUInt32(IAsyncResult)](m_nationalinstruments_daqmx_countermultichannelreader_endreadsinglesampleuint32.htm) with the returned 
IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

| Note |
| --- |
| Refer to Asynchronous Reads and Writes for additional information. |

##### See Also

###### Reference

CounterMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_endmemoryoptimizedreadmultisampledouble.htm language=enus -->
## TOPIC 00059: CounterMultiChannelReaderEndMemoryOptimizedReadMultiSampleDouble Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_endmemoryoptimizedreadmultisampledouble.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countermultichannelreader_endmemoryoptimizedreadmultisampledouble.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader.EndMemoryOptimizedReadMultiSampleDouble Method

### CounterMultiChannelReaderEndMemoryOptimizedReadMultiSampleDouble Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[,] EndMemoryOptimizedReadMultiSampleDouble(
	IAsyncResult asyncResult,
	out int actualNumberOfSamplesPerChannelRead
)
```

```text
Public Function EndMemoryOptimizedReadMultiSampleDouble ( 
	asyncResult As IAsyncResult,
	<OutAttribute> ByRef actualNumberOfSamplesPerChannelRead As Integer
) As Double(,)
```

###### Parameters

- **asyncResult**
  - Type: SystemIAsyncResult An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double).
- **actualNumberOfSamplesPerChannelRead**
  - Type: SystemInt32The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data.

###### Return Value

Double

Double

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | If data is or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; orFor asynchronous reads, if asyncResult is or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double). |
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

CounterMultiChannelReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginmemoryoptimizedreadmultisamplepulsefrequency.htm language=enus -->
## TOPIC 00060: CounterSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePulseFrequency Method (Int32, AsyncCallback, Object, CIDataFrequency)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginmemoryoptimizedreadmultisamplepulsefrequency.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countersinglechannelreader_beginmemoryoptimizedreadmultisamplepulsefrequency.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.BeginMemoryOptimizedReadMultiSamplePulseFrequency Method (Int32, AsyncCallback, Object, CIDataFrequency[])

### CounterSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePulseFrequency Method (Int32, AsyncCallback, Object, CIDataFrequency)

CIDataFrequency

CIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadMultiSamplePulseFrequency(
	int numberOfSamples,
	AsyncCallback callback,
	Object state,
	CIDataFrequency[] data
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSamplePulseFrequency ( 
	numberOfSamples As Integer,
	callback As AsyncCallback,
	state As Object,
	data As CIDataFrequency()
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
  - Type: NationalInstruments.DAQmxCIDataFrequencyAn initialized 1D array of CIDataFrequency samples that contains the read data. Each element in the array corresponds to a sample from the channel.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. The memory allocation for the buffer is available to a maximum of 2 GB.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePulseFrequency(IAsyncResult, Int32)](m_nationalinstruments_daqmx_countersinglechannelreader_endmemoryoptimizedreadmultisamplepulsefrequency.htm) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the
[DAQ Assistant](/csh?topicname=taskconfig/daq_config_asst_help.html).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

##### See Also

###### Reference

CounterSingleChannelReader Class

BeginMemoryOptimizedReadMultiSamplePulseFrequency Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countersinglechannelwriter_writesinglesample_2.htm language=enus -->
## TOPIC 00061: CounterSingleChannelWriterWriteSingleSample Method (Boolean, CODataTime)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countersinglechannelwriter_writesinglesample_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_countersinglechannelwriter_writesinglesample_2.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqexception__ctor_1.htm language=enus -->
## TOPIC 00062: DaqException Constructor (SerializationInfo, StreamingContext)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqexception__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqexception__ctor_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqexception__ctor_2.htm language=enus -->
## TOPIC 00063: DaqException Constructor (String)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqexception__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqexception__ctor_2.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_addcdaqsynchronizationconnection.htm language=enus -->
## TOPIC 00064: DaqSystemAddCDaqSynchronizationConnection Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_addcdaqsynchronizationconnection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_addcdaqsynchronizationconnection.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.AddCDaqSynchronizationConnection Method

### DaqSystemAddCDaqSynchronizationConnection Method

Adds a cDAQ Sync connection between devices. The connection is not verified.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void AddCDaqSynchronizationConnection(
	string portList
)
```

```text
Public Sub AddCDaqSynchronizationConnection ( 
	portList As String
)
```

###### Parameters

- **portList**
  - Type: SystemStringSpecifies the cDAQ Sync ports to connect.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_addnetworkdevice.htm language=enus -->
## TOPIC 00065: DaqSystemAddNetworkDevice Method (String, String, Boolean, Double)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_addnetworkdevice.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_addnetworkdevice.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_connectterminals.htm language=enus -->
## TOPIC 00066: DaqSystemConnectTerminals Method (String, String)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_connectterminals.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_connectterminals.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_createwatchdogtimertask.htm language=enus -->
## TOPIC 00067: DaqSystemCreateWatchdogTimerTask Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_createwatchdogtimertask.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_createwatchdogtimertask.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_getsavedchannelinfo.htm language=enus -->
## TOPIC 00068: DaqSystemGetSavedChannelInfo Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_getsavedchannelinfo.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_getsavedchannelinfo.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.GetSavedChannelInfo Method

### DaqSystemGetSavedChannelInfo Method

SavedChannelInfo

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public SavedChannelInfo GetSavedChannelInfo(
	string persistedName
)
```

```text
Public Function GetSavedChannelInfo ( 
	persistedName As String
) As SavedChannelInfo
```

###### Parameters

- **persistedName**
  - Type: SystemStringThe name of the global channel stored in MAX.

###### Return Value

SavedChannelInfo

SavedChannelInfo

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_getsavedtaskinfo.htm language=enus -->
## TOPIC 00069: DaqSystemGetSavedTaskInfo Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_getsavedtaskinfo.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_getsavedtaskinfo.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.GetSavedTaskInfo Method

### DaqSystemGetSavedTaskInfo Method

SavedTaskInfo

task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public SavedTaskInfo GetSavedTaskInfo(
	string persistedName
)
```

```text
Public Function GetSavedTaskInfo ( 
	persistedName As String
) As SavedTaskInfo
```

###### Parameters

- **persistedName**
  - Type: SystemStringThe name of the task stored in MAX.

###### Return Value

SavedTaskInfo

SavedTaskInfo

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_getswitchrelaycount.htm language=enus -->
## TOPIC 00070: DaqSystemGetSwitchRelayCount Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_getswitchrelaycount.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_getswitchrelaycount.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.GetSwitchRelayCount Method

### DaqSystemGetSwitchRelayCount Method

**Note: This API is now obsolete.**

Returns the number of times a relay has actuated on switches that support querying the relay count.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This method is obsolete.")]
public long GetSwitchRelayCount(
	string relay
)
```

```text
<ObsoleteAttribute("This method is obsolete.")>
Public Function GetSwitchRelayCount ( 
	relay As String
) As Long
```

###### Parameters

- **relay**
  - Type: SystemStringThe relay you want to query.

###### Return Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

You must wait for the switch to settle before this method can determine an accurate relay count. Use this method to track relay lifetime and usage.

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_getswitchrelaycounts.htm language=enus -->
## TOPIC 00071: DaqSystemGetSwitchRelayCounts Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_getswitchrelaycounts.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_daqsystem_getswitchrelaycounts.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.GetSwitchRelayCounts Method

### DaqSystemGetSwitchRelayCounts Method

**Note: This API is now obsolete.**

Returns the number of times a set of relays have actuated.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This method is obsolete.")]
public long[] GetSwitchRelayCounts(
	string relays
)
```

```text
<ObsoleteAttribute("This method is obsolete.")>
Public Function GetSwitchRelayCounts ( 
	relays As String
) As Long()
```

###### Parameters

- **relays**
  - Type: SystemStringThe set of relays you want to query. You can use a string that contains a comma-delimited list of relays.

###### Return Value

Int64

relays

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

You must wait for the switch to settle before this method can determine an accurate relay count. Use this method to track relay lifetime and usage.

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_dichannelcollection_tostring.htm language=enus -->
## TOPIC 00072: DIChannelCollectionToString Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_dichannelcollection_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_dichannelcollection_tostring.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitaledgewatchdogexpirationtrigger_tostring.htm language=enus -->
## TOPIC 00073: DigitalEdgeWatchdogExpirationTriggerToString Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitaledgewatchdogexpirationtrigger_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitaledgewatchdogexpirationtrigger_tostring.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeWatchdogExpirationTrigger.ToString Method

### DigitalEdgeWatchdogExpirationTriggerToString Method

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

DigitalEdgeWatchdogExpirationTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginmemoryoptimizedreadmultisampleportbyte_1.htm language=enus -->
## TOPIC 00074: DigitalMultiChannelReaderBeginMemoryOptimizedReadMultiSamplePortByte Method (Int32, AsyncCallback, Object, Byte, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginmemoryoptimizedreadmultisampleportbyte_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginmemoryoptimizedreadmultisampleportbyte_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.BeginMemoryOptimizedReadMultiSamplePortByte Method (Int32, AsyncCallback, Object, Byte[,], ReallocationPolicy)

### DigitalMultiChannelReaderBeginMemoryOptimizedReadMultiSamplePortByte Method (Int32, AsyncCallback, Object, Byte, ReallocationPolicy)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortByte(
	int samplesPerChannel,
	AsyncCallback callback,
	Object state,
	byte[,] data,
	ReallocationPolicy policy
)
```

```text
Public Function BeginMemoryOptimizedReadMultiSamplePortByte ( 
	samplesPerChannel As Integer,
	callback As AsyncCallback,
	state As Object,
	data As Byte(,),
	policy As ReallocationPolicy
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
  - Type: SystemByte An initialized 2D array of 8-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.
- **policy**
  - Type: NationalInstruments.DAQmxReallocationPolicy Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
this method, call [EndMemoryOptimizedReadMultiSamplePortByte(IAsyncResult, Int32)](m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadmultisampleportbyte.htm)
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

BeginMemoryOptimizedReadMultiSamplePortByte Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginmemoryoptimizedreadsinglesamplemultiline.htm language=enus -->
## TOPIC 00075: DigitalMultiChannelReaderBeginMemoryOptimizedReadSingleSampleMultiLine Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginmemoryoptimizedreadsinglesamplemultiline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginmemoryoptimizedreadsinglesamplemultiline.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.BeginMemoryOptimizedReadSingleSampleMultiLine Method

### DigitalMultiChannelReaderBeginMemoryOptimizedReadSingleSampleMultiLine Method

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
	bool[,] data
)
```

```text
Public Function BeginMemoryOptimizedReadSingleSampleMultiLine ( 
	callback As AsyncCallback,
	state As Object,
	data As Boolean(,)
) As IAsyncResult
```

###### Parameters

- **callback**
  - Type: SystemAsyncCallbackAn optional asynchronous callback that is called when the read is complete. Specify if you do not want a callback when the read is complete.
- **state**
  - Type: SystemObjectA user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify if you do not need to pass any additional information to the callback.
- **data**
  - Type: SystemBooleanAn initialized 2D array of Boolean samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a line in that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead.

###### Return Value

IAsyncResult

IAsyncResult

##### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with
this method, call [EndMemoryOptimizedReadSingleSampleMultiLine(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelreader_endmemoryoptimizedreadsinglesamplemultiline.htm)
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

NationalInstruments.DAQmx Namespace

###### Other Resources

Asynchronous Reads and Writes

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginreadmultisampleportbyte.htm language=enus -->
## TOPIC 00076: DigitalMultiChannelReaderBeginReadMultiSamplePortByte Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginreadmultisampleportbyte.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_beginreadmultisampleportbyte.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader.BeginReadMultiSamplePortByte Method

### DigitalMultiChannelReaderBeginReadMultiSamplePortByte Method

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginReadMultiSamplePortByte(
	int samplesPerChannel,
	AsyncCallback callback,
	Object state
)
```

```text
Public Function BeginReadMultiSamplePortByte ( 
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

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePortByte(Int32, AsyncCallback, Object), call [EndReadMultiSamplePortByte(IAsyncResult)](m_nationalinstruments_daqmx_digitalmultichannelreader_endreadmultisampleportbyte.htm) with the returned IAsyncResult.

Use this method for devices with up to eight lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](/csh?topicname=ninetdaqmxfx40/netdaqmxrsandws.html) for more information about memory limitations in NI-DAQmx read methods.

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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportint16.htm language=enus -->
## TOPIC 00077: DigitalMultiChannelReaderReadSingleSamplePortInt16 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readsinglesampleportint16.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readwaveform_1.htm language=enus -->
## TOPIC 00078: DigitalMultiChannelReaderReadWaveform Method (TimeSpan)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readwaveform_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelreader_readwaveform_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_3.htm language=enus -->
## TOPIC 00079: DigitalMultiChannelWriterBeginWriteMultiSamplePort Method (Boolean, UInt16, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_3.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_4.htm language=enus -->
## TOPIC 00080: DigitalMultiChannelWriterBeginWriteMultiSamplePort Method (Boolean, UInt32, AsyncCallback, Object)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_4.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritemultisampleport_4.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesamplesingleline.htm language=enus -->
## TOPIC 00081: DigitalMultiChannelWriterBeginWriteSingleSampleSingleLine Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesamplesingleline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_beginwritesinglesamplesingleline.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_tostring.htm language=enus -->
## TOPIC 00082: DigitalMultiChannelWriterToString Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_tostring.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport_1.htm language=enus -->
## TOPIC 00083: DigitalMultiChannelWriterWriteMultiSamplePort Method (Boolean, Int16)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writemultisampleport_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport_4.htm language=enus -->
## TOPIC 00084: DigitalMultiChannelWriterWriteSingleSamplePort Method (Boolean, UInt32)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport_4.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalmultichannelwriter_writesinglesampleport_4.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_writesinglesamplemultiline.htm language=enus -->
## TOPIC 00085: DigitalSingleChannelWriterWriteSingleSampleMultiLine Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_writesinglesamplemultiline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_writesinglesamplemultiline.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelWriter.WriteSingleSampleMultiLine Method

### DigitalSingleChannelWriterWriteSingleSampleMultiLine Method

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
	bool[] data
)
```

```text
Public Sub WriteSingleSampleMultiLine ( 
	autoStart As Boolean,
	data As Boolean()
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemBooleanA 1D array of samples to write to the task. Each element of the array corresponds to a digital line within the channel.

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

DigitalSingleChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_writesinglesampleport.htm language=enus -->
## TOPIC 00086: DigitalSingleChannelWriterWriteSingleSamplePort Method (Boolean, Byte)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_writesinglesampleport.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_digitalsinglechannelwriter_writesinglesampleport.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelWriter.WriteSingleSamplePort Method (Boolean, Byte)

### DigitalSingleChannelWriterWriteSingleSamplePort Method (Boolean, Byte)

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
	byte data
)
```

```text
Public Sub WriteSingleSamplePort ( 
	autoStart As Boolean,
	data As Byte
)
```

###### Parameters

- **autoStart**
  - Type: SystemBoolean If set to this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to if you have installed events on the task.
- **data**
  - Type: SystemByteA sample to write to the task.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](p_nationalinstruments_daqmx_daqstream_timeout.htm) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

##### See Also

###### Reference

DigitalSingleChannelWriter Class

WriteSingleSamplePort Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_dochannelcollection_createchannel.htm language=enus -->
## TOPIC 00087: DOChannelCollectionCreateChannel Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_dochannelcollection_createchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_dochannelcollection_createchannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DOChannelCollection.CreateChannel Method

### DOChannelCollectionCreateChannel Method

DOChannel

generate digital signals

DOChannelCollection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DOChannel CreateChannel(
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
) As DOChannel
```

###### Parameters

- **lines**
  - Type: SystemStringThe names of the digital lines or ports to use to create the virtual channel.
- **nameToAssign**
  - Type: SystemString One or more names to assign to the created local virtual channels. To use the physical channel name as the local virtual channel name, set this value to Empty.
- **grouping**
  - Type: NationalInstruments.DAQmxChannelLineGroupingThe grouping of digital lines into one or more DOChannel objects. If you specify one or more entire ports with lines, you must set grouping to OneChannelForAllLines.

###### Return Value

DOChannel

DOChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

DOChannel

DOChannel

lines

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateChannel(String, String, ChannelLineGrouping) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

##### See Also

###### Reference

DOChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_everynsamplesreadeventargs_getobjectdata.htm language=enus -->
## TOPIC 00088: EveryNSamplesReadEventArgsGetObjectData Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_everynsamplesreadeventargs_getobjectdata.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_everynsamplesreadeventargs_getobjectdata.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

EveryNSamplesReadEventArgs.GetObjectData Method

### EveryNSamplesReadEventArgsGetObjectData Method

SerializationInfo

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void GetObjectData(
	SerializationInfo info,
	StreamingContext context
)
```

```text
Protected Overridable Sub GetObjectData ( 
	info As SerializationInfo,
	context As StreamingContext
)
```

###### Parameters

- **info**
  - Type: System.Runtime.SerializationSerializationInfo Object that holds the serialized object data.
- **context**
  - Type: System.Runtime.SerializationStreamingContext Contextual information about the source or destination.

##### See Also

###### Reference

EveryNSamplesReadEventArgs Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust1142.htm language=enus -->
## TOPIC 00089: ExternalCalibrationSessionAdjust1142 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust1142.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust1142.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust1142 Method

### ExternalCalibrationSessionAdjust1142 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust1142(
	double referenceVoltage,
	double measuredOutput
)
```

```text
Public Sub Adjust1142 ( 
	referenceVoltage As Double,
	measuredOutput As Double
)
```

###### Parameters

- **referenceVoltage**
  - Type: SystemDoubleThe known voltage, in volts, to use as a reference for calibration.
- **measuredOutput**
  - Type: SystemDoubleThe measured output, in volts, for the channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

referenceVoltage

measuredOutput

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust1143.htm language=enus -->
## TOPIC 00090: ExternalCalibrationSessionAdjust1143 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust1143.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust1143.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust1143 Method

### ExternalCalibrationSessionAdjust1143 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust1143(
	double referenceVoltage,
	double measuredOutput
)
```

```text
Public Sub Adjust1143 ( 
	referenceVoltage As Double,
	measuredOutput As Double
)
```

###### Parameters

- **referenceVoltage**
  - Type: SystemDoubleThe known voltage, in volts, to use as a reference for calibration.
- **measuredOutput**
  - Type: SystemDoubleThe measured output, in volts, for the channel.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

referenceVoltage

measuredOutput

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust11601.htm language=enus -->
## TOPIC 00091: ExternalCalibrationSessionAdjust11601 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust11601.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust11601.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust11601 Method

### ExternalCalibrationSessionAdjust11601 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust11601(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust11601 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust11603.htm language=enus -->
## TOPIC 00092: ExternalCalibrationSessionAdjust11603 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust11603.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust11603.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust11603 Method

### ExternalCalibrationSessionAdjust11603 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust11603(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust11603 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust11605.htm language=enus -->
## TOPIC 00093: ExternalCalibrationSessionAdjust11605 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust11605.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust11605.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust11605 Method

### ExternalCalibrationSessionAdjust11605 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust11605(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust11605 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9205.htm language=enus -->
## TOPIC 00094: ExternalCalibrationSessionAdjust9205 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9205.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9205.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9205 Method

### ExternalCalibrationSessionAdjust9205 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9205(
	double value
)
```

```text
Public Sub Adjust9205 ( 
	value As Double
)
```

###### Parameters

- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9208gain.htm language=enus -->
## TOPIC 00095: ExternalCalibrationSessionAdjust9208Gain Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9208gain.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9208gain.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9208Gain Method

### ExternalCalibrationSessionAdjust9208Gain Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9208Gain(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9208Gain ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9209offset.htm language=enus -->
## TOPIC 00096: ExternalCalibrationSessionAdjust9209Offset Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9209offset.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9209offset.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9209Offset Method

### ExternalCalibrationSessionAdjust9209Offset Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9209Offset(
	string physicalChannels
)
```

```text
Public Sub Adjust9209Offset ( 
	physicalChannels As String
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemString Specifies the physical channel(s) to calibrate.

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9220.htm language=enus -->
## TOPIC 00097: ExternalCalibrationSessionAdjust9220 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9220.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9220.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9220 Method

### ExternalCalibrationSessionAdjust9220 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9220(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9220 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9221.htm language=enus -->
## TOPIC 00098: ExternalCalibrationSessionAdjust9221 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9221.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9221.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9221 Method

### ExternalCalibrationSessionAdjust9221 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9221(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9221 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9222.htm language=enus -->
## TOPIC 00099: ExternalCalibrationSessionAdjust9222 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9222.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9222.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9222 Method

### ExternalCalibrationSessionAdjust9222 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9222(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9222 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9226.htm language=enus -->
## TOPIC 00100: ExternalCalibrationSessionAdjust9226 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9226.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9226.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9226 Method

### ExternalCalibrationSessionAdjust9226 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9226(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9226 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9229.htm language=enus -->
## TOPIC 00101: ExternalCalibrationSessionAdjust9229 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9229.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9229.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9229 Method

### ExternalCalibrationSessionAdjust9229 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9229(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9229 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the physical channel(s) to calibrate.
- **value**
  - Type: SystemDoubleSpecifies the reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9251.htm language=enus -->
## TOPIC 00102: ExternalCalibrationSessionAdjust9251 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9251.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9251.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9251 Method

### ExternalCalibrationSessionAdjust9251 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9251(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9251 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemString The physical channel(s) to calibrate.
- **value**
  - Type: SystemDouble The reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9252.htm language=enus -->
## TOPIC 00103: ExternalCalibrationSessionAdjust9252 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9252.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9252.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9252 Method

### ExternalCalibrationSessionAdjust9252 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9252(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9252 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemString The physical channel(s) to calibrate.
- **value**
  - Type: SystemDouble The reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9253.htm language=enus -->
## TOPIC 00104: ExternalCalibrationSessionAdjust9253 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9253.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9253.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9253 Method

### ExternalCalibrationSessionAdjust9253 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9253(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9253 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemString The physical channel(s) to calibrate.
- **value**
  - Type: SystemDouble The reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9260.htm language=enus -->
## TOPIC 00105: ExternalCalibrationSessionAdjust9260 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9260.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_adjust9260.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Adjust9260 Method

### ExternalCalibrationSessionAdjust9260 Method

external calibration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Adjust9260(
	string physicalChannels,
	double value
)
```

```text
Public Sub Adjust9260 ( 
	physicalChannels As String,
	value As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemString The physical channel(s) to calibrate.
- **value**
  - Type: SystemDouble The reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup4322.htm language=enus -->
## TOPIC 00106: ExternalCalibrationSessionSetup4322 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup4322.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup4322.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup4322 Method

### ExternalCalibrationSessionSetup4322 Method

Configures the calibration task for an NI 4322 device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup4322(
	string physicalChannels,
	AOOutputType outputType,
	double outputValue
)
```

```text
Public Sub Setup4322 ( 
	physicalChannels As String,
	outputType As AOOutputType,
	outputValue As Double
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringThe physical channel(s) to calibrate.
- **outputType**
  - Type: NationalInstruments.DAQmxAOOutputTypeThe output type.
- **outputValue**
  - Type: SystemDoubleThe value for calibration.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9260.htm language=enus -->
## TOPIC 00107: ExternalCalibrationSessionSetup9260 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9260.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9260.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup9260 Method

### ExternalCalibrationSessionSetup9260 Method

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup9260(
	string physicalChannels,
	int value
)
```

```text
Public Sub Setup9260 ( 
	physicalChannels As String,
	value As Integer
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemString The physical channel(s) to calibrate.
- **value**
  - Type: SystemInt32 The reference value measured using a calibrator.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9266.htm language=enus -->
## TOPIC 00108: ExternalCalibrationSessionSetup9266 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9266.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setup9266.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.Setup9266 Method

### ExternalCalibrationSessionSetup9266 Method

Applies the specified DAC value to the AO channels, such that it can then be measured by a DMM

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Setup9266(
	string physicalChannels,
	int value
)
```

```text
Public Sub Setup9266 ( 
	physicalChannels As String,
	value As Integer
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemStringSpecifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels for devices installed in the system. You cannot specify more than one physical channel.
- **value**
  - Type: SystemInt32The binary number to write to the DAC.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setupdsa4480.htm language=enus -->
## TOPIC 00109: ExternalCalibrationSessionSetupDsa4480 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setupdsa4480.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_externalcalibrationsession_setupdsa4480.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.SetupDsa4480 Method

### ExternalCalibrationSessionSetupDsa4480 Method

Generates a specified voltage from the DSA device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void SetupDsa4480(
	string physicalChannels,
	CalibrationMode4480 calibrationMode
)
```

```text
Public Sub SetupDsa4480 ( 
	physicalChannels As String,
	calibrationMode As CalibrationMode4480
)
```

###### Parameters

- **physicalChannels**
  - Type: SystemString The physical channel(s) to calibrate.
- **calibrationMode**
  - Type: NationalInstruments.DAQmxCalibrationMode4480 The calibration mode for the device.

##### Remarks

calibration procedure for your device

| Note |
| --- |
| After you commit the calibration, you cannot undo it. If any calibration settings are incorrect, you must recalibrate the device. |

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_ifilteredtypedescriptor_getfilteredtypedescriptor_1.htm language=enus -->
## TOPIC 00110: IFilteredTypeDescriptorGetFilteredTypeDescriptor Method (PropertyFilterType, PropertyFilterFlags)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_ifilteredtypedescriptor_getfilteredtypedescriptor_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_ifilteredtypedescriptor_getfilteredtypedescriptor_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

IFilteredTypeDescriptor.GetFilteredTypeDescriptor Method (PropertyFilterType, PropertyFilterFlags)

### IFilteredTypeDescriptorGetFilteredTypeDescriptor Method (PropertyFilterType, PropertyFilterFlags)

Task

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
ICustomTypeDescriptor GetFilteredTypeDescriptor(
	PropertyFilterType filterType,
	PropertyFilterFlags filterFlags
)
```

```text
Function GetFilteredTypeDescriptor ( 
	filterType As PropertyFilterType,
	filterFlags As PropertyFilterFlags
) As ICustomTypeDescriptor
```

###### Parameters

- **filterType**
  - Type: NationalInstruments.DAQmxPropertyFilterTypeThe type of filtering to perform.
- **filterFlags**
  - Type: NationalInstruments.DAQmxPropertyFilterFlagsThe filtering options.

###### Return Value

ICustomTypeDescriptor

ICustomTypeDescriptor

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | An invalid enumeration value was passed as an argument to the function. |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Property filtering is a mechanism whereby you can programmatically retrieve a list of properties that are applicable to a specific task's subobject, based on the filtering type.

You can call the GetProperties method on the returned ICustomTypeDescriptor in order to access the list of properties as a PropertyDescriptorCollection. When GetProperties(Attribute) is called with an attribute array as a filter, the returned properties are filtered as if they all have the BrowsableAttribute set to .

##### See Also

###### Reference

IFilteredTypeDescriptor Interface

GetFilteredTypeDescriptor Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_linearscale__ctor.htm language=enus -->
## TOPIC 00111: LinearScale Constructor

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_linearscale__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_linearscale__ctor.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

LinearScale Constructor

### LinearScale Constructor

LinearScale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public LinearScale(
	string name,
	double slope,
	double yIntercept
)
```

```text
Public Sub New ( 
	name As String,
	slope As Double,
	yIntercept As Double
)
```

###### Parameters

- **name**
  - Type: SystemStringThe name of the custom scale for later use, such as when you create a virtual channel.
- **slope**
  - Type: SystemDoubleThe slope, m, in the equation.
- **yIntercept**
  - Type: SystemDoubleThe y-intercept, b, in the equation.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

The equation is identical for input and output. If the equation is in the form x = my + b, you must first solve for y in terms of x.

##### See Also

###### Reference

LinearScale Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_physicalchannel_configureteds.htm language=enus -->
## TOPIC 00112: PhysicalChannelConfigureTeds Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_physicalchannel_configureteds.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_physicalchannel_configureteds.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannel.ConfigureTeds Method

### PhysicalChannelConfigureTeds Method

TEDS

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureTeds()
```

```text
Public Sub ConfigureTeds
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This method temporarily overrides any TEDS configuration for the physical channel that you performed in Measurement Automation Explorer (MAX).

##### See Also

###### Reference

PhysicalChannel Class

ConfigureTeds Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_polynomialscale__ctor.htm language=enus -->
## TOPIC 00113: PolynomialScale Constructor (String, PolynomialDirection, Double, Double, Double)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_polynomialscale__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_polynomialscale__ctor.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PolynomialScale Constructor (String, PolynomialDirection, Double[], Double, Double)

### PolynomialScale Constructor (String, PolynomialDirection, Double, Double, Double)

PolynomialScale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public PolynomialScale(
	string name,
	PolynomialDirection direction,
	double[] coefficients,
	double rangeMinimum,
	double rangeMaximum
)
```

```text
Public Sub New ( 
	name As String,
	direction As PolynomialDirection,
	coefficients As Double(),
	rangeMinimum As Double,
	rangeMaximum As Double
)
```

###### Parameters

- **name**
  - Type: SystemString The name of the custom scale for later use, such as when you create a virtual channel.
- **direction**
  - Type: NationalInstruments.DAQmxPolynomialDirection The conversion direction of the specified polynomial. The opposite polynomial is computed by the PolynomialScale.
- **coefficients**
  - Type: SystemDouble The array of coefficients of a polynomial. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x3. This polynomial is used as either the forward or reverse polynomial depending on the direction specified.
- **rangeMinimum**
  - Type: SystemDouble The minimum of the range over which the polynomial specified is valid or of interest.
- **rangeMaximum**
  - Type: SystemDouble The maximum of the range over which the polynomial specified is valid or of interest.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

PolynomialScale Class

PolynomialScale Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_referencetrigger_configuredigitalpatterntrigger.htm language=enus -->
## TOPIC 00114: ReferenceTriggerConfigureDigitalPatternTrigger Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_referencetrigger_configuredigitalpatterntrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_referencetrigger_configuredigitalpatterntrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTrigger.ConfigureDigitalPatternTrigger Method

### ReferenceTriggerConfigureDigitalPatternTrigger Method

digital pattern

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureDigitalPatternTrigger(
	string source,
	string pattern,
	DigitalPatternReferenceTriggerCondition condition,
	long pretriggerSamples
)
```

```text
Public Sub ConfigureDigitalPatternTrigger ( 
	source As String,
	pattern As String,
	condition As DigitalPatternReferenceTriggerCondition,
	pretriggerSamples As Long
)
```

###### Parameters

- **source**
  - Type: SystemString The physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order.
- **pattern**
  - Type: SystemString The digital pattern that must be met for the trigger to occur.
- **condition**
  - Type: NationalInstruments.DAQmxDigitalPatternReferenceTriggerConditionThe condition under which the trigger occurs.
- **pretriggerSamples**
  - Type: SystemInt64The minimum number of samples to acquire per channel before recognizing the reference trigger.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

ConfigureDigitalPatternTrigger(String, String, DigitalPatternReferenceTriggerCondition, Int64)

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

ReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_referencetrigger_configurenone.htm language=enus -->
## TOPIC 00115: ReferenceTriggerConfigureNone Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_referencetrigger_configurenone.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_referencetrigger_configurenone.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTrigger.ConfigureNone Method

### ReferenceTriggerConfigureNone Method

reference triggering

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureNone()
```

```text
Public Sub ConfigureNone
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

ReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_savedtaskinfo_dispose.htm language=enus -->
## TOPIC 00116: SavedTaskInfoDispose Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_savedtaskinfo_dispose.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_savedtaskinfo_dispose.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SavedTaskInfo.Dispose Method

### SavedTaskInfoDispose Method

SavedTaskInfo

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Dispose()
```

```text
Public Sub Dispose
```

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

SavedTaskInfo Class

Dispose Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_scale_dispose_1.htm language=enus -->
## TOPIC 00117: ScaleDispose Method (Boolean)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_scale_dispose_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_scale_dispose_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Scale.Dispose Method (Boolean)

### ScaleDispose Method (Boolean)

Scale

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

Scale Class

Dispose Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_starttrigger_configuredigitaledgetrigger.htm language=enus -->
## TOPIC 00118: StartTriggerConfigureDigitalEdgeTrigger Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_starttrigger_configuredigitaledgetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_starttrigger_configuredigitaledgetrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

StartTrigger.ConfigureDigitalEdgeTrigger Method

### StartTriggerConfigureDigitalEdgeTrigger Method

rising or falling edge of a digital signal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureDigitalEdgeTrigger(
	string source,
	DigitalEdgeStartTriggerEdge edge
)
```

```text
Public Sub ConfigureDigitalEdgeTrigger ( 
	source As String,
	edge As DigitalEdgeStartTriggerEdge
)
```

###### Parameters

- **source**
  - Type: SystemString The name of a terminal where there is a digital signal to use as the source of the trigger.
- **edge**
  - Type: NationalInstruments.DAQmxDigitalEdgeStartTriggerEdge The edge of the digital signal to start acquiring or generating samples.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

ConfigureDigitalEdgeTrigger(String, DigitalEdgeStartTriggerEdge)

Task

Control(TaskAction)

Verify

##### See Also

###### Reference

StartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_switch_tostring.htm language=enus -->
## TOPIC 00119: SwitchToString Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_switch_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_switch_tostring.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Switch.ToString Method

### SwitchToString Method

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

Switch Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_tablescale__ctor.htm language=enus -->
## TOPIC 00120: TableScale Constructor

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_tablescale__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_tablescale__ctor.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

TableScale Constructor

### TableScale Constructor

TableScale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public TableScale(
	string name,
	double[] preScaledValues,
	double[] scaledValues
)
```

```text
Public Sub New ( 
	name As String,
	preScaledValues As Double(),
	scaledValues As Double()
)
```

###### Parameters

- **name**
  - Type: SystemStringThe name of the custom scale for later use, such as when you create a virtual channel.
- **preScaledValues**
  - Type: SystemDoubleAn array of prescaled values that map to the scaled values in scaledValues.
- **scaledValues**
  - Type: SystemDoubleAn array of scaled values that map to the prescaled values in prescaledValues.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

TableScale Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_control.htm language=enus -->
## TOPIC 00121: TaskControl Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_control.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_control.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Task.Control Method

### TaskControl Method

state

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Control(
	TaskAction mode
)
```

```text
Public Sub Control ( 
	mode As TaskAction
)
```

###### Parameters

- **mode**
  - Type: NationalInstruments.DAQmxTaskActionThe action to use to alter the state of the task.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

To start a task more quickly, set mode to [Commit](t_nationalinstruments_daqmx_taskaction.htm) to program the hardware with all parameters of the task prior to starting it.

If the task is in the running state and an asynchronous read or write on the task is in progress, calling Control(TaskAction) to move the task out of the running state does not return until the data from the pending read or write has been transferred to or from the task buffer. However, if mode is [Abort](t_nationalinstruments_daqmx_taskaction.htm), then Control(TaskAction) does not wait for the asynchronous read or write callback methods to finish. The pending asynchronous call stops immediately and raises a [DaqException](t_nationalinstruments_daqmx_daqexception.htm).

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_ondone.htm language=enus -->
## TOPIC 00122: TaskOnDone Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_ondone.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_ondone.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Task.OnDone Method

### TaskOnDone Method

Done

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void OnDone(
	TaskDoneEventArgs e
)
```

```text
Protected Overridable Sub OnDone ( 
	e As TaskDoneEventArgs
)
```

###### Parameters

- **e**
  - Type: NationalInstruments.DAQmxTaskDoneEventArgsA TaskDoneEventArgs that contains the event data.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_oneverynsamplesread.htm language=enus -->
## TOPIC 00123: TaskOnEveryNSamplesRead Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_oneverynsamplesread.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_oneverynsamplesread.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Task.OnEveryNSamplesRead Method

### TaskOnEveryNSamplesRead Method

EveryNSamplesRead

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void OnEveryNSamplesRead(
	EveryNSamplesReadEventArgs e
)
```

```text
Protected Overridable Sub OnEveryNSamplesRead ( 
	e As EveryNSamplesReadEventArgs
)
```

###### Parameters

- **e**
  - Type: NationalInstruments.DAQmxEveryNSamplesReadEventArgsAn EveryNSamplesReadEventArgs that contains the event data.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_onsampleclock.htm language=enus -->
## TOPIC 00124: TaskOnSampleClock Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_onsampleclock.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_onsampleclock.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Task.OnSampleClock Method

### TaskOnSampleClock Method

SampleClock

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
protected virtual void OnSampleClock(
	SampleClockEventArgs e
)
```

```text
Protected Overridable Sub OnSampleClock ( 
	e As SampleClockEventArgs
)
```

###### Parameters

- **e**
  - Type: NationalInstruments.DAQmxSampleClockEventArgsA SampleClockEventArgs that contains the event data.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_start.htm language=enus -->
## TOPIC 00125: TaskStart Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_start.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_start.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Task.Start Method

### TaskStart Method

state

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void Start()
```

```text
Public Sub Start
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

autoStart

When Should You Use the Start Function

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_tostring.htm language=enus -->
## TOPIC 00126: TaskToString Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_tostring.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Task.ToString Method

### TaskToString Method

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

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_waituntildone_1.htm language=enus -->
## TOPIC 00127: TaskWaitUntilDone Method (Int32)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_waituntildone_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_task_waituntildone_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Task.WaitUntilDone Method (Int32)

### TaskWaitUntilDone Method (Int32)

Waits for the measurement or generation to complete and returns if it has completed execution before the specified time elapses.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void WaitUntilDone(
	int millisecToWait
)
```

```text
Public Sub WaitUntilDone ( 
	millisecToWait As Integer
)
```

###### Parameters

- **millisecToWait**
  - Type: SystemInt32The maximum amount of time in milliseconds to wait for the measurement or generation to complete. This method returns an error if the time elapses. If you set the timeout to -1, the method always waits for the task to complete, regardless of the amount of time needed.

###### Return Value

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

WaitUntilDone(Int32)

Timing

WaitUntilDone(Int32)

IAsyncResult

##### See Also

###### Reference

Task Class

WaitUntilDone Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_taskdoneeventargs_checkforexception.htm language=enus -->
## TOPIC 00128: TaskDoneEventArgsCheckForException Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_taskdoneeventargs_checkforexception.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_taskdoneeventargs_checkforexception.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

TaskDoneEventArgs.CheckForException Method

### TaskDoneEventArgsCheckForException Method

Exception

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void CheckForException()
```

```text
Public Sub CheckForException
```

##### Remarks

Exception

Error

##### See Also

###### Reference

TaskDoneEventArgs Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_timing_configurechangedetection.htm language=enus -->
## TOPIC 00129: TimingConfigureChangeDetection Method (String, String, SampleQuantityMode)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_timing_configurechangedetection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_timing_configurechangedetection.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.ConfigureChangeDetection Method (String, String, SampleQuantityMode)

### TimingConfigureChangeDetection Method (String, String, SampleQuantityMode)

Configures the task to acquire samples on the rising and/or falling edges of the specified lines or ports.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureChangeDetection(
	string diRisingEdgePhysicalChannels,
	string diFallingEdgePhysicalChannels,
	SampleQuantityMode sampleMode
)
```

```text
Public Sub ConfigureChangeDetection ( 
	diRisingEdgePhysicalChannels As String,
	diFallingEdgePhysicalChannels As String,
	sampleMode As SampleQuantityMode
)
```

###### Parameters

- **diRisingEdgePhysicalChannels**
  - Type: SystemStringThe names of the digital lines or ports on which to detect rising edges. The lines or ports must be contained in the task. You can specify a string that defines a list or range of channels for this parameter.
- **diFallingEdgePhysicalChannels**
  - Type: SystemStringThe names of the digital lines or ports on which to detect falling edges. The lines or ports must be contained in the task. You can specify a string that defines a list or range of channels for this parameter.
- **sampleMode**
  - Type: NationalInstruments.DAQmxSampleQuantityModeThe duration of the task. A task is either finite and stops when the specified number of samples have been acquired, or it is continuous and continues to acquire samples until the task is explicitly stopped.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Use this method to configure a task to continuously acquire samples using [change detection timing](/csh?topicname=mxcncpts/;).

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. [ConfigureSampleClock](overload_nationalinstruments_daqmx_timing_configuresampleclock.htm) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task. You start the task with [Start](m_nationalinstruments_daqmx_task_start.htm), by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

You cannot apply this method to a subset of devices in the task, and you must apply this method to the task as a whole. You must call this method on the instance of [Timing](t_nationalinstruments_daqmx_timing.htm) returned from the [Timing](p_nationalinstruments_daqmx_task_timing.htm) property on the [Task](t_nationalinstruments_daqmx_task.htm) class. Accessing this method on instances of [Timing](t_nationalinstruments_daqmx_timing.htm) returned from the [ItemString](p_nationalinstruments_daqmx_timing_item.htm) property throws an exception.

##### See Also

###### Reference

Timing Class

ConfigureChangeDetection Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_timing_configurehandshaking_1.htm language=enus -->
## TOPIC 00130: TimingConfigureHandshaking Method (SampleQuantityMode, Int32)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_timing_configurehandshaking_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/m_nationalinstruments_daqmx_timing_configurehandshaking_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.ConfigureHandshaking Method (SampleQuantityMode, Int32)

### TimingConfigureHandshaking Method (SampleQuantityMode, Int32)

digital handshaking

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureHandshaking(
	SampleQuantityMode sampleMode,
	int samplesPerChannel
)
```

```text
Public Sub ConfigureHandshaking ( 
	sampleMode As SampleQuantityMode,
	samplesPerChannel As Integer
)
```

###### Parameters

- **sampleMode**
  - Type: NationalInstruments.DAQmxSampleQuantityModeThe duration of the task. A task is either finite and stops once the specified number of samples has been acquired or generated, or it is continuous and continues to acquire or generate samples until the task is explicitly stopped.
- **samplesPerChannel**
  - Type: SystemInt32The number of samples to acquire or generate for each channel in the task if sampleMode is FiniteSamples. If sampleMode is ContinuousSamples, NI-DAQmx uses this value to determine the buffer size.

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Use this method if the task requires a finite number of samples. These [devices](/csh?topicname=mxdevconsid/;) support handshake timing.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](t_nationalinstruments_daqmx_task.htm) are valid, you must verify the task by starting the task, either with [Start](m_nationalinstruments_daqmx_task_start.htm) or by reading from or writing to the task, or by calling [Control(TaskAction)](m_nationalinstruments_daqmx_task_control.htm) with [Verify](t_nationalinstruments_daqmx_taskaction.htm).

You cannot apply this method to a subset of devices in the task, and you must apply this method to the task as a whole. You must call this method on the instance of [Timing](t_nationalinstruments_daqmx_timing.htm) returned from the [Timing](p_nationalinstruments_daqmx_task_timing.htm) property on the [Task](t_nationalinstruments_daqmx_task.htm) class. Accessing this method on instances of [Timing](t_nationalinstruments_daqmx_timing.htm) returned from the [ItemString](p_nationalinstruments_daqmx_timing_item.htm) property throws an exception.

##### See Also

###### Reference

Timing Class

ConfigureHandshaking Overload

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_advancetrigger.htm language=enus -->
## TOPIC 00131: AdvanceTrigger Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_advancetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_advancetrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AdvanceTrigger Methods

### AdvanceTrigger Methods

The [AdvanceTrigger](t_nationalinstruments_daqmx_advancetrigger.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureDigitalEdgeTrigger | Configures a task to advance to the next entry in a scan list upon a rising or falling edge of a digital signal. |
|  | ConfigureNone | Disables advance triggering for the task. |
|  | ConfigureSoftwareTrigger | Configures a task to advance to the next entry in a scan list upon a software trigger. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | SendSoftwareTrigger | Sends a notification to the hardware from the running program to advance to the next entry in the switch scan list. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

AdvanceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_aichannel.htm language=enus -->
## TOPIC 00132: AIChannel Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_aichannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_aichannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel Methods

### AIChannel Methods

The [AIChannel](t_nationalinstruments_daqmx_aichannel.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by Channel. (Inherited from Channel.) |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by Channel or optionally releases only the unmanaged resources. (Inherited from Channel.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | PerformBridgeOffsetNullingCalibration | Performs a bridge offset nulling calibration on the virtual channels in the task. An error will occur if not all virtual channels in the task support this operation. |
|  | PerformBridgeOffsetNullingCalibration(Boolean) | Performs a bridge offset nulling calibration on the virtual channels in the task. |
|  | PerformBridgeShuntCalibration(Double, ShuntElementLocation, Double) | Performs shunt calibration for the virtual channels in the task using a bridge sensor. An error will occur if not all virtual channels in the task support this operation. |
|  | PerformBridgeShuntCalibration(Double, ShuntElementLocation, Double, Boolean) | Performs shunt calibration for the virtual channels in the task using a bridge sensor. |
|  | PerformBridgeShuntCalibration(Double, ShuntElementLocation, Double, ShuntCalibrationSelect, ShuntResistorSource) | Performs shunt calibration for the specified channels using a bridge sensor. |
|  | PerformBridgeShuntCalibration(Double, ShuntElementLocation, Double, ShuntCalibrationSelect, ShuntResistorSource, Boolean) | Performs shunt calibration for the specified channels using a bridge sensor. |
|  | PerformStrainShuntCalibration(Double, ShuntElementLocation) | Performs shunt calibration for the virtual channels in the task using a strain gage sensor. An error will occur if not all virtual channels in the task support this operation. |
|  | PerformStrainShuntCalibration(Double, ShuntElementLocation, Boolean) | Performs shunt calibration for the virtual channels in the task using a strain gage sensor. |
|  | PerformStrainShuntCalibration(Double, ShuntElementLocation, ShuntCalibrationSelect, ShuntResistorSource) | Performs shunt calibration for the specified channels using a strain gage sensor. |
|  | PerformStrainShuntCalibration(Double, ShuntElementLocation, ShuntCalibrationSelect, ShuntResistorSource, Boolean) | Performs shunt calibration for the specified channels using a strain gage sensor. |
|  | PerformThermocoupleLeadOffsetNullingCalibration | Performs thermocouple lead offset nulling calibration on the channels in the task to compensate for offsets introduced by open thermocouple detection. An error will occur if not all virtual channels in the task support this operation. |
|  | PerformThermocoupleLeadOffsetNullingCalibration(Boolean) | Performs thermocouple lead offset nulling calibration on the channels in the task to compensate for offsets introduced by open thermocouple detection. Use this method to specify whether or not to skip channels that do not support calibration. |
|  | ToString | Returns a string representation of the object. (Inherited from Channel.) |

Top

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_aichannelcollection.htm language=enus -->
## TOPIC 00133: AIChannelCollection Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_aichannelcollection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_aichannelcollection.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection Methods

### AIChannelCollection Methods

The [AIChannelCollection](t_nationalinstruments_daqmx_aichannelcollection.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateAccelerationChargeChannel(String, String, AITerminalConfiguration, Double, Double, AIAccelerationUnits, Double, AIAccelerationChargeSensitivityUnits) | Creates channel(s) that use an accelerometer to measure acceleration and adds the channel(s) to the task you specify with taskHandle. |
|  | CreateAccelerationChargeChannel(String, String, AITerminalConfiguration, Double, Double, String, Double, AIAccelerationChargeSensitivityUnits) | Creates channel(s) that use an accelerometer to measure acceleration and adds the channel(s) to the task you specify with taskHandle. |
|  | CreateAccelerationFourWireDCVoltageChannel(String, String, AITerminalConfiguration, Double, Double, AIAccelerationUnits, Double, AIAccelerationFourWireDCVoltageSensitivityUnits, AIExcitationSource, Double, Boolean) | Creates an AIChannel that measures acceleration using a 4-wire, DC voltage-based sensor connected to the channel. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateAccelerationFourWireDCVoltageChannel(String, String, AITerminalConfiguration, Double, Double, String, Double, AIAccelerationFourWireDCVoltageSensitivityUnits, AIExcitationSource, Double, Boolean) | Creates an AIChannel that specifies the sensitivity of the 4-wire, DC voltage-based sensor connected to the channel. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateAccelerometerChannel(String, String, AITerminalConfiguration, Double, Double, Double, AIAccelerometerSensitivityUnits, AIExcitationSource, Double, AIAccelerationUnits) | Creates an AIChannel that uses an accelerometer to measure acceleration. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateAccelerometerChannel(String, String, AITerminalConfiguration, Double, Double, Double, AIAccelerometerSensitivityUnits, AIExcitationSource, Double, String) | Creates an AIChannel with the specified custom scale that uses an accelerometer to measure acceleration. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateBridgeChannel(String, String, Double, Double, AIBridgeUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double) | Creates an AIChannel that measures voltage ratios from a Wheatstone bridge. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the AIChannelCollection. Use a custom scale or other scaling code to convert the voltage ratios to physical units. |
|  | CreateBridgeChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double) | Creates an AIChannel that measures voltage ratios from a Wheatstone bridge, with the specified custom scale. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the AIChannelCollection. Use a custom scale or other scaling code to convert the voltage ratios to physical units. |
|  | CreateBuiltInSensorTemperatureChannel | Creates an AIChannel to measure temperature with a built-in sensor of a terminal block or device. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateChargeChannel(String, String, AITerminalConfiguration, Double, Double, AIChargeUnits) | Creates an AIChannel to measure acceleration using a charge-based sensor. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateChargeChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel to measure acceleration using a charge-based sensor. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentChannel(String, String, AITerminalConfiguration, Double, Double, AICurrentUnits) | Creates an AIChannel with an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel with the specified custom scale and an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentChannel(String, String, AITerminalConfiguration, Double, Double, Double, AICurrentUnits) | Creates an AIChannel with the specified external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentChannel(String, String, AITerminalConfiguration, Double, Double, Double, String) | Creates an AIChannel with the specified custom scale and external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentChannel(String, String, AITerminalConfiguration, Double, Double, AICurrentUnits, AICurrentShuntLocation, Double, String) | Creates an AIChannel with the specified custom scale and external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentRmsChannel(String, String, AITerminalConfiguration, Double, Double, AICurrentAcrmsUnits) | Creates an AIChannel with an internal shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentRmsChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel with the specified custom scale and an internal shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentRmsChannel(String, String, AITerminalConfiguration, Double, Double, Double, AICurrentAcrmsUnits) | Creates an AIChannel with the specified external shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentRmsChannel(String, String, AITerminalConfiguration, Double, Double, Double, String) | Creates an AIChannel with the specified custom scale and external shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateDeviceTemperatureChannel | Obsolete. Creates an AIChannel to measure temperature with a built-in sensor of a terminal block or device. This method adds one or more physical channels to the AIChannelCollection. The CreateDeviceTemperatureChannel(String, String, AITemperatureUnits) method has been deprecated in favor of the CreateBuiltInSensorTemperatureChannel(String, String, AITemperatureUnits) method. |
|  | CreateEddyCurrentProximityProbeChannel(String, String, Double, Double, Double, AIEddyCurrentProximityProbeSensitivityUnits, AIEddyCurrentProximityProbeUnits) | Creates an AIChannel that uses an Eddy Current Proximity Probe to measure position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateEddyCurrentProximityProbeChannel(String, String, Double, Double, Double, AIEddyCurrentProximityProbeSensitivityUnits, String) | Creates an AIChannel with the specified custom scale that uses an Eddy Current Proximity Probe to measure position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceBridgePolynomialChannel(String, String, Double, Double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceBridgePolynomialChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceBridgeTableChannel(String, String, Double, Double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, AIBridgeElectricalUnits, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceBridgeTableChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, AIBridgeElectricalUnits, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceBridgeTwoPointLinearChannel(String, String, Double, Double, AIForceUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceBridgeTwoPointLinearChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceIepeChannel(String, String, AITerminalConfiguration, Double, Double, AIForceUnits, Double, AIForceIepeSensorSensitivityUnits, AIExcitationSource, Double) | Creates an AIChannel that uses an IEPE force sensor to measure force or load. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateForceIepeChannel(String, String, AITerminalConfiguration, Double, Double, String, Double, AIForceIepeSensorSensitivityUnits, AIExcitationSource, Double) | Creates an AIChannel that uses an IEPE force sensor to measure force or load, with the specified custom scale. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateFrequencyVoltageChannel(String, String, Double, Double, Double, Double, AIFrequencyUnits) | Creates an AIChannel to measure frequency using a frequency-to-voltage converter. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateFrequencyVoltageChannel(String, String, Double, Double, Double, Double, String) | Creates an AIChannel with the specified custom scale to measure frequency using a frequency-to-voltage converter. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateLvdtChannel(String, String, Double, Double, Double, AILvdtSensitivityUnits, AIExcitationSource, Double, Double, AIACExcitationWireMode, AILvdtUnits) | Creates an AIChannel that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateLvdtChannel(String, String, Double, Double, Double, AILvdtSensitivityUnits, AIExcitationSource, Double, Double, AIACExcitationWireMode, String) | Creates an AIChannel with the specified custom scale that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateMicrophoneChannel(String, String, Double, Double, AITerminalConfiguration, AIExcitationSource, Double, AISoundPressureUnits) | Creates an AIChannel that uses a microphone to measure sound pressure. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateMicrophoneChannel(String, String, Double, Double, AITerminalConfiguration, AIExcitationSource, Double, String) | Creates an AIChannel with the specified custom scale that uses a microphone to measure sound pressure. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | CreatePressureBridgePolynomialChannel(String, String, Double, Double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreatePressureBridgePolynomialChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreatePressureBridgeTableChannel(String, String, Double, Double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, AIBridgeElectricalUnits, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreatePressureBridgeTableChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, AIBridgeElectricalUnits, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreatePressureBridgeTwoPointLinearChannel(String, String, Double, Double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreatePressureBridgeTwoPointLinearChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateResistanceChannel(String, String, Double, Double, AIResistanceConfiguration, AIExcitationSource, Double, AIResistanceUnits) | Creates an AIChannel to measure resistance. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateResistanceChannel(String, String, Double, Double, AIResistanceConfiguration, AIExcitationSource, Double, String) | Creates an AIChannel with the specified custom scale to measure resistance. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateRosetteStrainGageChannel | Creates an AIChannel to measure two-dimensional strain using a rosette strain gage. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateRtdChannel | Creates an AIChannel that uses an RTD to measure temperature. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateRvdtChannel(String, String, Double, Double, Double, AIRvdtSensitivityUnits, AIExcitationSource, Double, Double, AIACExcitationWireMode, AIRvdtUnits) | Creates an AIChannel that uses an RVDT to measure angular position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateRvdtChannel(String, String, Double, Double, Double, AIRvdtSensitivityUnits, AIExcitationSource, Double, Double, AIACExcitationWireMode, String) | Creates an AIChannel with the specified custom scale that uses an RVDT to measure angular position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateStrainGageChannel(String, String, Double, Double, AIStrainGageConfiguration, AIExcitationSource, Double, Double, Double, Double, Double, Double, AIStrainUnits) | Creates an AIChannel to measure strain. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateStrainGageChannel(String, String, Double, Double, AIStrainGageConfiguration, AIExcitationSource, Double, Double, Double, Double, Double, Double, String) | Creates an AIChannel with the specified custom scale to measure strain. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsAccelerometerChannel(String, String, Double, Double, AIExcitationSource, Double, AIAccelerationUnits) | Creates an AIChannel that uses an accelerometer to measure acceleration. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsAccelerometerChannel(String, String, Double, Double, AIExcitationSource, Double, String) | Creates an AIChannel with the specified custom scale that uses an accelerometer to measure acceleration. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsBridgeChannel(String, String, Double, Double, AIBridgeUnits, AIExcitationSource, Double) | Creates an AIChannel that measures a a Wheatstone bridge. You must configure the physical channel(s) with TEDS information to use this method. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsBridgeChannel(String, String, Double, Double, String, AIExcitationSource, Double) | Creates an AIChannel that measures a a Wheatstone bridge, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. Use this instance with bridge-based sensors that measure phenomena other than strain, force, pressure, or torque, or that scale data to physical units NI-DAQmx does not support. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsCurrentChannel(String, String, AITerminalConfiguration, Double, Double, AICurrentUnits) | Creates an AIChannel with an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsCurrentChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel with the specified custom scale and an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsCurrentChannel(String, String, AITerminalConfiguration, Double, Double, Double, AICurrentUnits) | Creates an AIChannel with the specified external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsCurrentChannel(String, String, AITerminalConfiguration, Double, Double, Double, String) | Creates an AIChannel with the specified custom scale and external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsForceBridgeChannel(String, String, Double, Double, AIForceUnits, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsForceBridgeChannel(String, String, Double, Double, String, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsForceIepeChannel(String, String, AITerminalConfiguration, Double, Double, AIForceUnits, AIExcitationSource, Double) | Creates an AIChannel that uses an IEPE force sensor to measure force or load. You must configure the physical channel(s) with TEDS information to use this method. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsForceIepeChannel(String, String, AITerminalConfiguration, Double, Double, String, AIExcitationSource, Double) | Creates an AIChannel that uses an IEPE force sensor to measure force or load, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsLvdtChannel(String, String, Double, Double, AIExcitationSource, Double, Double, AIACExcitationWireMode, AILvdtUnits) | Creates an AIChannel that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsLvdtChannel(String, String, Double, Double, AIExcitationSource, Double, Double, AIACExcitationWireMode, String) | Creates an AIChannel with the specified custom scale that uses an LVDT to measure linear position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsMicrophoneChannel(String, String, Double, AITerminalConfiguration, AIExcitationSource, Double, AISoundPressureUnits) | Creates an AIChannel that uses a microphone to measure sound pressure. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsMicrophoneChannel(String, String, Double, AITerminalConfiguration, AIExcitationSource, Double, String) | Creates an AIChannel with the specified custom scale that uses a microphone to measure sound pressure. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsPressureBridgeChannel(String, String, Double, Double, AIPressureUnits, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. You must configure the physical channel(s) with TEDS information to use this method. |
|  | CreateTedsPressureBridgeChannel(String, String, Double, Double, String, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. You must configure the physical channel(s) with TEDS information to use this method. |
|  | CreateTedsResistanceChannel(String, String, Double, Double, AIResistanceConfiguration, AIExcitationSource, Double, AIResistanceUnits) | Creates an AIChannel to measure resistance. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsResistanceChannel(String, String, Double, Double, AIResistanceConfiguration, AIExcitationSource, Double, String) | Creates an AIChannel with the specified custom scale to measure resistance. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsRtdChannel | Creates an AIChannel that uses an RTD to measure temperature. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsRvdtChannel(String, String, Double, Double, AIExcitationSource, Double, Double, AIACExcitationWireMode, AIRvdtUnits) | Creates an AIChannel that uses an RVDT to measure angular position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsRvdtChannel(String, String, Double, Double, AIExcitationSource, Double, Double, AIACExcitationWireMode, String) | Creates an AIChannel that uses an RVDT to measure angular position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsStrainGageChannel(String, String, Double, Double, AIExcitationSource, Double, Double, Double, AIStrainUnits) | Creates an AIChannel to measure strain. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsStrainGageChannel(String, String, Double, Double, AIExcitationSource, Double, Double, Double, String) | Creates an AIChannel with the specified custom scale to measure strain. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsThermistorIExChannel | Creates an AIChannel that uses a thermistor to measure temperature. Use this method when the thermistor uses current excitation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsThermistorVExChannel | Creates an AIChannel that uses a thermistor to measure temperature. Use this method when the thermistor uses voltage excitation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsThermocoupleChannel(String, String, Double, Double, AITemperatureUnits) | Creates an AIChannel that uses a thermocouple to measure temperature using a built-in cold-junction compensation source. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsThermocoupleChannel(String, String, Double, Double, AITemperatureUnits, Double) | Creates an AIChannel that uses a thermocouple to measure temperature using a constant value cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsThermocoupleChannel(String, String, Double, Double, AITemperatureUnits, String) | Creates an AIChannel that uses a thermocouple to measure temperature using a measurement on another channel for cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsTorqueBridgeChannel(String, String, Double, Double, AITorqueUnits, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure torque. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsTorqueBridgeChannel(String, String, Double, Double, String, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsVoltageChannel(String, String, AITerminalConfiguration, Double, Double, AIVoltageUnits) | Creates an AIChannel to measure voltage. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsVoltageChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel with the specified custom scale to measure voltage. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsVoltageChannelWithExcitation(String, String, AITerminalConfiguration, Double, Double, AIExcitationSource, Double, AIVoltageUnits) | Creates an AIChannel to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsVoltageChannelWithExcitation(String, String, AITerminalConfiguration, Double, Double, AIExcitationSource, Double, String) | Creates an AIChannel with the specified custom scale to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateThermistorIExChannel | Creates an AIChannel that uses a thermistor to measure temperature. Use this method when the thermistor uses current excitation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateThermistorVExChannel | Creates an AIChannel that uses a thermistor to measure temperature. Use this method when the thermistor uses voltage excitation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateThermocoupleChannel(String, String, Double, Double, AIThermocoupleType, AITemperatureUnits) | Creates an AIChannel that uses a thermocouple to measure temperature using a built-in cold-junction compensation source. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateThermocoupleChannel(String, String, Double, Double, AIThermocoupleType, AITemperatureUnits, Double) | Creates an AIChannel that uses a thermocouple to measure temperature using a constant value cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateThermocoupleChannel(String, String, Double, Double, AIThermocoupleType, AITemperatureUnits, String) | Creates an AIChannel that uses a thermocouple to measure temperature using a measurement on another channel for cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTorqueBridgePolynomialChannel(String, String, Double, Double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTorqueBridgePolynomialChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications provide a polynomial to convert electrical values to physical values. When you use this scaling type, NI-DAQmx requires coefficients for a polynomial that converts electrical values to physical values (forward), as well as coefficients for a polynomial that converts physical values to electrical values (reverse). If you only know one set of coefficients, use PolynomialScale to generate the other set. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTorqueBridgeTableChannel(String, String, Double, Double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, AIBridgeElectricalUnits, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTorqueBridgeTableChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, AIBridgeElectricalUnits, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications provide a table of electrical values and the corresponding physical values. When you use this scaling type, NI-DAQmx performs linear scaling between each pair of electrical and physical values. The input limits specified with the minimum value and maximum value parameters must fall within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTorqueBridgeTwoPointLinearChannel(String, String, Double, Double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTorqueBridgeTwoPointLinearChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVelocityIepeChannel(String, String, AITerminalConfiguration, Double, Double, AIVelocityUnits, Double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, Double) | Creates an AIChannel that uses an IEPE velocity sensor to measure velocity. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVelocityIepeChannel(String, String, AITerminalConfiguration, Double, Double, String, Double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, Double) | Creates an AIChannel that uses an IEPE velocity sensor to measure velocity. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVoltageChannel(String, String, AITerminalConfiguration, Double, Double, AIVoltageUnits) | Creates an AIChannel to measure voltage. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVoltageChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel with the specified custom scale to measure voltage. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVoltageChannelWithExcitation(String, String, AITerminalConfiguration, Double, Double, AIBridgeConfiguration, AIExcitationSource, Double, Boolean, AIVoltageUnits) | Creates an AIChannel to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVoltageChannelWithExcitation(String, String, AITerminalConfiguration, Double, Double, AIBridgeConfiguration, AIExcitationSource, Double, Boolean, String) | Creates an AIChannel with the specified custom scale to measure voltage for custom sensors that require excitation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVoltageRmsChannel(String, String, AITerminalConfiguration, Double, Double, AIVoltageAcrmsUnits) | Creates an AIChannel to measure AC voltage. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVoltageRmsChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel with the specified custom scale to measure AC voltage. This method adds one or more physical channels to the AIChannelCollection. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetEnumerator | Returns an enumerator that you can use to iterate through the collection. |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_analogedgereferencetrigger.htm language=enus -->
## TOPIC 00134: AnalogEdgeReferenceTrigger Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_analogedgereferencetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_analogedgereferencetrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeReferenceTrigger Methods

### AnalogEdgeReferenceTrigger Methods

The [AnalogEdgeReferenceTrigger](t_nationalinstruments_daqmx_analogedgereferencetrigger.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

AnalogEdgeReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_analogmultichannelreader.htm language=enus -->
## TOPIC 00135: AnalogMultiChannelReader Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_analogmultichannelreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_analogmultichannelreader.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelReader Methods

### AnalogMultiChannelReader Methods

The [AnalogMultiChannelReader](t_nationalinstruments_daqmx_analogmultichannelreader.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginMemoryOptimizedReadMultiSample(Int32, AsyncCallback, Object, Double) | Begins an asynchronous read of one or more floating-point samples from one or more AIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSample(Int32, AsyncCallback, Object, Double, ReallocationPolicy) | Begins an asynchronous read of one or more floating-point samples from one or more AIChannel objects in a task. |
|  | BeginMemoryOptimizedReadWaveform(Int32, AsyncCallback, Object, AnalogWaveformDouble) | Begins an asynchronous read of one or more analog waveform samples from one or more AIChannel objects in a task. |
|  | BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, Object, AnalogWaveformDouble) | Begins an asynchronous, memory-optimized read of one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration. |
|  | BeginMemoryOptimizedReadWaveform(Int32, AsyncCallback, Object, AnalogWaveformDouble, ReallocationPolicy) | Begins an asynchronous read of one or more analog waveform samples from one or more AIChannel objects in a task. |
|  | BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, Object, AnalogWaveformDouble, ReallocationPolicy) | Begins an asynchronous, memory-optimized read of one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration. |
|  | BeginReadMultiSample | Begins an asynchronous read of one or more floating-point samples from one or more AIChannel objects in a task. |
|  | BeginReadSingleSample | Begins an asynchronous read of a single floating-point sample from one or more AIChannel objects in a task. |
|  | BeginReadWaveform(Int32, AsyncCallback, Object) | Begins an asynchronous read of one or more analog waveform samples from one or more AIChannel objects in a task. |
|  | BeginReadWaveform(TimeSpan, AsyncCallback, Object) | Begins an asynchronous read of one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndMemoryOptimizedReadMultiSample | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSample(Int32, AsyncCallback, Object, Double) and retrieves the read samples. |
|  | EndMemoryOptimizedReadWaveform | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadWaveform(Int32, AsyncCallback, Object, AnalogWaveformDouble) and retrieves the read samples. |
|  | EndReadMultiSample | Handles the end of an asynchronous read initiated with BeginReadMultiSample(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSample | Handles the end of an asynchronous read initiated with BeginReadSingleSample(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadWaveform | Handles the end of an asynchronous read initiated with BeginReadWaveform(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | MemoryOptimizedReadMultiSample(Int32, Double, Int32) | Reads one or more floating-point samples from one or more AIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSample(Int32, Double, ReallocationPolicy, Int32) | Reads one or more floating-point samples from one or more AIChannel objects in a task. |
|  | MemoryOptimizedReadWaveform(Int32, AnalogWaveformDouble) | Reads one or more analog waveform samples from one or more AIChannel objects in a task. |
|  | MemoryOptimizedReadWaveform(TimeSpan, AnalogWaveformDouble) | Performs a memory-optimized read of one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration. |
|  | MemoryOptimizedReadWaveform(Int32, AnalogWaveformDouble, ReallocationPolicy) | Reads one or more analog waveform samples from one or more AIChannel objects in a task. |
|  | MemoryOptimizedReadWaveform(TimeSpan, AnalogWaveformDouble, ReallocationPolicy) | Performs a memory-optimized read of one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration. |
|  | ReadMultiSample | Reads one or more floating-point samples from one or more AIChannel objects in a task. |
|  | ReadSingleSample | Reads a single floating-point sample from one or more AIChannel objects in a task. |
|  | ReadWaveform(Int32) | Reads one or more analog waveform samples from one or more AIChannel objects in a task. |
|  | ReadWaveform(TimeSpan) | Reads one or more analog waveform samples from one or more AIChannel objects in a task for a specified duration. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

AnalogMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_analogmultichannelwriter.htm language=enus -->
## TOPIC 00136: AnalogMultiChannelWriter Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_analogmultichannelwriter.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_analogmultichannelwriter.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelWriter Methods

### AnalogMultiChannelWriter Methods

The [AnalogMultiChannelWriter](t_nationalinstruments_daqmx_analogmultichannelwriter.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginWriteMultiSample | Begins an asynchronous write of one or more floating-point samples to one or more AOChannel objects in a task. |
|  | BeginWriteSingleSample | Begins an asynchronous write of a single floating-point sample to one or more AOChannel objects in a task. |
|  | BeginWriteWaveformTData | Begins an asynchronous write of one or more analog waveform samples to one or more AOChannel objects in a task. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndWrite | Handles the end of an asynchronous write initiated with BeginWriteMultiSample(Boolean, Double, AsyncCallback, Object) or BeginWriteSingleSample(Boolean, Double, AsyncCallback, Object). |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |
|  | WriteMultiSample | Writes one or more floating-point samples to one or more AOChannel objects in a task. |
|  | WriteSingleSample | Writes a single floating-point sample to one or more AOChannel objects in a task. |
|  | WriteWaveformTData | Writes one or more analog waveform samples to one or more AOChannel objects in a task. |

Top

##### See Also

###### Reference

AnalogMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_analogwindowreferencetrigger.htm language=enus -->
## TOPIC 00137: AnalogWindowReferenceTrigger Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_analogwindowreferencetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_analogwindowreferencetrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogWindowReferenceTrigger Methods

### AnalogWindowReferenceTrigger Methods

The [AnalogWindowReferenceTrigger](t_nationalinstruments_daqmx_analogwindowreferencetrigger.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

AnalogWindowReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_analogwindowstarttrigger.htm language=enus -->
## TOPIC 00138: AnalogWindowStartTrigger Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_analogwindowstarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_analogwindowstarttrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogWindowStartTrigger Methods

### AnalogWindowStartTrigger Methods

The [AnalogWindowStartTrigger](t_nationalinstruments_daqmx_analogwindowstarttrigger.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

AnalogWindowStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_cochannelcollection.htm language=enus -->
## TOPIC 00139: COChannelCollection Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_cochannelcollection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_cochannelcollection.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

COChannelCollection Methods

### COChannelCollection Methods

The [COChannelCollection](t_nationalinstruments_daqmx_cochannelcollection.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | CreatePulseChannelFrequency | Creates a COChannel to generate digital pulses defined by frequency and duty cycle. This method adds one or more channels to the COChannelCollection. |
|  | CreatePulseChannelTicks | Creates a COChannel to generate digital pulses defined by the number of timebase ticks that the pulse is at the high and low states. This method adds one or more channels to the COChannelCollection. |
|  | CreatePulseChannelTime | Creates a COChannel to generate digital pulses defined by the amount of time that the pulse is at the high and low states. This method adds one or more channels to the COChannelCollection. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetEnumerator | Returns an enumerator that you can use to iterate through the collection. |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

COChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_codatafrequency.htm language=enus -->
## TOPIC 00140: CODataFrequency Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_codatafrequency.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_codatafrequency.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CODataFrequency Methods

### CODataFrequency Methods

The [CODataFrequency](t_nationalinstruments_daqmx_codatafrequency.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals(Object) | Returns a value indicating if this instance is equal to the specified object. (Overrides ValueTypeEquals(Object).) |
|  | Equals(CODataFrequency) | Returns a value indicating if this instance is equal to the specified CODataFrequency object. |
|  | Equals(CODataFrequency, CODataFrequency) | Returns a value indicating if two specified instances of CODataFrequency are equal. |
|  | GetHashCode | Returns a hash code for the CODataFrequency object. (Overrides ValueTypeGetHashCode.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns the fully qualified type name of this instance. (Inherited from ValueType.) |

Top

##### See Also

###### Reference

CODataFrequency Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_countermultichannelreader.htm language=enus -->
## TOPIC 00141: CounterMultiChannelReader Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_countermultichannelreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_countermultichannelreader.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader Methods

### CounterMultiChannelReader Methods

The [CounterMultiChannelReader](t_nationalinstruments_daqmx_countermultichannelreader.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double) | Begins an asynchronous read of one or more Double samples from one or more CIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double, ReallocationPolicy) | Begins an asynchronous read of one or more Double samples from one or more CIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32) | Begins an asynchronous read of one or more Int32 samples from one or more CIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32, ReallocationPolicy) | Begins an asynchronous read of one or more Int32 samples from one or more CIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32) | Begins an asynchronous read of one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32, ReallocationPolicy) | Begins an asynchronous read of one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | BeginReadMultiSampleDouble | Begins an asynchronous read of one or more Double samples from one or more CIChannel objects in a task. |
|  | BeginReadMultiSampleInt32 | Begins an asynchronous read of one or more Int32 samples from one or more CIChannel objects in a task. |
|  | BeginReadMultiSampleUInt32 | Begins an asynchronous read of one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | BeginReadSingleSampleDouble | Begins an asynchronous read of a single Double sample from one or more CIChannel objects in a task. |
|  | BeginReadSingleSampleInt32 | Begins an asynchronous read of a single Int32 sample from one or more CIChannel objects in a task. |
|  | BeginReadSingleSampleUInt32 | Begins an asynchronous read of a single UInt32 sample from one or more CIChannel objects in a task. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndMemoryOptimizedReadMultiSampleDouble | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSampleInt32 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSampleUInt32 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32) and retrieves the read samples. |
|  | EndReadMultiSampleDouble | Handles the end of an asynchronous read initiated with BeginReadMultiSampleDouble(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSampleInt32 | Handles the end of an asynchronous read initiated with BeginReadMultiSampleInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSampleUInt32 | Handles the end of an asynchronous read initiated with BeginReadMultiSampleUInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSampleDouble | Handles the end of an asynchronous read initiated with BeginReadSingleSampleDouble(AsyncCallback, Object) and retrieves the read sample. |
|  | EndReadSingleSampleInt32 | Handles the end of an asynchronous read initiated with BeginReadSingleSampleInt32(AsyncCallback, Object) and retrieves the read sample. |
|  | EndReadSingleSampleUInt32 | Handles the end of an asynchronous read initiated with BeginReadSingleSampleUInt32(AsyncCallback, Object) and retrieves the read sample. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | MemoryOptimizedReadMultiSampleDouble(Int32, Double, Int32) | Reads one or more Double samples from one or more CIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSampleDouble(Int32, Double, ReallocationPolicy, Int32) | Reads one or more Double samples from one or more CIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSampleInt32(Int32, Int32, Int32) | Reads one or more Int32 samples from one or more CIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSampleInt32(Int32, Int32, ReallocationPolicy, Int32) | Reads one or more Int32 samples from one or more CIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSampleUInt32(Int32, UInt32, Int32) | Reads one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSampleUInt32(Int32, UInt32, ReallocationPolicy, Int32) | Reads one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | ReadMultiSampleDouble | Reads one or more Double samples from one or more CIChannel objects in a task. |
|  | ReadMultiSampleInt32 | Reads one or more Int32 samples from one or more CIChannel objects in a task. |
|  | ReadMultiSampleUInt32 | Reads one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | ReadSingleSampleDouble | Reads a single Double sample from one or more CIChannel objects in a task. |
|  | ReadSingleSampleInt32 | Reads a single Int32 sample from one or more CIChannel objects in a task. |
|  | ReadSingleSampleUInt32 | Reads a single UInt32 sample from one or more CIChannel objects in a task. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

CounterMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_countermultichannelwriter.htm language=enus -->
## TOPIC 00142: CounterMultiChannelWriter Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_countermultichannelwriter.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_countermultichannelwriter.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelWriter Methods

### CounterMultiChannelWriter Methods

The [CounterMultiChannelWriter](t_nationalinstruments_daqmx_countermultichannelwriter.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginWriteSingleSample(Boolean, CODataFrequency, AsyncCallback, Object) | Begins an asynchronous write of a single frequency sample to one or more COChannel objects in a counter output task. |
|  | BeginWriteSingleSample(Boolean, CODataTicks, AsyncCallback, Object) | Begins an asynchronous write of a single ticks sample to one or more COChannel objects in a counter output task. |
|  | BeginWriteSingleSample(Boolean, CODataTime, AsyncCallback, Object) | Begins an asynchronous write of a single time sample to one or more COChannel objects in a counter output task. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndWrite | Handles the end of an asynchronous write initiated with any of the counter asynchronous write methods, such as BeginWriteSingleSample(Boolean, CODataFrequency, AsyncCallback, Object). |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |
|  | WriteSingleSample(Boolean, CODataFrequency) | Writes a single frequency sample to one or more COChannel objects in a counter output task. |
|  | WriteSingleSample(Boolean, CODataTicks) | Writes a single ticks sample to one or more COChannel objects in a counter output task. |
|  | WriteSingleSample(Boolean, CODataTime) | Writes a single time sample to one or more COChannel objects in a counter output task. |

Top

##### See Also

###### Reference

CounterMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_counteroutputeventargs.htm language=enus -->
## TOPIC 00143: CounterOutputEventArgs Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_counteroutputeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_counteroutputeventargs.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterOutputEventArgs Methods

### CounterOutputEventArgs Methods

The [CounterOutputEventArgs](t_nationalinstruments_daqmx_counteroutputeventargs.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

CounterOutputEventArgs Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_countersinglechannelreader.htm language=enus -->
## TOPIC 00144: CounterSingleChannelReader Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_countersinglechannelreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_countersinglechannelreader.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader Methods

### CounterSingleChannelReader Methods

The [CounterSingleChannelReader](t_nationalinstruments_daqmx_countersinglechannelreader.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double) | Begins an asynchronous memory-optimized read of one or more Double samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more Double samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32) | Begins an asynchronous memory-optimized read of one or more Int32 samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more Int32 samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseFrequency(Int32, AsyncCallback, Object, CIDataFrequency) | Begins an asynchronous memory-optimized read of one or more CIDataFrequency samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseFrequency(Int32, AsyncCallback, Object, CIDataFrequency, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more CIDataFrequency samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseTicks(Int32, AsyncCallback, Object, CIDataTicks) | Begins an asynchronous memory-optimized read of one or more CIDataTicks samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseTicks(Int32, AsyncCallback, Object, CIDataTicks, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more CIDataTicks samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseTime(Int32, AsyncCallback, Object, CIDataTime) | Begins an asynchronous memory-optimized read of one or more CIDataTime samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseTime(Int32, AsyncCallback, Object, CIDataTime, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more CIDataTime samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32) | Begins an asynchronous memory-optimized read of one or more UInt32 samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more UInt32 samples from a single CIChannel in a task. |
|  | BeginReadMultiSampleDouble | Begins an asynchronous read of one or more Double samples from a counter task. |
|  | BeginReadMultiSampleInt32 | Begins an asynchronous read of one or more Int32 samples from a counter task. |
|  | BeginReadMultiSamplePulseFrequency | Begins an asynchronous read of one or more pulse samples in terms of frequency from a counter task. |
|  | BeginReadMultiSamplePulseTicks | Begins an asynchronous read of one or more pulse samples in terms of ticks from a counter task. |
|  | BeginReadMultiSamplePulseTime | Begins an asynchronous read of one or more pulse samples in terms of time from a counter task. |
|  | BeginReadMultiSampleUInt32 | Begins an asynchronous read of one or more UInt32 samples from a counter task. |
|  | BeginReadSingleSampleDouble | Begins an asynchronous read of a Double sample from a counter task. |
|  | BeginReadSingleSampleInt32 | Begins an asynchronous read of a 32-bit integer sample from a counter task. |
|  | BeginReadSingleSamplePulseFrequency | Begins an asynchronous read of a single pulse sample in terms of frequency from a counter task. |
|  | BeginReadSingleSamplePulseTicks | Begins an asynchronous read of a single pulse sample in terms of ticks from a counter task. |
|  | BeginReadSingleSamplePulseTime | Begins an asynchronous read of a single pulse sample in terms of time from a counter task. |
|  | BeginReadSingleSampleUInt32 | Begins an asynchronous read of a UInt32 sample from a counter task. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndMemoryOptimizedReadMultiSampleDouble | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSampleInt32 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSamplePulseFrequency | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePulseFrequency(Int32, AsyncCallback, Object, CIDataFrequency) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSamplePulseTicks | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePulseTicks(Int32, AsyncCallback, Object, CIDataTicks) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSamplePulseTime | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePulseTime(Int32, AsyncCallback, Object, CIDataTime) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSampleUInt32 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32) and retrieves the read samples. |
|  | EndReadMultiSampleDouble | Handles the end of an asynchronous read initiated with BeginReadMultiSampleDouble(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSampleInt32 | Handles the end of an asynchronous read initiated with BeginReadMultiSampleInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSamplePulseFrequency | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePulseFrequency(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSamplePulseTicks | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePulseTicks(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSamplePulseTime | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePulseTime(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSampleUInt32 | Handles the end of an asynchronous read initiated with BeginReadMultiSampleUInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSampleDouble | Handles the end of an asynchronous read initiated with BeginReadSingleSampleDouble(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSampleInt32 | Handles the end of an asynchronous read initiated with BeginReadSingleSampleInt32(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePulseFrequency | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePulseFrequency(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePulseTicks | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePulseTicks(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePulseTime | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePulseTime(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSampleUInt32 | Handles the end of an asynchronous read initiated with BeginReadSingleSampleUInt32(AsyncCallback, Object) and retrieves the read samples. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | MemoryOptimizedReadMultiSampleDouble(Int32, Double, Int32) | Reads one or more Double samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSampleDouble(Int32, Double, ReallocationPolicy, Int32) | Reads one or more Double samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSampleInt32(Int32, Int32, Int32) | Reads one or more Int32 samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSampleInt32(Int32, Int32, ReallocationPolicy, Int32) | Reads one or more Int32 samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseFrequency(Int32, CIDataFrequency, Int32) | Reads one or more CIDataFrequency samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseFrequency(Int32, CIDataFrequency, ReallocationPolicy, Int32) | Reads one or more CIDataFrequency samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseTicks(Int32, CIDataTicks, Int32) | Reads one or more CIDataTicks samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseTicks(Int32, CIDataTicks, ReallocationPolicy, Int32) | Reads one or more CIDataTicks samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseTime(Int32, CIDataTime, Int32) | Reads one or more CIDataTime samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseTime(Int32, CIDataTime, ReallocationPolicy, Int32) | Reads one or more CIDataTime samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSampleUInt32(Int32, UInt32, Int32) | Reads one or more UInt32 samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSampleUInt32(Int32, UInt32, ReallocationPolicy, Int32) | Reads one or more UInt32 samples from a single CIChannel in a task. |
|  | ReadMultiSampleDouble | Reads one or more Double samples from a counter task. |
|  | ReadMultiSampleInt32 | Reads one or more Int32 samples from a counter task. |
|  | ReadMultiSamplePulseFrequency | Reads one or more pulse samples in terms of frequency from a counter task. |
|  | ReadMultiSamplePulseTicks | Reads one or more pulse samples in terms of ticks from a counter task. |
|  | ReadMultiSamplePulseTime | Reads one or more pulse samples in terms of time from a counter task. |
|  | ReadMultiSampleUInt32 | Reads one or more UInt32 samples from a counter task. |
|  | ReadSingleSampleDouble | Reads a single Double sample from a counter task. |
|  | ReadSingleSampleInt32 | Reads a Int32 sample from a counter task. |
|  | ReadSingleSamplePulseFrequency | Reads a pulse sample in terms of frequency from a counter task. |
|  | ReadSingleSamplePulseTicks | Reads a pulse sample in terms of ticks from a counter task. |
|  | ReadSingleSamplePulseTime | Reads a pulse sample in terms of time from a counter task. |
|  | ReadSingleSampleUInt32 | Reads an UInt32 sample from a counter task. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_digitalpatternpausetrigger.htm language=enus -->
## TOPIC 00145: DigitalPatternPauseTrigger Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_digitalpatternpausetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_digitalpatternpausetrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternPauseTrigger Methods

### DigitalPatternPauseTrigger Methods

The [DigitalPatternPauseTrigger](t_nationalinstruments_daqmx_digitalpatternpausetrigger.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

DigitalPatternPauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_externalcalibrationsession.htm language=enus -->
## TOPIC 00146: ExternalCalibrationSession Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_externalcalibrationsession.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_externalcalibrationsession.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession Methods

### ExternalCalibrationSession Methods

The [ExternalCalibrationSession](t_nationalinstruments_daqmx_externalcalibrationsession.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Adjust1102 | Adjusts the external calibration constants for an SCXI-1102 module. |
|  | Adjust1104 | Adjusts the external calibration constants for an SCXI-1104 module. |
|  | Adjust1112 | Adjusts the external calibration constants for an SCXI-1112 module. |
|  | Adjust1122 | Adjusts the external calibration constants for an SCXI-1122 module. |
|  | Adjust1124 | Adjusts the external calibration constants for an SCXI-1124 module. |
|  | Adjust1125 | Adjusts the external calibration constants for an SCXI-1125 module. |
|  | Adjust1126 | Adjusts the external calibration constants for an SCXI-1126 module. |
|  | Adjust1141 | Adjusts the external calibration constants for an SCXI-1141 module. |
|  | Adjust1142 | Adjusts the external calibration constants for an SCXI-1142 module. |
|  | Adjust1143 | Adjusts the external calibration constants for an SCXI-1143 module. |
|  | Adjust11601 | Adjusts theexternal calibrationconstants for an NI FD-11601 device bank. |
|  | Adjust11603 | Adjusts theexternal calibrationconstants for an NI FD-11603 device bank. |
|  | Adjust11605 | Adjusts theexternal calibrationconstants for an NI FD-11605 device bank. |
|  | Adjust11613 | Adjusts theexternal calibrationconstants for an NI FD-11613 device bank. |
|  | Adjust11614 | Adjusts theexternal calibrationconstants for an NI FD-11614 device bank. |
|  | Adjust11634 | Adjusts theexternal calibrationconstants for an NI FD-11634 device bank. |
|  | Adjust11637 | Adjusts theexternal calibrationconstants for an NI FD-11637 device bank. |
|  | Adjust1502 | Adjusts the external calibration constants for an SCXI-1502 module. |
|  | Adjust1503 | Adjusts the external calibration constants for an SCXI-1503 module. |
|  | Adjust1503Current | Adjusts the external calibration constants for an SCXI-1503 module. |
|  | Adjust1520 | Adjusts the external calibration constants for an SCXI-1520 module. |
|  | Adjust1521 | Adjusts the external calibration constants for an SCXI-1521 module. |
|  | Adjust153x | Adjusts the external calibration constants for an SCXI-1530 or SCXI-1531 module. |
|  | Adjust1540 | Adjusts the external calibration constants for an SCXI-1540 module. |
|  | Adjust4204 | Adjusts the external calibration constants for an NI 4204 device. |
|  | Adjust4220 | Adjusts the external calibration constants for an NI 4220 device. |
|  | Adjust4224 | Adjusts the external calibration constants for an NI 4224 device. |
|  | Adjust4225 | Obsolete. The Adjust4225(String, Double, Double) method has been deprecated. Adjusts the external calibration constants for an NI 4225 device. |
|  | Adjust4300 | Adjusts the external calibration constants on an NI 4300 device. |
|  | Adjust4302 | Adjusts the external calibration constants for an NI 4302. Connect a known voltage to the device and specify that voltage with referenceVoltage. |
|  | Adjust4303 | Adjusts the external calibration constants for an NI 4303. Connect a known voltage to the device and specify that voltage with referenceVoltage. |
|  | Adjust4304 | Adjusts the external calibration constants for an NI 4304. Connect a known voltage to the device and specify that voltage with referenceVoltage. |
|  | Adjust4305 | Adjusts the external calibration constants for an NI 4305. Connect a known voltage to the device and specify that voltage with referenceVoltage. |
|  | Adjust4309 | Adjusts the calibration constants for a PXIe-4309 device. |
|  | Adjust4310 | Adjusts the calibration constants for a PXIe-4310 device. |
|  | Adjust4322 | Adjusts the external calibration constants on an NI 4322 device. |
|  | Adjust4339 | Adjusts the external calibration constants for an NI PXIe 4339 device. |
|  | Adjust433x | Adjusts the external calibration constants on an NI PXIe-433x device. |
|  | Adjust4353 | Adjusts the external calibration constants on an NI 4353 device. |
|  | Adjust4357 | Adjusts the external calibration constants for an NI 4357 device. |
|  | Adjust9201 | Adjusts the external calibration constants for an NI 9201 device. |
|  | Adjust9202 | Adjusts the external calibration constants for an NI 9202 device. |
|  | Adjust9203Gain | Adjusts the external calibration gain constants for an NI 9203 device. |
|  | Adjust9203Offset | Adjusts the external calibration offset constants for an NI 9203 device. |
|  | Adjust9205 | Adjusts the external calibration constants for an NI 9205 device. |
|  | Adjust9206 | Adjusts the external calibration constants for an NI 9206 device. |
|  | Adjust9207Gain | Adjusts the external calibration gain constants for an NI 9207 device. |
|  | Adjust9207Offset | Adjusts the external calibration offset constants for an NI 9207 device. |
|  | Adjust9208Gain | Adjusts the external calibration gain constants for an NI 9208 device. |
|  | Adjust9208Offset | Adjusts the external calibration offset constants for an NI 9208 device. |
|  | Adjust9209Gain | Adjusts the external calibration gain constants for an NI 9209 device. |
|  | Adjust9209Offset | Adjusts the external calibration offset constants for an NI 9209 device. |
|  | Adjust9210 | Adjusts the external calibration constants for an NI 9210 device. |
|  | Adjust9211 | Adjusts the external calibration constants for an NI 9211 device. |
|  | Adjust9212 | Adjusts the external calibration constants for an NI 9212 device. |
|  | Adjust9213 | Adjusts the external calibration constants for an NI 9213 device. |
|  | Adjust9214 | Adjusts the external calibration constants for an NI 9214 device. |
|  | Adjust9215 | Adjusts the external calibration constants for an NI 9215 device. |
|  | Adjust9216 | Adjusts the external calibration constants for an NI 9216 device. |
|  | Adjust9217 | Adjusts the external calibration constants for an NI 9217 device. |
|  | Adjust9218 | Adjusts the external calibration constants for an NI 9218 device. |
|  | Adjust9219 | Adjusts the external calibration constants for an NI 9219 device. |
|  | Adjust9220 | Adjusts the external calibration constants for an NI 9220 device. |
|  | Adjust9221 | Adjusts the external calibration constants for an NI 9221 device. |
|  | Adjust9222 | Adjusts the external calibration constants for an NI 9222 device. |
|  | Adjust9223 | Adjusts the external calibration constants for an NI 9223 device. |
|  | Adjust9224 | Adjusts the external calibration constants for an NI 9224 device. |
|  | Adjust9225 | Adjusts the external calibration constants for an NI 9225 device. |
|  | Adjust9226 | Adjusts the external calibration constants for an NI 9226 device. |
|  | Adjust9227 | Adjusts the external calibration constants for an NI 9227 device. |
|  | Adjust9228 | Adjusts the external calibration constants for an NI 9228 device. |
|  | Adjust9229 | Adjusts the external calibration constants for an NI 9229 device. |
|  | Adjust9230 | Adjusts the external calibration constants for an NI 9230 device. |
|  | Adjust9231 | Adjusts the external calibration constants for an NI 9231 device. |
|  | Adjust9232 | Adjusts the external calibration constants for an NI 9232 device. |
|  | Adjust9234Gain | Adjusts the external calibration gain constants for an NI 9234 device. |
|  | Adjust9234Offset | Adjusts the external calibration offset constants for an NI 9234 device. |
|  | Adjust9238 | Adjusts the external calibration constants for an NI 9238 device. |
|  | Adjust9239 | Adjusts the external calibration constants for an NI 9239 device. |
|  | Adjust9242 | Adjusts the external calibration constants for an NI 9242 device. |
|  | Adjust9244 | Adjusts the external calibration constants for an NI 9244 device. |
|  | Adjust9246 | Adjusts the external calibration constants for an NI 9246 device. |
|  | Adjust9247 | Adjusts the external calibration constants for an NI 9247 device. |
|  | Adjust9250 | Adjusts the external calibration constants for an NI 9250 device. |
|  | Adjust9251 | Adjusts the external calibration constants for an NI 9251 device. |
|  | Adjust9252 | Adjusts the external calibration constants for an NI 9252 device. |
|  | Adjust9253 | Adjusts the external calibration constants for an NI 9253 device. |
|  | Adjust9260 | Adjusts the external calibration constants for an NI 9260 device. |
|  | Adjust9262 | Adjusts the external calibration constants for an NI 9262 device. |
|  | Adjust9263 | Adjusts the external calibration constants for an NI 9263 device. |
|  | Adjust9264 | Adjusts the external calibration constants for an NI 9264 device. |
|  | Adjust9265 | Adjusts the external calibration constants for an NI 9265 device. |
|  | Adjust9266 | Adjusts the external calibration constants for an NI 9266 device. |
|  | Adjust9269 | Adjusts the external calibration constants for an NI 9269 device. |
|  | Adjust9775 | Adjusts the external calibration constants for an NI 9775 device. |
|  | AdjustAOSeries | Adjusts the external calibration constants on an AO Series device. |
|  | AdjustDsa4463 | Adjusts the external calibration constants for the analog output section of a NI 4463 device. |
|  | AdjustDsa4610 | Adjusts the external calibration gain constants for an NI 4610. |
|  | AdjustDsaAI(Double) | Adjusts the external calibration constants for the analog input section of a DSA device without shorting the input terminals. |
|  | AdjustDsaAI(Double, Boolean) | Adjusts the external calibration constants for the analog input section of a DSA device. You can specify whether you want to short the input terminals or not. |
|  | AdjustDsaAI(AICoupling, Double, Double) | Performs external calibration adjustment on a DSA device with the specified gain and coupling configuration. |
|  | AdjustDsaAO | Adjusts the external calibration constants for the analog output section of a DSA device. |
|  | AdjustDsaAOTimebase | Adjusts the external calibration constants for the timebase of a DSA device with an adjustible oscillator. |
|  | AdjustDsaTimebase | Adjusts the external calibration constants for the timebase of a DSA device with an adjustible oscillator. |
|  | AdjustESeries | Adjusts the external calibration constants on an E Series device. |
|  | AdjustMSeries | Adjusts the external calibration constants for an M Series device. |
|  | AdjustSCBaseboard | Adjusts the external calibration constants for the baseboard of an SC Series device. |
|  | AdjustSSeries | Adjusts the external calibration constants for an S Series device. |
|  | AdjustTioTimebase | Adjusts the external calibration constants for the timebase of a TIO device. |
|  | AdjustXSeries | Adjusts the external calibration constants for an X Series device. |
|  | ConnectSCExpressCalibrationAccessoryChannels | Configures a connection on the SC Express accessory for the specified physical channel(s). |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | CSeriesSetCalibrationTemperature | Specifies the temperature of a C Series device for the current external calibration session. |
|  | DisconnectSCExpressCalibrationAccessoryChannels | Disconnects the configured connection on an SC Express accessory and connects the accessory in the default configuration. |
|  | Dispose | Releases all resources used by ExternalCalibrationSession. |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by ExternalCalibrationSession or optionally releases only the unmanaged resources. |
|  | DsaSetCalibrationTemperature | Specifies the temperature of a DSA device for the current external calibration session. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | FieldDAQSetCalibrationTemperature | Specifies the temperature of a FieldDAQ device for the current external calibration session. |
|  | Get11601AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get11603AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get11605AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get11613AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get11614AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get11634AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get4302AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get4303AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get4304AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get4305AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get4322AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get4339AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9201AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9202AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9203AdjustmentPoints | Returns the reference current values to be used by a reference device to create a reference signal. |
|  | Get9207AdjustmentPoints | Returns the reference voltage or current values to be used by a reference device to create a reference signal. |
|  | Get9208AdjustmentPoints | Returns the reference current values to be used by a reference device to create a reference signal. |
|  | Get9209AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9212AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9213AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9214AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9215AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9216AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9217AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9218AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9219AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9220AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9221AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9222AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9223AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9224AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9225AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9226AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9227AdjustmentPoints | Returns the reference current values to be used by a reference device to create a reference signal. |
|  | Get9228AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9229AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9230AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9231AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9232AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9234AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9238AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9239AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9242AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9244AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9246AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9247AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9250AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9251AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9252AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9253AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9260AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9262AdjustmentPoints | Returns the reference voltage values to be measured by a reference device. |
|  | Get9263AdjustmentPoints | Returns the reference voltage values to be measured by a reference device. |
|  | Get9264AdjustmentPoints | Returns the reference voltage values to be measured by a reference device. |
|  | Get9265AdjustmentPoints | Returns the reference current values to be measured by a reference device. |
|  | Get9266AdjustmentPoints | Returns the reference current values to be measured by a reference device. |
|  | Get9269AdjustmentPoints | Returns the reference voltage values to be measured by a reference device. |
|  | Get9775AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | GetDsa4463AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | SaveChangesAndDispose | Closes an open external calibration session and saves the calibration changes made in the session. |
|  | SetSCExpressCalibrationAccessoryBridgeOutput | Configures an SC Express accessory to produce the bridge output specified in volts-per-volt. |
|  | Setup1102 | Configures the calibration task for an SCXI-1102 module. |
|  | Setup1104 | Configures the calibration task for an SCXI-1104 module. |
|  | Setup1112 | Configures the calibration task for an SCXI-1112 module. |
|  | Setup1122 | Configures the calibration task for an SCXI-1122 module. |
|  | Setup1124(String, Scxi1124Range, Int64) | Configures the calibration task for an SCXI-1124 module. |
|  | Setup1124(String, Scxi1124Range, UInt32) | Configures the calibration task for an SCXI-1124 module. |
|  | Setup1125 | Configures the calibration task for an SCXI-1125 module. |
|  | Setup1126 | Configures the channel and range for an SCXI-1126 module calibration task. |
|  | Setup1141 | Configures the gain value for an SCXI-1141 module calibration task. |
|  | Setup1142 | Configures the gain value for an SCXI-1142 module calibration task. |
|  | Setup1143 | Configures the gain value for an SCXI-1143 module calibration task. |
|  | Setup11605 | Sets up external calibration for an FD 11605 device. |
|  | Setup11634 | Sets up external calibration for an FD 11634 device. |
|  | Setup11637 | Sets up external calibration for an FD 11637 device. |
|  | Setup1502 | Configures the calibration task for an SCXI-1502 module. |
|  | Setup1503 | Configures the calibration task for an SCXI-1503 module. |
|  | Setup1520 | Configures the calibration task for an SCXI-1520 module. |
|  | Setup1521 | Configures the calibration task for an SCXI-1521 module. |
|  | Setup153x | Configures the gain value for an SCXI-1530 or SCXI-1531 module calibration task. |
|  | Setup1540 | Configures the gain value for an SCXI-1540 module calibration task. |
|  | Setup4302 | Initializes an NI PXIe-4302 device with the specified range for calibration. |
|  | Setup4303 | Initializes an NI PXIe-4303 device with the specified range for calibration. |
|  | Setup4304 | Initializes an NI PXIe-4304 device with the specified range for calibration. |
|  | Setup4305 | Initializes an NI PXIe-4305 device with the specified range for calibration. |
|  | Setup4322 | Configures the calibration task for an NI 4322 device. |
|  | Setup4339 | Initializes an NI PXIe 4339 device with the specified mode, range, and exitation for calibration. |
|  | Setup433x | Configures the calibration task for an NI PXIe-433x device. |
|  | Setup9218 | Sets up external calibration for an NI 9218 device. |
|  | Setup9219 | Sets up external calibration for an NI 9219 device. |
|  | Setup9242 | Reads the specified value from the ADC on the specified physical channel. This method requires a sweep of DAC values obtained from Get9242AdjustmentPoints. |
|  | Setup9244 | Reads the specified value from the ADC on the specified physical channel. This method requires a sweep of DAC values obtained from Get9244AdjustmentPoints. |
|  | Setup9260 | Writes the specified binary value to the DAC on the specified physical channel. This modules requires a sweep of DAC values obtained from the Get9260AdjustmentPoints. |
|  | Setup9262 | Writes the specified binary value to the DAC on the specified physical channel. This method requires a sweep of DAC values obtained from Get9262AdjustmentPoints. |
|  | Setup9263 | Writes the specified binary value to the DAC on the specified physical channel. This method requires a sweep of DAC values obtained from Get9263AdjustmentPoints. |
|  | Setup9264 | Writes the specified binary value to the DAC on the specified physical channel. This method requires a sweep of DAC values obtained from Get9264AdjustmentPoints. |
|  | Setup9265 | Writes the specified binary value to the DAC on the specified physical channel. This method requires a sweep of DAC values obtained from Get9265AdjustmentPoints. |
|  | Setup9266 | Applies the specified DAC value to the AO channels, such that it can then be measured by a DMM |
|  | Setup9269 | Writes the specified binary value to the DAC on the specified physical channel. This method requires a sweep of DAC values obtained from Get9269AdjustmentPoints. |
|  | SetupDsa4463 | Generates a specified voltage from the DSA device. |
|  | SetupDsa4480 | Generates a specified voltage from the DSA device. |
|  | SetupDsaAOTimebase | Generates a sine wave of a fixed frequency from the DSA device. You must measure the frequency of the generated sine wave and pass that value into AdjustDsaAOTimebase(Double, Boolean). |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_interlockedhandshaketrigger.htm language=enus -->
## TOPIC 00147: InterlockedHandshakeTrigger Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_interlockedhandshaketrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_interlockedhandshaketrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

InterlockedHandshakeTrigger Methods

### InterlockedHandshakeTrigger Methods

The [InterlockedHandshakeTrigger](t_nationalinstruments_daqmx_interlockedhandshaketrigger.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

InterlockedHandshakeTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_savedchannelinfo.htm language=enus -->
## TOPIC 00148: SavedChannelInfo Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_savedchannelinfo.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_savedchannelinfo.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SavedChannelInfo Methods

### SavedChannelInfo Methods

The [SavedChannelInfo](t_nationalinstruments_daqmx_savedchannelinfo.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by SavedChannelInfo. |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by SavedChannelInfo or optionally releases only the unmanaged resources. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

SavedChannelInfo Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_triggers.htm language=enus -->
## TOPIC 00149: Triggers Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_triggers.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_triggers.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Triggers Methods

### Triggers Methods

The [Triggers](t_nationalinstruments_daqmx_triggers.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

Triggers Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_watchdog.htm language=enus -->
## TOPIC 00150: Watchdog Methods

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_watchdog.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/methods_t_nationalinstruments_daqmx_watchdog.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Watchdog Methods

### Watchdog Methods

The [Watchdog](t_nationalinstruments_daqmx_watchdog.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ClearExpiration | Unlocks the device after the watchdog timer has expired. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetAOExpirationState | Specifies the state to set the analog output physical channels when the watchdog task expires. |
|  | GetAOExpirationStateType | Specifies the output type of the analog output physical channels when the watchdog task expires. |
|  | GetCOExpirationState | Specifies the state to set the counter output channel terminal when the watchdog task expires. |
|  | GetDOExpirationState | Specifies the state to which to set the digital physical channels when the watchdog task expires. You cannot modify the expiration state of dedicated digital input physical channels. |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ResetTimer | Resets the internal timer to 0. |
|  | SetAOExpirationState | Specifies the state to set the analog output physical channels when the watchdog task expires. |
|  | SetAOExpirationStateType | Specifies the output type of the analog output physical channels when the watchdog task expires. |
|  | SetCOExpirationState | Specifies the state to set the counter output channel terminal when the watchdog task expires. |
|  | SetDOExpirationState | Specifies the state to which to set the digital physical channels when the watchdog task expires. You cannot modify the expiration state of dedicated digital input physical channels. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### See Also

###### Reference

Watchdog Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/operators_t_nationalinstruments_daqmx_codatafrequency.htm language=enus -->
## TOPIC 00151: CODataFrequency Operators

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/operators_t_nationalinstruments_daqmx_codatafrequency.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/operators_t_nationalinstruments_daqmx_codatafrequency.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CODataFrequency Operators

### CODataFrequency Operators

The [CODataFrequency](t_nationalinstruments_daqmx_codatafrequency.htm) type exposes the following members.

##### Operators

|  | Name | Description |
| --- | --- | --- |
|  | Equality | Returns true if two CODataFrequency objects are equal. |
|  | Inequality | Returns true if two CODataFrequency objects are not equal. |

Top

##### See Also

###### Reference

CODataFrequency Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/operators_t_nationalinstruments_daqmx_codataticks.htm language=enus -->
## TOPIC 00152: CODataTicks Operators

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/operators_t_nationalinstruments_daqmx_codataticks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/operators_t_nationalinstruments_daqmx_codataticks.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CODataTicks Operators

### CODataTicks Operators

The [CODataTicks](t_nationalinstruments_daqmx_codataticks.htm) type exposes the following members.

##### Operators

|  | Name | Description |
| --- | --- | --- |
|  | Equality | Returns true if two CODataTicks objects are equal. |
|  | Inequality | Returns true if two CODataTicks objects are not equal. |

Top

##### See Also

###### Reference

CODataTicks Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannel_performstrainshuntcalibration.htm language=enus -->
## TOPIC 00153: AIChannelPerformStrainShuntCalibration Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannel_performstrainshuntcalibration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannel_performstrainshuntcalibration.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.PerformStrainShuntCalibration Method

### AIChannelPerformStrainShuntCalibration Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | PerformStrainShuntCalibration(Double, ShuntElementLocation) | Performs shunt calibration for the virtual channels in the task using a strain gage sensor. An error will occur if not all virtual channels in the task support this operation. |
|  | PerformStrainShuntCalibration(Double, ShuntElementLocation, Boolean) | Performs shunt calibration for the virtual channels in the task using a strain gage sensor. |
|  | PerformStrainShuntCalibration(Double, ShuntElementLocation, ShuntCalibrationSelect, ShuntResistorSource) | Performs shunt calibration for the specified channels using a strain gage sensor. |
|  | PerformStrainShuntCalibration(Double, ShuntElementLocation, ShuntCalibrationSelect, ShuntResistorSource, Boolean) | Performs shunt calibration for the specified channels using a strain gage sensor. |

Top

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createcurrentrmschannel.htm language=enus -->
## TOPIC 00154: AIChannelCollectionCreateCurrentRmsChannel Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createcurrentrmschannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createcurrentrmschannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateCurrentRmsChannel Method

### AIChannelCollectionCreateCurrentRmsChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateCurrentRmsChannel(String, String, AITerminalConfiguration, Double, Double, AICurrentAcrmsUnits) | Creates an AIChannel with an internal shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentRmsChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel with the specified custom scale and an internal shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentRmsChannel(String, String, AITerminalConfiguration, Double, Double, Double, AICurrentAcrmsUnits) | Creates an AIChannel with the specified external shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateCurrentRmsChannel(String, String, AITerminalConfiguration, Double, Double, Double, String) | Creates an AIChannel with the specified custom scale and external shunt resistor to measure AC current. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createeddycurrentproximityprobechannel.htm language=enus -->
## TOPIC 00155: AIChannelCollectionCreateEddyCurrentProximityProbeChannel Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createeddycurrentproximityprobechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createeddycurrentproximityprobechannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateEddyCurrentProximityProbeChannel Method

### AIChannelCollectionCreateEddyCurrentProximityProbeChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateEddyCurrentProximityProbeChannel(String, String, Double, Double, Double, AIEddyCurrentProximityProbeSensitivityUnits, AIEddyCurrentProximityProbeUnits) | Creates an AIChannel that uses an Eddy Current Proximity Probe to measure position. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateEddyCurrentProximityProbeChannel(String, String, Double, Double, Double, AIEddyCurrentProximityProbeSensitivityUnits, String) | Creates an AIChannel with the specified custom scale that uses an Eddy Current Proximity Probe to measure position. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createpressurebridgetwopointlinearchannel.htm language=enus -->
## TOPIC 00156: AIChannelCollectionCreatePressureBridgeTwoPointLinearChannel Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createpressurebridgetwopointlinearchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createpressurebridgetwopointlinearchannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreatePressureBridgeTwoPointLinearChannel Method

### AIChannelCollectionCreatePressureBridgeTwoPointLinearChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreatePressureBridgeTwoPointLinearChannel(String, String, Double, Double, AIPressureUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreatePressureBridgeTwoPointLinearChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createstraingagechannel.htm language=enus -->
## TOPIC 00157: AIChannelCollectionCreateStrainGageChannel Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createstraingagechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createstraingagechannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateStrainGageChannel Method

### AIChannelCollectionCreateStrainGageChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateStrainGageChannel(String, String, Double, Double, AIStrainGageConfiguration, AIExcitationSource, Double, Double, Double, Double, Double, Double, AIStrainUnits) | Creates an AIChannel to measure strain. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateStrainGageChannel(String, String, Double, Double, AIStrainGageConfiguration, AIExcitationSource, Double, Double, Double, Double, Double, Double, String) | Creates an AIChannel with the specified custom scale to measure strain. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedscurrentchannel.htm language=enus -->
## TOPIC 00158: AIChannelCollectionCreateTedsCurrentChannel Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedscurrentchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedscurrentchannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsCurrentChannel Method

### AIChannelCollectionCreateTedsCurrentChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateTedsCurrentChannel(String, String, AITerminalConfiguration, Double, Double, AICurrentUnits) | Creates an AIChannel with an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsCurrentChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel with the specified custom scale and an internal shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsCurrentChannel(String, String, AITerminalConfiguration, Double, Double, Double, AICurrentUnits) | Creates an AIChannel with the specified external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsCurrentChannel(String, String, AITerminalConfiguration, Double, Double, Double, String) | Creates an AIChannel with the specified custom scale and external shunt resistor to measure current. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedsforcebridgechannel.htm language=enus -->
## TOPIC 00159: AIChannelCollectionCreateTedsForceBridgeChannel Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedsforcebridgechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedsforcebridgechannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsForceBridgeChannel Method

### AIChannelCollectionCreateTedsForceBridgeChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateTedsForceBridgeChannel(String, String, Double, Double, AIForceUnits, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsForceBridgeChannel(String, String, Double, Double, String, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure force or load, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedspressurebridgechannel.htm language=enus -->
## TOPIC 00160: AIChannelCollectionCreateTedsPressureBridgeChannel Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedspressurebridgechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedspressurebridgechannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsPressureBridgeChannel Method

### AIChannelCollectionCreateTedsPressureBridgeChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateTedsPressureBridgeChannel(String, String, Double, Double, AIPressureUnits, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. You must configure the physical channel(s) with TEDS information to use this method. |
|  | CreateTedsPressureBridgeChannel(String, String, Double, Double, String, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure pressure, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. You must configure the physical channel(s) with TEDS information to use this method. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedsthermocouplechannel.htm language=enus -->
## TOPIC 00161: AIChannelCollectionCreateTedsThermocoupleChannel Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedsthermocouplechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedsthermocouplechannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsThermocoupleChannel Method

### AIChannelCollectionCreateTedsThermocoupleChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateTedsThermocoupleChannel(String, String, Double, Double, AITemperatureUnits) | Creates an AIChannel that uses a thermocouple to measure temperature using a built-in cold-junction compensation source. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsThermocoupleChannel(String, String, Double, Double, AITemperatureUnits, Double) | Creates an AIChannel that uses a thermocouple to measure temperature using a constant value cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsThermocoupleChannel(String, String, Double, Double, AITemperatureUnits, String) | Creates an AIChannel that uses a thermocouple to measure temperature using a measurement on another channel for cold-junction compensation. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedstorquebridgechannel.htm language=enus -->
## TOPIC 00162: AIChannelCollectionCreateTedsTorqueBridgeChannel Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedstorquebridgechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedstorquebridgechannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsTorqueBridgeChannel Method

### AIChannelCollectionCreateTedsTorqueBridgeChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateTedsTorqueBridgeChannel(String, String, Double, Double, AITorqueUnits, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure torque. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsTorqueBridgeChannel(String, String, Double, Double, String, AIExcitationSource, Double) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. You must configure the physical channel(s) with TEDS information to use this method. NI-DAQmx scales electrical values to physical values according to that TEDS information. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedsvoltagechannel.htm language=enus -->
## TOPIC 00163: AIChannelCollectionCreateTedsVoltageChannel Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedsvoltagechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtedsvoltagechannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTedsVoltageChannel Method

### AIChannelCollectionCreateTedsVoltageChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateTedsVoltageChannel(String, String, AITerminalConfiguration, Double, Double, AIVoltageUnits) | Creates an AIChannel to measure voltage. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTedsVoltageChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel with the specified custom scale to measure voltage. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtorquebridgetwopointlinearchannel.htm language=enus -->
## TOPIC 00164: AIChannelCollectionCreateTorqueBridgeTwoPointLinearChannel Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtorquebridgetwopointlinearchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createtorquebridgetwopointlinearchannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateTorqueBridgeTwoPointLinearChannel Method

### AIChannelCollectionCreateTorqueBridgeTwoPointLinearChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateTorqueBridgeTwoPointLinearChannel(String, String, Double, Double, AITorqueUnits, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateTorqueBridgeTwoPointLinearChannel(String, String, Double, Double, String, AIBridgeConfiguration, AIExcitationSource, Double, Double, Double, Double, AIBridgeElectricalUnits, Double, Double, AIBridgePhysicalUnits) | Creates an AIChannel that uses a Wheatstone bridge to measure torque, with the specified custom scale. Use this instance with sensors whose specifications do not provide a polynomial for scaling or a table of electrical and physical values. When you use this scaling type, NI-DAQmx uses two points of electrical and physical values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createvelocityiepechannel.htm language=enus -->
## TOPIC 00165: AIChannelCollectionCreateVelocityIepeChannel Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createvelocityiepechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createvelocityiepechannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateVelocityIepeChannel Method

### AIChannelCollectionCreateVelocityIepeChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateVelocityIepeChannel(String, String, AITerminalConfiguration, Double, Double, AIVelocityUnits, Double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, Double) | Creates an AIChannel that uses an IEPE velocity sensor to measure velocity. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVelocityIepeChannel(String, String, AITerminalConfiguration, Double, Double, String, Double, AIVelocityIepeSensorSensitivityUnits, AIExcitationSource, Double) | Creates an AIChannel that uses an IEPE velocity sensor to measure velocity. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createvoltagermschannel.htm language=enus -->
## TOPIC 00166: AIChannelCollectionCreateVoltageRmsChannel Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createvoltagermschannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_aichannelcollection_createvoltagermschannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.CreateVoltageRmsChannel Method

### AIChannelCollectionCreateVoltageRmsChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateVoltageRmsChannel(String, String, AITerminalConfiguration, Double, Double, AIVoltageAcrmsUnits) | Creates an AIChannel to measure AC voltage. This method adds one or more physical channels to the AIChannelCollection. |
|  | CreateVoltageRmsChannel(String, String, AITerminalConfiguration, Double, Double, String) | Creates an AIChannel with the specified custom scale to measure AC voltage. This method adds one or more physical channels to the AIChannelCollection. |

Top

##### See Also

###### Reference

AIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_analogsinglechannelreader_beginmemoryoptimizedreadwaveform.htm language=enus -->
## TOPIC 00167: AnalogSingleChannelReaderBeginMemoryOptimizedReadWaveform Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_analogsinglechannelreader_beginmemoryoptimizedreadwaveform.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_analogsinglechannelreader_beginmemoryoptimizedreadwaveform.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogSingleChannelReader.BeginMemoryOptimizedReadWaveform Method

### AnalogSingleChannelReaderBeginMemoryOptimizedReadWaveform Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | BeginMemoryOptimizedReadWaveform(Int32, AsyncCallback, Object, AnalogWaveformDouble) | Begins an asynchronous read of one or more analog waveform samples from a single AIChannel in a task. |
|  | BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, Object, AnalogWaveformDouble) | Begins an asynchronous, memory-optimized read of one or more analog waveform samples from a single AIChannel object in a task for a specified duration. |
|  | BeginMemoryOptimizedReadWaveform(Int32, AsyncCallback, Object, AnalogWaveformDouble, ReallocationPolicy) | Begins an asynchronous read of one or more analog waveform samples from a single AIChannel in a task. |
|  | BeginMemoryOptimizedReadWaveform(TimeSpan, AsyncCallback, Object, AnalogWaveformDouble, ReallocationPolicy) | Begins an asynchronous, memory-optimized read of one or more analog waveform samples from a single AIChannel object in a task for a specified duration. |

Top

##### See Also

###### Reference

AnalogSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_analogunscaledwriter_beginwrite.htm language=enus -->
## TOPIC 00168: AnalogUnscaledWriterBeginWrite Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_analogunscaledwriter_beginwrite.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_analogunscaledwriter_beginwrite.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogUnscaledWriter.BeginWrite Method

### AnalogUnscaledWriterBeginWrite Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | BeginWrite(Boolean, Int16, AsyncCallback, Object) | Begins an asynchronous write of one or more unscaled 16-bit integer samples to one or more AOChannel objects in a task. |
|  | BeginWrite(Boolean, Int32, AsyncCallback, Object) | Begins an asynchronous write of one or more unscaled 32-bit integer samples to one or more AOChannel objects in a task. |
|  | BeginWrite(Boolean, UInt16, AsyncCallback, Object) | Begins an asynchronous write of one or more unscaled 16-bit unsigned integer samples to one or more AOChannel objects in a task. |
|  | BeginWrite(Boolean, UInt32, AsyncCallback, Object) | Begins an asynchronous write of one or more unscaled 32-bit unsigned integer samples to one or more AOChannel objects in a task. |

Top

##### See Also

###### Reference

AnalogUnscaledWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_analogunscaledwriter_write.htm language=enus -->
## TOPIC 00169: AnalogUnscaledWriterWrite Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_analogunscaledwriter_write.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_analogunscaledwriter_write.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogUnscaledWriter.Write Method

### AnalogUnscaledWriterWrite Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | Write(Boolean, Int16) | Writes one or more unscaled 16-bit integer samples to one or more AOChannel objects in a task. |
|  | Write(Boolean, Int32) | Writes one or more unscaled 32-bit integer samples to one or more AOChannel objects in a task. |
|  | Write(Boolean, UInt16) | Writes one or more unscaled 16-bit unsigned integer samples to one or more AOChannel objects in a task. |
|  | Write(Boolean, UInt32) | Writes one or more unscaled 32-bit unsigned integer samples to one or more AOChannel objects in a task. |

Top

##### See Also

###### Reference

AnalogUnscaledWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_cichannelcollection_createangularencoderchannel.htm language=enus -->
## TOPIC 00170: CIChannelCollectionCreateAngularEncoderChannel Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_cichannelcollection_createangularencoderchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_cichannelcollection_createangularencoderchannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannelCollection.CreateAngularEncoderChannel Method

### CIChannelCollectionCreateAngularEncoderChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateAngularEncoderChannel(String, String, CIEncoderDecodingType, Boolean, Double, CIEncoderZIndexPhase, Int32, Double, CIAngularEncoderUnits) | Creates a CIChannel that uses an angular encoder to measure angular position. This method adds one channel to the CIChannelCollection. |
|  | CreateAngularEncoderChannel(String, String, CIEncoderDecodingType, Boolean, Double, CIEncoderZIndexPhase, Int32, Double, String) | Creates a CIChannel with the specified custom scale that uses an angular encoder to measure angular position. This method adds one channel to the CIChannelCollection. |

Top

##### See Also

###### Reference

CIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_cichannelcollection_createangularvelocitychannel.htm language=enus -->
## TOPIC 00171: CIChannelCollectionCreateAngularVelocityChannel Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_cichannelcollection_createangularvelocitychannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_cichannelcollection_createangularvelocitychannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannelCollection.CreateAngularVelocityChannel Method

### CIChannelCollectionCreateAngularVelocityChannel Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CreateAngularVelocityChannel(String, String, Double, Double, Int64, CIVelocityEncoderType, CIVelocityAngularEncoderUnits) | Creates a channel to measure angular velocity. |
|  | CreateAngularVelocityChannel(String, String, Double, Double, Int64, CIVelocityEncoderType, String) | Creates a channel to measure angular velocity. |
|  | CreateAngularVelocityChannel(String, String, Double, Double, UInt32, CIVelocityEncoderType, CIVelocityAngularEncoderUnits) | Creates a channel to measure angular velocity. |
|  | CreateAngularVelocityChannel(String, String, Double, Double, UInt32, CIVelocityEncoderType, String) | Creates a channel to measure angular velocity. |

Top

##### See Also

###### Reference

CIChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_cidataticks__ctor.htm language=enus -->
## TOPIC 00172: CIDataTicks Constructor

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_cidataticks__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_cidataticks__ctor.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataTicks Constructor

### CIDataTicks Constructor

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | CIDataTicks(Int32, Int32) | Initializes a new instance of the CIDataTicks object with the specified initial values. |
|  | CIDataTicks(UInt32, UInt32) | Initializes a new instance of the CIDataTicks object with the specified unsigned initial values. |

Top

##### See Also

###### Reference

CIDataTicks Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_cidataticks_equals.htm language=enus -->
## TOPIC 00173: CIDataTicksEquals Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_cidataticks_equals.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_cidataticks_equals.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataTicks.Equals Method

### CIDataTicksEquals Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | Equals(Object) | Returns a value indicating if this instance is equal to the specified object. (Overrides ValueTypeEquals(Object).) |
|  | Equals(CIDataTicks) | Returns a value indicating if this instance is equal to the specified CIDataTicks object. |
|  | Equals(CIDataTicks, CIDataTicks) | Returns a value indicating if two specified instances of CIDataTicks are equal. |

Top

##### See Also

###### Reference

CIDataTicks Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_cochannelcollection_item.htm language=enus -->
## TOPIC 00174: COChannelCollectionItem Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_cochannelcollection_item.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_cochannelcollection_item.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

COChannelCollection.Item Property

### COChannelCollectionItem Property

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | ItemInt64 | Gets the COChannel at the specified index. In Visual C#, this property is the indexer. |
|  | ItemString | Gets the COChannel with the specified virtual channel name. In Visual C#, this property is the indexer. |

Top

##### See Also

###### Reference

COChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_countermultichannelreader_beginmemoryoptimizedreadmultisampleuint32.htm language=enus -->
## TOPIC 00175: CounterMultiChannelReaderBeginMemoryOptimizedReadMultiSampleUInt32 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_countermultichannelreader_beginmemoryoptimizedreadmultisampleuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_countermultichannelreader_beginmemoryoptimizedreadmultisampleuint32.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader.BeginMemoryOptimizedReadMultiSampleUInt32 Method

### CounterMultiChannelReaderBeginMemoryOptimizedReadMultiSampleUInt32 Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32) | Begins an asynchronous read of one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32, ReallocationPolicy) | Begins an asynchronous read of one or more UInt32 samples from one or more CIChannel objects in a task. |

Top

##### See Also

###### Reference

CounterMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampledouble.htm language=enus -->
## TOPIC 00176: CounterSingleChannelReaderMemoryOptimizedReadMultiSampleDouble Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampledouble.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_countersinglechannelreader_memoryoptimizedreadmultisampledouble.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader.MemoryOptimizedReadMultiSampleDouble Method

### CounterSingleChannelReaderMemoryOptimizedReadMultiSampleDouble Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | MemoryOptimizedReadMultiSampleDouble(Int32, Double, Int32) | Reads one or more Double samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSampleDouble(Int32, Double, ReallocationPolicy, Int32) | Reads one or more Double samples from a single CIChannel in a task. |

Top

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_daqexception__ctor.htm language=enus -->
## TOPIC 00177: DaqException Constructor

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_daqexception__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_daqexception__ctor.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqException Constructor

### DaqException Constructor

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | DaqException | Initializes a new instance of the DaqException class. |
|  | DaqException(String) | Initializes a new instance of the DaqException class with the specified error message. |
|  | DaqException(SerializationInfo, StreamingContext) | Creates a new instance of the DaqException class with serialized data. |
|  | DaqException(String, Int32) | Initializes a new instance of the DaqException class with the specified error message and NI-DAQmx driver error code. |
|  | DaqException(String, Exception) | Initializes a new instance of the DaqException class with the specified error message and a reference to the inner exception that is the cause of the exception. |
|  | DaqException(String, Int32, Exception) | Initializes a new instance of the DaqException class with the specified error message, NI-DAQmx driver error code, and reference to the inner exception that is the cause of the exception. |

Top

##### See Also

###### Reference

DaqException Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_daqsystem_savescaleas.htm language=enus -->
## TOPIC 00178: DaqSystemSaveScaleAs Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_daqsystem_savescaleas.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_daqsystem_savescaleas.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem.SaveScaleAs Method

### DaqSystemSaveScaleAs Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | SaveScaleAs(Scale, String) | Saves the specified custom scale to Measurement Automation Explorer (MAX) under the specified name. |
|  | SaveScaleAs(Scale, String, String, SaveOptions) | Saves the specified custom scale to Measurement Automation Explorer (MAX) under the specified name and with specified author and options values. |

Top

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportbyte.htm language=enus -->
## TOPIC 00179: DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortByte Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportbyte.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportbyte.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.BeginMemoryOptimizedReadMultiSamplePortByte Method

### DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortByte Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | BeginMemoryOptimizedReadMultiSamplePortByte(Int32, AsyncCallback, Object, Byte) | Begins an asynchronous read of one or more 8-bit unsigned integer samples from a single DIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePortByte(Int32, AsyncCallback, Object, Byte, ReallocationPolicy) | Begins an asynchronous read of one or more 8-bit unsigned integer samples from a single DIChannel in a task. |

Top

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportint32.htm language=enus -->
## TOPIC 00180: DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortInt32 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportint32.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.BeginMemoryOptimizedReadMultiSamplePortInt32 Method

### DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortInt32 Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | BeginMemoryOptimizedReadMultiSamplePortInt32(Int32, AsyncCallback, Object, Int32) | Begins an asynchronous read of one or more 32-bit integer samples from a single DIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePortInt32(Int32, AsyncCallback, Object, Int32, ReallocationPolicy) | Begins an asynchronous read of one or more 32-bit integer samples from a single DIChannel in a task. |

Top

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportuint32.htm language=enus -->
## TOPIC 00181: DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortUInt32 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_digitalsinglechannelreader_beginmemoryoptimizedreadmultisampleportuint32.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.BeginMemoryOptimizedReadMultiSamplePortUInt32 Method

### DigitalSingleChannelReaderBeginMemoryOptimizedReadMultiSamplePortUInt32 Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | BeginMemoryOptimizedReadMultiSamplePortUInt32(Int32, AsyncCallback, Object, UInt32) | Begins an asynchronous read of one or more 32-bit unsigned integer samples from a single DIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePortUInt32(Int32, AsyncCallback, Object, UInt32, ReallocationPolicy) | Begins an asynchronous read of one or more 32-bit unsigned integer samples from a single DIChannel in a task. |

Top

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_digitalsinglechannelreader_memoryoptimizedreadmultisampleportuint32.htm language=enus -->
## TOPIC 00182: DigitalSingleChannelReaderMemoryOptimizedReadMultiSamplePortUInt32 Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_digitalsinglechannelreader_memoryoptimizedreadmultisampleportuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_digitalsinglechannelreader_memoryoptimizedreadmultisampleportuint32.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader.MemoryOptimizedReadMultiSamplePortUInt32 Method

### DigitalSingleChannelReaderMemoryOptimizedReadMultiSamplePortUInt32 Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | MemoryOptimizedReadMultiSamplePortUInt32(Int32, UInt32, Int32) | Reads one or more 32-bit unsigned integer samples from a single DIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePortUInt32(Int32, UInt32, ReallocationPolicy, Int32) | Reads one or more 32-bit unsigned integer samples from a single DIChannel in a task. |

Top

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_externalcalibrationsession_adjustdsaai.htm language=enus -->
## TOPIC 00183: ExternalCalibrationSessionAdjustDsaAI Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_externalcalibrationsession_adjustdsaai.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_externalcalibrationsession_adjustdsaai.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession.AdjustDsaAI Method

### ExternalCalibrationSessionAdjustDsaAI Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | AdjustDsaAI(Double) | Adjusts the external calibration constants for the analog input section of a DSA device without shorting the input terminals. |
|  | AdjustDsaAI(Double, Boolean) | Adjusts the external calibration constants for the analog input section of a DSA device. You can specify whether you want to short the input terminals or not. |
|  | AdjustDsaAI(AICoupling, Double, Double) | Performs external calibration adjustment on a DSA device with the specified gain and coupling configuration. |

Top

##### See Also

###### Reference

ExternalCalibrationSession Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_physicalchannel_writetedsdata.htm language=enus -->
## TOPIC 00184: PhysicalChannelWriteTedsData Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_physicalchannel_writetedsdata.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_physicalchannel_writetedsdata.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannel.WriteTedsData Method

### PhysicalChannelWriteTedsData Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | WriteTedsData(Byte, BasicTedsDataOption) | Write TEDS data from a Byte array to a sensor on the physical channel you specify. |
|  | WriteTedsData(String, BasicTedsDataOption) | Write TEDS data from a virtual TEDS file to a sensor on the physical channel you specify. |

Top

##### See Also

###### Reference

PhysicalChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_polynomialscale__ctor.htm language=enus -->
## TOPIC 00185: PolynomialScale Constructor

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_polynomialscale__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_polynomialscale__ctor.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PolynomialScale Constructor

### PolynomialScale Constructor

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | PolynomialScale(String, Double, Double) | Creates a new instance of the PolynomialScale class with the specified forward and reverse coefficients. |
|  | PolynomialScale(String, PolynomialDirection, Double, Double, Double) | Creates a new instance of the PolynomialScale class with the specified forward or reverse coefficients and automatically computes the other set of coefficients with the same order as the provided coefficients, using 1000 points in the specified range. |
|  | PolynomialScale(String, PolynomialDirection, Double, Double, Double, Int32, Int32) | Creates a new instance of the PolynomialScale class with the specified forward or reverse coefficients and automatically computes the other set of coefficients. |

Top

##### See Also

###### Reference

PolynomialScale Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_savedchannelinfo_dispose.htm language=enus -->
## TOPIC 00186: SavedChannelInfoDispose Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_savedchannelinfo_dispose.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_savedchannelinfo_dispose.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SavedChannelInfo.Dispose Method

### SavedChannelInfoDispose Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | Dispose | Releases all resources used by SavedChannelInfo. |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by SavedChannelInfo or optionally releases only the unmanaged resources. |

Top

##### See Also

###### Reference

SavedChannelInfo Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_timing_configurechangedetection.htm language=enus -->
## TOPIC 00187: TimingConfigureChangeDetection Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_timing_configurechangedetection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_timing_configurechangedetection.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.ConfigureChangeDetection Method

### TimingConfigureChangeDetection Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureChangeDetection(String, String, SampleQuantityMode) | Configures the task to acquire samples on the rising and/or falling edges of the specified lines or ports. |
|  | ConfigureChangeDetection(String, String, SampleQuantityMode, Int32) | Configures the task to acquire samples on the rising and/or falling edges of the specified lines or ports and sets the number of samples to acquire. |

Top

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_timing_configureimplicit.htm language=enus -->
## TOPIC 00188: TimingConfigureImplicit Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_timing_configureimplicit.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_timing_configureimplicit.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.ConfigureImplicit Method

### TimingConfigureImplicit Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureImplicit(SampleQuantityMode) | Sets only the duration of the task without specifying timing. |
|  | ConfigureImplicit(SampleQuantityMode, Int32) | Sets only the duration of the task and the number of samples to acquire or generate without specifying timing. |

Top

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_timing_configuresampleclock.htm language=enus -->
## TOPIC 00189: TimingConfigureSampleClock Method

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_timing_configuresampleclock.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/overload_nationalinstruments_daqmx_timing_configuresampleclock.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.ConfigureSampleClock Method

### TimingConfigureSampleClock Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureSampleClock(String, Double, SampleClockActiveEdge, SampleQuantityMode) | Sets the source of the sample clock and the rate of the sample clock. |
|  | ConfigureSampleClock(String, Double, SampleClockActiveEdge, SampleQuantityMode, Int32) | Sets the source of the sample clock, the rate of the sample clock, and the number of samples to acquire or generate. |

Top

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_accelerationchargesensitivityunits.htm language=enus -->
## TOPIC 00190: AIChannelAccelerationChargeSensitivityUnits Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_accelerationchargesensitivityunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_accelerationchargesensitivityunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.AccelerationChargeSensitivityUnits Property

### AIChannelAccelerationChargeSensitivityUnits Property

Specifies the units of AI.Accel.Charge.Sensitivity.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIAccelerationChargeSensitivityUnits AccelerationChargeSensitivityUnits { get; set; }
```

```text
Public Property AccelerationChargeSensitivityUnits As AIAccelerationChargeSensitivityUnits
	Get
	Set
```

###### Property Value

AIAccelerationChargeSensitivityUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_accelerationunits.htm language=enus -->
## TOPIC 00191: AIChannelAccelerationUnits Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_accelerationunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_accelerationunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.AccelerationUnits Property

### AIChannelAccelerationUnits Property

Specifies the units to use to return acceleration measurements from the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIAccelerationUnits AccelerationUnits { get; set; }
```

```text
Public Property AccelerationUnits As AIAccelerationUnits
	Get
	Set
```

###### Property Value

AIAccelerationUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_accelerometersensitivity.htm language=enus -->
## TOPIC 00192: AIChannelAccelerometerSensitivity Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_accelerometersensitivity.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_accelerometersensitivity.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.AccelerometerSensitivity Property

### AIChannelAccelerometerSensitivity Property

accelerometer

AccelerometerSensitivityUnits

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double AccelerometerSensitivity { get; set; }
```

```text
Public Property AccelerometerSensitivity As Double
	Get
	Set
```

###### Property Value

Double

accelerometer

AccelerometerSensitivityUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_attenuation.htm language=enus -->
## TOPIC 00193: AIChannelAttenuation Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_attenuation.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_attenuation.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.Attenuation Property

### AIChannelAttenuation Property

Specifies the amount of attenuation to use.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double Attenuation { get; set; }
```

```text
Public Property Attenuation As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_autozeromode.htm language=enus -->
## TOPIC 00194: AIChannelAutoZeroMode Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_autozeromode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_autozeromode.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.AutoZeroMode Property

### AIChannelAutoZeroMode Property

Specifies how often to measure ground. NI-DAQmx subtracts the measured ground voltage from every sample.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIAutoZeroMode AutoZeroMode { get; set; }
```

```text
Public Property AutoZeroMode As AIAutoZeroMode
	Get
	Set
```

###### Property Value

AIAutoZeroMode

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeelectricalunits.htm language=enus -->
## TOPIC 00195: AIChannelBridgeElectricalUnits Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeelectricalunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeelectricalunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.BridgeElectricalUnits Property

### AIChannelBridgeElectricalUnits Property

Specifies from which electrical unit to scale data. Select the same unit that the sensor data sheet or calibration certificate uses for electrical values.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIBridgeElectricalUnits BridgeElectricalUnits { get; set; }
```

```text
Public Property BridgeElectricalUnits As AIBridgeElectricalUnits
	Get
	Set
```

###### Property Value

AIBridgeElectricalUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeinitialratio.htm language=enus -->
## TOPIC 00196: AIChannelBridgeInitialRatio Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeinitialratio.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeinitialratio.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.BridgeInitialRatio Property

### AIChannelBridgeInitialRatio Property

BridgeInitialVoltage

BridgeInitialVoltage

ExcitationActualValue

BridgeInitialVoltage

ExcitationActualValue

BridgeInitialVoltage

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double BridgeInitialRatio { get; set; }
```

```text
Public Property BridgeInitialRatio As Double
	Get
	Set
```

###### Property Value

Double

BridgeInitialVoltage

BridgeInitialVoltage

ExcitationActualValue

BridgeInitialVoltage

ExcitationActualValue

BridgeInitialVoltage

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgephysicalunits.htm language=enus -->
## TOPIC 00197: AIChannelBridgePhysicalUnits Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgephysicalunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgephysicalunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.BridgePhysicalUnits Property

### AIChannelBridgePhysicalUnits Property

Specifies to which physical unit to scale electrical data. Select the same unit that the sensor data sheet or calibration certificate uses for physical values.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIBridgePhysicalUnits BridgePhysicalUnits { get; set; }
```

```text
Public Property BridgePhysicalUnits As AIBridgePhysicalUnits
	Get
	Set
```

###### Property Value

AIBridgePhysicalUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgescaletype.htm language=enus -->
## TOPIC 00198: AIChannelBridgeScaleType Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgescaletype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgescaletype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.BridgeScaleType Property

### AIChannelBridgeScaleType Property

scaling type

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIBridgeScaleType BridgeScaleType { get; set; }
```

```text
Public Property BridgeScaleType As AIBridgeScaleType
	Get
	Set
```

###### Property Value

AIBridgeScaleType

scaling type

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeshuntcalibrationaactualresistance.htm language=enus -->
## TOPIC 00199: AIChannelBridgeShuntCalibrationAActualResistance Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeshuntcalibrationaactualresistance.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeshuntcalibrationaactualresistance.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.BridgeShuntCalibrationAActualResistance Property

### AIChannelBridgeShuntCalibrationAActualResistance Property

Specifies in ohms the actual value of the internal shunt calibration A resistor.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double BridgeShuntCalibrationAActualResistance { get; set; }
```

```text
Public Property BridgeShuntCalibrationAActualResistance As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeshuntcalibrationaresistance.htm language=enus -->
## TOPIC 00200: AIChannelBridgeShuntCalibrationAResistance Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeshuntcalibrationaresistance.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeshuntcalibrationaresistance.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.BridgeShuntCalibrationAResistance Property

### AIChannelBridgeShuntCalibrationAResistance Property

Specifies in ohms the desired value of the internal shunt calibration A resistor.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double BridgeShuntCalibrationAResistance { get; set; }
```

```text
Public Property BridgeShuntCalibrationAResistance As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeshuntcalibrationbactualresistance.htm language=enus -->
## TOPIC 00201: AIChannelBridgeShuntCalibrationBActualResistance Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeshuntcalibrationbactualresistance.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeshuntcalibrationbactualresistance.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.BridgeShuntCalibrationBActualResistance Property

### AIChannelBridgeShuntCalibrationBActualResistance Property

Specifies in ohms the actual value of the internal shunt calibration B resistor.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double BridgeShuntCalibrationBActualResistance { get; set; }
```

```text
Public Property BridgeShuntCalibrationBActualResistance As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgetwopointlinearfirstphysicalvalue.htm language=enus -->
## TOPIC 00202: AIChannelBridgeTwoPointLinearFirstPhysicalValue Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgetwopointlinearfirstphysicalvalue.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgetwopointlinearfirstphysicalvalue.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.BridgeTwoPointLinearFirstPhysicalValue Property

### AIChannelBridgeTwoPointLinearFirstPhysicalValue Property

BridgeTwoPointLinearFirstElectricalValue

BridgePhysicalUnits

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double BridgeTwoPointLinearFirstPhysicalValue { get; set; }
```

```text
Public Property BridgeTwoPointLinearFirstPhysicalValue As Double
	Get
	Set
```

###### Property Value

Double

BridgeTwoPointLinearFirstElectricalValue

BridgePhysicalUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeunits.htm language=enus -->
## TOPIC 00203: AIChannelBridgeUnits Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_bridgeunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.BridgeUnits Property

### AIChannelBridgeUnits Property

voltage ratios

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIBridgeUnits BridgeUnits { get; set; }
```

```text
Public Property BridgeUnits As AIBridgeUnits
	Get
	Set
```

###### Property Value

AIBridgeUnits

voltage ratios

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_calibrationapplyifexpired.htm language=enus -->
## TOPIC 00204: AIChannelCalibrationApplyIfExpired Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_calibrationapplyifexpired.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_calibrationapplyifexpired.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.CalibrationApplyIfExpired Property

### AIChannelCalibrationApplyIfExpired Property

Specifies whether to apply the channel calibration to the channel after the expiration date has passed.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool CalibrationApplyIfExpired { get; set; }
```

```text
Public Property CalibrationApplyIfExpired As Boolean
	Get
	Set
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_calibrationoperatorname.htm language=enus -->
## TOPIC 00205: AIChannelCalibrationOperatorName Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_calibrationoperatorname.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_calibrationoperatorname.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.CalibrationOperatorName Property

### AIChannelCalibrationOperatorName Property

Specifies the name of the operator who performed the channel calibration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string CalibrationOperatorName { get; set; }
```

```text
Public Property CalibrationOperatorName As String
	Get
	Set
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_chargeunits.htm language=enus -->
## TOPIC 00206: AIChannelChargeUnits Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_chargeunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_chargeunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.ChargeUnits Property

### AIChannelChargeUnits Property

Specifies the units to use to return charge measurements from the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIChargeUnits ChargeUnits { get; set; }
```

```text
Public Property ChargeUnits As AIChargeUnits
	Get
	Set
```

###### Property Value

AIChargeUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_datatransfercustomthreshold.htm language=enus -->
## TOPIC 00207: AIChannelDataTransferCustomThreshold Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_datatransfercustomthreshold.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_datatransfercustomthreshold.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.DataTransferCustomThreshold Property

### AIChannelDataTransferCustomThreshold Property

DataTransferRequestCondition

OnBoardMemoryCustomThreshold

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long DataTransferCustomThreshold { get; set; }
```

```text
Public Property DataTransferCustomThreshold As Long
	Get
	Set
```

###### Property Value

Int64

DataTransferRequestCondition

OnBoardMemoryCustomThreshold

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_digitalfilternotchcenterfrequency.htm language=enus -->
## TOPIC 00208: AIChannelDigitalFilterNotchCenterFrequency Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_digitalfilternotchcenterfrequency.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_digitalfilternotchcenterfrequency.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.DigitalFilterNotchCenterFrequency Property

### AIChannelDigitalFilterNotchCenterFrequency Property

Specifies the center frequency of the stopband for the digital filter.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double DigitalFilterNotchCenterFrequency { get; set; }
```

```text
Public Property DigitalFilterNotchCenterFrequency As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_digitalfilterresponse.htm language=enus -->
## TOPIC 00209: AIChannelDigitalFilterResponse Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_digitalfilterresponse.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_digitalfilterresponse.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.DigitalFilterResponse Property

### AIChannelDigitalFilterResponse Property

Specifies the digital filter response.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public FilterResponse DigitalFilterResponse { get; set; }
```

```text
Public Property DigitalFilterResponse As FilterResponse
	Get
	Set
```

###### Property Value

FilterResponse

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_excitationactualvalue.htm language=enus -->
## TOPIC 00210: AIChannelExcitationActualValue Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_excitationactualvalue.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_excitationactualvalue.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.ExcitationActualValue Property

### AIChannelExcitationActualValue Property

Specifies the actual amount of excitation supplied by an internal excitation source. If you read an internal excitation source more precisely with an external device, set this property to the value you read. NI-DAQmx ignores this value for external excitation. When performing shunt calibration, some devices set this property automatically.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double ExcitationActualValue { get; set; }
```

```text
Public Property ExcitationActualValue As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_excitationdcorac.htm language=enus -->
## TOPIC 00211: AIChannelExcitationDCOrAC Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_excitationdcorac.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_excitationdcorac.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.ExcitationDCOrAC Property

### AIChannelExcitationDCOrAC Property

Specifies if the excitation supply is DC or AC.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIExcitationDCOrAC ExcitationDCOrAC { get; set; }
```

```text
Public Property ExcitationDCOrAC As AIExcitationDCOrAC
	Get
	Set
```

###### Property Value

AIExcitationDCOrAC

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_excitationvalue.htm language=enus -->
## TOPIC 00212: AIChannelExcitationValue Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_excitationvalue.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_excitationvalue.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.ExcitationValue Property

### AIChannelExcitationValue Property

ExcitationVoltageOrCurrent

Voltage

ExcitationVoltageOrCurrent

Current

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double ExcitationValue { get; set; }
```

```text
Public Property ExcitationValue As Double
	Get
	Set
```

###### Property Value

Double

ExcitationVoltageOrCurrent

Voltage

ExcitationVoltageOrCurrent

Current

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_excitationvoltageorcurrent.htm language=enus -->
## TOPIC 00213: AIChannelExcitationVoltageOrCurrent Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_excitationvoltageorcurrent.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_excitationvoltageorcurrent.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.ExcitationVoltageOrCurrent Property

### AIChannelExcitationVoltageOrCurrent Property

Specifies if the channel uses current or voltage excitation.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIExcitationVoltageOrCurrent ExcitationVoltageOrCurrent { get; set; }
```

```text
Public Property ExcitationVoltageOrCurrent As AIExcitationVoltageOrCurrent
	Get
	Set
```

###### Property Value

AIExcitationVoltageOrCurrent

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_filterdelay.htm language=enus -->
## TOPIC 00214: AIChannelFilterDelay Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_filterdelay.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_filterdelay.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.FilterDelay Property

### AIChannelFilterDelay Property

FilterDelayUnits

FilterDelayAdjustment

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double FilterDelay { get; }
```

```text
Public ReadOnly Property FilterDelay As Double
	Get
```

###### Property Value

Double

FilterDelayUnits

FilterDelayAdjustment

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_filterdelayadjustment.htm language=enus -->
## TOPIC 00215: AIChannelFilterDelayAdjustment Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_filterdelayadjustment.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_filterdelayadjustment.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.FilterDelayAdjustment Property

### AIChannelFilterDelayAdjustment Property

RemoveFilterDelay

FilterDelay

FilterDelayUnits

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double FilterDelayAdjustment { get; set; }
```

```text
Public Property FilterDelayAdjustment As Double
	Get
	Set
```

###### Property Value

Double

RemoveFilterDelay

FilterDelay

FilterDelayUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_filterdelayunits.htm language=enus -->
## TOPIC 00216: AIChannelFilterDelayUnits Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_filterdelayunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_filterdelayunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.FilterDelayUnits Property

### AIChannelFilterDelayUnits Property

FilterDelay

FilterDelayAdjustment

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIFilterDelayUnits FilterDelayUnits { get; set; }
```

```text
Public Property FilterDelayUnits As AIFilterDelayUnits
	Get
	Set
```

###### Property Value

AIFilterDelayUnits

FilterDelay

FilterDelayAdjustment

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_frequencyhysteresis.htm language=enus -->
## TOPIC 00217: AIChannelFrequencyHysteresis Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_frequencyhysteresis.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_frequencyhysteresis.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.FrequencyHysteresis Property

### AIChannelFrequencyHysteresis Property

FrequencyThresholdVoltage

FrequencyThresholdVoltage

FrequencyThresholdVoltage

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double FrequencyHysteresis { get; set; }
```

```text
Public Property FrequencyHysteresis As Double
	Get
	Set
```

###### Property Value

Double

FrequencyThresholdVoltage

FrequencyThresholdVoltage

FrequencyThresholdVoltage

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_frequencythresholdvoltage.htm language=enus -->
## TOPIC 00218: AIChannelFrequencyThresholdVoltage Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_frequencythresholdvoltage.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_frequencythresholdvoltage.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.FrequencyThresholdVoltage Property

### AIChannelFrequencyThresholdVoltage Property

Specifies the voltage level at which to recognize waveform repetitions. You should select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double FrequencyThresholdVoltage { get; set; }
```

```text
Public Property FrequencyThresholdVoltage As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_microphonesensitivity.htm language=enus -->
## TOPIC 00219: AIChannelMicrophoneSensitivity Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_microphonesensitivity.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_microphonesensitivity.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.MicrophoneSensitivity Property

### AIChannelMicrophoneSensitivity Property

microphone

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double MicrophoneSensitivity { get; set; }
```

```text
Public Property MicrophoneSensitivity As Double
	Get
	Set
```

###### Property Value

Double

microphone

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rangehigh.htm language=enus -->
## TOPIC 00220: AIChannelRangeHigh Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rangehigh.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rangehigh.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.RangeHigh Property

### AIChannelRangeHigh Property

Specifies the upper limit of the input range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double RangeHigh { get; set; }
```

```text
Public Property RangeHigh As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rawsamplejustification.htm language=enus -->
## TOPIC 00221: AIChannelRawSampleJustification Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rawsamplejustification.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rawsamplejustification.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.RawSampleJustification Property

### AIChannelRawSampleJustification Property

raw sample

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIRawSampleJustification RawSampleJustification { get; }
```

```text
Public ReadOnly Property RawSampleJustification As AIRawSampleJustification
	Get
```

###### Property Value

AIRawSampleJustification

raw sample

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_readopenchannelsexist.htm language=enus -->
## TOPIC 00222: AIChannelReadOpenChannelsExist Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_readopenchannelsexist.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_readopenchannelsexist.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.ReadOpenChannelsExist Property

### AIChannelReadOpenChannelsExist Property

ReadOpenChannels

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool ReadOpenChannelsExist { get; }
```

```text
Public ReadOnly Property ReadOpenChannelsExist As Boolean
	Get
```

###### Property Value

Boolean

ReadOpenChannels

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_resistanceunits.htm language=enus -->
## TOPIC 00223: AIChannelResistanceUnits Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_resistanceunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_resistanceunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.ResistanceUnits Property

### AIChannelResistanceUnits Property

Specifies the units to use to return resistance measurements.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIResistanceUnits ResistanceUnits { get; set; }
```

```text
Public Property ResistanceUnits As AIResistanceUnits
	Get
	Set
```

###### Property Value

AIResistanceUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rosettetype.htm language=enus -->
## TOPIC 00224: AIChannelRosetteType Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rosettetype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rosettetype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.RosetteType Property

### AIChannelRosetteType Property

Indicates the type of rosette gage.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIRosetteType RosetteType { get; }
```

```text
Public ReadOnly Property RosetteType As AIRosetteType
	Get
```

###### Property Value

AIRosetteType

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rtdb.htm language=enus -->
## TOPIC 00225: AIChannelRtdB Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rtdb.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rtdb.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.RtdB Property

### AIChannelRtdB Property

Callendar-Van Dusen equation

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double RtdB { get; set; }
```

```text
Public Property RtdB As Double
	Get
	Set
```

###### Property Value

Double

Callendar-Van Dusen equation

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rtdc.htm language=enus -->
## TOPIC 00226: AIChannelRtdC Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rtdc.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rtdc.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.RtdC Property

### AIChannelRtdC Property

Callendar-Van Dusen equation

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double RtdC { get; set; }
```

```text
Public Property RtdC As Double
	Get
	Set
```

###### Property Value

Double

Callendar-Van Dusen equation

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rtdr0.htm language=enus -->
## TOPIC 00227: AIChannelRtdR0 Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rtdr0.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rtdr0.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.RtdR0 Property

### AIChannelRtdR0 Property

Callendar-Van Dusen equation

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double RtdR0 { get; set; }
```

```text
Public Property RtdR0 As Double
	Get
	Set
```

###### Property Value

Double

Callendar-Van Dusen equation

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rtdtype.htm language=enus -->
## TOPIC 00228: AIChannelRtdType Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rtdtype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rtdtype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.RtdType Property

### AIChannelRtdType Property

type

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIRtdType RtdType { get; set; }
```

```text
Public Property RtdType As AIRtdType
	Get
	Set
```

###### Property Value

AIRtdType

type

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rvdtsensitivity.htm language=enus -->
## TOPIC 00229: AIChannelRvdtSensitivity Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rvdtsensitivity.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_rvdtsensitivity.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.RvdtSensitivity Property

### AIChannelRvdtSensitivity Property

RVDT

RvdtSensitivityUnits

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double RvdtSensitivity { get; set; }
```

```text
Public Property RvdtSensitivity As Double
	Get
	Set
```

###### Property Value

Double

RVDT

RvdtSensitivityUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_sampleandholdenable.htm language=enus -->
## TOPIC 00230: AIChannelSampleAndHoldEnable Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_sampleandholdenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_sampleandholdenable.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.SampleAndHoldEnable Property

### AIChannelSampleAndHoldEnable Property

AutoZeroMode

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool SampleAndHoldEnable { get; set; }
```

```text
Public Property SampleAndHoldEnable As Boolean
	Get
	Set
```

###### Property Value

Boolean

AutoZeroMode

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_sensorpowertype.htm language=enus -->
## TOPIC 00231: AIChannelSensorPowerType Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_sensorpowertype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_sensorpowertype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.SensorPowerType Property

### AIChannelSensorPowerType Property

Specifies the type of power supplied to the sensor.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AISensorPowerType SensorPowerType { get; set; }
```

```text
Public Property SensorPowerType As AISensorPowerType
	Get
	Set
```

###### Property Value

AISensorPowerType

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_sensorpowervoltage.htm language=enus -->
## TOPIC 00232: AIChannelSensorPowerVoltage Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_sensorpowervoltage.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_sensorpowervoltage.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.SensorPowerVoltage Property

### AIChannelSensorPowerVoltage Property

Specifies the voltage level for the sensor's power supply.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double SensorPowerVoltage { get; set; }
```

```text
Public Property SensorPowerVoltage As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_straingageconfiguration.htm language=enus -->
## TOPIC 00233: AIChannelStrainGageConfiguration Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_straingageconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_straingageconfiguration.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.StrainGageConfiguration Property

### AIChannelStrainGageConfiguration Property

bridge configuration

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIStrainGageConfiguration StrainGageConfiguration { get; set; }
```

```text
Public Property StrainGageConfiguration As AIStrainGageConfiguration
	Get
	Set
```

###### Property Value

AIStrainGageConfiguration

bridge configuration

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_straingagegagefactor.htm language=enus -->
## TOPIC 00234: AIChannelStrainGageGageFactor Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_straingagegagefactor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_straingagegagefactor.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.StrainGageGageFactor Property

### AIChannelStrainGageGageFactor Property

Specifies the sensitivity of the strain gage. Gage factor relates the change in electrical resistance to the change in strain. Refer to the sensor documentation for this value.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double StrainGageGageFactor { get; set; }
```

```text
Public Property StrainGageGageFactor As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_strainunits.htm language=enus -->
## TOPIC 00235: AIChannelStrainUnits Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_strainunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_strainunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.StrainUnits Property

### AIChannelStrainUnits Property

Specifies the units to use to return strain measurements from the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIStrainUnits StrainUnits { get; set; }
```

```text
Public Property StrainUnits As AIStrainUnits
	Get
	Set
```

###### Property Value

AIStrainUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_thermistorr1.htm language=enus -->
## TOPIC 00236: AIChannelThermistorR1 Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_thermistorr1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_thermistorr1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.ThermistorR1 Property

### AIChannelThermistorR1 Property

thermistor

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double ThermistorR1 { get; set; }
```

```text
Public Property ThermistorR1 As Double
	Get
	Set
```

###### Property Value

Double

thermistor

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_velocityiepesensordecibelreference.htm language=enus -->
## TOPIC 00237: AIChannelVelocityIepeSensorDecibelReference Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_velocityiepesensordecibelreference.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_velocityiepesensordecibelreference.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.VelocityIepeSensorDecibelReference Property

### AIChannelVelocityIepeSensorDecibelReference Property

Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double VelocityIepeSensorDecibelReference { get; set; }
```

```text
Public Property VelocityIepeSensorDecibelReference As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_voltagedecibelreference.htm language=enus -->
## TOPIC 00238: AIChannelVoltageDecibelReference Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_voltagedecibelreference.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannel_voltagedecibelreference.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannel.VoltageDecibelReference Property

### AIChannelVoltageDecibelReference Property

Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double VoltageDecibelReference { get; set; }
```

```text
Public Property VoltageDecibelReference As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannelcollection_item_1.htm language=enus -->
## TOPIC 00239: AIChannelCollectionItem Property (String)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannelcollection_item_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aichannelcollection_item_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIChannelCollection.Item Property (String)

### AIChannelCollectionItem Property (String)

AIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual AIChannel this[
	string virtualChannelName
] { get; }
```

```text
Public Overridable ReadOnly Default Property Item ( 
	virtualChannelName As String
) As AIChannel
	Get
```

###### Parameters

- **virtualChannelName**
  - Type: SystemStringOne or more virtual channel names that the retrieved AIChannel operates on.

###### Property Value

AIChannel

AIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

virtualChannelName

Channels

##### See Also

###### Reference

AIChannelCollection Class

Item Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Channels

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgereferencetrigger_coupling.htm language=enus -->
## TOPIC 00240: AnalogEdgeReferenceTriggerCoupling Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgereferencetrigger_coupling.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgereferencetrigger_coupling.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeReferenceTrigger.Coupling Property

### AnalogEdgeReferenceTriggerCoupling Property

terminal

virtual channel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogEdgeReferenceTriggerCoupling Coupling { get; set; }
```

```text
Public Property Coupling As AnalogEdgeReferenceTriggerCoupling
	Get
	Set
```

###### Property Value

AnalogEdgeReferenceTriggerCoupling

terminal

virtual channel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AnalogEdgeReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgereferencetrigger_digitalfilterenable.htm language=enus -->
## TOPIC 00241: AnalogEdgeReferenceTriggerDigitalFilterEnable Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgereferencetrigger_digitalfilterenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgereferencetrigger_digitalfilterenable.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeReferenceTrigger.DigitalFilterEnable Property

### AnalogEdgeReferenceTriggerDigitalFilterEnable Property

filter

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool DigitalFilterEnable { get; set; }
```

```text
Public Property DigitalFilterEnable As Boolean
	Get
	Set
```

###### Property Value

Boolean

filter

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AnalogEdgeReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgereferencetrigger_digitalfiltertimebasesource.htm language=enus -->
## TOPIC 00242: AnalogEdgeReferenceTriggerDigitalFilterTimebaseSource Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgereferencetrigger_digitalfiltertimebasesource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgereferencetrigger_digitalfiltertimebasesource.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeReferenceTrigger.DigitalFilterTimebaseSource Property

### AnalogEdgeReferenceTriggerDigitalFilterTimebaseSource Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string DigitalFilterTimebaseSource { get; set; }
```

```text
Public Property DigitalFilterTimebaseSource As String
	Get
	Set
```

###### Property Value

String

terminal

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AnalogEdgeReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgereferencetrigger_source.htm language=enus -->
## TOPIC 00243: AnalogEdgeReferenceTriggerSource Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgereferencetrigger_source.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgereferencetrigger_source.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeReferenceTrigger.Source Property

### AnalogEdgeReferenceTriggerSource Property

virtual channel

terminal

Reference Trigger

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string Source { get; set; }
```

```text
Public Property Source As String
	Get
	Set
```

###### Property Value

String

virtual channel

terminal

Reference Trigger

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

For E Series devices, if you use a channel name, the channel must be the only channel in the task. The only terminal you can use for 
E Series devices is PFI0.

##### See Also

###### Reference

AnalogEdgeReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_digitalfilterenable.htm language=enus -->
## TOPIC 00244: AnalogEdgeStartTriggerDigitalFilterEnable Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_digitalfilterenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_digitalfilterenable.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeStartTrigger.DigitalFilterEnable Property

### AnalogEdgeStartTriggerDigitalFilterEnable Property

filter

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool DigitalFilterEnable { get; set; }
```

```text
Public Property DigitalFilterEnable As Boolean
	Get
	Set
```

###### Property Value

Boolean

filter

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AnalogEdgeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_digitalfilterminimumpulsewidth.htm language=enus -->
## TOPIC 00245: AnalogEdgeStartTriggerDigitalFilterMinimumPulseWidth Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_digitalfilterminimumpulsewidth.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_digitalfilterminimumpulsewidth.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeStartTrigger.DigitalFilterMinimumPulseWidth Property

### AnalogEdgeStartTriggerDigitalFilterMinimumPulseWidth Property

filter

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double DigitalFilterMinimumPulseWidth { get; set; }
```

```text
Public Property DigitalFilterMinimumPulseWidth As Double
	Get
	Set
```

###### Property Value

Double

filter

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AnalogEdgeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_digitalfiltertimebaserate.htm language=enus -->
## TOPIC 00246: AnalogEdgeStartTriggerDigitalFilterTimebaseRate Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_digitalfiltertimebaserate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_digitalfiltertimebaserate.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeStartTrigger.DigitalFilterTimebaseRate Property

### AnalogEdgeStartTriggerDigitalFilterTimebaseRate Property

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double DigitalFilterTimebaseRate { get; set; }
```

```text
Public Property DigitalFilterTimebaseRate As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AnalogEdgeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_digitalfiltertimebasesource.htm language=enus -->
## TOPIC 00247: AnalogEdgeStartTriggerDigitalFilterTimebaseSource Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_digitalfiltertimebasesource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_digitalfiltertimebasesource.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeStartTrigger.DigitalFilterTimebaseSource Property

### AnalogEdgeStartTriggerDigitalFilterTimebaseSource Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string DigitalFilterTimebaseSource { get; set; }
```

```text
Public Property DigitalFilterTimebaseSource As String
	Get
	Set
```

###### Property Value

String

terminal

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AnalogEdgeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_digitalsynchronizationenable.htm language=enus -->
## TOPIC 00248: AnalogEdgeStartTriggerDigitalSynchronizationEnable Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_digitalsynchronizationenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_digitalsynchronizationenable.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeStartTrigger.DigitalSynchronizationEnable Property

### AnalogEdgeStartTriggerDigitalSynchronizationEnable Property

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool DigitalSynchronizationEnable { get; set; }
```

```text
Public Property DigitalSynchronizationEnable As Boolean
	Get
	Set
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AnalogEdgeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_hysteresis.htm language=enus -->
## TOPIC 00249: AnalogEdgeStartTriggerHysteresis Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_hysteresis.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_hysteresis.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeStartTrigger.Hysteresis Property

### AnalogEdgeStartTriggerHysteresis Property

hysteresis level

Slope

Rising

Level

Slope

Falling

Level

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double Hysteresis { get; set; }
```

```text
Public Property Hysteresis As Double
	Get
	Set
```

###### Property Value

Double

hysteresis level

Slope

Rising

Level

Slope

Falling

Level

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AnalogEdgeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_slope.htm language=enus -->
## TOPIC 00250: AnalogEdgeStartTriggerSlope Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_slope.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_slope.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeStartTrigger.Slope Property

### AnalogEdgeStartTriggerSlope Property

Specifies on which slope of the trigger signal to start acquiring or generating samples.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogEdgeStartTriggerSlope Slope { get; set; }
```

```text
Public Property Slope As AnalogEdgeStartTriggerSlope
	Get
	Set
```

###### Property Value

AnalogEdgeStartTriggerSlope

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AnalogEdgeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
