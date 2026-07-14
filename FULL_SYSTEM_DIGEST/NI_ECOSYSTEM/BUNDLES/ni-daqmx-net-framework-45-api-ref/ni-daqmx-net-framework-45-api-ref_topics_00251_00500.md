# NI DOCUMENT BUNDLE: ni-daqmx-net-framework-45-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-net-framework-45-api-ref start=251 end=500 -->
<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_source.htm language=enus -->
## TOPIC 00251: AnalogEdgeStartTriggerSource Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_source.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogedgestarttrigger_source.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeStartTrigger.Source Property

### AnalogEdgeStartTriggerSource Property

virtual channel

terminal

source

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

source

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

For E Series devices, if you use a channel name, the channel must be the first one in the task. The only terminal you can use for 
E Series devices is PFI0.

##### See Also

###### Reference

AnalogEdgeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analoglevelpausetrigger_coupling.htm language=enus -->
## TOPIC 00252: AnalogLevelPauseTriggerCoupling Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analoglevelpausetrigger_coupling.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analoglevelpausetrigger_coupling.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogLevelPauseTrigger.Coupling Property

### AnalogLevelPauseTriggerCoupling Property

terminal

virtual channel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogEdgePauseTriggerCoupling Coupling { get; set; }
```

```text
Public Property Coupling As AnalogEdgePauseTriggerCoupling
	Get
	Set
```

###### Property Value

AnalogEdgePauseTriggerCoupling

terminal

virtual channel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AnalogLevelPauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analoglevelpausetrigger_digitalfilterenable.htm language=enus -->
## TOPIC 00253: AnalogLevelPauseTriggerDigitalFilterEnable Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analoglevelpausetrigger_digitalfilterenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analoglevelpausetrigger_digitalfilterenable.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogLevelPauseTrigger.DigitalFilterEnable Property

### AnalogLevelPauseTriggerDigitalFilterEnable Property

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

AnalogLevelPauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analoglevelpausetrigger_level.htm language=enus -->
## TOPIC 00254: AnalogLevelPauseTriggerLevel Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analoglevelpausetrigger_level.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analoglevelpausetrigger_level.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogLevelPauseTrigger.Level Property

### AnalogLevelPauseTriggerLevel Property

Condition

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double Level { get; set; }
```

```text
Public Property Level As Double
	Get
	Set
```

###### Property Value

Double

Condition

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AnalogLevelPauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analoglevelpausetrigger_source.htm language=enus -->
## TOPIC 00255: AnalogLevelPauseTriggerSource Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analoglevelpausetrigger_source.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analoglevelpausetrigger_source.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogLevelPauseTrigger.Source Property

### AnalogLevelPauseTriggerSource Property

virtual channel

terminal

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

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

For E Series devices, if you use a channel name, the channel must be the only channel in the task. The only terminal you can use for 
E Series devices is PFI0.

##### See Also

###### Reference

AnalogLevelPauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultichannelwriter_synchronizecallbacks.htm language=enus -->
## TOPIC 00256: AnalogMultiChannelWriterSynchronizeCallbacks Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultichannelwriter_synchronizecallbacks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultichannelwriter_synchronizecallbacks.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelWriter.SynchronizeCallbacks Property

### AnalogMultiChannelWriterSynchronizeCallbacks Property

Specifies how events and callback delegates are invoked.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual bool SynchronizeCallbacks { get; set; }
```

```text
Public Overridable Property SynchronizeCallbacks As Boolean
	Get
	Set
```

###### Property Value

Boolean

Send(SendOrPostCallback, Object)

Post(SendOrPostCallback, Object)

###### Implements

##### Remarks

In some cases, callbacks and event handlers are executed in a different thread than the rest of the program. 
Therefore, you must take special care when accessing objects that have thread affinity, such as UI controls, 
from these callbacks and event handlers. For more information, refer to 
Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

##### See Also

###### Reference

AnalogMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Reading and Writing with NI-DAQmx Streams

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultiedgereferencetrigger_couplings.htm language=enus -->
## TOPIC 00257: AnalogMultiEdgeReferenceTriggerCouplings Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultiedgereferencetrigger_couplings.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultiedgereferencetrigger_couplings.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiEdgeReferenceTrigger.Couplings Property

### AnalogMultiEdgeReferenceTriggerCouplings Property

Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogMultiEdgeReferenceTriggerCoupling[] Couplings { get; set; }
```

```text
Public Property Couplings As AnalogMultiEdgeReferenceTriggerCoupling()
	Get
	Set
```

###### Property Value

AnalogMultiEdgeReferenceTriggerCoupling

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

AnalogMultiEdgeReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultiedgereferencetrigger_hystereses.htm language=enus -->
## TOPIC 00258: AnalogMultiEdgeReferenceTriggerHystereses Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultiedgereferencetrigger_hystereses.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultiedgereferencetrigger_hystereses.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiEdgeReferenceTrigger.Hystereses Property

### AnalogMultiEdgeReferenceTriggerHystereses Property

Specifies an array of hysteresis levels in the units of the measurement or generation. If the corresponding element of Ref.AnlgMultiEdge.Slopes is Rising, the trigger does not deassert until the source signal passes below the corresponding element of Ref.AnlgMultiEdge.Lvls minus the hysteresis. If Ref.AnlgEdge.Slope is Falling, the trigger does not deassert until the source signal passes above Ref.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Hystereses { get; set; }
```

```text
Public Property Hystereses As Double()
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

AnalogMultiEdgeReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultiedgereferencetrigger_levels.htm language=enus -->
## TOPIC 00259: AnalogMultiEdgeReferenceTriggerLevels Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultiedgereferencetrigger_levels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultiedgereferencetrigger_levels.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiEdgeReferenceTrigger.Levels Property

### AnalogMultiEdgeReferenceTriggerLevels Property

Specifies an array of thresholds in the units of the measurement or generation to start acquiring or generating samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] Levels { get; set; }
```

```text
Public Property Levels As Double()
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

AnalogMultiEdgeReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultiedgereferencetrigger_slopes.htm language=enus -->
## TOPIC 00260: AnalogMultiEdgeReferenceTriggerSlopes Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultiedgereferencetrigger_slopes.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultiedgereferencetrigger_slopes.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiEdgeReferenceTrigger.Slopes Property

### AnalogMultiEdgeReferenceTriggerSlopes Property

Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogMultiEdgeReferenceTriggerSlope[] Slopes { get; set; }
```

```text
Public Property Slopes As AnalogMultiEdgeReferenceTriggerSlope()
	Get
	Set
```

###### Property Value

AnalogMultiEdgeReferenceTriggerSlope

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

AnalogMultiEdgeReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultiedgestarttrigger_couplings.htm language=enus -->
## TOPIC 00261: AnalogMultiEdgeStartTriggerCouplings Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultiedgestarttrigger_couplings.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogmultiedgestarttrigger_couplings.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiEdgeStartTrigger.Couplings Property

### AnalogMultiEdgeStartTriggerCouplings Property

Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogMultiEdgeStartTriggerCoupling[] Couplings { get; set; }
```

```text
Public Property Couplings As AnalogMultiEdgeStartTriggerCoupling()
	Get
	Set
```

###### Property Value

AnalogMultiEdgeStartTriggerCoupling

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

AnalogMultiEdgeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogunscaledreader_synchronizecallbacks.htm language=enus -->
## TOPIC 00262: AnalogUnscaledReaderSynchronizeCallbacks Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogunscaledreader_synchronizecallbacks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogunscaledreader_synchronizecallbacks.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogUnscaledReader.SynchronizeCallbacks Property

### AnalogUnscaledReaderSynchronizeCallbacks Property

Specifies how events and callback delegates are invoked.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual bool SynchronizeCallbacks { get; set; }
```

```text
Public Overridable Property SynchronizeCallbacks As Boolean
	Get
	Set
```

###### Property Value

Boolean

Send(SendOrPostCallback, Object)

Post(SendOrPostCallback, Object)

###### Implements

##### Remarks

In some cases, callbacks and event handlers are executed in a different thread than the rest of the program. 
Therefore, you must take special care when accessing objects that have thread affinity, such as UI controls, 
from these callbacks and event handlers. For more information, refer to 

Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

##### See Also

###### Reference

AnalogUnscaledReader Class

NationalInstruments.DAQmx Namespace

###### Other Resources

Reading and Writing with NI-DAQmx Streams

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogwindowpausetrigger_condition.htm language=enus -->
## TOPIC 00263: AnalogWindowPauseTriggerCondition Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogwindowpausetrigger_condition.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogwindowpausetrigger_condition.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogWindowPauseTrigger.Condition Property

### AnalogWindowPauseTriggerCondition Property

WindowBottom

WindowTop

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogWindowPauseTriggerCondition Condition { get; set; }
```

```text
Public Property Condition As AnalogWindowPauseTriggerCondition
	Get
	Set
```

###### Property Value

AnalogWindowPauseTriggerCondition

WindowBottom

WindowTop

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AnalogWindowPauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogwindowreferencetrigger_condition.htm language=enus -->
## TOPIC 00264: AnalogWindowReferenceTriggerCondition Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogwindowreferencetrigger_condition.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogwindowreferencetrigger_condition.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogWindowReferenceTrigger.Condition Property

### AnalogWindowReferenceTriggerCondition Property

Reference Trigger

WindowBottom

WindowTop

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AnalogWindowReferenceTriggerCondition Condition { get; set; }
```

```text
Public Property Condition As AnalogWindowReferenceTriggerCondition
	Get
	Set
```

###### Property Value

AnalogWindowReferenceTriggerCondition

Reference Trigger

WindowBottom

WindowTop

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AnalogWindowReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogwindowreferencetrigger_windowbottom.htm language=enus -->
## TOPIC 00265: AnalogWindowReferenceTriggerWindowBottom Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogwindowreferencetrigger_windowbottom.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogwindowreferencetrigger_windowbottom.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogWindowReferenceTrigger.WindowBottom Property

### AnalogWindowReferenceTriggerWindowBottom Property

window

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double WindowBottom { get; set; }
```

```text
Public Property WindowBottom As Double
	Get
	Set
```

###### Property Value

Double

window

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AnalogWindowReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogwindowstarttrigger_digitalfilterenable.htm language=enus -->
## TOPIC 00266: AnalogWindowStartTriggerDigitalFilterEnable Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogwindowstarttrigger_digitalfilterenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogwindowstarttrigger_digitalfilterenable.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogWindowStartTrigger.DigitalFilterEnable Property

### AnalogWindowStartTriggerDigitalFilterEnable Property

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

AnalogWindowStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogwindowstarttrigger_windowtop.htm language=enus -->
## TOPIC 00267: AnalogWindowStartTriggerWindowTop Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogwindowstarttrigger_windowtop.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_analogwindowstarttrigger_windowtop.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogWindowStartTrigger.WindowTop Property

### AnalogWindowStartTriggerWindowTop Property

window

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double WindowTop { get; set; }
```

```text
Public Property WindowTop As Double
	Get
	Set
```

###### Property Value

Double

window

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AnalogWindowStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_dacoffsetvalue.htm language=enus -->
## TOPIC 00268: AOChannelDacOffsetValue Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_dacoffsetvalue.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_dacoffsetvalue.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AOChannel.DacOffsetValue Property

### AOChannelDacOffsetValue Property

Specifies in volts the value of the DAC offset voltage. To achieve best accuracy, the DAC offset value should be hand calibrated.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double DacOffsetValue { get; set; }
```

```text
Public Property DacOffsetValue As Double
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

AOChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_dacrangehigh.htm language=enus -->
## TOPIC 00269: AOChannelDacRangeHigh Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_dacrangehigh.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_dacrangehigh.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AOChannel.DacRangeHigh Property

### AOChannelDacRangeHigh Property

Specifies the upper limit of the output range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double DacRangeHigh { get; set; }
```

```text
Public Property DacRangeHigh As Double
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

AOChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_datatransfermechanism.htm language=enus -->
## TOPIC 00270: AOChannelDataTransferMechanism Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_datatransfermechanism.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_datatransfermechanism.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AOChannel.DataTransferMechanism Property

### AOChannelDataTransferMechanism Property

Specifies the data transfer mode for the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AODataTransferMechanism DataTransferMechanism { get; set; }
```

```text
Public Property DataTransferMechanism As AODataTransferMechanism
	Get
	Set
```

###### Property Value

AODataTransferMechanism

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AOChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_filterdelay.htm language=enus -->
## TOPIC 00271: AOChannelFilterDelay Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_filterdelay.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_filterdelay.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AOChannel.FilterDelay Property

### AOChannelFilterDelay Property

FilterDelayUnits

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double FilterDelay { get; set; }
```

```text
Public Property FilterDelay As Double
	Get
	Set
```

###### Property Value

Double

FilterDelayUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AOChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_filterdelayadjustment.htm language=enus -->
## TOPIC 00272: AOChannelFilterDelayAdjustment Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_filterdelayadjustment.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_filterdelayadjustment.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AOChannel.FilterDelayAdjustment Property

### AOChannelFilterDelayAdjustment Property

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

FilterDelay

FilterDelayUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AOChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_filterdelayunits.htm language=enus -->
## TOPIC 00273: AOChannelFilterDelayUnits Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_filterdelayunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_filterdelayunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AOChannel.FilterDelayUnits Property

### AOChannelFilterDelayUnits Property

FilterDelay

FilterDelayAdjustment

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AOFilterDelayUnits FilterDelayUnits { get; set; }
```

```text
Public Property FilterDelayUnits As AOFilterDelayUnits
	Get
	Set
```

###### Property Value

AOFilterDelayUnits

FilterDelay

FilterDelayAdjustment

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AOChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_functiongenerationsquaredutycycle.htm language=enus -->
## TOPIC 00274: AOChannelFunctionGenerationSquareDutyCycle Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_functiongenerationsquaredutycycle.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_functiongenerationsquaredutycycle.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AOChannel.FunctionGenerationSquareDutyCycle Property

### AOChannelFunctionGenerationSquareDutyCycle Property

Specifies the square wave duty cycle of the waveform to generate.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double FunctionGenerationSquareDutyCycle { get; set; }
```

```text
Public Property FunctionGenerationSquareDutyCycle As Double
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

AOChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_gain.htm language=enus -->
## TOPIC 00275: AOChannelGain Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_gain.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannel_gain.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AOChannel.Gain Property

### AOChannelGain Property

Specifies in decibels the gain factor to apply to the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double Gain { get; set; }
```

```text
Public Property Gain As Double
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

AOChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannelcollection_all.htm language=enus -->
## TOPIC 00276: AOChannelCollectionAll Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannelcollection_all.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_aochannelcollection_all.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AOChannelCollection.All Property

### AOChannelCollectionAll Property

AOChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual AOChannel All { get; }
```

```text
Public Overridable ReadOnly Property All As AOChannel
	Get
```

###### Property Value

AOChannel

AOChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

AOChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_countedgescountdirectiondigitalfilterenable.htm language=enus -->
## TOPIC 00277: CIChannelCountEdgesCountDirectionDigitalFilterEnable Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_countedgescountdirectiondigitalfilterenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_countedgescountdirectiondigitalfilterenable.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.CountEdgesCountDirectionDigitalFilterEnable Property

### CIChannelCountEdgesCountDirectionDigitalFilterEnable Property

filter

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool CountEdgesCountDirectionDigitalFilterEnable { get; set; }
```

```text
Public Property CountEdgesCountDirectionDigitalFilterEnable As Boolean
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

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_countedgescountdirectionlogiclevelbehavior.htm language=enus -->
## TOPIC 00278: CIChannelCountEdgesCountDirectionLogicLevelBehavior Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_countedgescountdirectionlogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_countedgescountdirectionlogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.CountEdgesCountDirectionLogicLevelBehavior Property

### CIChannelCountEdgesCountDirectionLogicLevelBehavior Property

Specifies the logic level behavior on the count reset line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CICountEdgesCountDirectionLogicLevelBehavior CountEdgesCountDirectionLogicLevelBehavior { get; set; }
```

```text
Public Property CountEdgesCountDirectionLogicLevelBehavior As CICountEdgesCountDirectionLogicLevelBehavior
	Get
	Set
```

###### Property Value

CICountEdgesCountDirectionLogicLevelBehavior

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_countedgescountresetlogiclevelbehavior.htm language=enus -->
## TOPIC 00279: CIChannelCountEdgesCountResetLogicLevelBehavior Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_countedgescountresetlogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_countedgescountresetlogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.CountEdgesCountResetLogicLevelBehavior Property

### CIChannelCountEdgesCountResetLogicLevelBehavior Property

Specifies the logic level behavior on the count reset line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CICountEdgesCountResetLogicLevelBehavior CountEdgesCountResetLogicLevelBehavior { get; set; }
```

```text
Public Property CountEdgesCountResetLogicLevelBehavior As CICountEdgesCountResetLogicLevelBehavior
	Get
	Set
```

###### Property Value

CICountEdgesCountResetLogicLevelBehavior

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_dutycycleterminal.htm language=enus -->
## TOPIC 00280: CIChannelDutyCycleTerminal Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_dutycycleterminal.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_dutycycleterminal.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.DutyCycleTerminal Property

### CIChannelDutyCycleTerminal Property

Specifies the input terminal of the signal to measure.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string DutyCycleTerminal { get; set; }
```

```text
Public Property DutyCycleTerminal As String
	Get
	Set
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderainputlogiclevelbehavior.htm language=enus -->
## TOPIC 00281: CIChannelEncoderAInputLogicLevelBehavior Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderainputlogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderainputlogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.EncoderAInputLogicLevelBehavior Property

### CIChannelEncoderAInputLogicLevelBehavior Property

Specifies the logic level behavior on the input line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIEncoderAInputLogicLevelBehavior EncoderAInputLogicLevelBehavior { get; set; }
```

```text
Public Property EncoderAInputLogicLevelBehavior As CIEncoderAInputLogicLevelBehavior
	Get
	Set
```

###### Property Value

CIEncoderAInputLogicLevelBehavior

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderainputterminalconfiguration.htm language=enus -->
## TOPIC 00282: CIChannelEncoderAInputTerminalConfiguration Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderainputterminalconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderainputterminalconfiguration.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.EncoderAInputTerminalConfiguration Property

### CIChannelEncoderAInputTerminalConfiguration Property

Specifies the input terminal configuration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIEncoderAInputTerminalConfiguration EncoderAInputTerminalConfiguration { get; set; }
```

```text
Public Property EncoderAInputTerminalConfiguration As CIEncoderAInputTerminalConfiguration
	Get
	Set
```

###### Property Value

CIEncoderAInputTerminalConfiguration

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderbinputdigitalfiltertimebasesource.htm language=enus -->
## TOPIC 00283: CIChannelEncoderBInputDigitalFilterTimebaseSource Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderbinputdigitalfiltertimebasesource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderbinputdigitalfiltertimebasesource.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.EncoderBInputDigitalFilterTimebaseSource Property

### CIChannelEncoderBInputDigitalFilterTimebaseSource Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string EncoderBInputDigitalFilterTimebaseSource { get; set; }
```

```text
Public Property EncoderBInputDigitalFilterTimebaseSource As String
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

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderbinputdigitalsynchronizationenable.htm language=enus -->
## TOPIC 00284: CIChannelEncoderBInputDigitalSynchronizationEnable Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderbinputdigitalsynchronizationenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderbinputdigitalsynchronizationenable.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.EncoderBInputDigitalSynchronizationEnable Property

### CIChannelEncoderBInputDigitalSynchronizationEnable Property

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool EncoderBInputDigitalSynchronizationEnable { get; set; }
```

```text
Public Property EncoderBInputDigitalSynchronizationEnable As Boolean
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

This property does not affect the minimum pulse width recognized by the device, 
but setting this property to does limit the speed at which the device recognizes transitions 
to less than the frequency of the internal timebase.

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderbinputlogiclevelbehavior.htm language=enus -->
## TOPIC 00285: CIChannelEncoderBInputLogicLevelBehavior Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderbinputlogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderbinputlogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.EncoderBInputLogicLevelBehavior Property

### CIChannelEncoderBInputLogicLevelBehavior Property

Specifies the logic level behavior on the input line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIEncoderBInputLogicLevelBehavior EncoderBInputLogicLevelBehavior { get; set; }
```

```text
Public Property EncoderBInputLogicLevelBehavior As CIEncoderBInputLogicLevelBehavior
	Get
	Set
```

###### Property Value

CIEncoderBInputLogicLevelBehavior

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderzindexvalue.htm language=enus -->
## TOPIC 00286: CIChannelEncoderZIndexValue Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderzindexvalue.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderzindexvalue.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.EncoderZIndexValue Property

### CIChannelEncoderZIndexValue Property

EncoderZIndexPhase

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double EncoderZIndexValue { get; set; }
```

```text
Public Property EncoderZIndexValue As Double
	Get
	Set
```

###### Property Value

Double

EncoderZIndexPhase

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderzinputdigitalfiltertimebasesource.htm language=enus -->
## TOPIC 00287: CIChannelEncoderZInputDigitalFilterTimebaseSource Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderzinputdigitalfiltertimebasesource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_encoderzinputdigitalfiltertimebasesource.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.EncoderZInputDigitalFilterTimebaseSource Property

### CIChannelEncoderZInputDigitalFilterTimebaseSource Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string EncoderZInputDigitalFilterTimebaseSource { get; set; }
```

```text
Public Property EncoderZInputDigitalFilterTimebaseSource As String
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

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_filterorder.htm language=enus -->
## TOPIC 00288: CIChannelFilterOrder Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_filterorder.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_filterorder.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.FilterOrder Property

### CIChannelFilterOrder Property

Specifies the corresponding filter order and defines the slope of the filter response.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long FilterOrder { get; set; }
```

```text
Public Property FilterOrder As Long
	Get
	Set
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_frequencyhysteresis.htm language=enus -->
## TOPIC 00289: CIChannelFrequencyHysteresis Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_frequencyhysteresis.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_frequencyhysteresis.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.FrequencyHysteresis Property

### CIChannelFrequencyHysteresis Property

FrequencyThresholdVoltage

FrequencyStartingEdge

FrequencyThresholdVoltage

FrequencyThresholdVoltage

FrequencyStartingEdge

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

FrequencyStartingEdge

FrequencyThresholdVoltage

FrequencyThresholdVoltage

FrequencyStartingEdge

FrequencyThresholdVoltage

FrequencyThresholdVoltage

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_pulseticksterminal.htm language=enus -->
## TOPIC 00290: CIChannelPulseTicksTerminal Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_pulseticksterminal.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_pulseticksterminal.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.PulseTicksTerminal Property

### CIChannelPulseTicksTerminal Property

input terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string PulseTicksTerminal { get; set; }
```

```text
Public Property PulseTicksTerminal As String
	Get
	Set
```

###### Property Value

String

input terminal

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_pulsetimedigitalfilterminimumpulsewidth.htm language=enus -->
## TOPIC 00291: CIChannelPulseTimeDigitalFilterMinimumPulseWidth Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_pulsetimedigitalfilterminimumpulsewidth.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_pulsetimedigitalfilterminimumpulsewidth.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.PulseTimeDigitalFilterMinimumPulseWidth Property

### CIChannelPulseTimeDigitalFilterMinimumPulseWidth Property

filter

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double PulseTimeDigitalFilterMinimumPulseWidth { get; set; }
```

```text
Public Property PulseTimeDigitalFilterMinimumPulseWidth As Double
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

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_pulsetimedigitalfiltertimebaserate.htm language=enus -->
## TOPIC 00292: CIChannelPulseTimeDigitalFilterTimebaseRate Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_pulsetimedigitalfiltertimebaserate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_pulsetimedigitalfiltertimebaserate.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.PulseTimeDigitalFilterTimebaseRate Property

### CIChannelPulseTimeDigitalFilterTimebaseRate Property

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double PulseTimeDigitalFilterTimebaseRate { get; set; }
```

```text
Public Property PulseTimeDigitalFilterTimebaseRate As Double
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

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_pulsewidthlogiclevelbehavior.htm language=enus -->
## TOPIC 00293: CIChannelPulseWidthLogicLevelBehavior Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_pulsewidthlogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_pulsewidthlogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.PulseWidthLogicLevelBehavior Property

### CIChannelPulseWidthLogicLevelBehavior Property

Specifies the logic level behavior on the input line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIPulseWidthLogicLevelBehavior PulseWidthLogicLevelBehavior { get; set; }
```

```text
Public Property PulseWidthLogicLevelBehavior As CIPulseWidthLogicLevelBehavior
	Get
	Set
```

###### Property Value

CIPulseWidthLogicLevelBehavior

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationfirstedgedigitalfiltertimebaserate.htm language=enus -->
## TOPIC 00294: CIChannelTwoEdgeSeparationFirstEdgeDigitalFilterTimebaseRate Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationfirstedgedigitalfiltertimebaserate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationfirstedgedigitalfiltertimebaserate.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.TwoEdgeSeparationFirstEdgeDigitalFilterTimebaseRate Property

### CIChannelTwoEdgeSeparationFirstEdgeDigitalFilterTimebaseRate Property

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double TwoEdgeSeparationFirstEdgeDigitalFilterTimebaseRate { get; set; }
```

```text
Public Property TwoEdgeSeparationFirstEdgeDigitalFilterTimebaseRate As Double
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

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationfirstedgedigitalsynchronizationenable.htm language=enus -->
## TOPIC 00295: CIChannelTwoEdgeSeparationFirstEdgeDigitalSynchronizationEnable Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationfirstedgedigitalsynchronizationenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationfirstedgedigitalsynchronizationenable.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.TwoEdgeSeparationFirstEdgeDigitalSynchronizationEnable Property

### CIChannelTwoEdgeSeparationFirstEdgeDigitalSynchronizationEnable Property

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool TwoEdgeSeparationFirstEdgeDigitalSynchronizationEnable { get; set; }
```

```text
Public Property TwoEdgeSeparationFirstEdgeDigitalSynchronizationEnable As Boolean
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

This property does not affect the minimum pulse width recognized by the device, 
but setting this property to does limit the speed at which the device recognizes transitions 
to less than the frequency of the internal timebase.

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationfirstterminal.htm language=enus -->
## TOPIC 00296: CIChannelTwoEdgeSeparationFirstTerminal Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationfirstterminal.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationfirstterminal.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.TwoEdgeSeparationFirstTerminal Property

### CIChannelTwoEdgeSeparationFirstTerminal Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string TwoEdgeSeparationFirstTerminal { get; set; }
```

```text
Public Property TwoEdgeSeparationFirstTerminal As String
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

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationsecondedgedigitalfilterenable.htm language=enus -->
## TOPIC 00297: CIChannelTwoEdgeSeparationSecondEdgeDigitalFilterEnable Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationsecondedgedigitalfilterenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationsecondedgedigitalfilterenable.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.TwoEdgeSeparationSecondEdgeDigitalFilterEnable Property

### CIChannelTwoEdgeSeparationSecondEdgeDigitalFilterEnable Property

filter

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool TwoEdgeSeparationSecondEdgeDigitalFilterEnable { get; set; }
```

```text
Public Property TwoEdgeSeparationSecondEdgeDigitalFilterEnable As Boolean
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

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationsecondedgedigitalfiltertimebasesource.htm language=enus -->
## TOPIC 00298: CIChannelTwoEdgeSeparationSecondEdgeDigitalFilterTimebaseSource Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationsecondedgedigitalfiltertimebasesource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationsecondedgedigitalfiltertimebasesource.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.TwoEdgeSeparationSecondEdgeDigitalFilterTimebaseSource Property

### CIChannelTwoEdgeSeparationSecondEdgeDigitalFilterTimebaseSource Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string TwoEdgeSeparationSecondEdgeDigitalFilterTimebaseSource { get; set; }
```

```text
Public Property TwoEdgeSeparationSecondEdgeDigitalFilterTimebaseSource As String
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

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationsecondedgedigitalsynchronizationenable.htm language=enus -->
## TOPIC 00299: CIChannelTwoEdgeSeparationSecondEdgeDigitalSynchronizationEnable Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationsecondedgedigitalsynchronizationenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationsecondedgedigitalsynchronizationenable.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.TwoEdgeSeparationSecondEdgeDigitalSynchronizationEnable Property

### CIChannelTwoEdgeSeparationSecondEdgeDigitalSynchronizationEnable Property

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool TwoEdgeSeparationSecondEdgeDigitalSynchronizationEnable { get; set; }
```

```text
Public Property TwoEdgeSeparationSecondEdgeDigitalSynchronizationEnable As Boolean
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

This property does not affect the minimum pulse width recognized by the device, 
but setting this property to does limit the speed at which the device recognizes transitions 
to less than the frequency of the internal timebase.

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationunits.htm language=enus -->
## TOPIC 00300: CIChannelTwoEdgeSeparationUnits Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_twoedgeseparationunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.TwoEdgeSeparationUnits Property

### CIChannelTwoEdgeSeparationUnits Property

Specifies the units to use to return two-edge separation measurements from the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CITwoEdgeSeparationUnits TwoEdgeSeparationUnits { get; set; }
```

```text
Public Property TwoEdgeSeparationUnits As CITwoEdgeSeparationUnits
	Get
	Set
```

###### Property Value

CITwoEdgeSeparationUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_velocityainputdigitalfilterenable.htm language=enus -->
## TOPIC 00301: CIChannelVelocityAInputDigitalFilterEnable Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_velocityainputdigitalfilterenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_velocityainputdigitalfilterenable.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.VelocityAInputDigitalFilterEnable Property

### CIChannelVelocityAInputDigitalFilterEnable Property

Specifies whether to apply the pulse width filter to the signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool VelocityAInputDigitalFilterEnable { get; set; }
```

```text
Public Property VelocityAInputDigitalFilterEnable As Boolean
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

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_velocityainputdigitalfiltertimebaserate.htm language=enus -->
## TOPIC 00302: CIChannelVelocityAInputDigitalFilterTimebaseRate Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_velocityainputdigitalfiltertimebaserate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_velocityainputdigitalfiltertimebaserate.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.VelocityAInputDigitalFilterTimebaseRate Property

### CIChannelVelocityAInputDigitalFilterTimebaseRate Property

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double VelocityAInputDigitalFilterTimebaseRate { get; set; }
```

```text
Public Property VelocityAInputDigitalFilterTimebaseRate As Double
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

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_velocityainputterminalconfiguration.htm language=enus -->
## TOPIC 00303: CIChannelVelocityAInputTerminalConfiguration Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_velocityainputterminalconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannel_velocityainputterminalconfiguration.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel.VelocityAInputTerminalConfiguration Property

### CIChannelVelocityAInputTerminalConfiguration Property

Specifies the input terminal configuration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIVelocityAInputTerminalConfiguration VelocityAInputTerminalConfiguration { get; set; }
```

```text
Public Property VelocityAInputTerminalConfiguration As CIVelocityAInputTerminalConfiguration
	Get
	Set
```

###### Property Value

CIVelocityAInputTerminalConfiguration

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannelcollection_item.htm language=enus -->
## TOPIC 00304: CIChannelCollectionItem Property (Int64)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannelcollection_item.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannelcollection_item.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannelCollection.Item Property (Int64)

### CIChannelCollectionItem Property (Int64)

CIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual CIChannel this[
	long index
] { get; }
```

```text
Public Overridable ReadOnly Default Property Item ( 
	index As Long
) As CIChannel
	Get
```

###### Parameters

- **index**
  - Type: SystemInt64The index of the channel to get.

###### Property Value

CIChannel

CIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

CIChannelCollection Class

Item Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Channels

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannelcollection_item_1.htm language=enus -->
## TOPIC 00305: CIChannelCollectionItem Property (String)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannelcollection_item_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cichannelcollection_item_1.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannelCollection.Item Property (String)

### CIChannelCollectionItem Property (String)

CIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual CIChannel this[
	string virtualChannelName
] { get; }
```

```text
Public Overridable ReadOnly Default Property Item ( 
	virtualChannelName As String
) As CIChannel
	Get
```

###### Parameters

- **virtualChannelName**
  - Type: SystemStringOne or more virtual channel names that the retrieved CIChannel operates on.

###### Property Value

CIChannel

CIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

virtualChannelName

Channels

##### See Also

###### Reference

CIChannelCollection Class

Item Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Channels

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cidataticks_lowticksuint32.htm language=enus -->
## TOPIC 00306: CIDataTicksLowTicksUInt32 Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cidataticks_lowticksuint32.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_cidataticks_lowticksuint32.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataTicks.LowTicksUInt32 Property

### CIDataTicksLowTicksUInt32 Property

Gets or sets the number of timebase ticks the pulse is low.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public uint LowTicksUInt32 { get; set; }
```

```text
Public Property LowTicksUInt32 As UInteger
	Get
	Set
```

###### Property Value

UInt32

##### See Also

###### Reference

CIDataTicks Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_commonmoderangeerrorchannels.htm language=enus -->
## TOPIC 00307: DaqStreamCommonModeRangeErrorChannels Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_commonmoderangeerrorchannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_commonmoderangeerrorchannels.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.CommonModeRangeErrorChannels Property

### DaqStreamCommonModeRangeErrorChannels Property

list of names

CommonModeRangeErrorChannelsExist

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] CommonModeRangeErrorChannels { get; }
```

```text
Public ReadOnly Property CommonModeRangeErrorChannels As String()
	Get
```

###### Property Value

String

list of names

CommonModeRangeErrorChannelsExist

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_currentwriteposition.htm language=enus -->
## TOPIC 00308: DaqStreamCurrentWritePosition Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_currentwriteposition.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_currentwriteposition.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.CurrentWritePosition Property

### DaqStreamCurrentWritePosition Property

Indicates the position in the buffer of the next sample to generate. This value is identical for all channels in the task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long CurrentWritePosition { get; }
```

```text
Public ReadOnly Property CurrentWritePosition As Long
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_loggingfilepath.htm language=enus -->
## TOPIC 00309: DaqStreamLoggingFilePath Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_loggingfilepath.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_loggingfilepath.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.LoggingFilePath Property

### DaqStreamLoggingFilePath Property

log

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string LoggingFilePath { get; set; }
```

```text
Public Property LoggingFilePath As String
	Get
	Set
```

###### Property Value

String

log

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_loggingsamplesperfile.htm language=enus -->
## TOPIC 00310: DaqStreamLoggingSamplesPerFile Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_loggingsamplesperfile.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_loggingsamplesperfile.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.LoggingSamplesPerFile Property

### DaqStreamLoggingSamplesPerFile Property

LoggingFilePath

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long LoggingSamplesPerFile { get; set; }
```

```text
Public Property LoggingSamplesPerFile As Long
	Get
	Set
```

###### Property Value

Int64

LoggingFilePath

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_numberofinputchannels.htm language=enus -->
## TOPIC 00311: DaqStreamNumberOfInputChannels Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_numberofinputchannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_numberofinputchannels.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.NumberOfInputChannels Property

### DaqStreamNumberOfInputChannels Property

ChannelsToRead

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long NumberOfInputChannels { get; }
```

```text
Public ReadOnly Property NumberOfInputChannels As Long
	Get
```

###### Property Value

Int64

ChannelsToRead

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_overloadedinputchannels.htm language=enus -->
## TOPIC 00312: DaqStreamOverloadedInputChannels Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_overloadedinputchannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_overloadedinputchannels.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.OverloadedInputChannels Property

### DaqStreamOverloadedInputChannels Property

list of names

overloaded

OverloadedInputChannelsExist

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] OverloadedInputChannels { get; }
```

```text
Public ReadOnly Property OverloadedInputChannels As String()
	Get
```

###### Property Value

String

list of names

overloaded

OverloadedInputChannelsExist

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_overloadedinputchannelsexist.htm language=enus -->
## TOPIC 00313: DaqStreamOverloadedInputChannelsExist Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_overloadedinputchannelsexist.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_overloadedinputchannelsexist.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.OverloadedInputChannelsExist Property

### DaqStreamOverloadedInputChannelsExist Property

overload

OverloadedInputChannels

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool OverloadedInputChannelsExist { get; }
```

```text
Public ReadOnly Property OverloadedInputChannelsExist As Boolean
	Get
```

###### Property Value

Boolean

overload

OverloadedInputChannels

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readoffset.htm language=enus -->
## TOPIC 00314: DaqStreamReadOffset Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readoffset.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readoffset.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.ReadOffset Property

### DaqStreamReadOffset Property

ReadRelativeTo

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public int ReadOffset { get; set; }
```

```text
Public Property ReadOffset As Integer
	Get
	Set
```

###### Property Value

Int32

ReadRelativeTo

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readovercurrentchannelsexist.htm language=enus -->
## TOPIC 00315: DaqStreamReadOvercurrentChannelsExist Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readovercurrentchannelsexist.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readovercurrentchannelsexist.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.ReadOvercurrentChannelsExist Property

### DaqStreamReadOvercurrentChannelsExist Property

overcurrent condition

ReadOvercurrentChannels

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool ReadOvercurrentChannelsExist { get; }
```

```text
Public ReadOnly Property ReadOvercurrentChannelsExist As Boolean
	Get
```

###### Property Value

Boolean

overcurrent condition

ReadOvercurrentChannels

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readoverwritemode.htm language=enus -->
## TOPIC 00316: DaqStreamReadOverwriteMode Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readoverwritemode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readoverwritemode.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.ReadOverwriteMode Property

### DaqStreamReadOverwriteMode Property

Specifies whether to overwrite samples in the buffer that you have not yet read.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public ReadOverwriteMode ReadOverwriteMode { get; set; }
```

```text
Public Property ReadOverwriteMode As ReadOverwriteMode
	Get
	Set
```

###### Property Value

ReadOverwriteMode

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readsleeptime.htm language=enus -->
## TOPIC 00317: DaqStreamReadSleepTime Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readsleeptime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readsleeptime.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.ReadSleepTime Property

### DaqStreamReadSleepTime Property

ReadWaitMode

Sleep

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double ReadSleepTime { get; set; }
```

```text
Public Property ReadSleepTime As Double
	Get
	Set
```

###### Property Value

Double

ReadWaitMode

Sleep

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readsynchronizationunlockedchannels.htm language=enus -->
## TOPIC 00318: DaqStreamReadSynchronizationUnlockedChannels Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readsynchronizationunlockedchannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readsynchronizationunlockedchannels.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.ReadSynchronizationUnlockedChannels Property

### DaqStreamReadSynchronizationUnlockedChannels Property

Indicates the channels from devices in an unlocked target.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] ReadSynchronizationUnlockedChannels { get; }
```

```text
Public ReadOnly Property ReadSynchronizationUnlockedChannels As String()
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readsynchronizationunlockedchannelsexist.htm language=enus -->
## TOPIC 00319: DaqStreamReadSynchronizationUnlockedChannelsExist Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readsynchronizationunlockedchannelsexist.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_daqstream_readsynchronizationunlockedchannelsexist.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream.ReadSynchronizationUnlockedChannelsExist Property

### DaqStreamReadSynchronizationUnlockedChannelsExist Property

Indicates whether the target is currently locked to the grand master. Devices may report PLL Unlock either during acquisition or after acquisition.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool ReadSynchronizationUnlockedChannelsExist { get; }
```

```text
Public ReadOnly Property ReadSynchronizationUnlockedChannelsExist As Boolean
	Get
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aibridgeranges.htm language=enus -->
## TOPIC 00320: DeviceAIBridgeRanges Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aibridgeranges.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aibridgeranges.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AIBridgeRanges Property

### DeviceAIBridgeRanges Property

Indicates pairs of input voltage ratio ranges, in volts per volt, supported by devices that acquire using ratiometric measurements. Each pair consists of the low value followed by the high value.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] AIBridgeRanges { get; }
```

```text
Public ReadOnly Property AIBridgeRanges As Double()
	Get
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aicurrentranges.htm language=enus -->
## TOPIC 00321: DeviceAICurrentRanges Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aicurrentranges.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aicurrentranges.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AICurrentRanges Property

### DeviceAICurrentRanges Property

Indicates the pairs of current input ranges supported by this device. Each pair consists of the low value, followed by the high value.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] AICurrentRanges { get; }
```

```text
Public ReadOnly Property AICurrentRanges As Double()
	Get
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aifrequencyranges.htm language=enus -->
## TOPIC 00322: DeviceAIFrequencyRanges Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aifrequencyranges.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aifrequencyranges.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AIFrequencyRanges Property

### DeviceAIFrequencyRanges Property

Indicates the pairs of frequency input ranges supported by this device. Each pair consists of the low value, followed by the high value.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] AIFrequencyRanges { get; }
```

```text
Public ReadOnly Property AIFrequencyRanges As Double()
	Get
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aigains.htm language=enus -->
## TOPIC 00323: DeviceAIGains Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aigains.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aigains.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AIGains Property

### DeviceAIGains Property

Indicates the input gain settings supported by this device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] AIGains { get; }
```

```text
Public ReadOnly Property AIGains As Double()
	Get
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aimaximummultichannelrate.htm language=enus -->
## TOPIC 00324: DeviceAIMaximumMultiChannelRate Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aimaximummultichannelrate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aimaximummultichannelrate.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AIMaximumMultiChannelRate Property

### DeviceAIMaximumMultiChannelRate Property

AIMaximumSingleChannelRate

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double AIMaximumMultiChannelRate { get; }
```

```text
Public ReadOnly Property AIMaximumMultiChannelRate As Double
	Get
```

###### Property Value

Double

AIMaximumSingleChannelRate

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aiminimumrate.htm language=enus -->
## TOPIC 00325: DeviceAIMinimumRate Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aiminimumrate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aiminimumrate.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AIMinimumRate Property

### DeviceAIMinimumRate Property

Indicates the minimum rate for an analog input task on this device. NI-DAQmx returns a warning or error if you attempt to sample at a slower rate.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double AIMinimumRate { get; }
```

```text
Public ReadOnly Property AIMinimumRate As Double
	Get
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aocurrentranges.htm language=enus -->
## TOPIC 00326: DeviceAOCurrentRanges Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aocurrentranges.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aocurrentranges.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AOCurrentRanges Property

### DeviceAOCurrentRanges Property

Indicates pairs of output current ranges supported by this device. Each pair consists of the low value, followed by the high value.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] AOCurrentRanges { get; }
```

```text
Public ReadOnly Property AOCurrentRanges As Double()
	Get
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aominimumrate.htm language=enus -->
## TOPIC 00327: DeviceAOMinimumRate Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aominimumrate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aominimumrate.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AOMinimumRate Property

### DeviceAOMinimumRate Property

Indicates the minimum analog output rate of the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double AOMinimumRate { get; }
```

```text
Public ReadOnly Property AOMinimumRate As Double
	Get
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aonumberofsynchronizationpulsesources.htm language=enus -->
## TOPIC 00328: DeviceAONumberOfSynchronizationPulseSources Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aonumberofsynchronizationpulsesources.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aonumberofsynchronizationpulsesources.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AONumberOfSynchronizationPulseSources Property

### DeviceAONumberOfSynchronizationPulseSources Property

Indicates the number of Analog Output synchronization pulse sources supported by the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long AONumberOfSynchronizationPulseSources { get; }
```

```text
Public ReadOnly Property AONumberOfSynchronizationPulseSources As Long
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aophysicalchannels.htm language=enus -->
## TOPIC 00329: DeviceAOPhysicalChannels Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aophysicalchannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aophysicalchannels.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AOPhysicalChannels Property

### DeviceAOPhysicalChannels Property

Indicates an array containing the names of the analog output physical channels available on the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string[] AOPhysicalChannels { get; }
```

```text
Public ReadOnly Property AOPhysicalChannels As String()
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aovoltageranges.htm language=enus -->
## TOPIC 00330: DeviceAOVoltageRanges Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aovoltageranges.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_aovoltageranges.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.AOVoltageRanges Property

### DeviceAOVoltageRanges Property

Indicates pairs of output voltage ranges supported by this device. Each pair consists of the low value, followed by the high value.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] AOVoltageRanges { get; }
```

```text
Public ReadOnly Property AOVoltageRanges As Double()
	Get
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_cisupportedmeasurementtypes.htm language=enus -->
## TOPIC 00331: DeviceCISupportedMeasurementTypes Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_cisupportedmeasurementtypes.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_cisupportedmeasurementtypes.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.CISupportedMeasurementTypes Property

### DeviceCISupportedMeasurementTypes Property

Gets the measurement types supported by the physical channels of the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CIMeasurementType[] CISupportedMeasurementTypes { get; }
```

```text
Public ReadOnly Property CISupportedMeasurementTypes As CIMeasurementType()
	Get
```

###### Property Value

CIMeasurementType

CIMeasurementType

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_compactdaqchassisdevicename.htm language=enus -->
## TOPIC 00332: DeviceCompactDaqChassisDeviceName Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_compactdaqchassisdevicename.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_compactdaqchassisdevicename.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.CompactDaqChassisDeviceName Property

### DeviceCompactDaqChassisDeviceName Property

Indicates the name of the CompactDAQ chassis that contains this module.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string CompactDaqChassisDeviceName { get; }
```

```text
Public ReadOnly Property CompactDaqChassisDeviceName As String
	Get
```

###### Property Value

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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_lowpasscutofffrequenciesdiscretevalues.htm language=enus -->
## TOPIC 00333: DeviceLowpassCutoffFrequenciesDiscreteValues Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_lowpasscutofffrequenciesdiscretevalues.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_lowpasscutofffrequenciesdiscretevalues.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.LowpassCutoffFrequenciesDiscreteValues Property

### DeviceLowpassCutoffFrequenciesDiscreteValues Property

LowpassCutoffFrequenciesRangeValues

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] LowpassCutoffFrequenciesDiscreteValues { get; }
```

```text
Public ReadOnly Property LowpassCutoffFrequenciesDiscreteValues As Double()
	Get
```

###### Property Value

Double

LowpassCutoffFrequenciesRangeValues

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_pxichassisnumber.htm language=enus -->
## TOPIC 00334: DevicePxiChassisNumber Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_pxichassisnumber.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_pxichassisnumber.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.PxiChassisNumber Property

### DevicePxiChassisNumber Property

Indicates the PXI chassis number of the device, as identified in MAX.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long PxiChassisNumber { get; }
```

```text
Public ReadOnly Property PxiChassisNumber As Long
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_pxislotnumber.htm language=enus -->
## TOPIC 00335: DevicePxiSlotNumber Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_pxislotnumber.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_pxislotnumber.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.PxiSlotNumber Property

### DevicePxiSlotNumber Property

Indicates the PXI slot number of the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long PxiSlotNumber { get; }
```

```text
Public ReadOnly Property PxiSlotNumber As Long
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_recommendedaccessoryconnectioncountlimit.htm language=enus -->
## TOPIC 00336: DeviceRecommendedAccessoryConnectionCountLimit Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_recommendedaccessoryconnectioncountlimit.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_recommendedaccessoryconnectioncountlimit.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.RecommendedAccessoryConnectionCountLimit Property

### DeviceRecommendedAccessoryConnectionCountLimit Property

Indicates the recommended connection count limit for an accessory. If the accessory connection count exceeds this limit, the accessory could require maintenance.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long RecommendedAccessoryConnectionCountLimit { get; }
```

```text
Public ReadOnly Property RecommendedAccessoryConnectionCountLimit As Long
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_selfcalibrationdatetime.htm language=enus -->
## TOPIC 00337: DeviceSelfCalibrationDateTime Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_selfcalibrationdatetime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_selfcalibrationdatetime.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.SelfCalibrationDateTime Property

### DeviceSelfCalibrationDateTime Property

Gets the last date and time that the device underwent a self-calibration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DateTime SelfCalibrationDateTime { get; }
```

```text
Public ReadOnly Property SelfCalibrationDateTime As DateTime
	Get
```

###### Property Value

DateTime

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_timetriggercount.htm language=enus -->
## TOPIC 00338: DeviceTimeTriggerCount Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_timetriggercount.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_device_timetriggercount.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Device.TimeTriggerCount Property

### DeviceTimeTriggerCount Property

Indicates the number of time triggers available on the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long TimeTriggerCount { get; }
```

```text
Public ReadOnly Property TimeTriggerCount As Long
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Device Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_datatransferrequestcondition.htm language=enus -->
## TOPIC 00339: DIChannelDataTransferRequestCondition Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_datatransferrequestcondition.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_datatransferrequestcondition.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DIChannel.DataTransferRequestCondition Property

### DIChannelDataTransferRequestCondition Property

Specifies under what condition to transfer data from the onboard memory of the device to the buffer.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DIDataTransferRequestCondition DataTransferRequestCondition { get; set; }
```

```text
Public Property DataTransferRequestCondition As DIDataTransferRequestCondition
	Get
	Set
```

###### Property Value

DIDataTransferRequestCondition

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_digitalfilterminimumpulsewidth.htm language=enus -->
## TOPIC 00340: DIChannelDigitalFilterMinimumPulseWidth Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_digitalfilterminimumpulsewidth.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_digitalfilterminimumpulsewidth.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DIChannel.DigitalFilterMinimumPulseWidth Property

### DIChannelDigitalFilterMinimumPulseWidth Property

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

DIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_digitalfiltertimebaserate.htm language=enus -->
## TOPIC 00341: DIChannelDigitalFilterTimebaseRate Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_digitalfiltertimebaserate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_digitalfiltertimebaserate.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DIChannel.DigitalFilterTimebaseRate Property

### DIChannelDigitalFilterTimebaseRate Property

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

DIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_digitalfiltertimebasesource.htm language=enus -->
## TOPIC 00342: DIChannelDigitalFilterTimebaseSource Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_digitalfiltertimebasesource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_digitalfiltertimebasesource.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DIChannel.DigitalFilterTimebaseSource Property

### DIChannelDigitalFilterTimebaseSource Property

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

DIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_invertlines.htm language=enus -->
## TOPIC 00343: DIChannelInvertLines Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_invertlines.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_invertlines.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DIChannel.InvertLines Property

### DIChannelInvertLines Property

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool InvertLines { get; set; }
```

```text
Public Property InvertLines As Boolean
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

DIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_logicfamily.htm language=enus -->
## TOPIC 00344: DIChannelLogicFamily Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_logicfamily.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannel_logicfamily.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DIChannel.LogicFamily Property

### DIChannelLogicFamily Property

Specifies the logic family to use for acquisition. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DILogicFamily LogicFamily { get; set; }
```

```text
Public Property LogicFamily As DILogicFamily
	Get
	Set
```

###### Property Value

DILogicFamily

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannelcollection_item.htm language=enus -->
## TOPIC 00345: DIChannelCollectionItem Property (Int64)

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannelcollection_item.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dichannelcollection_item.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DIChannelCollection.Item Property (Int64)

### DIChannelCollectionItem Property (Int64)

DIChannel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DIChannel this[
	long index
] { get; }
```

```text
Public ReadOnly Default Property Item ( 
	index As Long
) As DIChannel
	Get
```

###### Parameters

- **index**
  - Type: SystemInt64The zero-based index of the entry to locate in the collection.

###### Property Value

DIChannel

DIChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DIChannelCollection Class

Item Overload

NationalInstruments.DAQmx Namespace

###### Other Resources

Channels

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_digitalfiltertimebaserate.htm language=enus -->
## TOPIC 00346: DigitalEdgeReferenceTriggerDigitalFilterTimebaseRate Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_digitalfiltertimebaserate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_digitalfiltertimebaserate.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeReferenceTrigger.DigitalFilterTimebaseRate Property

### DigitalEdgeReferenceTriggerDigitalFilterTimebaseRate Property

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

DigitalEdgeReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_digitalfiltertimebasesource.htm language=enus -->
## TOPIC 00347: DigitalEdgeReferenceTriggerDigitalFilterTimebaseSource Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_digitalfiltertimebasesource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_digitalfiltertimebasesource.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeReferenceTrigger.DigitalFilterTimebaseSource Property

### DigitalEdgeReferenceTriggerDigitalFilterTimebaseSource Property

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

DigitalEdgeReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_edge.htm language=enus -->
## TOPIC 00348: DigitalEdgeReferenceTriggerEdge Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_edge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_edge.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeReferenceTrigger.Edge Property

### DigitalEdgeReferenceTriggerEdge Property

Reference Trigger

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DigitalEdgeReferenceTriggerEdge Edge { get; set; }
```

```text
Public Property Edge As DigitalEdgeReferenceTriggerEdge
	Get
	Set
```

###### Property Value

DigitalEdgeReferenceTriggerEdge

Reference Trigger

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DigitalEdgeReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_source.htm language=enus -->
## TOPIC 00349: DigitalEdgeReferenceTriggerSource Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_source.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitaledgereferencetrigger_source.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeReferenceTrigger.Source Property

### DigitalEdgeReferenceTriggerSource Property

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

terminal

Reference Trigger

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DigitalEdgeReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitaledgestarttrigger_digitalfiltertimebasesource.htm language=enus -->
## TOPIC 00350: DigitalEdgeStartTriggerDigitalFilterTimebaseSource Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitaledgestarttrigger_digitalfiltertimebasesource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitaledgestarttrigger_digitalfiltertimebasesource.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeStartTrigger.DigitalFilterTimebaseSource Property

### DigitalEdgeStartTriggerDigitalFilterTimebaseSource Property

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

DigitalEdgeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitallevelpausetrigger_condition.htm language=enus -->
## TOPIC 00351: DigitalLevelPauseTriggerCondition Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitallevelpausetrigger_condition.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitallevelpausetrigger_condition.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalLevelPauseTrigger.Condition Property

### DigitalLevelPauseTriggerCondition Property

Specifies whether the task pauses while the signal is high or low.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DigitalLevelPauseTriggerCondition Condition { get; set; }
```

```text
Public Property Condition As DigitalLevelPauseTriggerCondition
	Get
	Set
```

###### Property Value

DigitalLevelPauseTriggerCondition

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DigitalLevelPauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitalpatternreferencetrigger_pattern.htm language=enus -->
## TOPIC 00352: DigitalPatternReferenceTriggerPattern Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitalpatternreferencetrigger_pattern.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitalpatternreferencetrigger_pattern.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternReferenceTrigger.Pattern Property

### DigitalPatternReferenceTriggerPattern Property

digital pattern

Reference Trigger

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string Pattern { get; set; }
```

```text
Public Property Pattern As String
	Get
	Set
```

###### Property Value

String

digital pattern

Reference Trigger

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DigitalPatternReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitalpatternstarttrigger_condition.htm language=enus -->
## TOPIC 00353: DigitalPatternStartTriggerCondition Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitalpatternstarttrigger_condition.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_digitalpatternstarttrigger_condition.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternStartTrigger.Condition Property

### DigitalPatternStartTriggerCondition Property

physical channels

Source

digital pattern

Pattern

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DigitalPatternStartTriggerCondition Condition { get; set; }
```

```text
Public Property Condition As DigitalPatternStartTriggerCondition
	Get
	Set
```

###### Property Value

DigitalPatternStartTriggerCondition

physical channels

Source

digital pattern

Pattern

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DigitalPatternStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dochannel_numberoflines.htm language=enus -->
## TOPIC 00354: DOChannelNumberOfLines Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dochannel_numberoflines.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dochannel_numberoflines.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DOChannel.NumberOfLines Property

### DOChannelNumberOfLines Property

Indicates the number of digital lines in the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long NumberOfLines { get; }
```

```text
Public ReadOnly Property NumberOfLines As Long
	Get
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DOChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dochannelcollection_count.htm language=enus -->
## TOPIC 00355: DOChannelCollectionCount Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dochannelcollection_count.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_dochannelcollection_count.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DOChannelCollection.Count Property

### DOChannelCollectionCount Property

Gets the number of elements in the collection.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public virtual int Count { get; }
```

```text
Public Overridable ReadOnly Property Count As Integer
	Get
```

###### Property Value

Int32

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

DOChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_advancetriggeroutputterminal.htm language=enus -->
## TOPIC 00356: ExportSignalsAdvanceTriggerOutputTerminal Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_advancetriggeroutputterminal.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_advancetriggeroutputterminal.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExportSignals.AdvanceTriggerOutputTerminal Property

### ExportSignalsAdvanceTriggerOutputTerminal Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string AdvanceTriggerOutputTerminal { get; set; }
```

```text
Public Property AdvanceTriggerOutputTerminal As String
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

ExportSignals Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_counteroutputeventoutputbehavior.htm language=enus -->
## TOPIC 00357: ExportSignalsCounterOutputEventOutputBehavior Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_counteroutputeventoutputbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_counteroutputeventoutputbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExportSignals.CounterOutputEventOutputBehavior Property

### ExportSignalsCounterOutputEventOutputBehavior Property

Specifies whether the exported Counter Output Event pulses or changes from one state to the other when the counter reaches terminal count.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public CounterOutputEventOutputBehavior CounterOutputEventOutputBehavior { get; set; }
```

```text
Public Property CounterOutputEventOutputBehavior As CounterOutputEventOutputBehavior
	Get
	Set
```

###### Property Value

CounterOutputEventOutputBehavior

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Upon reaching terminal count, the counter can issue a pulse. Use [CounterOutputEventPulsePolarity](p_nationalinstruments_daqmx_exportsignals_counteroutputeventpulsepolarity.htm) to select a high or low pulse.

Upon reaching terminal count, the output terminal of the counter can change state, or toggle. For example, if the terminal is initially at a low state, 
it changes to high state and stays at the high state until the next terminal count. The terminal then changes to low state. Use [CounterOutputEventIdleState](p_nationalinstruments_daqmx_exportsignals_counteroutputeventidlestate.htm) to select the initial state of the terminal.

When counting up, a counter reaches terminal count when it reaches the maximum value (2^24 - 1 for a 24-bit counter). When counting 
down, a counter reaches terminal count when it reaches 0.

##### See Also

###### Reference

ExportSignals Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_dataactiveeventoutputterminal.htm language=enus -->
## TOPIC 00358: ExportSignalsDataActiveEventOutputTerminal Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_dataactiveeventoutputterminal.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_dataactiveeventoutputterminal.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExportSignals.DataActiveEventOutputTerminal Property

### ExportSignalsDataActiveEventOutputTerminal Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string DataActiveEventOutputTerminal { get; set; }
```

```text
Public Property DataActiveEventOutputTerminal As String
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

ExportSignals Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_handshakeeventoutputbehavior.htm language=enus -->
## TOPIC 00359: ExportSignalsHandshakeEventOutputBehavior Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_handshakeeventoutputbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_handshakeeventoutputbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExportSignals.HandshakeEventOutputBehavior Property

### ExportSignalsHandshakeEventOutputBehavior Property

Specifies the output behavior of the Handshake Event.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public HandshakeEventOutputBehavior HandshakeEventOutputBehavior { get; set; }
```

```text
Public Property HandshakeEventOutputBehavior As HandshakeEventOutputBehavior
	Get
	Set
```

###### Property Value

HandshakeEventOutputBehavior

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ExportSignals Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_handshakeeventoutputterminal.htm language=enus -->
## TOPIC 00360: ExportSignalsHandshakeEventOutputTerminal Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_handshakeeventoutputterminal.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_handshakeeventoutputterminal.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExportSignals.HandshakeEventOutputTerminal Property

### ExportSignalsHandshakeEventOutputTerminal Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string HandshakeEventOutputTerminal { get; set; }
```

```text
Public Property HandshakeEventOutputTerminal As String
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

ExportSignals Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_readyfortransfereventlevelactivelevel.htm language=enus -->
## TOPIC 00361: ExportSignalsReadyForTransferEventLevelActiveLevel Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_readyfortransfereventlevelactivelevel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_readyfortransfereventlevelactivelevel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExportSignals.ReadyForTransferEventLevelActiveLevel Property

### ExportSignalsReadyForTransferEventLevelActiveLevel Property

Specifies the active level of the exported Ready for Transfer Event.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public ReadyForTransferEventLevelActiveLevel ReadyForTransferEventLevelActiveLevel { get; set; }
```

```text
Public Property ReadyForTransferEventLevelActiveLevel As ReadyForTransferEventLevelActiveLevel
	Get
	Set
```

###### Property Value

ReadyForTransferEventLevelActiveLevel

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ExportSignals Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_readyfortransfereventoutputterminal.htm language=enus -->
## TOPIC 00362: ExportSignalsReadyForTransferEventOutputTerminal Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_readyfortransfereventoutputterminal.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_readyfortransfereventoutputterminal.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExportSignals.ReadyForTransferEventOutputTerminal Property

### ExportSignalsReadyForTransferEventOutputTerminal Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string ReadyForTransferEventOutputTerminal { get; set; }
```

```text
Public Property ReadyForTransferEventOutputTerminal As String
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

ExportSignals Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_referenceclock10mhzoutputterminal.htm language=enus -->
## TOPIC 00363: ExportSignalsReferenceClock10MHzOutputTerminal Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_referenceclock10mhzoutputterminal.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_referenceclock10mhzoutputterminal.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExportSignals.ReferenceClock10MHzOutputTerminal Property

### ExportSignalsReferenceClock10MHzOutputTerminal Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string ReferenceClock10MHzOutputTerminal { get; set; }
```

```text
Public Property ReferenceClock10MHzOutputTerminal As String
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

ExportSignals Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_sampleclockoutputbehavior.htm language=enus -->
## TOPIC 00364: ExportSignalsSampleClockOutputBehavior Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_sampleclockoutputbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_sampleclockoutputbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExportSignals.SampleClockOutputBehavior Property

### ExportSignalsSampleClockOutputBehavior Property

Specifies whether the exported Sample Clock issues a pulse at the beginning of a sample or changes to a high state for the duration of the sample.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public SampleClockOutputBehavior SampleClockOutputBehavior { get; set; }
```

```text
Public Property SampleClockOutputBehavior As SampleClockOutputBehavior
	Get
	Set
```

###### Property Value

SampleClockOutputBehavior

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

E Series devices might require many AI Convert Clock pulses to acquire one sample. Each pulse of the Sample Clock initiates the acquisition of one 
sample per channel in the task. Each sample per channel requires a pulse from the AI Convert Clock.

This property is valid for the AI Sample Clock only.

##### See Also

###### Reference

ExportSignals Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_synchronizationpulseeventoutputterminal.htm language=enus -->
## TOPIC 00365: ExportSignalsSynchronizationPulseEventOutputTerminal Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_synchronizationpulseeventoutputterminal.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_synchronizationpulseeventoutputterminal.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExportSignals.SynchronizationPulseEventOutputTerminal Property

### ExportSignalsSynchronizationPulseEventOutputTerminal Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string SynchronizationPulseEventOutputTerminal { get; set; }
```

```text
Public Property SynchronizationPulseEventOutputTerminal As String
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

ExportSignals Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_watchdogexpiredeventoutputterminal.htm language=enus -->
## TOPIC 00366: ExportSignalsWatchdogExpiredEventOutputTerminal Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_watchdogexpiredeventoutputterminal.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_exportsignals_watchdogexpiredeventoutputterminal.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExportSignals.WatchdogExpiredEventOutputTerminal Property

### ExportSignalsWatchdogExpiredEventOutputTerminal Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string WatchdogExpiredEventOutputTerminal { get; set; }
```

```text
Public Property WatchdogExpiredEventOutputTerminal As String
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

ExportSignals Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_handshaketrigger_interlocked.htm language=enus -->
## TOPIC 00367: HandshakeTriggerInterlocked Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_handshaketrigger_interlocked.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_handshaketrigger_interlocked.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

HandshakeTrigger.Interlocked Property

### HandshakeTriggerInterlocked Property

InterlockedHandshakeTrigger

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public InterlockedHandshakeTrigger Interlocked { get; }
```

```text
Public ReadOnly Property Interlocked As InterlockedHandshakeTrigger
	Get
```

###### Property Value

InterlockedHandshakeTrigger

InterlockedHandshakeTrigger

##### See Also

###### Reference

HandshakeTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_handshaketrigger_type.htm language=enus -->
## TOPIC 00368: HandshakeTriggerType Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_handshaketrigger_type.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_handshaketrigger_type.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

HandshakeTrigger.Type Property

### HandshakeTriggerType Property

Handshake Trigger

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public HandshakeTriggerType Type { get; set; }
```

```text
Public Property Type As HandshakeTriggerType
	Get
	Set
```

###### Property Value

HandshakeTriggerType

Handshake Trigger

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

HandshakeTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_interlockedhandshaketrigger_assertedlevel.htm language=enus -->
## TOPIC 00369: InterlockedHandshakeTriggerAssertedLevel Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_interlockedhandshaketrigger_assertedlevel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_interlockedhandshaketrigger_assertedlevel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

InterlockedHandshakeTrigger.AssertedLevel Property

### InterlockedHandshakeTriggerAssertedLevel Property

Handshake Trigger

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public InterlockedHandshakeTriggerAssertedLevel AssertedLevel { get; set; }
```

```text
Public Property AssertedLevel As InterlockedHandshakeTriggerAssertedLevel
	Get
	Set
```

###### Property Value

InterlockedHandshakeTriggerAssertedLevel

Handshake Trigger

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

InterlockedHandshakeTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_physicalchannel_powercontrolenable.htm language=enus -->
## TOPIC 00370: PhysicalChannelPowerControlEnable Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_physicalchannel_powercontrolenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_physicalchannel_powercontrolenable.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannel.PowerControlEnable Property

### PhysicalChannelPowerControlEnable Property

Specifies whether to turn on the sensor's power supply.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool PowerControlEnable { get; set; }
```

```text
Public Property PowerControlEnable As Boolean
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

PhysicalChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_physicalchannel_tedsversionletter.htm language=enus -->
## TOPIC 00371: PhysicalChannelTedsVersionLetter Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_physicalchannel_tedsversionletter.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_physicalchannel_tedsversionletter.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannel.TedsVersionLetter Property

### PhysicalChannelTedsVersionLetter Property

Indicates the version letter of the sensor.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string TedsVersionLetter { get; }
```

```text
Public ReadOnly Property TedsVersionLetter As String
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

PhysicalChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_polynomialscale_forwardcoefficients.htm language=enus -->
## TOPIC 00372: PolynomialScaleForwardCoefficients Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_polynomialscale_forwardcoefficients.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_polynomialscale_forwardcoefficients.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PolynomialScale.ForwardCoefficients Property

### PolynomialScaleForwardCoefficients Property

Specifies an array of coefficients for the polynomial that converts pre-scaled values to scaled values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double[] ForwardCoefficients { get; set; }
```

```text
Public Property ForwardCoefficients As Double()
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

##### See Also

###### Reference

PolynomialScale Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_referencetrigger_autotriggered.htm language=enus -->
## TOPIC 00373: ReferenceTriggerAutoTriggered Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_referencetrigger_autotriggered.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_referencetrigger_autotriggered.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTrigger.AutoTriggered Property

### ReferenceTriggerAutoTriggered Property

AutoTriggerEnable

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool AutoTriggered { get; }
```

```text
Public ReadOnly Property AutoTriggered As Boolean
	Get
```

###### Property Value

Boolean

AutoTriggerEnable

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_referencetrigger_autotriggerenable.htm language=enus -->
## TOPIC 00374: ReferenceTriggerAutoTriggerEnable Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_referencetrigger_autotriggerenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_referencetrigger_autotriggerenable.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTrigger.AutoTriggerEnable Property

### ReferenceTriggerAutoTriggerEnable Property

Specifies whether to send a software trigger to the device when a hardware trigger is no longer active in order to prevent a timeout.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool AutoTriggerEnable { get; set; }
```

```text
Public Property AutoTriggerEnable As Boolean
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

ReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_referencetrigger_maximumnumberoftriggerstodetect.htm language=enus -->
## TOPIC 00375: ReferenceTriggerMaximumNumberOfTriggersToDetect Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_referencetrigger_maximumnumberoftriggerstodetect.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_referencetrigger_maximumnumberoftriggerstodetect.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTrigger.MaximumNumberOfTriggersToDetect Property

### ReferenceTriggerMaximumNumberOfTriggersToDetect Property

Specifies the maximum number of times the task will detect a reference trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum Number of Triggers to Detect to be 0 causes the driver to automatically set this value to the maximum possible number of triggers detectable by the device and configuration combination. Note: The number of detected triggers may be less than number of trigger events occurring, because the devices were unable to respond to the trigger.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long MaximumNumberOfTriggersToDetect { get; set; }
```

```text
Public Property MaximumNumberOfTriggersToDetect As Long
	Get
	Set
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_referencetrigger_timestamptimescale.htm language=enus -->
## TOPIC 00376: ReferenceTriggerTimestampTimescale Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_referencetrigger_timestamptimescale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_referencetrigger_timestamptimescale.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTrigger.TimestampTimescale Property

### ReferenceTriggerTimestampTimescale Property

Specifies the reference trigger timestamp timescale.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public ReferenceTriggerTimestampTimescale TimestampTimescale { get; set; }
```

```text
Public Property TimestampTimescale As ReferenceTriggerTimestampTimescale
	Get
	Set
```

###### Property Value

ReferenceTriggerTimestampTimescale

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

ReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_referencetrigger_triggerwindow.htm language=enus -->
## TOPIC 00377: ReferenceTriggerTriggerWindow Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_referencetrigger_triggerwindow.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_referencetrigger_triggerwindow.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTrigger.TriggerWindow Property

### ReferenceTriggerTriggerWindow Property

Specifies the duration in seconds after the task starts during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. If no triggers are detected during the entire period, then no data will be returned. Specifying a Trigger Window of -1 causes the window to be infinite.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double TriggerWindow { get; set; }
```

```text
Public Property TriggerWindow As Double
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

ReferenceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_savedscaleinfo_author.htm language=enus -->
## TOPIC 00378: SavedScaleInfoAuthor Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_savedscaleinfo_author.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_savedscaleinfo_author.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SavedScaleInfo.Author Property

### SavedScaleInfoAuthor Property

Indicates the author of the custom scale.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string Author { get; }
```

```text
Public ReadOnly Property Author As String
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

SavedScaleInfo Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_savedtaskinfo_name.htm language=enus -->
## TOPIC 00379: SavedTaskInfoName Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_savedtaskinfo_name.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_savedtaskinfo_name.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SavedTaskInfo.Name Property

### SavedTaskInfoName Property

Gets the name of the task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string Name { get; }
```

```text
Public ReadOnly Property Name As String
	Get
```

###### Property Value

String

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

SavedTaskInfo Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_scale_description.htm language=enus -->
## TOPIC 00380: ScaleDescription Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_scale_description.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_scale_description.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Scale.Description Property

### ScaleDescription Property

Specifies a description for the scale.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string Description { get; set; }
```

```text
Public Property Description As String
	Get
	Set
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Scale Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_scale_name.htm language=enus -->
## TOPIC 00381: ScaleName Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_scale_name.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_scale_name.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Scale.Name Property

### ScaleName Property

scale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string Name { get; set; }
```

```text
Public Property Name As String
	Get
	Set
```

###### Property Value

String

String

scale

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Scale Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_scale_scaledunits.htm language=enus -->
## TOPIC 00382: ScaleScaledUnits Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_scale_scaledunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_scale_scaledunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Scale.ScaledUnits Property

### ScaleScaledUnits Property

Specifies the units to use for scaled values. You can use an arbitrary string.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string ScaledUnits { get; set; }
```

```text
Public Property ScaledUnits As String
	Get
	Set
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Scale Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_singlepoint_convertlateerrorstowarnings.htm language=enus -->
## TOPIC 00383: SinglePointConvertLateErrorsToWarnings Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_singlepoint_convertlateerrorstowarnings.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_singlepoint_convertlateerrorstowarnings.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SinglePoint.ConvertLateErrorsToWarnings Property

### SinglePointConvertLateErrorsToWarnings Property

WaitForNextSampleClock(Double)

NumberOfWarmupIterations

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool ConvertLateErrorsToWarnings { get; set; }
```

```text
Public Property ConvertLateErrorsToWarnings As Boolean
	Get
	Set
```

###### Property Value

Boolean

WaitForNextSampleClock(Double)

NumberOfWarmupIterations

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

SinglePoint Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_singlepoint_numberofwarmupiterations.htm language=enus -->
## TOPIC 00384: SinglePointNumberOfWarmupIterations Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_singlepoint_numberofwarmupiterations.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_singlepoint_numberofwarmupiterations.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SinglePoint.NumberOfWarmupIterations Property

### SinglePointNumberOfWarmupIterations Property

WaitForNextSampleClock(Double)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long NumberOfWarmupIterations { get; set; }
```

```text
Public Property NumberOfWarmupIterations As Long
	Get
	Set
```

###### Property Value

Int64

WaitForNextSampleClock(Double)

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

SinglePoint Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_singlepoint_waitfornextsampleclockwaitmode.htm language=enus -->
## TOPIC 00385: SinglePointWaitForNextSampleClockWaitMode Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_singlepoint_waitfornextsampleclockwaitmode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_singlepoint_waitfornextsampleclockwaitmode.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SinglePoint.WaitForNextSampleClockWaitMode Property

### SinglePointWaitForNextSampleClockWaitMode Property

WaitForNextSampleClock(Double)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public WaitForNextSampleClockWaitMode WaitForNextSampleClockWaitMode { get; set; }
```

```text
Public Property WaitForNextSampleClockWaitMode As WaitForNextSampleClockWaitMode
	Get
	Set
```

###### Property Value

WaitForNextSampleClockWaitMode

WaitForNextSampleClock(Double)

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

SinglePoint Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_starttrigger_delay.htm language=enus -->
## TOPIC 00386: StartTriggerDelay Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_starttrigger_delay.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_starttrigger_delay.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

StartTrigger.Delay Property

### StartTriggerDelay Property

DelayUnits

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double Delay { get; set; }
```

```text
Public Property Delay As Double
	Get
	Set
```

###### Property Value

Double

DelayUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

StartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_starttrigger_delayunits.htm language=enus -->
## TOPIC 00387: StartTriggerDelayUnits Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_starttrigger_delayunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_starttrigger_delayunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

StartTrigger.DelayUnits Property

### StartTriggerDelayUnits Property

Delay

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public StartTriggerDelayUnits DelayUnits { get; set; }
```

```text
Public Property DelayUnits As StartTriggerDelayUnits
	Get
	Set
```

###### Property Value

StartTriggerDelayUnits

Delay

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

StartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_starttrigger_triggerwindow.htm language=enus -->
## TOPIC 00388: StartTriggerTriggerWindow Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_starttrigger_triggerwindow.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_starttrigger_triggerwindow.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

StartTrigger.TriggerWindow Property

### StartTriggerTriggerWindow Property

Specifies the period of time in seconds after the task starts during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples for any triggers detected. If no triggers are detected during the entire period, then no data will be returned. Ensure the period of time specified covers the entire time span desired for trigger detection to avoid missed triggers. Specifying a Trigger Window of -1 causes the window to be infinite.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double TriggerWindow { get; set; }
```

```text
Public Property TriggerWindow As Double
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

StartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_switch_relaylist.htm language=enus -->
## TOPIC 00389: SwitchRelayList Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_switch_relaylist.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_switch_relaylist.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Switch.RelayList Property

### SwitchRelayList Property

Indicates a 
comma-delimited list of relay names.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string RelayList { get; }
```

```text
Public ReadOnly Property RelayList As String
	Get
```

###### Property Value

String

##### See Also

###### Reference

Switch Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_switchchannel_impedance.htm language=enus -->
## TOPIC 00390: SwitchChannelImpedance Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_switchchannel_impedance.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_switchchannel_impedance.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchChannel.Impedance Property

### SwitchChannelImpedance Property

Indicates in ohms the switch impedance. This value is important in the RF domain and should match the impedance of the sources and loads.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double Impedance { get; }
```

```text
Public ReadOnly Property Impedance As Double
	Get
```

###### Property Value

Double

##### See Also

###### Reference

SwitchChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_switchchannel_maxaccarrypower.htm language=enus -->
## TOPIC 00391: SwitchChannelMaxACCarryPower Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_switchchannel_maxaccarrypower.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_switchchannel_maxaccarrypower.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchChannel.MaxACCarryPower Property

### SwitchChannelMaxACCarryPower Property

Indicates in watts the maximum AC power that the device can carry.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double MaxACCarryPower { get; }
```

```text
Public ReadOnly Property MaxACCarryPower As Double
	Get
```

###### Property Value

Double

##### See Also

###### Reference

SwitchChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_switchscan_breakmode.htm language=enus -->
## TOPIC 00392: SwitchScanBreakMode Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_switchscan_breakmode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_switchscan_breakmode.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchScan.BreakMode Property

### SwitchScanBreakMode Property

Specifies the action to take between each entry in a scan list.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public SwitchScanBreakMode BreakMode { get; set; }
```

```text
Public Property BreakMode As SwitchScanBreakMode
	Get
	Set
```

###### Property Value

SwitchScanBreakMode

##### See Also

###### Reference

SwitchScan Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_switchscan_iswaitingforadvance.htm language=enus -->
## TOPIC 00393: SwitchScanIsWaitingForAdvance Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_switchscan_iswaitingforadvance.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_switchscan_iswaitingforadvance.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchScan.IsWaitingForAdvance Property

### SwitchScanIsWaitingForAdvance Property

Indicates if the switch hardware is waiting for an Advance Trigger. If the hardware is waiting, it completed the previous entry in the scan list.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool IsWaitingForAdvance { get; }
```

```text
Public ReadOnly Property IsWaitingForAdvance As Boolean
	Get
```

###### Property Value

Boolean

##### See Also

###### Reference

SwitchScan Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_task_dichannels.htm language=enus -->
## TOPIC 00394: TaskDIChannels Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_task_dichannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_task_dichannels.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Task.DIChannels Property

### TaskDIChannels Property

Gets the collection of digital input channels in the task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DIChannelCollection DIChannels { get; }
```

```text
Public ReadOnly Property DIChannels As DIChannelCollection
	Get
```

###### Property Value

DIChannelCollection

DIChannelCollection

DIChannel

##### Remarks

Each task can contain
only one type of channel. You must use the channels property that corresponds to the type of channels in the task to access the channels in the task.

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_task_dochannels.htm language=enus -->
## TOPIC 00395: TaskDOChannels Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_task_dochannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_task_dochannels.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Task.DOChannels Property

### TaskDOChannels Property

Gets the collection of digital output channels in the task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public DOChannelCollection DOChannels { get; }
```

```text
Public ReadOnly Property DOChannels As DOChannelCollection
	Get
```

###### Property Value

DOChannelCollection

DOChannelCollection

DOChannel

##### Remarks

Each task can contain
only one type of channel. You must use the channels property that corresponds to the type of channels in the task to access the channels in the task.

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_task_timing.htm language=enus -->
## TOPIC 00396: TaskTiming Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_task_timing.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_task_timing.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Task.Timing Property

### TaskTiming Property

Gets the timing configurations for the task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public Timing Timing { get; }
```

```text
Public ReadOnly Property Timing As Timing
	Get
```

###### Property Value

Timing

Timing

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_task_triggers.htm language=enus -->
## TOPIC 00397: TaskTriggers Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_task_triggers.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_task_triggers.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Task.Triggers Property

### TaskTriggers Property

Gets the triggers for the task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public Triggers Triggers { get; }
```

```text
Public ReadOnly Property Triggers As Triggers
	Get
```

###### Property Value

Triggers

Triggers

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timearmstarttrigger_timescale.htm language=enus -->
## TOPIC 00398: TimeArmStartTriggerTimescale Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timearmstarttrigger_timescale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timearmstarttrigger_timescale.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

TimeArmStartTrigger.Timescale Property

### TimeArmStartTriggerTimescale Property

Specifies the timescale to be used for timestamps used in an arm start time trigger.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public TimeArmStartTriggerTimescale Timescale { get; set; }
```

```text
Public Property Timescale As TimeArmStartTriggerTimescale
	Get
	Set
```

###### Property Value

TimeArmStartTriggerTimescale

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

TimeArmStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timearmstarttrigger_triggertime.htm language=enus -->
## TOPIC 00399: TimeArmStartTriggerTriggerTime Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timearmstarttrigger_triggertime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timearmstarttrigger_triggertime.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

TimeArmStartTrigger.TriggerTime Property

### TimeArmStartTriggerTriggerTime Property

Gets or sets when to trigger the arm start trigger.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public PrecisionDateTime TriggerTime { get; set; }
```

```text
Public Property TriggerTime As PrecisionDateTime
	Get
	Set
```

###### Property Value

PrecisionDateTime

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The trigger time is represented by a PrecisionDateTime expressed as a UTC time. To set a trigger time based on the current system time, use UtcNow, adding an offset, rather than Now. |

##### See Also

###### Reference

TimeArmStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timestarttrigger_timescale.htm language=enus -->
## TOPIC 00400: TimeStartTriggerTimescale Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timestarttrigger_timescale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timestarttrigger_timescale.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

TimeStartTrigger.Timescale Property

### TimeStartTriggerTimescale Property

Specifies the timescale to be used for timestamps used in a time trigger.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public TimeStartTriggerTimescale Timescale { get; set; }
```

```text
Public Property Timescale As TimeStartTriggerTimescale
	Get
	Set
```

###### Property Value

TimeStartTriggerTimescale

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

TimeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timestarttrigger_triggertime.htm language=enus -->
## TOPIC 00401: TimeStartTriggerTriggerTime Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timestarttrigger_triggertime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timestarttrigger_triggertime.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

TimeStartTrigger.TriggerTime Property

### TimeStartTriggerTriggerTime Property

Gets or sets when to trigger the start trigger.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public PrecisionDateTime TriggerTime { get; set; }
```

```text
Public Property TriggerTime As PrecisionDateTime
	Get
	Set
```

###### Property Value

PrecisionDateTime

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The trigger time is represented by a PrecisionDateTime expressed as a UTC time. To set a trigger time based on the current system time, use UtcNow, adding an offset, rather than Now. |

##### See Also

###### Reference

TimeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_aiconvertactiveedge.htm language=enus -->
## TOPIC 00402: TimingAIConvertActiveEdge Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_aiconvertactiveedge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_aiconvertactiveedge.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.AIConvertActiveEdge Property

### TimingAIConvertActiveEdge Property

Specifies on which edge of the clock pulse an analog-to-digital conversion takes place.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIConvertActiveEdge AIConvertActiveEdge { get; set; }
```

```text
Public Property AIConvertActiveEdge As AIConvertActiveEdge
	Get
	Set
```

###### Property Value

AIConvertActiveEdge

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This property is useful primarily when the signal you use as the AI Convert Clock is not a periodic clock. For example, set this property 
to [Rising](t_nationalinstruments_daqmx_aiconvertactiveedge.htm) to perform an analog to digital conversion on each rising edge of an aperiodic signal.

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_aiconverttimebasedivisor.htm language=enus -->
## TOPIC 00403: TimingAIConvertTimebaseDivisor Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_aiconverttimebasedivisor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_aiconverttimebasedivisor.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.AIConvertTimebaseDivisor Property

### TimingAIConvertTimebaseDivisor Property

Specifies the number of AI Convert Clock Timebase pulses needed to produce a single AI Convert Clock pulse.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long AIConvertTimebaseDivisor { get; set; }
```

```text
Public Property AIConvertTimebaseDivisor As Long
	Get
	Set
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_aiconverttimebasesource.htm language=enus -->
## TOPIC 00404: TimingAIConvertTimebaseSource Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_aiconverttimebasesource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_aiconverttimebasesource.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.AIConvertTimebaseSource Property

### TimingAIConvertTimebaseSource Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AIConvertTimebaseSource AIConvertTimebaseSource { get; set; }
```

```text
Public Property AIConvertTimebaseSource As AIConvertTimebaseSource
	Get
	Set
```

###### Property Value

AIConvertTimebaseSource

terminal

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_changedetectiondifallingedgephysicalchannels.htm language=enus -->
## TOPIC 00405: TimingChangeDetectionDIFallingEdgePhysicalChannels Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_changedetectiondifallingedgephysicalchannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_changedetectiondifallingedgephysicalchannels.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.ChangeDetectionDIFallingEdgePhysicalChannels Property

### TimingChangeDetectionDIFallingEdgePhysicalChannels Property

list or range

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string ChangeDetectionDIFallingEdgePhysicalChannels { get; set; }
```

```text
Public Property ChangeDetectionDIFallingEdgePhysicalChannels As String
	Get
	Set
```

###### Property Value

String

list or range

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_changedetectiondirisingedgephysicalchannels.htm language=enus -->
## TOPIC 00406: TimingChangeDetectionDIRisingEdgePhysicalChannels Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_changedetectiondirisingedgephysicalchannels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_changedetectiondirisingedgephysicalchannels.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.ChangeDetectionDIRisingEdgePhysicalChannels Property

### TimingChangeDetectionDIRisingEdgePhysicalChannels Property

list or range

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string ChangeDetectionDIRisingEdgePhysicalChannels { get; set; }
```

```text
Public Property ChangeDetectionDIRisingEdgePhysicalChannels As String
	Get
	Set
```

###### Property Value

String

list or range

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_delayfromsampleclock.htm language=enus -->
## TOPIC 00407: TimingDelayFromSampleClock Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_delayfromsampleclock.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_delayfromsampleclock.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.DelayFromSampleClock Property

### TimingDelayFromSampleClock Property

DelayFromSampleClockUnits

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double DelayFromSampleClock { get; set; }
```

```text
Public Property DelayFromSampleClock As Double
	Get
	Set
```

###### Property Value

Double

DelayFromSampleClockUnits

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_digitalfilterenable.htm language=enus -->
## TOPIC 00408: TimingDigitalFilterEnable Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_digitalfilterenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_digitalfilterenable.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.DigitalFilterEnable Property

### TimingDigitalFilterEnable Property

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

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_digitalfilterminimumpulsewidth.htm language=enus -->
## TOPIC 00409: TimingDigitalFilterMinimumPulseWidth Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_digitalfilterminimumpulsewidth.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_digitalfilterminimumpulsewidth.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.DigitalFilterMinimumPulseWidth Property

### TimingDigitalFilterMinimumPulseWidth Property

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

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_digitalfiltertimebaserate.htm language=enus -->
## TOPIC 00410: TimingDigitalFilterTimebaseRate Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_digitalfiltertimebaserate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_digitalfiltertimebaserate.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.DigitalFilterTimebaseRate Property

### TimingDigitalFilterTimebaseRate Property

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

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclockrate.htm language=enus -->
## TOPIC 00411: TimingSampleClockRate Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclockrate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclockrate.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SampleClockRate Property

### TimingSampleClockRate Property

Specifies the sampling rate in samples per channel per second. If you use an external source for the Sample Clock, set this input to the maximum expected rate of that clock.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double SampleClockRate { get; set; }
```

```text
Public Property SampleClockRate As Double
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

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclocktimebasedivisor.htm language=enus -->
## TOPIC 00412: TimingSampleClockTimebaseDivisor Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclocktimebasedivisor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclocktimebasedivisor.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SampleClockTimebaseDivisor Property

### TimingSampleClockTimebaseDivisor Property

Specifies the number of Sample Clock Timebase pulses needed to produce a single Sample Clock pulse.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long SampleClockTimebaseDivisor { get; set; }
```

```text
Public Property SampleClockTimebaseDivisor As Long
	Get
	Set
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

The rate of the Sample Clock is equal to (frequency of Sample Clock Timebase) / (value of this property).

If the Sample Clock Timebase is not a periodic clock, the value of this property determines the number 
of Sample Clock Timebase edges that the device must receive before producing each Sample Clock pulse. Use [SampleClockTimebaseActiveEdge](p_nationalinstruments_daqmx_timing_sampleclocktimebaseactiveedge.htm) to specify
the polarity of these edges.

Setting this property has a similar effect to setting [SampleClockRate](p_nationalinstruments_daqmx_timing_sampleclockrate.htm). Use [SampleClockRate](p_nationalinstruments_daqmx_timing_sampleclockrate.htm) when you know the rate of the Sample Clock Timebase 
and you want to acquire or generate samples at the specified rate. Use this property when you have an external timebase that 
you want to divide down and use as the Sample Clock, but you do not know rate of the external timebase.

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclocktimebaserate.htm language=enus -->
## TOPIC 00413: TimingSampleClockTimebaseRate Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclocktimebaserate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclocktimebaserate.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SampleClockTimebaseRate Property

### TimingSampleClockTimebaseRate Property

Specifies the rate of the Sample Clock Timebase. Some applications require that you specify a rate when you use any signal other than the onboard Sample Clock Timebase. NI-DAQmx requires this rate to calculate other timing parameters.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double SampleClockTimebaseRate { get; set; }
```

```text
Public Property SampleClockTimebaseRate As Double
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

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclocktimebaseterminal.htm language=enus -->
## TOPIC 00414: TimingSampleClockTimebaseTerminal Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclocktimebaseterminal.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclocktimebaseterminal.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SampleClockTimebaseTerminal Property

### TimingSampleClockTimebaseTerminal Property

SampleClockTimebaseSource

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string SampleClockTimebaseTerminal { get; }
```

```text
Public ReadOnly Property SampleClockTimebaseTerminal As String
	Get
```

###### Property Value

String

SampleClockTimebaseSource

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclocktimingresponsemode.htm language=enus -->
## TOPIC 00415: TimingSampleClockTimingResponseMode Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclocktimingresponsemode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclocktimingresponsemode.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SampleClockTimingResponseMode Property

### TimingSampleClockTimingResponseMode Property

**Note: This API is now obsolete.**

ConfigurePipelinedSampleClock(String, Double, SampleClockActiveEdge, SampleQuantityMode, Int32)

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("The SampleClockTimingResponseMode property is deprecated.  Please use the ConfigurePipelinedSampleClock method instead.")]
public SampleClockTimingResponseMode SampleClockTimingResponseMode { get; set; }
```

```text
<ObsoleteAttribute("The SampleClockTimingResponseMode property is deprecated.  Please use the ConfigurePipelinedSampleClock method instead.")>
Public Property SampleClockTimingResponseMode As SampleClockTimingResponseMode
	Get
	Set
```

###### Property Value

SampleClockTimingResponseMode

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclockunderflowbehavior.htm language=enus -->
## TOPIC 00416: TimingSampleClockUnderflowBehavior Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclockunderflowbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampleclockunderflowbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SampleClockUnderflowBehavior Property

### TimingSampleClockUnderflowBehavior Property

Specifies the action to take when the onboard memory of the device becomes empty. In either case, the sample clock does not stop.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public SampleClockUnderflowBehavior SampleClockUnderflowBehavior { get; set; }
```

```text
Public Property SampleClockUnderflowBehavior As SampleClockUnderflowBehavior
	Get
	Set
```

###### Property Value

SampleClockUnderflowBehavior

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampletimingengine.htm language=enus -->
## TOPIC 00417: TimingSampleTimingEngine Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampletimingengine.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_sampletimingengine.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SampleTimingEngine Property

### TimingSampleTimingEngine Property

timing engine

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long SampleTimingEngine { get; set; }
```

```text
Public Property SampleTimingEngine As Long
	Get
	Set
```

###### Property Value

Int64

timing engine

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_singlepoint.htm language=enus -->
## TOPIC 00418: TimingSinglePoint Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_singlepoint.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_singlepoint.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SinglePoint Property

### TimingSinglePoint Property

SinglePoint

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public SinglePoint SinglePoint { get; }
```

```text
Public ReadOnly Property SinglePoint As SinglePoint
	Get
```

###### Property Value

SinglePoint

SinglePoint

##### Remarks

You cannot apply [SinglePoint](t_nationalinstruments_daqmx_singlepoint.htm) to a subset of devices in the task and you must apply [SinglePoint](t_nationalinstruments_daqmx_singlepoint.htm) to the task as a whole. Call [SinglePoint](t_nationalinstruments_daqmx_singlepoint.htm) on the instance of [Timing](t_nationalinstruments_daqmx_timing.htm) returned from the [Timing](p_nationalinstruments_daqmx_task_timing.htm) property on the [Task](t_nationalinstruments_daqmx_task.htm) class. Accessing [SinglePoint](t_nationalinstruments_daqmx_singlepoint.htm) on instances of [Timing](t_nationalinstruments_daqmx_timing.htm) returned from the [ItemString](p_nationalinstruments_daqmx_timing_item.htm) property throws an exception.

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationclockinterval.htm language=enus -->
## TOPIC 00419: TimingSynchronizationClockInterval Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationclockinterval.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationclockinterval.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SynchronizationClockInterval Property

### TimingSynchronizationClockInterval Property

Specifies the interval, in Sample Clock periods, between each internal Synchronization Clock pulse. NI-DAQmx uses this pulse for synchronization of triggers between multiple devices at different rates. Refer to device documentation for information about how to calculate this value.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public long SynchronizationClockInterval { get; set; }
```

```text
Public Property SynchronizationClockInterval As Long
	Get
	Set
```

###### Property Value

Int64

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulseminimumdelaytostart.htm language=enus -->
## TOPIC 00420: TimingSynchronizationPulseMinimumDelayToStart Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulseminimumdelaytostart.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulseminimumdelaytostart.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SynchronizationPulseMinimumDelayToStart Property

### TimingSynchronizationPulseMinimumDelayToStart Property

Specifies in seconds the amount of time that elapses after the master device issues the synchronization pulse before the task starts.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double SynchronizationPulseMinimumDelayToStart { get; set; }
```

```text
Public Property SynchronizationPulseMinimumDelayToStart As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

Read [SynchronizationPulseTime](p_nationalinstruments_daqmx_timing_synchronizationpulsetime.htm) for all slave devices, and set this property for the master device to the maximum of those values.

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulsesource.htm language=enus -->
## TOPIC 00421: TimingSynchronizationPulseSource Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulsesource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulsesource.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SynchronizationPulseSource Property

### TimingSynchronizationPulseSource Property

terminal

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string SynchronizationPulseSource { get; set; }
```

```text
Public Property SynchronizationPulseSource As String
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

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulseterminal.htm language=enus -->
## TOPIC 00422: TimingSynchronizationPulseTerminal Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulseterminal.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulseterminal.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SynchronizationPulseTerminal Property

### TimingSynchronizationPulseTerminal Property

Indicates the name of the internal Synchronization Pulse terminal for the task. This property does not return the name of the source terminal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public string SynchronizationPulseTerminal { get; }
```

```text
Public ReadOnly Property SynchronizationPulseTerminal As String
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulsetime.htm language=enus -->
## TOPIC 00423: TimingSynchronizationPulseTime Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulsetime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulsetime.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SynchronizationPulseTime Property

### TimingSynchronizationPulseTime Property

Indicates in seconds the delay required to reset the ADCs/DACs after the device receives the synchronization pulse.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public double SynchronizationPulseTime { get; }
```

```text
Public ReadOnly Property SynchronizationPulseTime As Double
	Get
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

This time is the minimum delay required by the device between the receipt of the synchronization pulse and the start of the acquisition. Read this 
property for all slave devices and set [SynchronizationPulseMinimumDelayToStart](p_nationalinstruments_daqmx_timing_synchronizationpulseminimumdelaytostart.htm) for the master device to the maximum of these delays.

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulsetimescale.htm language=enus -->
## TOPIC 00424: TimingSynchronizationPulseTimescale Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulsetimescale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulsetimescale.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SynchronizationPulseTimescale Property

### TimingSynchronizationPulseTimescale Property

Specifies the timescale to be used for timestamps for a sync pulse.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public SynchronizationPulseTimescale SynchronizationPulseTimescale { get; set; }
```

```text
Public Property SynchronizationPulseTimescale As SynchronizationPulseTimescale
	Get
	Set
```

###### Property Value

SynchronizationPulseTimescale

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulsetriggertime.htm language=enus -->
## TOPIC 00425: TimingSynchronizationPulseTriggerTime Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulsetriggertime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulsetriggertime.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SynchronizationPulseTriggerTime Property

### TimingSynchronizationPulseTriggerTime Property

Gets or sets the start time of the synchronization pulse.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public PrecisionDateTime SynchronizationPulseTriggerTime { get; set; }
```

```text
Public Property SynchronizationPulseTriggerTime As PrecisionDateTime
	Get
	Set
```

###### Property Value

PrecisionDateTime

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### Remarks

| Note |
| --- |
| The trigger time is represented by a PrecisionDateTime expressed as a UTC time. To set a trigger time based on the current system time, use UtcNow, adding an offset, rather than Now. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulsetype.htm language=enus -->
## TOPIC 00426: TimingSynchronizationPulseType Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulsetype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_timing_synchronizationpulsetype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Timing.SynchronizationPulseType Property

### TimingSynchronizationPulseType Property

Specifies the type of sync pulse used in the task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public SynchronizationPulseType SynchronizationPulseType { get; set; }
```

```text
Public Property SynchronizationPulseType As SynchronizationPulseType
	Get
	Set
```

###### Property Value

SynchronizationPulseType

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Timing Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_triggers_advancetrigger.htm language=enus -->
## TOPIC 00427: TriggersAdvanceTrigger Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_triggers_advancetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_triggers_advancetrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Triggers.AdvanceTrigger Property

### TriggersAdvanceTrigger Property

AdvanceTrigger

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public AdvanceTrigger AdvanceTrigger { get; }
```

```text
Public ReadOnly Property AdvanceTrigger As AdvanceTrigger
	Get
```

###### Property Value

AdvanceTrigger

AdvanceTrigger

##### See Also

###### Reference

Triggers Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_watchdog_hasexpired.htm language=enus -->
## TOPIC 00428: WatchdogHasExpired Property

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_watchdog_hasexpired.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/p_nationalinstruments_daqmx_watchdog_hasexpired.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Watchdog.HasExpired Property

### WatchdogHasExpired Property

Indicates if the watchdog timer expired. You can read this property only while the task is running.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public bool HasExpired { get; }
```

```text
Public ReadOnly Property HasExpired As Boolean
	Get
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| DaqException | The NI-DAQmx driver returned an error. |

##### See Also

###### Reference

Watchdog Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_advancetrigger.htm language=enus -->
## TOPIC 00429: AdvanceTrigger Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_advancetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_advancetrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AdvanceTrigger Properties

### AdvanceTrigger Properties

The [AdvanceTrigger](t_nationalinstruments_daqmx_advancetrigger.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DigitalEdge | Gets the DigitalEdgeAdvanceTrigger. |
|  | Type | Obsolete. (Deprecated) Specifies the type of trigger to use to advance to the next entry in a switch scan list. |

Top

##### See Also

###### Reference

AdvanceTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_analogmultichannelwriter.htm language=enus -->
## TOPIC 00430: AnalogMultiChannelWriter Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_analogmultichannelwriter.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_analogmultichannelwriter.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiChannelWriter Properties

### AnalogMultiChannelWriter Properties

The [AnalogMultiChannelWriter](t_nationalinstruments_daqmx_analogmultichannelwriter.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### See Also

###### Reference

AnalogMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_analogmultiedgestarttrigger.htm language=enus -->
## TOPIC 00431: AnalogMultiEdgeStartTrigger Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_analogmultiedgestarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_analogmultiedgestarttrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiEdgeStartTrigger Properties

### AnalogMultiEdgeStartTrigger Properties

The [AnalogMultiEdgeStartTrigger](t_nationalinstruments_daqmx_analogmultiedgestarttrigger.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Couplings | Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
|  | Hystereses | Specifies an array of hysteresis levels in the units of the measurement or generation. If the corresponding element of Start.AnlgMultiEdge.Slopes is Rising, the trigger does not deassert until the source signal passes below the corresponding element of Start.AnlgMultiEdge.Lvls minus the hysteresis. If Start.AnlgEdge.Slope is Falling, the trigger does not deassert until the source signal passes above Start.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
|  | Levels | Specifies an array of thresholds in the units of the measurement or generation to start acquiring or generating samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
|  | Slopes | Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
|  | Sources | Specifies a list and/or range of analog sources that are going to be used for Analog triggering. Each source corresponds to an element in each of the Analog Multi Edge property arrays, if they are not empty. |

Top

##### See Also

###### Reference

AnalogMultiEdgeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_analogwindowpausetrigger.htm language=enus -->
## TOPIC 00432: AnalogWindowPauseTrigger Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_analogwindowpausetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_analogwindowpausetrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogWindowPauseTrigger Properties

### AnalogWindowPauseTrigger Properties

The [AnalogWindowPauseTrigger](t_nationalinstruments_daqmx_analogwindowpausetrigger.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Condition | Specifies whether the task pauses while the trigger signal is inside or outside the window you specify with WindowBottom and WindowTop. |
|  | Coupling | Specifies the coupling for the source signal of the terminal if the source is a terminal rather than a virtual channel. |
|  | DigitalFilterEnable | Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly. |
|  | DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
|  | DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | Source | Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger. |
|  | WindowBottom | Specifies the lower limit of the window. Specify this value in the units of the measurement or generation. |
|  | WindowTop | Specifies the upper limit of the window. Specify this value in the units of the measurement or generation. |

Top

##### See Also

###### Reference

AnalogWindowPauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cichannel.htm language=enus -->
## TOPIC 00433: CIChannel Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cichannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cichannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIChannel Properties

### CIChannel Properties

The [CIChannel](t_nationalinstruments_daqmx_cichannel.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AngularEncoderInitialAngle | Specifies the starting angle of the encoder. This value is in the units you specify with AngularEncoderUnits. |
|  | AngularEncoderPulsesPerRevolution | Specifies the number of pulses the encoder generates per revolution. This value is the number of pulses on either signal A or signal B, not the total number of pulses on both signal A and signal B. |
|  | AngularEncoderUnits | Specifies the units to use to return angular position measurements from the channel. |
|  | Count | Indicates the current value of the count register. |
|  | CountEdgesActiveEdge | Specifies on which edges to increment or decrement the counter. |
|  | CountEdgesCountDirection | Specifies whether to increment or decrement the counter on each edge. |
|  | CountEdgesCountDirectionDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | CountEdgesCountDirectionDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | CountEdgesCountDirectionDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | CountEdgesCountDirectionDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | CountEdgesCountDirectionDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | CountEdgesCountDirectionHysteresis | Specifies a hysteresis level applied to the CountEdgesCountDirectionThresholdVoltage. The source signal must fall below CountEdgesCountDirectionThresholdVoltage minus the hysteresis before a change in count direction occurs. |
|  | CountEdgesCountDirectionLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
|  | CountEdgesCountDirectionTerminal | Specifies the source terminal of the digital signal that controls the count direction if CountEdgesCountDirection is ExternallyControlled. |
|  | CountEdgesCountDirectionTerminalConfiguration | Specifies the input terminal configuration. |
|  | CountEdgesCountDirectionThresholdVoltage | Specifies the voltage level applied to the Count Direction terminal. When the signal is above this threshold, the counter counts up. When the signal is below this threshold, the counter counts down. |
|  | CountEdgesCountResetActiveEdge | Specifies on which edge of the signal to reset the count. |
|  | CountEdgesCountResetDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | CountEdgesCountResetDigitalFilterMinimumPulseWidth | Specifies the minimum pulse width the filter recognizes. |
|  | CountEdgesCountResetDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | CountEdgesCountResetDigitalFilterTimebaseSource | Specifies the input of the signal to use as the timebase of the pulse width filter. |
|  | CountEdgesCountResetDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | CountEdgesCountResetEnable | Specifies whether to reset the count on the active edge specified with CountEdgesCountResetTerminal. |
|  | CountEdgesCountResetHysteresis | Specifies a hysteresis level applied to CountEdgesCountResetThresholdVoltage. When CountEdgesCountResetActiveEdge is rising, the source signal must first fall below CountEdgesCountResetThresholdVoltage minus the hysteresis before a rising edge is detected at CountEdgesCountResetThresholdVoltage. When CountEdgesCountResetActiveEdge is falling, the source signal must first rise above CountEdgesCountResetThresholdVoltage plus the hysteresis before a falling edge is detected at CountEdgesCountResetThresholdVoltage. |
|  | CountEdgesCountResetLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
|  | CountEdgesCountResetResetCount | Specifies the value to reset the count to. |
|  | CountEdgesCountResetTerminal | Specifies the input terminal of the signal to reset the count. |
|  | CountEdgesCountResetTerminalConfiguration | Specifies the input terminal configuration. |
|  | CountEdgesCountResetThresholdVoltage | Specifies the voltage level at which to recognize the counter reset event. |
|  | CountEdgesDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | CountEdgesDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | CountEdgesDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | CountEdgesDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | CountEdgesDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | CountEdgesGateDigitalFilterEnable | Specifies whether to apply the pulse width filter to the gate input signal. |
|  | CountEdgesGateDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the digital filter recognizes. |
|  | CountEdgesGateDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | CountEdgesGateDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | CountEdgesGateEnable | Specifies whether to enable the functionality to gate the counter input signal for a count edges measurement. |
|  | CountEdgesGateHysteresis | Specifies a hysteresis level applied to the CountEdgesGateThresholdVoltage. When CountEdgesGatePauseState is High, the source signal must fall below CountEdgesGateThresholdVoltage minus the hysteresis before the counter resumes counting. When CountEdgesGatePauseState is Low, the source signal must rise above CountEdgesGateThresholdVoltage plus the hysteresis before the counter resumes counting. |
|  | CountEdgesGateLogicLevelBehavior | Specifies the logic level behavior on the gate input line. |
|  | CountEdgesGatePauseState | Specifies whether the counter gates input pulses while the signal is high or low. |
|  | CountEdgesGateTerminal | Specifies the gate terminal. |
|  | CountEdgesGateTerminalConfiguration | Specifies the gate terminal configuration. |
|  | CountEdgesGateThresholdVoltage | Specifies the voltage level at which to recognize the counter gate signal. |
|  | CountEdgesHysteresis | Specifies a hysteresis level to apply to CountEdgesThresholdVoltage. When CountEdgesActiveEdge is rising, the source signal must first fall below CountEdgesThresholdVoltage minus the hysteresis before a rising edge is detected at CountEdgesThresholdVoltage. When CountEdgesActiveEdge is falling, the source signal must first rise above CountEdgesThresholdVoltage plus the hysteresis before a falling edge is detected at CountEdgesThresholdVoltage. |
|  | CountEdgesInitialCount | Specifies the starting value from which to count. |
|  | CountEdgesLogicLevelBehavior | Specifies the logic level behavior on the input line. |
|  | CountEdgesTerminal | Specifies the input terminal of the signal to measure. |
|  | CountEdgesTerminalConfiguration | Specifies the input terminal configuration. |
|  | CountEdgesThresholdVoltage | Specifies the voltage level at which to recognize waveform repetitions. Select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls. |
|  | CounterTimebaseActiveEdge | Specifies whether a timebase cycle is from rising edge to rising edge or from falling edge to falling edge. |
|  | CounterTimebaseDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | CounterTimebaseDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | CounterTimebaseDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | CounterTimebaseDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | CounterTimebaseDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | CounterTimebaseMasterTimebaseDivisor | Specifies the divisor for an external counter timebase. You can divide the counter timebase in order to measure slower signals without causing the count register to roll over. |
|  | CounterTimebaseRate | Specifies in Hertz the frequency of the counter timebase. Specifying the rate of a counter timebase allows you to take measurements in terms of time or frequency rather than in ticks of the timebase. If you use an external timebase and do not specify the rate, you can take measurements only in terms of ticks of the timebase. |
|  | CounterTimebaseSource | Specifies the terminal of the timebase to use for the counter. |
|  | CustomScaleName | Specifies the name of a custom scale for the channel. |
|  | DataTransferMechanism | Specifies the data transfer mode for the channel. |
|  | DataTransferRequestCondition | Specifies under what condition to transfer data from the onboard memory of the device to the buffer. |
|  | Description | Specifies a user-defined description for the channel. (Inherited from Channel.) |
|  | DuplicateCountPrevention | Specifies whether to enable duplicate count prevention for the channel. Duplicate count prevention is enabled by default. Setting Prescaler disables duplicate count prevention unless you explicitly enable it. |
|  | DutyCycleDigitalFilterEnabled | Specifies whether to apply the pulse width filter to the signal. |
|  | DutyCycleDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the digital filter recognizes. |
|  | DutyCycleDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | DutyCycleDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | DutyCycleLogicLevelBehavior | Specifies the logic level behavior on the input line. |
|  | DutyCycleStartingEdge | Specifies which edge of the input signal to begin the duty cycle measurement. |
|  | DutyCycleTerminal | Specifies the input terminal of the signal to measure. |
|  | DutyCycleTerminalConfiguration | Specifies the input terminal configuration. |
|  | EncoderAInputDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | EncoderAInputDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | EncoderAInputDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | EncoderAInputDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | EncoderAInputDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | EncoderAInputLogicLevelBehavior | Specifies the logic level behavior on the input line. |
|  | EncoderAInputTerminal | Specifies the terminal to which signal A is connected. |
|  | EncoderAInputTerminalConfiguration | Specifies the input terminal configuration. |
|  | EncoderBInputDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | EncoderBInputDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | EncoderBInputDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | EncoderBInputDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | EncoderBInputDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | EncoderBInputLogicLevelBehavior | Specifies the logic level behavior on the input line. |
|  | EncoderBInputTerminal | Specifies the terminal to which signal B is connected. |
|  | EncoderBInputTerminalConfiguration | Specifies the input terminal configuration. |
|  | EncoderDecodingType | Specifies how to count and interpret the pulses the encoder generates on signal A and signal B. X1, X2, and X4 are valid for quadrature encoders only. TwoPulseCounting is valid for two-pulse encoders only. |
|  | EncoderZIndexEnable | Specifies whether to use Z indexing for the channel. |
|  | EncoderZIndexPhase | Specifies the states at which signal A and signal B must be while signal Z is high for NI-DAQmx to reset the measurement. If signal Z is never high while signal A and signal B are high, for example, you must choose a phase other than AHighBHigh. |
|  | EncoderZIndexValue | Specifies the value to which to reset the measurement when signal Z is high and signal A and signal B are at the states you specify with EncoderZIndexPhase. Specify this value in the units of the measurement. |
|  | EncoderZInputDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | EncoderZInputDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | EncoderZInputDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | EncoderZInputDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | EncoderZInputDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | EncoderZInputLogicLevelBehavior | Specifies the logic level behavior on the input line. |
|  | EncoderZInputTerminal | Specifies the terminal to which signal Z is connected. |
|  | EncoderZInputTerminalConfiguration | Specifies the input terminal configuration. |
|  | FilterDelay | Indicates the amount of time between when the input signal transitions and when the filtered sample is read by the host device. This value is in the units specified with FilterDelayUnits. |
|  | FilterDelayUnits | Specifies the units of FilterDelay. |
|  | FilterEnabled | Specifies the corresponding filter enable/disable state. |
|  | FilterFrequency | Specifies the corresponding filter frequency (cutoff or center) of the filter response. |
|  | FilterOrder | Specifies the corresponding filter order and defines the slope of the filter response. |
|  | FilterResponse | Specifies the corresponding filter response and defines the shape of the filter response. |
|  | FrequencyDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | FrequencyDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | FrequencyDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | FrequencyDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | FrequencyDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | FrequencyDivisor | Specifies the value by which to divide the input signal if FrequencyMeasurementMethod is LargeRangeTwoCounter. The larger the divisor, the more accurate the measurement. However, too large a value could cause the count register to roll over, which results in an incorrect measurement. |
|  | FrequencyEnableAveraging | Specifies whether to enable averaging mode for Sample Clock-timed frequency measurements. |
|  | FrequencyHysteresis | Specifies a hysteresis level to apply to FrequencyThresholdVoltage. When FrequencyStartingEdge is rising, the source signal must first fall below FrequencyThresholdVoltage minus the hysteresis before a rising edge is detected at FrequencyThresholdVoltage. When FrequencyStartingEdge is falling, the source signal must first rise above FrequencyThresholdVoltage plus the hysteresis before a falling edge is detected at FrequencyThresholdVoltage. |
|  | FrequencyLogicalLevelBehavior | Specifies the logic level behavior on the input line. |
|  | FrequencyMeasurementMethod | Specifies the method to use to measure the frequency of the signal. |
|  | FrequencyMeasurementTime | Specifies in seconds the length of time to measure the frequency of the signal if FrequencyMeasurementMethod is HighFrequencyTwoCounter. Measurement accuracy increases with increased measurement time and with increased signal frequency. If you measure a high-frequency signal for too long, however, the count register could roll over, which results in an incorrect measurement. |
|  | FrequencyStartingEdge | Specifies between which edges to measure the frequency of the signal. |
|  | FrequencyTerminal | Specifies the input terminal of the signal to measure. |
|  | FrequencyTerminalConfiguration | Specifies the input terminal configuration. |
|  | FrequencyThresholdVoltage | Specifies the voltage level at which to recognize waveform repetitions. Select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls. |
|  | FrequencyUnits | Specifies the units to use to return frequency measurements. |
|  | GpsSyncMethod | Specifies the method to use to synchronize the counter to a GPS receiver. |
|  | GpsSyncSource | Specifies the terminal to which the GPS synchronization signal is connected. |
|  | IsGlobal | Indicates whether the channel is a global channel. (Inherited from Channel.) |
|  | LinearEncoderDistancePerPulse | Specifies the distance to measure for each pulse the encoder generates on signal A or signal B. This value is in the units you specify with LinearEncoderUnits. |
|  | LinearEncoderInitialPosition | Specifies the position of the encoder when the measurement begins. This value is in the units you specify with LinearEncoderUnits. |
|  | LinearEncoderUnits | Specifies the units to use to return linear encoder measurements from the channel. |
|  | Maximum | Specifies the maximum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced maximum value that the hardware can measure with the current settings. |
|  | MaximumMeasurementPeriod | Specifies the maximum period (in seconds) in which the device will recognize signals. For frequency measurements, a signal with a higher period than the one set in this property will return 0 Hz. For duty cycle, the device will return 0 or 1 depending on the state of the line during the max defined period of time. Period measurements will return NaN. Pulse width measurement will return zero. |
|  | MeasurementType | Indicates the measurement to take with the channel. |
|  | MemoryMappingEnable | Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash. |
|  | Minimum | Specifies the minimum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced minimum value that the hardware can measure with the current settings. |
|  | NumberPossiblyInvalidSamples | Indicates the number of samples that the device might have overwritten before it could transfer them to the buffer. |
|  | OutputState | Indicates the current state of the out terminal of the counter. |
|  | PeriodDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | PeriodDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | PeriodDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | PeriodDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | PeriodDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | PeriodDivisor | Specifies the value by which to divide the input signal if PeriodMeasurementMethod is LargeRangeTwoCounter. The larger the divisor, the more accurate the measurement. However, too large a value could cause the count register to roll over, which results in an incorrect measurement. |
|  | PeriodEnableAveraging | Specifies whether to enable averaging mode for Sample Clock-timed period measurements. |
|  | PeriodHysteresis | Specifies a hysteresis level to apply to PeriodThresholdVoltage. When PeriodStartingEdge is rising, the source signal must first fall below PeriodThresholdVoltage minus the hysteresis before a rising edge is detected at PeriodThresholdVoltage. When PeriodStartingEdge is falling, the source signal must first rise above PeriodThresholdVoltage plus the hysteresis before a falling edge is detected at PeriodThresholdVoltage. |
|  | PeriodLogicLevelBehavior | Specifies the logic level behavior on the input line. |
|  | PeriodMeasurementMethod | Specifies the method to use to measure the period of the signal. |
|  | PeriodMeasurementTime | Specifies in seconds the length of time to measure the period of the signal if PeriodMeasurementMethod is HighFrequencyTwoCounter. Measurement accuracy increases with increased measurement time and with increased signal frequency. If you measure a high-frequency signal for too long, however, the count register could roll over, which results in an incorrect measurement. |
|  | PeriodStartingEdge | Specifies between which edges to measure the period of the signal. |
|  | PeriodTerminal | Specifies the input terminal of the signal to measure. |
|  | PeriodTerminalConfiguration | Specifies the input terminal configuration. |
|  | PeriodThresholdVoltage | Specifies the voltage level at which to recognize waveform repetitions. Select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls. |
|  | PeriodUnits | Specifies the unit to use to return period measurements. |
|  | PhysicalName | Specifies the name of the physical channel upon which this virtual channel is based. (Inherited from Channel.) |
|  | Prescaler | Specifies the divisor to apply to the signal you connect to the counter source terminal. Scaled data that you read takes this setting into account. You should use a prescaler only when you connect an external signal to the counter source terminal and when that signal has a higher frequency than the fastest onboard timebase. Setting this value disables duplicate count prevention unless you explicitly set DuplicateCountPrevention to . |
|  | PulseFrequencyDigitalFilterEnable | Specifies whether to apply a digital filter to the signal to measure. |
|  | PulseFrequencyDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | PulseFrequencyDigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | PulseFrequencyDigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
|  | PulseFrequencyDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | PulseFrequencyLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
|  | PulseFrequencyStartingEdge | Specifies on which edge of the input signal to begin pulse measurement. |
|  | PulseFrequencyTerminal | Specifies the input terminal of the signal to measure. |
|  | PulseFrequencyTerminalConfiguration | Specifies the input terminal configuration. |
|  | PulseFrequencyUnits | Specifies the units to use to return pulse specifications in terms of frequency. |
|  | PulseTicksDigitalFilterEnable | Specifies whether to apply a digital filter to the signal to measure. |
|  | PulseTicksDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | PulseTicksDigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | PulseTicksDigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
|  | PulseTicksDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | PulseTicksLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
|  | PulseTicksStartingEdge | Specifies on which edge of the input signal to begin pulse measurement. |
|  | PulseTicksTerminal | Specifies the input terminal of the signal to measure. |
|  | PulseTicksTerminalConfiguration | Specifies the input terminal configuration. |
|  | PulseTimeDigitalFilterEnable | Specifies whether to apply a digital filter to the signal to measure. |
|  | PulseTimeDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | PulseTimeDigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | PulseTimeDigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
|  | PulseTimeDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | PulseTimeLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
|  | PulseTimeStartingEdge | Specifies on which edge of the input signal to begin pulse measurement. |
|  | PulseTimeTerminal | Specifies the input terminal of the signal to measure. |
|  | PulseTimeTerminalConfiguration | Specifies the input terminal configuration. |
|  | PulseTimeUnits | Specifies the units to use to return pulse specifications in terms of high time and low time. |
|  | PulseWidthDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | PulseWidthDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | PulseWidthDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | PulseWidthDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | PulseWidthDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | PulseWidthLogicLevelBehavior | Specifies the logic level behavior on the input line. |
|  | PulseWidthStartingEdge | Specifies on which edge of the input signal to begin each pulse width measurement. |
|  | PulseWidthTerminal | Specifies the input terminal of the signal to measure. |
|  | PulseWidthTerminalConfiguration | Specifies the input terminal configuration. |
|  | PulseWidthUnits | Specifies the units to use to return pulse width measurements. |
|  | SampleClockOverrunBehavior | Specifies the counter behavior when data is read but a new value was not detected during a sample clock. |
|  | SampleClockOverrunSentinelValue | Specifies the sentinel value returned when the No New Sample Behavior is set to Sentinel Value. |
|  | SemiPeriodDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | SemiPeriodDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | SemiPeriodDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | SemiPeriodDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | SemiPeriodDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | SemiPeriodLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
|  | SemiPeriodStartingEdge | Specifies on which edge of the input signal to begin semi-period measurement. Semi-period measurements alternate between high time and low time, starting on this edge. |
|  | SemiPeriodTerminal | Specifies the input terminal of the signal to measure. |
|  | SemiPeriodTerminalConfiguration | Specifies the input terminal configuration. |
|  | SemiPeriodUnits | Specifies the units to use to return semi-period measurements. |
|  | SynchronizationUnlockBehavior | Specifies the action to take if the target loses its synchronization to the grand master. (Inherited from Channel.) |
|  | TerminalCountReached | Indicates whether the counter rolled over. When you query this property, NI-DAQmx resets it to . |
|  | TimestampInitialSeconds | Specifies the number of seconds that elapsed since the beginning of the current year. This value is ignored if GpsSyncMethod is IrigB. |
|  | TimestampUnits | Specifies the units to use to return timestamp measurements. |
|  | TwoEdgeSeparationFirstEdge | Specifies on which edge of the first signal to start each measurement. |
|  | TwoEdgeSeparationFirstEdgeDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | TwoEdgeSeparationFirstEdgeDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | TwoEdgeSeparationFirstEdgeDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | TwoEdgeSeparationFirstEdgeDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | TwoEdgeSeparationFirstEdgeDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | TwoEdgeSeparationFirstLogicLevelBehavior | Specifies the logic level behavior on the input line. |
|  | TwoEdgeSeparationFirstTerminal | Specifies the source terminal of the digital signal that starts each measurement. |
|  | TwoEdgeSeparationFirstTerminalConfiguration | Specifies the input terminal configuration. |
|  | TwoEdgeSeparationSecondEdge | Specifies on which edge of the second signal to stop each measurement. |
|  | TwoEdgeSeparationSecondEdgeDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | TwoEdgeSeparationSecondEdgeDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | TwoEdgeSeparationSecondEdgeDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | TwoEdgeSeparationSecondEdgeDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | TwoEdgeSeparationSecondEdgeDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | TwoEdgeSeparationSecondLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
|  | TwoEdgeSeparationSecondTerminal | Specifies the source terminal of the digital signal that stops each measurement. |
|  | TwoEdgeSeparationSecondTerminalConfiguration | Specifies the input terminal configuration. |
|  | TwoEdgeSeparationUnits | Specifies the units to use to return two-edge separation measurements from the channel. |
|  | Type | Indicates the type of the virtual channel. (Inherited from Channel.) |
|  | UsbTransferRequestCount | Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. |
|  | UsbTransferRequestSize | Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. |
|  | VelocityAInputDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | VelocityAInputDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the digital filter recognizes. |
|  | VelocityAInputDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | VelocityAInputDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | VelocityAInputLogicLevelBehavior | Specifies the logic level behavior of the input terminal. |
|  | VelocityAInputTerminal | Specifies the terminal to which signal A is connected. |
|  | VelocityAInputTerminalConfiguration | Specifies the input terminal configuration. |
|  | VelocityAngularEncoderPulsesPerRevolution | Specifies the number of pulses the encoder generates per revolution. This value is the number of pulses on either signal A or signal B, not the total number of pulses on both signal A and signal B. |
|  | VelocityAngularEncoderUnits | Specifies the units to use to return angular velocity counter measurements. |
|  | VelocityBInputDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | VelocityBInputDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the digital filter recognizes. |
|  | VelocityBInputDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | VelocityBInputDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | VelocityBInputLogicLevelBehavior | Specifies the logic level behavior of the input terminal. |
|  | VelocityBInputTerminal | Specifies the terminal to which signal B is connected. |
|  | VelocityBInputTerminalConfiguration | Specifies the input terminal configuration. |
|  | VelocityDecodingType | Specifies how to count and interpret the pulses the encoder generates on signal A and signal B. X1, X2, and X4 are valid for quadrature encoders only. Two Pulse Counting is valid for two-pulse encoders only. |
|  | VelocityDivisor | Specifies the value by which to divide the input signal. |
|  | VelocityLinearEncoderDistancePerPulse | Specifies the distance to measure for each pulse the encoder generates on signal A or signal B. This value is in the units you specify in CI.Velocity.LinEncoder.DistUnits. |
|  | VelocityLinearEncoderUnits | Specifies the units to use to return linear encoder velocity measurements from the channel. |
|  | VelocityMeasurementTime | Specifies in seconds the length of time to measure the velocity of the signal. |
|  | VirtualName | Gets the name of the virtual channel. (Inherited from Channel.) |
|  | VoltageThresholdLevel | Specifies the digital threshold value in Volts for high and low input transitions. Some devices do not support this for differential channels. |

Top

##### See Also

###### Reference

CIChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cidatafrequency.htm language=enus -->
## TOPIC 00434: CIDataFrequency Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cidatafrequency.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cidatafrequency.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataFrequency Properties

### CIDataFrequency Properties

The [CIDataFrequency](t_nationalinstruments_daqmx_cidatafrequency.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DutyCycle | Gets or sets the duty cycle of the pulse. |
|  | Frequency | Gets or sets the frequency of the pulse. |

Top

##### See Also

###### Reference

CIDataFrequency Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cidataticks.htm language=enus -->
## TOPIC 00435: CIDataTicks Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cidataticks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cidataticks.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataTicks Properties

### CIDataTicks Properties

The [CIDataTicks](t_nationalinstruments_daqmx_cidataticks.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | HighTicksInt32 | Gets or sets the number of timebase ticks the pulse is high. |
|  | HighTicksUInt32 | Gets or sets the number of timebase ticks the pulse is high. |
|  | LowTicksInt32 | Gets or sets the number of timebase ticks the pulse is low. |
|  | LowTicksUInt32 | Gets or sets the number of timebase ticks the pulse is low. |

Top

##### See Also

###### Reference

CIDataTicks Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cidatatime.htm language=enus -->
## TOPIC 00436: CIDataTime Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cidatatime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cidatatime.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIDataTime Properties

### CIDataTime Properties

The [CIDataTime](t_nationalinstruments_daqmx_cidatatime.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | HighTime | Gets or sets the amount of time the pulse is high. |
|  | LowTime | Gets or sets the amount of time the pulse is low. |

Top

##### See Also

###### Reference

CIDataTime Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cochannel.htm language=enus -->
## TOPIC 00437: COChannel Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cochannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cochannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

COChannel Properties

### COChannel Properties

The [COChannel](t_nationalinstruments_daqmx_cochannel.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AutoIncrementCount | Specifies a number of timebase ticks by which to increase the time spent in the idle state for each successive pulse. |
|  | ConstrainedGenerationMode | Specifies constraints to apply when the counter generates pulses. Constraining the counter reduces the device resources required for counter operation. Constraining the counter can also allow additional analog or counter tasks on the device to run concurrently. For continuous counter tasks, NI-DAQmx consumes no device resources when the counter is constrained. For finite counter tasks, resource use increases with the frequency regardless of the constraint mode. However, fixed frequency constraints significantly reduce resource usage, and fixed duty cycle constraint marginally reduces it. |
|  | Count | Indicates the current value of the count register. |
|  | CounterTimebaseActiveEdge | Specifies whether a timebase cycle is from rising edge to rising edge or from falling edge to falling edge. |
|  | CounterTimebaseDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | CounterTimebaseDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | CounterTimebaseDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | CounterTimebaseDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | CounterTimebaseDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | CounterTimebaseMasterTimebaseDivisor | Specifies the divisor for an external counter timebase. You can divide the counter timebase in order to generate slower signals without causing the count register to roll over. |
|  | CounterTimebaseRate | Specifies in Hertz the frequency of the counter timebase. Specifying the rate of a counter timebase allows you to define output pulses in seconds rather than in ticks of the timebase. If you use an external timebase and do not specify the rate, you can define output pulses only in ticks of the timebase. |
|  | CounterTimebaseSource | Specifies the terminal of the timebase to use for the counter. Typically, NI-DAQmx uses one of the internal counter timebases when generating pulses. Use this property to specify an external timebase and produce custom pulse widths that are not possible using the internal timebases. |
|  | DataTransferMechanism | Specifies the data transfer mode for the device. For buffered operations, use DMA or USB Bulk. For non-buffered operations, use Polled. |
|  | DataTransferRequestCondition | Specifies under what condition to transfer data from the buffer to the onboard memory of the device. |
|  | Description | Specifies a user-defined description for the channel. (Inherited from Channel.) |
|  | EnableInitialDelayOnRetrigger | Specifies whether to apply the initial delay to retriggered pulse trains. |
|  | IsGlobal | Indicates whether the channel is a global channel. (Inherited from Channel.) |
|  | MemoryMappingEnable | Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash. |
|  | OutputState | Indicates the current state of the output terminal of the counter. |
|  | OutputType | Indicates how to define pulses generated on the channel. |
|  | PhysicalName | Specifies the name of the physical channel upon which this virtual channel is based. (Inherited from Channel.) |
|  | Prescaler | Specifies the divisor to apply to the signal you connect to the counter source terminal. Pulse generations defined by frequency or time take this setting into account, but pulse generations defined by ticks do not. You should use a prescaler only when you connect an external signal to the counter source terminal and when that signal has a higher frequency than the fastest onboard timebase. |
|  | PulseDone | Indicates if the task completed pulse generation. Use this value for retriggerable pulse generation when you need to determine if the device generated the current pulse. For retriggerable tasks, when you query this property, NI-DAQmx resets it to . |
|  | PulseDutyCycle | Specifies the duty cycle of the pulses. The duty cycle of a signal is the width of the pulse divided by period. NI-DAQmx uses this ratio and the pulse frequency to determine the width of the pulses and the delay between pulses. |
|  | PulseFrequency | Specifies the frequency of the pulses to generate. This value is in the units you specify with PulseFrequencyUnits or when you create the channel. |
|  | PulseFrequencyInitialDelay | Specifies in seconds the amount of time to wait before generating the first pulse. |
|  | PulseFrequencyUnits | Specifies the units in which to define pulse frequency. |
|  | PulseHighTicks | Specifies the number of ticks the pulse is high. |
|  | PulseHighTime | Specifies the amount of time that the pulse is at a high voltage. This value is in the units you specify with PulseTimeUnits or when you create the channel. |
|  | PulseIdleState | Specifies the resting state of the output terminal. |
|  | PulseLowTicks | Specifies the number of ticks the pulse is low. |
|  | PulseLowTime | Specifies the amount of time that the pulse is at a low voltage. This value is in the units you specify with PulseTimeUnits or when you create the channel. |
|  | PulseTerminal | Specifies on which terminal to generate pulses. |
|  | PulseTicksInitialDelay | Specifies the number of ticks to wait before generating the first pulse. |
|  | PulseTimeInitialDelay | Specifies in seconds the amount of time to wait before generating the first pulse. |
|  | PulseTimeUnits | Specifies the units in which to define high and low pulse time. |
|  | ReadyForNewValue | Indicates whether the counter is ready for new continuous pulse train values. |
|  | SynchronizationUnlockBehavior | Specifies the action to take if the target loses its synchronization to the grand master. (Inherited from Channel.) |
|  | Type | Indicates the type of the virtual channel. (Inherited from Channel.) |
|  | UsbTransferRequestCount | Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. |
|  | UsbTransferRequestSize | Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. |
|  | UseOnlyOnBoardMemory | Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory directly after you start the task. Onboard memory includes data FIFOs. |
|  | VirtualName | Gets the name of the virtual channel. (Inherited from Channel.) |

Top

##### See Also

###### Reference

COChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cochannelcollection.htm language=enus -->
## TOPIC 00438: COChannelCollection Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cochannelcollection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_cochannelcollection.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

COChannelCollection Properties

### COChannelCollection Properties

The [COChannelCollection](t_nationalinstruments_daqmx_cochannelcollection.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | All | Gets a COChannel that operates on all of the channels in the task. |
|  | Count | Gets the number of elements in the collection. |
|  | ItemInt64 | Gets the COChannel at the specified index. In Visual C#, this property is the indexer. |
|  | ItemString | Gets the COChannel with the specified virtual channel name. In Visual C#, this property is the indexer. |

Top

##### See Also

###### Reference

COChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_codatafrequency.htm language=enus -->
## TOPIC 00439: CODataFrequency Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_codatafrequency.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_codatafrequency.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CODataFrequency Properties

### CODataFrequency Properties

The [CODataFrequency](t_nationalinstruments_daqmx_codatafrequency.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DutyCycle | Gets or sets the duty cycle of the pulse. |
|  | Frequency | Gets or sets the frequency of the pulse. |

Top

##### See Also

###### Reference

CODataFrequency Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_codataticks.htm language=enus -->
## TOPIC 00440: CODataTicks Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_codataticks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_codataticks.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CODataTicks Properties

### CODataTicks Properties

The [CODataTicks](t_nationalinstruments_daqmx_codataticks.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | HighTicksInt32 | Gets or sets the number of timebase ticks the pulse is high. |
|  | HighTicksUInt32 | Gets or sets the number of timebase ticks the pulse is high. |
|  | LowTicksInt32 | Gets or sets the number of timebase ticks the pulse is low. |
|  | LowTicksUInt32 | Gets or sets the number of timebase ticks the pulse is low. |

Top

##### See Also

###### Reference

CODataTicks Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_codatatime.htm language=enus -->
## TOPIC 00441: CODataTime Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_codatatime.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_codatatime.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CODataTime Properties

### CODataTime Properties

The [CODataTime](t_nationalinstruments_daqmx_codatatime.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | HighTime | Gets or sets the amount of time the pulse is high. |
|  | LowTime | Gets or sets the amount of time the pulse is low. |

Top

##### See Also

###### Reference

CODataTime Structure

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_countermultichannelreader.htm language=enus -->
## TOPIC 00442: CounterMultiChannelReader Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_countermultichannelreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_countermultichannelreader.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader Properties

### CounterMultiChannelReader Properties

The [CounterMultiChannelReader](t_nationalinstruments_daqmx_countermultichannelreader.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### See Also

###### Reference

CounterMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_countermultichannelwriter.htm language=enus -->
## TOPIC 00443: CounterMultiChannelWriter Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_countermultichannelwriter.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_countermultichannelwriter.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelWriter Properties

### CounterMultiChannelWriter Properties

The [CounterMultiChannelWriter](t_nationalinstruments_daqmx_countermultichannelwriter.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### See Also

###### Reference

CounterMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_countersinglechannelreader.htm language=enus -->
## TOPIC 00444: CounterSingleChannelReader Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_countersinglechannelreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_countersinglechannelreader.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader Properties

### CounterSingleChannelReader Properties

The [CounterSingleChannelReader](t_nationalinstruments_daqmx_countersinglechannelreader.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### See Also

###### Reference

CounterSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_daqstream.htm language=enus -->
## TOPIC 00445: DaqStream Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_daqstream.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_daqstream.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqStream Properties

### DaqStream Properties

The [DaqStream](t_nationalinstruments_daqmx_daqstream.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AccessoryInsertionOrRemovalDetected | Indicates if any device(s) in the task detected the insertion or removal of an accessory since the task started. Reading this property clears the accessory change status for all channels in the task. You must read this property before you read DevicesWithInsertedOrRemovedAccessories. Otherwise, you will receive an error. |
|  | AvailableSamplesPerChannel | Indicates the number of samples available to read per channel. This value is the same for all channels in the task. |
|  | Buffer | Gets the buffer for the task. |
|  | ChannelsToRead | Sets a subset of channels in the task from which to read. |
|  | CommonModeRangeErrorChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected a common mode range violation. You must read CommonModeRangeErrorChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | CommonModeRangeErrorChannelsExist | Indicates if the device(s) detected a common mode range violation for any virtual channel in the task. Common mode range violation occurs when the voltage of either the positive terminal or negative terminal to ground are out of range. Reading this property clears the common mode range violation status for all channels in the task. You must read this property before you read CommonModeRangeErrorChannels. Otherwise, you will receive an error. |
|  | CurrentReadPosition | Indicates in samples per channel the current position in the buffer. |
|  | CurrentWritePosition | Indicates the position in the buffer of the next sample to generate. This value is identical for all channels in the task. |
|  | DevicesWithInsertedOrRemovedAccessories | Indicates the names of any devices that detected the insertion or removal of an accessory since the task started. You must read AccessoryInsertionOrRemovalDetected before you read this property. Otherwise, you will receive an error. |
|  | DigitalLinesPerInputChannel | Indicates the number of lines per channel that NI-DAQmx returns in a sample for line-based reads. If a channel has fewer lines than this number, the extra lines are . |
|  | DigitalLinesPerOutputChannel | Indicates the number of Boolean values expected per channel in a sample for line-based writes. This property is determined by the channel in the task with the most digital lines. If a channel has fewer lines than this number, NI-DAQmx ignores the extra Boolean values. |
|  | LoggingFilePath | Specifies the path to the TDMS file to which you want to log data. If the file path is changed while the task is running, this takes effect on the next sample interval (if Logging.SampsPerFile has been set) or when DAQmx Start New File is called. New file paths can be specified by ending with "\\" or "/". Files created after specifying a new file path retain the same name and numbering sequence. |
|  | LoggingFilePreallocationSize | Specifies a size in samples to be used to pre-allocate space on disk. Pre-allocation can improve file I/O performance, especially in situations where multiple files are being written to disk. For finite tasks, the default behavior is to pre-allocate the file based on the number of samples you configure the task to acquire. |
|  | LoggingFileWriteSize | Specifies the size, in samples, in which data will be written to disk. The size must be evenly divisible by the volume sector size, in bytes. |
|  | LoggingMode | Specifies whether to enable logging and whether to allow reading data while logging. Log mode allows for the best performance. However, you cannot read data while logging if you specify this mode. If you want to read data while logging, specify Log and Read mode. |
|  | LoggingPause | Specifies whether logging is paused while a task is executing. If LoggingMode is set to Log and Read mode, this value is taken into consideration on the next call to DAQmx Read, where data is written to disk. If LoggingMode is set to Log Only mode, this value is taken into consideration the next time that data is written to disk. A new TDMS group is written when logging is resumed from a paused state. |
|  | LoggingSamplesPerFile | Specifies how many samples to write to each file. When the file reaches the number of samples specified, a new file is created with the naming convention of <filename>_####.tdms, where #### starts at 0001 and increments automatically with each new file. For example, if the file specified is C:\\data.tdms, the next file name used is C:\\data_0001.tdms. To disable file spanning behavior, set this attribute to 0. If LoggingFilePath is changed while this attribute is set, the new file path takes effect on the next file created. |
|  | NumberOfInputChannels | Indicates the number of channels that reading from the task reads from the task. This value is the number of channels in the task or the number of channels you specify with ChannelsToRead. |
|  | NumberOfOutputChannels | Indicates the number of channels that writing to the task writes to the task. This value is the number of channels in the task. |
|  | OpenThermocoupleChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected an open thermcouple. You must read OpenThermocoupleChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | OpenThermocoupleChannelsExist | Indicates if the device(s) detected an open thermocouple connected to any virtual channel in the task. Reading this property clears the open thermocouple status for all channels in the task. You must read this property before you read OpenThermocoupleChannels. Otherwise, you will receive an error. |
|  | OutputBufferSpaceAvailable | Indicates in samples per channel the amount of available space in the buffer. |
|  | OverloadedInputChannels | Indicates a list of names of any overloaded virtual channels in the task. You must read OverloadedInputChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | OverloadedInputChannelsExist | Indicates if the device(s) detected an overload in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read OverloadedInputChannels. Otherwise, you will receive an error. |
|  | PhaseLockedLoopUnlockedChannels | Indicates the channels that had their PLLs unlock. |
|  | PhaseLockedLoopUnlockedChannelsExist | Indicates whether the PLL is currently locked, or whether it became unlocked during the previous acquisition. Devices may report PLL Unlock either during acquisition or after acquisition. |
|  | ReadAllAvailableSamples | Specifies whether subsequent read operations read all samples currently available in the buffer or wait for the buffer to become full before reading. NI-DAQmx uses this setting for finite acquisitions and only when the number of samples to read is -1. For continuous acquisitions when the number of samples to read is -1, a read operation always reads all samples currently available in the buffer. |
|  | ReadAutoStart | Specifies if reading from the task automatically starts the task if you did not start the task explicitly by using starting the task. The default value is . When reading from the task starts a finite acquisition task, it also stops the task after reading the last sample. |
|  | ReadExcitationFaultChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected an excitation fault condition. You must read ReadExcitationFaultChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | ReadExcitationFaultChannelsExist | Indicates if the device(s) detected an excitation fault condition for any virtual channel in the task. Reading this property clears the excitation fault status for all channels in the task. You must read this property before you read ReadExcitationFaultChannels. Otherwise, you will receive an error. |
|  | ReadInputLimitsFaultChannels | Indicates the virtual channels that have detected samples outside the upper or lower limits configured for each channel in the task. You must read ReadInputLimitsFaultChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | ReadInputLimitsFaultChannelsExist | Indicates if the device or devices detected a sample that was outside the upper or lower limits configured for each channel in the task. Reading this property clears the input limits fault channel status for all channels in the task. You must read this property before you read ReadInputLimitsFaultChannels. Otherwise, you will receive an error. Note: Fault detection applies to both positive and negative inputs. For instance, if you specify a lower limit of 2 mA and an upper limit of 12 mA, NI-DAQmx detects a fault at 15 mA and -15 mA, but not at -6 mA because it is in the range of -12 mA to -2 mA. |
|  | ReadOffset | Specifies an offset in samples per channel at which to begin a read operation. This offset is relative to the location you specify with ReadRelativeTo. |
|  | ReadOpenCurrentLoopChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected an open current loop. You must read ReadOpenCurrentLoopChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | ReadOpenCurrentLoopChannelsExist | Indicates if the device(s) detected an open current loop for any virtual channel in the task. Reading this property clears the open current loop status for all channels in the task. You must read this property before you read ReadOpenCurrentLoopChannels. Otherwise, you will receive an error. |
|  | ReadOvercurrentChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected an overcurrent condition. You must read ReadOvercurrentChannelsExist before you read this property. Otherwise, you will receive an error. On some devices, you must restart the task for all overcurrent channels to recover. |
|  | ReadOvercurrentChannelsExist | Indicates if the device(s) detected an overcurrent condition for any virtual channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before you read ReadOvercurrentChannels. Otherwise, you will receive an error. |
|  | ReadOvertemperatureChannels | Indicates a list of names of any overtemperature virtual channels. You must read ReadOvertemperatureChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | ReadOvertemperatureChannelsExist | Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this property before you read ReadOvertemperatureChannels. Otherwise, you will receive an error. |
|  | ReadOverwriteMode | Specifies whether to overwrite samples in the buffer that you have not yet read. |
|  | ReadPowerSupplyFaultChannels | Indicates the virtual channels that have detected a power supply fault. You must read WritePowerSupplyFaultChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | ReadPowerSupplyFaultChannelsExist | Indicates if the device or devices detected a power supply fault condition in any virtual channel in the task. Reading this property clears the power supply fault status for all channels in this task. You must read this property before you read ReadPowerSupplyFaultChannels. Otherwise, you will receive an error. |
|  | ReadRawDataWidth | Indicates in bytes the size of a raw sample from the task. |
|  | ReadRelativeTo | Specifies the point in the buffer at which to begin a read operation. If you also specify an offset with ReadOffset, the read operation begins at that offset relative to the point you select with this property. The default value is CurrentReadPosition unless you configure a Reference Trigger for the task. If you configure a Reference Trigger, the default value is FirstPretriggerSample. |
|  | ReadSleepTime | Specifies in seconds the amount of time to sleep after checking for available samples if ReadWaitMode is Sleep. |
|  | ReadSynchronizationUnlockedChannels | Indicates the channels from devices in an unlocked target. |
|  | ReadSynchronizationUnlockedChannelsExist | Indicates whether the target is currently locked to the grand master. Devices may report PLL Unlock either during acquisition or after acquisition. |
|  | ReadWaitMode | Specifies how reading from the task waits for samples to become available. |
|  | TdmsLoggingGroupName | Specifies the name of the group to create within the TDMS file for data from this task. If you append data to an existing file and the specified group already exists, NI-DAQmx appends a number symbol and a number to the group name, incrementing that number until finding a group name that does not exist. For example, if you specify a group name of Voltage Task, and that group already exists, NI-DAQmx assigns the group name Voltage Task #1, then Voltage Task #2. |
|  | TdmsLoggingOperation | Specifies how to open the TDMS file. |
|  | Timeout | Gets or sets the amount of time in milliseconds to wait for reads or writes to complete. |
|  | TotalSamplesAcquiredPerChannel | Indicates the total number of samples acquired by each channel. NI-DAQmx returns a single value because this value is the same for all channels. For retriggered acquisitions, this value is the cumulative number of samples across all retriggered acquisitions. |
|  | TotalSamplesGeneratedPerChannel | Indicates the total number of samples generated by each channel in the task. This value is identical for all channels in the task. |
|  | WaveformAttributeMode | Gets or sets the type of information returned from a waveform read. |
|  | WriteExternalOvervoltageChannels | Indicates a list of names of any virtual channels in the task for which an External Overvoltage condition has been detected. You must read External OvervoltageChansExist before you read this property. Otherwise, you will receive an error. |
|  | WriteExternalOvervoltageChannelsExist | Indicates if the device(s) detected an External Overvoltage condition for any channel in the task. Reading this property clears the External Overvoltage status for all channels in the task. You must read this property before you read External OvervoltageChans. Otherwise, you will receive an error. |
|  | WriteOffset | Specifies in samples per channel an offset at which a write operation begins. This offset is relative to the location you specify with WriteRelativeTo. |
|  | WriteOpenCurrentLoopChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected an open current loop. You must read WriteOpenCurrentLoopChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | WriteOpenCurrentLoopChannelsExist | Indicates if the device(s) detected an open current loop for any channel in the task. Reading this property clears the open current loop status for all channels in the task. You must read this property before you read WriteOpenCurrentLoopChannels. Otherwise, you will receive an error. |
|  | WriteOvercurrentChannels | Indicates a list of names of any virtual channels in the task for which an overcurrent condition has been detected. You must read WriteOvercurrentChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | WriteOvercurrentChannelsExist | Indicates if the device(s) detected an overcurrent condition for any channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before you read WriteOvercurrentChannels. Otherwise, you will receive an error. |
|  | WriteOverloadedChannels | Indicates a list of names of any overloaded virtual channels in the task. You must read WriteOverloadedChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | WriteOverloadedChannelsExist | Indicates if the device(s) detected an overload in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read WriteOverloadedChannels. Otherwise, you will receive an error. |
|  | WriteOvertemperatureChannels | Indicates a list of names of any overtemperature virtual channels. You must read WriteOvertemperatureChannelsExist before you read this property. Otherwise, you will receive an error. The list of names may be empty if the device cannot determine the source of the overtemperature. |
|  | WriteOvertemperatureChannelsExist | Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this property before you read WriteOvertemperatureChannels. Otherwise, you will receive an error. |
|  | WritePowerSupplyFaultChannels | Indicates a list of names of any virtual channels in the task that have a power supply fault. You must read WritePowerSupplyFaultChannelsExist before you read this property. Otherwise, you will receive an error. |
|  | WritePowerSupplyFaultChannelsExist | Indicates if the device(s) detected a power supply fault for any channel in the task. Reading this property clears the power supply fault status for all channels in the task. You must read this property before you read WritePowerSupplyFaultChannels. Otherwise, you will receive an error. |
|  | WriteRawDataWidth | Indicates in bytes the required size of a raw sample to write to the task. |
|  | WriteRegenerationMode | Specifies whether to allow NI-DAQmx to generate the same data multiple times. |
|  | WriteRelativeTo | Specifies the point in the buffer at which to write data. If you also specify an offset with WriteOffset, the write operation begins at that offset relative to this point you select with this property. |
|  | WriteSleepTime | Specifies in seconds the amount of time to sleep after checking for available buffer space if WriteWaitMode is Sleep. |
|  | WriteSynchronizationUnlockedChannels | Indicates the channels from devices in an unlocked target. |
|  | WriteSynchronizationUnlockedChannelsExist | Indicates whether the target is currently locked to the grand master. Devices may report PLL Unlock either during acquisition or after acquisition. |
|  | WriteWaitMode | Specifies how writing to the task waits for space to become available in the buffer. |

Top

##### See Also

###### Reference

DaqStream Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_daqsystem.htm language=enus -->
## TOPIC 00446: DaqSystem Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_daqsystem.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_daqsystem.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqSystem Properties

### DaqSystem Properties

The [DaqSystem](t_nationalinstruments_daqmx_daqsystem.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Devices | Indicates the names of all devices installed in the system. |
|  | DriverMajorVersion | Indicates the major portion of the installed version of NI-DAQmx, such as 7 for version 7.0. |
|  | DriverMinorVersion | Indicates the minor portion of the installed version of NI-DAQmx, such as 0 for version 7.0. |
|  | DriverUpdateVersion | Indicates the update portion of the installed version of NI-DAQmx, such as 1 for version 9.0.1. |
|  | GlobalChannels | Indicates an array that contains the names of all global channels saved on the system. |
|  | IsReadOrWriteLate | Obsolete. Determines if a hardware-timed single-point read or write operation is overdue on the current thread. The IsReadOrWriteLate property has been deprecated in favor of the WaitForNextSampleClock(Double) method. |
|  | LastDaqWarning | Gets the DaqWarningEventArgs for the last DaqWarning event that occurred. |
|  | Local | Gets an instance of the DaqSystem class that represents the local DAQ system. |
|  | Scales | Indicates an array that contains the names of all custom scales saved on the system. |
|  | SwitchChannels | Obsolete. Gets an array that contains the switch channel names of devices installed in the system. |
|  | SwitchRelays | Obsolete. Gets an array that contains the switch relay names of devices installed in the system. |
|  | SwitchTopologies | Obsolete. Gets an array containing the names of all switch topologies. |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
|  | Tasks | Indicates an array that contains the names of all tasks saved on the system. |

Top

##### See Also

###### Reference

DaqSystem Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_daqwarningeventargs.htm language=enus -->
## TOPIC 00447: DaqWarningEventArgs Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_daqwarningeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_daqwarningeventargs.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqWarningEventArgs Properties

### DaqWarningEventArgs Properties

The [DaqWarningEventArgs](t_nationalinstruments_daqmx_daqwarningeventargs.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Error | Gets the NI-DAQmx driver code for the warning that occurred. Zero means no warning occurred. |
|  | Message | Gets a message that describes the warning. |

Top

##### See Also

###### Reference

DaqWarningEventArgs Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitaledgewatchdogexpirationtrigger.htm language=enus -->
## TOPIC 00448: DigitalEdgeWatchdogExpirationTrigger Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitaledgewatchdogexpirationtrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitaledgewatchdogexpirationtrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeWatchdogExpirationTrigger Properties

### DigitalEdgeWatchdogExpirationTrigger Properties

The [DigitalEdgeWatchdogExpirationTrigger](t_nationalinstruments_daqmx_digitaledgewatchdogexpirationtrigger.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Edge | Specifies on which edge of a digital signal to expire the watchdog task. |
|  | Source | Specifies the name of a terminal where a digital signal exists to use as the source of the Expiration Trigger. |

Top

##### See Also

###### Reference

DigitalEdgeWatchdogExpirationTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitallevelpausetrigger.htm language=enus -->
## TOPIC 00449: DigitalLevelPauseTrigger Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitallevelpausetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitallevelpausetrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalLevelPauseTrigger Properties

### DigitalLevelPauseTrigger Properties

The [DigitalLevelPauseTrigger](t_nationalinstruments_daqmx_digitallevelpausetrigger.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Condition | Specifies whether the task pauses while the signal is high or low. |
|  | DigitalFilterEnable | Specifies whether to apply a digital filter to the trigger signal. |
|  | DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | DigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | DigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | Source | Specifies the name of a terminal where there is a digital signal to use as the source of the Pause Trigger. |

Top

##### See Also

###### Reference

DigitalLevelPauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitalmultichannelreader.htm language=enus -->
## TOPIC 00450: DigitalMultiChannelReader Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitalmultichannelreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitalmultichannelreader.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelReader Properties

### DigitalMultiChannelReader Properties

The [DigitalMultiChannelReader](t_nationalinstruments_daqmx_digitalmultichannelreader.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### See Also

###### Reference

DigitalMultiChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitalmultichannelwriter.htm language=enus -->
## TOPIC 00451: DigitalMultiChannelWriter Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitalmultichannelwriter.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitalmultichannelwriter.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalMultiChannelWriter Properties

### DigitalMultiChannelWriter Properties

The [DigitalMultiChannelWriter](t_nationalinstruments_daqmx_digitalmultichannelwriter.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### See Also

###### Reference

DigitalMultiChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitalpatternpausetrigger.htm language=enus -->
## TOPIC 00452: DigitalPatternPauseTrigger Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitalpatternpausetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitalpatternpausetrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternPauseTrigger Properties

### DigitalPatternPauseTrigger Properties

The [DigitalPatternPauseTrigger](t_nationalinstruments_daqmx_digitalpatternpausetrigger.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Condition | Specifies if the Pause Trigger occurs when the physical channels specified with Source match or differ from the digital pattern specified with Pattern. |
|  | Pattern | Specifies the digital pattern that must be met for the Pause Trigger to occur. |
|  | Source | Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the lines within the port are in ascending order. |

Top

##### See Also

###### Reference

DigitalPatternPauseTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitalsinglechannelreader.htm language=enus -->
## TOPIC 00453: DigitalSingleChannelReader Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitalsinglechannelreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitalsinglechannelreader.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader Properties

### DigitalSingleChannelReader Properties

The [DigitalSingleChannelReader](t_nationalinstruments_daqmx_digitalsinglechannelreader.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### See Also

###### Reference

DigitalSingleChannelReader Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitalsinglechannelwriter.htm language=enus -->
## TOPIC 00454: DigitalSingleChannelWriter Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitalsinglechannelwriter.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_digitalsinglechannelwriter.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelWriter Properties

### DigitalSingleChannelWriter Properties

The [DigitalSingleChannelWriter](t_nationalinstruments_daqmx_digitalsinglechannelwriter.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### See Also

###### Reference

DigitalSingleChannelWriter Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_dochannel.htm language=enus -->
## TOPIC 00455: DOChannel Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_dochannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_dochannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DOChannel Properties

### DOChannel Properties

The [DOChannel](t_nationalinstruments_daqmx_dochannel.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DataTransferMechanism | Specifies the data transfer mode for the device. |
|  | DataTransferRequestCondition | Specifies under what condition to transfer data from the buffer to the onboard memory of the device. |
|  | Description | Specifies a user-defined description for the channel. (Inherited from Channel.) |
|  | GenerateOn | Specifies on which edge of the sample clock to generate samples. |
|  | InvertLines | Specifies whether to invert the lines in the channel. If you set this property to , the lines are at high logic when off and at low logic when on. |
|  | IsGlobal | Indicates whether the channel is a global channel. (Inherited from Channel.) |
|  | LineStatesDoneState | Specifies the state of the lines in a digital output task when the task completes execution. |
|  | LineStatesPausedState | Specifies the state of the lines in a digital output task when the task pauses. |
|  | LineStatesStartState | Specifies the state of the lines in a digital output task when the task starts. |
|  | LogicFamily | Specifies the logic family to use for generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families. |
|  | MemoryMappingEnable | Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash. |
|  | NumberOfLines | Indicates the number of digital lines in the channel. |
|  | OutputDriveType | Specifies the drive type for digital output channels. |
|  | OvercurrentAutoReenable | Specifies whether to automatically reenable channels after they no longer exceed the current limit specified by OvercurrentLimit. |
|  | OvercurrentLimit | Specifies the current threshold in Amperes for the channel. A value of 0 means the channel observes no limit. Devices can monitor only a finite number of current thresholds simultaneously. If you attempt to monitor additional thresholds, NI-DAQmx returns an error. |
|  | OvercurrentReenablePeriod | Specifies the delay in seconds between the time a channel no longer exceeds the current limit and the reactivation of that channel, if OvercurrentAutoReenable is . |
|  | PhysicalName | Specifies the name of the physical channel upon which this virtual channel is based. (Inherited from Channel.) |
|  | SynchronizationUnlockBehavior | Specifies the action to take if the target loses its synchronization to the grand master. (Inherited from Channel.) |
|  | Tristate | Specifies whether to stop driving the channel and set it to a high-impedance state. You must commit the task for this setting to take effect. |
|  | Type | Indicates the type of the virtual channel. (Inherited from Channel.) |
|  | UsbTransferRequestCount | Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. |
|  | UsbTransferRequestSize | Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. |
|  | UseOnlyOnBoardMemory | Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory after you start the task. Onboard memory includes data FIFOs. |
|  | VirtualName | Gets the name of the virtual channel. (Inherited from Channel.) |

Top

##### See Also

###### Reference

DOChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_dochannelcollection.htm language=enus -->
## TOPIC 00456: DOChannelCollection Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_dochannelcollection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_dochannelcollection.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DOChannelCollection Properties

### DOChannelCollection Properties

The [DOChannelCollection](t_nationalinstruments_daqmx_dochannelcollection.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | All | Gets a DOChannel that operates on all of the channels in the task. |
|  | Count | Gets the number of elements in the collection. |
|  | ItemInt64 | Gets the DOChannel at the specified index. In Visual C#, this property is the indexer. |
|  | ItemString | Gets the DOChannel with the specified virtual channel name. In Visual C#, this property is the indexer. |

Top

##### See Also

###### Reference

DOChannelCollection Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_savedchannelinfo.htm language=enus -->
## TOPIC 00457: SavedChannelInfo Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_savedchannelinfo.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_savedchannelinfo.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SavedChannelInfo Properties

### SavedChannelInfo Properties

The [SavedChannelInfo](t_nationalinstruments_daqmx_savedchannelinfo.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AllowInteractiveDeletion | Indicates whether the global channel can be deleted through MAX. |
|  | AllowInteractiveEditing | Indicates whether the global channel can be edited in the DAQ Assistant. |
|  | Author | Indicates the author of the global channel. |
|  | Name | Gets the name of the channel. |

Top

##### See Also

###### Reference

SavedChannelInfo Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_savedscaleinfo.htm language=enus -->
## TOPIC 00458: SavedScaleInfo Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_savedscaleinfo.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_savedscaleinfo.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SavedScaleInfo Properties

### SavedScaleInfo Properties

The [SavedScaleInfo](t_nationalinstruments_daqmx_savedscaleinfo.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AllowInteractiveDeletion | Indicates whether the custom scale can be deleted through MAX. |
|  | AllowInteractiveEditing | Indicates whether the custom scale can be edited in the DAQ Assistant. |
|  | Author | Indicates the author of the custom scale. |
|  | Name | Gets the name of the scale. |

Top

##### See Also

###### Reference

SavedScaleInfo Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_savedtaskinfo.htm language=enus -->
## TOPIC 00459: SavedTaskInfo Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_savedtaskinfo.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_savedtaskinfo.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SavedTaskInfo Properties

### SavedTaskInfo Properties

The [SavedTaskInfo](t_nationalinstruments_daqmx_savedtaskinfo.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AllowInteractiveDeletion | Indicates whether the task can be deleted through MAX. |
|  | AllowInteractiveEditing | Indicates whether the task can be edited in the DAQ Assistant. |
|  | Author | Indicates the author of the task. |
|  | Name | Gets the name of the task. |

Top

##### See Also

###### Reference

SavedTaskInfo Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_singlepoint.htm language=enus -->
## TOPIC 00460: SinglePoint Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_singlepoint.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_singlepoint.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SinglePoint Properties

### SinglePoint Properties

The [SinglePoint](t_nationalinstruments_daqmx_singlepoint.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | ConvertLateErrorsToWarnings | Specifies if WaitForNextSampleClock(Double), reading from the task, and writing to the task convert late errors to warnings. NI-DAQmx returns no late warnings or errors until the number of warmup iterations you specify with NumberOfWarmupIterations execute. |
|  | NumberOfWarmupIterations | Specifies the number of loop iterations that must occur before WaitForNextSampleClock(Double) and reading from the task return any late warnings or errors. The system needs a number of iterations to stabilize. During this period, a large amount of jitter occurs, potentially causing reads and writes to be late. The default number of warmup iterations is 100. Specify a larger number if needed to stabilize the system. |
|  | ReportMissedSamples | Specifies whether reading from the task returns lateness errors or warnings when it detects missed Sample Clock pulses. This setting does not affect WaitForNextSampleClock(Double). Set this property to for applications that need to detect lateness without using WaitForNextSampleClock(Double). |
|  | WaitForNextSampleClockWaitMode | Specifies how WaitForNextSampleClock(Double) waits for the next Sample Clock pulse. |
|  | WriteRecoveryMode | Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes. |

Top

##### See Also

###### Reference

SinglePoint Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_switch.htm language=enus -->
## TOPIC 00461: Switch Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_switch.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_switch.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Switch Properties

### Switch Properties

The [Switch](t_nationalinstruments_daqmx_switch.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AutoConnectAnalogBus | Specifies if NI-DAQmx routes multiplexed channels to the analog bus backplane. Only the SCXI-1127 and SCXI-1128 support this property. |
|  | IsSettled | Indicates when SettlingTime has expired. |
|  | NumberOfColumns | Gets the number of columns on a device in a matrix switch topology. This value is always 1 if the device is in a mux topology. |
|  | NumberOfRelays | Indicates the number of relays on the device. This value matches the number of relay names in RelayList. |
|  | NumberOfRows | Indicates the number of rows on a device in a matrix switch topology. Indicates the number of multiplexed channels on a device in a mux topology. |
|  | NumberOfSwitchChannels | Indicates the number of switch channels for the current topology of the device. This value matches the number of channel names in SwitchChannelList. |
|  | PowerDownLatchingRelaysAfterSettling | Specifies if WaitForSettling powers down latching relays after waiting for the device to settle. |
|  | RelayList | Indicates a comma-delimited list of relay names. |
|  | SettlingTime | Specifies in seconds the amount of time to wait for the switch to settle (or debounce). NI-DAQmx adds this time to the settling time of the motherboard. Modify this property only if the switch does not settle within the settling time of the motherboard. Refer to device documentation for supported settling times. |
|  | SupportedTopologies | Gets an array of the names of all switch topologies supported by this switch device. |
|  | SwitchChannelList | Indicates a comma-delimited list of channel names for the current topology of the device. |
|  | Temperature | Indicates the current temperature as read by the Switch module in degrees Celsius. Refer to your device documentation for more information. |
|  | Topology | Indicates the current topology of the device. This value is one of the topology options in SetTopologyAndReset(String). |

Top

##### See Also

###### Reference

Switch Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_switchchannel.htm language=enus -->
## TOPIC 00462: SwitchChannel Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_switchchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_switchchannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchChannel Properties

### SwitchChannel Properties

The [SwitchChannel](t_nationalinstruments_daqmx_switchchannel.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AnalogBusSharingEnable | Specifies whether to enable sharing of an analog bus line so that multiple switch devices can connect to it simultaneously. For each device that will share the analog bus line, set this property to to enable sharing on the channel that connects to the analog bus line. Analog bus sharing is disabled by default. |
|  | Bandwidth | Indicates in Hertz the maximum frequency of a signal that can pass through the switch without significant deterioration. |
|  | Impedance | Indicates in ohms the switch impedance. This value is important in the RF domain and should match the impedance of the sources and loads. |
|  | MaxACCarryCurrent | Indicates in amperes the maximum AC current that the device can carry. |
|  | MaxACCarryPower | Indicates in watts the maximum AC power that the device can carry. |
|  | MaxACSwitchCurrent | Indicates in amperes the maximum AC current that the device can switch. This current is always against an RMS voltage level. |
|  | MaxACSwitchPower | Indicates in watts the maximum AC power that the device can switch. |
|  | MaxACVoltage | Indicates in volts the maximum AC RMS voltage that the device can switch. |
|  | MaxDCCarryCurrent | Indicates in amperes the maximum DC current that the device can carry. |
|  | MaxDCCarryPower | Indicates in watts the maximum DC power that the device can carry. |
|  | MaxDCSwitchCurrent | Indicates in amperes the maximum DC current that the device can switch. This current is always against a DC voltage level. |
|  | MaxDCSwitchPower | Indicates in watts the maximum DC power that the device can switch. |
|  | MaxDCVoltage | Indicates in volts the maximum DC voltage that the device can switch. |
|  | Usage | Specifies how you can use the channel. Using this property acts as a safety mechanism to prevent you from connecting two source channels, for example. |
|  | WireMode | Indicates the number of wires that the channel switches. |

Top

##### See Also

###### Reference

SwitchChannel Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_switchscan.htm language=enus -->
## TOPIC 00463: SwitchScan Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_switchscan.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_switchscan.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchScan Properties

### SwitchScan Properties

The [SwitchScan](t_nationalinstruments_daqmx_switchscan.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | BreakMode | Specifies the action to take between each entry in a scan list. |
|  | IsWaitingForAdvance | Indicates if the switch hardware is waiting for an Advance Trigger. If the hardware is waiting, it completed the previous entry in the scan list. |
|  | RepeatMode | Specifies if the task advances through the scan list multiple times. |

Top

##### See Also

###### Reference

SwitchScan Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_tablescale.htm language=enus -->
## TOPIC 00464: TableScale Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_tablescale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_tablescale.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

TableScale Properties

### TableScale Properties

The [TableScale](t_nationalinstruments_daqmx_tablescale.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Specifies a description for the scale. (Inherited from Scale.) |
|  | Name | Gets the name of the scale. (Inherited from Scale.) |
|  | PreScaledUnits | Specifies the units of the values that you want to scale. (Inherited from Scale.) |
|  | PreScaledValues | Specifies an array of pre-scaled values. These values map directly to the values in ScaledValues. |
|  | ScaledUnits | Specifies the units to use for scaled values. You can use an arbitrary string. (Inherited from Scale.) |
|  | ScaledValues | Specifies an array of scaled values. These values map directly to the values in PreScaledValues. |
|  | Type | Gets the type of scale. (Inherited from Scale.) |

Top

##### See Also

###### Reference

TableScale Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_task.htm language=enus -->
## TOPIC 00465: Task Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_task.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_task.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Task Properties

### Task Properties

The [Task](t_nationalinstruments_daqmx_task.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AccessoryInsertionOrRemovalDetected | Indicates if any devices in the task detected the insertion or removal of an accessory since the task started. Reading this property clears the accessory change status for all channels in the task. You must read this property before you read DevicesWithInsertedOrRemovedAccessories. Otherwise, you will receive an error. |
|  | AIChannels | Gets the collection of analog input channels in the task. |
|  | AOChannels | Gets the collection of analog output channels in the task. |
|  | CIChannels | Gets the collection of counter input channels in the task. |
|  | COChannels | Gets the collection of counter output channels in the task. |
|  | Devices | Indicates an array containing the names of all devices in the task. |
|  | DevicesWithInsertedOrRemovedAccessories | Indicates the names of any devices that detected the insertion or removal of an accessory since the task started. You must read AccessoryInsertionOrRemovalDetected before you read this property. Otherwise, you will receive an error. |
|  | DIChannels | Gets the collection of digital input channels in the task. |
|  | DOChannels | Gets the collection of digital output channels in the task. |
|  | EveryNSamplesReadEventInterval | Gets or sets the interval, in number of samples per channel, at which EveryNSamplesRead is called. |
|  | EveryNSamplesWrittenEventInterval | Gets or sets the interval, in number of samples per channel, at which EveryNSamplesWritten is called. |
|  | ExportSignals | Gets the exported signal configuration for the task. |
|  | IsDone | Indicates whether the task completed execution. |
|  | Stream | Gets the stream for the task. |
|  | SwitchScan | Gets the switch scan configuration for the task. |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
|  | Timing | Gets the timing configurations for the task. |
|  | Triggers | Gets the triggers for the task. |
|  | Watchdog | Gets the watchdog configuration and control object for the task. |

Top

##### See Also

###### Reference

Task Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_taskdoneeventargs.htm language=enus -->
## TOPIC 00466: TaskDoneEventArgs Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_taskdoneeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_taskdoneeventargs.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

TaskDoneEventArgs Properties

### TaskDoneEventArgs Properties

The [TaskDoneEventArgs](t_nationalinstruments_daqmx_taskdoneeventargs.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Error | Gets the Exception that occurred, if any. |

Top

##### See Also

###### Reference

TaskDoneEventArgs Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_timestarttrigger.htm language=enus -->
## TOPIC 00467: TimeStartTrigger Properties

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_timestarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/properties_t_nationalinstruments_daqmx_timestarttrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

TimeStartTrigger Properties

### TimeStartTrigger Properties

The [TimeStartTrigger](t_nationalinstruments_daqmx_timestarttrigger.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Timescale | Specifies the timescale to be used for timestamps used in a time trigger. |
|  | TriggerTime | Gets or sets when to trigger the start trigger. |

Top

##### See Also

###### Reference

TimeStartTrigger Class

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aibridgeconfiguration11637.htm language=enus -->
## TOPIC 00468: AIBridgeConfiguration11637 Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aibridgeconfiguration11637.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aibridgeconfiguration11637.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIBridgeConfiguration11637 Enumeration

### AIBridgeConfiguration11637 Enumeration

Specifies the type of Wheatstone bridge connected to the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIBridgeConfiguration11637
```

```text
Public Enumeration AIBridgeConfiguration11637
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | FullBridge | 10182 | Sensor connected to the FD-11637 is a full bridge. |
|  | HalfBridge | 10187 | Sensor connected to the FD-11637 is a half bridge. |
|  | QuarterBridge350OhmCompletionResistor | 16164 | Sensor connected to the FD-11637 is a quarter bridge with the resistance of 350 Ohms. |
|  | QuarterBridge120OhmCompletionResistor | 16163 | Sensor connected to the FD-11637 is a quarter bridge with the resistance of 120 Ohms. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aibridgephysicalunits.htm language=enus -->
## TOPIC 00469: AIBridgePhysicalUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aibridgephysicalunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aibridgephysicalunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIBridgePhysicalUnits Enumeration

### AIBridgePhysicalUnits Enumeration

Specifies to which physical unit to scale electrical data. Select the same unit that the sensor data sheet or calibration certificate uses for physical values.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIBridgePhysicalUnits
```

```text
Public Enumeration AIBridgePhysicalUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Newtons | 15875 | Newtons. |
|  | Pounds | 15876 | Pounds. |
|  | KilogramForce | 15877 | kilograms-force. |
|  | Pascals | 10081 | Pascals. |
|  | PoundsPerSquareInch | 15879 | Pounds per square inch. |
|  | Bar | 15880 | Bar. |
|  | NewtonMeters | 15881 | Newton metres. |
|  | InchOunces | 15882 | Ounce-inches. |
|  | InchPounds | 15883 | Pound-inches. |
|  | FootPounds | 15884 | Pound-feet. |

##### Remarks

BridgePhysicalUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ailowpassswitchedcapacitorclocksource.htm language=enus -->
## TOPIC 00470: AILowpassSwitchedCapacitorClockSource Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ailowpassswitchedcapacitorclocksource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ailowpassswitchedcapacitorclocksource.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AILowpassSwitchedCapacitorClockSource Enumeration

### AILowpassSwitchedCapacitorClockSource Enumeration

Specifies the source of the filter clock. If you need a higher resolution for the filter, you can supply an external clock to increase the resolution. Refer to the SCXI-1141/1142/1143 User Manual for more information.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AILowpassSwitchedCapacitorClockSource
```

```text
Public Enumeration AILowpassSwitchedCapacitorClockSource
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Internal | 10200 | Internal to the device. |
|  | External | 10167 | External to the device. |

##### Remarks

LowpassSwitchedCapacitorClockSource

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ailvdtsensitivityunits.htm language=enus -->
## TOPIC 00471: AILvdtSensitivityUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ailvdtsensitivityunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ailvdtsensitivityunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AILvdtSensitivityUnits Enumeration

### AILvdtSensitivityUnits Enumeration

LvdtSensitivity

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AILvdtSensitivityUnits
```

```text
Public Enumeration AILvdtSensitivityUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | MillivoltsPerVoltPerMillimeter | 12506 | mVolts/Volt/mMeter. |
|  | MillivoltsPerVoltPerMilliinch | 12505 | mVolts/Volt/0.001 Inch. |

##### Remarks

LvdtSensitivity

LvdtSensitivityUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ailvdtunits.htm language=enus -->
## TOPIC 00472: AILvdtUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ailvdtunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ailvdtunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AILvdtUnits Enumeration

### AILvdtUnits Enumeration

Specifies the units to use to return linear position measurements from the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AILvdtUnits
```

```text
Public Enumeration AILvdtUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Meters | 10219 | Meters. |
|  | Inches | 10379 | Inches. |
|  | FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

##### Remarks

LvdtUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airawdatacompressiontype.htm language=enus -->
## TOPIC 00473: AIRawDataCompressionType Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airawdatacompressiontype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airawdatacompressiontype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIRawDataCompressionType Enumeration

### AIRawDataCompressionType Enumeration

raw samples

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIRawDataCompressionType
```

```text
Public Enumeration AIRawDataCompressionType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | None | 10230 | Do not compress samples. |
|  | LosslessPacking | 12555 | Remove unused bits from samples. No resolution is lost. |
|  | LossyLsbRemoval | 12556 | Remove unused bits from samples. Then, if necessary, remove bits from samples until the samples are the size specified with LossyLsbRemovalCompressedSampleSize. This compression type limits resolution to the specified sample size. |

##### Remarks

raw samples

RawDataCompressionType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airesistanceconfiguration.htm language=enus -->
## TOPIC 00474: AIResistanceConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airesistanceconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airesistanceconfiguration.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIResistanceConfiguration Enumeration

### AIResistanceConfiguration Enumeration

Specifies the resistance configuration for the channel. NI-DAQmx uses this value for any resistance-based measurements, including temperature measurement using a thermistor or RTD.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIResistanceConfiguration
```

```text
Public Enumeration AIResistanceConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | TwoWire | 2 | 2-wire mode. |
|  | ThreeWire | 3 | 3-wire mode. |
|  | FourWire | 4 | 4-wire mode. |

##### Remarks

ResistanceConfiguration

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airesistanceunits.htm language=enus -->
## TOPIC 00475: AIResistanceUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airesistanceunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airesistanceunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIResistanceUnits Enumeration

### AIResistanceUnits Enumeration

Specifies the units to use to return resistance measurements.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIResistanceUnits
```

```text
Public Enumeration AIResistanceUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Ohms | 10384 | Ohms. |
|  | FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |
|  | FromTeds | 12516 | Units defined by TEDS information associated with the channel. |

##### Remarks

ResistanceUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airesolutionunits.htm language=enus -->
## TOPIC 00476: AIResolutionUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airesolutionunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airesolutionunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIResolutionUnits Enumeration

### AIResolutionUnits Enumeration

Resolution

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIResolutionUnits
```

```text
Public Enumeration AIResolutionUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Bits | 10109 | Bits. |

##### Remarks

Resolution

ResolutionUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airosettemeasurementtype.htm language=enus -->
## TOPIC 00477: AIRosetteMeasurementType Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airosettemeasurementtype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airosettemeasurementtype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIRosetteMeasurementType Enumeration

### AIRosetteMeasurementType Enumeration

Specifies the type of rosette measurement.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIRosetteMeasurementType
```

```text
Public Enumeration AIRosetteMeasurementType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | PrincipalStrain1 | 15971 | The maximum tensile strain coplanar to the surface of the material under stress. |
|  | PrincipalStrain2 | 15972 | The minimum tensile strain coplanar to the surface of the material under stress. |
|  | PrincipalStrainAngle | 15973 | The angle at which the principal strains of the rosette occur. |
|  | CartesianStrainX | 15974 | The tensile strain coplanar to the surface of the material under stress in the X coordinate direction. |
|  | CartesianStrainY | 15975 | The tensile strain coplanar to the surface of the material under stress in the Y coordinate direction. |
|  | CartesianShearStrainXY | 15976 | The tensile strain coplanar to the surface of the material under stress in the XY coordinate direction. |
|  | MaximumShearStrain | 15977 | The maximum strain coplanar to the cross section of the material under stress. |
|  | MaximumShearStrainAngle | 15978 | The angle at which the maximum shear strain of the rosette occurs. |

##### Remarks

RosetteMeasurementType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airosettetype.htm language=enus -->
## TOPIC 00478: AIRosetteType Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airosettetype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airosettetype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIRosetteType Enumeration

### AIRosetteType Enumeration

Indicates the type of rosette gage.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIRosetteType
```

```text
Public Enumeration AIRosetteType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rectangular | 15968 | A rectangular rosette consists of three strain gages, each separated by a 45 degree angle. |
|  | Delta | 15969 | A delta rosette consists of three strain gages, each separated by a 60 degree angle. |
|  | Tee | 15970 | A tee rosette consists of two gages oriented at 90 degrees with respect to each other. |

##### Remarks

RosetteType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airtdtype.htm language=enus -->
## TOPIC 00479: AIRtdType Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airtdtype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airtdtype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIRtdType Enumeration

### AIRtdType Enumeration

type

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIRtdType
```

```text
Public Enumeration AIRtdType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Pt3750 | 12481 | Pt3750. |
|  | Pt3851 | 10071 | Pt3851. |
|  | Pt3911 | 12482 | Pt3911. |
|  | Pt3916 | 10069 | Pt3916. |
|  | Pt3920 | 10053 | Pt3920. |
|  | Pt3928 | 12483 | Pt3928. |
|  | Custom | 10137 | You must use RtdA, RtdB, and RtdC to supply the coefficients for the Callendar-Van Dusen equation. |

##### Remarks

type

RtdType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airvdtsensitivityunits.htm language=enus -->
## TOPIC 00480: AIRvdtSensitivityUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airvdtsensitivityunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_airvdtsensitivityunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIRvdtSensitivityUnits Enumeration

### AIRvdtSensitivityUnits Enumeration

RvdtSensitivity

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIRvdtSensitivityUnits
```

```text
Public Enumeration AIRvdtSensitivityUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | MillivoltsPerVoltPerDegree | 12507 | mVolts/Volt/Degree. |
|  | MillivoltsPerVoltPerRadian | 12508 | mVolts/Volt/Radian. |

##### Remarks

RvdtSensitivity

RvdtSensitivityUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aitemperatureunits.htm language=enus -->
## TOPIC 00481: AITemperatureUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aitemperatureunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aitemperatureunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AITemperatureUnits Enumeration

### AITemperatureUnits Enumeration

Specifies the units to use to return temperature measurements from the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AITemperatureUnits
```

```text
Public Enumeration AITemperatureUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | DegreesC | 10143 | Degrees Celsius. |
|  | DegreesF | 10144 | Degrees Fahrenheit. |
|  | Kelvins | 10325 | Kelvins. |
|  | DegreesR | 10145 | Degrees Rankine. |
|  | FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

##### Remarks

TemperatureUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aivelocityunits.htm language=enus -->
## TOPIC 00482: AIVelocityUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aivelocityunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aivelocityunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIVelocityUnits Enumeration

### AIVelocityUnits Enumeration

Specifies in which unit to return velocity measurements from the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIVelocityUnits
```

```text
Public Enumeration AIVelocityUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | MetersPerSecond | 15959 | Meters per second. |
|  | InchesPerSecond | 15960 | Inches per second. |
|  | FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

##### Remarks

VelocityUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aivoltageacrmsunits.htm language=enus -->
## TOPIC 00483: AIVoltageAcrmsUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aivoltageacrmsunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aivoltageacrmsunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIVoltageAcrmsUnits Enumeration

### AIVoltageAcrmsUnits Enumeration

Specifies the units to use to return voltage RMS measurements from the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIVoltageAcrmsUnits
```

```text
Public Enumeration AIVoltageAcrmsUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Volts | 10348 | Volts. |
|  | FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |
|  | FromTeds | 12516 | Units defined by TEDS information associated with the channel. |

##### Remarks

VoltageAcrmsUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aivoltageunits.htm language=enus -->
## TOPIC 00484: AIVoltageUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aivoltageunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aivoltageunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AIVoltageUnits Enumeration

### AIVoltageUnits Enumeration

Specifies the units to use to return voltage measurements from the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AIVoltageUnits
```

```text
Public Enumeration AIVoltageUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Volts | 10348 | Volts. |
|  | FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |
|  | FromTeds | 12516 | Units defined by TEDS information associated with the channel. |

##### Remarks

VoltageUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogedgestarttrigger.htm language=enus -->
## TOPIC 00485: AnalogEdgeStartTrigger Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogedgestarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogedgestarttrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeStartTrigger Class

### AnalogEdgeStartTrigger Class

analog edge

start triggers

StartTrigger

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class AnalogEdgeStartTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class AnalogEdgeStartTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The AnalogEdgeStartTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Coupling | Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. |
|  | DigitalFilterEnable | Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay above or below the trigger level for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the hysteresis window rapidly. |
|  | DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
|  | DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | Hysteresis | Specifies a hysteresis level in the units of the measurement or generation. If Slope is Rising, the trigger does not deassert until the source signal passes below Level minus the hysteresis. If Slope is Falling, the trigger does not deassert until the source signal passes above Level plus the hysteresis. Hysteresis is always enabled. Set this property to a non-zero value to use hysteresis. |
|  | Level | Specifies at what threshold in the units of the measurement or generation to start acquiring or generating samples. Use Slope to specify on which slope to trigger on this threshold. |
|  | Slope | Specifies on which slope of the trigger signal to start acquiring or generating samples. |
|  | Source | Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Start Trigger. |

Top

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

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogedgestarttriggerslope.htm language=enus -->
## TOPIC 00486: AnalogEdgeStartTriggerSlope Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogedgestarttriggerslope.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogedgestarttriggerslope.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogEdgeStartTriggerSlope Enumeration

### AnalogEdgeStartTriggerSlope Enumeration

Specifies on which slope of the trigger signal to start acquiring or generating samples.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AnalogEdgeStartTriggerSlope
```

```text
Public Enumeration AnalogEdgeStartTriggerSlope
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Trigger on the rising slope of the signal. |
|  | Falling | 10171 | Trigger on the falling slope of the signal. |

##### Remarks

Slope

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogmultiedgereferencetriggercoupling.htm language=enus -->
## TOPIC 00487: AnalogMultiEdgeReferenceTriggerCoupling Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogmultiedgereferencetriggercoupling.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogmultiedgereferencetriggercoupling.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiEdgeReferenceTriggerCoupling Enumeration

### AnalogMultiEdgeReferenceTriggerCoupling Enumeration

Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AnalogMultiEdgeReferenceTriggerCoupling
```

```text
Public Enumeration AnalogMultiEdgeReferenceTriggerCoupling
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AC | 10045 | Alternating Current. |
|  | DC | 10050 | Direct Current. |

##### Remarks

Couplings

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogmultiedgereferencetriggerslope.htm language=enus -->
## TOPIC 00488: AnalogMultiEdgeReferenceTriggerSlope Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogmultiedgereferencetriggerslope.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogmultiedgereferencetriggerslope.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiEdgeReferenceTriggerSlope Enumeration

### AnalogMultiEdgeReferenceTriggerSlope Enumeration

Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AnalogMultiEdgeReferenceTriggerSlope
```

```text
Public Enumeration AnalogMultiEdgeReferenceTriggerSlope
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Trigger on the rising slope of the signal. |
|  | Falling | 10171 | Trigger on the falling slope of the signal. |

##### Remarks

Slopes

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogmultiedgestarttriggercoupling.htm language=enus -->
## TOPIC 00489: AnalogMultiEdgeStartTriggerCoupling Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogmultiedgestarttriggercoupling.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogmultiedgestarttriggercoupling.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogMultiEdgeStartTriggerCoupling Enumeration

### AnalogMultiEdgeStartTriggerCoupling Enumeration

Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AnalogMultiEdgeStartTriggerCoupling
```

```text
Public Enumeration AnalogMultiEdgeStartTriggerCoupling
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AC | 10045 | Alternating Current. |
|  | DC | 10050 | Direct Current. |

##### Remarks

Couplings

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogunscaledreader.htm language=enus -->
## TOPIC 00490: AnalogUnscaledReader Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogunscaledreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogunscaledreader.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogUnscaledReader Class

### AnalogUnscaledReader Class

Contains methods that read unscaled samples from a task.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class AnalogUnscaledReader : MarshalByRefObject, 
	ISynchronizeCallbacks, ISupportSynchronizationContext
```

```text
Public Class AnalogUnscaledReader
	Inherits MarshalByRefObject
	Implements ISynchronizeCallbacks, ISupportSynchronizationContext
```

The AnalogUnscaledReader type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | AnalogUnscaledReader | Creates a new instance of the AnalogUnscaledReader class to read from the specified DaqStream. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginReadInt16 | Begins an asynchronous read of one or more unscaled 16-bit integer samples from one or more AIChannel objects in a task. |
|  | BeginReadInt32 | Begins an asynchronous read of one or more unscaled 32-bit integer samples from one or more AIChannel objects in a task. |
|  | BeginReadUInt16 | Begins an asynchronous read of one or more unscaled 16-bit unsigned integer samples from one or more AIChannel objects in a task. |
|  | BeginReadUInt32 | Begins an asynchronous read of one or more unscaled 32-bit unsigned integer samples from one or more AIChannel objects in a task. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndReadInt16 | Handles the end of an asynchronous read initiated with BeginReadInt16(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadInt32 | Handles the end of an asynchronous read initiated with BeginReadInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadUInt16 | Handles the end of an asynchronous read initiated with BeginReadUInt16(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadUInt32 | Handles the end of an asynchronous read initiated with BeginReadUInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ReadInt16 | Reads one or more unscaled 16-bit integer samples from one or more AIChannel objects in a task. |
|  | ReadInt32 | Reads one or more unscaled 32-bit integer samples from one or more AIChannel objects in a task. |
|  | ReadUInt16 | Reads one or more unscaled 16-bit unsigned integer samples from one or more AIChannel objects in a task. |
|  | ReadUInt32 | Reads one or more unscaled 32-bit unsigned integer samples from one or more AIChannel objects in a task. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogunscaledwriter.htm language=enus -->
## TOPIC 00491: AnalogUnscaledWriter Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogunscaledwriter.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogunscaledwriter.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogUnscaledWriter Class

### AnalogUnscaledWriter Class

Contains methods that write unscaled samples to a task.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class AnalogUnscaledWriter : MarshalByRefObject, 
	ISynchronizeCallbacks, ISupportSynchronizationContext
```

```text
Public Class AnalogUnscaledWriter
	Inherits MarshalByRefObject
	Implements ISynchronizeCallbacks, ISupportSynchronizationContext
```

The AnalogUnscaledWriter type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | AnalogUnscaledWriter | Creates a new instance of the AnalogUnscaledWriter class to write to the specified DaqStream. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginWrite(Boolean, Int16, AsyncCallback, Object) | Begins an asynchronous write of one or more unscaled 16-bit integer samples to one or more AOChannel objects in a task. |
|  | BeginWrite(Boolean, Int32, AsyncCallback, Object) | Begins an asynchronous write of one or more unscaled 32-bit integer samples to one or more AOChannel objects in a task. |
|  | BeginWrite(Boolean, UInt16, AsyncCallback, Object) | Begins an asynchronous write of one or more unscaled 16-bit unsigned integer samples to one or more AOChannel objects in a task. |
|  | BeginWrite(Boolean, UInt32, AsyncCallback, Object) | Begins an asynchronous write of one or more unscaled 32-bit unsigned integer samples to one or more AOChannel objects in a task. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndWrite | Handles the end of an asynchronous write initiated with BeginWrite(Boolean, UInt16, AsyncCallback, Object). |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |
|  | Write(Boolean, Int16) | Writes one or more unscaled 16-bit integer samples to one or more AOChannel objects in a task. |
|  | Write(Boolean, Int32) | Writes one or more unscaled 32-bit integer samples to one or more AOChannel objects in a task. |
|  | Write(Boolean, UInt16) | Writes one or more unscaled 16-bit unsigned integer samples to one or more AOChannel objects in a task. |
|  | Write(Boolean, UInt32) | Writes one or more unscaled 32-bit unsigned integer samples to one or more AOChannel objects in a task. |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogwindowpausetriggercondition.htm language=enus -->
## TOPIC 00492: AnalogWindowPauseTriggerCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogwindowpausetriggercondition.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogwindowpausetriggercondition.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogWindowPauseTriggerCondition Enumeration

### AnalogWindowPauseTriggerCondition Enumeration

WindowBottom

WindowTop

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AnalogWindowPauseTriggerCondition
```

```text
Public Enumeration AnalogWindowPauseTriggerCondition
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | InsideWindow | 10199 | Pause the measurement or generation while the trigger is inside the window. |
|  | OutsideWindow | 10251 | Pause the measurement or generation while the signal is outside the window. |

##### Remarks

WindowBottom

WindowTop

Condition

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogwindowstarttrigger.htm language=enus -->
## TOPIC 00493: AnalogWindowStartTrigger Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogwindowstarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogwindowstarttrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogWindowStartTrigger Class

### AnalogWindowStartTrigger Class

analog window

start triggers

StartTrigger

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class AnalogWindowStartTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class AnalogWindowStartTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The AnalogWindowStartTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Condition | Specifies whether the task starts acquiring or generating samples when the signal enters or leaves the window you specify with WindowBottom and WindowTop. |
|  | Coupling | Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. |
|  | DigitalFilterEnable | Specifies whether to apply a digital filter to the digital output of the analog triggering circuitry (the Analog Comparison Event). When enabled, the analog signal must stay within the trigger window for the minimum pulse width before being recognized. Use filtering for noisy trigger signals that transition in and out of the window rapidly. |
|  | DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
|  | DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | Source | Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Start Trigger. |
|  | WindowBottom | Specifies the lower limit of the window. Specify this value in the units of the measurement or generation. |
|  | WindowTop | Specifies the upper limit of the window. Specify this value in the units of the measurement or generation. |

Top

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

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogwindowstarttriggercoupling.htm language=enus -->
## TOPIC 00494: AnalogWindowStartTriggerCoupling Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogwindowstarttriggercoupling.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_analogwindowstarttriggercoupling.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogWindowStartTriggerCoupling Enumeration

### AnalogWindowStartTriggerCoupling Enumeration

terminal

virtual channel

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AnalogWindowStartTriggerCoupling
```

```text
Public Enumeration AnalogWindowStartTriggerCoupling
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AC | 10045 | Alternating Current. |
|  | DC | 10050 | Direct Current. |

##### Remarks

terminal

virtual channel

Coupling

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aofunctiongenerationmodulationtype.htm language=enus -->
## TOPIC 00495: AOFunctionGenerationModulationType Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aofunctiongenerationmodulationtype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aofunctiongenerationmodulationtype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AOFunctionGenerationModulationType Enumeration

### AOFunctionGenerationModulationType Enumeration

Specifies if the device generates a modulated version of the waveform using the original waveform as a carrier and input from an external terminal as the signal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AOFunctionGenerationModulationType
```

```text
Public Enumeration AOFunctionGenerationModulationType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AM | 14756 | Amplitude modulation. |
|  | FM | 14757 | Frequency modulation. |
|  | None | 10230 | No modulation. |

##### Remarks

FunctionGenerationModulationType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aooutputtype.htm language=enus -->
## TOPIC 00496: AOOutputType Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aooutputtype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aooutputtype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AOOutputType Enumeration

### AOOutputType Enumeration

Indicates whether the channel generates voltage, current, or a waveform.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AOOutputType
```

```text
Public Enumeration AOOutputType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Voltage | 10322 | Voltage generation. |
|  | Current | 10134 | Current generation. |
|  | FunctionGeneration | 14750 | Function generation. |

##### Remarks

OutputType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aopowerupoutputbehavior.htm language=enus -->
## TOPIC 00497: AOPowerUpOutputBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aopowerupoutputbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aopowerupoutputbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AOPowerUpOutputBehavior Enumeration

### AOPowerUpOutputBehavior Enumeration

Specifies the analog output state of the physical channels for some devices when your computer is powered on or the device is reset in NI-DAQmx.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AOPowerUpOutputBehavior
```

```text
Public Enumeration AOPowerUpOutputBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Voltage | 10322 | Voltage output. |
|  | Current | 10134 | Current output. |
|  | HighImpedance | 12527 | High-impedance state. |

##### Remarks

For all NI-DAQmx simulated devices, power-up states are not persisted.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aoresolutionunits.htm language=enus -->
## TOPIC 00498: AOResolutionUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aoresolutionunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_aoresolutionunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

AOResolutionUnits Enumeration

### AOResolutionUnits Enumeration

Resolution

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum AOResolutionUnits
```

```text
Public Enumeration AOResolutionUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Bits | 10109 | Bits. |

##### Remarks

Resolution

ResolutionUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_armstarttrigger.htm language=enus -->
## TOPIC 00499: ArmStartTrigger Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_armstarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_armstarttrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ArmStartTrigger Class

### ArmStartTrigger Class

arms the task for a start trigger

StartTrigger

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class ArmStartTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class ArmStartTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The ArmStartTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DigitalEdge | Gets the DigitalEdgeArmStartTrigger. |
|  | Terminal | Indicates the name of the internal Arm Start Trigger terminal for the task. This property does not return the name of the trigger source terminal. |
|  | Time | Gets the TimeArmStartTrigger. |
|  | Timestamp | Gets the arm start trigger timestamp. |
|  | TimestampEnable | Specifies whether the arm start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time. |
|  | TimestampTimescale | Specifies the arm start trigger timestamp timescale. |
|  | Type | Specifies the type of trigger to use to arm the task for a Start Trigger. If you configure an Arm Start Trigger, the task does not respond to a Start Trigger until the device receives the Arm Start Trigger. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureDigitalEdgeTrigger | Configures a task to arm for a start trigger upon a rising or falling edge of a digital signal. |
|  | ConfigureNone | Disables arm start triggering for the task. |
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

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_armstarttriggertimestamptimescale.htm language=enus -->
## TOPIC 00500: ArmStartTriggerTimestampTimescale Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_armstarttriggertimestamptimescale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_armstarttriggertimestamptimescale.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ArmStartTriggerTimestampTimescale Enumeration

### ArmStartTriggerTimestampTimescale Enumeration

Specifies the arm start trigger timestamp timescale.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ArmStartTriggerTimestampTimescale
```

```text
Public Enumeration ArmStartTriggerTimestampTimescale
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | HostTime | 16126 | Use the host device. |
|  | IODeviceTime | 16127 | Use the I/O device. |

##### Remarks

TimestampTimescale

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
