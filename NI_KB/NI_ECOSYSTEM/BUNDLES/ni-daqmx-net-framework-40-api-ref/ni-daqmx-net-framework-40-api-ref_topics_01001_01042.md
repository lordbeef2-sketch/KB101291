# NI DOCUMENT BUNDLE: ni-daqmx-net-framework-40-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-net-framework-40-api-ref start=1001 end=1042 -->
<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_physicalchanneltypes.htm language=enus -->
## TOPIC 01001: PhysicalChannelTypes Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_physicalchanneltypes.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_physicalchanneltypes.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannelTypes Enumeration

### PhysicalChannelTypes Enumeration

Specifies the types of physical channels to include when requesting a list of 
physical channels.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[FlagsAttribute]
public enum PhysicalChannelTypes
```

```text
<FlagsAttribute>
Public Enumeration PhysicalChannelTypes
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AI | 1 | Analog inputs. |
|  | AO | 2 | Analog outputs. |
|  | DILine | 4 | Digital input lines. |
|  | DIPort | 8 | Digital input ports. |
|  | DOLine | 16 | Digital output lines. |
|  | DOPort | 32 | Digital output ports. |
|  | CI | 64 | Counter inputs. |
|  | CO | 128 | Counter outputs. |
|  | All | 255 | All types of physical channels. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_polynomialdirection.htm language=enus -->
## TOPIC 01002: PolynomialDirection Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_polynomialdirection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_polynomialdirection.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PolynomialDirection Enumeration

### PolynomialDirection Enumeration

Specifies the direction of the conversion the provided polynomial coefficients perform.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum PolynomialDirection
```

```text
Public Enumeration PolynomialDirection
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Forward | 0 | The provided coefficients are the coefficients of the forward polynomial. |
|  | Reverse | 1 | The provided coefficients are the coefficients of the reverse polynomial. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_productcategory.htm language=enus -->
## TOPIC 01003: ProductCategory Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_productcategory.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_productcategory.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ProductCategory Enumeration

### ProductCategory Enumeration

Indicates the product category of the device. This category corresponds to the category displayed in MAX when creating NI-DAQmx simulated devices.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ProductCategory
```

```text
Public Enumeration ProductCategory
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | MSeriesDaq | 14643 | M Series DAQ. |
|  | XSeriesDaq | 15858 | X Series DAQ. |
|  | ESeriesDaq | 14642 | E Series DAQ. |
|  | SSeriesDaq | 14644 | S Series DAQ. |
|  | BSeriesDaq | 14662 | B Series DAQ. |
|  | SCSeriesDaq | 14645 | SC Series DAQ. |
|  | UsbDaq | 14646 | USB DAQ. |
|  | AOSeries | 14647 | AO Series. |
|  | DigitalIO | 14648 | Digital I/O. |
|  | TioSeries | 14661 | TIO Series. |
|  | DynamicSignalAcquisition | 14649 | Dynamic Signal Acquisition. |
|  | Switches | 14650 | Switches. |
|  | CompactDaqChassis | 14658 | CompactDAQ chassis. |
|  | CompactRioChassis | 16144 | CompactRIO Chassis. |
|  | CSeriesModule | 14659 | C Series I/O module. |
|  | ScxiModule | 14660 | SCXI module. |
|  | SccConnectorBlock | 14704 | SCC Connector Block. |
|  | SccModule | 14705 | SCC Module. |
|  | NIElvis | 14755 | NI ELVIS. |
|  | NetworkDAQ | 14829 | Network DAQ. |
|  | SCExpress | 15886 | SC Express. |
|  | FieldDaq | 16151 | FieldDAQ. |
|  | Unknown | 12588 | Unknown category. |

##### Remarks

ProductCategory

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_propertyfiltertype.htm language=enus -->
## TOPIC 01004: PropertyFilterType Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_propertyfiltertype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_propertyfiltertype.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PropertyFilterType Enumeration

### PropertyFilterType Enumeration

Specifies the type of property filtering to perform.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum PropertyFilterType
```

```text
Public Enumeration PropertyFilterType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | All | 0 | Returns all of the properties that belong to the Task subobject. |
|  | ConfiguredDevices | 1 | Returns only the properties that apply to the configured devices on the system and belong to the Task subobject. |
|  | DevicesInTask | 2 | Returns only the properties that apply to the devices being used in the task and belong to the Task subobject. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_readoverwritemode.htm language=enus -->
## TOPIC 01005: ReadOverwriteMode Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_readoverwritemode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_readoverwritemode.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ReadOverwriteMode Enumeration

### ReadOverwriteMode Enumeration

Specifies whether to overwrite samples in the buffer that you have not yet read.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ReadOverwriteMode
```

```text
Public Enumeration ReadOverwriteMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | OverwriteUnreadSamples | 10252 | When an acquisition encounters unread data in the buffer, the acquisition continues and overwrites the unread samples with new ones. You can read the new samples by setting ReadRelativeTo to MostRecentSample and setting ReadOffset to the appropriate number of samples. |
|  | DoNotOverwriteUnreadSamples | 10159 | The acquisition stops when it encounters a sample in the buffer that you have not read. |

##### Remarks

ReadOverwriteMode

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_reallocationpolicy.htm language=enus -->
## TOPIC 01006: ReallocationPolicy Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_reallocationpolicy.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_reallocationpolicy.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ReallocationPolicy Enumeration

### ReallocationPolicy Enumeration

Specifies the behavior of a memory-optimized read method operation when the operation yields more samples than the current capacity of the buffer can allocate.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ReallocationPolicy
```

```text
Public Enumeration ReallocationPolicy
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | DoNotReallocate | 0 | The read operation is limited to read up to the capacity of the provided buffer. |
|  | ToGrow | 1 | The read operation can request more memory if the operation yields more samples than the capacity of the provided buffer. You must use initialized data; otherwise, your application could throw a DaqException. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_referencetrigger.htm language=enus -->
## TOPIC 01007: ReferenceTrigger Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_referencetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_referencetrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTrigger Class

### ReferenceTrigger Class

reference point between the pretrigger samples and the post-trigger samples

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class ReferenceTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class ReferenceTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The ReferenceTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AnalogEdge | Gets the AnalogEdgeReferenceTrigger. |
|  | AnalogMultiEdge | Gets the AnalogMultiEdgeReferenceTrigger. |
|  | AnalogWindow | Gets the AnalogWindowReferenceTrigger. |
|  | AutoTriggered | Indicates whether a completed acquisition was triggered by the auto trigger. If an acquisition has not completed after the task starts, this property returns . This property is only applicable when AutoTriggerEnable is . |
|  | AutoTriggerEnable | Specifies whether to send a software trigger to the device when a hardware trigger is no longer active in order to prevent a timeout. |
|  | Delay | Specifies in seconds the time to wait after the device receives the Reference Trigger before switching from pretrigger to posttrigger samples. |
|  | DigitalEdge | Gets the DigitalEdgeReferenceTrigger. |
|  | DigitalPattern | Gets the DigitalPatternReferenceTrigger. |
|  | MaximumNumberOfTriggersToDetect | Specifies the maximum number of times the task will detect a reference trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum Number of Triggers to Detect to be 0 causes the driver to automatically set this value to the maximum possible number of triggers detectable by the device and configuration combination. Note: The number of detected triggers may be less than number of trigger events occurring, because the devices were unable to respond to the trigger. |
|  | PretriggerSamples | Specifies the minimum number of pretrigger samples to acquire from each channel before recognizing the reference trigger. Post-trigger samples per channel are equal to SamplesPerChannel minus the number of pretrigger samples per channel. |
|  | Retriggerable | Specifies whether a finite task resets, acquires pretrigger samples, and waits for another Reference Trigger after the task completes. When you set this property to TRUE, the device will acquire post-trigger samples, reset, and acquire pretrigger samples each time the Reference Trigger occurs until the task stops. The device ignores a trigger if it is in the process of acquiring signals. |
|  | RetriggerWindow | Specifies the duration in seconds after each trigger during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. Specifying a Retrigger Window of -1 causes the window to be infinite. |
|  | Terminal | Indicates the name of the internal Reference Trigger terminal for the task. This property does not return the name of the trigger source terminal. |
|  | Timestamp | Gets the reference trigger timestamp. |
|  | TimestampEnable | Specifies whether the reference trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time. |
|  | TimestampTimescale | Specifies the reference trigger timestamp timescale. |
|  | TriggerWindow | Specifies the duration in seconds after the task starts during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. If no triggers are detected during the entire period, then no data will be returned. Specifying a Trigger Window of -1 causes the window to be infinite. |
|  | Type | Specifies the type of trigger to use to mark a reference point for the measurement. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAnalogEdgeTrigger | Configures the task to stop the acquisition when the device acquires all pretrigger samples; an analog signal reaches the level you specify; and the device acquires all post-trigger samples. |
|  | ConfigureAnalogMultiEdgeTrigger | Configures the task to stop the acquisition when the device acquires all pretrigger samples, any of the configured analog signals reaches the levels you specify, and the device acquires all post-trigger samples. |
|  | ConfigureAnalogWindowTrigger | Configures the task to stop the acquisition when the device acquires all pretrigger samples; an analog signal enters or leaves a range you specify; and the device acquires all post-trigger samples. |
|  | ConfigureDigitalEdgeTrigger | Configures the task to stop the acquisition when the device acquires all pretrigger samples, detects a rising or falling edge of a digital signal, and acquires all post-trigger samples. |
|  | ConfigureDigitalPatternTrigger | Configures a task to stop the acquisition when the device acquires all pretrigger samples, matches a digital pattern, and acquires all posttrigger samples. |
|  | ConfigureNone | Disables reference triggering for the measurement. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_referencetriggerpulsepolarity.htm language=enus -->
## TOPIC 01008: ReferenceTriggerPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_referencetriggerpulsepolarity.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_referencetriggerpulsepolarity.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTriggerPulsePolarity Enumeration

### ReferenceTriggerPulsePolarity Enumeration

Specifies the polarity of the exported Reference Trigger.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ReferenceTriggerPulsePolarity
```

```text
Public Enumeration ReferenceTriggerPulsePolarity
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ActiveHigh | 10095 | High state is the active state. |
|  | ActiveLow | 10096 | Low state is the active state. |

##### Remarks

ReferenceTriggerPulsePolarity

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_referencetriggertype.htm language=enus -->
## TOPIC 01009: ReferenceTriggerType Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_referencetriggertype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_referencetriggertype.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTriggerType Enumeration

### ReferenceTriggerType Enumeration

type

reference

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ReferenceTriggerType
```

```text
Public Enumeration ReferenceTriggerType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AnalogEdge | 10099 | Trigger when an analog signal signal crosses a threshold. |
|  | AnalogMultiEdge | 16108 | Trigger when any of the configured analog signals cross their respective thresholds. |
|  | DigitalEdge | 10150 | Trigger on the rising or falling edge of a digital signal. |
|  | DigitalPattern | 10398 | Trigger when digital physical channels match a digital pattern. |
|  | AnalogWindow | 10103 | Trigger when an analog signal enters or leaves a range of values. The range is in the units of the measurement. |
|  | Time | 15996 | Trigger when a specified time is reached. |
|  | None | 10230 | Disable triggering for the task. |

##### Remarks

type

reference

Type

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_sampleclockeventhandler.htm language=enus -->
## TOPIC 01010: SampleClockEventHandler Delegate

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_sampleclockeventhandler.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_sampleclockeventhandler.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SampleClockEventHandler Delegate

### SampleClockEventHandler Delegate

SampleClock

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public delegate void SampleClockEventHandler(
	Object sender,
	SampleClockEventArgs e
)
```

```text
Public Delegate Sub SampleClockEventHandler ( 
	sender As Object,
	e As SampleClockEventArgs
)
```

###### Parameters

- **sender**
  - Type: SystemObject The Task that caused this event.
- **e**
  - Type: NationalInstruments.DAQmxSampleClockEventArgs A SampleClockEventArgs that contains the event data.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_sampleclocktimebaseactiveedge.htm language=enus -->
## TOPIC 01011: SampleClockTimebaseActiveEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_sampleclocktimebaseactiveedge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_sampleclocktimebaseactiveedge.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SampleClockTimebaseActiveEdge Enumeration

### SampleClockTimebaseActiveEdge Enumeration

Specifies on which edge to recognize a Sample Clock Timebase pulse. This property is useful primarily when the signal you use as the Sample Clock Timebase is not a periodic clock.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum SampleClockTimebaseActiveEdge
```

```text
Public Enumeration SampleClockTimebaseActiveEdge
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Rising edge(s). |
|  | Falling | 10171 | Falling edge(s). |

##### Remarks

SampleClockTimebaseActiveEdge

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_sampleclocktimingresponsemode.htm language=enus -->
## TOPIC 01012: SampleClockTimingResponseMode Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_sampleclocktimingresponsemode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_sampleclocktimingresponsemode.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SampleClockTimingResponseMode Enumeration

### SampleClockTimingResponseMode Enumeration

Specifies how the device responds to the sample clock and to triggers.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum SampleClockTimingResponseMode
```

```text
Public Enumeration SampleClockTimingResponseMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | SingleCycle | 14613 | Device responds by the next sample clock edge. |
|  | Multicycle | 14614 | Device acquires or generates samples on the next sample clock edge, but does not respond to certain triggers until a few sample clock edges later. Refer to device documentation for information about which triggers the multicycle response mode affects. This response mode allows higher data transfer rates at the cost of increased latency for responding to triggers. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_savedscaleinfo.htm language=enus -->
## TOPIC 01013: SavedScaleInfo Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_savedscaleinfo.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_savedscaleinfo.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SavedScaleInfo Class

### SavedScaleInfo Class

custom scale

GetSavedScaleInfo(String)

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class SavedScaleInfo : MarshalByRefObject, 
	IDisposable
```

```text
Public Class SavedScaleInfo
	Inherits MarshalByRefObject
	Implements IDisposable
```

The SavedScaleInfo type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AllowInteractiveDeletion | Indicates whether the custom scale can be deleted through MAX. |
|  | AllowInteractiveEditing | Indicates whether the custom scale can be edited in the DAQ Assistant. |
|  | Author | Indicates the author of the custom scale. |
|  | Name | Gets the name of the scale. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by SavedScaleInfo. |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by SavedScaleInfo or optionally releases only the unmanaged resources. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_savedtaskinfo.htm language=enus -->
## TOPIC 01014: SavedTaskInfo Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_savedtaskinfo.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_savedtaskinfo.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SavedTaskInfo Class

### SavedTaskInfo Class

task

GetSavedTaskInfo(String)

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class SavedTaskInfo : MarshalByRefObject, 
	IDisposable
```

```text
Public Class SavedTaskInfo
	Inherits MarshalByRefObject
	Implements IDisposable
```

The SavedTaskInfo type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AllowInteractiveDeletion | Indicates whether the task can be deleted through MAX. |
|  | AllowInteractiveEditing | Indicates whether the task can be edited in the DAQ Assistant. |
|  | Author | Indicates the author of the task. |
|  | Name | Gets the name of the task. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by SavedTaskInfo. |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by SavedTaskInfo or optionally releases only the unmanaged resources. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_saveoptions.htm language=enus -->
## TOPIC 01015: SaveOptions Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_saveoptions.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_saveoptions.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SaveOptions Enumeration

### SaveOptions Enumeration

task

local or global channel

custom scale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[FlagsAttribute]
public enum SaveOptions
```

```text
<FlagsAttribute>
Public Enumeration SaveOptions
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AllowInteractiveEditing | 1 | The saved object may be edited through an interactive tool, such as Measurement Automation Explorer (MAX). |
|  | AllowInteractiveDeletion | 2 | The saved object may be deleted through an interactive tool, such as Measurement Automation Explorer (MAX). |
|  | OverwriteExisting | 4 | If a saved object already exists in Measurement Automation Explorer (MAX) with the same name as the new object, the new object overwrites the old object. |
|  | None | 0 | No options are enabled. |
|  | Default | 3 | The AllowInteractiveDeletion and AllowInteractiveEditing options are enabled. |
|  | All | 7 | All options are enabled. |

##### Remarks

You can specify multiple options by using bitwise or combining individual values.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_scale.htm language=enus -->
## TOPIC 01016: Scale Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_scale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_scale.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Scale Class

### Scale Class

custom scale

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public abstract class Scale : MarshalByRefObject, 
	IDisposable
```

```text
Public MustInherit Class Scale
	Inherits MarshalByRefObject
	Implements IDisposable
```

The Scale type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | Scale | Creates a new instance of the Scale class with the specified scale name. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Specifies a description for the scale. |
|  | Name | Gets the name of the scale. |
|  | PreScaledUnits | Specifies the units of the values that you want to scale. |
|  | ScaledUnits | Specifies the units to use for scaled values. You can use an arbitrary string. |
|  | Type | Gets the type of scale. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by Scale. |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by Scale or optionally releases only the unmanaged resources. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

Scale is the base class for [LinearScale](t_nationalinstruments_daqmx_linearscale.htm), [PolynomialScale](t_nationalinstruments_daqmx_polynomialscale.htm), [RangeMapScale](t_nationalinstruments_daqmx_rangemapscale.htm), and [TableScale](t_nationalinstruments_daqmx_tablescale.htm). All instances of Scale are of one of the derived class types. Refer to the derived class documentation for more information.

When you create a scale, you must provide the scale with a name because the scale is associated with channels through its name. You can create and configure a scale in Measurement Automation Explorer (MAX) or with the constructor of a class that derives from Scale.

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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_scaleprescaledunits.htm language=enus -->
## TOPIC 01017: ScalePreScaledUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_scaleprescaledunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_scaleprescaledunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ScalePreScaledUnits Enumeration

### ScalePreScaledUnits Enumeration

Specifies the units of the values that you want to scale.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ScalePreScaledUnits
```

```text
Public Enumeration ScalePreScaledUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Volts | 10348 | Volts. |
|  | Amps | 10342 | Amperes. |
|  | DegreesF | 10144 | Degrees Fahrenheit. |
|  | DegreesC | 10143 | Degrees Celsius. |
|  | DegreesR | 10145 | Degrees Rankine. |
|  | Kelvins | 10325 | Kelvins. |
|  | Strain | 10299 | Strain. |
|  | Ohms | 10384 | Ohms. |
|  | Hertz | 10373 | Hertz. |
|  | Seconds | 10364 | Seconds. |
|  | Meters | 10219 | Meters. |
|  | Inches | 10379 | Inches. |
|  | Degrees | 10146 | Degrees. |
|  | Radians | 10273 | Radians. |
|  | Ticks | 10304 | Ticks. |
|  | RPM | 16080 | Revolutions per minute. |
|  | RadiansPerSecond | 16081 | Radians per second. |
|  | DegreesPerSecond | 16082 | Degrees per second. |
|  | G | 10186 | 1 g is approximately equal to 9.81 m/s/s. |
|  | MetersPerSecondSquared | 12470 | Meters per second per second. |
|  | InchesPerSecondSquared | 12471 | Inches per second per second. |
|  | MetersPerSecond | 15959 | Meters per second. |
|  | InchesPerSecond | 15960 | Inches per second. |
|  | Pascals | 10081 | Pascals. |
|  | Newtons | 15875 | Newtons. |
|  | Pounds | 15876 | Pounds. |
|  | KilogramForce | 15877 | Kilograms-force. |
|  | PoundsPerSquareInch | 15879 | Pounds per square inch. |
|  | Bar | 15880 | Bar. |
|  | NewtonMeters | 15881 | Newton meters. |
|  | InchOunces | 15882 | Ounce-inches. |
|  | InchPounds | 15883 | Pound-inches. |
|  | FootPounds | 15884 | Pound-feet. |
|  | VoltsPerVolt | 15896 | Volts per volt. |
|  | MillivoltsPerVolt | 15897 | Millivolts per volt. |
|  | Coulombs | 16102 | Coulombs. |
|  | PicoCoulombs | 16103 | PicoCoulombs. |
|  | FromTeds | 12516 | Units defined by TEDS information associated with the channel. |

##### Remarks

PreScaledUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_shuntcalibrationselect.htm language=enus -->
## TOPIC 01018: ShuntCalibrationSelect Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_shuntcalibrationselect.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_shuntcalibrationselect.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ShuntCalibrationSelect Enumeration

### ShuntCalibrationSelect Enumeration

Specifies the shunt calibration switch(es) to enable.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ShuntCalibrationSelect
```

```text
Public Enumeration ShuntCalibrationSelect
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | A | 12513 | Switch A |
|  | B | 12514 | Switch B |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_shuntelementlocation.htm language=enus -->
## TOPIC 01019: ShuntElementLocation Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_shuntelementlocation.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_shuntelementlocation.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ShuntElementLocation Enumeration

### ShuntElementLocation Enumeration

Specifies which resistor to use to calibrate the channel(s).

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ShuntElementLocation
```

```text
Public Enumeration ShuntElementLocation
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | R1 | 12465 | Resistor 1. |
|  | R2 | 12466 | Resistor 2. |
|  | R3 | 12467 | Resistor 3. |
|  | R4 | 14813 | Resistor 4. |
|  | None | 10230 | No resistor. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_shuntresistorsource.htm language=enus -->
## TOPIC 01020: ShuntResistorSource Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_shuntresistorsource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_shuntresistorsource.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ShuntResistorSource Enumeration

### ShuntResistorSource Enumeration

Specifies whether to use internal or external shunt.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ShuntResistorSource
```

```text
Public Enumeration ShuntResistorSource
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | UserProvided | 10167 | Use an external shunt. |
|  | BuiltIn | 10200 | Use the internal shunt. |
|  | Default | -1 | Use the default shunt. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_signalroutingmodifiers.htm language=enus -->
## TOPIC 01021: SignalRoutingModifiers Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_signalroutingmodifiers.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_signalroutingmodifiers.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SignalRoutingModifiers Enumeration

### SignalRoutingModifiers Enumeration

inverted

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[FlagsAttribute]
public enum SignalRoutingModifiers
```

```text
<FlagsAttribute>
Public Enumeration SignalRoutingModifiers
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | InvertPolarity | 1 | The signal is inverted. |

##### Remarks

If the device is not capable of signal inversion or if a previous route reserved the inversion circuitry in an incompatible configuration, attempting to invert the signal causes an error.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_singlepoint.htm language=enus -->
## TOPIC 01022: SinglePoint Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_singlepoint.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_singlepoint.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SinglePoint Class

### SinglePoint Class

Task

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class SinglePoint : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class SinglePoint
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The SinglePoint type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | ConvertLateErrorsToWarnings | Specifies if WaitForNextSampleClock(Double), reading from the task, and writing to the task convert late errors to warnings. NI-DAQmx returns no late warnings or errors until the number of warmup iterations you specify with NumberOfWarmupIterations execute. |
|  | NumberOfWarmupIterations | Specifies the number of loop iterations that must occur before WaitForNextSampleClock(Double) and reading from the task return any late warnings or errors. The system needs a number of iterations to stabilize. During this period, a large amount of jitter occurs, potentially causing reads and writes to be late. The default number of warmup iterations is 100. Specify a larger number if needed to stabilize the system. |
|  | ReportMissedSamples | Specifies whether reading from the task returns lateness errors or warnings when it detects missed Sample Clock pulses. This setting does not affect WaitForNextSampleClock(Double). Set this property to for applications that need to detect lateness without using WaitForNextSampleClock(Double). |
|  | WaitForNextSampleClockWaitMode | Specifies how WaitForNextSampleClock(Double) waits for the next Sample Clock pulse. |
|  | WriteRecoveryMode | Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |
|  | WaitForNextSampleClock | Waits until the next pulse of the sample clock occurs, with a timeout value of 10 seconds. |
|  | WaitForNextSampleClock(Double) | Waits until the next pulse of the sample clock occurs. |

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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_starttrigger.htm language=enus -->
## TOPIC 01023: StartTrigger Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_starttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_starttrigger.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

StartTrigger Class

### StartTrigger Class

how the task begins measurement or generation

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class StartTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class StartTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The StartTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AnalogEdge | Gets the AnalogEdgeStartTrigger. |
|  | AnalogMultiEdge | Gets the AnalogMultiEdgeStartTrigger. |
|  | AnalogWindow | Gets the AnalogWindowStartTrigger. |
|  | Delay | Specifies an amount of time to wait after the Start Trigger is received before acquiring or generating the first sample. This value is in the units you specify with DelayUnits. |
|  | DelayUnits | Specifies the units of Delay. |
|  | DigitalEdge | Gets the DigitalEdgeStartTrigger. |
|  | DigitalPattern | Gets the DigitalPatternStartTrigger. |
|  | MaximumNumberOfTriggersToDetect | Specifies the maximum number of times the task will detect a start trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum Number of Triggers to Detect to be 0 causes the driver to automatically set this value to the maximum possible number of triggers detectable by the device and configuration combination. Note: The number of detected triggers may be less than number of trigger events occurring, because the devices were unable to respond to the trigger. |
|  | Retriggerable | Specifies whether a finite task resets and waits for another Start Trigger after the task completes. When you set this property to , the device performs a finite acquisition or generation each time the Start Trigger occurs until the task stops. The device ignores a trigger if it is in the process of acquiring or generating signals. |
|  | RetriggerWindow | Specifies the period of time in seconds after each trigger during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples that it already started. Ensure the period of time specified covers the entire time span desired for retrigger detection to avoid missed triggers. Specifying a Retrigger Window of -1 causes the window to be infinite. |
|  | Terminal | Indicates the name of the internal Start Trigger terminal for the task. This property does not return the name of the trigger source terminal. |
|  | Time | Gets the TimeStartTrigger. |
|  | Timestamp | Gets the start trigger timestamp. |
|  | TimestampEnable | Specifies whether the start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time. |
|  | TimestampTimescale | Specifies the start trigger timestamp timescale. |
|  | TriggerWindow | Specifies the period of time in seconds after the task starts during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples for any triggers detected. If no triggers are detected during the entire period, then no data will be returned. Ensure the period of time specified covers the entire time span desired for trigger detection to avoid missed triggers. Specifying a Trigger Window of -1 causes the window to be infinite. |
|  | Type | Specifies the type of trigger to use to start a task. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAnalogEdgeTrigger | Configures the task to start acquiring or generating samples when an analog signal crosses the level you specify. |
|  | ConfigureAnalogMultiEdgeTrigger | Configures the task to start acquiring or generating samples when any of the configured analog signals cross the respective levels you specify. |
|  | ConfigureAnalogWindowTrigger | Configures the task to start acquiring or generating samples when an analog signal enters or leaves a range you specify. |
|  | ConfigureDigitalEdgeTrigger | Configures the task to start acquiring or generating samples on a rising or falling edge of a digital signal. |
|  | ConfigureDigitalPatternTrigger | Configures the task to start acquiring or generating samples when a digital pattern is matched. |
|  | ConfigureNone | Configures the task to start acquiring or generating samples immediately upon starting the task. |
|  | ConfigureTimeTrigger | Configures the task to start acquiring or generating samples at a the specified triggerTime. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_starttriggerdelayunits.htm language=enus -->
## TOPIC 01024: StartTriggerDelayUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_starttriggerdelayunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_starttriggerdelayunits.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

StartTriggerDelayUnits Enumeration

### StartTriggerDelayUnits Enumeration

Delay

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum StartTriggerDelayUnits
```

```text
Public Enumeration StartTriggerDelayUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | SampleClockPeriods | 10286 | Complete periods of the Sample Clock. |
|  | Seconds | 10364 | Seconds. |
|  | Ticks | 10304 | Timebase ticks. |

##### Remarks

Delay

DelayUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_starttriggerpulsepolarity.htm language=enus -->
## TOPIC 01025: StartTriggerPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_starttriggerpulsepolarity.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_starttriggerpulsepolarity.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

StartTriggerPulsePolarity Enumeration

### StartTriggerPulsePolarity Enumeration

Specifies the polarity of the exported Start Trigger.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum StartTriggerPulsePolarity
```

```text
Public Enumeration StartTriggerPulsePolarity
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ActiveHigh | 10095 | High state is the active state. |
|  | ActiveLow | 10096 | Low state is the active state. |

##### Remarks

StartTriggerPulsePolarity

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_starttriggertimestamptimescale.htm language=enus -->
## TOPIC 01026: StartTriggerTimestampTimescale Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_starttriggertimestamptimescale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_starttriggertimestamptimescale.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

StartTriggerTimestampTimescale Enumeration

### StartTriggerTimestampTimescale Enumeration

Specifies the start trigger timestamp timescale.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum StartTriggerTimestampTimescale
```

```text
Public Enumeration StartTriggerTimestampTimescale
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_starttriggertype.htm language=enus -->
## TOPIC 01027: StartTriggerType Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_starttriggertype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_starttriggertype.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

StartTriggerType Enumeration

### StartTriggerType Enumeration

type

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum StartTriggerType
```

```text
Public Enumeration StartTriggerType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AnalogEdge | 10099 | Trigger when an analog signal signal crosses a threshold. |
|  | AnalogMultiEdge | 16108 | Trigger when any of the configured analog signals cross their respective thresholds. |
|  | DigitalEdge | 10150 | Trigger on the rising or falling edge of a digital signal. |
|  | DigitalPattern | 10398 | Trigger when digital physical channels match a digital pattern. |
|  | AnalogWindow | 10103 | Trigger when an analog signal enters or leaves a range of values. The range is in the units of the measurement. |
|  | Time | 15996 | Trigger when a specified time is reached. |
|  | None | 10230 | Disable triggering for the task. |

##### Remarks

type

Type

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switch.htm language=enus -->
## TOPIC 01028: Switch Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switch.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switch.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Switch Class

### Switch Class

**Note: This API is now obsolete.**

Encapsulates a switch device and contains properties and methods that operate on switch devices outside the context of a task.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This type is obsolete.")]
public class Switch : MarshalByRefObject
```

```text
<ObsoleteAttribute("This type is obsolete.")>
Public Class Switch
	Inherits MarshalByRefObject
```

The Switch type exposes the following members.

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

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | SetTopologyAndReset | Resets a switch device and sets its topology. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |
|  | WaitForSettling | Waits for the settling time on the device to expire. |

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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchchannel.htm language=enus -->
## TOPIC 01029: SwitchChannel Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchchannel.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchChannel Class

### SwitchChannel Class

**Note: This API is now obsolete.**

Encapsulates a channel on a switch device and contains properties and methods that operate on switch channels outside the context of a task. This class also defines the intended use of particular switch channels in tasks.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This type is obsolete.")]
public class SwitchChannel : MarshalByRefObject, 
	IDisposable
```

```text
<ObsoleteAttribute("This type is obsolete.")>
Public Class SwitchChannel
	Inherits MarshalByRefObject
	Implements IDisposable
```

The SwitchChannel type exposes the following members.

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

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by SwitchChannel. |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by SwitchChannel or optionally releases only the unmanaged resources. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

LoadSwitchChannel(String)

Local

DaqSystem

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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchchannelusage.htm language=enus -->
## TOPIC 01030: SwitchChannelUsage Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchchannelusage.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchchannelusage.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchChannelUsage Enumeration

### SwitchChannelUsage Enumeration

**Note: This API is now obsolete.**

Specifies how you can use the channel. Using this property acts as a safety mechanism to prevent you from connecting two source channels, for example.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This enum is obsolete.")]
public enum SwitchChannelUsage
```

```text
<ObsoleteAttribute("This enum is obsolete.")>
Public Enumeration SwitchChannelUsage
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Source | 10439 | You can use the channel only as an input for a signal. |
|  | Load | 10440 | You can use the channel only as the output for a signal passing through the switch. |
|  | ReservedForRouting | 10441 | You can use the channel only to complete routes within a switch. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchpathstatus.htm language=enus -->
## TOPIC 01031: SwitchPathStatus Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchpathstatus.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchpathstatus.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchPathStatus Enumeration

### SwitchPathStatus Enumeration

**Note: This API is now obsolete.**

Specifies the status of the requested path.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This enum is obsolete.")]
public enum SwitchPathStatus
```

```text
<ObsoleteAttribute("This enum is obsolete.")>
Public Enumeration SwitchPathStatus
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | PathAvailable | 10431 | A path is available between the channels. |
|  | PathAlreadyExists | 10432 | The channels are already connected. |
|  | PathUnsupported | 10433 | No path is available between the channels. You might need to reserve more channels for routing to create an available path. |
|  | ChannelInUse | 10434 | The path between the two endpoints is unavailable because another connection is already using a channel needed for routing. |
|  | SourceChannelConflict | 10435 | No path is available between the two channels because connecting the channels would directly or indirectly connect two source channels. |
|  | ChannelReservedForRouting | 10436 | One of the endpoint channels is reserved for routing. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchrelayposition.htm language=enus -->
## TOPIC 01032: SwitchRelayPosition Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchrelayposition.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchrelayposition.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchRelayPosition Enumeration

### SwitchRelayPosition Enumeration

**Note: This API is now obsolete.**

Specifies the position of each specified relay.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This enum is obsolete.")]
public enum SwitchRelayPosition
```

```text
<ObsoleteAttribute("This enum is obsolete.")>
Public Enumeration SwitchRelayPosition
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Open | 10437 | The relay is open. |
|  | Closed | 10438 | The relay is closed. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchscan.htm language=enus -->
## TOPIC 01033: SwitchScan Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchscan.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchscan.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchScan Class

### SwitchScan Class

**Note: This API is now obsolete.**

switch scan list

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This type is obsolete.")]
public class SwitchScan : MarshalByRefObject, IFilteredTypeDescriptor
```

```text
<ObsoleteAttribute("This type is obsolete.")>
Public Class SwitchScan
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The SwitchScan type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | BreakMode | Specifies the action to take between each entry in a scan list. |
|  | IsWaitingForAdvance | Indicates if the switch hardware is waiting for an Advance Trigger. If the hardware is waiting, it completed the previous entry in the scan list. |
|  | RepeatMode | Specifies if the task advances through the scan list multiple times. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
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

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchscanbreakmode.htm language=enus -->
## TOPIC 01034: SwitchScanBreakMode Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchscanbreakmode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_switchscanbreakmode.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchScanBreakMode Enumeration

### SwitchScanBreakMode Enumeration

**Note: This API is now obsolete.**

Specifies the action to take between each entry in a scan list.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This enum is obsolete.")]
public enum SwitchScanBreakMode
```

```text
<ObsoleteAttribute("This enum is obsolete.")>
Public Enumeration SwitchScanBreakMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | NoAction | 10227 | When advancing to the next entry in the scan list, leave all previous connections intact. |
|  | BreakBeforeMake | 10110 | When advancing to the next entry in the scan list, disconnect all previous connections before making any new connections. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_synchronizationpulsetimescale.htm language=enus -->
## TOPIC 01035: SynchronizationPulseTimescale Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_synchronizationpulsetimescale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_synchronizationpulsetimescale.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SynchronizationPulseTimescale Enumeration

### SynchronizationPulseTimescale Enumeration

Specifies the timescale to be used for timestamps for a sync pulse.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum SynchronizationPulseTimescale
```

```text
Public Enumeration SynchronizationPulseTimescale
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | HostTime | 16126 | Use the host device. |
|  | IODeviceTime | 16127 | Use the I/O device. |

##### Remarks

SynchronizationPulseTimescale

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_task.htm language=enus -->
## TOPIC 01036: Task Class

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_task.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_task.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Task Class

### Task Class

virtual channels

DAQmx Task

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class Task : MarshalByRefObject, IDisposable, ISynchronizeCallbacks, 
	ISupportSynchronizationContext
```

```text
Public Class Task
	Inherits MarshalByRefObject
	Implements IDisposable, ISynchronizeCallbacks, ISupportSynchronizationContext
```

The Task type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | Task | Initializes a new instance of the Task class with a unique name. |
|  | Task(String) | Initializes a new instance of the Task class with the specified name. |

Top

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

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | AddGlobalChannel | Adds a preconfigured, global channel to the task. |
|  | ConfigureLogging(String, TdmsLoggingOperation, LoggingMode) | Configures logging to a .tdms file when the acquisition starts. |
|  | ConfigureLogging(String, TdmsLoggingOperation, LoggingMode, String) | Configures logging to a .tdms file when the acquisition starts with the specified TDMS channel group name. |
|  | Control | Alters the state of the task according to the mode you specify. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by Task. |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by Task or optionally releases only the unmanaged resources. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | OnCounterOutput | Raises the CounterOutput event. |
|  | OnDigitalChangeDetection | Raises the DigitalChangeDetection event. |
|  | OnDone | Raises the Done event. |
|  | OnEveryNSamplesRead | Raises the EveryNSamplesRead event. |
|  | OnEveryNSamplesWritten | Raises the EveryNSamplesWritten event. |
|  | OnSampleClock | Raises the SampleClock event. |
|  | OnSampleComplete | Raises the SampleComplete event. |
|  | Start | Transitions the task to the running state, which begins the measurement or generation. |
|  | StartNewFile | Starts a new TDMS file the next time data is written to disk. |
|  | Stop | Transitions the task from the running to the committed state, which ends the measurement or generation. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |
|  | WaitForValidTimestamp(TimestampEvent) | Waits indefinitely until the specified timestampEvent has a value. |
|  | WaitForValidTimestamp(TimestampEvent, TimeSpan) | Waits until the specified timestampEvent has a value. |
|  | WaitUntilDone | Waits for the measurement or generation to complete, regardless of the amount of time needed, and returns if it has completed execution. |
|  | WaitUntilDone(Int32) | Waits for the measurement or generation to complete and returns if it has completed execution before the specified time elapses. |
|  | WaitUntilDone(TimeSpan) | Waits for the measurement or generation to complete and returns if it has completed execution before the specified TimeSpan elapses. |

Top

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

##### Remarks

Task

Task

DaqStream

Task

Stream

Task

| Note |
| --- |
| Some DAQ devices are not currently supported by the NI-DAQmx driver. Refer to NI-DAQ Readme for a complete listing of supported hardware. |

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

###### Other Resources

Tasks

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_taskdoneeventhandler.htm language=enus -->
## TOPIC 01037: TaskDoneEventHandler Delegate

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_taskdoneeventhandler.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_taskdoneeventhandler.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

TaskDoneEventHandler Delegate

### TaskDoneEventHandler Delegate

Done

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public delegate void TaskDoneEventHandler(
	Object sender,
	TaskDoneEventArgs e
)
```

```text
Public Delegate Sub TaskDoneEventHandler ( 
	sender As Object,
	e As TaskDoneEventArgs
)
```

###### Parameters

- **sender**
  - Type: SystemObject The Task that caused this event.
- **e**
  - Type: NationalInstruments.DAQmxTaskDoneEventArgs A TaskDoneEventArgs that contains the event data.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_terminalconfigurationtypes.htm language=enus -->
## TOPIC 01038: TerminalConfigurationTypes Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_terminalconfigurationtypes.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_terminalconfigurationtypes.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

TerminalConfigurationTypes Enumeration

### TerminalConfigurationTypes Enumeration

Specifies a set of terminal configuration types a physical channel may support.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[FlagsAttribute]
public enum TerminalConfigurationTypes
```

```text
<FlagsAttribute>
Public Enumeration TerminalConfigurationTypes
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | None | 0 | Physical channel does not support any terminal configuration types. |
|  | Rse | 1 | Referenced Single-Ended. |
|  | Nrse | 2 | Non-Referenced Single-Ended. |
|  | Differential | 4 | Differential. |
|  | Pseudodifferential | 8 | Pseudodifferential. |

##### Remarks

Specifies a set of terminal configuration types a physical channel may support.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_terminaltypes.htm language=enus -->
## TOPIC 01039: TerminalTypes Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_terminaltypes.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_terminaltypes.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

TerminalTypes Enumeration

### TerminalTypes Enumeration

Specifies the types of terminals to include when requesting a list of terminals.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[FlagsAttribute]
public enum TerminalTypes
```

```text
<FlagsAttribute>
Public Enumeration TerminalTypes
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Basic | 1 | Terminals commonly used in typical measurement applications. |
|  | Advanced | 2 | Terminals that are often internal to a device or terminals rarely used in typical measurement applications. |
|  | All | 3 | Both basic and advanced terminals. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_watchdogdoexpirationstate.htm language=enus -->
## TOPIC 01040: WatchdogDOExpirationState Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_watchdogdoexpirationstate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_watchdogdoexpirationstate.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

WatchdogDOExpirationState Enumeration

### WatchdogDOExpirationState Enumeration

Specifies the state to which to set the digital physical channels when the watchdog task expires. You cannot modify the expiration state of dedicated digital input physical channels.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum WatchdogDOExpirationState
```

```text
Public Enumeration WatchdogDOExpirationState
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | High | 10192 | Logic high. |
|  | Low | 10214 | Logic low. |
|  | Tristate | 10310 | High-impedance state. You can select this state only on devices with bidirectional lines. You cannot select this state for dedicated digital output lines. On some devices, you can select this value only for entire ports. |
|  | NoChange | 10160 | Do not change the state of the lines. On some devices, you can select this value only for entire ports. |

##### Remarks

Specifies the state to which to set the digital physical channels when the watchdog task expires. You cannot modify the expiration state of dedicated digital input physical channels. Use this enumeration to get or set the value of NationalInstruments.DAQmx.Watchdog.DOExpirationState.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_waveformattributemodes.htm language=enus -->
## TOPIC 01041: WaveformAttributeModes Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_waveformattributemodes.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_waveformattributemodes.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

WaveformAttributeModes Enumeration

### WaveformAttributeModes Enumeration

Specifies the type of information returned from waveform reads.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[FlagsAttribute]
public enum WaveformAttributeModes
```

```text
<FlagsAttribute>
Public Enumeration WaveformAttributeModes
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | None | 0 | Returns only the waveform data itself, with no timing information or extended properties. Use this value for optimal performance. |
|  | Timing | 1 | Returns timing information in addition to the waveform data. This value may degrade performance when performing waveform reads. |
|  | ExtendedProperties | 2 | Returns extended properties in addition to the waveform data. This value may degrade performance when performing waveform reads. |

##### Remarks

The value of this property may affect performance when performing waveform reads.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-40-api-ref path=ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_writerecoverymode.htm language=enus -->
## TOPIC 01042: WriteRecoveryMode Enumeration

- bundle_id: `ni-daqmx-net-framework-40-api-ref`
- source_path: `ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_writerecoverymode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-40-api-ref/raw/resource/enus/ninetdaqmxfx40ref/html/t_nationalinstruments_daqmx_writerecoverymode.htm
- document_id: `ni-daqmx-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

WriteRecoveryMode Enumeration

### WriteRecoveryMode Enumeration

Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum WriteRecoveryMode
```

```text
Public Enumeration WriteRecoveryMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | WaitForInterrupt | 12523 | Attempt to recover when the system receives an interrupt service request. This mode is the most CPU efficient and best suited for recovery at lower pulse train frequencies. |
|  | Poll | 12524 | Repeatedly attempt to recover as fast as possible. This mode has the highest probability of recovery success at the expense of CPU efficiency. |

##### Remarks

WriteRecoveryMode

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
