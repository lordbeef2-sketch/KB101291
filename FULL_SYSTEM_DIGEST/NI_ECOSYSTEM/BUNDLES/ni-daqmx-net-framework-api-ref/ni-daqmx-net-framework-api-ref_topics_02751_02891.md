# NI DOCUMENT BUNDLE: ni-daqmx-net-framework-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-net-framework-api-ref start=2751 end=2891 -->
<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-taskdoneeventargs.html language=enus -->
## TOPIC 02751: TaskDoneEventArgs Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-taskdoneeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-taskdoneeventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data for the Done event. Derives fromEventArgsISerializableSyntaxNamespace: NationalInstruments.DAQmxpublic class TaskDoneEventArgs : EventArgs, ISerializableRemarksExample applications are located in the <Public Documents>\National Instruments\NI-DAQ\Examples\DotNET4.x directory or in the

### TaskDoneEventArgs Class

Provides data for the [Done](nationalinstruments-daqmx-task-done.html) event.

#### Derives from

- EventArgs
- ISerializable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class TaskDoneEventArgs : EventArgs, ISerializable

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| TaskDoneEventArgs(Exception) | Initializes a new instance of the TaskDoneEventArgs class with the specified exception. |

#### Properties

| Name | Description |
| --- | --- |
| Error | Gets the Exception that occurred, if any. |

#### Methods

| Name | Description |
| --- | --- |
| GetObjectData(SerializationInfo, StreamingContext) | Sets the SerializationInfo object with information about the exception. |
| CheckForException() | Throws the Exception that occurred, if any exists. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-taskdoneeventhandler__object-taskdoneeventargs.html language=enus -->
## TOPIC 02752: TaskDoneEventHandler Delegate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-taskdoneeventhandler__object-taskdoneeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-taskdoneeventhandler__object-taskdoneeventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the method that handles the Done event. SyntaxNamespace: NationalInstrumentspublic delegate void TaskDoneEventHandler(object sender, TaskDoneEventArgs e)ParametersNameTypeDescriptionsenderobjectThe Task that caused this event.eTaskDoneEventArgsA TaskDoneEventArgs that contains the event d

### TaskDoneEventHandler Delegate

Represents the method that handles the [Done](nationalinstruments-daqmx-task-done.html) event.

#### Syntax

**Namespace:**NationalInstruments

public delegate void TaskDoneEventHandler(object sender, TaskDoneEventArgs e)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sender | object | The Task that caused this event. |
| e | TaskDoneEventArgs | A TaskDoneEventArgs that contains the event data. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-tdmsloggingoperation.html language=enus -->
## TOPIC 02753: TdmsLoggingOperation Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-tdmsloggingoperation.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-tdmsloggingoperation.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how to open the TDMS file. SyntaxNamespace: NationalInstruments.DAQmxpublic enum TdmsLoggingOperationRemarksSpecifies how to open the TDMS file. Use this enumeration to get or set the value of TdmsLoggingOperation.MembersNameValueDescriptionOpen10437Open an existing TDMS file, and append d

### TdmsLoggingOperation Enumeration

Specifies how to open the [TDMS](/csh?context=nidaqmx_mxcncpts_datalogging) file.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum TdmsLoggingOperation

#### Remarks

Specifies how to open the [TDMS](/csh?context=nidaqmx_mxcncpts_datalogging) file. Use this enumeration to get or set the value of [TdmsLoggingOperation](nationalinstruments-daqmx-daqstream-tdmsloggingoperation.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Open | 10437 | Open an existing TDMS file, and append data to that file. If the file does not exist, NI-DAQmx returns an error. |
| OpenOrCreate | 15846 | Open an existing TDMS file, and append data to that file. If the file does not exist, NI-DAQmx creates a new TDMS file. |
| CreateOrReplace | 15847 | Create a new TDMS file, or replace an existing TDMS file. |
| Create | 15848 | Create a new TDMS file. If the file already exists, NI-DAQmx returns an error. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-terminalconfigurationtypes.html language=enus -->
## TOPIC 02754: TerminalConfigurationTypes Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-terminalconfigurationtypes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-terminalconfigurationtypes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a set of terminal configuration types a physical channel may support. SyntaxNamespace: NationalInstruments.DAQmxpublic enum TerminalConfigurationTypesRemarksSpecifies a set of terminal configuration types a physical channel may support.MembersNameValueDescriptionNone0x0Physical channel doe

### TerminalConfigurationTypes Enumeration

Specifies a set of terminal configuration types a physical channel may support.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum TerminalConfigurationTypes

#### Remarks

Specifies a set of terminal configuration types a physical channel may support.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0x0 | Physical channel does not support any terminal configuration types. |
| Rse | 0x1 | Referenced Single-Ended. |
| Nrse | 0x2 | Non-Referenced Single-Ended. |
| Differential | 0x4 | Differential. |
| Pseudodifferential | 0x8 | Pseudodifferential. |

#### See Also

- AITerminalConfigurations
- AOTerminalConfigurations

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-terminaltypes.html language=enus -->
## TOPIC 02755: TerminalTypes Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-terminaltypes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-terminaltypes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the types of terminals to include when requesting a list of terminals. SyntaxNamespace: NationalInstruments.DAQmxpublic enum TerminalTypesMembersNameValueDescriptionBasic0x1Terminals commonly used in typical measurement applications. Advanced0x2Terminals that are often internal to a device

### TerminalTypes Enumeration

Specifies the types of terminals to include when requesting a list of terminals.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum TerminalTypes

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Basic | 0x1 | Terminals commonly used in typical measurement applications. |
| Advanced | 0x2 | Terminals that are often internal to a device or terminals rarely used in typical measurement applications. |
| All | 0x3 | Both basic and advanced terminals. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timearmstarttrigger-timescale.html language=enus -->
## TOPIC 02756: Timescale

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timearmstarttrigger-timescale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timearmstarttrigger-timescale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timescale to be used for timestamps used in an arm start time trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic TimeArmStartTriggerTimescale Timescale { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Timescale

Specifies the timescale to be used for timestamps used in an arm start time trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [TimeArmStartTriggerTimescale](nationalinstruments-daqmx-timearmstarttriggertimescale.html) Timescale { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

TimeArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timearmstarttrigger-tostring.html language=enus -->
## TOPIC 02757: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timearmstarttrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timearmstarttrigger-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

Parent topic:

TimeArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timearmstarttrigger-triggertime.html language=enus -->
## TOPIC 02758: TriggerTime

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timearmstarttrigger-triggertime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timearmstarttrigger-triggertime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets when to trigger the arm start trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic PrecisionDateTime TriggerTime { get; set; }RemarksWhen to trigger the arm start trigger. The trigger time is represented by a PrecisionDateTime expressed as a UTC time. To set a trigger time based on

### TriggerTime

Gets or sets when to trigger the arm start trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public PrecisionDateTime TriggerTime { get; set; }

#### Remarks

When to trigger the arm start trigger.

Note

The trigger time is represented by a PrecisionDateTime expressed as a UTC time. To set a trigger time based on the current system time, use PrecisionDateTime.UtcNow, adding an offset, rather than PrecisionDateTime.Now.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

TimeArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timearmstarttrigger.html language=enus -->
## TOPIC 02759: TimeArmStartTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timearmstarttrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timearmstarttrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides properties for configuring time arm start triggers. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class TimeArmStartTrigger : MarshalByRefObject, IFilteredTypeDescriptorRemarksFor more information refer to Time-Based Features for Netwo

### TimeArmStartTrigger Class

Provides properties for configuring time arm start triggers.

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class TimeArmStartTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Time-Based Features for Network-Synchronized Devices

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Timescale | Specifies the timescale to be used for timestamps used in an arm start time trigger. |
| TriggerTime | Gets or sets when to trigger the arm start trigger. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timearmstarttriggertimescale.html language=enus -->
## TOPIC 02760: TimeArmStartTriggerTimescale Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timearmstarttriggertimescale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timearmstarttriggertimescale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timescale to be used for timestamps used in an arm start time trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic enum TimeArmStartTriggerTimescaleRemarksSpecifies the timescale to be used for timestamps used in an arm start time trigger. Use this enumeration to get or set the va

### TimeArmStartTriggerTimescale Enumeration

Specifies the timescale to be used for timestamps used in an arm start time trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum TimeArmStartTriggerTimescale

#### Remarks

Specifies the timescale to be used for timestamps used in an arm start time trigger. Use this enumeration to get or set the value of [Timescale](nationalinstruments-daqmx-timearmstarttrigger-timescale.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| HostTime | 16126 | Use the host device. |
| IODeviceTime | 16127 | Use the I/O device. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timestampevent.html language=enus -->
## TOPIC 02761: TimestampEvent Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timestampevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timestampevent.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the type of timestamp event. SyntaxNamespace: NationalInstruments.DAQmxpublic enum TimestampEventMembersNameValueDescriptionStartTrigger12491Start trigger timestamp. ReferenceTrigger12490Reference trigger timestamp. ArmStartTrigger14641Arm start trigger timestamp. FirstSample16130First sa

### TimestampEvent Enumeration

Represents the type of timestamp event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum TimestampEvent

#### Members

| Name | Value | Description |
| --- | --- | --- |
| StartTrigger | 12491 | Start trigger timestamp. |
| ReferenceTrigger | 12490 | Reference trigger timestamp. |
| ArmStartTrigger | 14641 | Arm start trigger timestamp. |
| FirstSample | 16130 | First sample timestamp. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timestarttrigger-timescale.html language=enus -->
## TOPIC 02762: Timescale

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timestarttrigger-timescale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timestarttrigger-timescale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timescale to be used for timestamps used in a time trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic TimeStartTriggerTimescale Timescale { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Timescale

Specifies the timescale to be used for timestamps used in a time trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [TimeStartTriggerTimescale](nationalinstruments-daqmx-timestarttriggertimescale.html) Timescale { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

TimeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timestarttrigger-tostring.html language=enus -->
## TOPIC 02763: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timestarttrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timestarttrigger-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

Parent topic:

TimeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timestarttrigger-triggertime.html language=enus -->
## TOPIC 02764: TriggerTime

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timestarttrigger-triggertime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timestarttrigger-triggertime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets when to trigger the start trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic PrecisionDateTime TriggerTime { get; set; }RemarksWhen to trigger the start trigger.The trigger time is represented by a PrecisionDateTime expressed as a UTC time. To set a trigger time based on the curr

### TriggerTime

Gets or sets when to trigger the start trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public PrecisionDateTime TriggerTime { get; set; }

#### Remarks

When to trigger the start trigger.

Note

The trigger time is represented by a PrecisionDateTime expressed as a UTC time. To set a trigger time based on the current system time, use PrecisionDateTime.UtcNow, adding an offset, rather than PrecisionDateTime.Now.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

TimeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timestarttrigger.html language=enus -->
## TOPIC 02765: TimeStartTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timestarttrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timestarttrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides properties for configuring time start triggers. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class TimeStartTrigger : MarshalByRefObject, IFilteredTypeDescriptorRemarksFor more information refer to Time-Based Features for Network-Sync

### TimeStartTrigger Class

Provides properties for configuring time start triggers.

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class TimeStartTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Time-Based Features for Network-Synchronized Devices

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Timescale | Specifies the timescale to be used for timestamps used in a time trigger. |
| TriggerTime | Gets or sets when to trigger the start trigger. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timestarttriggertimescale.html language=enus -->
## TOPIC 02766: TimeStartTriggerTimescale Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timestarttriggertimescale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timestarttriggertimescale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timescale to be used for timestamps used in a time trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic enum TimeStartTriggerTimescaleRemarksSpecifies the timescale to be used for timestamps used in a time trigger. Use this enumeration to get or set the value of Timescale.MembersN

### TimeStartTriggerTimescale Enumeration

Specifies the timescale to be used for timestamps used in a time trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum TimeStartTriggerTimescale

#### Remarks

Specifies the timescale to be used for timestamps used in a time trigger. Use this enumeration to get or set the value of [Timescale](nationalinstruments-daqmx-timestarttrigger-timescale.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| HostTime | 16126 | Use the host device. |
| IODeviceTime | 16127 | Use the I/O device. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-aiconvertactiveedge.html language=enus -->
## TOPIC 02767: AIConvertActiveEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-aiconvertactiveedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-aiconvertactiveedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the clock pulse an analog-to-digital conversion takes place. SyntaxNamespace: NationalInstruments.DAQmxpublic AIConvertActiveEdge AIConvertActiveEdge { get; set; }RemarksThis property is useful primarily when the signal you use as the AI Convert Clock is not a periodic clo

### AIConvertActiveEdge

Specifies on which edge of the clock pulse an analog-to-digital conversion takes place.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIConvertActiveEdge](nationalinstruments-daqmx-aiconvertactiveedge.html) AIConvertActiveEdge { get; set; }

#### Remarks

This property is useful primarily when the signal you use as the AI Convert Clock is not a periodic clock. For example, set this property to [Rising](nationalinstruments-daqmx-aiconvertactiveedge.html) to perform an analog to digital conversion on each rising edge of an aperiodic signal.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-aiconvertmaximumrate.html language=enus -->
## TOPIC 02768: AIConvertMaximumRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-aiconvertmaximumrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-aiconvertmaximumrate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the maximum convert rate supported by the task, given the current devices and channel count. SyntaxNamespace: NationalInstruments.DAQmxpublic double AIConvertMaximumRate { get; }RemarksThis rate is generally faster than the default AI Convert Clock rate selected by NI-DAQmx, because NI-DAQ

### AIConvertMaximumRate

Indicates the maximum convert rate supported by the task, given the current devices and channel count.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double AIConvertMaximumRate { get; }

#### Remarks

This rate is generally faster than the default AI Convert Clock rate selected by NI-DAQmx, because NI-DAQmx adds in an additional 10 microseconds per channel settling time to compensate for most potential system settling constraints.

For single channel tasks, the maximum AI Convert Clock rate is the maximum rate of the ADC. For multiple channel tasks, the maximum AI Convert Clock rate is the maximum convert rate of the analog hardware, including the ADC, filters, multiplexers, and amplifiers. Signal conditioning accessories can further constrain the maximum AI Convert Clock based on timing and settling requirements.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-aiconvertrate.html language=enus -->
## TOPIC 02769: AIConvertRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-aiconvertrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-aiconvertrate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in Hertz the rate at which to clock the analog-to-digital converter. This clock is specific to the analog input section of multiplexed devices. SyntaxNamespace: NationalInstruments.DAQmxpublic double AIConvertRate { get; set; }RemarksBy default, NI-DAQmx selects the maximum convert rate su

### AIConvertRate

Specifies in Hertz the rate at which to clock the analog-to-digital converter. This clock is specific to the analog input section of [multiplexed devices](/csh?context=nidaqmx_mxcncpts_multisimulsamp).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double AIConvertRate { get; set; }

#### Remarks

By default, NI-DAQmx selects the maximum convert rate supported by the device, plus up to 10 microseconds per channel settling time. Other task settings, such as high channel counts or setting [DelayFromSampleClock](nationalinstruments-daqmx-timing-delayfromsampleclock.html), can result in a faster default convert rate.

CompactDAQ applies up to 10 microseconds of settling time for all C Series devices even if the maximum convert rates of the devices differ.

If you connect signal conditioning accessories with track and hold capabilities, such as an SCXI module, to the device, NI-DAQmx uses the fastest convert rate possible that meets the settling requirements for the slowest module sampled. Refer to the device documentation for the signal conditioning accessory for more information.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-aiconvertsource.html language=enus -->
## TOPIC 02770: AIConvertSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-aiconvertsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-aiconvertsource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the AI Convert Clock. SyntaxNamespace: NationalInstruments.DAQmxpublic string AIConvertSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AIConvertSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the AI Convert Clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string AIConvertSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-aiconverttimebasedivisor.html language=enus -->
## TOPIC 02771: AIConvertTimebaseDivisor

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-aiconverttimebasedivisor.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-aiconverttimebasedivisor.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of AI Convert Clock Timebase pulses needed to produce a single AI Convert Clock pulse. SyntaxNamespace: NationalInstruments.DAQmxpublic long AIConvertTimebaseDivisor { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error

### AIConvertTimebaseDivisor

Specifies the number of AI Convert Clock Timebase pulses needed to produce a single AI Convert Clock pulse.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long AIConvertTimebaseDivisor { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-aiconverttimebasesource.html language=enus -->
## TOPIC 02772: AIConvertTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-aiconverttimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-aiconverttimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the AI Convert Clock Timebase. SyntaxNamespace: NationalInstruments.DAQmxpublic AIConvertTimebaseSource AIConvertTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AIConvertTimebaseSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the AI Convert Clock Timebase.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIConvertTimebaseSource](nationalinstruments-daqmx-aiconverttimebasesource.html) AIConvertTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-changedetectiondifallingedgephysicalchannels.html language=enus -->
## TOPIC 02773: ChangeDetectionDIFallingEdgePhysicalChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-changedetectiondifallingedgephysicalchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-changedetectiondifallingedgephysicalchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the names of the digital lines or ports on which to detect falling edges. The lines or ports must be used by virtual channels in the task. You also can specify a string that contains a list or range of digital lines or ports. SyntaxNamespace: NationalInstruments.DAQmxpublic string ChangeDe

### ChangeDetectionDIFallingEdgePhysicalChannels

Specifies the names of the digital lines or ports on which to detect falling edges. The lines or ports must be used by virtual channels in the task. You also can specify a string that contains a [list or range](/csh?context=nidaqmx_mxcncpts_physchannames) of digital lines or ports.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string ChangeDetectionDIFallingEdgePhysicalChannels { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-changedetectiondirisingedgephysicalchannels.html language=enus -->
## TOPIC 02774: ChangeDetectionDIRisingEdgePhysicalChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-changedetectiondirisingedgephysicalchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-changedetectiondirisingedgephysicalchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the names of the digital lines or ports on which to detect rising edges. The lines or ports must be used by virtual channels in the task. You also can specify a string that contains a list or range of digital lines or ports. SyntaxNamespace: NationalInstruments.DAQmxpublic string ChangeDet

### ChangeDetectionDIRisingEdgePhysicalChannels

Specifies the names of the digital lines or ports on which to detect rising edges. The lines or ports must be used by virtual channels in the task. You also can specify a string that contains a [list or range](/csh?context=nidaqmx_mxcncpts_physchannames) of digital lines or ports.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string ChangeDetectionDIRisingEdgePhysicalChannels { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-changedetectionditristate.html language=enus -->
## TOPIC 02775: ChangeDetectionDITristate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-changedetectionditristate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-changedetectionditristate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to tristate lines specified with ChangeDetectionDIRisingEdgePhysicalChannels and ChangeDetectionDIFallingEdgePhysicalChannels that are not in a virtual channel in the task. If you set this property to true, NI-DAQmx tristates rising/falling edge lines that are not in a virtual chan

### ChangeDetectionDITristate

Specifies whether to tristate lines specified with [ChangeDetectionDIRisingEdgePhysicalChannels](nationalinstruments-daqmx-timing-changedetectiondirisingedgephysicalchannels.html) and [ChangeDetectionDIFallingEdgePhysicalChannels](nationalinstruments-daqmx-timing-changedetectiondifallingedgephysicalchannels.html) that are not in a virtual channel in the task. If you set this property to true, NI-DAQmx tristates rising/falling edge lines that are not in a virtual channel in the task. If you set this property to false, NI-DAQmx does not modify the configuration of rising/falling edge lines that are not in a virtual channel in the task, even if the lines were previously tristated. Set this property to false to detect changes on lines in other tasks or to detect changes on output-only lines.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ChangeDetectionDITristate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-changedetectionoverflowed.html language=enus -->
## TOPIC 02776: ChangeDetectionOverflowed

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-changedetectionoverflowed.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-changedetectionoverflowed.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if samples were missed because change detection events occurred faster than the device could handle them. Some devices detect overflows differently than others. SyntaxNamespace: NationalInstruments.DAQmxpublic bool ChangeDetectionOverflowed { get; }ExceptionsTypeDescriptionNationalInstrume

### ChangeDetectionOverflowed

Indicates if samples were missed because change detection events occurred faster than the device could handle them. [Some devices](/csh?context=nidaqmx_mxdevconsid_changedetstaticdio) detect overflows differently than others.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ChangeDetectionOverflowed { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-configurechangedetection__string-string-samplequantitymode-int.html language=enus -->
## TOPIC 02777: ConfigureChangeDetection(string, string, SampleQuantityMode, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-configurechangedetection__string-string-samplequantitymode-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-configurechangedetection__string-string-samplequantitymode-int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the task to acquire samples on the rising and/or falling edges of the specified lines or ports and sets the number of samples to acquire. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureChangeDetection(string diRisingEdgePhysicalChannels, string diFallingEdgePhysicalChannel

### ConfigureChangeDetection(string, string, SampleQuantityMode, int)

Configures the task to acquire samples on the rising and/or falling edges of the specified lines or ports and sets the number of samples to acquire.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureChangeDetection(string diRisingEdgePhysicalChannels, string diFallingEdgePhysicalChannels, SampleQuantityMode sampleMode, int samplesPerChannel)

#### Remarks

Use this method to configure a task to acquire a finite number of samples using [change detection timing](/csh?context=nidaqmx_mxcncpts_smpletimingtype).

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

You cannot apply this method to a subset of devices in the task, and you must apply this method to the task as a whole. You must call this method on the instance of [Timing](nationalinstruments-daqmx-timing.html) returned from the [Timing](nationalinstruments-daqmx-task-timing.html) property on the [Task](nationalinstruments-daqmx-task.html) class. Accessing this method on instances of [Timing](nationalinstruments-daqmx-timing.html) returned from the NationalInstruments.DAQmx.Timing.Item(string) property throws an exception.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| diRisingEdgePhysicalChannels | string | The names of the digital lines or ports on which to detect rising edges. The lines or ports must be contained in the task. You can specify a string that defines a list or range of channels for this parameter. |
| diFallingEdgePhysicalChannels | string | The names of the digital lines or ports on which to detect falling edges. The lines or ports must be contained in the task. You can specify a string that defines a list or range of channels for this parameter. |
| sampleMode | SampleQuantityMode | The duration of the task. A task is either finite and stops when the specified number of samples have been acquired, or it is continuous and continues to acquire samples until the task is explicitly stopped. |
| samplesPerChannel | int | The number of samples to acquire from each channel in the task if sampleMode is FiniteSamples. If sampleMode is ContinuousSamples, NI-DAQmx uses this value to determine the buffer size. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-configurechangedetection__string-string-samplequantitymode.html language=enus -->
## TOPIC 02778: ConfigureChangeDetection(string, string, SampleQuantityMode)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-configurechangedetection__string-string-samplequantitymode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-configurechangedetection__string-string-samplequantitymode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the task to acquire samples on the rising and/or falling edges of the specified lines or ports. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureChangeDetection(string diRisingEdgePhysicalChannels, string diFallingEdgePhysicalChannels, SampleQuantityMode sampleMode)RemarksUs

### ConfigureChangeDetection(string, string, SampleQuantityMode)

Configures the task to acquire samples on the rising and/or falling edges of the specified lines or ports.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureChangeDetection(string diRisingEdgePhysicalChannels, string diFallingEdgePhysicalChannels, SampleQuantityMode sampleMode)

#### Remarks

Use this method to configure a task to continuously acquire samples using [change detection timing](/csh?context=nidaqmx_mxcncpts_smpletimingtype).

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. Overload:NationalInstruments.DAQmx.Timing.ConfigureSampleClock does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task. You start the task with [Start](nationalinstruments-daqmx-task-start.html), by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

You cannot apply this method to a subset of devices in the task, and you must apply this method to the task as a whole. You must call this method on the instance of [Timing](nationalinstruments-daqmx-timing.html) returned from the [Timing](nationalinstruments-daqmx-task-timing.html) property on the [Task](nationalinstruments-daqmx-task.html) class. Accessing this method on instances of [Timing](nationalinstruments-daqmx-timing.html) returned from the NationalInstruments.DAQmx.Timing.Item(string) property throws an exception.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| diRisingEdgePhysicalChannels | string | The names of the digital lines or ports on which to detect rising edges. The lines or ports must be contained in the task. You can specify a string that defines a list or range of channels for this parameter. |
| diFallingEdgePhysicalChannels | string | The names of the digital lines or ports on which to detect falling edges. The lines or ports must be contained in the task. You can specify a string that defines a list or range of channels for this parameter. |
| sampleMode | SampleQuantityMode | The duration of the task. A task is either finite and stops when the specified number of samples have been acquired, or it is continuous and continues to acquire samples until the task is explicitly stopped. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-configurehandshaking__samplequantitymode-int.html language=enus -->
## TOPIC 02779: ConfigureHandshaking(SampleQuantityMode, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-configurehandshaking__samplequantitymode-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-configurehandshaking__samplequantitymode-int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines the sample timing and duration of the task with the specified number of samples, using standard 8255/82C55 digital handshaking between the device and a peripheral device. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureHandshaking(SampleQuantityMode sampleMode, int samplesP

### ConfigureHandshaking(SampleQuantityMode, int)

Determines the sample timing and duration of the task with the specified number of samples, using standard 8255/82C55 [digital handshaking](/csh?context=nidaqmx_mxcncpts_handshaking) between the device and a peripheral device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureHandshaking(SampleQuantityMode sampleMode, int samplesPerChannel)

#### Remarks

Use this method if the task requires a finite number of samples. These [devices](/csh?context=nidaqmx_mxdevconsid_handtiming) support handshake timing.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

You cannot apply this method to a subset of devices in the task, and you must apply this method to the task as a whole. You must call this method on the instance of [Timing](nationalinstruments-daqmx-timing.html) returned from the [Timing](nationalinstruments-daqmx-task-timing.html) property on the [Task](nationalinstruments-daqmx-task.html) class. Accessing this method on instances of [Timing](nationalinstruments-daqmx-timing.html) returned from the NationalInstruments.DAQmx.Timing.Item(string) property throws an exception.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sampleMode | SampleQuantityMode | The duration of the task. A task is either finite and stops once the specified number of samples has been acquired or generated, or it is continuous and continues to acquire or generate samples until the task is explicitly stopped. |
| samplesPerChannel | int | The number of samples to acquire or generate for each channel in the task if sampleMode is FiniteSamples. If sampleMode is ContinuousSamples, NI-DAQmx uses this value to determine the buffer size. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-configurehandshaking__samplequantitymode.html language=enus -->
## TOPIC 02780: ConfigureHandshaking(SampleQuantityMode)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-configurehandshaking__samplequantitymode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-configurehandshaking__samplequantitymode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines the sample timing and duration of the task using standard 8255/82C55 digital handshaking between the device and a peripheral device. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureHandshaking(SampleQuantityMode sampleMode)RemarksUse this method for continuous operations. T

### ConfigureHandshaking(SampleQuantityMode)

Determines the sample timing and duration of the task using standard 8255/82C55 [digital handshaking](/csh?context=nidaqmx_mxcncpts_handshaking) between the device and a peripheral device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureHandshaking(SampleQuantityMode sampleMode)

#### Remarks

Use this method for continuous operations. These [devices](/csh?context=nidaqmx_mxdevconsid_handtiming) support handshake timing.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

You cannot apply this method to a subset of devices in the task, and you must apply this method to the task as a whole. You must call this method on the instance of [Timing](nationalinstruments-daqmx-timing.html) returned from the [Timing](nationalinstruments-daqmx-task-timing.html) property on the [Task](nationalinstruments-daqmx-task.html) class. Accessing this method on instances of [Timing](nationalinstruments-daqmx-timing.html) returned from the NationalInstruments.DAQmx.Timing.Item(string) property throws an exception.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sampleMode | SampleQuantityMode | The duration of the task. A task is either finite and stops once the specified number of samples has been acquired or generated, or it is continuous and continues to acquire or generate samples until the task is explicitly stopped. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-configurehandshakingburstexportclock__string-double-digitallevelpausetriggercondition-readyfortransfereventlevelactivelevel-sampleclockpulsepolarity-sam...d2464e2158.html language=enus -->
## TOPIC 02781: ConfigureHandshakingBurstExportClock(string, double, DigitalLevelPauseTriggerCondition, ReadyForTransferEventLevelActiveLevel, SampleClockPulsePolarity, SampleQuantityMode, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-configurehandshakingburstexportclock__string-double-digitallevelpausetriggercondition-readyfortransfereventlevelactivelevel-sampleclockpulsepolarity-sam...d2464e2158.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-configurehandshakingburstexportclock__string-double-digitallevelpausetriggercondition-readyfortransfereventlevelactivelevel-sampleclockpulsepolarity-sam...d2464e2158.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines when the DAQ device transfers data to a peripheral device, using the onboard sample clock of the DAQ device to control burst handshake timing and exporting that clock for use by the peripheral device. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureHandshakingBurstExportClo

### ConfigureHandshakingBurstExportClock(string, double, DigitalLevelPauseTriggerCondition, ReadyForTransferEventLevelActiveLevel, SampleClockPulsePolarity, SampleQuantityMode, int)

Determines when the DAQ device transfers data to a peripheral device, using the onboard sample clock of the DAQ device to control [burst handshake timing](/csh?context=nidaqmx_mxcncpts_smpletimingtype) and exporting that clock for use by the peripheral device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureHandshakingBurstExportClock(string sampleClockOutputTerminal, double rate, DigitalLevelPauseTriggerCondition pauseCondition, ReadyForTransferEventLevelActiveLevel level, SampleClockPulsePolarity pulsePolarity, SampleQuantityMode sampleMode, int samplesPerChannel)

#### Remarks

These [devices](/csh?context=nidaqmx_mxdevconsid_bursthandtiming) support burst handshake timing for digital I/O.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureHandshakingBurstExportClock(string, double, DigitalLevelPauseTriggerCondition, ReadyForTransferEventLevelActiveLevel, SampleClockPulsePolarity, SampleQuantityMode, int) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

You cannot apply ConfigureHandshakingBurstExportClock(string, double, DigitalLevelPauseTriggerCondition, ReadyForTransferEventLevelActiveLevel, SampleClockPulsePolarity, SampleQuantityMode, int) to a subset of devices in the task, and you must apply ConfigureHandshakingBurstExportClock(string, double, DigitalLevelPauseTriggerCondition, ReadyForTransferEventLevelActiveLevel, SampleClockPulsePolarity, SampleQuantityMode, int) to the task as a whole. You must call ConfigureHandshakingBurstExportClock(string, double, DigitalLevelPauseTriggerCondition, ReadyForTransferEventLevelActiveLevel, SampleClockPulsePolarity, SampleQuantityMode, int) on the instance of [Timing](nationalinstruments-daqmx-timing.html) returned from the [Timing](nationalinstruments-daqmx-task-timing.html) property on the [Task](nationalinstruments-daqmx-task.html) class. Accessing this method on instances of [Timing](nationalinstruments-daqmx-timing.html) returned from the NationalInstruments.DAQmx.Timing.Item(string) property throws an exception.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sampleClockOutputTerminal | string | The terminal to which to export the sample clock. |
| rate | double | The rate of the sample clock, in hertz. |
| pauseCondition | DigitalLevelPauseTriggerCondition | Specifies whether the task pauses while the trigger signal is high or low. |
| level | ReadyForTransferEventLevelActiveLevel | The active level for the data transfer event. |
| pulsePolarity | SampleClockPulsePolarity | The polarity of the exported sample clock. |
| sampleMode | SampleQuantityMode | The duration of the task. A task is either finite and stops once the specified number of samples has been acquired or generated, or it is continuous and continues to acquire or generate samples until the task is explicitly stopped. |
| samplesPerChannel | int | The number of samples to acquire or generate for each channel in the task if sampleMode is FiniteSamples. If sampleMode is ContinuousSamples, NI-DAQmx uses this value to determine the buffer size. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-configurehandshakingburstimportclock__string-double-sampleclockactiveedge-digitallevelpausetriggercondition-readyfortransfereventlevelactivelevel-sample...d2464e2313.html language=enus -->
## TOPIC 02782: ConfigureHandshakingBurstImportClock(string, double, SampleClockActiveEdge, DigitalLevelPauseTriggerCondition, ReadyForTransferEventLevelActiveLevel, SampleQuantityMode, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-configurehandshakingburstimportclock__string-double-sampleclockactiveedge-digitallevelpausetriggercondition-readyfortransfereventlevelactivelevel-sample...d2464e2313.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-configurehandshakingburstimportclock__string-double-sampleclockactiveedge-digitallevelpausetriggercondition-readyfortransfereventlevelactivelevel-sample...d2464e2313.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines when the DAQ device transfers data to a peripheral device, using an imported sample clock to control burst handshake timing. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureHandshakingBurstImportClock(string signalSource, double rate, SampleClockActiveEdge activeEdge, Digit

### ConfigureHandshakingBurstImportClock(string, double, SampleClockActiveEdge, DigitalLevelPauseTriggerCondition, ReadyForTransferEventLevelActiveLevel, SampleQuantityMode, int)

Determines when the DAQ device transfers data to a peripheral device, using an imported sample clock to control [burst handshake timing](/csh?context=nidaqmx_mxcncpts_smpletimingtype).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureHandshakingBurstImportClock(string signalSource, double rate, SampleClockActiveEdge activeEdge, DigitalLevelPauseTriggerCondition pauseCondition, ReadyForTransferEventLevelActiveLevel level, SampleQuantityMode sampleMode, int samplesPerChannel)

#### Remarks

These [devices](/csh?context=nidaqmx_mxdevconsid_bursthandtiming) support burst handshake timing for digital I/O.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureHandshakingBurstImportClock(string, double, SampleClockActiveEdge, DigitalLevelPauseTriggerCondition, ReadyForTransferEventLevelActiveLevel, SampleQuantityMode, int) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

You cannot apply ConfigureHandshakingBurstImportClock(string, double, SampleClockActiveEdge, DigitalLevelPauseTriggerCondition, ReadyForTransferEventLevelActiveLevel, SampleQuantityMode, int) to a subset of devices in the task, and you must apply ConfigureHandshakingBurstImportClock(string, double, SampleClockActiveEdge, DigitalLevelPauseTriggerCondition, ReadyForTransferEventLevelActiveLevel, SampleQuantityMode, int) to the task as a whole. You must call ConfigureHandshakingBurstImportClock(string, double, SampleClockActiveEdge, DigitalLevelPauseTriggerCondition, ReadyForTransferEventLevelActiveLevel, SampleQuantityMode, int) on the instance of [Timing](nationalinstruments-daqmx-timing.html) returned from the [Timing](nationalinstruments-daqmx-task-timing.html) property on the [Task](nationalinstruments-daqmx-task.html) class. Accessing this method on instances of [Timing](nationalinstruments-daqmx-timing.html) returned from the NationalInstruments.DAQmx.Timing.Item(string) property throws an exception.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalSource | string | The source terminal of the sample clock. To use the internal clock of the device, set this value to Empty. |
| rate | double | The rate of the sample clock, in hertz. |
| activeEdge | SampleClockActiveEdge | The edges of the sample clock pulses on which to acquire or generate samples. |
| pauseCondition | DigitalLevelPauseTriggerCondition | Specifies whether the task pauses while the trigger signal is high or low. |
| level | ReadyForTransferEventLevelActiveLevel | The active level for the data transfer event. |
| sampleMode | SampleQuantityMode | The duration of the task. A task is either finite and stops once the specified number of samples has been acquired or generated, or it is continuous and continues to acquire or generate samples until the task is explicitly stopped. |
| samplesPerChannel | int | The number of samples to acquire or generate for each channel in the task if sampleMode is FiniteSamples. If sampleMode is ContinuousSamples, NI-DAQmx uses this value to determine the buffer size. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-configureimplicit__samplequantitymode-int.html language=enus -->
## TOPIC 02783: ConfigureImplicit(SampleQuantityMode, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-configureimplicit__samplequantitymode-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-configureimplicit__samplequantitymode-int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets only the duration of the task and the number of samples to acquire or generate without specifying timing. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureImplicit(SampleQuantityMode sampleMode, int samplesPerChannel)RemarksTypically, you use implicit timing when sample timing is

### ConfigureImplicit(SampleQuantityMode, int)

Sets only the duration of the task and the number of samples to acquire or generate without specifying timing.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureImplicit(SampleQuantityMode sampleMode, int samplesPerChannel)

#### Remarks

Typically, you use [implicit timing](/csh?context=nidaqmx_mxcncpts_smpletimingtype) when sample timing is not required for the task, such as for a task that uses counters for buffered frequency measurement, buffered period measurement, or pulse train generation. Use this method if the task requires a finite number of samples.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

You cannot apply this method to a subset of devices in the task, and you must apply this method to the task as a whole. You must call this method on the instance of [Timing](nationalinstruments-daqmx-timing.html) returned from the [Timing](nationalinstruments-daqmx-task-timing.html) property on the [Task](nationalinstruments-daqmx-task.html) class. Accessing this method on instances of [Timing](nationalinstruments-daqmx-timing.html) returned from the NationalInstruments.DAQmx.Timing.Item(string) property throws an exception.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sampleMode | SampleQuantityMode | The duration of the task. A task is either finite and stops once the specified number of samples have been acquired or generated, or it is continuous and continues to acquire or generate samples until the task is explicitly stopped. |
| samplesPerChannel | int | The number of samples to acquire or generate for each channel in the task if sampleMode is FiniteSamples. For finite counter output tasks, samplesPerChannel is the number of pulses to generate. If sample mode is ContinuousSamples, NI-DAQmx uses this value to determine the buffer size. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-configureimplicit__samplequantitymode.html language=enus -->
## TOPIC 02784: ConfigureImplicit(SampleQuantityMode)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-configureimplicit__samplequantitymode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-configureimplicit__samplequantitymode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets only the duration of the task without specifying timing. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureImplicit(SampleQuantityMode sampleMode)RemarksTypically, you use implicit timing when sample timing is not required for the task, such as for a task that uses counters for buf

### ConfigureImplicit(SampleQuantityMode)

Sets only the duration of the task without specifying timing.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureImplicit(SampleQuantityMode sampleMode)

#### Remarks

Typically, you use [implicit timing](/csh?context=nidaqmx_mxcncpts_smpletimingtype) when sample timing is not required for the task, such as for a task that uses counters for buffered frequency measurement, buffered period measurement, or pulse train generation. Use this method for continuous operations.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

You cannot apply this method to a subset of devices in the task, and you must apply this method to the task as a whole. You must call this method on the instance of [Timing](nationalinstruments-daqmx-timing.html) returned from the [Timing](nationalinstruments-daqmx-task-timing.html) property on the [Task](nationalinstruments-daqmx-task.html) class. Accessing this method on instances of [Timing](nationalinstruments-daqmx-timing.html) returned from the NationalInstruments.DAQmx.Timing.Item(string) property throws an exception.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sampleMode | SampleQuantityMode | The duration of the task. A task is either finite and stops once the specified number of samples have been acquired or generated, or it is continuous and continues to acquire or generate samples until the task is explicitly stopped. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-configurepipelinedsampleclock__string-double-sampleclockactiveedge-samplequantitymode-int.html language=enus -->
## TOPIC 02785: ConfigurePipelinedSampleClock(string, double, SampleClockActiveEdge, SampleQuantityMode, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-configurepipelinedsampleclock__string-double-sampleclockactiveedge-samplequantitymode-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-configurepipelinedsampleclock__string-double-sampleclockactiveedge-samplequantitymode-int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the source of the sample clock, the rate of the sample clock, the number of samples to acquire or generate, and configures the sample clock for pipelining. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigurePipelinedSampleClock(string signalSource, double rate, SampleClockActiveEdge

### ConfigurePipelinedSampleClock(string, double, SampleClockActiveEdge, SampleQuantityMode, int)

Sets the source of the [sample clock](/csh?context=nidaqmx_mxcncpts_sampclock), the rate of the sample clock, the number of samples to acquire or generate, and configures the sample clock for pipelining.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigurePipelinedSampleClock(string signalSource, double rate, SampleClockActiveEdge activeEdge, SampleQuantityMode sampleMode, int samplesPerChannel)

#### Remarks

The device acquires or generates samples on each sample clock edge, but does not respond to certain triggers until a few sample clock edges later. Pipelining allows higher data transfer rates at the cost of increased trigger response latency. Refer to the device documentation for information about which triggers pipelining affects. This timing type allows handshaking using the Pause trigger, the Ready for Transfer event, or the Data Active event. Refer to the device documentation for more information.

This timing type is supported only by the NI 6536 and NI 6537.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

You cannot apply this method to a subset of devices in the task, and you must apply this method to the task as a whole. You must call this method on the instance of [Timing](nationalinstruments-daqmx-timing.html) returned from the [Timing](nationalinstruments-daqmx-task-timing.html) property on the [Task](nationalinstruments-daqmx-task.html) class. Accessing this method on instances of [Timing](nationalinstruments-daqmx-timing.html) returned from the NationalInstruments.DAQmx.Timing.Item(string) property throws an exception.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalSource | string | The source terminal of the clock. To use the internal clock of the device, set this value to Empty. |
| rate | double | The sampling rate in samples per second. If you use an external source for the sample clock, set this input to the maximum expected rate of that clock. |
| activeEdge | SampleClockActiveEdge | The edges of sample clock pulses on which to acquire or generate samples. |
| sampleMode | SampleQuantityMode | The duration of the task. A task is either finite and stops once the specified number of samples have been acquired or generated, or it is continuous and continues to acquire or generate samples until the task is explicitly stopped. |
| samplesPerChannel | int | The number of samples to acquire or generate if sampleMode is FiniteSamples. If sample mode is ContinuousSamples, NI-DAQmx uses this value to determine the buffer size. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-configuresampleclock__string-double-sampleclockactiveedge-samplequantitymode-int.html language=enus -->
## TOPIC 02786: ConfigureSampleClock(string, double, SampleClockActiveEdge, SampleQuantityMode, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-configuresampleclock__string-double-sampleclockactiveedge-samplequantitymode-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-configuresampleclock__string-double-sampleclockactiveedge-samplequantitymode-int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the source of the sample clock, the rate of the sample clock, and the number of samples to acquire or generate. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureSampleClock(string signalSource, double rate, SampleClockActiveEdge activeEdge, SampleQuantityMode sampleMode, int sampl

### ConfigureSampleClock(string, double, SampleClockActiveEdge, SampleQuantityMode, int)

Sets the source of the [sample clock](/csh?context=nidaqmx_mxcncpts_sampclock), the rate of the sample clock, and the number of samples to acquire or generate.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureSampleClock(string signalSource, double rate, SampleClockActiveEdge activeEdge, SampleQuantityMode sampleMode, int samplesPerChannel)

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. this method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

You cannot apply this method to a subset of devices in the task, and you must apply this method to the task as a whole. You must call this method on the instance of [Timing](nationalinstruments-daqmx-timing.html) returned from the [Timing](nationalinstruments-daqmx-task-timing.html) property on the [Task](nationalinstruments-daqmx-task.html) class. Accessing this method on instances of [Timing](nationalinstruments-daqmx-timing.html) returned from the NationalInstruments.DAQmx.Timing.Item(string) property throws an exception.

Note

Before calling this method, you must configure channels on the task using one of the channel collection properties (for example, [CreateVoltageChannel(string, string, AITerminalConfiguration, double, double, string)](nationalinstruments-daqmx-aichannelcollection-createvoltagechannel__string-string-aiterminalconfiguration-double-double-string.html) on [AIChannels](nationalinstruments-daqmx-task-aichannels.html)).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalSource | string | The source terminal of the clock. To use the internal clock of the device, set this value to Empty. |
| rate | double | The sampling rate in samples per second. If you use an external source for the sample clock, set this input to the maximum expected rate of that clock. |
| activeEdge | SampleClockActiveEdge | The edges of sample clock pulses on which to acquire or generate samples. |
| sampleMode | SampleQuantityMode | The duration of the task. A task is either finite and stops once the specified number of samples have been acquired or generated, or it is continuous and continues to acquire or generate samples until the task is explicitly stopped. |
| samplesPerChannel | int | The number of samples to acquire or generate if sampleMode is FiniteSamples. If sample mode is ContinuousSamples, NI-DAQmx uses this value to determine the buffer size. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-configuresampleclock__string-double-sampleclockactiveedge-samplequantitymode.html language=enus -->
## TOPIC 02787: ConfigureSampleClock(string, double, SampleClockActiveEdge, SampleQuantityMode)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-configuresampleclock__string-double-sampleclockactiveedge-samplequantitymode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-configuresampleclock__string-double-sampleclockactiveedge-samplequantitymode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the source of the sample clock and the rate of the sample clock. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureSampleClock(string signalSource, double rate, SampleClockActiveEdge activeEdge, SampleQuantityMode sampleMode)RemarksThe NI-DAQmx driver does not determine if the requ

### ConfigureSampleClock(string, double, SampleClockActiveEdge, SampleQuantityMode)

Sets the source of the [sample clock](/csh?context=nidaqmx_mxcncpts_sampclock) and the rate of the sample clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureSampleClock(string signalSource, double rate, SampleClockActiveEdge activeEdge, SampleQuantityMode sampleMode)

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. This method does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

You cannot apply this method to a subset of devices in the task, and you must apply this method to the task as a whole. You must call this method on the instance of [Timing](nationalinstruments-daqmx-timing.html) returned from the [Timing](nationalinstruments-daqmx-task-timing.html) property on the [Task](nationalinstruments-daqmx-task.html) class. Accessing this method on instances of [Timing](nationalinstruments-daqmx-timing.html) returned from the NationalInstruments.DAQmx.Timing.Item(string) property throws an exception.

Note

Before calling this method, you must configure channels on the task using one of the channel collection properties (for example, [CreateVoltageChannel(string, string, AITerminalConfiguration, double, double, string)](nationalinstruments-daqmx-aichannelcollection-createvoltagechannel__string-string-aiterminalconfiguration-double-double-string.html) on [AIChannels](nationalinstruments-daqmx-task-aichannels.html)).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalSource | string | The source terminal of the clock. To use the internal clock of the device, set this value to Empty. |
| rate | double | The sampling rate in samples per second. If you use an external source for the sample clock, set this input to the maximum expected rate of that clock. |
| activeEdge | SampleClockActiveEdge | The edges of sample clock pulses on which to acquire or generate samples. |
| sampleMode | SampleQuantityMode | The duration of the task. A task is either finite and stops once the specified number of samples have been acquired or generated, or it is continuous and continues to acquire or generate samples until the task is explicitly stopped. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-delayfromsampleclock.html language=enus -->
## TOPIC 02788: DelayFromSampleClock

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-delayfromsampleclock.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-delayfromsampleclock.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of time to wait after receiving a Sample Clock edge before beginning to acquire the sample. This value is in the units you specify with DelayFromSampleClockUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double DelayFromSampleClock { get; set; }ExceptionsTypeDescriptionN

### DelayFromSampleClock

Specifies the amount of time to wait after receiving a Sample Clock edge before beginning to acquire the sample. This value is in the units you specify with [DelayFromSampleClockUnits](nationalinstruments-daqmx-timing-delayfromsampleclockunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DelayFromSampleClock { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-delayfromsampleclockunits.html language=enus -->
## TOPIC 02789: DelayFromSampleClockUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-delayfromsampleclockunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-delayfromsampleclockunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of DelayFromSampleClock. SyntaxNamespace: NationalInstruments.DAQmxpublic DelayFromSampleClockUnits DelayFromSampleClockUnits { get; set; }RemarksNI-DAQmx uses the AI Convert Clock timebase to produce the delay. If you set this property to Ticks and N is the value of DelayFromSam

### DelayFromSampleClockUnits

Specifies the units of [DelayFromSampleClock](nationalinstruments-daqmx-timing-delayfromsampleclock.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DelayFromSampleClockUnits](nationalinstruments-daqmx-delayfromsampleclockunits.html) DelayFromSampleClockUnits { get; set; }

#### Remarks

NI-DAQmx uses the AI Convert Clock timebase to produce the delay.

If you set this property to [Ticks](nationalinstruments-daqmx-delayfromsampleclockunits.html) and N is the value of [DelayFromSampleClock](nationalinstruments-daqmx-timing-delayfromsampleclock.html), N pulses of the AI Convert Clock Timebase occur after receiving a Sample Clock pulse before the acquisition of the sample begins.

If you set this property to [Seconds](nationalinstruments-daqmx-delayfromsampleclockunits.html), that number of seconds elapses after receiving a Sample Clock pulse before the acquisition of the sample begins.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-digitalfilterenable.html language=enus -->
## TOPIC 02790: DigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-digitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-digitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the AI Convert Clock. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterEnable

Specifies whether to apply a digital [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the AI Convert Clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-digitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 02791: DigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-digitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-digitalfilterminimumpulsewidth.html
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

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-digitalfiltertimebaserate.html language=enus -->
## TOPIC 02792: DigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-digitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-digitalfiltertimebaserate.html
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

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-digitalfiltertimebasesource.html language=enus -->
## TOPIC 02793: DigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-digitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-digitalfiltertimebasesource.html
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

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-digitalsynchronizationenable.html language=enus -->
## TOPIC 02794: DigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-digitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-digitalsynchronizationenable.html
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

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-dispose__bool.html language=enus -->
## TOPIC 02795: Dispose(bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-dispose__bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-dispose__bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases the managed and unmanaged resources used by Task or optionally releases only the unmanaged resources. SyntaxNamespace: NationalInstruments.DAQmxprotected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)RemarksRefer to Cleaning Up Unmanaged Resources for more information on implementing

### Dispose(bool)

Releases the managed and unmanaged resources used by [Task](nationalinstruments-daqmx-task.html) or optionally releases only the unmanaged resources.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)

#### Remarks

Refer to [Cleaning Up Unmanaged Resources](https://#) for more information on implementing a Dispose method and using objects that implement IDisposable.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| A_0 | bool | true to release both managed and unmanaged resources used by Task; false to release only unmanaged resources used by Task. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-firstsampleclockoffset.html language=enus -->
## TOPIC 02796: FirstSampleClockOffset

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-firstsampleclockoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-firstsampleclockoffset.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies, in seconds, the offset to apply to the FirstSampleClockTime value. This offset modifies when the first sample clock occurs and is used to account for known delays in the signal path. SyntaxNamespace: NationalInstruments.DAQmxpublic double FirstSampleClockOffset { get; set; }ExceptionsType

### FirstSampleClockOffset

Specifies, in seconds, the offset to apply to the [FirstSampleClockTime](nationalinstruments-daqmx-timing-firstsampleclocktime.html) value. This offset modifies when the first sample clock occurs and is used to account for known delays in the signal path.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FirstSampleClockOffset { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-firstsampleclocktime.html language=enus -->
## TOPIC 02797: FirstSampleClockTime

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-firstsampleclocktime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-firstsampleclocktime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the time of the first sample clock. SyntaxNamespace: NationalInstruments.DAQmxpublic PrecisionDateTime FirstSampleClockTime { get; set; }RemarksThe time of the first sample clock.The first sample clock time is represented by a PrecisionDateTime expressed as a UTC time. To set a time bas

### FirstSampleClockTime

Gets or sets the time of the first sample clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public PrecisionDateTime FirstSampleClockTime { get; set; }

#### Remarks

The time of the first sample clock.

Note

The first sample clock time is represented by a PrecisionDateTime expressed as a UTC time. To set a time based on the current system time, use PrecisionDateTime.UtcNow, adding an offset, rather than PrecisionDateTime.Now.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-firstsampleclocktimescale.html language=enus -->
## TOPIC 02798: FirstSampleClockTimescale

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-firstsampleclocktimescale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-firstsampleclocktimescale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timescale to be used for the value of FirstSampleClockTime. SyntaxNamespace: NationalInstruments.DAQmxpublic FirstSampleClockTimescale FirstSampleClockTimescale { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FirstSampleClockTimescale

Specifies the timescale to be used for the value of [FirstSampleClockTime](nationalinstruments-daqmx-timing-firstsampleclocktime.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [FirstSampleClockTimescale](nationalinstruments-daqmx-firstsampleclocktimescale.html) FirstSampleClockTimescale { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-firstsampletimestamp.html language=enus -->
## TOPIC 02799: FirstSampleTimestamp

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-firstsampletimestamp.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-firstsampletimestamp.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the timestamp of the first sample. SyntaxNamespace: NationalInstruments.DAQmxpublic PrecisionDateTime FirstSampleTimestamp { get; }RemarksThe timestamp of the first sample.The timestamp returned is expressed as a UTC time. To read this property, you must first set FirstSampleTimestampEnable to

### FirstSampleTimestamp

Gets the timestamp of the first sample.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public PrecisionDateTime FirstSampleTimestamp { get; }

#### Remarks

The timestamp of the first sample.

Note

The timestamp returned is expressed as a UTC time.

FirstSampleTimestampEnable

true

For more information on timestamps in NI-DAQmx, see [Timestamps](/csh?context=nidaqmx_mxdevconsid_timestamps).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-firstsampletimestampenable.html language=enus -->
## TOPIC 02800: FirstSampleTimestampEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-firstsampletimestampenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-firstsampletimestampenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the first sample timestamp. SyntaxNamespace: NationalInstruments.DAQmxpublic bool FirstSampleTimestampEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FirstSampleTimestampEnable

Specifies whether to enable the first sample timestamp.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool FirstSampleTimestampEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-firstsampletimestamptimescale.html language=enus -->
## TOPIC 02801: FirstSampleTimestampTimescale

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-firstsampletimestamptimescale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-firstsampletimestamptimescale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timescale to be used for the first sample timestamp. SyntaxNamespace: NationalInstruments.DAQmxpublic FirstSampleTimestampTimescale FirstSampleTimestampTimescale { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FirstSampleTimestampTimescale

Specifies the timescale to be used for the first sample timestamp.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [FirstSampleTimestampTimescale](nationalinstruments-daqmx-firstsampletimestamptimescale.html) FirstSampleTimestampTimescale { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-handshakedelayaftertransfer.html language=enus -->
## TOPIC 02802: HandshakeDelayAfterTransfer

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-handshakedelayaftertransfer.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-handshakedelayaftertransfer.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of seconds to wait after a handshake cycle before starting a new handshake cycle. SyntaxNamespace: NationalInstruments.DAQmxpublic double HandshakeDelayAfterTransfer { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error

### HandshakeDelayAfterTransfer

Specifies the number of seconds to wait after a handshake cycle before starting a new handshake cycle.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double HandshakeDelayAfterTransfer { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-handshakesampleinputdatacondition.html language=enus -->
## TOPIC 02803: HandshakeSampleInputDataCondition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-handshakesampleinputdatacondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-handshakesampleinputdatacondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the Handshake Trigger an input task latches the data from the peripheral device. SyntaxNamespace: NationalInstruments.DAQmxpublic HandshakeSampleInputDataCondition HandshakeSampleInputDataCondition { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptio

### HandshakeSampleInputDataCondition

Specifies on which edge of the Handshake Trigger an input task latches the data from the peripheral device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [HandshakeSampleInputDataCondition](nationalinstruments-daqmx-handshakesampleinputdatacondition.html) HandshakeSampleInputDataCondition { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-handshakestartcondition.html language=enus -->
## TOPIC 02804: HandshakeStartCondition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-handshakestartcondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-handshakestartcondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the point in the handshake cycle that the device is in when the task starts. SyntaxNamespace: NationalInstruments.DAQmxpublic HandshakeStartCondition HandshakeStartCondition { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### HandshakeStartCondition

Specifies the point in the handshake cycle that the device is in when the task starts.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [HandshakeStartCondition](nationalinstruments-daqmx-handshakestartcondition.html) HandshakeStartCondition { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-implicitunderflowbehavior.html language=enus -->
## TOPIC 02805: ImplicitUnderflowBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-implicitunderflowbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-implicitunderflowbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the action to take when the onboard memory of the device becomes empty. SyntaxNamespace: NationalInstruments.DAQmxpublic ImplicitUnderflowBehavior ImplicitUnderflowBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ImplicitUnderflowBehavior

Specifies the action to take when the onboard memory of the device becomes empty.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ImplicitUnderflowBehavior](nationalinstruments-daqmx-implicitunderflowbehavior.html) ImplicitUnderflowBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-mastertimebaserate.html language=enus -->
## TOPIC 02806: MasterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-mastertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-mastertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the rate of the Master Timebase. SyntaxNamespace: NationalInstruments.DAQmxpublic double MasterTimebaseRate { get; set; }RemarksThis property is useful only when the source of the Master Timebase is not the onboard 20 MHz timebase. NI-DAQmx requires the Master Timebase rate to calculate ot

### MasterTimebaseRate

Specifies the rate of the Master Timebase.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double MasterTimebaseRate { get; set; }

#### Remarks

This property is useful only when the source of the Master Timebase is not the onboard 20 MHz timebase. NI-DAQmx requires the Master Timebase rate to calculate other timing parameters.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-mastertimebasesource.html language=enus -->
## TOPIC 02807: MasterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-mastertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-mastertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the Master Timebase. On an E Series device, you can choose only between the onboard 20MHz Timebase or the RTSI7 terminal. SyntaxNamespace: NationalInstruments.DAQmxpublic string MasterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstrume

### MasterTimebaseSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the Master Timebase. On an E Series device, you can choose only between the onboard 20MHz Timebase or the RTSI7 terminal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string MasterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-ondemandaoissimultaneous.html language=enus -->
## TOPIC 02808: OnDemandAOIsSimultaneous

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-ondemandaoissimultaneous.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-ondemandaoissimultaneous.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to update all channels in the task simultaneously, rather than updating channels independently when you write a sample to that channel. SyntaxNamespace: NationalInstruments.DAQmxpublic bool OnDemandAOIsSimultaneous { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.Daq

### OnDemandAOIsSimultaneous

Specifies whether to update all channels in the task simultaneously, rather than updating channels independently when you write a sample to that channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool OnDemandAOIsSimultaneous { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-referenceclockrate.html language=enus -->
## TOPIC 02809: ReferenceClockRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-referenceclockrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-referenceclockrate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency of the Reference Clock. SyntaxNamespace: NationalInstruments.DAQmxpublic double ReferenceClockRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ReferenceClockRate

Specifies the frequency of the Reference Clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ReferenceClockRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-referenceclocksource.html language=enus -->
## TOPIC 02810: ReferenceClockSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-referenceclocksource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-referenceclocksource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the Reference Clock. SyntaxNamespace: NationalInstruments.DAQmxpublic string ReferenceClockSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ReferenceClockSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the Reference Clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string ReferenceClockSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclockactiveedge.html language=enus -->
## TOPIC 02811: SampleClockActiveEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclockactiveedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclockactiveedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of a clock pulse sampling takes place. This property is useful primarily when the signal you use as the Sample Clock is not a periodic clock. SyntaxNamespace: NationalInstruments.DAQmxpublic SampleClockActiveEdge SampleClockActiveEdge { get; set; }ExceptionsTypeDescriptionNat

### SampleClockActiveEdge

Specifies on which edge of a clock pulse sampling takes place. This property is useful primarily when the signal you use as the Sample Clock is not a periodic clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SampleClockActiveEdge](nationalinstruments-daqmx-sampleclockactiveedge.html) SampleClockActiveEdge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclockdigitalfilterenable.html language=enus -->
## TOPIC 02812: SampleClockDigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclockdigitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclockdigitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool SampleClockDigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SampleClockDigitalFilterEnable

Specifies whether to apply the pulse width [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool SampleClockDigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclockdigitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 02813: SampleClockDigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclockdigitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclockdigitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double SampleClockDigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SampleClockDigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double SampleClockDigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclockdigitalfiltertimebaserate.html language=enus -->
## TOPIC 02814: SampleClockDigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclockdigitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclockdigitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double SampleClockDigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI

### SampleClockDigitalFilterTimebaseRate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double SampleClockDigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclockdigitalfiltertimebasesource.html language=enus -->
## TOPIC 02815: SampleClockDigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclockdigitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclockdigitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string SampleClockDigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an erro

### SampleClockDigitalFilterTimebaseSource

Specifies the input [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the pulse width filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string SampleClockDigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclockdigitalsynchronizationenable.html language=enus -->
## TOPIC 02816: SampleClockDigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclockdigitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclockdigitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool SampleClockDigitalSynchronizationEnable { get; set; }RemarksThis property does not affect the minimum pulse width recognized by the

### SampleClockDigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool SampleClockDigitalSynchronizationEnable { get; set; }

#### Remarks

This property does not affect the minimum pulse width recognized by the device, but setting this property to true does limit the speed at which the device recognizes transitions to less than the frequency of the internal timebase.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclockmaximumrate.html language=enus -->
## TOPIC 02817: SampleClockMaximumRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclockmaximumrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclockmaximumrate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the maximum Sample Clock rate supported by the task, based on other timing settings. For output tasks, the maximum Sample Clock rate is the maximum rate of the DAC. For input tasks, NI-DAQmx calculates the maximum sampling rate differently for multiplexed devices than simultaneous sampling

### SampleClockMaximumRate

Indicates the maximum Sample Clock rate supported by the task, based on other timing settings. For output tasks, the maximum Sample Clock rate is the maximum rate of the DAC. For input tasks, NI-DAQmx calculates the maximum sampling rate differently for [multiplexed devices than simultaneous sampling devices](/csh?context=nidaqmx_mxcncpts_multisimulsamp).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double SampleClockMaximumRate { get; }

#### Remarks

For multiplexed devices, NI-DAQmx calculates the maximum sample clock rate based on the maximum AI Convert Clock rate unless you set [AIConvertRate](nationalinstruments-daqmx-timing-aiconvertrate.html). If you set that property, NI-DAQmx calculates the maximum sample clock rate based on that setting. Use [AIConvertMaximumRate](nationalinstruments-daqmx-timing-aiconvertmaximumrate.html) to query the maximum AI Convert Clock rate. NI-DAQmx also uses the minimum sample clock delay to calculate the maximum sample clock rate unless you set [DelayFromSampleClock](nationalinstruments-daqmx-timing-delayfromsampleclock.html).

For simultaneous sampling devices, the maximum Sample Clock rate is the maximum rate of the ADC.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclockoverrunbehavior.html language=enus -->
## TOPIC 02818: SampleClockOverrunBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclockoverrunbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclockoverrunbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the action to take if Sample Clock edges occur faster than the device can handle them. SyntaxNamespace: NationalInstruments.DAQmxpublic SampleClockOverrunBehavior SampleClockOverrunBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver retu

### SampleClockOverrunBehavior

Specifies the action to take if Sample Clock edges occur faster than the device can handle them.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SampleClockOverrunBehavior](nationalinstruments-daqmx-sampleclockoverrunbehavior.html) SampleClockOverrunBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclockrate.html language=enus -->
## TOPIC 02819: SampleClockRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclockrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclockrate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sampling rate in samples per channel per second. If you use an external source for the Sample Clock, set this input to the maximum expected rate of that clock. SyntaxNamespace: NationalInstruments.DAQmxpublic double SampleClockRate { get; set; }ExceptionsTypeDescriptionNationalInstrume

### SampleClockRate

Specifies the sampling rate in samples per channel per second. If you use an external source for the Sample Clock, set this input to the maximum expected rate of that clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double SampleClockRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclocksource.html language=enus -->
## TOPIC 02820: SampleClockSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclocksource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclocksource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the Sample Clock. SyntaxNamespace: NationalInstruments.DAQmxpublic string SampleClockSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SampleClockSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the Sample Clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string SampleClockSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclockterminal.html language=enus -->
## TOPIC 02821: SampleClockTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclockterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclockterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the internal Sample Clock terminal for the task. This property does not return the name of the Sample Clock source terminal specified with SampleClockSource. SyntaxNamespace: NationalInstruments.DAQmxpublic string SampleClockTerminal { get; }ExceptionsTypeDescriptionNationalIns

### SampleClockTerminal

Indicates the name of the internal Sample Clock terminal for the task. This property does not return the name of the Sample Clock source terminal specified with [SampleClockSource](nationalinstruments-daqmx-timing-sampleclocksource.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string SampleClockTerminal { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclocktimebaseactiveedge.html language=enus -->
## TOPIC 02822: SampleClockTimebaseActiveEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclocktimebaseactiveedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclocktimebaseactiveedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge to recognize a Sample Clock Timebase pulse. This property is useful primarily when the signal you use as the Sample Clock Timebase is not a periodic clock. SyntaxNamespace: NationalInstruments.DAQmxpublic SampleClockTimebaseActiveEdge SampleClockTimebaseActiveEdge { get; set;

### SampleClockTimebaseActiveEdge

Specifies on which edge to recognize a Sample Clock Timebase pulse. This property is useful primarily when the signal you use as the Sample Clock Timebase is not a periodic clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SampleClockTimebaseActiveEdge](nationalinstruments-daqmx-sampleclocktimebaseactiveedge.html) SampleClockTimebaseActiveEdge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclocktimebasedivisor.html language=enus -->
## TOPIC 02823: SampleClockTimebaseDivisor

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclocktimebasedivisor.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclocktimebasedivisor.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of Sample Clock Timebase pulses needed to produce a single Sample Clock pulse. SyntaxNamespace: NationalInstruments.DAQmxpublic long SampleClockTimebaseDivisor { get; set; }RemarksThe rate of the Sample Clock is equal to (frequency of Sample Clock Timebase) / (value of this prop

### SampleClockTimebaseDivisor

Specifies the number of Sample Clock Timebase pulses needed to produce a single Sample Clock pulse.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long SampleClockTimebaseDivisor { get; set; }

#### Remarks

The rate of the Sample Clock is equal to (frequency of Sample Clock Timebase) / (value of this property).

If the Sample Clock Timebase is not a periodic clock, the value of this property determines the number of Sample Clock Timebase edges that the device must receive before producing each Sample Clock pulse. Use [SampleClockTimebaseActiveEdge](nationalinstruments-daqmx-timing-sampleclocktimebaseactiveedge.html) to specify the polarity of these edges.

Setting this property has a similar effect to setting [SampleClockRate](nationalinstruments-daqmx-timing-sampleclockrate.html). Use [SampleClockRate](nationalinstruments-daqmx-timing-sampleclockrate.html) when you know the rate of the Sample Clock Timebase and you want to acquire or generate samples at the specified rate. Use this property when you have an external timebase that you want to divide down and use as the Sample Clock, but you do not know rate of the external timebase.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclocktimebasemastertimebasedivisor.html language=enus -->
## TOPIC 02824: SampleClockTimebaseMasterTimebaseDivisor

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclocktimebasemastertimebasedivisor.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclocktimebasemastertimebasedivisor.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of pulses of the Master Timebase needed to produce a single pulse of the Sample Clock Timebase. SyntaxNamespace: NationalInstruments.DAQmxpublic long SampleClockTimebaseMasterTimebaseDivisor { get; set; }RemarksThe rate of the Sample Clock Timebase is equal to (frequency of Mast

### SampleClockTimebaseMasterTimebaseDivisor

Specifies the number of pulses of the Master Timebase needed to produce a single pulse of the Sample Clock Timebase.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long SampleClockTimebaseMasterTimebaseDivisor { get; set; }

#### Remarks

The rate of the Sample Clock Timebase is equal to (frequency of Master Timebase) / (value of this property). The only valid values for this property are 1 and 200.

Setting this property has a similar effect to setting [SampleClockTimebaseRate](nationalinstruments-daqmx-timing-sampleclocktimebaserate.html). Use [SampleClockTimebaseRate](nationalinstruments-daqmx-timing-sampleclocktimebaserate.html) when you know the rate of the Master Timebase and you want to produce a Sample Clock Timebase at the specified rate. Use this property when you have an external Master Timebase that you want to divide down and use as the Sample Clock Timebase, but you do not know rate of that external Master Timebase.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclocktimebaserate.html language=enus -->
## TOPIC 02825: SampleClockTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclocktimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclocktimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the rate of the Sample Clock Timebase. Some applications require that you specify a rate when you use any signal other than the onboard Sample Clock Timebase. NI-DAQmx requires this rate to calculate other timing parameters. SyntaxNamespace: NationalInstruments.DAQmxpublic double SampleClo

### SampleClockTimebaseRate

Specifies the rate of the Sample Clock Timebase. Some applications require that you specify a rate when you use any signal other than the onboard Sample Clock Timebase. NI-DAQmx requires this rate to calculate other timing parameters.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double SampleClockTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclocktimebasesource.html language=enus -->
## TOPIC 02826: SampleClockTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclocktimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclocktimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the Sample Clock Timebase. SyntaxNamespace: NationalInstruments.DAQmxpublic string SampleClockTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SampleClockTimebaseSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the Sample Clock Timebase.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string SampleClockTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclocktimebaseterminal.html language=enus -->
## TOPIC 02827: SampleClockTimebaseTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclocktimebaseterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclocktimebaseterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the internal Sample Clock Timebase terminal for the task. This property does not return the name of the Sample Clock Timebase source terminal specified with SampleClockTimebaseSource. SyntaxNamespace: NationalInstruments.DAQmxpublic string SampleClockTimebaseTerminal { get; }Ex

### SampleClockTimebaseTerminal

Indicates the name of the internal Sample Clock Timebase terminal for the task. This property does not return the name of the Sample Clock Timebase source terminal specified with [SampleClockTimebaseSource](nationalinstruments-daqmx-timing-sampleclocktimebasesource.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string SampleClockTimebaseTerminal { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclocktimingresponsemode.html language=enus -->
## TOPIC 02828: SampleClockTimingResponseMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclocktimingresponsemode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclocktimingresponsemode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: The SampleClockTimingResponseMode property is obsolete. Please use the ConfigurePipelinedSampleClock method instead. Will error if used Specifies how the device responds to the sample clock and to triggers. This property has been deprecated in favor of the ConfigurePipelinedSampleClock(str

### SampleClockTimingResponseMode

**Obsolete: The SampleClockTimingResponseMode property is obsolete. Please use the ConfigurePipelinedSampleClock method instead. Will error if used** 
Specifies how the device responds to the sample clock and to triggers. This property has been deprecated in favor of the [ConfigurePipelinedSampleClock(string, double, SampleClockActiveEdge, SampleQuantityMode, int)](nationalinstruments-daqmx-timing-configurepipelinedsampleclock__string-double-sampleclockactiveedge-samplequantitymode-int.html) method.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SampleClockTimingResponseMode](nationalinstruments-daqmx-sampleclocktimingresponsemode.html) SampleClockTimingResponseMode { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampleclockunderflowbehavior.html language=enus -->
## TOPIC 02829: SampleClockUnderflowBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampleclockunderflowbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampleclockunderflowbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the action to take when the onboard memory of the device becomes empty. In either case, the sample clock does not stop. SyntaxNamespace: NationalInstruments.DAQmxpublic SampleClockUnderflowBehavior SampleClockUnderflowBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx

### SampleClockUnderflowBehavior

Specifies the action to take when the onboard memory of the device becomes empty. In either case, the sample clock does not stop.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SampleClockUnderflowBehavior](nationalinstruments-daqmx-sampleclockunderflowbehavior.html) SampleClockUnderflowBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-samplequantitymode.html language=enus -->
## TOPIC 02830: SampleQuantityMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-samplequantitymode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-samplequantitymode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if a task acquires or generates a finite number of samples or if it continuously acquires or generates samples. SyntaxNamespace: NationalInstruments.DAQmxpublic SampleQuantityMode SampleQuantityMode { get; set; }RemarksFor an analog input task with a Reference Trigger, you must set this pr

### SampleQuantityMode

Specifies if a task acquires or generates a finite number of samples or if it continuously acquires or generates samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SampleQuantityMode](nationalinstruments-daqmx-samplequantitymode.html) SampleQuantityMode { get; set; }

#### Remarks

For an analog input task with a [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger), you must set this property to [FiniteSamples](nationalinstruments-daqmx-samplequantitymode.html) even though the task runs continuously until the Reference Trigger occurs.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-samplesperchannel.html language=enus -->
## TOPIC 02831: SamplesPerChannel

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-samplesperchannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-samplesperchannel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of samples to acquire or generate for each channel if SampleQuantityMode is FiniteSamples. If SampleQuantityMode is ContinuousSamples, NI-DAQmx uses this value to determine the buffer size. SyntaxNamespace: NationalInstruments.DAQmxpublic long SamplesPerChannel { get; set; }Rema

### SamplesPerChannel

Specifies the number of samples to acquire or generate for each channel if [SampleQuantityMode](nationalinstruments-daqmx-timing-samplequantitymode.html) is [FiniteSamples](nationalinstruments-daqmx-samplequantitymode.html). If [SampleQuantityMode](nationalinstruments-daqmx-timing-samplequantitymode.html) is [ContinuousSamples](nationalinstruments-daqmx-samplequantitymode.html), NI-DAQmx uses this value to [determine the buffer size](/csh?context=nidaqmx_mxcncpts_buffersize).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long SamplesPerChannel { get; set; }

#### Remarks

To configure an analog output task to generate a finite number of cycles of a waveform, set this property to (desired number of cycles) * (number of samples per cycle).

This property affects the [buffer allocation](/csh?context=nidaqmx_mxcncpts_buffersize) for the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampletimingengine.html language=enus -->
## TOPIC 02832: SampleTimingEngine

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampletimingengine.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampletimingengine.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which timing engine to use for the task. SyntaxNamespace: NationalInstruments.DAQmxpublic long SampleTimingEngine { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SampleTimingEngine

Specifies which [timing engine](/csh?context=nidaqmx_mxdevconsid_multitimingengines) to use for the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long SampleTimingEngine { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-sampletimingtype.html language=enus -->
## TOPIC 02833: SampleTimingType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-sampletimingtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-sampletimingtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of sample timing to use for the task. SyntaxNamespace: NationalInstruments.DAQmxpublic SampleTimingType SampleTimingType { get; set; }RemarksSelect SampleClock when a hardware signal (usually a clock) must acquire or produce samples. To perform buffered edge counting, for example,

### SampleTimingType

Specifies the [type of sample timing](/csh?context=nidaqmx_mxcncpts_smpletimingtype) to use for the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SampleTimingType](nationalinstruments-daqmx-sampletimingtype.html) SampleTimingType { get; set; }

#### Remarks

Select [SampleClock](nationalinstruments-daqmx-sampletimingtype.html) when a hardware signal (usually a clock) must acquire or produce samples. To perform buffered edge counting, for example, select [SampleClock](nationalinstruments-daqmx-sampletimingtype.html) and use [SampleClockSource](nationalinstruments-daqmx-timing-sampleclocksource.html) to specify the source of the Sample clock.

Select [Handshake](nationalinstruments-daqmx-sampletimingtype.html) to use bidirectional hardware signals to time the exchange of digital data between two devices.

Select [BurstHandshake](nationalinstruments-daqmx-sampletimingtype.html) to run at a slower rate but with the capability for per sample evaluation of triggers and events to pause the operation.

Select [PipelinedSampleClock](nationalinstruments-daqmx-sampletimingtype.html) on supported devices to run at the maximum sample rate with a few Sample clock cycles delay before the device can respond to triggers and events.

Select [OnDemand](nationalinstruments-daqmx-sampletimingtype.html) to acquire data only when reading from the task executes or to generate data only when writing to the task executes.

Select [Implicit](nationalinstruments-daqmx-sampletimingtype.html) to perform a buffered period or frequency counter measurement or to generate a finite pulse train.

Select [ChangeDetection](nationalinstruments-daqmx-sampletimingtype.html) to capture data only when certain digital lines change states and without continuously transferring unnecessary data during periods of inactivity.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-singlepoint.html language=enus -->
## TOPIC 02834: SinglePoint

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-singlepoint.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-singlepoint.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an instance of SinglePoint. SyntaxNamespace: NationalInstruments.DAQmxpublic SinglePoint SinglePoint { get; }RemarksThe SinglePoint instance.You cannot apply SinglePoint to a subset of devices in the task and you must apply SinglePoint to the task as a whole. Call SinglePoint on the instance of

### SinglePoint

Gets an instance of [SinglePoint](nationalinstruments-daqmx-singlepoint.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SinglePoint](nationalinstruments-daqmx-singlepoint.html) SinglePoint { get; }

#### Remarks

The [SinglePoint](nationalinstruments-daqmx-singlepoint.html) instance.

You cannot apply [SinglePoint](nationalinstruments-daqmx-singlepoint.html) to a subset of devices in the task and you must apply [SinglePoint](nationalinstruments-daqmx-singlepoint.html) to the task as a whole. Call [SinglePoint](nationalinstruments-daqmx-singlepoint.html) on the instance of [Timing](nationalinstruments-daqmx-timing.html) returned from the [Timing](nationalinstruments-daqmx-task-timing.html) property on the [Task](nationalinstruments-daqmx-task.html) class. Accessing [SinglePoint](nationalinstruments-daqmx-singlepoint.html) on instances of [Timing](nationalinstruments-daqmx-timing.html) returned from the NationalInstruments.DAQmx.Timing.Item(string) property throws an exception.

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-synchronizationclockinterval.html language=enus -->
## TOPIC 02835: SynchronizationClockInterval

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-synchronizationclockinterval.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-synchronizationclockinterval.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the interval, in Sample Clock periods, between each internal Synchronization Clock pulse. NI-DAQmx uses this pulse for synchronization of triggers between multiple devices at different rates. Refer to device documentation for information about how to calculate this value. SyntaxNamespace:

### SynchronizationClockInterval

Specifies the interval, in Sample Clock periods, between each internal Synchronization Clock pulse. NI-DAQmx uses this pulse for synchronization of triggers between multiple devices at different rates. Refer to device documentation for information about how to calculate this value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long SynchronizationClockInterval { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-synchronizationpulseminimumdelaytostart.html language=enus -->
## TOPIC 02836: SynchronizationPulseMinimumDelayToStart

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-synchronizationpulseminimumdelaytostart.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-synchronizationpulseminimumdelaytostart.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the amount of time that elapses after the master device issues the synchronization pulse before the task starts. SyntaxNamespace: NationalInstruments.DAQmxpublic double SynchronizationPulseMinimumDelayToStart { get; set; }RemarksRead SynchronizationPulseTime for all slave device

### SynchronizationPulseMinimumDelayToStart

Specifies in seconds the amount of time that elapses after the master device issues the synchronization pulse before the task starts.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double SynchronizationPulseMinimumDelayToStart { get; set; }

#### Remarks

Read [SynchronizationPulseTime](nationalinstruments-daqmx-timing-synchronizationpulsetime.html) for all slave devices, and set this property for the master device to the maximum of those values.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-synchronizationpulseresetdelay.html language=enus -->
## TOPIC 02837: SynchronizationPulseResetDelay

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-synchronizationpulseresetdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-synchronizationpulseresetdelay.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the amount of time to wait after the Synchronization Pulse before resetting the ADCs or DACs on the device. When synchronizing devices, query SynchronizationPulseResetTime on all devices and note the largest reset time. Then, for each device, subtract the reset time from the lar

### SynchronizationPulseResetDelay

Specifies in seconds the amount of time to wait after the Synchronization Pulse before resetting the ADCs or DACs on the device. When synchronizing devices, query [SynchronizationPulseResetTime](nationalinstruments-daqmx-timing-synchronizationpulseresettime.html) on all devices and note the largest reset time. Then, for each device, subtract the reset time from the largest reset time and set this property to the resulting value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double SynchronizationPulseResetDelay { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-synchronizationpulseresettime.html language=enus -->
## TOPIC 02838: SynchronizationPulseResetTime

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-synchronizationpulseresettime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-synchronizationpulseresettime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in seconds the amount of time required for the ADCs or DACs on the device to reset. When synchronizing devices, query this property on all devices and note the largest reset time. Then, for each device, subtract the value of this property from the largest reset time and set Synchronization

### SynchronizationPulseResetTime

Indicates in seconds the amount of time required for the ADCs or DACs on the device to reset. When synchronizing devices, query this property on all devices and note the largest reset time. Then, for each device, subtract the value of this property from the largest reset time and set [SynchronizationPulseResetDelay](nationalinstruments-daqmx-timing-synchronizationpulseresetdelay.html) to the resulting value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double SynchronizationPulseResetTime { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-synchronizationpulsesource.html language=enus -->
## TOPIC 02839: SynchronizationPulseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-synchronizationpulsesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-synchronizationpulsesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the synchronization pulse. The synchronization pulse resets the clock dividers and the ADCs/DACs on the device. SyntaxNamespace: NationalInstruments.DAQmxpublic string SynchronizationPulseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.

### SynchronizationPulseSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the synchronization pulse. The synchronization pulse resets the clock dividers and the ADCs/DACs on the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string SynchronizationPulseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-synchronizationpulseterminal.html language=enus -->
## TOPIC 02840: SynchronizationPulseTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-synchronizationpulseterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-synchronizationpulseterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the internal Synchronization Pulse terminal for the task. This property does not return the name of the source terminal. SyntaxNamespace: NationalInstruments.DAQmxpublic string SynchronizationPulseTerminal { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionT

### SynchronizationPulseTerminal

Indicates the name of the internal Synchronization Pulse terminal for the task. This property does not return the name of the source terminal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string SynchronizationPulseTerminal { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-synchronizationpulsetime.html language=enus -->
## TOPIC 02841: SynchronizationPulseTime

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-synchronizationpulsetime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-synchronizationpulsetime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in seconds the delay required to reset the ADCs/DACs after the device receives the synchronization pulse. SyntaxNamespace: NationalInstruments.DAQmxpublic double SynchronizationPulseTime { get; }RemarksThis time is the minimum delay required by the device between the receipt of the synchro

### SynchronizationPulseTime

Indicates in seconds the delay required to reset the ADCs/DACs after the device receives the synchronization pulse.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double SynchronizationPulseTime { get; }

#### Remarks

This time is the minimum delay required by the device between the receipt of the synchronization pulse and the start of the acquisition. Read this property for all slave devices and set [SynchronizationPulseMinimumDelayToStart](nationalinstruments-daqmx-timing-synchronizationpulseminimumdelaytostart.html) for the master device to the maximum of these delays.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-synchronizationpulsetimescale.html language=enus -->
## TOPIC 02842: SynchronizationPulseTimescale

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-synchronizationpulsetimescale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-synchronizationpulsetimescale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timescale to be used for timestamps for a sync pulse. SyntaxNamespace: NationalInstruments.DAQmxpublic SynchronizationPulseTimescale SynchronizationPulseTimescale { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SynchronizationPulseTimescale

Specifies the timescale to be used for timestamps for a sync pulse.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SynchronizationPulseTimescale](nationalinstruments-daqmx-synchronizationpulsetimescale.html) SynchronizationPulseTimescale { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-synchronizationpulsetriggertime.html language=enus -->
## TOPIC 02843: SynchronizationPulseTriggerTime

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-synchronizationpulsetriggertime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-synchronizationpulsetriggertime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the start time of the synchronization pulse. SyntaxNamespace: NationalInstruments.DAQmxpublic PrecisionDateTime SynchronizationPulseTriggerTime { get; set; }RemarksThe start time of the synchronization pulse.The trigger time is represented by a PrecisionDateTime expressed as a UTC time.

### SynchronizationPulseTriggerTime

Gets or sets the start time of the synchronization pulse.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public PrecisionDateTime SynchronizationPulseTriggerTime { get; set; }

#### Remarks

The start time of the synchronization pulse.

Note

The trigger time is represented by a PrecisionDateTime expressed as a UTC time. To set a trigger time based on the current system time, use PrecisionDateTime.UtcNow, adding an offset, rather than PrecisionDateTime.Now.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-synchronizationpulsetype.html language=enus -->
## TOPIC 02844: SynchronizationPulseType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-synchronizationpulsetype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-synchronizationpulsetype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of sync pulse used in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic SynchronizationPulseType SynchronizationPulseType { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SynchronizationPulseType

Specifies the type of sync pulse used in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SynchronizationPulseType](nationalinstruments-daqmx-synchronizationpulsetype.html) SynchronizationPulseType { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-this__string.html language=enus -->
## TOPIC 02845: this[string deviceNames]

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-this__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-this__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an instance of Timing that contains settings for only the specified devices. In Visual C#, this property is the indexer. SyntaxNamespace: NationalInstruments.DAQmxpublic Timing this[string deviceNames] { get; }RemarksThe specified instance of Timing.Use the NationalInstruments.DAQmx.Timing.Item

### this[string deviceNames]

Gets an instance of [Timing](nationalinstruments-daqmx-timing.html) that contains settings for only the specified devices. In Visual C#, this property is the indexer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [Timing](nationalinstruments-daqmx-timing.html) this[string deviceNames] { get; }

#### Remarks

The specified instance of [Timing](nationalinstruments-daqmx-timing.html).

Use the NationalInstruments.DAQmx.Timing.Item(string) property to retrieve an instance of [Timing](nationalinstruments-daqmx-timing.html) that applies only to certain devices in your task. NationalInstruments.DAQmx.Timing.Item(string) allows you to set timing properties differently on different devices in your task. If you want to set a property on all devices in the task, you can use the [Timing](nationalinstruments-daqmx-task-timing.html) property of the [Task](nationalinstruments-daqmx-task.html) class.

This property is only supported by certain National Instruments devices. Please refer to your product-specific documentation to determine which properties, if any, you can set on a device-specific basis.

Some members of the [Timing](nationalinstruments-daqmx-timing.html) class do not apply to a subset of devices in the task and apply only to the task as a whole. You must call these members on the instance of [Timing](nationalinstruments-daqmx-timing.html) returned from the [Timing](nationalinstruments-daqmx-task-timing.html) property of the [Task](nationalinstruments-daqmx-task.html) class. Accessing these members on instances of [Timing](nationalinstruments-daqmx-timing.html) returned from this property throws an exception. These members include the [SinglePoint](nationalinstruments-daqmx-timing-singlepoint.html) property, this property, and configuration methods, like [ConfigureSampleClock(string, double, SampleClockActiveEdge, SampleQuantityMode, int)](nationalinstruments-daqmx-timing-configuresampleclock__string-double-sampleclockactiveedge-samplequantitymode-int.html).

You can use the [Devices](nationalinstruments-daqmx-task-devices.html) property to determine what devices are in a task.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deviceNames | string | One or more device names that the retrieved Timing class operates on. Use a comma to separate multiple device names. You may pass Empty or null to specify all devices in the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### See Also

- Devices

Parent topic:

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing-tostring.html language=enus -->
## TOPIC 02846: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing-tostring.html
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

Timing Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-timing.html language=enus -->
## TOPIC 02847: Timing Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-timing.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties and methods that configure the sample timing and duration of the Task. Derives fromMarshalByRefObjectIFilteredTypeDescriptorIServiceProviderSyntaxNamespace: NationalInstruments.DAQmxpublic class Timing : MarshalByRefObject, IFilteredTypeDescriptor, IServiceProviderRemarksExample

### Timing Class

Contains properties and methods that configure the [sample timing](/csh?context=nidaqmx_mxcncpts_smpletimingtype) and duration of the [Task](nationalinstruments-daqmx-task.html).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor
- IServiceProvider

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class Timing : MarshalByRefObject, IFilteredTypeDescriptor, IServiceProvider

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AIConvertActiveEdge | Specifies on which edge of the clock pulse an analog-to-digital conversion takes place. |
| AIConvertMaximumRate | Indicates the maximum convert rate supported by the task, given the current devices and channel count. |
| AIConvertRate | Specifies in Hertz the rate at which to clock the analog-to-digital converter. This clock is specific to the analog input section of multiplexed devices. |
| AIConvertSource | Specifies the terminal of the signal to use as the AI Convert Clock. |
| AIConvertTimebaseDivisor | Specifies the number of AI Convert Clock Timebase pulses needed to produce a single AI Convert Clock pulse. |
| AIConvertTimebaseSource | Specifies the terminal of the signal to use as the AI Convert Clock Timebase. |
| ChangeDetectionDIFallingEdgePhysicalChannels | Specifies the names of the digital lines or ports on which to detect falling edges. The lines or ports must be used by virtual channels in the task. You also can specify a string that contains a list or range of digital lines or ports. |
| ChangeDetectionDIRisingEdgePhysicalChannels | Specifies the names of the digital lines or ports on which to detect rising edges. The lines or ports must be used by virtual channels in the task. You also can specify a string that contains a list or range of digital lines or ports. |
| ChangeDetectionDITristate | Specifies whether to tristate lines specified with ChangeDetectionDIRisingEdgePhysicalChannels and ChangeDetectionDIFallingEdgePhysicalChannels that are not in a virtual channel in the task. If you set this property to true, NI-DAQmx tristates rising/falling edge lines that are not in a virtual channel in the task. If you set this property to false, NI-DAQmx does not modify the configuration of rising/falling edge lines that are not in a virtual channel in the task, even if the lines were previously tristated. Set this property to false to detect changes on lines in other tasks or to detect changes on output-only lines. |
| ChangeDetectionOverflowed | Indicates if samples were missed because change detection events occurred faster than the device could handle them. Some devices detect overflows differently than others. |
| DelayFromSampleClock | Specifies the amount of time to wait after receiving a Sample Clock edge before beginning to acquire the sample. This value is in the units you specify with DelayFromSampleClockUnits. |
| DelayFromSampleClockUnits | Specifies the units of DelayFromSampleClock. |
| DigitalFilterEnable | Specifies whether to apply a digital filter to the AI Convert Clock. |
| DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
| DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
| DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
| DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
| FirstSampleClockOffset | Specifies, in seconds, the offset to apply to the FirstSampleClockTime value. This offset modifies when the first sample clock occurs and is used to account for known delays in the signal path. |
| FirstSampleClockTime | Gets or sets the time of the first sample clock. |
| FirstSampleClockTimescale | Specifies the timescale to be used for the value of FirstSampleClockTime. |
| FirstSampleTimestamp | Gets the timestamp of the first sample. |
| FirstSampleTimestampEnable | Specifies whether to enable the first sample timestamp. |
| FirstSampleTimestampTimescale | Specifies the timescale to be used for the first sample timestamp. |
| HandshakeDelayAfterTransfer | Specifies the number of seconds to wait after a handshake cycle before starting a new handshake cycle. |
| HandshakeSampleInputDataCondition | Specifies on which edge of the Handshake Trigger an input task latches the data from the peripheral device. |
| HandshakeStartCondition | Specifies the point in the handshake cycle that the device is in when the task starts. |
| ImplicitUnderflowBehavior | Specifies the action to take when the onboard memory of the device becomes empty. |
| MasterTimebaseRate | Specifies the rate of the Master Timebase. |
| MasterTimebaseSource | Specifies the terminal of the signal to use as the Master Timebase. On an E Series device, you can choose only between the onboard 20MHz Timebase or the RTSI7 terminal. |
| OnDemandAOIsSimultaneous | Specifies whether to update all channels in the task simultaneously, rather than updating channels independently when you write a sample to that channel. |
| ReferenceClockRate | Specifies the frequency of the Reference Clock. |
| ReferenceClockSource | Specifies the terminal of the signal to use as the Reference Clock. |
| SampleClockActiveEdge | Specifies on which edge of a clock pulse sampling takes place. This property is useful primarily when the signal you use as the Sample Clock is not a periodic clock. |
| SampleClockDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
| SampleClockDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
| SampleClockDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
| SampleClockDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
| SampleClockDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
| SampleClockMaximumRate | Indicates the maximum Sample Clock rate supported by the task, based on other timing settings. For output tasks, the maximum Sample Clock rate is the maximum rate of the DAC. For input tasks, NI-DAQmx calculates the maximum sampling rate differently for multiplexed devices than simultaneous sampling devices. |
| SampleClockOverrunBehavior | Specifies the action to take if Sample Clock edges occur faster than the device can handle them. |
| SampleClockRate | Specifies the sampling rate in samples per channel per second. If you use an external source for the Sample Clock, set this input to the maximum expected rate of that clock. |
| SampleClockSource | Specifies the terminal of the signal to use as the Sample Clock. |
| SampleClockTerminal | Indicates the name of the internal Sample Clock terminal for the task. This property does not return the name of the Sample Clock source terminal specified with SampleClockSource. |
| SampleClockTimebaseActiveEdge | Specifies on which edge to recognize a Sample Clock Timebase pulse. This property is useful primarily when the signal you use as the Sample Clock Timebase is not a periodic clock. |
| SampleClockTimebaseDivisor | Specifies the number of Sample Clock Timebase pulses needed to produce a single Sample Clock pulse. |
| SampleClockTimebaseMasterTimebaseDivisor | Specifies the number of pulses of the Master Timebase needed to produce a single pulse of the Sample Clock Timebase. |
| SampleClockTimebaseRate | Specifies the rate of the Sample Clock Timebase. Some applications require that you specify a rate when you use any signal other than the onboard Sample Clock Timebase. NI-DAQmx requires this rate to calculate other timing parameters. |
| SampleClockTimebaseSource | Specifies the terminal of the signal to use as the Sample Clock Timebase. |
| SampleClockTimebaseTerminal | Indicates the name of the internal Sample Clock Timebase terminal for the task. This property does not return the name of the Sample Clock Timebase source terminal specified with SampleClockTimebaseSource. |
| SampleClockTimingResponseMode | Obsolete: The SampleClockTimingResponseMode property is obsolete. Please use the ConfigurePipelinedSampleClock method instead. Will error if usedSpecifies how the device responds to the sample clock and to triggers. This property has been deprecated in favor of the ConfigurePipelinedSampleClock(string, double, SampleClockActiveEdge, SampleQuantityMode, int) method. |
| SampleClockUnderflowBehavior | Specifies the action to take when the onboard memory of the device becomes empty. In either case, the sample clock does not stop. |
| SampleQuantityMode | Specifies if a task acquires or generates a finite number of samples or if it continuously acquires or generates samples. |
| SamplesPerChannel | Specifies the number of samples to acquire or generate for each channel if SampleQuantityMode is FiniteSamples. If SampleQuantityMode is ContinuousSamples, NI-DAQmx uses this value to determine the buffer size. |
| SampleTimingEngine | Specifies which timing engine to use for the task. |
| SampleTimingType | Specifies the type of sample timing to use for the task. |
| SinglePoint | Gets an instance of SinglePoint. |
| SynchronizationClockInterval | Specifies the interval, in Sample Clock periods, between each internal Synchronization Clock pulse. NI-DAQmx uses this pulse for synchronization of triggers between multiple devices at different rates. Refer to device documentation for information about how to calculate this value. |
| SynchronizationPulseMinimumDelayToStart | Specifies in seconds the amount of time that elapses after the master device issues the synchronization pulse before the task starts. |
| SynchronizationPulseResetDelay | Specifies in seconds the amount of time to wait after the Synchronization Pulse before resetting the ADCs or DACs on the device. When synchronizing devices, query SynchronizationPulseResetTime on all devices and note the largest reset time. Then, for each device, subtract the reset time from the largest reset time and set this property to the resulting value. |
| SynchronizationPulseResetTime | Indicates in seconds the amount of time required for the ADCs or DACs on the device to reset. When synchronizing devices, query this property on all devices and note the largest reset time. Then, for each device, subtract the value of this property from the largest reset time and set SynchronizationPulseResetDelay to the resulting value. |
| SynchronizationPulseSource | Specifies the terminal of the signal to use as the synchronization pulse. The synchronization pulse resets the clock dividers and the ADCs/DACs on the device. |
| SynchronizationPulseTerminal | Indicates the name of the internal Synchronization Pulse terminal for the task. This property does not return the name of the source terminal. |
| SynchronizationPulseTime | Indicates in seconds the delay required to reset the ADCs/DACs after the device receives the synchronization pulse. |
| SynchronizationPulseTimescale | Specifies the timescale to be used for timestamps for a sync pulse. |
| SynchronizationPulseTriggerTime | Gets or sets the start time of the synchronization pulse. |
| SynchronizationPulseType | Specifies the type of sync pulse used in the task. |
| this[string deviceNames] | Gets an instance of Timing that contains settings for only the specified devices. In Visual C#, this property is the indexer. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureChangeDetection(string, string, SampleQuantityMode, int) | Configures the task to acquire samples on the rising and/or falling edges of the specified lines or ports and sets the number of samples to acquire. |
| ConfigureChangeDetection(string, string, SampleQuantityMode) | Configures the task to acquire samples on the rising and/or falling edges of the specified lines or ports. |
| ConfigureHandshaking(SampleQuantityMode, int) | Determines the sample timing and duration of the task with the specified number of samples, using standard 8255/82C55 digital handshaking between the device and a peripheral device. |
| ConfigureHandshaking(SampleQuantityMode) | Determines the sample timing and duration of the task using standard 8255/82C55 digital handshaking between the device and a peripheral device. |
| ConfigureHandshakingBurstExportClock(string, double, DigitalLevelPauseTriggerCondition, ReadyForTransferEventLevelActiveLevel, SampleClockPulsePolarity, SampleQuantityMode, int) | Determines when the DAQ device transfers data to a peripheral device, using the onboard sample clock of the DAQ device to control burst handshake timing and exporting that clock for use by the peripheral device. |
| ConfigureHandshakingBurstImportClock(string, double, SampleClockActiveEdge, DigitalLevelPauseTriggerCondition, ReadyForTransferEventLevelActiveLevel, SampleQuantityMode, int) | Determines when the DAQ device transfers data to a peripheral device, using an imported sample clock to control burst handshake timing. |
| ConfigureImplicit(SampleQuantityMode, int) | Sets only the duration of the task and the number of samples to acquire or generate without specifying timing. |
| ConfigureImplicit(SampleQuantityMode) | Sets only the duration of the task without specifying timing. |
| ConfigurePipelinedSampleClock(string, double, SampleClockActiveEdge, SampleQuantityMode, int) | Sets the source of the sample clock, the rate of the sample clock, the number of samples to acquire or generate, and configures the sample clock for pipelining. |
| ConfigureSampleClock(string, double, SampleClockActiveEdge, SampleQuantityMode, int) | Sets the source of the sample clock, the rate of the sample clock, and the number of samples to acquire or generate. |
| ConfigureSampleClock(string, double, SampleClockActiveEdge, SampleQuantityMode) | Sets the source of the sample clock and the rate of the sample clock. |
| ToString() | Returns a string representation of the object. |
| Dispose(bool) | Releases the managed and unmanaged resources used by Task or optionally releases only the unmanaged resources. |

#### See Also

- Task
- Timing

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-triggers-advancetrigger.html language=enus -->
## TOPIC 02848: AdvanceTrigger

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-triggers-advancetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-triggers-advancetrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the AdvanceTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic AdvanceTrigger AdvanceTrigger { get; }RemarksThe AdvanceTrigger.

### AdvanceTrigger

Gets the [AdvanceTrigger](nationalinstruments-daqmx-advancetrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AdvanceTrigger](nationalinstruments-daqmx-advancetrigger.html) AdvanceTrigger { get; }

#### Remarks

The [AdvanceTrigger](nationalinstruments-daqmx-advancetrigger.html).

Parent topic:

Triggers Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-triggers-armstarttrigger.html language=enus -->
## TOPIC 02849: ArmStartTrigger

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-triggers-armstarttrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-triggers-armstarttrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ArmStartTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic ArmStartTrigger ArmStartTrigger { get; }RemarksThe ArmStartTrigger.

### ArmStartTrigger

Gets the [ArmStartTrigger](nationalinstruments-daqmx-armstarttrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ArmStartTrigger](nationalinstruments-daqmx-armstarttrigger.html) ArmStartTrigger { get; }

#### Remarks

The [ArmStartTrigger](nationalinstruments-daqmx-armstarttrigger.html).

Parent topic:

Triggers Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-triggers-handshaketrigger.html language=enus -->
## TOPIC 02850: HandshakeTrigger

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-triggers-handshaketrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-triggers-handshaketrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the HandshakeTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic HandshakeTrigger HandshakeTrigger { get; }RemarksThe HandshakeTrigger.

### HandshakeTrigger

Gets the [HandshakeTrigger](nationalinstruments-daqmx-handshaketrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [HandshakeTrigger](nationalinstruments-daqmx-handshaketrigger.html) HandshakeTrigger { get; }

#### Remarks

The [HandshakeTrigger](nationalinstruments-daqmx-handshaketrigger.html).

Parent topic:

Triggers Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-triggers-pausetrigger.html language=enus -->
## TOPIC 02851: PauseTrigger

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-triggers-pausetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-triggers-pausetrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the PauseTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic PauseTrigger PauseTrigger { get; }RemarksThe PauseTrigger.

### PauseTrigger

Gets the [PauseTrigger](nationalinstruments-daqmx-pausetrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [PauseTrigger](nationalinstruments-daqmx-pausetrigger.html) PauseTrigger { get; }

#### Remarks

The [PauseTrigger](nationalinstruments-daqmx-pausetrigger.html).

Parent topic:

Triggers Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-triggers-referencetrigger.html language=enus -->
## TOPIC 02852: ReferenceTrigger

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-triggers-referencetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-triggers-referencetrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ReferenceTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic ReferenceTrigger ReferenceTrigger { get; }RemarksThe ReferenceTrigger.

### ReferenceTrigger

Gets the [ReferenceTrigger](nationalinstruments-daqmx-referencetrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ReferenceTrigger](nationalinstruments-daqmx-referencetrigger.html) ReferenceTrigger { get; }

#### Remarks

The [ReferenceTrigger](nationalinstruments-daqmx-referencetrigger.html).

Parent topic:

Triggers Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-triggers-starttrigger.html language=enus -->
## TOPIC 02853: StartTrigger

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-triggers-starttrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-triggers-starttrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the StartTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic StartTrigger StartTrigger { get; }RemarksThe StartTrigger.

### StartTrigger

Gets the [StartTrigger](nationalinstruments-daqmx-starttrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [StartTrigger](nationalinstruments-daqmx-starttrigger.html) StartTrigger { get; }

#### Remarks

The [StartTrigger](nationalinstruments-daqmx-starttrigger.html).

Parent topic:

Triggers Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-triggers-synchronizationtype.html language=enus -->
## TOPIC 02854: SynchronizationType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-triggers-synchronizationtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-triggers-synchronizationtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the role of the device in a synchronized system. Setting this value to Master or Slave enables trigger skew correction. If you enable trigger skew correction, set this property to Master on only one device, and set this property to Slave on the other devices. SyntaxNamespace: NationalInstr

### SynchronizationType

Specifies the role of the device in a synchronized system. Setting this value to [Master](nationalinstruments-daqmx-triggersynchronizationtype.html) or [Slave](nationalinstruments-daqmx-triggersynchronizationtype.html) enables [trigger skew correction](/csh?context=nidaqmx_mxcncpts_synctriggerskewcorrect). If you enable trigger skew correction, set this property to [Master](nationalinstruments-daqmx-triggersynchronizationtype.html) on only one device, and set this property to [Slave](nationalinstruments-daqmx-triggersynchronizationtype.html) on the other devices.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [TriggerSynchronizationType](nationalinstruments-daqmx-triggersynchronizationtype.html) SynchronizationType { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Triggers Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-triggers-tostring.html language=enus -->
## TOPIC 02855: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-triggers-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-triggers-tostring.html
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

Triggers Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-triggers-watchdogexpirationtrigger.html language=enus -->
## TOPIC 02856: WatchdogExpirationTrigger

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-triggers-watchdogexpirationtrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-triggers-watchdogexpirationtrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the WatchdogExpirationTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic WatchdogExpirationTrigger WatchdogExpirationTrigger { get; }RemarksThe WatchdogExpirationTrigger.

### WatchdogExpirationTrigger

Gets the [WatchdogExpirationTrigger](nationalinstruments-daqmx-watchdogexpirationtrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [WatchdogExpirationTrigger](nationalinstruments-daqmx-watchdogexpirationtrigger.html) WatchdogExpirationTrigger { get; }

#### Remarks

The [WatchdogExpirationTrigger](nationalinstruments-daqmx-watchdogexpirationtrigger.html).

Parent topic:

Triggers Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-triggers.html language=enus -->
## TOPIC 02857: Triggers Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-triggers.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains members that configure all of the triggers that can affect a Task. Derives fromMarshalByRefObjectSyntaxNamespace: NationalInstruments.DAQmxpublic class Triggers : MarshalByRefObjectThread SafetyAll members of this type are safe for multithreaded operations.PropertiesNameDescriptionAdvanceTr

### Triggers Class

Contains members that configure all of the [triggers](/csh?context=nidaqmx_mxcncpts_triggering) that can affect a [Task](nationalinstruments-daqmx-task.html).

#### Derives from

- MarshalByRefObject

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class Triggers : MarshalByRefObject

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AdvanceTrigger | Gets the AdvanceTrigger. |
| ArmStartTrigger | Gets the ArmStartTrigger. |
| HandshakeTrigger | Gets the HandshakeTrigger. |
| PauseTrigger | Gets the PauseTrigger. |
| ReferenceTrigger | Gets the ReferenceTrigger. |
| StartTrigger | Gets the StartTrigger. |
| SynchronizationType | Specifies the role of the device in a synchronized system. Setting this value to Master or Slave enables trigger skew correction. If you enable trigger skew correction, set this property to Master on only one device, and set this property to Slave on the other devices. |
| WatchdogExpirationTrigger | Gets the WatchdogExpirationTrigger. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- Task
- Triggers

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-triggersynchronizationtype.html language=enus -->
## TOPIC 02858: TriggerSynchronizationType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-triggersynchronizationtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-triggersynchronizationtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the role of the device in a synchronized system. Setting this value to Master or Slave enables trigger skew correction. If you enable trigger skew correction, set this property to Master on only one device, and set this property to Slave on the other devices. SyntaxNamespace: NationalInstr

### TriggerSynchronizationType Enumeration

Specifies the role of the device in a synchronized system. Setting this value to Master or Slave enables [trigger skew correction](/csh?context=nidaqmx_mxcncpts_synctriggerskewcorrect). If you enable trigger skew correction, set this property to Master on only one device, and set this property to Slave on the other devices.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum TriggerSynchronizationType

#### Remarks

Specifies the role of the device in a synchronized system. Setting this value to Master or Slave enables [trigger skew correction](/csh?context=nidaqmx_mxcncpts_synctriggerskewcorrect). If you enable trigger skew correction, set this property to Master on only one device, and set this property to Slave on the other devices. Use this enumeration to get or set the value of [SynchronizationType](nationalinstruments-daqmx-triggers-synchronizationtype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 10230 | Disables trigger skew correction. |
| Master | 15888 | Device is the source for shared clocks and triggers. |
| Slave | 15889 | Device uses clocks and triggers from the master device. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-triggerusagetypes.html language=enus -->
## TOPIC 02859: TriggerUsageTypes Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-triggerusagetypes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-triggerusagetypes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a set of trigger types a device may support. SyntaxNamespace: NationalInstruments.DAQmxpublic enum TriggerUsageTypesRemarksSpecifies a set of trigger types a device may support.MembersNameValueDescriptionNone0x0Device supports no trigger types. Advance0x1Device supports advance triggers. P

### TriggerUsageTypes Enumeration

Specifies a set of trigger types a device may support.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum TriggerUsageTypes

#### Remarks

Specifies a set of trigger types a device may support.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0x0 | Device supports no trigger types. |
| Advance | 0x1 | Device supports advance triggers. |
| Pause | 0x2 | Device supports pause triggers. |
| Reference | 0x4 | Device supports reference triggers. |
| Start | 0x8 | Device supports start triggers. |
| Handshake | 0x10 | Device supports handshake triggers. |
| ArmStart | 0x20 | Device supports arm start triggers. |

#### See Also

- AITriggerUsage
- AOTriggerUsage
- CITriggerUsage
- COTriggerUsage
- DITriggerUsage
- DOTriggerUsage

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-waitfornextsampleclockwaitmode.html language=enus -->
## TOPIC 02860: WaitForNextSampleClockWaitMode Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-waitfornextsampleclockwaitmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-waitfornextsampleclockwaitmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how WaitForNextSampleClock(double) waits for the next Sample Clock pulse. SyntaxNamespace: NationalInstruments.DAQmxpublic enum WaitForNextSampleClockWaitModeRemarksSpecifies how WaitForNextSampleClock(double) waits for the next Sample Clock pulse. Use this enumeration to get or set the va

### WaitForNextSampleClockWaitMode Enumeration

Specifies how [WaitForNextSampleClock(double)](nationalinstruments-daqmx-singlepoint-waitfornextsampleclock__double.html) waits for the next Sample Clock pulse.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum WaitForNextSampleClockWaitMode

#### Remarks

Specifies how [WaitForNextSampleClock(double)](nationalinstruments-daqmx-singlepoint-waitfornextsampleclock__double.html) waits for the next Sample Clock pulse. Use this enumeration to get or set the value of [WaitForNextSampleClockWaitMode](nationalinstruments-daqmx-singlepoint-waitfornextsampleclockwaitmode.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| WaitForInterrupt | 12523 | Check for Sample Clock pulses when the system receives an interrupt service request. This mode is the most CPU efficient, but results in lower possible sampling rates. |
| Poll | 12524 | Repeatedly check for Sample Clock pulses as fast as possible. This mode allows for the highest sampling rates at the expense of CPU efficiency. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdog-clearexpiration.html language=enus -->
## TOPIC 02861: ClearExpiration()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdog-clearexpiration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdog-clearexpiration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unlocks the device after the watchdog timer has expired. SyntaxNamespace: NationalInstruments.DAQmxpublic void ClearExpiration()ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ClearExpiration()

Unlocks the device after the [watchdog timer](/csh?context=nidaqmx_mxdevconsid_watchdogtimers) has expired.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ClearExpiration()

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Watchdog Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdog-getaoexpirationstate__string.html language=enus -->
## TOPIC 02862: GetAOExpirationState(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdog-getaoexpirationstate__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdog-getaoexpirationstate__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state to set the analog output physical channels when the watchdog task expires. SyntaxNamespace: NationalInstruments.DAQmxpublic double GetAOExpirationState(string physicalChannelName)ParametersNameTypeDescriptionphysicalChannelNamestringThe physical channel name for which to retrieve

### GetAOExpirationState(string)

Specifies the state to set the analog output physical channels when the watchdog task expires.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double GetAOExpirationState(string physicalChannelName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The physical channel name for which to retrieve the setting. |

#### Returns

Refer to summary.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Watchdog Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdog-getaoexpirationstatetype__string.html language=enus -->
## TOPIC 02863: GetAOExpirationStateType(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdog-getaoexpirationstatetype__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdog-getaoexpirationstatetype__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output type of the analog output physical channels when the watchdog task expires. SyntaxNamespace: NationalInstruments.DAQmxpublic WatchdogAOExpirationStateType GetAOExpirationStateType(string physicalChannelName)ParametersNameTypeDescriptionphysicalChannelNamestringThe physical chann

### GetAOExpirationStateType(string)

Specifies the output type of the analog output physical channels when the watchdog task expires.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [WatchdogAOExpirationStateType](nationalinstruments-daqmx-watchdogaoexpirationstatetype.html) GetAOExpirationStateType(string physicalChannelName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The physical channel name for which to retrieve the setting. |

#### Returns

Refer to summary.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Watchdog Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdog-getcoexpirationstate__string.html language=enus -->
## TOPIC 02864: GetCOExpirationState(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdog-getcoexpirationstate__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdog-getcoexpirationstate__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state to set the counter output channel terminal when the watchdog task expires. SyntaxNamespace: NationalInstruments.DAQmxpublic WatchdogCOExpirationState GetCOExpirationState(string physicalChannelName)ParametersNameTypeDescriptionphysicalChannelNamestringThe physical channel name fo

### GetCOExpirationState(string)

Specifies the state to set the counter output channel terminal when the watchdog task expires.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [WatchdogCOExpirationState](nationalinstruments-daqmx-watchdogcoexpirationstate.html) GetCOExpirationState(string physicalChannelName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The physical channel name for which to retrieve the setting. |

#### Returns

Refer to summary.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Watchdog Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdog-getdoexpirationstate__string.html language=enus -->
## TOPIC 02865: GetDOExpirationState(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdog-getdoexpirationstate__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdog-getdoexpirationstate__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state to which to set the digital physical channels when the watchdog task expires. You cannot modify the expiration state of dedicated digital input physical channels. SyntaxNamespace: NationalInstruments.DAQmxpublic WatchdogDOExpirationState GetDOExpirationState(string physicalChanne

### GetDOExpirationState(string)

Specifies the state to which to set the digital physical channels when the watchdog task expires. You cannot modify the expiration state of dedicated digital input physical channels.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [WatchdogDOExpirationState](nationalinstruments-daqmx-watchdogdoexpirationstate.html) GetDOExpirationState(string physicalChannelName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The physical channel name for which to retrieve the setting. |

#### Returns

Refer to summary.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Watchdog Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdog-hasexpired.html language=enus -->
## TOPIC 02866: HasExpired

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdog-hasexpired.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdog-hasexpired.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the watchdog timer expired. You can read this property only while the task is running. SyntaxNamespace: NationalInstruments.DAQmxpublic bool HasExpired { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### HasExpired

Indicates if the watchdog timer expired. You can read this property only while the task is running.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool HasExpired { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Watchdog Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdog-resettimer.html language=enus -->
## TOPIC 02867: ResetTimer()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdog-resettimer.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdog-resettimer.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the internal timer to 0. SyntaxNamespace: NationalInstruments.DAQmxpublic void ResetTimer()RemarksYou must continually reset the internal timer to prevent it from timing out and locking out the device. ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned

### ResetTimer()

Resets the internal timer to 0.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ResetTimer()

#### Remarks

You must continually reset the internal timer to prevent it from timing out and locking out the device.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Watchdog Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdog-setaoexpirationstate__string-double.html language=enus -->
## TOPIC 02868: SetAOExpirationState(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdog-setaoexpirationstate__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdog-setaoexpirationstate__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state to set the analog output physical channels when the watchdog task expires. SyntaxNamespace: NationalInstruments.DAQmxpublic void SetAOExpirationState(string physicalChannelName, double value)ParametersNameTypeDescriptionphysicalChannelNamestringThe physical channel name to which

### SetAOExpirationState(string, double)

Specifies the state to set the analog output physical channels when the watchdog task expires.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SetAOExpirationState(string physicalChannelName, double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The physical channel name to which to apply value . |
| value | double | The setting to apply to the given physical channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Watchdog Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdog-setaoexpirationstatetype__string-watchdogaoexpirationstatetype.html language=enus -->
## TOPIC 02869: SetAOExpirationStateType(string, WatchdogAOExpirationStateType)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdog-setaoexpirationstatetype__string-watchdogaoexpirationstatetype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdog-setaoexpirationstatetype__string-watchdogaoexpirationstatetype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output type of the analog output physical channels when the watchdog task expires. SyntaxNamespace: NationalInstruments.DAQmxpublic void SetAOExpirationStateType(string physicalChannelName, WatchdogAOExpirationStateType value)ParametersNameTypeDescriptionphysicalChannelNamestringThe ph

### SetAOExpirationStateType(string, WatchdogAOExpirationStateType)

Specifies the output type of the analog output physical channels when the watchdog task expires.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SetAOExpirationStateType(string physicalChannelName, WatchdogAOExpirationStateType value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The physical channel name to which to apply value . |
| value | WatchdogAOExpirationStateType | The setting to apply to the given physical channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Watchdog Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdog-setcoexpirationstate__string-watchdogcoexpirationstate.html language=enus -->
## TOPIC 02870: SetCOExpirationState(string, WatchdogCOExpirationState)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdog-setcoexpirationstate__string-watchdogcoexpirationstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdog-setcoexpirationstate__string-watchdogcoexpirationstate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state to set the counter output channel terminal when the watchdog task expires. SyntaxNamespace: NationalInstruments.DAQmxpublic void SetCOExpirationState(string physicalChannelName, WatchdogCOExpirationState value)ParametersNameTypeDescriptionphysicalChannelNamestringThe physical cha

### SetCOExpirationState(string, WatchdogCOExpirationState)

Specifies the state to set the counter output channel terminal when the watchdog task expires.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SetCOExpirationState(string physicalChannelName, WatchdogCOExpirationState value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The physical channel name to which to apply value . |
| value | WatchdogCOExpirationState | The setting to apply to the given physical channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Watchdog Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdog-setdoexpirationstate__string-watchdogdoexpirationstate.html language=enus -->
## TOPIC 02871: SetDOExpirationState(string, WatchdogDOExpirationState)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdog-setdoexpirationstate__string-watchdogdoexpirationstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdog-setdoexpirationstate__string-watchdogdoexpirationstate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state to which to set the digital physical channels when the watchdog task expires. You cannot modify the expiration state of dedicated digital input physical channels. SyntaxNamespace: NationalInstruments.DAQmxpublic void SetDOExpirationState(string physicalChannelName, WatchdogDOExpi

### SetDOExpirationState(string, WatchdogDOExpirationState)

Specifies the state to which to set the digital physical channels when the watchdog task expires. You cannot modify the expiration state of dedicated digital input physical channels.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SetDOExpirationState(string physicalChannelName, WatchdogDOExpirationState value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The physical channel name to which to apply value . |
| value | WatchdogDOExpirationState | The setting to apply to the given physical channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Watchdog Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdog-timeout.html language=enus -->
## TOPIC 02872: Timeout

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdog-timeout.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdog-timeout.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the amount of time until the watchdog timer expires. A value of -1 means the internal timer never expires. Set this input to -1 if you use an Expiration Trigger to expire the watchdog task. SyntaxNamespace: NationalInstruments.DAQmxpublic double Timeout { get; set; }ExceptionsTy

### Timeout

Specifies in seconds the amount of time until the watchdog timer expires. A value of -1 means the internal timer never expires. Set this input to -1 if you use an Expiration Trigger to expire the watchdog task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Timeout { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Watchdog Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdog-tostring.html language=enus -->
## TOPIC 02873: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdog-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdog-tostring.html
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

Watchdog Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdog.html language=enus -->
## TOPIC 02874: Watchdog Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdog.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdog.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties and methods for configuring and controlling a watchdog timer Task. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class Watchdog : MarshalByRefObject, IFilteredTypeDescriptorRemarksExample applications are located in the <Pub

### Watchdog Class

Contains properties and methods for configuring and controlling a [watchdog timer](/csh?context=nidaqmx_mxdevconsid_watchdogtimers) [Task](nationalinstruments-daqmx-task.html).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class Watchdog : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| HasExpired | Indicates if the watchdog timer expired. You can read this property only while the task is running. |
| Timeout | Specifies in seconds the amount of time until the watchdog timer expires. A value of -1 means the internal timer never expires. Set this input to -1 if you use an Expiration Trigger to expire the watchdog task. |

#### Methods

| Name | Description |
| --- | --- |
| ClearExpiration() | Unlocks the device after the watchdog timer has expired. |
| GetAOExpirationState(string) | Specifies the state to set the analog output physical channels when the watchdog task expires. |
| GetAOExpirationStateType(string) | Specifies the output type of the analog output physical channels when the watchdog task expires. |
| GetCOExpirationState(string) | Specifies the state to set the counter output channel terminal when the watchdog task expires. |
| GetDOExpirationState(string) | Specifies the state to which to set the digital physical channels when the watchdog task expires. You cannot modify the expiration state of dedicated digital input physical channels. |
| ResetTimer() | Resets the internal timer to 0. |
| SetAOExpirationState(string, double) | Specifies the state to set the analog output physical channels when the watchdog task expires. |
| SetAOExpirationStateType(string, WatchdogAOExpirationStateType) | Specifies the output type of the analog output physical channels when the watchdog task expires. |
| SetCOExpirationState(string, WatchdogCOExpirationState) | Specifies the state to set the counter output channel terminal when the watchdog task expires. |
| SetDOExpirationState(string, WatchdogDOExpirationState) | Specifies the state to which to set the digital physical channels when the watchdog task expires. You cannot modify the expiration state of dedicated digital input physical channels. |
| ToString() | Returns a string representation of the object. |

#### See Also

- Task
- Watchdog

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdogaoexpirationstatetype.html language=enus -->
## TOPIC 02875: WatchdogAOExpirationStateType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdogaoexpirationstatetype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdogaoexpirationstatetype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output type of the analog output physical channels when the watchdog task expires. SyntaxNamespace: NationalInstruments.DAQmxpublic enum WatchdogAOExpirationStateTypeRemarksSpecifies the output type of the analog output physical channels when the watchdog task expires. Use this enumera

### WatchdogAOExpirationStateType Enumeration

Specifies the output type of the analog output physical channels when the watchdog task expires.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum WatchdogAOExpirationStateType

#### Remarks

Specifies the output type of the analog output physical channels when the watchdog task expires. Use this enumeration to get or set the value of NationalInstruments.DAQmx.Watchdog.AOExpirationStateType.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Voltage | 10322 | Voltage output. |
| Current | 10134 | Current output. |
| NoChange | 10160 | Expiration does not affect the port. Do not change the state of any lines in the port, and do not lock the port. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdogcoexpirationstate.html language=enus -->
## TOPIC 02876: WatchdogCOExpirationState Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdogcoexpirationstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdogcoexpirationstate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state to set the counter output channel terminal when the watchdog task expires. SyntaxNamespace: NationalInstruments.DAQmxpublic enum WatchdogCOExpirationStateRemarksSpecifies the state to set the counter output channel terminal when the watchdog task expires. Use this enumeration to

### WatchdogCOExpirationState Enumeration

Specifies the state to set the counter output channel terminal when the watchdog task expires.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum WatchdogCOExpirationState

#### Remarks

Specifies the state to set the counter output channel terminal when the watchdog task expires. Use this enumeration to get or set the value of NationalInstruments.DAQmx.Watchdog.COExpirationState.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Low | 10214 | Low logic. |
| High | 10192 | High logic. |
| NoChange | 10160 | Expiration does not affect the state of the counter output. The channels retain their states at the time of the watchdog timer expiration, and no further counter generation runs. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdogdoexpirationstate.html language=enus -->
## TOPIC 02877: WatchdogDOExpirationState Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdogdoexpirationstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdogdoexpirationstate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state to which to set the digital physical channels when the watchdog task expires. You cannot modify the expiration state of dedicated digital input physical channels. SyntaxNamespace: NationalInstruments.DAQmxpublic enum WatchdogDOExpirationStateRemarksSpecifies the state to which to

### WatchdogDOExpirationState Enumeration

Specifies the state to which to set the digital physical channels when the watchdog task expires. You cannot modify the expiration state of dedicated digital input physical channels.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum WatchdogDOExpirationState

#### Remarks

Specifies the state to which to set the digital physical channels when the watchdog task expires. You cannot modify the expiration state of dedicated digital input physical channels. Use this enumeration to get or set the value of NationalInstruments.DAQmx.Watchdog.DOExpirationState.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| High | 10192 | Logic high. |
| Low | 10214 | Logic low. |
| Tristate | 10310 | High-impedance state. You can select this state only on devices with bidirectional lines. You cannot select this state for dedicated digital output lines. On some devices, you can select this value only for entire ports. |
| NoChange | 10160 | Do not change the state of the lines. On some devices, you can select this value only for entire ports. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdogexpirationtrigger-configuredigitaledgetrigger__string-digitaledgewatchdogexpirationtriggeredge.html language=enus -->
## TOPIC 02878: ConfigureDigitalEdgeTrigger(string, DigitalEdgeWatchdogExpirationTriggerEdge)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdogexpirationtrigger-configuredigitaledgetrigger__string-digitaledgewatchdogexpirationtriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdogexpirationtrigger-configuredigitaledgetrigger__string-digitaledgewatchdogexpirationtriggeredge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the watchdog timer to expire upon a rising or falling edge of a digital signal. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureDigitalEdgeTrigger(string source, DigitalEdgeWatchdogExpirationTriggerEdge edge)RemarksThe NI-DAQmx driver does not determine if the requested set

### ConfigureDigitalEdgeTrigger(string, DigitalEdgeWatchdogExpirationTriggerEdge)

Configures the [watchdog timer](/csh?context=nidaqmx_mxdevconsid_watchdogtimers) to expire upon a [rising or falling edge of a digital signal](/csh?context=nidaqmx_mxcncpts_digtrigger).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureDigitalEdgeTrigger(string source, DigitalEdgeWatchdogExpirationTriggerEdge edge)

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureDigitalEdgeTrigger(string, DigitalEdgeWatchdogExpirationTriggerEdge) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The terminal of the trigger signal. |
| edge | DigitalEdgeWatchdogExpirationTriggerEdge | The edge of the trigger signal that causes a watchdog expiration trigger to occur. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

WatchdogExpirationTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdogexpirationtrigger-configurenone.html language=enus -->
## TOPIC 02879: ConfigureNone()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdogexpirationtrigger-configurenone.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdogexpirationtrigger-configurenone.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables watchdog expiration triggering for the task. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureNone()RemarksThe NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureNone does not throw an exception for parameter values t

### ConfigureNone()

Disables [watchdog expiration triggering](/csh?context=nidaqmx_mxcncpts_expirationtrigger) for the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureNone()

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureNone does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

WatchdogExpirationTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdogexpirationtrigger-digitaledge.html language=enus -->
## TOPIC 02880: DigitalEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdogexpirationtrigger-digitaledge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdogexpirationtrigger-digitaledge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalEdgeWatchdogExpirationTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalEdgeWatchdogExpirationTrigger DigitalEdge { get; }RemarksThe DigitalEdgeWatchdogExpirationTrigger.

### DigitalEdge

Gets the [DigitalEdgeWatchdogExpirationTrigger](nationalinstruments-daqmx-digitaledgewatchdogexpirationtrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DigitalEdgeWatchdogExpirationTrigger](nationalinstruments-daqmx-digitaledgewatchdogexpirationtrigger.html) DigitalEdge { get; }

#### Remarks

The [DigitalEdgeWatchdogExpirationTrigger](nationalinstruments-daqmx-digitaledgewatchdogexpirationtrigger.html).

Parent topic:

WatchdogExpirationTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdogexpirationtrigger-tostring.html language=enus -->
## TOPIC 02881: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdogexpirationtrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdogexpirationtrigger-tostring.html
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

WatchdogExpirationTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdogexpirationtrigger-triggeronnetworkconnectionlost.html language=enus -->
## TOPIC 02882: TriggerOnNetworkConnectionLost

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdogexpirationtrigger-triggeronnetworkconnectionlost.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdogexpirationtrigger-triggeronnetworkconnectionlost.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the watchdog timer behavior when the network connection is lost between the host and the chassis. If set to true, the watchdog timer expires when the chassis detects the loss of network connection. SyntaxNamespace: NationalInstruments.DAQmxpublic bool TriggerOnNetworkConnectionLost { get;

### TriggerOnNetworkConnectionLost

Specifies the watchdog timer behavior when the network connection is lost between the host and the chassis. If set to true, the watchdog timer expires when the chassis detects the loss of network connection.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool TriggerOnNetworkConnectionLost { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

WatchdogExpirationTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdogexpirationtrigger-type.html language=enus -->
## TOPIC 02883: Type

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdogexpirationtrigger-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdogexpirationtrigger-type.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of trigger to use to expire a watchdog task. SyntaxNamespace: NationalInstruments.DAQmxpublic WatchdogExpirationTriggerType Type { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Type

Specifies the type of trigger to use to expire a watchdog task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [WatchdogExpirationTriggerType](nationalinstruments-daqmx-watchdogexpirationtriggertype.html) Type { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

WatchdogExpirationTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdogexpirationtrigger.html language=enus -->
## TOPIC 02884: WatchdogExpirationTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdogexpirationtrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdogexpirationtrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties and methods that configure a trigger to cause the watchdog to expire in a watchdog timer task. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class WatchdogExpirationTrigger : MarshalByRefObject, IFilteredTypeDescriptorRemark

### WatchdogExpirationTrigger Class

Contains properties and methods that configure a trigger to cause the [watchdog to expire](/csh?context=nidaqmx_mxcncpts_expirationtrigger) in a [watchdog timer](/csh?context=nidaqmx_mxdevconsid_watchdogtimers) task.

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class WatchdogExpirationTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DigitalEdge | Gets the DigitalEdgeWatchdogExpirationTrigger. |
| TriggerOnNetworkConnectionLost | Specifies the watchdog timer behavior when the network connection is lost between the host and the chassis. If set to true, the watchdog timer expires when the chassis detects the loss of network connection. |
| Type | Specifies the type of trigger to use to expire a watchdog task. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureDigitalEdgeTrigger(string, DigitalEdgeWatchdogExpirationTriggerEdge) | Configures the watchdog timer to expire upon a rising or falling edge of a digital signal. |
| ConfigureNone() | Disables watchdog expiration triggering for the task. |
| ToString() | Returns a string representation of the object. |

#### See Also

- Triggers
- WatchdogExpirationTrigger

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-watchdogexpirationtriggertype.html language=enus -->
## TOPIC 02885: WatchdogExpirationTriggerType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-watchdogexpirationtriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-watchdogexpirationtriggertype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of trigger to use to expire a watchdog task. SyntaxNamespace: NationalInstruments.DAQmxpublic enum WatchdogExpirationTriggerTypeRemarksSpecifies the type of trigger to use to expire a watchdog task. Use this enumeration to get or set the value of Type.MembersNameValueDescriptionDi

### WatchdogExpirationTriggerType Enumeration

Specifies the type of trigger to use to expire a watchdog task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum WatchdogExpirationTriggerType

#### Remarks

Specifies the type of trigger to use to expire a watchdog task. Use this enumeration to get or set the value of [Type](nationalinstruments-daqmx-watchdogexpirationtrigger-type.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| DigitalEdge | 10150 | Trigger on a rising or falling edge of a digital signal. |
| Time | 15996 | Trigger when a specified time is reached. |
| None | 10230 | Disable the trigger. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-waveformattributemodes.html language=enus -->
## TOPIC 02886: WaveformAttributeModes Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-waveformattributemodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-waveformattributemodes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of information returned from waveform reads. SyntaxNamespace: NationalInstruments.DAQmxpublic enum WaveformAttributeModesRemarksThe value of this property may affect performance when performing waveform reads.MembersNameValueDescriptionNone0x0Returns only the waveform data itself,

### WaveformAttributeModes Enumeration

Specifies the type of information returned from waveform reads.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum WaveformAttributeModes

#### Remarks

The value of this property may affect performance when performing waveform reads.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0x0 | Returns only the waveform data itself, with no timing information or extended properties. Use this value for optimal performance. |
| Timing | 0x1 | Returns timing information in addition to the waveform data. This value may degrade performance when performing waveform reads. |
| ExtendedProperties | 0x2 | Returns extended properties in addition to the waveform data. This value may degrade performance when performing waveform reads. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-writerecoverymode.html language=enus -->
## TOPIC 02887: WriteRecoveryMode Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-writerecoverymode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-writerecoverymode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes. SyntaxNamespace: NationalInstruments.DAQmxpublic enum WriteRecoveryModeRemarksSpecifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes. Us

### WriteRecoveryMode Enumeration

Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum WriteRecoveryMode

#### Remarks

Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes. Use this enumeration to get or set the value of [WriteRecoveryMode](nationalinstruments-daqmx-singlepoint-writerecoverymode.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| WaitForInterrupt | 12523 | Attempt to recover when the system receives an interrupt service request. This mode is the most CPU efficient and best suited for recovery at lower pulse train frequencies. |
| Poll | 12524 | Repeatedly attempt to recover as fast as possible. This mode has the highest probability of recovery success at the expense of CPU efficiency. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-writeregenerationmode.html language=enus -->
## TOPIC 02888: WriteRegenerationMode Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-writeregenerationmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-writeregenerationmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to allow NI-DAQmx to generate the same data multiple times. SyntaxNamespace: NationalInstruments.DAQmxpublic enum WriteRegenerationModeRemarksSpecifies whether to allow NI-DAQmx to generate the same data multiple times. Use this enumeration to get or set the value of WriteRegenerat

### WriteRegenerationMode Enumeration

Specifies whether to allow NI-DAQmx to generate the same data multiple times.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum WriteRegenerationMode

#### Remarks

Specifies whether to allow NI-DAQmx to generate the same data multiple times. Use this enumeration to get or set the value of [WriteRegenerationMode](nationalinstruments-daqmx-daqstream-writeregenerationmode.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AllowRegeneration | 10097 | Allow NI-DAQmx to regenerate samples that the device previously generated. When you choose this value, the write marker returns to the beginning of the buffer after the device generates all samples currently in the buffer. |
| DoNotAllowRegeneration | 10158 | Do not allow NI-DAQmx to regenerate samples the device previously generated. When you choose this value, NI-DAQmx waits for you to write more samples to the buffer or until the timeout expires. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-writerelativeto.html language=enus -->
## TOPIC 02889: WriteRelativeTo Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-writerelativeto.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-writerelativeto.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the point in the buffer at which to write data. If you also specify an offset with WriteOffset, the write operation begins at that offset relative to this point you select with this property. SyntaxNamespace: NationalInstruments.DAQmxpublic enum WriteRelativeToRemarksSpecifies the point in

### WriteRelativeTo Enumeration

Specifies the point in the buffer at which to write data. If you also specify an offset with [WriteOffset](nationalinstruments-daqmx-daqstream-writeoffset.html), the write operation begins at that offset relative to this point you select with this property.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum WriteRelativeTo

#### Remarks

Specifies the point in the buffer at which to write data. If you also specify an offset with [WriteOffset](nationalinstruments-daqmx-daqstream-writeoffset.html), the write operation begins at that offset relative to this point you select with this property. Use this enumeration to get or set the value of [WriteRelativeTo](nationalinstruments-daqmx-daqstream-writerelativeto.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FirstSample | 10424 | Write samples relative to the first sample. |
| CurrentWritePosition | 10430 | Write samples relative to the current position in the buffer. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-writewaitmode.html language=enus -->
## TOPIC 02890: WriteWaitMode Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-writewaitmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-writewaitmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how writing to the task waits for space to become available in the buffer. SyntaxNamespace: NationalInstruments.DAQmxpublic enum WriteWaitModeRemarksSpecifies how writing to the task waits for space to become available in the buffer. Use this enumeration to get or set the value of WriteWai

### WriteWaitMode Enumeration

Specifies how writing to the task waits for space to become available in the buffer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum WriteWaitMode

#### Remarks

Specifies how writing to the task waits for space to become available in the buffer. Use this enumeration to get or set the value of [WriteWaitMode](nationalinstruments-daqmx-daqstream-writewaitmode.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Poll | 12524 | Repeatedly check for available buffer space as fast as possible. This mode allows for the highest sampling rates at the expense of CPU efficiency. |
| Yield | 12525 | Repeatedly check for available buffer space, but yield control to other threads after each check. This mode offers a balance between sampling rate and CPU efficiency. |
| Sleep | 12547 | Check for available buffer space once per the amount of time specified in WriteSleepTime. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx.html language=enus -->
## TOPIC 02891: NationalInstruments.DAQmx

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionAIChannelEncapsulates one or more analog input virtual channels and the properties for an analog input virtual channel. AIChannelCollectionContains the collection of analog input channels for a Task. AOChannelEncapsulates one or more analog output channels and the properties fo

### NationalInstruments.DAQmx

#### Classes

| Name | Description |
| --- | --- |
| AIChannel | Encapsulates one or more analog input virtual channels and the properties for an analog input virtual channel. |
| AIChannelCollection | Contains the collection of analog input channels for a Task. |
| AOChannel | Encapsulates one or more analog output channels and the properties for an analog output channel. |
| AOChannelCollection | Contains the collection of analog output channels for a Task. |
| AdvanceTrigger | Contains properties and methods that configure how the switch task advances to the next entry in the scan list and causes the switch to advance programmatically. |
| AnalogEdgeReferenceTrigger | Contains properties to configure analog edge reference triggers. |
| AnalogEdgeStartTrigger | Contains properties to configure analog edge start triggers. For more information, refer to StartTrigger. |
| AnalogLevelPauseTrigger | Contains properties to configure analog level pause triggers. For more information, refer to PauseTrigger. |
| AnalogMultiChannelReader | Contains methods for reading samples from one or more analog input channels in a task. |
| AnalogMultiChannelWriter | Contains methods for writing samples to one or more analog output channels in a task. |
| AnalogMultiEdgeReferenceTrigger | Provides properties for configuring analog multi-edge reference triggers. |
| AnalogMultiEdgeStartTrigger | Provides properties for configuring analog multi-edge start triggers. |
| AnalogSingleChannelReader | Contains methods for reading samples from the analog input channel in a task. |
| AnalogSingleChannelWriter | Contains methods for writing samples to the analog output channel in a task. |
| AnalogUnscaledReader | Contains methods that read unscaled samples from a task. |
| AnalogUnscaledWriter | Contains methods that write unscaled samples to a task. |
| AnalogWindowPauseTrigger | Contains properties to configure analog window pause triggers. For more information, refer to PauseTrigger. |
| AnalogWindowReferenceTrigger | Contains properties to configure analog window reference triggers. For more information, refer to ReferenceTrigger. |
| AnalogWindowStartTrigger | Contains properties to configure analog window start triggers. For more information, refer to StartTrigger. |
| ArmStartTrigger | Contains properties and methods that configure a trigger that arms the task for a start trigger. For more information, refer to StartTrigger. |
| CIChannel | Encapsulates one counter/timer input channel and the properties for a counter/timer input channel. |
| CIChannelCollection | Contains the collection of counter/timer input channels for a Task. |
| COChannel | Encapsulates one or more counter/timer output channels and the properties for a counter/timer output channel. |
| COChannelCollection | Contains the collection of counter/timer output channels for a Task. |
| Channel | Represents a channel or a set of channels and the properties you can set on a channel. |
| CounterMultiChannelReader | Contains methods for reading samples from one or more counter input channels in a task. |
| CounterMultiChannelWriter | Contains methods for writing samples to one or more counter output channels in a counter output task. |
| CounterOutputEventArgs | Provides data for the CounterOutput event. |
| CounterSingleChannelReader | Contains methods for reading samples from the counter input channel in a task. |
| CounterSingleChannelWriter | Contains methods for writing samples to a single counter output channel in a counter output task. |
| DIChannel | Encapsulates one or more digital input channels and the properties for a digital input channel. |
| DIChannelCollection | Contains the collection of digital input channels for a Task. |
| DOChannel | Encapsulates one or more digital output channels and the properties for a digital output channel. |
| DOChannelCollection | Contains the collection of digital output channels for a Task. |
| DaqBuffer | Exposes a buffer on a Task that can be used to read or write samples to or from an NI-DAQmx task. |
| DaqException | Represents the exception that is thrown when an NI-DAQmx driver error occurs. |
| DaqStream | Exposes a data stream on a Task that can be used to control reading and writing behavior and can be used in conjunction with reader and writer classes to read or write samples to or from an NI-DAQmx task. |
| DaqSystem | Contains methods that access tasks, scales, and global channels stored in Measurement & Automation Explorer (MAX), performs immediate operations on DAQ hardware, and creates classes from which you can get information about the hardware. |
| DaqWarningEventArgs | Provides data for the DaqWarning event. |
| Device | Encapsulates a DAQ device and contains methods and properties that operate on devices outside the context of a task. |
| DigitalChangeDetectionEventArgs | Provides data for the DigitalChangeDetection event. |
| DigitalEdgeAdvanceTrigger | Contains properties to configure digital edge advance triggers. For more information, refer to AdvanceTrigger. |
| DigitalEdgeArmStartTrigger | Contains properties to configure digital edge arm start triggers. For more information, refer to ArmStartTrigger. |
| DigitalEdgeReferenceTrigger | Contains properties to configure digital edge reference triggers. For more information, refer to ReferenceTrigger. |
| DigitalEdgeStartTrigger | Contains properties to configure digital edge start triggers. For more information, refer to StartTrigger. |
| DigitalEdgeWatchdogExpirationTrigger | Contains properties to configure digital edge watchdog expiration triggers. For more information, refer to WatchdogExpirationTrigger. |
| DigitalLevelPauseTrigger | Contains properties to configure digital level pause triggers. For more information, refer to PauseTrigger. |
| DigitalMultiChannelReader | Contains methods for reading samples from one or more digital input or output channels in a task. |
| DigitalMultiChannelWriter | Contains methods for writing samples to one or more digital output channels in a task. |
| DigitalPatternPauseTrigger | Contains properties that let a task pause the acquisition or generation when the device matches a digital pattern. |
| DigitalPatternReferenceTrigger | Contains properties that let a task stop the acquisition when the device acquires all pretrigger samples, matches a digital pattern, and acquires all posttrigger samples. |
| DigitalPatternStartTrigger | Contains properties that let a task start acquiring or generating samples when a digital pattern is matched. |
| DigitalSingleChannelReader | Contains methods for reading samples from the digital input or output channel in a task. |
| DigitalSingleChannelWriter | Contains methods for writing samples to the digital output channel in a task. |
| EveryNSamplesReadEventArgs | Provides data for the EveryNSamplesRead event. |
| EveryNSamplesWrittenEventArgs | Provides data for the EveryNSamplesWritten event. |
| ExportSignals | Encapsulates the signals that are available for routing off of the DAQ device, the properties that define which terminal the signals are routed to, and the programmable characteristics of the signals for a Task. |
| ExternalCalibrationSession | Represents a handle to an external calibration session on a device. |
| HandshakeTrigger | Contains properties and methods that configure handshake trigger signals on a task. |
| InterlockedHandshakeTrigger | Contains properties to configure interlocked handshake triggers. For more information, refer to HandshakeTrigger. |
| LinearScale | Encapsulates a linear custom scale that scales values using the equation y = mx + b. |
| PauseTrigger | Contains properties and methods that configure signals and triggers that pause a task. |
| PhysicalChannel | Encapsulates one or more channels on an NI-DAQmx device and contains functions and properties that operate on the channel outside the context of a task. |
| PolynomialScale | Encapsulates a custom scale that scales values by using an nth-order polynomial equation. |
| RangeMapScale | Encapsulates a custom scale that scales values proportionally from a range of prescaled values to a range of scaled values. |
| ReferenceTrigger | Contains properties and methods that configure the trigger that creates the reference point between the pretrigger samples and the post-trigger samples. |
| SampleClockEventArgs | Provides data for the SampleClock event. |
| SampleCompleteEventArgs | Provides data for the SampleComplete event. |
| SavedChannelInfo | Encapsulates information about a global channel stored in Measurement & Automation Explorer (MAX). You can retrieve an instance of this class by calling GetSavedChannelInfo(string). |
| SavedScaleInfo | Encapsulates information about a custom scale stored in Measurement & Automation Explorer (MAX). You can retrieve an instance of this class by calling GetSavedScaleInfo(string). |
| SavedTaskInfo | Encapsulates information about a task stored in Measurement & Automation Explorer (MAX). You can retrieve an instance of this class by calling GetSavedTaskInfo(string). |
| Scale | Encapsulates a custom scale that translates between prescaled quantities in device units and quantities scaled to the units of interest. |
| SinglePoint | Contains properties and methods that configure how to align to the sample clock of the Task. |
| StartTrigger | Contains properties and methods that configure how the task begins measurement or generation. |
| Switch | Obsolete: This type is obsolete. Will warn if usedEncapsulates a switch device and contains properties and methods that operate on switch devices outside the context of a task. |
| SwitchChannel | Obsolete: This type is obsolete. Will warn if usedEncapsulates a channel on a switch device and contains properties and methods that operate on switch channels outside the context of a task. This class also defines the intended use of particular switch channels in tasks. |
| SwitchScan | Obsolete: This type is obsolete. Will warn if usedContains properties for a switch scan list. |
| TableScale | Encapsulates a custom scale that maps an array of prescaled values to an array of corresponding scaled values, with all other values scaled proportionally. |
| Task | Represents a collection of virtual channels and their per-channel properties and timing, triggering, and other properties that apply to the DAQmx Task. |
| TaskDoneEventArgs | Provides data for the Done event. |
| TimeArmStartTrigger | Provides properties for configuring time arm start triggers. |
| TimeStartTrigger | Provides properties for configuring time start triggers. |
| Timing | Contains properties and methods that configure the sample timing and duration of the Task. |
| Triggers | Contains members that configure all of the triggers that can affect a Task. |
| Watchdog | Contains properties and methods for configuring and controlling a watchdog timer Task. |
| WatchdogExpirationTrigger | Contains properties and methods that configure a trigger to cause the watchdog to expire in a watchdog timer task. |

#### Interfaces

| Name | Description |
| --- | --- |
| IFilteredTypeDescriptor | Defines the interface that is implemented by all Task subobjects that can perform property filtering by programmatically returning an ICustomTypeDescriptor that contains the list of filtered properties for the subobject. |

#### Structures

| Name | Description |
| --- | --- |
| AIPowerMeasurement | Encapsulates a power measurement specified in terms of voltage and current. |
| AIUnscaledPowerMeasurement | Encapsulates a power measurement specified in terms of voltage and current. |
| CIDataFrequency | Encapsulates a counter input specified in terms of frequency and duty cycle. |
| CIDataTicks | Encapsulates a counter input specified in terms of timebase ticks. |
| CIDataTime | Encapsulates a counter input specified in terms of time. |
| CODataFrequency | Encapsulates a counter output specified in terms of frequency and duty cycle. |
| CODataTicks | Encapsulates a counter output specified in terms of timebase ticks. |
| CODataTime | Encapsulates a counter output specified in terms of time. |

#### Enumerations

| Name | Description |
| --- | --- |
| AIACExcitationWireMode | Specifies the number of leads on the LVDT or RVDT. Some sensors require you to tie leads together to create a four- or five- wire sensor. Refer to the sensor documentation for more information. |
| AIAccelerationChargeSensitivityUnits | Specifies the units of AI.Accel.Charge.Sensitivity. |
| AIAccelerationFourWireDCVoltageSensitivityUnits | Specifies the units of AI.Accel.4WireDCVoltage.Sensitivity. |
| AIAccelerationUnits | Specifies the units to use to return acceleration measurements from the channel. |
| AIAccelerometerSensitivityUnits | Specifies the units of AccelerometerSensitivity. |
| AIAdcTimingMode | Specifies the ADC timing mode, controlling the tradeoff between speed and effective resolution. Some ADC timing modes provide increased powerline noise rejection. On devices that have an AI Convert clock, this setting affects both the maximum and default values for AIConvertRate. You must use the same ADC timing mode for all channels on a device, but you can use different ADC timing modes for different devices in the same task. |
| AIAutoZeroMode | Specifies how often to measure ground. NI-DAQmx subtracts the measured ground voltage from every sample. |
| AIBridgeConfiguration | Specifies the type of Wheatstone bridge connected to the channel. |
| AIBridgeConfiguration11637 | Specifies the type of Wheatstone bridge connected to the channel. |
| AIBridgeElectricalUnits | Specifies from which electrical unit to scale data. Select the same unit that the sensor data sheet or calibration certificate uses for electrical values. |
| AIBridgePhysicalUnits | Specifies to which physical unit to scale electrical data. Select the same unit that the sensor data sheet or calibration certificate uses for physical values. |
| AIBridgeScaleType | Specifies the scaling type to use when scaling electrical values from the sensor to physical units. |
| AIBridgeShuntCalibrationSelect | Specifies which shunt calibration switch(es) to enable. Use BridgeShuntCalibrationEnable to enable the switch(es) you specify with this property. |
| AIBridgeUnits | Specifies in which unit to return voltage ratios from the channel. |
| AIChannelCalibrationScaleType | Specifies the method or equation form that the calibration scale uses. |
| AIChargeUnits | Specifies the units to use to return charge measurements from the channel. |
| AIConvertActiveEdge | Specifies on which edge of the clock pulse an analog-to-digital conversion takes place. |
| AIConvertClockPulsePolarity | Indicates the polarity of the exported AI Convert Clock. The polarity is fixed and independent of the active edge of the source of the AI Convert Clock. |
| AIConvertTimebaseSource | Specifies the terminal of the signal to use as the AI Convert Clock Timebase. |
| AICoupling | Specifies the coupling for the channel. |
| AICurrentAcrmsUnits | Specifies the units to use to return current RMS measurements from the channel. |
| AICurrentShuntLocation | Specifies the shunt resistor location for current measurements. |
| AICurrentUnits | Specifies the units to use to return current measurements from the channel. |
| AIDataTransferMechanism | Specifies the data transfer mode for the device. |
| AIDataTransferRequestCondition | Specifies under what condition to transfer data from the onboard memory of the device to the buffer. |
| AIDigitalFilterType | Indicates the AI digital filter types supported by the device. |
| AIEddyCurrentProximityProbeSensitivityUnits | Specifies the units of EddyCurrentProximityProbeSensitivity. |
| AIEddyCurrentProximityProbeUnits | Specifies the units to use to return proximity measurements from the channel. |
| AIExcitationDCOrAC | Specifies if the excitation supply is DC or AC. |
| AIExcitationSense | Specifies whether to use local or remote sense to sense excitation. |
| AIExcitationSource | Specifies the source of excitation. |
| AIExcitationVoltageOrCurrent | Specifies if the channel uses current or voltage excitation. |
| AIFilterDelayUnits | Specifies the units of FilterDelay and FilterDelayAdjustment. |
| AIFilterResponse | Specifies the corresponding filter response and defines the shape of the filter response. |
| AIForceIepeSensorSensitivityUnits | Specifies the units for ForceIepeSensorSensitivity. |
| AIForceUnits | Specifies in which unit to return force or load measurements from the channel. |
| AIFrequencyUnits | Specifies the units to use to return frequency measurements from the channel. |
| AIHoldCompleteEventPulsePolarity | Specifies the polarity of an exported AI Hold Complete Event pulse. |
| AILowpassSwitchedCapacitorClockSource | Specifies the source of the filter clock. If you need a higher resolution for the filter, you can supply an external clock to increase the resolution. Refer to the SCXI-1141/1142/1143 User Manual for more information. |
| AILvdtSensitivityUnits | Specifies the units of LvdtSensitivity. |
| AILvdtUnits | Specifies the units to use to return linear position measurements from the channel. |
| AIMeasurementType | Indicates the measurement to take with the analog input channel and in some cases, such as for temperature measurements, the sensor to use. |
| AIPowerUnits | Specifies the units to use to return power measurements from the channel. |
| AIPressureUnits | Specifies in which unit to return pressure measurements from the channel. |
| AIRawDataCompressionType | Specifies the type of compression to apply to raw samples returned from the device. |
| AIRawSampleJustification | Indicates the justification of a raw sample from the device. |
| AIResistanceConfiguration | Specifies the resistance configuration for the channel. NI-DAQmx uses this value for any resistance-based measurements, including temperature measurement using a thermistor or RTD. |
| AIResistanceUnits | Specifies the units to use to return resistance measurements. |
| AIResolutionUnits | Indicates the units of Resolution. |
| AIRosetteMeasurementType | Specifies the type of rosette measurement. |
| AIRosetteType | Indicates the type of rosette gage. |
| AIRtdType | Specifies the type of RTD connected to the channel. |
| AIRvdtSensitivityUnits | Specifies the units of RvdtSensitivity. |
| AIRvdtUnits | Specifies the units to use to return angular position measurements from the channel. |
| AISensorPowerConfiguration | Specifies whether to turn on the sensor's power supply or to leave the configuration unchanged. |
| AISensorPowerType | Specifies the type of power supplied to the sensor. |
| AISoundPressureUnits | Specifies the units to use to return sound pressure measurements from the channel. |
| AIStrainGageConfiguration | Specifies the bridge configuration of the strain gages. |
| AIStrainUnits | Specifies the units to use to return strain measurements from the channel. |
| AITemperatureUnits | Specifies the units to use to return temperature measurements from the channel. |
| AITerminalConfiguration | Specifies the terminal configuration for the channel. |
| AIThermocoupleCjcSource | Indicates the source of cold-junction compensation. |
| AIThermocoupleScaleType | Specifies the method or equation form that the thermocouple scale uses. |
| AIThermocoupleType | Specifies the type of thermocouple connected to the channel. Thermocouple types differ in composition and measurement range. |
| AITorqueUnits | Specifies in which unit to return torque measurements from the channel. |
| AIVelocityIepeSensorSensitivityUnits | Specifies the units for VelocityIepeSensorSensitivity. |
| AIVelocityUnits | Specifies in which unit to return velocity measurements from the channel. |
| AIVoltageAcrmsUnits | Specifies the units to use to return voltage RMS measurements from the channel. |
| AIVoltageUnits | Specifies the units to use to return voltage measurements from the channel. |
| AOCurrentUnits | Specifies in what units to generate current on the channel. Write data to the channel in the units you select. |
| AODacOffsetSource | Specifies the source of the DAC offset voltage. The value of this voltage source determines the full-scale value of the DAC. |
| AODacReferenceSource | Specifies the source of the DAC reference voltage. The value of this voltage source determines the full-scale value of the DAC. |
| AODataTransferMechanism | Specifies the data transfer mode for the device. |
| AODataTransferRequestCondition | Specifies under what condition to transfer data from the buffer to the onboard memory of the device. |
| AOFilterDelayUnits | Specifies the units of FilterDelay and FilterDelayAdjustment. |
| AOFunctionGenerationModulationType | Specifies if the device generates a modulated version of the waveform using the original waveform as a carrier and input from an external terminal as the signal. |
| AOFunctionGenerationType | Specifies the kind of the waveform to generate. |
| AOIdleOutputBehavior | Specifies the state of the channel when no generation is in progress. |
| AOOutputType | Indicates whether the channel generates voltage, current, or a waveform. |
| AOPowerUpOutputBehavior | Specifies the analog output state of the physical channels for some devices when your computer is powered on or the device is reset in NI-DAQmx. |
| AOResolutionUnits | Specifies the units of Resolution. |
| AOTerminalConfiguration | Specifies the terminal configuration of the channel. |
| AOVoltageUnits | Specifies in what units to generate voltage on the channel. Write data to the channel in the units you select. |
| AdvanceCompleteEventPulsePolarity | Specifies the polarity of the exported Advance Complete Event. |
| AdvanceTriggerPulsePolarity | Indicates the polarity of the exported Advance Trigger. |
| AdvanceTriggerPulseWidthUnits | Specifies the units of AdvanceTriggerPulseWidth. |
| AdvanceTriggerType | Obsolete: This enum is obsolete. Will warn if used(Deprecated) Specifies the type of trigger to use to advance to the next entry in a switch scan list. |
| AnalogEdgePauseTriggerCoupling | Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. |
| AnalogEdgeReferenceTriggerCoupling | Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. |
| AnalogEdgeReferenceTriggerSlope | Specifies on which slope of the source signal the Reference Trigger occurs. |
| AnalogEdgeStartTriggerCoupling | Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. |
| AnalogEdgeStartTriggerSlope | Specifies on which slope of the trigger signal to start acquiring or generating samples. |
| AnalogLevelPauseTriggerCondition | Specifies whether the task pauses above or below the threshold you specify with Level. |
| AnalogMultiEdgeReferenceTriggerCoupling | Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
| AnalogMultiEdgeReferenceTriggerSlope | Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Ref.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
| AnalogMultiEdgeStartTriggerCoupling | Specifies an array that describes the couplings for the corresponding source signal of the trigger if the source is a terminal rather than a virtual channel. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
| AnalogMultiEdgeStartTriggerSlope | Specifies an array of slopes on which to trigger task to start generating or acquiring samples. Each element of the array corresponds to a source in Start.AnlgMultiEdge.Srcs and an element in each of the other Analog Multi Edge property arrays, if they are not empty. |
| AnalogWindowPauseTriggerCondition | Specifies whether the task pauses while the trigger signal is inside or outside the window you specify with WindowBottom and WindowTop. |
| AnalogWindowPauseTriggerCoupling | Specifies the coupling for the source signal of the terminal if the source is a terminal rather than a virtual channel. |
| AnalogWindowReferenceTriggerCondition | Specifies whether the Reference Trigger occurs when the source signal enters the window or when it leaves the window. Use WindowBottom and WindowTop to specify the window. |
| AnalogWindowReferenceTriggerCoupling | Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. |
| AnalogWindowStartTriggerCondition | Specifies whether the task starts acquiring or generating samples when the signal enters or leaves the window you specify with WindowBottom and WindowTop. |
| AnalogWindowStartTriggerCoupling | Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel. |
| ArmStartTriggerTimestampTimescale | Specifies the arm start trigger timestamp timescale. |
| ArmStartTriggerType | Specifies the type of trigger to use to arm the task for a Start Trigger. If you configure an Arm Start Trigger, the task does not respond to a Start Trigger until the device receives the Arm Start Trigger. |
| BasicTedsDataOption | Specifies how to handle basic TEDS data in a TEDS bitstream. |
| BridgeShuntCalibrationSource | Specifies whether to use internal or external shunt when Shunt Cal A is selected. |
| CIAngularEncoderUnits | Specifies the units to use to return angular position measurements from the channel. |
| CICountEdgesActiveEdge | Specifies on which edges to increment or decrement the counter. |
| CICountEdgesCountDirection | Specifies whether to increment or decrement the counter on each edge. |
| CICountEdgesCountDirectionLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
| CICountEdgesCountDirectionTerminalConfiguration | Specifies the input terminal configuration. |
| CICountEdgesCountResetActiveEdge | Specifies on which edge of the signal to reset the count. |
| CICountEdgesCountResetLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
| CICountEdgesCountResetTerminalConfiguration | Specifies the input terminal configuration. |
| CICountEdgesGateLogicLevelBehavior | Specifies the logic level behavior on the gate input line. |
| CICountEdgesGatePauseState | Specifies whether the counter gates input pulses while the signal is high or low. |
| CICountEdgesGateTerminalConfiguration | Specifies the gate terminal configuration. |
| CICountEdgesLogicLevelBehavior | Specifies the logic level behavior on the input line. |
| CICountEdgesTerminalConfiguration | Specifies the input terminal configuration. |
| CICounterTimebaseActiveEdge | Specifies whether a timebase cycle is from rising edge to rising edge or from falling edge to falling edge. |
| CIDataTransferMechanism | Specifies the data transfer mode for the channel. |
| CIDataTransferRequestCondition | Specifies under what condition to transfer data from the onboard memory of the device to the buffer. |
| CIDutyCycleLogicLevelBehavior | Specifies the logic level behavior on the input line. |
| CIDutyCycleStartingEdge | Specifies which edge of the input signal to begin the duty cycle measurement. |
| CIDutyCycleTerminalConfiguration | Specifies the input terminal configuration. |
| CIEncoderAInputLogicLevelBehavior | Specifies the logic level behavior on the input line. |
| CIEncoderAInputTerminalConfiguration | Specifies the input terminal configuration. |
| CIEncoderBInputLogicLevelBehavior | Specifies the logic level behavior on the input line. |
| CIEncoderBInputTerminalConfiguration | Specifies the input terminal configuration. |
| CIEncoderDecodingType | Specifies how to count and interpret the pulses the encoder generates on signal A and signal B. X1, X2, and X4 are valid for quadrature encoders only. TwoPulseCounting is valid for two-pulse encoders only. |
| CIEncoderZIndexPhase | Specifies the states at which signal A and signal B must be while signal Z is high for NI-DAQmx to reset the measurement. If signal Z is never high while signal A and signal B are high, for example, you must choose a phase other than AHighBHigh. |
| CIEncoderZInputLogicLevelBehavior | Specifies the logic level behavior on the input line. |
| CIEncoderZInputTerminalConfiguration | Specifies the input terminal configuration. |
| CIFilterDelayUnits | Specifies the units of FilterDelay. |
| CIFilterResponse | Specifies the corresponding filter response and defines the shape of the filter response. |
| CIFrequencyLogicLevelBehavior | Specifies the logic level behavior on the input line. |
| CIFrequencyMeasurementMethod | Specifies the method to use to measure the frequency of the signal. |
| CIFrequencyStartingEdge | Specifies between which edges to measure the frequency of the signal. |
| CIFrequencyTerminalConfiguration | Specifies the input terminal configuration. |
| CIFrequencyUnits | Specifies the units to use to return frequency measurements. |
| CIGpsSyncMethod | Specifies the method to use to synchronize the counter to a GPS receiver. |
| CILinearEncoderUnits | Specifies the units to use to return linear encoder measurements from the channel. |
| CIMeasurementType | Indicates the measurement to take with the channel. |
| CIOutputState | Indicates the current state of the out terminal of the counter. |
| CIPeriodLogicLevelBehavior | Specifies the logic level behavior on the input line. |
| CIPeriodMeasurementMethod | Specifies the method to use to measure the period of the signal. |
| CIPeriodStartingEdge | Specifies between which edges to measure the period of the signal. |
| CIPeriodTerminalConfiguration | Specifies the input terminal configuration. |
| CIPeriodUnits | Specifies the unit to use to return period measurements. |
| CIPulseFrequencyLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
| CIPulseFrequencyStartingEdge | Specifies on which edge of the input signal to begin pulse measurement. |
| CIPulseFrequencyTerminalConfiguration | Specifies the input terminal configuration. |
| CIPulseFrequencyUnits | Specifies the units to use to return pulse specifications in terms of frequency. |
| CIPulseTicksLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
| CIPulseTicksStartingEdge | Specifies on which edge of the input signal to begin pulse measurement. |
| CIPulseTicksTerminalConfiguration | Specifies the input terminal configuration. |
| CIPulseTimeLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
| CIPulseTimeStartingEdge | Specifies on which edge of the input signal to begin pulse measurement. |
| CIPulseTimeTerminalConfiguration | Specifies the input terminal configuration. |
| CIPulseTimeUnits | Specifies the units to use to return pulse specifications in terms of high time and low time. |
| CIPulseWidthLogicLevelBehavior | Specifies the logic level behavior on the input line. |
| CIPulseWidthStartingEdge | Specifies on which edge of the input signal to begin each pulse width measurement. |
| CIPulseWidthTerminalConfiguration | Specifies the input terminal configuration. |
| CIPulseWidthUnits | Specifies the units to use to return pulse width measurements. |
| CISampleClockOverrunBehavior | Specifies the counter behavior when data is read but a new value was not detected during a sample clock. |
| CISemiPeriodLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
| CISemiPeriodStartingEdge | Specifies on which edge of the input signal to begin semi-period measurement. Semi-period measurements alternate between high time and low time, starting on this edge. |
| CISemiPeriodTerminalConfiguration | Specifies the input terminal configuration. |
| CISemiPeriodUnits | Specifies the units to use to return semi-period measurements. |
| CITimestampUnits | Specifies the units to use to return timestamp measurements. |
| CITwoEdgeSeparationFirstEdge | Specifies on which edge of the first signal to start each measurement. |
| CITwoEdgeSeparationFirstLogicLevelBehavior | Specifies the logic level behavior on the input line. |
| CITwoEdgeSeparationFirstTerminalConfiguration | Specifies the input terminal configuration. |
| CITwoEdgeSeparationSecondEdge | Specifies on which edge of the second signal to stop each measurement. |
| CITwoEdgeSeparationSecondLogicLevelBehavior | Specifies the logic level behavior on the count reset line. |
| CITwoEdgeSeparationSecondTerminalConfiguration | Specifies the input terminal configuration. |
| CITwoEdgeSeparationUnits | Specifies the units to use to return two-edge separation measurements from the channel. |
| CIVelocityAInputLogicLevelBehavior | Specifies the logic level behavior of the input terminal. |
| CIVelocityAInputTerminalConfiguration | Specifies the input terminal configuration. |
| CIVelocityAngularEncoderUnits | Specifies the units to use to return angular velocity counter measurements. |
| CIVelocityBInputLogicLevelBehavior | Specifies the logic level behavior of the input terminal. |
| CIVelocityBInputTerminalConfiguration | Specifies the input terminal configuration. |
| CIVelocityEncoderType | Specifies how to count and interpret the pulses the encoder generates on signal A and signal B. X1, X2, and X4 are valid for quadrature encoders only. Two Pulse Counting is valid for two-pulse encoders only. |
| CIVelocityLinearEncoderUnits | Specifies the units to use to return linear encoder velocity measurements from the channel. |
| COConstrainedGenerationMode | Specifies constraints to apply when the counter generates pulses. Constraining the counter reduces the device resources required for counter operation. Constraining the counter can also allow additional analog or counter tasks on the device to run concurrently. For continuous counter tasks, NI-DAQmx consumes no device resources when the counter is constrained. For finite counter tasks, resource use increases with the frequency regardless of the constraint mode. However, fixed frequency constraints significantly reduce resource usage, and fixed duty cycle constraint marginally reduces it. |
| COCounterTimebaseActiveEdge | Specifies whether a timebase cycle is from rising edge to rising edge or from falling edge to falling edge. |
| CODataTransferMechanism | Specifies the data transfer mode for the device. For buffered operations, use DMA or USB Bulk. For non-buffered operations, use Polled. |
| CODataTransferRequestCondition | Specifies under what condition to transfer data from the buffer to the onboard memory of the device. |
| COOutputState | Indicates the current state of the output terminal of the counter. |
| COOutputType | Indicates how to define pulses generated on the channel. |
| COPulseFrequencyUnits | Specifies the units in which to define pulse frequency. |
| COPulseIdleState | Specifies the resting state of the output terminal. |
| COPulseTimeUnits | Specifies the units in which to define high and low pulse time. |
| CalibrationCoupling9775 | Represents the coupling of the calibration constants to be adjusted on the C Series NI 9775. |
| CalibrationInputTerminalConfiguration4463 | Specifies the input terminal configuration for the channel to calibrate on an NI PXIe 4463 device. |
| CalibrationInputTerminalConfiguration9209 | Specifies the input terminal configuration for the channel to calibrate on an NI 9209 device. |
| CalibrationMode4339 | Specifies which measurements to use to calibrate an NI 4339 device. |
| CalibrationMode4480 | Specifies which measurements to use to calibrate an NI 4480 device. |
| ChangeDetectionEventPulsePolarity | Specifies the polarity of an exported Change Detection Event pulse. |
| ChannelLineGrouping | Specifies how to group digital lines into one or more virtual channels. |
| ChannelSynchronizationUnlockBehavior | Specifies the action to take if the target loses its synchronization to the grand master. |
| ChannelType | Indicates the type of the virtual channel. |
| CounterOutputEventIdleState | Specifies the initial state of the output terminal of the counter when CounterOutputEventOutputBehavior is Toggle. The terminal enters this state when NI-DAQmx commits the task. |
| CounterOutputEventOutputBehavior | Specifies whether the exported Counter Output Event pulses or changes from one state to the other when the counter reaches terminal count. |
| CounterOutputEventPulsePolarity | Specifies the polarity of the pulses at the output terminal of the counter when CounterOutputEventOutputBehavior is Pulse. NI-DAQmx ignores this property if CounterOutputEventOutputBehavior is Toggle. |
| CouplingTypes | Specifies a set of coupling types a device may support. |
| DIAcquireOn | Specifies on which edge of the sample clock to acquire samples. |
| DIDataTransferMechanism | Specifies the data transfer mode for the device. |
| DIDataTransferRequestCondition | Specifies under what condition to transfer data from the onboard memory of the device to the buffer. |
| DILogicFamily | Specifies the logic family to use for acquisition. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families. |
| DODataTransferMechanism | Specifies the data transfer mode for the device. |
| DODataTransferRequestCondition | Specifies under what condition to transfer data from the buffer to the onboard memory of the device. |
| DOGenerateOn | Specifies on which edge of the sample clock to generate samples. |
| DOLineStatesDoneState | Specifies the state of the lines in a digital output task when the task completes execution. |
| DOLineStatesPausedState | Specifies the state of the lines in a digital output task when the task pauses. |
| DOLineStatesStartState | Specifies the state of the lines in a digital output task when the task starts. |
| DOLogicFamily | Specifies the logic family to use for generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families. |
| DOOutputDriveType | Specifies the drive type for digital output channels. |
| DataActiveEventLevelActiveLevel | Specifies the polarity of the exported Data Active Event. |
| DelayFromSampleClockUnits | Specifies the units of DelayFromSampleClock. |
| DeviceBusType | Indicates the bus type of the device. |
| DigPortLogicFamily | Specifies the digital port logic family to use for acquisition and generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families. |
| DigitalEdgeAdvanceTriggerEdge | Obsolete: This enum is obsolete. Will warn if used(Deprecated) Specifies on which edge of a digital signal to advance to the next entry in a scan list. |
| DigitalEdgeArmStartTriggerEdge | Specifies on which edge of a digital signal to arm the task for a Start Trigger. |
| DigitalEdgeReferenceTriggerEdge | Specifies on what edge of a digital pulse the Reference Trigger occurs. |
| DigitalEdgeStartTriggerEdge | Specifies on which edge of a digital pulse to start acquiring or generating samples. |
| DigitalEdgeWatchdogExpirationTriggerEdge | Specifies on which edge of a digital signal to expire the watchdog task. |
| DigitalLevelPauseTriggerCondition | Specifies whether the task pauses while the signal is high or low. |
| DigitalPatternPauseTriggerCondition | Specifies if the Pause Trigger occurs when the physical channels specified with Source match or differ from the digital pattern specified with Pattern. |
| DigitalPatternReferenceTriggerCondition | Specifies whether the Reference Trigger occurs when the physical channels specified with Source match or differ from the digital pattern specified with Pattern. |
| DigitalPatternStartTriggerCondition | Specifies whether the Start Trigger occurs when the physical channels specified with Source match or differ from the digital pattern specified with Pattern. |
| DigitalPowerUpState | Specifies the power up state to set for the physical channel. |
| DigitalPullUpPullDownResistorState | Specifies the pull up pull down level for each physical channel. |
| ExcitationIdleOutputBehavior | Specifies whether this channel will disable excitation after the task is uncommitted. Setting this to Zero Volts or Amps disables excitation after task uncommit. Setting this attribute to Maintain Existing Value leaves the excitation on after task uncommit. |
| ExportSignal | Specifies the name of the trigger, clock, or event to export. |
| FilterResponse | Specifies the digital filter response. |
| FilterType | Specifies the digital filter type. |
| FirstSampleClockTimescale | Specifies the timescale to be used for the value of FirstSampleClockTime. |
| FirstSampleTimestampTimescale | Specifies the timescale to be used for the first sample timestamp. |
| HandshakeEventInterlockedAssertedLevel | Specifies the asserted level of the exported Handshake Event if HandshakeEventOutputBehavior is Interlocked. |
| HandshakeEventOutputBehavior | Specifies the output behavior of the Handshake Event. |
| HandshakeEventPulsePolarity | Specifies the polarity of the exported Handshake Event if HandshakeEventOutputBehavior is Pulse. |
| HandshakeSampleInputDataCondition | Specifies on which edge of the Handshake Trigger an input task latches the data from the peripheral device. |
| HandshakeStartCondition | Specifies the point in the handshake cycle that the device is in when the task starts. |
| HandshakeTriggerType | Specifies the type of Handshake Trigger to use. |
| IDPinStatus | Indicates status of each ID Pin. |
| ImplicitUnderflowBehavior | Specifies the action to take when the onboard memory of the device becomes empty. |
| InputCalibrationSource | Specifies the input source selection. |
| InterlockedHandshakeTriggerAssertedLevel | Specifies the asserted level of the Handshake Trigger. |
| LoggingMode | Specifies whether to enable logging and whether to allow reading data while logging. Log mode allows for the best performance. However, you cannot read data while logging if you specify this mode. If you want to read data while logging, specify Log and Read mode. |
| LogicFamily | Specifies the logic family to use for generation and acquisition. |
| PauseTriggerLevelActiveLevel | Specifies the active level of the exported Pause Trigger. |
| PauseTriggerType | Specifies the type of trigger to use to pause a task. |
| PhysicalChannelAIPowerControlType | Specifies the type of power supplied to the sensor. |
| PhysicalChannelAISensorPowerType | Indicates the types of power supplied to the sensor supported by this channel. |
| PhysicalChannelAccess | Specifies the physical channel access types to include when requesting a list of physical channels. |
| PhysicalChannelTypes | Specifies the types of physical channels to include when requesting a list of physical channels. |
| PolynomialDirection | Specifies the direction of the conversion the provided polynomial coefficients perform. |
| PowerCalibrationType | Specifies the calibration type. |
| PowerIdleOutputBehavior | Specifies whether to disable the output or maintain the existing value after the task is uncommitted. |
| PowerOutputState | Indicates power channel operating state. Can be read at any time during a task. |
| ProductCategory | Indicates the product category of the device. This category corresponds to the category displayed in MAX when creating NI-DAQmx simulated devices. |
| PropertyFilterFlags | Specifies a set of property filtering options. |
| PropertyFilterType | Specifies the type of property filtering to perform. |
| ReadOverwriteMode | Specifies whether to overwrite samples in the buffer that you have not yet read. |
| ReadRelativeTo | Specifies the point in the buffer at which to begin a read operation. If you also specify an offset with ReadOffset, the read operation begins at that offset relative to the point you select with this property. The default value is CurrentReadPosition unless you configure a Reference Trigger for the task. If you configure a Reference Trigger, the default value is FirstPretriggerSample. |
| ReadWaitMode | Specifies how reading from the task waits for samples to become available. |
| ReadyForStartEventLevelActiveLevel | Specifies the polarity of the exported Ready for Start Event. |
| ReadyForTransferEventDeassertCondition | Specifies when the ready for transfer event deasserts. |
| ReadyForTransferEventLevelActiveLevel | Specifies the active level of the exported Ready for Transfer Event. |
| ReallocationPolicy | Specifies the behavior of a memory-optimized read method operation when the operation yields more samples than the current capacity of the buffer can allocate. |
| ReferenceTriggerPulsePolarity | Specifies the polarity of the exported Reference Trigger. |
| ReferenceTriggerTimestampTimescale | Specifies the reference trigger timestamp timescale. |
| ReferenceTriggerType | Specifies the type of trigger to use to mark a reference point for the measurement. |
| SampleClockActiveEdge | Specifies on which edge of a clock pulse sampling takes place. This property is useful primarily when the signal you use as the Sample Clock is not a periodic clock. |
| SampleClockOutputBehavior | Specifies whether the exported Sample Clock issues a pulse at the beginning of a sample or changes to a high state for the duration of the sample. |
| SampleClockOverrunBehavior | Specifies the action to take if Sample Clock edges occur faster than the device can handle them. |
| SampleClockPulsePolarity | Specifies the polarity of the exported Sample Clock if SampleClockOutputBehavior is Pulse. |
| SampleClockTimebaseActiveEdge | Specifies on which edge to recognize a Sample Clock Timebase pulse. This property is useful primarily when the signal you use as the Sample Clock Timebase is not a periodic clock. |
| SampleClockTimingResponseMode | Specifies how the device responds to the sample clock and to triggers. |
| SampleClockUnderflowBehavior | Specifies the action to take when the onboard memory of the device becomes empty. In either case, the sample clock does not stop. |
| SampleQuantityMode | Specifies if a task acquires or generates a finite number of samples or if it continuously acquires or generates samples. |
| SampleTimingType | Specifies the type of sample timing to use for the task. |
| SaveOptions | Specifies various options used to save a task, a local or global channel , or a custom scale to Measurement & Automation Explorer (MAX). |
| ScalePreScaledUnits | Specifies the units of the values that you want to scale. |
| ScaleType | Specifies the type of custom scale. |
| Scxi1124Range | Specifies the range for the SCXI 1124 calibration values. |
| Sense | Specifies whether to use local or remote sense to sense the output voltage. DAQmx Read (Power Supply) will return remote or local voltage based on the Remote Sense attribute value. Reading this property will return the user-defined value. |
| ShuntCalibrationSelect | Specifies the shunt calibration switch(es) to enable. |
| ShuntElementLocation | Specifies which resistor to use to calibrate the channel(s). |
| ShuntResistorSource | Specifies whether to use internal or external shunt. |
| SignalRoutingModifiers | Specifies if the signal routed from the source terminal to the destination terminal is inverted. |
| StartTriggerDelayUnits | Specifies the units of Delay. |
| StartTriggerPulsePolarity | Specifies the polarity of the exported Start Trigger. |
| StartTriggerTimestampTimescale | Specifies the start trigger timestamp timescale. |
| StartTriggerType | Specifies the type of trigger to use to start a task. |
| SwitchChannelUsage | Obsolete: This enum is obsolete. Will warn if used Specifies how you can use the channel. Using this property acts as a safety mechanism to prevent you from connecting two source channels, for example. |
| SwitchPathStatus | Obsolete: This enum is obsolete. Will warn if usedSpecifies the status of the requested path. |
| SwitchRelayPosition | Obsolete: This enum is obsolete. Will warn if usedSpecifies the position of each specified relay. |
| SwitchScanBreakMode | Obsolete: This enum is obsolete. Will warn if used Specifies the action to take between each entry in a scan list. |
| SwitchScanRepeatMode | Obsolete: This enum is obsolete. Will warn if used Specifies if the task advances through the scan list multiple times. |
| SynchronizationPulseTimescale | Specifies the timescale to be used for timestamps for a sync pulse. |
| SynchronizationPulseType | Specifies the type of sync pulse used in the task. |
| TaskAction | Specifies how to alter the state of the task. |
| TdmsLoggingOperation | Specifies how to open the TDMS file. |
| TerminalConfigurationTypes | Specifies a set of terminal configuration types a physical channel may support. |
| TerminalTypes | Specifies the types of terminals to include when requesting a list of terminals. |
| TimeArmStartTriggerTimescale | Specifies the timescale to be used for timestamps used in an arm start time trigger. |
| TimeStartTriggerTimescale | Specifies the timescale to be used for timestamps used in a time trigger. |
| TimestampEvent | Represents the type of timestamp event. |
| TriggerSynchronizationType | Specifies the role of the device in a synchronized system. Setting this value to Master or Slave enables trigger skew correction. If you enable trigger skew correction, set this property to Master on only one device, and set this property to Slave on the other devices. |
| TriggerUsageTypes | Specifies a set of trigger types a device may support. |
| WaitForNextSampleClockWaitMode | Specifies how WaitForNextSampleClock(double) waits for the next Sample Clock pulse. |
| WatchdogAOExpirationStateType | Specifies the output type of the analog output physical channels when the watchdog task expires. |
| WatchdogCOExpirationState | Specifies the state to set the counter output channel terminal when the watchdog task expires. |
| WatchdogDOExpirationState | Specifies the state to which to set the digital physical channels when the watchdog task expires. You cannot modify the expiration state of dedicated digital input physical channels. |
| WatchdogExpirationTriggerType | Specifies the type of trigger to use to expire a watchdog task. |
| WaveformAttributeModes | Specifies the type of information returned from waveform reads. |
| WriteRecoveryMode | Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes. |
| WriteRegenerationMode | Specifies whether to allow NI-DAQmx to generate the same data multiple times. |
| WriteRelativeTo | Specifies the point in the buffer at which to write data. If you also specify an offset with WriteOffset, the write operation begins at that offset relative to this point you select with this property. |
| WriteWaitMode | Specifies how writing to the task waits for space to become available in the buffer. |

#### Delegates

| Name | Description |
| --- | --- |
| CounterOutputEventHandler | Represents the method that handles the CounterOutput event. |
| DaqWarningEventHandler | Represents the method that handles the DaqWarning event. |
| DigitalChangeDetectionEventHandler | Represents the method that handles the DigitalChangeDetection event. |
| EveryNSamplesReadEventHandler | Represents the method that handles the EveryNSamplesRead event. |
| EveryNSamplesWrittenEventHandler | Represents the method that handles the EveryNSamplesWritten event. |
| SampleClockEventHandler | Represents the method that handles the SampleClock event. |
| SampleCompleteEventHandler | Represents the method that handles the SampleComplete event. |
| TaskDoneEventHandler | Represents the method that handles the Done event. |
